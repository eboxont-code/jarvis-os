> **Archived wiped install.** This file is not current setup. The Windows install it describes has been removed. Nothing here is installed, enabled, connected, configured, paired, running, or done. Checked boxes, version numbers, and pairing notes below are historical and do not apply. Follow the fresh-install guide in the repository root `README.md`, and use the root `REQUIREMENTS.md` as the checklist.

# OpenJarvis front-door adapter

Implementation notes from a wiped install. The repository root `REQUIREMENTS.md` is the checklist. These scripts are not a current installer.

Ordinary greetings/questions retain native OpenJarvis chat. Explicit coding requests route through the approved local OpenClaw Gateway job-ID-only delegate to installed OpenCode ACP and local Ollama; verified file/test receipts return to the same chat. Other bridge requests use one restricted model coordinator, which remains slow/unreliable. `/local ` explicitly uses original Jarvis; client-tool requests retain their native route. See the dated handoff for the actual GUI167s edit/test pass, active Stop/recovery pass and remaining Companion/reboot limitations. The router is bounded lexical routing, not unrestricted semantic task planning.

The in-process addon replaces only the existing chat route callable, retaining the original app's middleware/authentication and route dependencies. The original checkout is preserved. The project watchdog launches `backend_bootstrap.py` only when its adjacent `frontdoor.json` manifest exists; otherwise it uses the original installed CLI.

The isolated account holds `gateway_job.py`, `code_server.py`, `acp_client.py`, `projects.py`, `verify_project.py`, its coordinator workspace and operational job receipts. Prompts stay local. Never upload job inputs, complete active configuration, diagnostic ZIPs or private backups.

Coding is limited to bridge-owned projects, source/tests/README edits and one exact verifier command. It has no general shell, installer, network, browser, external-directory or messaging grant. The verifier executes a restricted pure-Python subset under process/time/memory limits; it is not a general operating-system sandbox. Broader programs require separately reviewed permissions. Test results and protected hashes are checked independently of model prose.

Each request gets a new isolated session with bounded conversation context, one coding claim and a deadline. Cancellation targets that request's run only. Unknown shutdown leaves an `unsettled.json` latch that blocks new bridge requests until an operator verifies shutdown; never delete it merely to retry. The coding process also holds an OS file lock. The addon never calls OpenJarvis chat from OpenClaw, preventing a delegation loop.

Run tests using the existing OpenJarvis environment, without installing packages:

```powershell
<existing-venv-python> -m unittest discover -s <this-directory> -p 'test_*.py' -v
```

The existing startup/watchdog sources and tests are in the parent runtime directory; run its tests separately as well. Deployment must preserve the existing startup manifest and backups. Do not rerun one-time activation or port-change helpers on another machine without fresh inventory and approval for the exact changes.

Code projects use the no-download local alias jarvis-code-qwen27b:16k. `prepare_code_model.py` refuses a missing installed source and preserves existing aliases; do not run it blindly. It creates a supported local manifest referencing existing weights, never a pull/download. Global Code and original Ollama models remain preserved.
