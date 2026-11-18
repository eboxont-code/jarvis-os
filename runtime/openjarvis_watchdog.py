"""Normal-user OpenJarvis health/recovery. No configuration, installs or inference."""
import datetime as dt
import json
import os
import pathlib
import socket
import subprocess
import sys
import time
import start_ai_stack as boot

HERE=pathlib.Path(__file__).resolve().parent
STATE=HERE/'runtime-health.json'
STOP=HERE/'watchdog.stop'
BOOT_ID=''

def healthy():
    try:return boot.get_json('http://127.0.0.1:8000/health').get('status')=='ok'
    except (OSError,ValueError):return False

def port_open():
    try:
        with socket.create_connection(('127.0.0.1',8000),timeout=2):return True
    except OSError:return False

def select_inventory(rows,executable):
    apps={r['ProcessId'] for r in rows if str(r.get('ExecutablePath','')).casefold()==str(executable).casefold()}
    roots={r['ProcessId'] for r in rows if r.get('RootServe')}
    return [dict(r,Desktop=r['ProcessId'] in apps) for r in rows if
       r['ProcessId'] in apps or r['ProcessId'] in roots or
       (r.get('Name')=='uv.exe' and r.get('ParentProcessId') in apps) or
       (r.get('Name')=='python.exe' and r.get('Serve8000') and r.get('ParentProcessId') in roots)]

def inventory(executable):
    # Never export command lines. Match this user's exact preserved checkout.
    app=str(executable).replace("'","''")
    root=str(pathlib.Path.home()/'OpenJarvis').replace("'","''")
    serve="($_.CommandLine -match '(jarvis.exe|openjarvis.cli)' -and $_.CommandLine -match '\\bserve\\b' -and $_.CommandLine -match '--port[ =]+8000(?:\\s|$)')"
    script=("ConvertTo-Json -InputObject @(Get-CimInstance Win32_Process|Where-Object {"
      "$_.ExecutablePath -eq '"+app+"' -or $_.Name -in 'python.exe','uv.exe'}|"
      "Select-Object ProcessId,ParentProcessId,Name,ExecutablePath,@{n='CreationDate';e={$_.CreationDate.ToString('o')}},"
      "@{n='Serve8000';e={"+serve+"}},@{n='RootServe';e={$_.Name -eq 'python.exe' -and "
      "$_.CommandLine -like '*"+root+"\\.venv\\Scripts\\*' -and "+serve+"}}) -Compress")
    return select_inventory(boot.run_json([boot.PS,'-NoProfile','-NonInteractive','-Command',script],20),executable)

def eligible(rows,now):
    apps=[r for r in rows if r.get('Desktop')]
    if len(apps)!=1:return False
    started=dt.datetime.fromisoformat(apps[0]['CreationDate'])
    return (now-started).total_seconds()>=360

def may_retry(history,now):
    return sum(now-t<1800 for t in history)<2

def stop_exact(rows):
    # Snapshot identity must still match. Never taskkill /T or kill by name.
    # Each target was selected by exact desktop path/child or fixed local
    # checkout's jarvis-serve command; unrelated Python/app processes excluded.
    targets={r['ProcessId'] for r in rows}
    for row in sorted(rows,key=lambda r:(not r.get('Desktop'),r.get('ParentProcessId') not in targets)):
        target=int(row['ProcessId']); stamp=row['CreationDate'].replace("'","''")
        path=str(row['ExecutablePath']).replace("'","''")
        script=("$p=Get-CimInstance Win32_Process -Filter 'ProcessId = "+str(target)+"'; "
          "if($p -and $p.CreationDate.ToString('o') -eq '"+stamp+"' -and $p.ExecutablePath -eq '"+path+"') "
          "{Stop-Process -Id "+str(target)+" -ErrorAction Stop}; '{\"ok\":true}'")
        boot.run_json([boot.PS,'-NoProfile','-NonInteractive','-Command',script],20)

