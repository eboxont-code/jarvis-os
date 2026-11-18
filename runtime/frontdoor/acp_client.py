"""Bounded client for the already-installed OpenCode ACP server. No downloads."""
import json,queue,subprocess,threading,time,uuid

FLAGS=getattr(subprocess,'CREATE_NO_WINDOW',0)

class ACPError(RuntimeError):pass

class Client:
    def __init__(self,executable,cwd,cancel=lambda:False):
        self.cancelled=cancel;self.next_id=1;self.messages=queue.Queue();self.output=[];self.tool_events=[];self.denials=0
        self.process=subprocess.Popen([str(executable),'acp'],cwd=cwd,stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,stderr=subprocess.DEVNULL,creationflags=FLAGS)
        self.writer=threading.Lock();self.session=None;self.on_tool_update=None;self.tool_state={};self.completed=lambda:False
        threading.Thread(target=self._read,daemon=True).start()

    def send(self,doc):
        raw=(json.dumps(doc,separators=(',',':'))+'\n').encode()
        with self.writer:self.process.stdin.write(raw);self.process.stdin.flush()

    def _read(self):
        try:
            for line in self.process.stdout:
                if len(line)>2_000_000:raise ACPError('frame_too_large')
                try:self.messages.put(json.loads(line))
                except ValueError:continue
        finally:self.messages.put({'bridge_eof':True})

    def call(self,method,params,seconds):
        request_id=self.next_id;self.next_id+=1
        self.send({'jsonrpc':'2.0','id':request_id,'method':method,'params':params})
        end=time.monotonic()+seconds
        while time.monotonic()<end:
            if method=='session/prompt' and self.completed():
                self.cancel();return {'stopReason':'bridge_verified'}
            if self.cancelled():self.cancel();raise ACPError('cancelled')
            try:message=self.messages.get(timeout=.5)
            except queue.Empty:continue
            if message.get('bridge_eof'):raise ACPError('server_exited')
            if message.get('method')=='session/request_permission':
                self.denials+=1
                self.send({'jsonrpc':'2.0','id':message['id'],'result':{'outcome':{'outcome':'cancelled'}}})
                continue
            if message.get('method')=='session/update':
                update=message.get('params',{}).get('update',{});kind=update.get('sessionUpdate')
                if kind=='agent_message_chunk' and update.get('content',{}).get('type')=='text':
                    self.output.append(update['content']['text'])
                if kind in ('tool_call','tool_call_update'):
                    tool_id=update.get('toolCallId')
                    self.tool_state.setdefault(tool_id,{}).update(update)
                    update=self.tool_state[tool_id]
                    self.tool_events.append({k:update.get(k) for k in ('toolCallId','title','kind','status')})
                    if self.on_tool_update and self.on_tool_update(self,update):
                        self.cancel();return {'stopReason':'bridge_verified'}
                continue
            if 'method' in message and 'id' in message:
                self.send({'jsonrpc':'2.0','id':message['id'],'error':{'code':-32601,'message':'Unsupported client method'}})
                continue
            if message.get('id')==request_id:
                if message.get('error'):raise ACPError('protocol_error_'+str(message['error'].get('code','unknown')))
                return message.get('result',{})
        self.cancel();raise ACPError('deadline_exceeded')

    def initialize(self,cwd):
        result=self.call('initialize',{'protocolVersion':1,'clientCapabilities':{},
             'clientInfo':{'name':'jarvis-frontdoor','version':'1'}},30)
        if result.get('protocolVersion')!=1:raise ACPError('unsupported_protocol')
        result=self.call('session/new',{'cwd':str(cwd),'mcpServers':[]},30)
        self.session_info=result
        self.session=result['sessionId']
        model=result.get('models',{}).get('currentModelId','')
        for option in result.get('configOptions',[]):
            if option.get('category')=='model' or option.get('id')=='model':model=option.get('currentValue',model)
        if model and not model.startswith('ollama/'):
            raise ACPError('nonlocal_model_refused')
        return {'protocol':1,'model_local':model.startswith('ollama/'),'model':model}

    def prompt(self,text,seconds=240):
        return self.call('session/prompt',{'sessionId':self.session,
                         'prompt':[{'type':'text','text':text}]},seconds)

    def cancel(self):
        if self.session and self.process.poll() is None:
            try:self.send({'jsonrpc':'2.0','method':'session/cancel','params':{'sessionId':self.session}})
            except (OSError,ValueError):pass

    def close(self):
        try:self.process.stdin.close()
        except OSError:pass
        try:self.process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            self.process.terminate()
            try:self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:self.process.kill();self.process.wait(timeout=5)
