"""Install/undo the user-requested startup owner. Normal-user privilege only."""
import argparse,datetime,hashlib,json,os,pathlib,re,shutil,subprocess,sys
import winreg

SOURCE=pathlib.Path(__file__).resolve().parent
RUNTIME=pathlib.Path.home()/'Documents/Codex/jarvis-os-runtime'
LOCAL=pathlib.Path(os.environ['LOCALAPPDATA'])
ROAMING=pathlib.Path(os.environ['APPDATA'])
STARTUP=ROAMING/'Microsoft/Windows/Start Menu/Programs/Startup'
SETTINGS=ROAMING/'OpenClawTray/settings.json'
RUN_KEY=r'Software\Microsoft\Windows\CurrentVersion\Run'
WAIT_TASK='OpenClaw Companion - Wait for Gateway'
PS=pathlib.Path(os.environ['SystemRoot'])/'System32/WindowsPowerShell/v1.0/powershell.exe'
FLAGS=getattr(subprocess,'CREATE_NO_WINDOW',0)

def q(s):return "'"+str(s).replace("'","''")+"'"
def sha(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def ps(code):
    p=subprocess.run([str(PS),'-NoProfile','-NonInteractive','-Command',"$ErrorActionPreference='Stop'; "+code],
                     capture_output=True,text=True,encoding='utf-8-sig',timeout=30,creationflags=FLAGS)
    if p.returncode:
        if 'access is denied' in p.stderr.lower() or 'unauthorizedaccess' in p.stderr.lower():
            raise RuntimeError('startup_task_permission_denied')
        raise RuntimeError('windows_startup_operation_failed')
    return p.stdout
def write_json(path,data):path.write_text(json.dumps(data,indent=2),encoding='utf-8')
def patch_autostart(value):
    raw=SETTINGS.read_bytes();bom=raw.startswith(b'\xef\xbb\xbf');text=raw.decode('utf-8-sig');before=json.loads(text)
    new,count=re.subn(r'("AutoStart"\s*:\s*)(?:true|false)',lambda m:m[1]+str(value).lower(),text,count=1)
    assert count==1
    after=json.loads(new);assert {k for k in set(before)|set(after) if before.get(k)!=after.get(k)}<={'AutoStart'}
    SETTINGS.write_bytes((b'\xef\xbb\xbf' if bom else b'')+new.encode())
def companion_running():
    return ps("@(Get-Process -Name 'OpenClaw.Tray.WinUI' -ErrorAction SilentlyContinue).Count").strip()!='0'
def run_value():
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER,RUN_KEY) as key:
        try:return winreg.QueryValueEx(key,'OpenClawTray')[0]
        except FileNotFoundError:return None

def uninstall(state):
    # Refuse to overwrite later user startup edits. Restore only AutoStart,
    # preserving every other current Companion setting and saved credential.
    if companion_running():raise RuntimeError('close_companion_before_rollback')
    if ps("@(Get-CimInstance Win32_Process | Where-Object { $_.Name -eq 'pythonw.exe' -and $_.CommandLine -like '*jarvis-os-runtime\\openjarvis_watchdog.py*' }).Count").strip()!='0':
        raise RuntimeError('stop_watchdog_before_rollback')
    link=STARTUP/'JARVIS AI Stack.lnk'
    if link.exists():
        if sha(link)!=state.get('installed_shortcut_hash'):raise RuntimeError('newer_startup_shortcut_preserved')
        destination=pathlib.Path(state['backup'])/'removed-JARVIS-AI-Stack.lnk'
        if destination.exists():raise RuntimeError('rollback_destination_exists')
        shutil.move(str(link),str(destination))
    for row in state['shortcuts']:
        src=pathlib.Path(row['backup']);dst=pathlib.Path(row['original'])
        if src.exists():
            assert sha(src)==row['sha256']
            if dst.exists():raise RuntimeError('newer_original_shortcut_preserved')
            shutil.copy2(src,dst)
    patch_autostart(state['original_autostart'])
    if state['run_value'] is not None:
        if run_value() is not None:raise RuntimeError('newer_run_value_preserved')
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER,RUN_KEY,0,winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key,'OpenClawTray',0,winreg.REG_SZ,state['run_value'])
    if state['wait_task_present'] and state['wait_task_enabled']:
        ps('Enable-ScheduledTask -TaskName '+q(WAIT_TASK)+' | Out-Null')
    state['installed']=False;state['rolled_back']=True;write_json(RUNTIME/'installation.json',state)

