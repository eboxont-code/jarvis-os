import json,pathlib,tempfile,time,threading,unittest
from unittest.mock import patch
import code_server as c

class CodeGuardTests(unittest.TestCase):
    def test_inactive_or_non_coding_jobs_cannot_delegate(self):
        with tempfile.TemporaryDirectory() as d:
            root=pathlib.Path(d);jid='c'*32;file=root/(jid+'.json')
            with patch.object(c,'JOBS',root):
                for job in ({'state':'pending','deadline':time.time()+60,'code_allowed':True},{'state':'running','deadline':time.time()+60,'code_allowed':False},{'state':'running','deadline':0,'code_allowed':True}):
                    file.write_text(json.dumps(job))
                    with self.assertRaises(ValueError):c.approved_job(jid)
    def test_arguments_do_not_expose_commands_or_paths(self):
        with self.assertRaises(ValueError):c.code_task({'job_id':'c'*32,'project':'main','task':'hello','command':'arbitrary'},threading.Event())
        self.assertEqual(set(c.TOOL['inputSchema']['properties']),{'job_id','project','task'})
    def test_unknown_tools_refused(self):
        output=[]
        with patch.object(c,'emit',side_effect=output.append):c.respond_call({'id':42,'params':{'name':'exec','arguments':{}}},threading.Event())
        self.assertTrue(output[0]['result']['isError'])
    def test_credentials_refused_before_job_or_project_access(self):
        with patch.object(c,'approved_job') as approved:
            with self.assertRaises(ValueError):c.code_task({'job_id':'c'*32,'project':'main','task':'password=abcdefghijklmnopqrstuvwxyz'},threading.Event())
            approved.assert_not_called()

if __name__=='__main__':unittest.main()
