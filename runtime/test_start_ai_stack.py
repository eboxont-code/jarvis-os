import copy
import pathlib
import tempfile
import unittest
from unittest.mock import patch
import start_ai_stack as app

def ready():
    return {'ok':True,'schemaVersion':1,'command':'gateway-service status',
            'integration':{'kind':'isolated-session','version':1,'gatewayLaunch':{'version':1}},
            'gateway':{'state':'running','port':50368,
                       'launch':{'version':1,'attemptId':'a'*32},
                       'ownership':{'sandboxId':'fixture','agentUserSid':'fixture',
                                    'listeners':[{'port':50368,'processId':12,'sequenceNumber':2,
                                                  'processStartTimeUtc':'2026-11-18T00:00:00+00:00'}]}}}

class StartupTests(unittest.TestCase):
    def test_open_port_and_running_do_not_authorize_launch(self):
        d=ready();self.assertTrue(app.gateway_ready(d))
        for field in ['port','ownership']:
            bad=copy.deepcopy(d);del bad['gateway'][field]
            self.assertFalse(app.gateway_ready(bad))

    def test_wrong_contract_or_listener_identity_rejected(self):
        for mutate in [lambda d:d['integration'].update(version=2),
                       lambda d:d['gateway']['ownership']['listeners'][0].update(sequenceNumber=0),
                       lambda d:d['gateway']['ownership']['listeners'][0].update(processStartTimeUtc='bad'),
                       lambda d:d['gateway']['ownership']['listeners'].append(d['gateway']['ownership']['listeners'][0]),
                       lambda d:d['gateway']['launch'].update(attemptId='not-an-attempt')]:
            d=ready();mutate(d);self.assertFalse(app.gateway_ready(d))

    def test_wait_is_bounded_and_recovers_without_second_start(self):
        now=[0];calls=[]
        def sleep(s):now[0]+=s
        def check():calls.append(now[0]);return len(calls)==3
        self.assertTrue(app.wait_until(check,10,clock=lambda:now[0],sleep=sleep))
        self.assertEqual(calls,[0,4,8])
        now[0]=0
        self.assertFalse(app.wait_until(lambda:False,9,clock=lambda:now[0],sleep=sleep))
        self.assertEqual(now[0],9)

    def test_existing_app_is_not_launched_twice(self):
        with tempfile.TemporaryDirectory() as d:
            p=pathlib.Path(d)/'app.exe';p.write_bytes(b'fixture')
            with patch.object(app,'existing',return_value=True),patch.object(app.subprocess,'Popen') as launch:
                app.launch_once(p);launch.assert_not_called()

    @unittest.skipUnless(app.PS.is_file(), 'Windows process inventory integration')
    def test_native_process_inventory_is_always_a_json_list(self):
        self.assertIsInstance(app.processes(),list)

    def test_failure_log_never_copies_raw_command_output(self):
        with tempfile.TemporaryDirectory() as d,patch.object(app,'HERE',pathlib.Path(d)):
            s=app.Startup({});s.record('native_admission',False,'missing_or_invalid_native_listener_proof')
            text=(pathlib.Path(d)/'startup-last.json').read_text()
            self.assertNotIn('agentUserSid',text);self.assertNotIn('sandboxId',text)
            self.assertIn('"ready": false',text)

    def test_one_ready_component_does_not_mark_whole_stack_ready(self):
        import json
        with tempfile.TemporaryDirectory() as d,patch.object(app,'HERE',pathlib.Path(d)):
            s=app.Startup({});s.record('ollama',True)
            self.assertFalse(json.loads((pathlib.Path(d)/'startup-last.json').read_text())['ready'])

    def test_fixed_local_endpoint_whitelist(self):
        for u in ['https://example.org','http://127.0.0.1:8000/v1/chat/completions',
                  'http://127.0.0.1:50368/','http://localhost:11434/api/pull']:
            with self.assertRaises(app.NotReady):app.get_json(u)

    def test_command_failure_does_not_expose_stderr(self):
        result=app.subprocess.CompletedProcess(['fixture'],1,stdout='',stderr='password=PRIVATE_FIXTURE')
        with patch.object(app.subprocess,'run',return_value=result):
            with self.assertRaises(app.NotReady) as caught:app.run_json(['fixture'])
        self.assertEqual(str(caught.exception),'local_command_failed')

    def test_probe_failure_preserves_safe_stage_only(self):
        result=app.subprocess.CompletedProcess(['fixture'],1,stdout='{"ready":false,"stage":"mcp_live_calls","error_type":"AssertionError"}',stderr='PRIVATE_FIXTURE')
        with patch.object(app.subprocess,'run',return_value=result):
            data=app.run_json(['fixture'],accept_error_json=True)
        self.assertEqual(data['stage'],'mcp_live_calls')
        result.stdout='{"ready":false,"token":"PRIVATE_FIXTURE"}'
        with patch.object(app.subprocess,'run',return_value=result):
            with self.assertRaises(app.NotReady):app.run_json(['fixture'],accept_error_json=True)

    def test_companion_retry_preserves_apps_it_did_not_start(self):
        from unittest.mock import Mock
        child=Mock();child.poll.return_value=None
        with patch.object(app,'launch_once') as launch:
            with self.assertRaises(app.NotReady):app.retry_owned_companion('fixture',None,ready())
            bad=ready();del bad['gateway']['port']
            with self.assertRaises(app.NotReady):app.retry_owned_companion('fixture',child,bad)
            child.terminate.assert_not_called();launch.assert_not_called()

    def test_companion_retry_targets_exact_owned_handle_once(self):
        from unittest.mock import Mock
        child=Mock();child.poll.return_value=None
        with patch.object(app,'existing',return_value=False),patch.object(app,'launch_once') as launch:
            app.retry_owned_companion('fixture',child,ready())
            child.terminate.assert_called_once();child.wait.assert_called_once_with(timeout=15)
            launch.assert_called_once_with('fixture',['--background'])

    def test_missing_contract_prevents_companion_even_with_open_port(self):
        with tempfile.TemporaryDirectory() as d:
            cfg=pathlib.Path(d)/'inference.json'
            cfg.write_text('{"confirmed":true,"model":"qwen3.5:4b"}')
            manifest={'ollama':'ollama','inference_config':str(cfg)}
            s=app.Startup(manifest);broken=ready();del broken['gateway']['port']
            def api(url):
                return {'version':'fixture'} if url.endswith('version') else {'models':[{'name':'qwen3.5:4b'}]}
            with patch.object(s,'record'),patch.object(s,'status',return_value=broken),patch.object(app,'get_json',side_effect=api),patch.object(app,'launch_once') as launch,patch.object(app,'wait_until',side_effect=lambda f,*a:bool(f())):
                with self.assertRaises(app.NotReady):s.execute()
                launch.assert_called_once_with('ollama')

