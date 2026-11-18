import unittest,tempfile,pathlib,time
from unittest.mock import patch
import gateway_job as g
from gateway_job import direct_coding_request,selected_project
class DirectRouterTests(unittest.TestCase):
    def job(self,text,allowed=True):return {'code_allowed':allowed,'messages':[{'role':'user','content':text}]}
    def test_explicit_coding_routes_without_an_extra_manager_model(self):
        self.assertTrue(direct_coding_request(self.job('Use OpenCode to fix project invoice-final')))
        self.assertTrue(direct_coding_request(self.job('Build a Python calculator')))
        self.assertFalse(direct_coding_request(self.job('Explain this Python function')))
        self.assertFalse(direct_coding_request(self.job('Fix the desktop',False)))
    def test_only_owned_slug_project_is_selected(self):
        self.assertEqual(selected_project('Fix project invoice-final.'),'invoice-final')
        self.assertEqual(selected_project('Fix project invoice-final: add tax'),'invoice-final')
        self.assertEqual(selected_project('Build a calculator'),'main')
        for text in ('Fix project C:\\outside','Fix project x/outside'):
            with self.assertRaises(ValueError):selected_project(text)
    def test_native_path_calls_gateway_once_and_returns_its_verified_receipt(self):
        with tempfile.TemporaryDirectory() as d,patch.object(g,'JOBS',pathlib.Path(d)),patch.object(g,'rpc',return_value={'owned_worker_exited':True,'receipt':{'status':'candidate','project':'main','owned_acp_process_exited':True}}) as rpc,patch.object(g,'finish_receipt',return_value={'status':'passed','verification':{'passed':True,'tests_run':3}}):
            job=self.job('Use OpenCode to fix this Python function');job['deadline']=time.time()+60
            r=g.direct_run('a'*32,job)
            self.assertTrue(r['gateway_acknowledged']);self.assertEqual(r['code']['status'],'passed')
            self.assertEqual(rpc.call_count,1);self.assertEqual(rpc.call_args.args[0],'jarvis.frontdoor.code')
    def test_unavailable_delegate_has_no_retry_or_model_fallback(self):
        with tempfile.TemporaryDirectory() as d,patch.object(g,'JOBS',pathlib.Path(d)),patch.object(g,'rpc',side_effect=RuntimeError('unavailable')) as rpc:
            job=self.job('Use OpenCode to fix this Python function');job['deadline']=time.time()+60
            r=g.direct_run('a'*32,job);self.assertEqual(r['status'],'failed');self.assertEqual(rpc.call_count,1)
    def test_missing_verifier_preserves_the_actual_worker_failure(self):
        with tempfile.TemporaryDirectory() as d,patch.object(g,'JOBS',pathlib.Path(d)),patch.object(g,'code_evidence',return_value=None):
            receipt={'project':'main','native_session_id':'ses_fixture','reason':'deadline_exceeded'}
            result=g.finish_receipt('a'*32,receipt)
            self.assertEqual(result['status'],'failed')
            self.assertEqual(result['reason'],'deadline_exceeded')
            self.assertEqual(result['verification_reason'],'native_verifier_evidence_missing')
if __name__=='__main__':unittest.main()