def install():
    if companion_running():raise RuntimeError('close_companion_before_startup_owner_change')
    statefile=RUNTIME/'installation.json'
    if statefile.exists():raise RuntimeError('installation_already_recorded_do_not_overwrite_backup')
    RUNTIME.mkdir(parents=True,exist_ok=True)
    families=list((LOCAL/'Microsoft/WindowsApps').glob('OpenClawFoundation.OpenClawGateway_*'))
    assert len(families)==1
    clawctl=families[0]/'clawctl.exe';assert clawctl.is_file()
    p=subprocess.run([str(clawctl),'status','--json'],capture_output=True,text=True,encoding='utf-8-sig',timeout=30,creationflags=FLAGS)
    assert p.returncode==0
    shared=pathlib.Path(json.loads(p.stdout)['session']['sharedFolder']);assert shared.is_dir()
    isolated=shared/'jarvis-startup-20261118';isolated.mkdir(exist_ok=True)
    for name in ('start_ai_stack.py','test_start_ai_stack.py','install_startup.py',
                 'openjarvis_watchdog.py','test_openjarvis_watchdog.py'):
        if SOURCE.resolve()!=(RUNTIME).resolve():shutil.copy2(SOURCE/name,RUNTIME/name)
    shutil.copy2(SOURCE/'isolated_readiness_probe.py',isolated/'isolated_readiness_probe.py')
    apps={'ollama':LOCAL/'Programs/Ollama/ollama app.exe',
          'openjarvis':LOCAL/'OpenJarvis/openjarvis-desktop.exe',
          'companion':LOCAL/'OpenClawTray/OpenClaw.Tray.WinUI.exe',
          'opencode':LOCAL/'Programs/ai.opencode.desktop/OpenCode.exe'}
    assert all(p.is_file() for p in apps.values())
    manifest={k:str(v) for k,v in apps.items()}
    manifest.update(clawctl=str(clawctl),isolated_probe=str(isolated/'isolated_readiness_probe.py'),
                    inference_config=str(pathlib.Path.home()/'.openjarvis/inference.json'),
                    opencode_config=str(pathlib.Path.home()/'.config/opencode/opencode.json'))
    write_json(RUNTIME/'manifest.json',manifest)
    backup=RUNTIME/'backups'/datetime.datetime.now().strftime('%Y%m%d-%H%M%S');backup.mkdir(parents=True)
    shutil.copy2(SETTINGS,backup/'companion-settings.original.json');assert sha(SETTINGS)==sha(backup/'companion-settings.original.json')
    task=ps('$t=Get-ScheduledTask -TaskName '+q(WAIT_TASK)+' -ErrorAction SilentlyContinue; if($t){Export-ScheduledTask -TaskName '+q(WAIT_TASK)+'}')
    (backup/'wait-task.original.xml').write_text(task,encoding='utf-8')
    enabled=bool(task) and '<Enabled>true</Enabled>' in task
    state={'backup':str(backup),'original_autostart':json.loads(SETTINGS.read_text(encoding='utf-8-sig'))['AutoStart'],
           'original_settings_sha256':sha(SETTINGS),'run_value':run_value(),
           'wait_task_present':bool(task),'wait_task_enabled':enabled,'shortcuts':[],'installed':False}
    for name in ('OpenClaw Companion.lnk','Ollama.lnk'):
        src=STARTUP/name
        if src.exists():
            dst=backup/name;shutil.copy2(src,dst);assert sha(src)==sha(dst)
            state['shortcuts'].append({'original':str(src),'backup':str(dst),'sha256':sha(src)})
    write_json(statefile,state)
    # Backups are verified before any existing startup registration changes.
    try:
        if task:ps('Disable-ScheduledTask -TaskName '+q(WAIT_TASK)+' | Out-Null')
        patch_autostart(False)
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER,RUN_KEY,0,winreg.KEY_SET_VALUE) as key:
            try:winreg.DeleteValue(key,'OpenClawTray')
            except FileNotFoundError:pass
        for row in state['shortcuts']:
            src=pathlib.Path(row['original'])
            # Move each exact shortcut outside Startup. Never delete it.
            destination=backup/('disabled-'+src.name);assert not destination.exists()
            shutil.move(str(src),str(destination))
        link=STARTUP/'JARVIS AI Stack.lnk';assert not link.exists()
        pythonw=pathlib.Path(sys.executable).with_name('pythonw.exe');assert pythonw.is_file()
        ps('$w=New-Object -ComObject WScript.Shell;$s=$w.CreateShortcut('+q(link)+');'
           '$s.TargetPath='+q(pythonw)+';$s.Arguments='+q('"'+str(RUNTIME/'start_ai_stack.py')+'"')+';'
           '$s.WorkingDirectory='+q(RUNTIME)+';$s.Description="Start existing AI stack after readiness checks";$s.Save()')
        state['installed_shortcut_hash']=sha(link);state['installed']=True
        write_json(statefile,state)
    except Exception:
        # Partial rollback uses the original copies, with no destructive cleanup.
        for row in state['shortcuts']:
            dst=pathlib.Path(row['original'])
            if not dst.exists():shutil.copy2(row['backup'],dst)
        patch_autostart(state['original_autostart'])
        if state['run_value'] is not None and run_value() is None:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER,RUN_KEY,0,winreg.KEY_SET_VALUE) as key:
                winreg.SetValueEx(key,'OpenClawTray',0,winreg.REG_SZ,state['run_value'])
        if task and enabled:ps('Enable-ScheduledTask -TaskName '+q(WAIT_TASK)+' | Out-Null')
        state['rolled_back']=True;write_json(statefile,state)
        raise
    print(json.dumps({'installed':True,'startup_owner':'JARVIS AI Stack.lnk','backups_verified':True,'elevated':False}))

if __name__=='__main__':
    args=argparse.ArgumentParser();args.add_argument('--undo',action='store_true');opts=args.parse_args()
    try:
        if opts.undo:uninstall(json.loads((RUNTIME/'installation.json').read_text()));print('{"rolled_back":true}')
        else:install()
    except Exception as exc:
        print(json.dumps({'installed':False,'error_type':type(exc).__name__,
                          'reason':str(exc) if re.fullmatch('[a-z_]+',str(exc)) else 'operation_failed_private_details_omitted'}));raise SystemExit(1)
