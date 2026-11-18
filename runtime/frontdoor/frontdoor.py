"""OpenJarvis route addon. Existing application auth/middleware remain in place."""
import asyncio,json,pathlib,re,subprocess,time,uuid
from fastapi import HTTPException,Request
from starlette.responses import StreamingResponse,JSONResponse

HERE=pathlib.Path(__file__).resolve().parent
CONFIG=HERE/'frontdoor.json'
SECRET=re.compile(r'(?i)(?:\bsk-[A-Za-z0-9_-]{16,}|\bgh[pousr]_[A-Za-z0-9]{20,}|(?:api[_-]?key|password|access[_-]?token|bearer)\s*[:=]\s*[^\s]{8,})')
CODING=re.compile(r'(?i)\b(opencode|code|coding|implement|program|python|function|script|unit tests?|src/|(?:build|create).{0,35}(?:app|tool|calculator|website|web page|test))\b')

def messages_for(body):
    rows=[]
    for message in body.messages[-12:]:
        m=message.model_dump() if hasattr(message,'model_dump') else dict(message)
        if m.get('role') not in ('user','assistant'):continue
        content=m.get('content')
        if not isinstance(content,str):raise HTTPException(400,'Bridge accepts text messages only.')
        if SECRET.search(content):raise HTTPException(400,'Remove credentials before sending this request.')
        rows.append({'role':m['role'],'content':content})
    if not rows or rows[-1]['role']!='user':raise HTTPException(400,'A user message is required.')
    if sum(len(m['content']) for m in rows)>18000:raise HTTPException(400,'Conversation is too long for this bounded bridge. Start a new chat.')
    return rows

def receipt_text(result):
    code=result.get('code')
    if not code:return result['message']
    v=code.get('verification',{})
    return ('OpenCode task '+code['status']+'.\n\nProject: '+code.get('project','')+
      '\nFiles changed: '+((', '.join(code['changed_files']) or 'none') if 'changed_files' in code else 'not recorded')+
      '\nTests: '+str(v.get('tests_run','not recorded'))+'; failures: '+str(v.get('failures','unknown'))+
      '; errors: '+str(v.get('errors','unknown'))+'; exit: '+str(v.get('exit_code','unknown'))+
      '\nLocal provider evidence: '+str(code.get('native',{}).get('available',False))+
      '\n\n'+code.get('opencode_report',code.get('reason','')))

def unfinished_job(jobs):
    # Survives backend loss: never submit a duplicate while an earlier worker
    # is active or its shutdown is unknown. Operators inspect before recovery.
    paths=[p for p in jobs.glob('*.json') if re.fullmatch('[a-f0-9]{32}',p.stem)]
    if len(paths)>1000:raise RuntimeError('job_record_limit_review_required')
    return any(json.loads(p.read_text()).get('state') in ('pending','running') for p in paths)

def install(app):
    from openjarvis.server.routes import ChatCompletionRequest
    route=next(r for r in app.routes if getattr(r,'path',None)=='/v1/chat/completions')
    original=route.dependant.call
    lock=asyncio.Lock()

    async def bridge(request_body:ChatCompletionRequest,request:Request):
        latest=request_body.messages[-1].content if request_body.messages else ''
        if request_body.tools or (isinstance(latest,str) and latest.startswith('/local ')):
            if isinstance(latest,str) and latest.startswith('/local '):request_body.messages[-1].content=latest[7:]
            return await original(request_body,request)
        rows=messages_for(request_body)
        if lock.locked():raise HTTPException(409,'Another bridge task is running. Stop it or wait for its result.')
        await lock.acquire()
        try:
            cfg=json.loads(CONFIG.read_text());jobs=pathlib.Path(cfg['shared'])/'jobs';jobs.mkdir(exist_ok=True)
            if (jobs/'unsettled.json').exists():raise RuntimeError('previous_shutdown_unconfirmed')
            if unfinished_job(jobs):raise RuntimeError('previous_bridge_job_unfinished')
            jid=uuid.uuid4().hex
            job={'state':'pending','deadline':time.time()+660,'messages':rows,'code_allowed':bool(CODING.search(rows[-1]['content']))}
            (jobs/(jid+'.json')).write_text(json.dumps(job),encoding='utf-8')
            command="& 'C:\\Python314\\python.exe' '"+str(pathlib.Path(cfg['shared'])/'gateway_job.py').replace("'","''")+"' "+jid
            process=subprocess.Popen([cfg['clawctl'],'pwsh','--command',command],stdin=subprocess.DEVNULL,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
        except Exception as exc:
            lock.release()
            details={'previous_shutdown_unconfirmed':'The previous bridge shutdown is unconfirmed. Verify that run before retrying.',
                     'previous_bridge_job_unfinished':'An earlier bridge request is unfinished. It was preserved; no duplicate was started.',
                     'job_record_limit_review_required':'The local job archive requires operator review before more requests.'}
            raise HTTPException(503,details.get(str(exc),'Cannot start the supported OpenClaw session.'))
        async def finish():
            while process.poll() is None:await asyncio.sleep(.3)
            lock.release()
        async def stream():
            def event(value):return 'data: '+json.dumps(value)+'\n\n'
            yield event({'choices':[{'delta':{'role':'assistant','content':'OpenClaw is coordinating this request…\n\n'},'index':0}]})
            code_announced=False
            try:
                while process.poll() is None:
                    if await request.is_disconnected():
                        (jobs/(jid+'.cancel')).touch();return
                    yield ': bridge heartbeat\n\n'
                    if not code_announced and (jobs/(jid+'.code-started.json')).exists():
                        yield event({'choices':[{'delta':{'content':'OpenCode is editing and testing in its guarded project…\n\n'},'index':0}]})
                        code_announced=True
                    await asyncio.sleep(2)
                path=jobs/(jid+'.result.json')
                result=json.loads(path.read_text()) if path.exists() else {'message':'OpenClaw bridge exited without a result. No retry was made.'}
                answer=SECRET.sub('[REDACTED]',receipt_text(result))
                yield event({'choices':[{'delta':{'content':answer},'index':0,'finish_reason':None}]})
                yield event({'choices':[{'delta':{},'index':0,'finish_reason':'stop'}]})
                yield 'data: [DONE]\n\n'
            finally:
                if process.poll() is None:(jobs/(jid+'.cancel')).touch()
                asyncio.create_task(finish())
        if request_body.stream:return StreamingResponse(stream(),media_type='text/event-stream')
        try:
            while process.poll() is None:
                if await request.is_disconnected():(jobs/(jid+'.cancel')).touch();raise HTTPException(499,'Cancelled')
                await asyncio.sleep(1)
            result=json.loads((jobs/(jid+'.result.json')).read_text())
            return JSONResponse({'id':jid,'object':'chat.completion','model':'ollama/qwen3.8:27b','choices':[{'index':0,'message':{'role':'assistant','content':SECRET.sub('[REDACTED]',receipt_text(result))},'finish_reason':'stop'}]})
        finally:asyncio.create_task(finish())
    route.dependant.call=bridge
    app.state.frontdoor_enabled=True
    return app
