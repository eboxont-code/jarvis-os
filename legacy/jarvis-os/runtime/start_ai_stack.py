"""Normal-user, local-only, bounded startup for the existing JARVIS apps.

No inference, installs, configuration edits or credential exports. A failed
Companion launched by this worker may receive one ownership-gated client retry.
Runtime readiness is not project status; MASTER_TODO.md remains authoritative.
"""
import datetime as dt
import json
import os
import pathlib
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
FLAGS = getattr(subprocess, 'CREATE_NO_WINDOW', 0)
PS = pathlib.Path(os.environ.get('SystemRoot', r'C:\Windows')) / 'System32/WindowsPowerShell/v1.0/powershell.exe'

class NotReady(RuntimeError):
    pass

def run_json(args, timeout=25, accept_error_json=False):
    p = subprocess.run([str(a) for a in args], capture_output=True, timeout=timeout,
                       encoding='utf-8-sig', creationflags=FLAGS)
    if p.returncode and not accept_error_json:
        raise NotReady('local_command_failed')
    try:
        value=json.loads(p.stdout)
        if p.returncode and (not isinstance(value,dict) or value.get('ready') is not False
                             or not set(value)<= {'ready','error_type','stage'}):
            raise NotReady('local_command_failed')
        return value
    except ValueError:
        raise NotReady('local_command_invalid_json') from None

def gateway_ready(doc):
    """Only gate a launch; Companion still performs its own native authorization."""
    try:
        g = doc['gateway']; i = doc['integration']; own = g['ownership']
        if not (doc['ok'] is True and doc['schemaVersion'] == 1
                and doc['command'] == 'gateway-service status'
                and i['kind'] == 'isolated-session' and i['version'] == 1
                and g['state'] == 'running' and g['port'] == 18789
                and own['sandboxId'] and own['agentUserSid']):
            return False
        if 'gatewayLaunch' in i:
            if i['gatewayLaunch']['version'] != 1 or g['launch']['version'] != 1:
                return False
            if not re.fullmatch('[a-f0-9]{32}', g['launch']['attemptId']):
                return False
        matches = [r for r in own['listeners'] if r['port'] == 18789]
        if len(matches) != 1:
            return False
        r = matches[0]
        return (type(r['processId']) is int and r['processId'] > 0
                and type(r['sequenceNumber']) is int and r['sequenceNumber'] > 0
                and dt.datetime.fromisoformat(r['processStartTimeUtc']).tzinfo is not None)
    except (KeyError, TypeError, ValueError):
        return False

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None

def get_json(url):
    if url not in {
        'http://127.0.0.1:11434/api/version', 'http://127.0.0.1:11434/api/tags',
        'http://127.0.0.1:8000/health', 'http://127.0.0.1:8000/v1/models',
    }:
        raise NotReady('endpoint_not_allowed')
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    with opener.open(url, timeout=3) as response:
        raw = response.read(1_000_001)
    if len(raw) > 1_000_000:
        raise NotReady('response_too_large')
    return json.loads(raw)

def wait_until(check, seconds, interval=4, clock=time.monotonic, sleep=time.sleep):
    end = clock() + seconds
    while True:
        try:
            if check():
                return True
        except (OSError, ValueError, NotReady, subprocess.TimeoutExpired):
            pass
        remaining = end - clock()
        if remaining <= 0:
            return False
        sleep(min(interval, remaining))

def processes():
    # Select only metadata; never return command lines or settings.
    command = ('ConvertTo-Json -InputObject @(Get-CimInstance Win32_Process | Where-Object { $_.Name -in '
               '"ollama app.exe","ollama.exe","openjarvis-desktop.exe",'
               '"OpenClaw.Tray.WinUI.exe","OpenCode.exe","opencode.exe" } | '
               'Select-Object ProcessId,Name,ExecutablePath) -Compress')
    rows = run_json([PS, '-NoProfile', '-NonInteractive', '-Command', command])
    return rows if isinstance(rows, list) else [rows] if rows else []

def existing(path):
    return any(str(r.get('ExecutablePath', '')).casefold() == str(path).casefold()
               for r in processes())

def launch_once(path, args=()):
    path = pathlib.Path(path)
    if not path.is_file():
        raise NotReady('installed_application_missing')
    if not existing(path):
        return subprocess.Popen([str(path), *args], cwd=path.parent, stdin=subprocess.DEVNULL,
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                                creationflags=FLAGS)
    return None

