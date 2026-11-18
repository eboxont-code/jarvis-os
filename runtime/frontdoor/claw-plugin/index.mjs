import fs from 'node:fs/promises';
import path from 'node:path';
import {spawn} from 'node:child_process';

// Reviewed deployment workspace, not an interpreter/runtime-path override.
export const ROOT=String.raw`C:\Users\T3-P2\Shared\jarvis-frontdoor-20261118`;
export const PYTHON=String.raw`C:\Python314\python.exe`;

export function fixedWorker(root,jid,signal,io=fs,launch=spawn){
  return new Promise((resolve,reject)=>{
    const child=launch(PYTHON,[path.join(root,'code_server.py'),'--job',jid],
      {cwd:root,shell:false,windowsHide:true,stdio:['ignore','pipe','ignore']});
    let output='',settled=false;
    const cancel=()=>{io.writeFile(path.join(root,'jobs',jid+'.cancel'),'').catch(()=>{});};
    const timer=setTimeout(()=>{cancel();child.kill();},420_000);
    signal?.addEventListener('abort',cancel,{once:true});
    const done=(err,value)=>{
      if(settled)return;settled=true;clearTimeout(timer);
      signal?.removeEventListener('abort',cancel);err?reject(err):resolve(value);
    };
    child.stdout.on('data',chunk=>{
      output+=String(chunk);
      if(output.length>128_000){cancel();child.kill();done(new Error('worker_output_limit'));}
    });
    child.on('error',()=>done(new Error('worker_launch_failed')));
    child.on('close',code=>{
      if(code!==0)return done(new Error('worker_failed'));
      try{
        const receipt=JSON.parse(output);
        if(receipt.owned_acp_process_exited!==true)throw Error('shutdown_unconfirmed');
        done(null,{receipt,owned_worker_exited:true});
      }catch{done(new Error('invalid_worker_receipt'));}
    });
  });
}

export function createHandler({root=ROOT,io=fs,run=fixedWorker,now=()=>Date.now()/1000}={}){
  const active=new Set();
  return async ({params,respond,signal,hasCurrentClientAuthority})=>{
    let jid,claimed=false;
    const authorized=()=>{signal?.throwIfAborted();if(!hasCurrentClientAuthority?.())throw Error('authorization_ended');};
    try{
      authorized();
      if(!params||Array.isArray(params)||Object.keys(params).length!==1||!Object.hasOwn(params,'job_id')||typeof params.job_id!=='string'||!/^[a-f0-9]{32}$/.test(params.job_id))throw Error('invalid_job');
      jid=params.job_id;if(active.has(jid))throw Error('duplicate_job');
      const file=path.join(root,'jobs',jid+'.json');const stat=await io.lstat(file);
      if(!stat.isFile()||stat.isSymbolicLink())throw Error('invalid_job_file');
      if(path.resolve(await io.realpath(file))!==path.resolve(file))throw Error('reparse_job_refused');
      const job=JSON.parse(await io.readFile(file,'utf8'));
      if(job.state!=='running'||job.code_allowed!==true||!Number.isFinite(job.deadline)||job.deadline<=now()||job.deadline-now()>900)throw Error('inactive_job');
      if(typeof job.project!=='string'||!/^[a-z][a-z0-9-]{0,31}$/.test(job.project))throw Error('invalid_project');
      authorized();active.add(jid);claimed=true;
      const result=await run(root,jid,signal,io);
      authorized();respond(true,{...result,delegate_version:1},undefined);
    }catch(error){
      const reason=/^[a-z_]+$/.test(String(error?.message))?error.message:'delegate_failed';
      respond(false,undefined,{code:'UNAVAILABLE',message:reason});
    }finally{if(claimed)active.delete(jid);}
  };
}

export default {
  id:'jarvis-frontdoor-bridge',name:'Guarded Jarvis delegate',
  register(api){
    api.registerGatewayMethod('jarvis.frontdoor.status',({respond})=>respond(true,{registered:true,delegate_version:1,job_id_only:true},undefined),{scope:'operator.read'});
    api.registerGatewayMethod('jarvis.frontdoor.code',createHandler(),{scope:'operator.write'});
  }
};
