"""Fixed local-only bounded streaming smoke test. Never emits response content."""
import json,time,urllib.request
start=time.monotonic();marker='OPENJARVIS_REPAIRED_OK';text=''
payload={'model':'qwen3.8:27b','messages':[{'role':'user','content':'Reply exactly '+marker+'.'}],
         'tools':[],'stream':True,'max_tokens':256,'temperature':0}
opener=urllib.request.build_opener(urllib.request.ProxyHandler({}))
request=urllib.request.Request('http://127.0.0.1:8000/v1/chat/completions',data=json.dumps(payload).encode(),headers={'Content-Type':'application/json'})
try:
    with opener.open(request,timeout=90) as response:
        for raw in response:
            if time.monotonic()-start>90:raise TimeoutError()
            if not raw.startswith(b'data: '):continue
            if raw.strip()==b'data: [DONE]':break
            d=json.loads(raw[6:])
            for c in d.get('choices',[]):text+=c.get('delta',{}).get('content','') or ''
    print(json.dumps({'local_chat_pass':marker in text,'elapsed_seconds':round(time.monotonic()-start,1),'tool_calls_requested':False}))
except Exception as exc:
    print(json.dumps({'local_chat_pass':False,'error_type':type(exc).__name__,'elapsed_seconds':round(time.monotonic()-start,1)}));raise SystemExit(1)
