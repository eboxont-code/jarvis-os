@echo off
setlocal
pushd "%~dp0"
"C:\Python314\python.exe" "%~dp0health_report.py"
if errorlevel 1 (
  echo The status report could not be refreshed. Review the error above.
  pause
  popd
  exit /b 1
)
start "" "%~dp0reports\jarvis-status.html"
popd
endlocal
