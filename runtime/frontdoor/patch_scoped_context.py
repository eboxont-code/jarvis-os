import pathlib,json,subprocess,shutil
root=pathlib.Path(__file__).resolve().parent
patch={'agents':{'entries':{'jarvis-frontdoor':{'models':{'ollama/qwen3.8:27b':{'params':{'num_ctx':16384,'think':False}}}}}}}
p=root/'context.patch.json';p.write_text(json.dumps(patch))
config=pathlib.Path.home()/'.openclaw/openclaw.json';before=config.read_bytes();backup=config.with_name('openclaw.before-frontdoor-context-20261118.json')
if not backup.exists():backup.write_bytes(before)
assert backup.read_bytes()==before
for dry in (True,False):
 args=[shutil.which('openclaw'),'config','patch','--file',str(p)]+(['--dry-run','--json'] if dry else [])
 r=subprocess.run(args,capture_output=True,text=True,encoding='utf-8',timeout=180)
 print(json.dumps({'dry_run':dry,'passed':r.returncode==0}),flush=True)
 if r.returncode:
  if dry:
   try:print(json.dumps({'errors':json.loads(r.stdout).get('errors')}))
   except ValueError:pass
  raise SystemExit(1)
a=json.loads(before);b=json.loads(config.read_bytes())
assert a['agents']['entries']['main']==b['agents']['entries']['main']
assert a['models']==b['models']
print(json.dumps({'main_agent_unchanged':True,'global_models_unchanged':True,'scoped_context':16384}))
