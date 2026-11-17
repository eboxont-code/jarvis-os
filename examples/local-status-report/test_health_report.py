import unittest
import health_report as app

URLS={
 'http://127.0.0.1:8000/health':{'status':'ok'},
 'http://127.0.0.1:8000/v1/info':{'model':'qwen3.5:4b'},
 'http://127.0.0.1:8000/v1/models':{'data':[{'id':'qwen3.5:4b'}]},
 'http://127.0.0.1:11434/api/version':{'version':'fixture-local'},
 'http://127.0.0.1:11434/api/tags':{'models':[{'name':'qwen3.5:4b'}]},
 'http://127.0.0.1:11434/api/ps':{'models':[{'name':'qwen3.5:4b','context_length':16384}]},
}
class ReportTests(unittest.TestCase):
 def test_live_fields_and_fixed_endpoints(self):
  calls=[]
  def fetch(url):calls.append(url);return URLS[url]
  report=app.collect_status(fetch_json=fetch)
  self.assertTrue(report['openjarvis']['available']);self.assertTrue(report['ollama']['available'])
  self.assertEqual(report['openjarvis']['model'],'qwen3.5:4b')
  self.assertEqual(report['ollama']['version'],'fixture-local')
  self.assertEqual(set(calls),set(URLS));self.assertEqual(len(calls),6)
 def test_offline_safe_error(self):
  def fail(url):raise OSError('DO_NOT_LEAK_PRIVATE_ERROR')
  report=app.collect_status(fetch_json=fail)
  self.assertFalse(report['openjarvis']['available']);self.assertFalse(report['ollama']['available'])
  self.assertNotIn('DO_NOT_LEAK_PRIVATE_ERROR',app.render_html(report))
 def test_html_escapes_model_names(self):
  def fetch(url):
   if url.endswith('/v1/info'):return {'model':'<script>alert(1)</script>'}
   return URLS[url]
  page=app.render_html(app.collect_status(fetch_json=fetch))
  self.assertNotIn('<script>alert(1)</script>',page);self.assertIn('&lt;script&gt;',page)
 def test_standalone_page_and_honest_integration_labels(self):
  page=app.render_html(app.collect_status(fetch_json=URLS.__getitem__))
  for name in ('OpenJarvis','Ollama','OpenClaw','OpenCode'):self.assertIn(name,page)
  self.assertIn('<html',page.lower());self.assertNotIn('<script src=',page.lower())
  self.assertNotIn('fonts.googleapis',page.lower());self.assertNotIn('https://cdn',page.lower())
