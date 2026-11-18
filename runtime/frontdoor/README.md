# OpenJarvis front-door adapter

Implementation and operational records only. The root MASTER_TODO.md is the sole project-status authority. Read the dated front-door handoff before deployment; scripts contain this machine's verified paths and are not portable installers.

Ordinary OpenJarvis text chat enters one restricted OpenClaw coordinator. It can answer using the existing local Ollama model, call three read-only service-status tools, or delegate one coding job through `jarvis-code` MCP to the installed OpenCode ACP executable. Results return to the same OpenJarvis conversation. `/local ` uses the original OpenJarvis chat route; requests with client tools retain their native route.

The in-process addon replaces only the existing chat route callable, retaining the original app's middleware/authentication and route dependencies. The original checkout is preserved. The project watchdog launches `backend_bootstrap.py` only when its adjacent `frontdoor.json` manifest exists; otherwise it uses the original installed CLI.

The isolated account holds `gateway_job.py`, `code_server.py`, `acp_client.py`, `projects.py`, `verify_project.py`, its coordinator workspace and operational job receipts. Prompts stay local. Never upload job inputs, complete active configuration, diagnostic ZIPs or private backups.

Coding is limited to bridge-owned projects, source/tests/README edits and one exact verifier command. It has no general shell, installer, network, browser, external-directory or messaging grant. The verifier executes a restricted pure-Python subset under process/time/memory limits; it is not a general operating-system sandbox. Broader programs require separately reviewed permissions. Test results and protected hashes are checked independently of model prose.

Each request gets a new isolated session with bounded conversation context, one coding claim and a deadline. Cancellation targets that request's run only. Unknown shutdown leaves an `unsettled.json` latch that blocks new bridge requests until an operator verifies shutdown; never delete it merely to retry. The coding process also holds an OS file lock. The addon never calls OpenJarvis chat from OpenClaw, preventing a delegation loop.

Run tests using the existing OpenJarvis environment, without installing packages:

```powershell
<existing-venv-python> -m unittest discover -s <this-directory> -p 'test_*.py' -v
```

The existing startup/watchdog sources and tests are in the parent runtime directory; run its tests separately as well. Deployment must preserve the existing startup manifest and backups. Do not rerun one-time activation or port-change helpers on another machine without fresh inventory and approval for the exact changes.
