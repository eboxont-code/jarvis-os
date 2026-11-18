import queue,unittest
from unittest.mock import Mock
from acp_client import Client

class CompletionTests(unittest.TestCase):
    def client(self):
        c=Client.__new__(Client);c.next_id=1;c.messages=queue.Queue();c.cancelled=lambda:False
        c.send=Mock();c.cancel=Mock();c.output=[];c.tool_events=[];c.tool_state={};c.denials=0
        c.completed=lambda:False
        return c
    def test_native_verified_callback_can_end_without_more_narration(self):
        c=self.client()
        c.on_tool_update=lambda client,u:u.get('kind')=='execute' and u.get('status')=='completed'
        for update in ({'sessionUpdate':'tool_call','toolCallId':'one','kind':'execute','status':'pending'},
                       {'sessionUpdate':'tool_call_update','toolCallId':'one','status':'completed'}):
            c.messages.put({'method':'session/update','params':{'update':update}})
        result=c.call('session/prompt',{},1)
        self.assertEqual(result['stopReason'],'bridge_verified');c.cancel.assert_called_once()
    def test_assistant_pass_claim_does_not_complete_a_turn(self):
        c=self.client();c.on_tool_update=lambda client,u:False
        c.messages.put({'method':'session/update','params':{'update':{'sessionUpdate':'agent_message_chunk','content':{'type':'text','text':'All tests passed'}}}})
        c.messages.put({'id':1,'result':{'stopReason':'end_turn'}})
        self.assertEqual(c.call('session/prompt',{},1)['stopReason'],'end_turn');c.cancel.assert_not_called()
    def test_independent_worker_completion_signal_stops_only_prompt(self):
        c=self.client();c.completed=lambda:True;c.on_tool_update=None
        self.assertEqual(c.call('session/prompt',{},1)['stopReason'],'bridge_verified')
        c.cancel.assert_called_once()

if __name__=='__main__':unittest.main()
