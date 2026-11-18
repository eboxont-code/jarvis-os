import asyncio,json,pathlib,tempfile,unittest
from unittest.mock import patch
import httpx
from fastapi import FastAPI,Request,Header,HTTPException,Depends
from openjarvis.server.routes import ChatCompletionRequest
import frontdoor,projects,verify_project

class BridgeTests(unittest.TestCase):
    def app(self):
        app=FastAPI()
        @app.post('/v1/chat/completions')
        async def original(request_body:ChatCompletionRequest,request:Request):return {'local':True}
        frontdoor.install(app);return app
    def test_launch_failure_releases_busy_lock(self):
        async def run():
            app=self.app()
            async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app),base_url='http://test') as c:
                with patch.object(frontdoor,'CONFIG',pathlib.Path('nonexistent-frontdoor-manifest')):
                    for _ in range(2):
                        r=await c.post('/v1/chat/completions',json=self.body('hello').model_dump())
                        self.assertEqual(r.status_code,503)
        asyncio.run(run())
    def test_real_stream_shape_with_owned_worker_result(self):
        class Process:
            def poll(self):return 0
        with tempfile.TemporaryDirectory() as d:
            root=pathlib.Path(d);config=root/'frontdoor.json';config.write_text(json.dumps({'shared':str(root),'clawctl':'fixture'}))
            def start(*args,**kwargs):
                jid=next((root/'jobs').glob('*.json')).stem
                (root/'jobs'/(jid+'.result.json')).write_text(json.dumps({'message':'ROUNDTRIP_FIXTURE_OK'}))
                return Process()
            async def run():
                async with httpx.AsyncClient(transport=httpx.ASGITransport(app=self.app()),base_url='http://test') as c:
                    b=self.body('hello');b.stream=True
                    with patch.object(frontdoor,'CONFIG',config),patch.object(frontdoor.subprocess,'Popen',side_effect=start) as launch:
                        r=await c.post('/v1/chat/completions',json=b.model_dump())
                        self.assertIn('ROUNDTRIP_FIXTURE_OK',r.text);self.assertIn('data: [DONE]',r.text)
                        self.assertEqual(launch.call_count,1)
            asyncio.run(run())
    def body(self,text):return ChatCompletionRequest(model='test',messages=[{'role':'user','content':text}])
    def test_credentials_rejected(self):
        with self.assertRaises(HTTPException):frontdoor.messages_for(self.body('api_key=abcdefghijklmnopqrstuvwxyz'))
    def test_context_bound(self):
        with self.assertRaises(HTTPException):frontdoor.messages_for(self.body('x'*18001))
    def test_worker_record_blocks_duplicates_even_after_deadline(self):
        with tempfile.TemporaryDirectory() as directory:
            root=pathlib.Path(directory);p=root/('d'*32+'.json')
            p.write_text(json.dumps({'state':'running','deadline':0}))
            self.assertTrue(frontdoor.unfinished_job(root))
            p.write_text(json.dumps({'state':'finished'}))
            self.assertFalse(frontdoor.unfinished_job(root))
    def test_coding_intent(self):
        self.assertTrue(frontdoor.CODING.search('Fix the Python function'))
        self.assertTrue(frontdoor.CODING.search('Use OpenCode to repair this project'))
        self.assertTrue(frontdoor.CODING.search('Build a website'))
        self.assertFalse(frontdoor.CODING.search('What is two plus two?'))
    def test_project_paths(self):
        for value in ('../outside','C:/Users','CON','a/b','x'*33):
            with self.assertRaises(ValueError):projects.project_path(value)
    def test_no_code_claim_invented(self):
        text=frontdoor.receipt_text({'message':'ordinary answer'})
        self.assertEqual(text,'ordinary answer')
        failed=frontdoor.receipt_text({'code':{'status':'failed','project':'fixture'}})
        self.assertIn('Files changed: not recorded',failed)
        self.assertIn('Tests: not recorded',failed)
    def test_verifier_refuses_io_and_dynamic_access(self):
        with tempfile.TemporaryDirectory() as directory:
            root=pathlib.Path(directory);file=root/'test.py'
            for source in ('import os\nos.system("echo unsafe")','open("outside")','getattr(str,"format")','x.__class__','import socket'):
                file.write_text(source)
                with patch.object(verify_project,'ROOT',root),self.assertRaises(ValueError):verify_project.validate([file])
    def test_auth_dependency_preserved_and_local_route(self):
        async def check(authorization:str=Header(default='')):
            if authorization!='local-test':raise HTTPException(401,'required')
        app=FastAPI()
        @app.post('/v1/chat/completions',dependencies=[Depends(check)])
        async def original(request_body:ChatCompletionRequest,request:Request):
            return {'local':request_body.messages[-1].content}
        frontdoor.install(app)
        async def run():
            async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app),base_url='http://test') as c:
                body=self.body('/local hello').model_dump()
                a=await c.post('/v1/chat/completions',json=body)
                b=await c.post('/v1/chat/completions',json=body,headers={'authorization':'local-test'})
                self.assertEqual(a.status_code,401);self.assertEqual(b.json(),{'local':'hello'})
        asyncio.run(run())

if __name__=='__main__':unittest.main()
