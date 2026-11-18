"""Fixed-loopback, concurrent connector status/health evidence; no contents."""
import concurrent.futures,json,time,urllib.request
opener=urllib.request.build_opener(urllib.request.ProxyHandler({}))
def fetch(path):
    start=time.monotonic()
    with opener.open('http://127.0.0.1:8000'+path,timeout=25) as r:
        d=json.loads(r.read(1_000_000))
    return d,time.monotonic()-start
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
    future=pool.submit(fetch,'/v1/connectors')
    samples=[]
    for _ in range(5):
        data,elapsed=fetch('/health');assert data.get('status')=='ok'
        samples.append(round(elapsed,3));time.sleep(.1)
    data,elapsed=future.result(timeout=30)
result={'connector_status_ok':isinstance(data.get('connectors'),list),'connector_count':len(data.get('connectors',[])),
        'connector_seconds':round(elapsed,3),'concurrent_health_seconds':samples}
assert result['connector_status_ok'] and max(samples)<3
print(json.dumps(result))
