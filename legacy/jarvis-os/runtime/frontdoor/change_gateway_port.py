"""Operator-approved offline gateway.port change; private backup stays in profile."""
import json,pathlib,re,hashlib
p=pathlib.Path.home()/'.openclaw/openclaw.json'
raw=p.read_bytes();text=raw.decode('utf-8-sig');old=json.loads(text)
assert old['gateway']['port']==50368,'unexpected_current_port'
new=json.loads(text);new['gateway']['port']=18789
backup=p.with_name('openclaw.before-port-18789-20261118.json')
if backup.exists():assert backup.read_bytes()==raw,'backup_collision'
else:backup.write_bytes(raw)
# Parse and compare the entire document, never export its values.
assert {k for k in old if old[k]!=new[k]}=={'gateway'}
assert {k for k in old['gateway'] if old['gateway'][k]!=new['gateway'][k]}=={'port'}
out=json.dumps(new,indent=2).encode('utf-8')
assert p.read_bytes()==raw,'concurrent_configuration_change'
p.write_bytes(out)
assert json.loads(p.read_bytes())==new
print(json.dumps({'changed':'gateway.port','old_port':50368,'new_port':18789,'backup_verified':backup.read_bytes()==raw,'other_values_unchanged':True}))
