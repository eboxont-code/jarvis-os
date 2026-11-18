import test from 'node:test';
import assert from 'node:assert/strict';
import {EventEmitter} from 'node:events';
import path from 'node:path';
import plugin,{createHandler,fixedWorker,PYTHON} from './index.mjs';
const jid='a'.repeat(32),root=String.raw`C:\test-bridge`;
function fixture(job={state:'running',code_allowed:true,deadline:160,project:'invoice-final'}){
  let runs=0;const results=[];
  const io={lstat:async()=>({isFile:()=>true,isSymbolicLink:()=>false}),realpath:async p=>p,readFile:async()=>JSON.stringify(job)};
  const handler=createHandler({root,io,now:()=>100,run:async()=>{runs++;return {receipt:{status:'candidate'},owned_worker_exited:true};}});
  return {handler,results,get runs(){return runs;},invoke:params=>handler({params,respond:(...x)=>results.push(x),hasCurrentClientAuthority:()=>true})};
}
test('only reviewed read/write RPC methods register',()=>{
  const rows=[];plugin.register({registerGatewayMethod:(...x)=>rows.push(x)});
  assert.deepEqual(rows.map(x=>[x[0],x[2].scope]),[['jarvis.frontdoor.status','operator.read'],['jarvis.frontdoor.code','operator.write']]);
});
test('valid job dispatches once and returns its owned receipt',async()=>{
  const f=fixture();await f.invoke({job_id:jid});assert.equal(f.runs,1);assert.equal(f.results[0][0],true);
});
test('paths, commands, prompts and unknown arguments are refused',async()=>{
  for(const params of [{job_id:'../outside'},{job_id:jid,command:'anything'},{job_id:jid,task:'private'}]){
    const f=fixture();await f.invoke(params);assert.equal(f.runs,0);assert.equal(f.results[0][0],false);
  }
});
test('inactive/noncoding jobs cannot spawn',async()=>{
  for(const job of [{state:'pending',code_allowed:true,deadline:160,project:'x'},{state:'running',code_allowed:false,deadline:160,project:'x'},{state:'running',code_allowed:true,deadline:99,project:'x'}]){
    const f=fixture(job);await f.invoke({job_id:jid});assert.equal(f.runs,0);
  }
});
test('ended operator authority cannot dispatch',async()=>{
  const f=fixture();await f.handler({params:{job_id:jid},respond:(...x)=>f.results.push(x),hasCurrentClientAuthority:()=>false});assert.equal(f.runs,0);
});
test('a refused duplicate cannot release the original running claim',async()=>{
  let release,runs=0;const wait=new Promise(resolve=>release=resolve),results=[];
  const io={lstat:async()=>({isFile:()=>true,isSymbolicLink:()=>false}),realpath:async p=>p,readFile:async()=>JSON.stringify({state:'running',code_allowed:true,deadline:160,project:'x'})};
  const h=createHandler({root,io,now:()=>100,run:async()=>{runs++;await wait;return {};}});
  const request=()=>h({params:{job_id:jid},respond:(...x)=>results.push(x),hasCurrentClientAuthority:()=>true});
  const first=request();await new Promise(resolve=>setImmediate(resolve));
  await request();await request();assert.equal(runs,1);release();await first;
});
test('fixed launch contains only interpreter, reviewed script and validated job id',async()=>{
  const child=new EventEmitter();child.stdout=new EventEmitter();child.kill=()=>{};let launchArgs;
  const work=fixedWorker(root,jid,undefined,{writeFile:async()=>{}},(...args)=>{launchArgs=args;return child;});
  child.stdout.emit('data',JSON.stringify({owned_acp_process_exited:true,status:'candidate'}));child.emit('close',0);
  assert.equal((await work).owned_worker_exited,true);
  assert.equal(launchArgs[0],PYTHON);assert.deepEqual(launchArgs[1],[path.join(root,'code_server.py'),'--job',jid]);assert.equal(launchArgs[2].shell,false);
});
test('an unconfirmed worker shutdown is never reported as success',async()=>{
  const child=new EventEmitter();child.stdout=new EventEmitter();child.kill=()=>{};
  const work=fixedWorker(root,jid,undefined,{writeFile:async()=>{}},()=>child);
  child.stdout.emit('data','{}');child.emit('close',0);await assert.rejects(work,/invalid_worker_receipt/);
});
