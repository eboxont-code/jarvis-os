"""Project creation/verification under one owned Shared directory only."""
import hashlib,json,os,pathlib,re,subprocess,time

HERE=pathlib.Path(__file__).resolve().parent
PROJECTS=HERE/'projects'
COMMAND=r'C:\Python314\python.exe verify.py'
MODEL='jarvis-code-qwen27b:16k'

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def no_reparse(path):
    for part in [path,*path.parents]:
        if part==HERE.parent:break
        if part.exists() and (part.is_symlink() or (hasattr(part,'is_junction') and part.is_junction())):raise ValueError('reparse_path_refused')

def project_path(name):
    if not isinstance(name,str) or not re.fullmatch('[a-z][a-z0-9-]{0,31}',name) or name.upper() in {'CON','PRN','AUX','NUL','COM1','LPT1'}:raise ValueError('invalid_project')
    path=PROJECTS/name;no_reparse(path)
    if not path.resolve().is_relative_to(PROJECTS.resolve()):raise ValueError('outside_workspace')
    return path

def ensure_project(name,fixture=False):
    root=project_path(name)
    if (root/'.bridge-policy.json').exists():return root
    if root.exists():raise ValueError('unmanaged_project_preserved')
    (root/'src').mkdir(parents=True);(root/'tests').mkdir()
    (root/'src/__init__.py').write_text('')
    (root/'verify.py').write_bytes((HERE/'verify_project.py').read_bytes())
    permissions=[{'action':'*','resource':'*','effect':'deny'},
      {'action':'read','resource':'*','effect':'allow'},
      {'action':'external_directory','resource':'*','effect':'deny'},
      {'action':'edit','resource':'src/**','effect':'allow'},
      {'action':'edit','resource':'tests/**','effect':'allow'},
      {'action':'edit','resource':'README.md','effect':'allow'},
      {'action':'read','resource':'*.env*','effect':'deny'},
      {'action':'edit','resource':'*.env*','effect':'deny'},
      {'action':'shell','resource':COMMAND,'effect':'allow'}]
    if fixture:permissions.append({'action':'edit','resource':'tests/**','effect':'deny'})
    config={'model':'ollama/'+MODEL,'enabled_providers':['ollama'],'permissions':permissions,
      'agents':{'title':{'disabled':True}},
      'providers':{'ollama':{'models':{MODEL:{
        'body':{'think':False,'reasoning_effort':'none'},
        'limit':{'context':16384,'output':2048}}}}}}
    (root/'opencode.jsonc').write_text(json.dumps(config,indent=2))
    (root/'AGENTS.md').write_text('# OpenJarvis front-door coding project\n'
      'The root jarvis-os MASTER_TODO is sole project-status authority; operator syncs it. '
      'Work only in this project. Use local Ollama only. No installs/downloads, cloud, credentials, '
      'outside files, network, app/global settings, delegation, deletion or service/process control. '
      'Edit only src/, tests/ and README.md allowed by opencode.jsonc. Preserve protected files. '
      'Do not open .env or credential files. No alternate shell commands or wrappers. '
      'Run exactly '+COMMAND+'. Verifier executes only restricted pure-Python tests; report '
      'runtime_permission_required honestly for broader programs. Do not bypass the verifier. '
      'At most three test attempts. Fix once after a genuine failure, then return immediately '
      'with changed files, actual test counts and remaining issues. No competing tracker.\n')
    if fixture:
        (root/'src/math.py').write_text('def add(a, b):\n    return a - b\n')
        (root/'tests/test_math.py').write_text('import unittest\nfrom src.math import add\nclass MathTests(unittest.TestCase):\n    def test_positive(self): self.assertEqual(add(2,3),5)\n    def test_negative(self): self.assertEqual(add(-2,3),1)\n    def test_zero(self): self.assertEqual(add(0,0),0)\n')
    protected=['AGENTS.md','opencode.jsonc','verify.py']+(['tests/test_math.py'] if fixture else [])
    policy={'version':1,'protected':{p:digest(root/p) for p in protected},'fixture':fixture}
    (root/'.bridge-policy.json').write_text(json.dumps(policy,indent=2))
    result=subprocess.run(['git','init','--quiet',str(root)],capture_output=True,timeout=15,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    if result.returncode:raise RuntimeError('project_git_init_failed')
    return root

def snapshot(root):
    no_reparse(root)
    result={}
    for directory in ('src','tests'):
        for path in (root/directory).rglob('*'):
            no_reparse(path)
            if path.is_file():
                if len(result)>128 or path.stat().st_size>200_000:raise ValueError('project_size_limit')
                result[str(path.relative_to(root)).replace('\\','/')]=digest(path)
    if (root/'README.md').is_file():result['README.md']=digest(root/'README.md')
    policy=json.loads((root/'.bridge-policy.json').read_text())
    if any(not (root/p).is_file() or digest(root/p)!=h for p,h in policy['protected'].items()):raise ValueError('protected_file_changed')
    return result

def verify(root):
    snapshot(root)
    p=subprocess.run([r'C:\Python314\python.exe','verify.py'],cwd=root,capture_output=True,text=True,encoding='utf-8',timeout=30,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
    try:result=json.loads(p.stdout.strip().splitlines()[-1])
    except (ValueError,IndexError):return {'passed':False,'exit_code':p.returncode,'reason':'verifier_invalid_result'}
    result['exit_code']=p.returncode
    return result
