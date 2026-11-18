"""Read-only native bindings/protocol checks; no agent prompts or model calls."""
import json,pathlib,queue,subprocess,sys,threading,time,urllib.parse,uuid
HOME=pathlib.Path.home()
ROOT=pathlib.Path(__file__).resolve().parent
FLAGS=getattr(subprocess,'CREATE_NO_WINDOW',0)

def command():
    import shutil
    c=shutil.which('openclaw')
    if not c:raise ValueError('cli_not_found')
    return c

def rpc(method):
    if method not in ('health','node.list'):raise ValueError('method_not_allowed')
    p=subprocess.run([command(),'gateway','call',method,'--json','--timeout','10000'],
                     capture_output=True,text=True,encoding='utf-8',timeout=18,creationflags=FLAGS)
    if p.returncode:raise ValueError('gateway_rpc_failed')
    return json.loads(p.stdout)

def acp_initialize(executable):
    p=subprocess.Popen([executable,'acp'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,
                       stderr=subprocess.DEVNULL,cwd=ROOT,text=True,encoding='utf-8',creationflags=FLAGS)
    responses=queue.Queue()
    def reader():
        for line in p.stdout:
            if len(line)>1_000_000:break
            try:responses.put(json.loads(line))
            except ValueError:pass
    threading.Thread(target=reader,daemon=True).start()
    try:
        request={'jsonrpc':'2.0','id':1,'method':'initialize','params':{'protocolVersion':1,'clientCapabilities':{},'clientInfo':{'name':'jarvis-startup-readiness','version':'1'}}}
        p.stdin.write(json.dumps(request)+'\n');p.stdin.flush()
        end=time.monotonic()+25
        while time.monotonic()<end:
            try:r=responses.get(timeout=1)
            except queue.Empty:continue
            if r.get('id')==1:
                return not r.get('error') and r.get('result',{}).get('protocolVersion')==1
        return False
    finally:
        p.stdin.close()
        try:p.wait(timeout=8)
        except subprocess.TimeoutExpired:
            p.terminate()
            try:p.wait(timeout=5)
            except subprocess.TimeoutExpired:p.kill();p.wait(timeout=5)

def main():
    phase=sys.argv[1]
    if phase=='health':
        d=rpc('health');return {'ready':d.get('ok') is True}
    if phase=='node':
        rows=rpc('node.list').get('nodes',[])
        return {'ready':len(rows)==1 and rows[0].get('connected') is True and rows[0].get('paired') is True}
    if phase not in ('connections','acp'):raise ValueError('phase_not_allowed')
    c=json.loads((HOME/'.openclaw/openclaw.json').read_text(encoding='utf-8-sig'))
    providers=c.get('models',{}).get('providers',{})
    defaults=c.get('agents',{}).get('defaults',{}).get('model',{})
    primary=defaults.get('primary','') if isinstance(defaults,dict) else defaults
    assert set(providers)=={'ollama'}
    assert all(urllib.parse.urlparse(p.get('baseUrl','')).hostname in ('127.0.0.1','localhost','::1') for p in providers.values())
    assert str(primary).startswith('ollama/') and (not isinstance(defaults,dict) or not defaults.get('fallbacks'))
    entry=c['plugins']['entries']['acpx'];assert entry.get('enabled') is True
    executable=entry['config']['agents']['opencode']['command'];assert pathlib.Path(executable).is_file()
    assert entry['config']['agents']['opencode'].get('args')==['acp']
    if phase=='acp':return {'ready':bool(acp_initialize(executable))}
    # Use the already approved three-tool adapter directly, without adding or
    # changing a Gateway registration or launching a model task.
    adapter=ROOT.parent/'jarvis-readonly-mcp-20261118/openjarvis_readonly_mcp_adapter.py'
    names=['openjarvis_health','openjarvis_models','openjarvis_runtime_status']
    server=c['mcp']['servers']['openjarvis-readonly']
    assert pathlib.Path(server['command']).resolve()==pathlib.Path(sys.executable).resolve()
    assert len(server['args'])==1 and pathlib.Path(server['args'][0]).resolve()==adapter.resolve()
    assert set(server['toolFilter']['include'])==set(names)
    assert server['requestTimeoutMs']==10000 and server['connectionTimeoutMs']==10000
    assert server['codex']['defaultToolsApprovalMode']=='prompt'
    requests=[{'jsonrpc':'2.0','id':1,'method':'initialize'},
              {'jsonrpc':'2.0','method':'notifications/initialized'},
              {'jsonrpc':'2.0','id':2,'method':'tools/list'}]
    requests += [{'jsonrpc':'2.0','id':i+3,'method':'tools/call','params':{'name':n,'arguments':{}}} for i,n in enumerate(names)]
    p=subprocess.run([sys.executable,str(adapter)],input=''.join(json.dumps(r)+'\n' for r in requests),
                     capture_output=True,text=True,encoding='utf-8',timeout=25,creationflags=FLAGS)
    assert p.returncode==0
    replies=[json.loads(line) for line in p.stdout.splitlines()];assert len(replies)==5
    assert [t['name'] for t in replies[1]['result']['tools']]==names
    assert all(not r['result']['isError'] and json.loads(r['result']['content'][0]['text'])['available'] for r in replies[2:])
    assert acp_initialize(executable)
    return {'ready':True,'local_provider':True,'mcp_tools':3,'acp_initialize':True}

if __name__=='__main__':
    try:print(json.dumps(main()))
    except Exception as exc:
        print(json.dumps({'ready':False,'error_type':type(exc).__name__}));raise SystemExit(1)
