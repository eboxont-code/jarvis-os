# JARVIS Local Status Report

Refresh the report with the existing Python installation:

```powershell
C:\Python314\python.exe health_report.py
```

Open `reports/jarvis-status.html` in your browser. The JSON snapshot is beside it.

The tool reads six fixed local OpenJarvis/Ollama health and model endpoints. It uses Python standard library and has $0 additional cost. Refreshing the report does not run inference.

OpenClaw/OpenCode integration evidence is a dated record from this workflow, not a live health promise. Without integration-evidence.json those entries remain unverified. Service errors are shown as unavailable.

The report is an operational health view, not a project TODO or replacement for MASTER_TODO.md.
