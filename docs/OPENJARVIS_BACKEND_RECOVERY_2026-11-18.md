# OpenJarvis backend recovery — 18 November 2026

This is implementation/evidence documentation, not another project tracker.
[MASTER_TODO.md](../MASTER_TODO.md) alone controls priority and current status.

## Failure observed and authorised repair

After the actual Windows reboot at11:15 Brisbane, the original login worker
recorded ready at11:24 (511.4 seconds). A later desktop instance had a live
registered Python backend but no8000 listener. Ollama11434 remained healthy.
The user explicitly requested fixing it and preventing recurrence.

One exact OpenJarvis desktop/backend restart briefly restored health in48.4s,
then the listener failed again; the subsequent chat test got ConnectionResetError.
No Gateway, Companion or Ollama restart was performed. Two isolated existing-CLI
diagnostics followed. The first returned a real local chat marker in16.7s then
lost its listener; only traceback/error indicators were captured, so the exact
exception/root cause remains unproven. The second stayed healthy across at least
193.1s of observations and returned the same local marker in2.3s. Do not claim a
permanent application-source or native-package fix from this evidence.

## Installed mitigation and ongoing recovery

The project-owned [watchdog](../runtime/openjarvis_watchdog.py) now runs at
normal-user privilege, independently of Codex. The revised
[startup worker](../runtime/start_ai_stack.py) launches it before the desktop,
waits for real API health and a fresh heartbeat from the actual watchdog PID,
then starts the preserved desktop on its existing healthy-backend attach path.

A backend is started with the already installed OpenJarvis venv Python and
the existing CLI module, fixed loopback8000, explicit Ollama engine and the
confirmed saved model, only if that model already exists in Ollama. Agent remains
simple. No uv sync, dependency install, model pull, source/build replacement,
saved-setting edit, new provider or cloud fallback is introduced. Standard
streams go to DEVNULL so the service does not depend on a transient console or
unread output pipe. The desktop can remain open during backend recovery.

The watchdog checks every15s, with bounded local HTTP/process calls.
After three failed checks it may recover only a confirmed closed-port backend.
It preserves any live8000 listener, including an unhealthy-but-listening process;
it does not kill a possibly busy request merely because health times out.
It never restarts Gateway, Companion, Ollama or the desktop as automatic recovery.
A snapshot-selected failed backend must match this user's exact checkout,
jarvis-serve/module command and explicit8000 port; stop rechecks PID, creation time
and executable path. No process-name kill or taskkill tree is used.

Recovery is limited to two attempts in30 minutes, persisted across watchdog
restarts on the same Windows boot. A different actual boot resets that budget.
A360s startup grace protects a newly starting desktop; a previously healthy
backend or explicitly requested bootstrap can be recovered after confirmed failure.
An OS-held lock prevents duplicate watchdogs.

The current-state file is:
C:\Users\Boxont\Documents\Codex\jarvis-os-runtime\runtime-health.json

It contains a timestamp, watchdog PID, boolean/phase, boot identifier, bounded
event history and retry times. It contains no raw logs, config values, prompts or
credentials. Read its freshness and actual process as well as the boolean.
startup-last.json remains historical startup acceptance, not continuous health.
The startup worker now refuses to report success if the watchdog is paused,
missing, dead or stale even when an old health snapshot says true.

The watchdog's --bootstrap mode keeps the local backend available without opening
or reopening the GUI; closing the desktop does not remove the local MCP backend.
A watchdog run without bootstrap does not initially relaunch an absent desktop.
The native desktop's ordinary attach path is used; original executable,
custom source, models, settings, databases and backups remain in place.

## Verification

-24 tests pass: original13 startup checks plus11 recovery/readiness boundary tests.
 Python compilation passes. Tests cover healthy/listening preservation, unknown
 new port owner, exact process identity, desktop preservation, model absence,
 installed local-only launch, retry limit/boot reset, and stale/dead heartbeat.
- An actual controlled fault stopped only the isolated test backend while desktop
 PID24616 remained open. The production watchdog autonomously confirmed closed
 port, entered recovering and restored health; event interval38.7s is the backend
 recovery work after detection, not total fault downtime. No operator relaunch
 was issued after fault injection.
- A subsequent real streaming chat on existing qwen3.8:27b returned the fixed marker
 in2.5s, with no tool requests.
- Actual isolated probe passed all three read-only adapter tools, matching catalogue,
 local-only bindings and ACP initialize protocol1.
- Revised warm startup passed all app/native gates in18.2s before the final fresh-PID
 heartbeat gate was added; the final run is recorded in the master execution log.
 This is a warm adoption test, not another Windows reboot.
- Final independent native device.status returned exit0/ok and one paired online
 Node; active isolated Gateway hash and all four protected host configs unchanged.
 Original installed OpenJarvis EXE hash also unchanged.
- Actual dashboard shows OpenJarvis API, Ollama, hardware/GPU and inference telemetry
 HEALTHY. Red backend warning cleared. The remaining high-VRAM alert is real27B
 model resource usage; warning thresholds/model settings were not altered.

Sanitized evidence: [fault recovery](evidence/backend-recovery-2026-11-18/fault-recovery.json),
[post-repair startup](evidence/backend-recovery-2026-11-18/startup.json).
Source [tests](../runtime/test_openjarvis_watchdog.py) and
[bounded local chat smoke check](../runtime/check_openjarvis_recovery_chat.py) are available.

## Stop, rollback and continuation

To deliberately pause automatic recovery, create watchdog.stop in the stable
runtime folder, then wait for the watchdog to exit. This does not terminate
the running backend. To resume, remove only that marker and launch the installed
watchdog with existing Pythonw and --bootstrap, or use the next normal login.
Startup intentionally reports watchdog_deliberately_paused while that marker exists.

Before undoing startup installation, pause the watchdog and fully exit Companion.
The installer now refuses rollback while the watchdog runs. The original
startup installer has been updated to copy the watchdog/tests as well.
Keep all local installation.json/settings/task/shortcut backups private.
The pre-repair worker is retained locally as
work/backend-recovery/start_ai_stack.before.py in the authorised Codex workspace,
and its prior source is in Git history. Do not rerun installation on this already
installed PC.

Next acceptance: an actual subsequent Windows restart/sign-in using this
backend-first/watchdog version, followed by fresh sustained API/UI/MCP/native
checks without intervention. Longer-term stability and the internal listener-loss
exception are not proven. If a live-listener hang or retry limit is reached, the
watchdog reports it without a restart loop; diagnose that exact state rather than
resetting profiles/security or concealing the failure.

No model downloads, new packages, spending, cloud inference, security/pairing/ACL
changes, app reinstall/update, original source edit or database reset occurred.