class DesktopAttachRegression(unittest.TestCase):
    def test_native_attach_requires_two_fast_healthy_probes(self):
        with patch.object(app,'get_json',return_value={'status':'ok'}) as get:
            self.assertTrue(app.native_attach_ready(clock=lambda:0,sleep=lambda _:None))
            self.assertEqual(get.call_count,2)

    def test_healthy_but_slow_backend_does_not_open_native_attach_gate(self):
        with patch.object(app,'get_json',return_value={'status':'ok'}):
            times=iter([0,2.06])
            self.assertFalse(app.native_attach_ready(clock=lambda:next(times),sleep=lambda _:None))

    def test_catalogue_retry_survives_timeout_before_matching_models(self):
        with tempfile.TemporaryDirectory() as directory,patch.object(app,'HERE',pathlib.Path(directory)),patch.object(app.time,'sleep'):
            s=app.Startup({});expected={'fixture'}
            with patch.object(app,'get_json',side_effect=[TimeoutError(),{'data':[]},{'data':[{'id':'fixture'}]}]) as get:
                s.required('shared_models',lambda:{r['id'] for r in app.get_json('http://127.0.0.1:8000/v1/models')['data']}==expected,120)
                self.assertEqual(get.call_count,3)
                self.assertTrue(s.checks['shared_models']['ready'])

if __name__=='__main__':unittest.main()
