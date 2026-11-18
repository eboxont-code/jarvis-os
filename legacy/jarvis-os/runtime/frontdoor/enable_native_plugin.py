import pathlib,json,copy,subprocess,shutil,socket,sys
root=pathlib.Path(__file__).resolve().parent;cfg=pathlib.Path.home()/'.openclaw/openclaw.json';raw=cfg.read_bytes();c=json.loads(raw)
plugin=root/'claw-plugin';assert (plugin/'index.mjs').is_file()
paths=list(c.get('plugins',{}).get('load',{}).get('paths',[]))
if str(plugin) not in paths:paths.append(str(plugin))
patch={'plugins':{'load':{'paths':paths},'entries':{'jarvis-frontdoor-bridge':{'enabled':True}}}}
allow=c.get('plugins',{}).get('allow')
if isinstance(allow,list):patch['plugins']['allow']=list(dict.fromkeys([*allow,'jarvis-frontdoor-bridge']))
p=root/'native-plugin.patch.json';p.write_text(json.dumps(patch))
if sys.argv[-1]=='prepare':print(json.dumps({'prepared':True,'new_plugin_only':True,'dependencies_added':0}));raise SystemExit(0)
with socket.socket() as s:assert s.connect_ex(('127.0.0.1',18789))!=0,'Gateway_must_be_stopped_before_approved_activation'
b=cfg.with_name('openclaw.before-native-delegate-20261118.json')
if not b.exists():b.write_bytes(raw)
assert b.read_bytes()==raw
for dry in (True,False):
 args=[shutil.which('openclaw'),'config','patch','--file',str(p)]+(['--dry-run','--json'] if dry else [])
 r=subprocess.run(args,capture_output=True,text=True,encoding='utf-8',timeout=180)
 print(json.dumps({'dry_run':dry,'passed':r.returncode==0}),flush=True)
 if r.returncode:
  if dry:
   try:print(json.dumps({'errors':json.loads(r.stdout).get('errors')}))
   except ValueError:pass
  raise SystemExit(1)
after=json.loads(cfg.read_bytes())
print(json.dumps({'enabled':after['plugins']['entries']['jarvis-frontdoor-bridge']['enabled'],'existing_agents_unchanged':after['agents']==c['agents'],'model_settings_unchanged':after['models']==c['models'],'auth_unchanged':after['gateway']==c['gateway']}))
