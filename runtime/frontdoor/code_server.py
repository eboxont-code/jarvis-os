"""One guarded MCP coding tool. No arbitrary command, cwd, file or provider input."""
import hashlib,json,os,pathlib,re,subprocess,sys,threading,time,uuid
from projects import HERE,COMMAND,ensure_project,snapshot,verify
from acp_client import Client,ACPError

JOBS=HERE/'jobs';ACTIVE={};OUTPUT=threading.Lock()
SECRET=re.compile(r'(?i)(?:\bsk-[A-Za-z0-9_-]{16,}|\bgh[pousr]_[A-Za-z0-9]{20,}|(?:api[_-]?key|password|access[_-]?token|bearer)\s*[:=]\s*[^\s]{8,})')

def emit(doc):
    with OUTPUT:print(json.dumps(doc,separators=(',',':')),flush=True)

def approved_job(job_id):
    if not re.fullmatch('[a-f0-9]{32}',job_id):raise ValueError('invalid_job')
    path=JOBS/(job_id+'.json')
    job=json.loads(path.read_text())
    if job.get('state')!='running' or job.get('deadline',0)<time.time():raise ValueError('inactive_job')
    if job.get('code_allowed') is not True:raise ValueError('explicit_coding_request_required')
    return job

def native_evidence(executable,session,root):
    if not re.fullmatch('ses_[A-Za-z0-9_-]+',session):return {'available':False}
    p=subprocess.run([executable,'session','export',session],cwd=root,capture_output=True,text=True,encoding='utf-8',timeout=25)
    if p.returncode:return {'available':False}
    d=json.loads(p.stdout);models=[];tools=[]
    def walk(v):
        if isinstance(v,dict):
            if v.get('type')=='assistant' and isinstance(v.get('model'),dict):models.append({k:x for k,x in v['model'].items() if k in ('id','providerID')})
            if v.get('type')=='tool' or isinstance(v.get('tool'),str):
                state=v.get('state',{});meta=state.get('metadata',{})
                supplied=state.get('input',v.get('input',{}))
                tools.append({'tool':v.get('tool',v.get('name')),'status':state.get('status'),'exit_code':meta.get('exitCode',meta.get('exit')),
                    'permitted_verifier':isinstance(supplied,dict) and supplied.get('command')==COMMAND,
                    'permission_denied':'permission' in str(state.get('error','')).lower() or 'denied' in str(state.get('error','')).lower()})
            for child in v.values():walk(child)
        elif isinstance(v,list):
            for child in v:walk(child)
    walk(d)
    if any(m.get('providerID') not in (None,'ollama') for m in models):raise ValueError('nonlocal_provider')
    return {'available':True,'models':models,'tools':tools}

def code_task(args,cancel_event):
    if set(args)!={'job_id','project','task'} or not all(isinstance(x,str) for x in args.values()):raise ValueError('arguments_not_allowed')
    if not args['task'].strip() or len(args['task'])>6000 or SECRET.search(args['task']):raise ValueError('unsafe_or_oversized_task')
    job=approved_job(args['job_id']);root=ensure_project(args['project'])
    import msvcrt
    coding_lock=(HERE/'coding.lock').open('a+b')
    coding_lock.seek(0);coding_lock.write(b'0');coding_lock.flush();coding_lock.seek(0)
    try:msvcrt.locking(coding_lock.fileno(),msvcrt.LK_NBLCK,1)
    except OSError:
        coding_lock.close();raise ValueError('another_coding_task_is_running')
    claim=JOBS/(args['job_id']+'.code-claim')
    try:fd=os.open(claim,os.O_CREAT|os.O_EXCL|os.O_WRONLY);os.close(fd)
    except Exception:
        coding_lock.close();raise
    (JOBS/(args['job_id']+'.code-started.json')).write_text(json.dumps({'project':args['project'],'stage':'OpenCode editing and testing'}))
    before=snapshot(root)
    c=json.loads((pathlib.Path.home()/'.openclaw/openclaw.json').read_text(encoding='utf-8-sig'))
    executable=c['plugins']['entries']['acpx']['config']['agents']['opencode']['command']
    cancelled=lambda:cancel_event.is_set() or (JOBS/(args['job_id']+'.cancel')).exists() or time.time()>job['deadline']
    client=Client(executable,root,cancelled);start=time.monotonic()
    try:
        init=client.initialize(root)
        # An outer worker verifies native persisted tools/tests without a
        # re-entrant export/process launch from an active ACP callback.
        (JOBS/(args['job_id']+'.code-session.json')).write_text(json.dumps({'project':args['project'],'session':client.session}))
        client.completed=lambda:(JOBS/(args['job_id']+'.finish-code')).exists()
        prompt=('Use only existing local ollama/qwen3.8:27b. Work in this exact project only. '
          'Read AGENTS.md and source/tests before editing. Edit only permitted src/, tests/, README.md; '
          'respect protected tests if policy denies their edit. No delegation, installs, network, credentials or outside paths. '
          'Run exactly '+COMMAND+'; no wrappers or alternate commands. Do not call unittest.main in source/tests. '
          'Tests may directly import from src.module import function; avoid module.attribute calls. '
          'Verifier rejects filesystem/network/import permissions it cannot safely execute; report that honestly. '
          'At most three test runs and one repair after a failing test. After success return immediately with files and actual counts. '
          'Task: '+args['task'])
        response=client.prompt(prompt,min(300,max(1,job['deadline']-time.time())))
        if response.get('stopReason') not in ('end_turn','max_tokens','bridge_verified'):raise ACPError('coding_incomplete')
        client.close()
        after=snapshot(root)
        answer=''.join(client.output)[-6000:]
        if response.get('stopReason')=='bridge_verified':answer='OpenCode completed the permitted verifier. The adapter stopped the completed coding turn before further narration or commands.'
        answer=SECRET.sub('[REDACTED]',answer)
        receipt={'status':'candidate','project':args['project'],
          'project_path':str(root),'changed_files':sorted(p for p in set(before)|set(after) if before.get(p)!=after.get(p)),
          'native_session_id':client.session,'opencode_report':answer,'permission_requests_denied':client.denials,
          'elapsed_seconds':round(time.monotonic()-start,1),'completion_reason':response.get('stopReason'),'transport':'OpenClaw MCP tool -> installed OpenCode ACP'}
    except Exception as exc:
        client.cancel();client.close()
        receipt={'status':'cancelled' if cancelled() else 'failed','project':args['project'],
              'error_type':type(exc).__name__,'reason':str(exc) if re.fullmatch('[a-z0-9_]+',str(exc)) else 'coding_failed'}
        if not cancelled():
            try:
                after=snapshot(root);receipt['changed_files']=sorted(p for p in set(before)|set(after) if before.get(p)!=after.get(p))
                receipt['native_session_id']=client.session
                receipt['status']='partial' if receipt['changed_files'] else 'failed'
            except Exception:receipt['evidence_incomplete']=True
    finally:
        client.close();coding_lock.close()
    receipt['owned_acp_process_exited']=client.process.poll() is not None
    receipt['adapter_revision']=3
    (JOBS/(args['job_id']+'.code-result.json')).write_text(json.dumps(receipt,indent=2))
    return receipt

