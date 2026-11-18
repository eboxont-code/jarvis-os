"""Real ASGI concurrency regression with private disposable connector/database."""
import asyncio,hashlib,pathlib,sqlite3,tempfile,time,unittest
from unittest.mock import patch
import httpx
from fastapi import FastAPI
from openjarvis.server import connectors_router as router_module
from openjarvis.core import config
from openjarvis.core.registry import ConnectorRegistry
from openjarvis.connectors import store as store_module

class FixtureConnector:
    display_name='fixture';auth_type='none'
    def knowledge_sources(self):return ('fixture',)
    def is_connected(self):time.sleep(.65);return False

class ConnectorResponsiveness(unittest.IsolatedAsyncioTestCase):
    async def test_slow_connector_does_not_block_health_and_status_reads_no_writes(self):
        with tempfile.TemporaryDirectory() as directory:
            root=pathlib.Path(directory);db=root/'knowledge.db'
            with sqlite3.connect(db) as conn:
                conn.execute('CREATE TABLE knowledge_chunks(source TEXT)')
                conn.executemany('INSERT INTO knowledge_chunks VALUES(?)',[('fixture',),('fixture',),('other',)])
            conn.close()
            before=hashlib.sha256(db.read_bytes()).hexdigest()
            original=sqlite3.connect;calls=[]
            def connect(*args,**kwargs):calls.append((str(args[0]),kwargs));return original(*args,**kwargs)
            class OldStoreFixture:
                def __init__(self):self._conn=connect(db)
                def __enter__(self):return self
                def __exit__(self,*args):self._conn.close()
            app=FastAPI()
            app.include_router(router_module.create_connectors_router())
            @app.get('/health')
            async def health():return {'status':'ok'}
            with patch.object(config,'DEFAULT_CONFIG_DIR',root),patch.object(router_module,'_ensure_connectors_registered'),patch.dict(router_module._instances,{'fixture':FixtureConnector()},clear=True),patch.object(ConnectorRegistry,'keys',return_value=['fixture']),patch.object(store_module,'KnowledgeStore',OldStoreFixture),patch.object(sqlite3,'connect',side_effect=connect):
                async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app),base_url='http://fixture') as client:
                    started=time.monotonic();request=asyncio.create_task(client.get('/v1/connectors'))
                    await asyncio.sleep(.05)
                    response=await client.get('/health');elapsed=time.monotonic()-started
                    listing=await request
                self.assertEqual(response.json(),{'status':'ok'})
                self.assertLess(elapsed,.3,'connector work blocked the event loop/health')
                self.assertEqual(listing.json()['connectors'][0]['chunks'],2)
                self.assertTrue(calls)
                self.assertTrue(all('mode=ro' in path and opts.get('uri') is True for path,opts in calls),'status must use a read-only SQLite URI')
                self.assertEqual(hashlib.sha256(db.read_bytes()).hexdigest(),before)

if __name__=='__main__':unittest.main()
