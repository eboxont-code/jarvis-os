"""One-time operator activation in the authorised normal-user runtime workspace."""
import importlib,json,pathlib,shutil,subprocess,sys,time,datetime
SOURCE=pathlib.Path(__file__).resolve().parent
STACK_SOURCE=SOURCE if (SOURCE/'openjarvis_watchdog.py').is_file() else SOURCE.parent
RUNTIME=pathlib.Path.home()/'Documents/Codex/jarvis-os-runtime'
sys.path.insert(0,str(RUNTIME))
import openjarvis_watchdog as w

def report(stage):print(json.dumps({'stage':stage}),flush=True)
def main():
    assert RUNTIME.is_dir() and w.healthy(),'live_baseline_required'
    marker=RUNTIME/'watchdog.stop';assert not marker.exists(),'existing_stop_request_preserved'
    refresh='--refresh' in sys.argv
    if refresh:
        shared=pathlib.Path(json.loads((RUNTIME/'frontdoor/frontdoor.json').read_text())['shared'])
        for p in (shared/'jobs').glob('*.json'):
            d=json.loads(p.read_text())
            assert not (d.get('state') in ('pending','running') and d.get('deadline',0)>time.time()),'active_bridge_job_preserved'
    suffix='frontdoor-refresh-'+datetime.datetime.now().strftime('%Y%m%d-%H%M%S') if refresh else 'frontdoor-20261118'
    backup=RUNTIME/'backups'/suffix;backup.mkdir(exist_ok=True)
    for name in ('openjarvis_watchdog.py','test_openjarvis_watchdog.py'):
        p=RUNTIME/name;q=backup/name
        assert not q.exists(),'activation_already_attempted_review_required'
        shutil.copy2(p,q);assert q.read_bytes()==p.read_bytes()
    if refresh:
        for name in ('frontdoor.py','backend_bootstrap.py'):shutil.copy2(RUNTIME/'frontdoor'/name,backup/name)
    marker.touch();report('pausing_project_watchdog')
    until=time.time()+40
    while time.time()<until:
        d=json.loads(w.STATE.read_text())
        if d.get('phase')=='stopped_by_marker':break
        time.sleep(1)
    else:raise RuntimeError('watchdog_pause_not_confirmed')
    time.sleep(1)
    for name in ('openjarvis_watchdog.py','test_openjarvis_watchdog.py'):shutil.copy2(STACK_SOURCE/name,RUNTIME/name)
    addon=RUNTIME/'frontdoor';addon.mkdir(exist_ok=True)
    for name in ('frontdoor.py','backend_bootstrap.py'):shutil.copy2(SOURCE/name,addon/name)
    config={'clawctl':str(pathlib.Path.home()/'AppData/Local/Microsoft/WindowsApps/OpenClawFoundation.OpenClawGateway_rfcbke2p71se2/clawctl.exe'),
            'shared':r'C:\Users\T3-P2\Shared\jarvis-frontdoor-20261118'}
    (addon/'frontdoor.json').write_text(json.dumps(config,indent=2))
    manifest=json.loads((RUNTIME/'manifest.json').read_text(encoding='utf-8-sig'))
    rows=w.inventory(manifest['openjarvis']);w.stop_exact([r for r in rows if not r.get('Desktop')])
    assert not w.port_open(),'new_listener_preserved'
    importlib.reload(w);w.launch_backend();report('bridge_backend_starting')
    if not w.boot.wait_until(w.healthy,240,interval=3):
        report('activation_failed_rolling_back')
        rows=w.inventory(manifest['openjarvis']);w.stop_exact([r for r in rows if not r.get('Desktop')])
        if refresh:
            for name in ('frontdoor.py','backend_bootstrap.py'):shutil.copy2(backup/name,addon/name)
        else:(addon/'frontdoor.json').rename(addon/'frontdoor.disabled.json')
        shutil.copy2(backup/'openjarvis_watchdog.py',RUNTIME/'openjarvis_watchdog.py')
        importlib.reload(w);w.launch_backend()
        recovered=w.boot.wait_until(w.healthy,360,interval=3)
        marker.unlink()
        subprocess.Popen([r'C:\Python314\pythonw.exe',str(RUNTIME/'openjarvis_watchdog.py'),'--bootstrap'],creationflags=w.boot.FLAGS)
        print(json.dumps({'bridge_activated':False,'original_backend_recovered':recovered}),flush=True)
        return 1
    marker.unlink()
    subprocess.Popen([r'C:\Python314\pythonw.exe',str(RUNTIME/'openjarvis_watchdog.py'),'--bootstrap'],creationflags=w.boot.FLAGS)
    print(json.dumps({'bridge_activated':True,'health_passed':True,'desktop_preserved':True}),flush=True)
    return 0

if __name__=='__main__':raise SystemExit(main())
