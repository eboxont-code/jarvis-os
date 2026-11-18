"""Bridge-owned verifier. Parse first; execute only a restricted pure-Python test subset."""
import ast,io,json,pathlib,sys,unittest

ROOT=pathlib.Path(__file__).resolve().parent
ALLOWED_BUILTINS={'abs','all','any','bool','dict','enumerate','float','int','isinstance','len','list','max','min','print','range','reversed','round','set','sorted','str','sum','tuple','zip','ValueError','TypeError','AssertionError'}
ALLOWED_ATTRS={'TestCase','assertEqual','assertNotEqual','assertTrue','assertFalse','assertRaises','assertIsNone','assertIsNotNone','assertIn','assertNotIn','assertAlmostEqual','assertGreater','assertLess','strip','lower','upper','split','join','append','extend','sort','get','keys','values','items','sqrt','isfinite','floor','ceil','sin','cos','pi','e'}

def resource_limits():
    # Limits apply only to this verification process, never OpenCode/Ollama/apps.
    if sys.platform!='win32':raise ValueError('runtime_resource_isolation_unavailable')
    import ctypes
    from ctypes import wintypes as w
    class Basic(ctypes.Structure):
        _fields_=[('process_time',ctypes.c_longlong),('job_time',ctypes.c_longlong),('flags',w.DWORD),('min_ws',ctypes.c_size_t),('max_ws',ctypes.c_size_t),('active',w.DWORD),('affinity',ctypes.c_size_t),('priority',w.DWORD),('scheduling',w.DWORD)]
    class Extended(ctypes.Structure):
        _fields_=[('basic',Basic),('io',ctypes.c_ulonglong*6),('process_memory',ctypes.c_size_t),('job_memory',ctypes.c_size_t),('peak_process',ctypes.c_size_t),('peak_job',ctypes.c_size_t)]
    kernel=ctypes.WinDLL('kernel32',use_last_error=True)
    kernel.CreateJobObjectW.restype=w.HANDLE;kernel.CreateJobObjectW.argtypes=[ctypes.c_void_p,w.LPCWSTR]
    kernel.SetInformationJobObject.argtypes=[w.HANDLE,ctypes.c_int,ctypes.c_void_p,w.DWORD]
    kernel.AssignProcessToJobObject.argtypes=[w.HANDLE,w.HANDLE]
    kernel.GetCurrentProcess.restype=w.HANDLE
    handle=kernel.CreateJobObjectW(None,None);limits=Extended()
    limits.basic.flags=0x100|0x8|0x2;limits.basic.active=1;limits.basic.process_time=15*10_000_000
    limits.process_memory=256*1024*1024
    if not handle or not kernel.SetInformationJobObject(handle,9,ctypes.byref(limits),ctypes.sizeof(limits)) or not kernel.AssignProcessToJobObject(handle,kernel.GetCurrentProcess()):raise ValueError('runtime_resource_isolation_unavailable')
    return handle

def validate(files):
    trees={}
    for path in files:
        if path.is_symlink() or (hasattr(path,'is_junction') and path.is_junction()) or not path.resolve().is_relative_to(ROOT):raise ValueError('path_boundary')
        if path.stat().st_size>100_000:raise ValueError('source_too_large')
        trees[path]=ast.parse(path.read_text(encoding='utf-8-sig'))
    declared={n.name for t in trees.values() for n in ast.walk(t) if isinstance(n,(ast.FunctionDef,ast.ClassDef))}
    for tree in trees.values():
        for node in ast.walk(tree):
            if isinstance(node,(ast.AsyncFunctionDef,ast.With,ast.AsyncWith,ast.Global,ast.Nonlocal,ast.Delete)):raise ValueError('runtime_permission_required')
            if isinstance(node,(ast.FunctionDef,ast.ClassDef)) and node.name.startswith('__'):raise ValueError('dunder_refused')
            if isinstance(node,ast.Name) and node.id.startswith('__') and node.id!='__name__':raise ValueError('dunder_refused')
            if isinstance(node,ast.Attribute) and (node.attr.startswith('_') or node.attr not in ALLOWED_ATTRS):raise ValueError('runtime_permission_required')
            if isinstance(node,(ast.Import,ast.ImportFrom)):
                modules=[a.name for a in node.names] if isinstance(node,ast.Import) else [node.module or '']
                for module in modules:
                    if module not in {'math','unittest'} and not module.startswith('src.') and module!='src':raise ValueError('runtime_permission_required')
                if isinstance(node,ast.ImportFrom) and node.module=='unittest' and any(a.name!='TestCase' for a in node.names):raise ValueError('runtime_permission_required')
                if isinstance(node,ast.ImportFrom) and node.module=='math' and any(a.name not in ALLOWED_ATTRS for a in node.names):raise ValueError('runtime_permission_required')
            if isinstance(node,ast.Call):
                if isinstance(node.func,ast.Name) and node.func.id not in ALLOWED_BUILTINS|declared:raise ValueError('runtime_permission_required')
                if not isinstance(node.func,(ast.Name,ast.Attribute)):raise ValueError('dynamic_call_refused')
            if isinstance(node,(ast.Assign,ast.AnnAssign,ast.AugAssign)):
                targets=node.targets if isinstance(node,ast.Assign) else [node.target]
                for target in targets:
                    if isinstance(target,ast.Attribute):raise ValueError('attribute_mutation_refused')
    return trees

def main():
    resource_handle=resource_limits()
    files=list((ROOT/'src').rglob('*.py'))+list((ROOT/'tests').rglob('*.py'))
    if not files:raise ValueError('no_python_sources')
    validate(files)
    sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT))
    suite=unittest.defaultTestLoader.discover(str(ROOT/'tests'),pattern='test_*.py')
    output=io.StringIO();result=unittest.TextTestRunner(stream=output,verbosity=1).run(suite)
    passed=result.wasSuccessful() and result.testsRun>0
    print(json.dumps({'passed':passed,'syntax_passed':True,'runtime_checked':True,'exit_code':0 if passed else 1,
       'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
       'details':output.getvalue()[-5000:] if not passed else ''}))
    return 0 if passed else 1

if __name__=='__main__':
    try:raise SystemExit(main())
    except (SyntaxError,ValueError) as exc:
        print(json.dumps({'passed':False,'runtime_checked':False,'exit_code':2,
                          'reason':str(exc) if isinstance(exc,ValueError) else 'syntax_error'}));raise SystemExit(2)