def watchdog_ready():
    try:
        d=json.loads((HERE/'runtime-health.json').read_text())
        age=(dt.datetime.now(dt.timezone.utc)-dt.datetime.fromisoformat(d['checked_at'])).total_seconds()
        pid=d['watchdog_pid']
        if d.get('openjarvis_ready') is not True or not 0<=age<60 or type(pid) is not int or pid<=0:
            return False
        path=str(HERE/'openjarvis_watchdog.py').replace("'","''")
        command=("$p=Get-CimInstance Win32_Process -Filter 'ProcessId = "+str(pid)+"'; "
          "@{alive=([bool]($p -and $p.Name -eq 'pythonw.exe' -and $p.CommandLine -like '*"+path+"*'))}|ConvertTo-Json -Compress")
        return run_json([PS,'-NoProfile','-NonInteractive','-Command',command],20).get('alive') is True
    except (OSError,ValueError,KeyError,TypeError,NotReady,subprocess.TimeoutExpired):return False

def native_attach_ready(clock=time.monotonic,sleep=time.sleep):
    # Actual desktop 1.0.5 performs two health probes with a two-second timeout.
    # Keep one second of headroom; don't open a second would-be server when the
    # healthy API is too slow for native attach. No setup/security bypass.
    for index in range(2):
        started=clock()
        if get_json('http://127.0.0.1:8000/health').get('status')!='ok' or clock()-started>=1:
            return False
        if index==0:sleep(.5)
    return True

def retry_owned_companion(path, child, current_gateway):
    # A retained Popen handle identifies our exact process, even if PIDs recycle.
    # Never restart a previously running app, a replacement, or an unverified
    # Gateway. No Gateway lifecycle/pairing/credential/configuration operation.
    if child is None:
        raise NotReady('existing_companion_preserved')
    if not gateway_ready(current_gateway):
        raise NotReady('companion_retry_missing_ownership_proof')
    if child.poll() is None:
        child.terminate()
        child.wait(timeout=15)
    if existing(path):
        raise NotReady('replacement_companion_preserved')
    return launch_once(path, ['--background'])

def host_opencode_local(config):
    try:
        d = json.loads(pathlib.Path(config).read_text(encoding='utf-8-sig'))
        p = d.get('provider', {})
        return (set(p) == {'ollama'} and d.get('enabled_providers') == ['ollama']
                and str(d.get('model', '')).startswith('ollama/')
                and urllib.parse.urlparse(p['ollama']['options']['baseURL']).hostname
                    in {'127.0.0.1', 'localhost', '::1'})
    except (OSError, ValueError, KeyError, TypeError):
        return False

