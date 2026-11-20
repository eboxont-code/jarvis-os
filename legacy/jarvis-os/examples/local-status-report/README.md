> **Archived wiped install.** This file is not current setup. The Windows install it describes has been removed. Nothing here is installed, enabled, connected, configured, paired, running, or done. Checked boxes, version numbers, and pairing notes below are historical and do not apply. Follow the fresh-install guide in the repository root `README.md`, and use the root `REQUIREMENTS.md` as the checklist.

# JARVIS Local Status Report

After Python is installed, refresh the report:

```powershell
C:\Python314\python.exe health_report.py
```

Open `reports/jarvis-status.html` in your browser. The JSON snapshot is beside it.

The tool reads six fixed local OpenJarvis/Ollama health and model endpoints. It uses Python standard library and has $0 additional cost. Refreshing the report does not run inference.

OpenClaw/OpenCode integration evidence is a dated record from this workflow, not a live health promise. Without integration-evidence.json those entries remain unverified. Service errors are shown as unavailable.

The report is an operational health view, not a project TODO or replacement for MASTER_TODO.md.
