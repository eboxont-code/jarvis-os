import copy,pathlib,sys,unittest
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent.parent))
from isolated_readiness_probe import local_provider_policy

class LocalProviderTests(unittest.TestCase):
    def config(self):return {'models':{'providers':{'ollama':{'baseUrl':'http://127.0.0.1:11434'},'jarvis-local':{'api':'ollama','baseUrl':'http://127.0.0.1:11434','models':[{'id':'qwen3.8:27b','contextTokens':16384,'params':{'num_ctx':16384,'think':False}}]}}}}
    def test_existing_local_provider_and_exact_bridge_alias(self):
        c=self.config();self.assertTrue(local_provider_policy(c));del c['models']['providers']['jarvis-local'];self.assertTrue(local_provider_policy(c))
    def test_remote_and_unrecognised_providers_are_denied(self):
        for key,url in [('jarvis-local','https://example.com'),('paid-cloud','http://127.0.0.1:11434')]:
            c=self.config();c['models']['providers'][key]={'baseUrl':url}
            with self.assertRaises(AssertionError):local_provider_policy(c)
    def test_alias_cannot_expand_context_or_change_protocol(self):
        for key,value in [('api','openai-completions'),('baseUrl','http://127.0.0.1:9999')]:
            c=self.config();c['models']['providers']['jarvis-local'][key]=value
            with self.assertRaises(AssertionError):local_provider_policy(c)
        c=self.config();c['models']['providers']['jarvis-local']['models'][0]['params']['think']=True
        with self.assertRaises(AssertionError):local_provider_policy(c)

if __name__=='__main__':unittest.main()