class Startup:
    def __init__(self, manifest):
        self.m = manifest
        self.checks = {}
        self.started = time.monotonic()

    def record(self, phase, ready, detail=''):
        self.checks[phase] = {'ready': bool(ready), 'detail': detail,
                              'elapsed_seconds': round(time.monotonic() - self.started, 1)}
        doc = {'checked_at': dt.datetime.now(dt.timezone.utc).isoformat(),
               'ready': self.checks.get('complete', {}).get('ready') is True
                        and all(v['ready'] for v in self.checks.values()),
               'checks': self.checks,
               'scope': 'Startup runtime checks only; no inference or reboot acceptance claim.'}
        target = HERE / 'startup-last.json'; temp = target.with_suffix('.tmp')
        temp.write_text(json.dumps(doc, indent=2), encoding='utf-8')
        temp.replace(target)

    def required(self, phase, check, seconds, detail=''):
        self.record(phase, False, 'waiting')
        if not wait_until(check, seconds):
            reason=detail or self.checks[phase]['detail']
            self.record(phase, False, reason if reason not in ('','waiting') else 'deadline_exceeded')
            raise NotReady(phase)
        self.record(phase, True)

    def status(self):
        return run_json([self.m['clawctl'], 'gateway-service', 'status', '--json'], 20)

    def probe(self, phase):
        # Fixed project helper and fixed phase; no secrets passed in arguments.
        if phase not in {'health', 'connections', 'node'}:
            raise NotReady('invalid_probe')
        quoted = self.m['isolated_probe'].replace("'", "''")
        command = "& 'C:\\Python314\\python.exe' '" + quoted + "' " + phase
        result=run_json([self.m['clawctl'], 'pwsh', '--command', command], 75, accept_error_json=True)
        if result.get('ready') is False:
            stage=result.get('stage','probe_not_ready')
            if not re.fullmatch('[a-z_]+',stage):stage='probe_not_ready'
            field={'health':'gateway_authenticated','connections':'mcp_acp_bindings','node':'companion_node'}[phase]
            self.record(field,False,stage)
        return result

    def execute(self):
        launch_once(self.m['ollama'])
        self.required('ollama', lambda: bool(get_json('http://127.0.0.1:11434/api/version').get('version')), 90)
        tags = {m['name'] for m in get_json('http://127.0.0.1:11434/api/tags')['models']}
        cfg = json.loads(pathlib.Path(self.m['inference_config']).read_text(encoding='utf-8-sig'))
        if not cfg.get('confirmed') or cfg.get('model') not in tags or 'qwen3.5:4b' not in tags:
            raise NotReady('existing_model_confirmation_failed')

        try:
            current = self.status()
        except (NotReady, subprocess.TimeoutExpired):
            current = {}
        state = current.get('gateway', {}).get('state')
        if state in {'not-started', 'stopped'}:
            # One supported start; a caller timeout never triggers a second start.
            try:
                run_json([self.m['clawctl'], 'gateway-service', 'start', '--json'], 120)
            except (NotReady, subprocess.TimeoutExpired):
                pass
        elif state not in {'starting', 'running'}:
            raise NotReady('gateway_state_not_startable')
        self.required('gateway_contract', lambda: gateway_ready(self.status()), 300,
                      'missing_or_invalid_native_listener_proof')
        self.required('gateway_authenticated', lambda: self.probe('health').get('ready') is True, 100)

        # A separate locked normal-user watchdog provides ongoing health and
        # bounded closed-port recovery after this one-time startup exits.
        watchdog=HERE/'openjarvis_watchdog.py'
        if not watchdog.is_file():
            raise NotReady('watchdog_missing')
        if (HERE/'watchdog.stop').exists():
            raise NotReady('watchdog_deliberately_paused')
        subprocess.Popen([str(pathlib.Path(sys.executable).with_name('pythonw.exe')),str(watchdog),'--bootstrap'],
                         cwd=HERE,stdin=subprocess.DEVNULL,stdout=subprocess.DEVNULL,
                         stderr=subprocess.DEVNULL,creationflags=FLAGS)
        self.required('openjarvis', lambda: get_json('http://127.0.0.1:8000/health').get('status') == 'ok', 360)
        self.required('openjarvis_watchdog',watchdog_ready,60)
        self.required('desktop_attach_ready',native_attach_ready,90,
                      'api_too_slow_for_native_two_second_attach')
        # Start the preserved desktop only after a healthy backend exists;
        # its normal attach path avoids a second backend/dependency-sync launch.
        launch_once(self.m['openjarvis'])
        self.required('shared_models',lambda: {r['id'] for r in
                      get_json('http://127.0.0.1:8000/v1/models')['data']}==tags,120,
                      'model_catalogue_timeout_or_mismatch')
        self.required('mcp_acp_bindings', lambda: self.probe('connections').get('ready') is True, 240)

        # The ACP handshake probe is now closed. Recheck actual package proof
        # twice before Companion starts; an open TCP port alone is insufficient.
        self.required('native_admission', lambda: gateway_ready(self.status()), 100)
        time.sleep(3)
        if not gateway_ready(self.status()):
            raise NotReady('native_admission_changed')
        owned_companion=launch_once(self.m['companion'], ['--background'])
        try:
            self.required('companion_node', lambda: self.probe('node').get('ready') is True, 90,
                          'saved_node_did_not_connect')
        except NotReady:
            self.record('companion_retry', False, 'one_launcher_owned_client_retry')
            retry_owned_companion(self.m['companion'],owned_companion,self.status())
            self.required('companion_node', lambda: self.probe('node').get('ready') is True, 150,
                          'saved_node_did_not_connect_no_further_retry')
            self.record('companion_retry', True, 'one_client_retry_gateway_unchanged')

        if not host_opencode_local(self.m['opencode_config']):
            raise NotReady('opencode_local_provider_check_failed')
        launch_once(self.m['opencode'])
        self.required('opencode_desktop', lambda: existing(self.m['opencode']), 60)
        self.record('complete', True, 'existing_apps_and_saved_runtime_connections_ready')

def main():
    import msvcrt
    # An OS-held lock prevents duplicate launchers; no stale-file cleanup.
    lock = (HERE / 'startup.lock').open('a+b')
    lock.seek(0); lock.write(b'0'); lock.flush(); lock.seek(0)
    try:
        msvcrt.locking(lock.fileno(), msvcrt.LK_NBLCK, 1)
    except OSError:
        return 0
    startup = None
    try:
        m = json.loads((HERE / 'manifest.json').read_text(encoding='utf-8-sig'))
        startup = Startup(m)
        startup.execute()
        return 0
    except Exception as exc:
        # No exception text/stdout/stderr/settings can leak into the boot log.
        if startup:
            code = str(exc) if isinstance(exc, NotReady) else type(exc).__name__
            startup.record('complete', False, code if re.fullmatch('[a-zA-Z0-9_]+', code) else 'startup_failed')
        return 1
    finally:
        lock.close()

if __name__ == '__main__':
    raise SystemExit(main())
