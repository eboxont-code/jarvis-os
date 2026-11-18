"""Create a no-download context alias of one already-installed local model.

Run manually after fresh inventory. Never pulls, replaces or removes a model.
"""
import json,urllib.request
SOURCE='qwen3.8:27b'
ALIAS='jarvis-code-qwen27b:16k'
BASE='http://127.0.0.1:11434'

def request(path,data=None):
    raw=None if data is None else json.dumps(data).encode()
    req=urllib.request.Request(BASE+path,data=raw,headers={'Content-Type':'application/json'})
    with urllib.request.urlopen(req,timeout=60) as response:return json.load(response)

def prepare():
    before={m['name']:m['digest'] for m in request('/api/tags')['models']}
    if SOURCE not in before:raise ValueError('installed_source_required_no_download')
    if ALIAS in before:raise ValueError('existing_alias_preserved_review_required')
    source=request('/api/show',{'model':SOURCE})
    result=request('/api/create',{'model':ALIAS,'from':SOURCE,'parameters':{'num_ctx':16384},'stream':False})
    if result.get('status')!='success':raise RuntimeError('alias_creation_failed')
    after={m['name']:m['digest'] for m in request('/api/tags')['models']}
    if any(after.get(k)!=v for k,v in before.items()):raise RuntimeError('original_model_inventory_changed')
    alias=request('/api/show',{'model':ALIAS})
    fields=('format','family','families','parameter_size','quantization_level','runner')
    if any(alias.get('details',{}).get(k)!=source.get('details',{}).get(k) for k in fields) or '16384' not in alias.get('parameters',''):
        raise RuntimeError('alias_verification_failed')
    weights=lambda model:[line for line in model.get('modelfile','').splitlines() if line.startswith('FROM ')]
    if not weights(source) or weights(alias)!=weights(source):raise RuntimeError('existing_weights_not_confirmed')
    return {'original_models_preserved':len(before),'local_alias':ALIAS,'context_parameter':16384,'downloads':0}

if __name__=='__main__':print(json.dumps(prepare()))
