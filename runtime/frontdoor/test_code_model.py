import unittest
from unittest.mock import patch
import prepare_code_model as m

class LocalModelTests(unittest.TestCase):
    def test_absent_source_cannot_trigger_a_download(self):
        with patch.object(m,'request',return_value={'models':[]}) as request:
            with self.assertRaisesRegex(ValueError,'installed_source_required'):m.prepare()
            self.assertEqual(request.call_count,1)

    def test_existing_alias_is_preserved(self):
        with patch.object(m,'request',return_value={'models':[{'name':m.SOURCE,'digest':'a'},{'name':m.ALIAS,'digest':'b'}]}) as request:
            with self.assertRaisesRegex(ValueError,'existing_alias_preserved'):m.prepare()
            self.assertEqual(request.call_count,1)

    def test_creation_reuses_only_the_installed_source(self):
        original={'models':[{'name':m.SOURCE,'digest':'a'}]}
        after={'models':[{'name':m.SOURCE,'digest':'a'},{'name':m.ALIAS,'digest':'b'}]}
        source={'details':{'family':'qwen35'},'modelfile':'FROM existing-weight-blob'}
        alias={**source,'parameters':'num_ctx 16384'}
        with patch.object(m,'request',side_effect=[original,source,{'status':'success'},after,alias]) as request:
            self.assertEqual(m.prepare()['downloads'],0)
            self.assertEqual(request.call_args_list[2].args,('/api/create',{'model':m.ALIAS,'from':m.SOURCE,'parameters':{'num_ctx':16384},'stream':False}))

if __name__=='__main__':unittest.main()
