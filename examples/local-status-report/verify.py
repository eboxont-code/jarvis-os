import io,json,sys,unittest
sys.dont_write_bytecode=True
suite=unittest.defaultTestLoader.discover('.',pattern='test_health_report.py')
buffer=io.StringIO()
result=unittest.TextTestRunner(stream=buffer,verbosity=1).run(suite)
ok=result.wasSuccessful() and result.testsRun==4
print(json.dumps({'passed':ok,'exit_code':0 if ok else 1,'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors)}))
if not ok:print(buffer.getvalue())
sys.exit(0 if ok else 1)
