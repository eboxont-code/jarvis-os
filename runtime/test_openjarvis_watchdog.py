import datetime as dt
import json
import pathlib
import tempfile
import unittest
from unittest.mock import patch
import openjarvis_watchdog as w

class RecoveryTests(unittest.TestCase):
    def test_venv_server_child_selected_but_unrelated_python_preserved(self):
        rows=[{'ProcessId':1,'ExecutablePath':'desktop.exe','Name':'desktop.exe'},
          {'ProcessId':2,'ExecutablePath':'venv/python.exe','Name':'python.exe','RootServe':True},
          {'ProcessId':3,'ParentProcessId':2,'ExecutablePath':'base/python.exe','Name':'python.exe','Serve8000':True},
          {'ProcessId':4,'ParentProcessId':99,'Name':'python.exe','Serve8000':True},
          {'ProcessId':5,'ParentProcessId':2,'Name':'python.exe','Serve8000':False}]
        selected=w.select_inventory(rows,'desktop.exe')
        self.assertEqual({r['ProcessId'] for r in selected},{1,2,3})

    def test_server_leaf_stops_before_venv_shim(self):
        rows=[{'ProcessId':2,'ParentProcessId':99,'CreationDate':'fixture','ExecutablePath':'parent.exe'},
              {'ProcessId':3,'ParentProcessId':2,'CreationDate':'fixture','ExecutablePath':'child.exe'}]
        with patch.object(w.boot,'run_json') as run:
            w.stop_exact(rows)
        self.assertIn('ProcessId = 3',run.call_args_list[0].args[0][-1])

    def test_startup_grace_and_ambiguous_desktops_prevent_recovery(self):
        now=dt.datetime.now(dt.timezone.utc)
        app={'Desktop':True,'CreationDate':now.isoformat()}
        self.assertFalse(w.eligible([app],now))
        app['CreationDate']=(now-dt.timedelta(seconds=361)).isoformat()
        self.assertTrue(w.eligible([app],now))
        self.assertFalse(w.eligible([app,app],now))
        self.assertFalse(w.eligible([],now))

    def test_two_recoveries_per_thirty_minutes_limit(self):
        self.assertTrue(w.may_retry([],2000))
        self.assertTrue(w.may_retry([100],2000))
        self.assertFalse(w.may_retry([1900,1950],2000))

    def test_budget_survives_guard_restart_but_resets_on_new_windows_boot(self):
        previous={'boot_id':'first','recovery_times':[1900,1950]}
        self.assertEqual(w.budget_history(previous,'first'),[1900,1950])
        self.assertEqual(w.budget_history(previous,'second'),[])

    def test_stale_or_dead_watchdog_is_not_readiness(self):
        with tempfile.TemporaryDirectory() as directory,patch.object(w.boot,'HERE',pathlib.Path(directory)):
            file=pathlib.Path(directory)/'runtime-health.json'
            data={'openjarvis_ready':True,'watchdog_pid':123,'checked_at':(dt.datetime.now(dt.timezone.utc)-dt.timedelta(seconds=65)).isoformat()}
            file.write_text(json.dumps(data))
            with patch.object(w.boot,'run_json') as run:
                self.assertFalse(w.boot.watchdog_ready());run.assert_not_called()
            data['checked_at']=dt.datetime.now(dt.timezone.utc).isoformat();file.write_text(json.dumps(data))
            with patch.object(w.boot,'run_json',return_value={'alive':False}):
                self.assertFalse(w.boot.watchdog_ready())

    def test_backend_reuses_installed_environment_and_fixed_loopback(self):
        with tempfile.TemporaryDirectory() as directory:
            home=pathlib.Path(directory);python=home/'OpenJarvis/.venv/Scripts/python.exe'
            python.parent.mkdir(parents=True);python.write_bytes(b'fixture')
            cfg=home/'.openjarvis/inference.json';cfg.parent.mkdir();cfg.write_text(json.dumps({'confirmed':True,'model':'fixture-local'}))
            with patch.object(w.pathlib.Path,'home',return_value=home),patch.object(w.boot,'get_json',return_value={'models':[{'name':'fixture-local'}]}),patch.object(w.subprocess,'Popen') as launch:
                w.launch_backend();argv=launch.call_args.args[0]
                self.assertEqual(argv[:4],[str(python),'-m','openjarvis.cli','serve'])
                self.assertEqual(argv[argv.index('--host')+1],'127.0.0.1')
                self.assertEqual(argv[argv.index('--engine')+1],'ollama')
                self.assertNotIn('uv',argv);self.assertNotIn('sync',argv)
                self.assertEqual(launch.call_args.kwargs['stderr'],w.subprocess.DEVNULL)
                self.assertEqual(launch.call_args.kwargs['env']['OLLAMA_HOST'],'http://127.0.0.1:11434')
                self.assertIsNot(launch.call_args.kwargs['env'],w.os.environ)

    def test_missing_model_prevents_backend_launch_or_download(self):
        with tempfile.TemporaryDirectory() as directory:
            home=pathlib.Path(directory);python=home/'OpenJarvis/.venv/Scripts/python.exe'
            python.parent.mkdir(parents=True);python.write_bytes(b'fixture')
            cfg=home/'.openjarvis/inference.json';cfg.parent.mkdir();cfg.write_text(json.dumps({'confirmed':True,'model':'missing-local'}))
            with patch.object(w.pathlib.Path,'home',return_value=home),patch.object(w.boot,'get_json',return_value={'models':[]}),patch.object(w.subprocess,'Popen') as launch:
                with self.assertRaises(w.boot.NotReady):w.launch_backend()
                launch.assert_not_called()

    def test_healthy_app_or_live_listener_is_never_stopped(self):
        for health,listener in [(True,False),(False,True)]:
            with patch.object(w,'healthy',return_value=health),patch.object(w,'port_open',return_value=listener),patch.object(w,'stop_exact') as stop:
                with self.assertRaises(w.boot.NotReady):w.recover('fixture',[])
                stop.assert_not_called()

    def test_new_port_owner_prevents_relaunch(self):
        with patch.object(w,'healthy',return_value=False),patch.object(w,'port_open',side_effect=[False,True]),patch.object(w,'stop_exact'),patch.object(w,'launch_backend') as launch:
            with self.assertRaises(w.boot.NotReady):w.recover('fixture',[])
            launch.assert_not_called()

    def test_desktop_is_preserved_during_backend_recovery(self):
        rows=[{'Desktop':True,'ProcessId':1},{'Desktop':False,'ProcessId':2}]
        with patch.object(w,'healthy',return_value=False),patch.object(w,'port_open',return_value=False),patch.object(w,'stop_exact') as stop,patch.object(w,'launch_backend'),patch.object(w.boot,'wait_until',return_value=True):
            w.recover('fixture',rows)
            stop.assert_called_once_with([rows[1]])

    def test_recovery_launches_once_and_wait_is_bounded(self):
        with patch.object(w,'healthy',return_value=False),patch.object(w,'port_open',return_value=False),patch.object(w,'stop_exact'),patch.object(w,'launch_backend') as launch,patch.object(w.boot,'wait_until',return_value=True) as wait:
            self.assertTrue(w.recover('fixture',[]))
            launch.assert_called_once_with()
            self.assertEqual(wait.call_args.args[1],360)

    def test_stop_uses_pid_creation_time_and_path_not_process_name(self):
        row={'ProcessId':123,'CreationDate':'2026-11-18T00:00:00+00:00','ExecutablePath':'fixture.exe','Desktop':True}
        with patch.object(w.boot,'run_json',return_value={'ok':True}) as run:
            w.stop_exact([row])
            script=run.call_args.args[0][-1]
            self.assertIn('ProcessId = 123',script)
            self.assertIn('CreationDate',script)
            self.assertIn('ExecutablePath',script)
            self.assertNotIn('taskkill',script)
            self.assertNotIn('Stop-Process -Name',script)

if __name__=='__main__':unittest.main()
