"""Read-only local status report. No services, settings or dependencies added."""
import datetime
import html
import json
import pathlib
import urllib.request

ENDPOINTS = {
    'health': 'http://127.0.0.1:8000/health',
    'info': 'http://127.0.0.1:8000/v1/info',
    'jarvis_models': 'http://127.0.0.1:8000/v1/models',
    'version': 'http://127.0.0.1:11434/api/version',
    'tags': 'http://127.0.0.1:11434/api/tags',
    'ps': 'http://127.0.0.1:11434/api/ps',
}
BASE = pathlib.Path(__file__).resolve().parent

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None

def _fetch_json(url):
    if url not in ENDPOINTS.values():
        raise ValueError('unsupported_endpoint')
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    with opener.open(url, timeout=3) as response:
        body = response.read(1_000_001)
    if len(body) > 1_000_000:
        raise ValueError('response_too_large')
    result = json.loads(body)
    if not isinstance(result, dict):
        raise ValueError('invalid_response')
    return result

def render_value(value):
    return html.escape(json.dumps(value, indent=2, ensure_ascii=False))

def collect_status(fetch_json=None):
    fetch = fetch_json or _fetch_json
    data = {}
    for key, url in ENDPOINTS.items():
        try:
            value = fetch(url)
            data[key] = value if isinstance(value, dict) else {}
        except Exception:
            data[key] = {}
    def names(items, field):
        if not isinstance(items, list):
            return []
        return sorted({item[field][:200] for item in items if isinstance(item, dict) and isinstance(item.get(field), str)})
    model = data['info'].get('model')
    version = data['version'].get('version')
    loaded = data['ps'].get('models', [])
    loaded = [{'name': x.get('name', '')[:200], 'context_length': x.get('context_length')}
              for x in loaded if isinstance(x, dict) and isinstance(x.get('name'), str)] if isinstance(loaded, list) else []
    return {
        'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'openjarvis': {'available': data['health'].get('status') == 'ok',
                      'model': model[:200] if isinstance(model, str) else 'Unavailable',
                      'models': names(data['jarvis_models'].get('data'), 'id')},
        'ollama': {'available': isinstance(version, str) and bool(version),
                   'version': version[:100] if isinstance(version, str) else 'Unavailable',
                   'models': names(data['tags'].get('models'), 'name'), 'loaded_models': loaded},
    }

def render_html(report):
    cards = []
    for label, key in [('OpenJarvis', 'openjarvis'), ('Ollama', 'ollama')]:
        section = report.get(key, {})
        state = 'Responding' if section.get('available') else 'Unavailable'
        details = render_value(section)
        cards.append(f'<section><h2>{label}</h2><strong>{state}</strong><pre>{details}</pre></section>')
    evidence = report.get('integration', {})
    for label, key in [('OpenClaw', 'openclaw'), ('OpenCode', 'opencode')]:
        proof = evidence.get(key, {}) if isinstance(evidence, dict) else {}
        state = 'Verified in the dated workflow below' if proof.get('status') == 'verified' else 'Not yet verified'
        details = render_value(proof)
        cards.append(f'<section><h2>{label}</h2><strong>{state}</strong><p>Integration evidence; not a live service check.</p><pre>{details}</pre></section>')
    checked = html.escape(str(report.get('checked_at', 'Unknown')))
    return ('<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>JARVIS Local Status</title><style>body{font:16px system-ui;background:#101724;color:#e5edf7;max-width:1100px;margin:32px auto;padding:0 20px}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px}section{background:#1c293d;padding:20px;border-radius:12px}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:13px}p{color:#b8c8df}</style>'
            f'<h1>JARVIS Local Status</h1><p>Live API checks at {checked}. Refresh with the Python script.</p><main>'
            + ''.join(cards) + '</main><p>This operational report does not replace the project MASTER_TODO.md.</p></html>')


def main():
    report = collect_status()
    proof = BASE / 'integration-evidence.json'
    if proof.exists():
        try:
            evidence = json.loads(proof.read_text(encoding='utf-8'))
            if isinstance(evidence, dict):
                report['integration'] = evidence
        except (OSError, ValueError):
            pass
    folder = BASE / 'reports'
    folder.mkdir(exist_ok=True)
    (folder / 'jarvis-status.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    (folder / 'jarvis-status.html').write_text(render_html(report), encoding='utf-8')
    print(json.dumps({'html_report':str(folder / 'jarvis-status.html'),'json_report':str(folder / 'jarvis-status.json')}))

if __name__ == '__main__':
    main()
