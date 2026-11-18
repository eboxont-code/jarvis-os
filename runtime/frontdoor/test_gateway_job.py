import json,pathlib,tempfile,time,unittest
from unittest.mock import patch
import gateway_job as g

class WorkerTests(unittest.TestCase):
    def test_rejects_non_job_path(self):
        with self.assertRaises(ValueError):g.run('../config')
    def test_polls_then_returns_only_assistant_text(self):
        with tempfile.TemporaryDirectory() as d:
            root=pathlib.Path(d);jid='a'*32
            (root/(jid+'.json')).write_text(json.dumps({'state':'pending','deadline':time.time()+60,'code_allowed':False,'messages':[{'role':'user','content':'hello'}]}))
            calls=[]
            def rpc(method,params):
                calls.append((method,params))
                if method=='chat.send':return {'runId':'own'}
                if method=='agent.wait':return {'status':'ok','endedAt':123}
                if method=='sessions.get':return {'messages':[{'role':'user','content':'private prompt'},{'role':'assistant','content':[{'type':'thinking','thinking':'private'},{'type':'text','text':'Hello'}]}]}
                raise AssertionError(method)
            with patch.object(g,'JOBS',root),patch.object(g,'rpc',side_effect=rpc):result=g.run(jid)
            self.assertEqual(result['message'],'Hello')
            self.assertEqual(json.loads((root/(jid+'.json')).read_text())['state'],'finished')
            self.assertEqual(calls[0][1]['sessionKey'],'agent:jarvis-frontdoor:bridge-'+jid)
    def test_cancel_targets_only_own_run(self):
        with tempfile.TemporaryDirectory() as d:
            root=pathlib.Path(d);jid='b'*32
            (root/(jid+'.json')).write_text(json.dumps({'state':'pending','deadline':time.time()+60,'code_allowed':False,'messages':[]}))
            (root/(jid+'.cancel')).touch();calls=[]
            def rpc(method,params):
                calls.append((method,params));return {'runId':'only-own-run','session':{'hasActiveRun':False}}
            with patch.object(g,'JOBS',root),patch.object(g,'rpc',side_effect=rpc):r=g.run(jid)
            self.assertEqual(r['status'],'cancelled')
            self.assertIn(('chat.abort',{'sessionKey':'agent:jarvis-frontdoor:bridge-'+jid,'runId':'only-own-run'}),calls)

if __name__=='__main__':unittest.main()