TOOL={'name':'code_task','description':'Delegate one coding task to installed local OpenCode ACP in a bridge-owned project. Requires the active bridge job_id supplied by the coordinator request. Returns actual files and independent test evidence. No other directories, commands, network or delegation.','inputSchema':{'type':'object','properties':{'job_id':{'type':'string'},'project':{'type':'string','description':'Lowercase project name, e.g. bridge-smoke. Only owned projects are accessible.'},'task':{'type':'string'}},'required':['job_id','project','task'],'additionalProperties':False}}

def respond_call(doc,event):
    try:
        params=doc.get('params',{})
        if params.get('name')!='code_task':raise ValueError('tool_not_allowed')
        result=code_task(params.get('arguments',{}),event)
        value={'content':[{'type':'text','text':json.dumps(result)}],'isError':False}
    except Exception as exc:
        value={'content':[{'type':'text','text':json.dumps({'status':'refused','reason':str(exc) if re.fullmatch('[a-z0-9_]+',str(exc)) else type(exc).__name__})}],'isError':True}
    emit({'jsonrpc':'2.0','id':doc['id'],'result':value});ACTIVE.pop(doc['id'],None)

def main():
    for raw in sys.stdin.buffer:
        if len(raw)>100_000:continue
        try:doc=json.loads(raw)
        except ValueError:continue
        method=doc.get('method');request_id=doc.get('id')
        if method=='initialize':emit({'jsonrpc':'2.0','id':request_id,'result':{'protocolVersion':'2024-11-05','capabilities':{'tools':{}},'serverInfo':{'name':'jarvis-code','version':'3'}}})
        elif method=='tools/list':emit({'jsonrpc':'2.0','id':request_id,'result':{'tools':[TOOL]}})
        elif method=='tools/call':
            event=threading.Event();ACTIVE[request_id]=event
            threading.Thread(target=respond_call,args=(doc,event),daemon=True).start()
        elif method=='notifications/cancelled':
            event=ACTIVE.get(doc.get('params',{}).get('requestId'))
            if event:event.set()
        elif request_id is not None:emit({'jsonrpc':'2.0','id':request_id,'error':{'code':-32601,'message':'Method not allowed'}})
    for event in list(ACTIVE.values()):event.set()
    deadline=time.monotonic()+12
    while ACTIVE and time.monotonic()<deadline:time.sleep(.1)

if __name__=='__main__':
    if len(sys.argv)==3 and sys.argv[1]=='--job':
        jid=sys.argv[2]
        try:
            job=approved_job(jid)
            receipt=code_task({'job_id':jid,'project':job['project'],'task':job['messages'][-1]['content']},threading.Event())
            receipt['transport']='OpenClaw native delegate -> installed OpenCode ACP'
            (JOBS/(jid+'.code-result.json')).write_text(json.dumps(receipt,indent=2))
            print(json.dumps(receipt),flush=True)
        except Exception as exc:
            print(json.dumps({'status':'refused','error_type':type(exc).__name__,'owned_acp_process_exited':True}),flush=True)
    else:main()
