import pathlib,json,copy,subprocess,shutil,sys
root=pathlib.Path(__file__).resolve().parent;cfg=pathlib.Path.home()/'.openclaw/openclaw.json';raw=cfg.read_bytes();c=json.loads(raw)
old=c['models']['providers']['ollama'];row=next(copy.deepcopy(m) for m in old['models'] if m['id']=='qwen3.8:27b')
row.update(contextTokens=16384,maxTokens=1024);row['params']={**row.get('params',{}),'num_ctx':16384,'think':False}
provider={'api':'ollama','baseUrl':'http://127.0.0.1:11434','apiKey':'ollama-local','models':[row]}
patch={'models':{'providers':{'jarvis-local':provider}},'agents':{'entries':{'jarvis-frontdoor':{'model':{'primary':'jarvis-local/qwen3.8:27b','fallbacks':[]},'models':{'jarvis-local/qwen3.8:27b':{'params':{'maxTokens':1024,'thinking':'off'},'codeMode':False}}}}}}
p=root/'bridge-local-model.patch.json';p.write_text(json.dumps(patch))
apply=sys.argv[-1]=='apply'
if apply:
 b=cfg.with_name('openclaw.before-bridge-local-model-20261118.json')
 if not b.exists():b.write_bytes(raw)
 assert b.read_bytes()==raw
args=[shutil.which('openclaw'),'config','patch','--file',str(p)]+([] if apply else ['--dry-run','--json'])
r=subprocess.run(args,capture_output=True,text=True,encoding='utf-8',timeout=180)
print(json.dumps({'applied':apply and r.returncode==0,'passed':r.returncode==0,'same_existing_model':True,'new_endpoint_loopback_only':True,'original_provider_unchanged':json.loads(cfg.read_bytes())['models']['providers']['ollama']==old}))
if r.returncode:
 try:print(json.dumps({'errors':json.loads(r.stdout).get('errors')}))
 except ValueError:pass
raise SystemExit(r.returncode)