def launch_backend():
    # Use the installed environment directly: no uv sync, install or download.
    root=pathlib.Path.home()/'OpenJarvis'
    python=root/'.venv/Scripts/python.exe'
    cfg=json.loads((pathlib.Path.home()/'.openjarvis/inference.json').read_text(encoding='utf-8-sig'))
    tags={m['name'] for m in boot.get_json('http://127.0.0.1:11434/api/tags')['models']}
    if not python.is_file() or not cfg.get('confirmed') or cfg.get('model') not in tags:
        raise boot.NotReady('existing_local_backend_or_model_missing')
    # Supported Ollama environment setting, scoped to our child only. Windows
    # localhost/IPv6 fallback took >2s, exceeding the desktop's 2s attach probe.
    # Never change the user's saved configuration or global environment.
    environment=os.environ.copy()
    environment['OLLAMA_HOST']='http://127.0.0.1:11434'
    return subprocess.Popen([str(python),'-m','openjarvis.cli','serve','--host','127.0.0.1',
       '--port','8000','--engine','ollama','--model',cfg['model'],'--agent','simple'],
       cwd=root,stdin=subprocess.DEVNULL,stdout=subprocess.DEVNULL,
       stderr=subprocess.DEVNULL,creationflags=boot.FLAGS,env=environment)

def recover(executable,rows):
    if healthy() or port_open():raise boot.NotReady('recovery_precondition_changed')
    # Keep the desktop/chat window open. Stop only its verified failed backend.
    stop_exact([r for r in rows if not r.get('Desktop')])
    if port_open():raise boot.NotReady('port_claimed_by_another_process')
    launch_backend()
    return boot.wait_until(healthy,360,interval=5)

def budget_history(previous,boot_id):
    return previous.get('recovery_times',[]) if previous.get('boot_id')==boot_id else []

def save(ready,phase,history,events):
    data={'checked_at':dt.datetime.now(dt.timezone.utc).isoformat(),'watchdog_pid':os.getpid(),'openjarvis_ready':ready,
          'phase':phase,'boot_id':BOOT_ID,'recovery_times':history,'events':events[-20:],
          'scope':'Current OpenJarvis health only; startup-last.json is historical startup evidence.'}
    temp=STATE.with_suffix('.tmp');temp.write_text(json.dumps(data,indent=2));temp.replace(STATE)

def main():
    global BOOT_ID
    import msvcrt
    with (HERE/'watchdog.lock').open('a+b') as lock:
        if lock.seek(0,2)==0:lock.write(b'0');lock.flush()
        lock.seek(0)
        try:msvcrt.locking(lock.fileno(),msvcrt.LK_NBLCK,1)
        except OSError:return
        manifest=json.loads((HERE/'manifest.json').read_text(encoding='utf-8-sig'))
        executable=manifest['openjarvis'];history=[];events=[];failures=0
        bootstrap='--bootstrap' in sys.argv;ever_healthy=False
        BOOT_ID=boot.run_json([boot.PS,'-NoProfile','-NonInteractive','-Command',
          "@{boot=(Get-CimInstance Win32_OperatingSystem).LastBootUpTime.ToString('o')}|ConvertTo-Json -Compress"],20)['boot']
        if STATE.exists():
            previous=json.loads(STATE.read_text());history=budget_history(previous,BOOT_ID);events=previous.get('events',[])
        while not STOP.exists():
            try:
                ok=healthy();rows=inventory(executable);now=time.time()
                history=[t for t in history if now-t<1800]
                if ok:failures=0;phase='healthy';ever_healthy=True
                elif not rows and not bootstrap:failures=0;phase='desktop_closed_no_relaunch'
                else:
                    failures+=1;phase='unhealthy_observing'
                    if failures>=3 and (ever_healthy or bootstrap or eligible(rows,dt.datetime.now(dt.timezone.utc))):
                        if port_open():phase='unhealthy_listener_preserved'
                        elif not may_retry(history,now):phase='recovery_limit_reached'
                        else:
                            history.append(now);events.append({'time':now,'event':'confirmed_closed_port_recovery'})
                            save(False,'recovering',history,events)
                            ok=recover(executable,rows);failures=0
                            phase='recovered' if ok else 'recovery_failed'
                            events.append({'time':time.time(),'event':phase})
                save(ok,phase,history,events)
            except Exception as exc:
                # No raw stderr, command line, settings, device or exception text.
                save(False,'diagnostic_error_'+type(exc).__name__,history,events)
            time.sleep(15)
        save(healthy(),'stopped_by_marker',history,events)

if __name__=='__main__':main()
