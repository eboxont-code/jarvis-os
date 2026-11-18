# Automatic readiness of the existing Windows AI stack

`MASTER_TODO.md` is the project-status authority. This document describes the
normal-user startup mechanism, acceptance boundary and rollback. For a new agent,
read the [self-contained continuation handoff](CONTINUATION_HANDOFF_2026-11-18_AUTOSTART.md)
for exact observation-first reboot checks, installed locations and sanitized
[attempt evidence](evidence/autostart-2026-11-18/attempt-4.json).

## Later backend recovery repair — 18 November

The first real reboot did trigger this launcher, but a later OpenJarvis backend
lost its listener. The current implementation adds a locked ongoing watchdog and
starts the existing backend before attaching the desktop. Read
[the backend recovery record](OPENJARVIS_BACKEND_RECOVERY_2026-11-18.md) for current
behavior, fault-test evidence, retry/heartbeat limits and rollback. The safe
`runtime-health.json` is current health; `startup-last.json` is a dated startup
snapshot. Final revised warm startup passed18.6s including live watchdog PID and
fresh heartbeat; actual Windows reboot acceptance of this revised version remains
pending in the master.

## After Windows sign-in

One user Startup shortcut, **JARVIS AI Stack**, launches the installed
`C:\Python314\pythonw.exe` with
`%USERPROFILE%\Documents\Codex\jarvis-os-runtime\start_ai_stack.py`.
No Codex process, subscription, cloud inference, package install or model download
is a startup dependency. Interactive desktop apps require the user to sign in;
this does not configure automatic Windows login.

The sequence is:

1. Start the existing Ollama app if absent; wait for its local API and confirm the
   saved OpenJarvis model and existing startup fallback are already installed.
2. Adopt the official Gateway's existing logon start, or request **one** supported
   `gateway-service start` if stopped. Wait for a complete native status contract
   including the selected port, listener identity and launch receipt, then check
   authenticated Gateway health. An open TCP port alone does not pass.
3. Start the normal-user locked watchdog with bootstrap; it starts the existing
   venv/CLI backend only when needed, using the installed confirmed local model.
   Require actual health, a fresh heartbeat from the real watchdog process and
   a model catalogue matching Ollama, then attach the existing desktop if absent.
   No dependency sync or model download is used.
4. Check the retained exact-three-tool read-only MCP registration, real adapter
   status calls, local-only Ollama configuration and existing OpenCode ACP
   initialization. Close the probe before continuing. No agent/model prompt is sent.
5. Recheck the real Gateway proof, then start Companion with its existing saved
   connection. Require the existing paired Node to become connected automatically.
   If its first handoff fails, permit one normal retry of only the Companion
   process this launcher started, after rechecking current Gateway ownership.
   Existing independently started or replacement Companion processes are preserved.
   Companion still performs its own native ownership and credential checks.
6. Confirm the host OpenCode configuration is local Ollama only and start its
   existing desktop app. The coding harness remains available on demand rather
   than creating a perpetual coding job at login.

The official Gateway logon task is preserved. The old Companion Run entry,
Companion Startup shortcut, Ollama Startup shortcut and port-only wait task are
backed up before their duplicate launches are disabled. Companion's own
`AutoStart` preference is set false because JARVIS owns the ordered launch.
No other Companion setting, saved connection, token, pairing or permission is
changed. Keep the independent Companion startup entry disabled to retain ordering.

## Failure and duplicate protection

An OS-held file lock permits one launcher. Existing exact app executables are
adopted, not launched twice. Readiness waits and subprocess calls have deadlines.
Missing model files, incomplete Gateway proof, offline Node or provider mismatch
produce a failed result; the launcher does not reset, repair, reinstall, switch
profiles, fabricate ownership proof, restart pre-existing applications or run a paid
fallback. Only its own failed Companion can be retried once; Gateway, Ollama and
the OpenJarvis desktop are never automatically restarted. Only the exact failed
OpenJarvis backend with confirmed closed port can receive bounded ongoing
recovery; see the later backend recovery record above. A timed-out Gateway start command
is never retried as a second start.

The operational snapshot is
`%USERPROFILE%\Documents\Codex\jarvis-os-runtime\startup-last.json`.
Its overall `ready` flag stays false until every phase completes. It contains
only phase names, booleans, bounded error codes and elapsed times, never command
output, credentials or raw settings. It is a runtime check, not another project
TODO or status tracker.

The existing Gateway packaging can omit its port/ownership proof when an ACP
backend introduces an additional listener. Startup initializes/closes its probe
before native admission, then uses Companion's normal handshake. This sequencing
does not fix that package defect or bypass security; admission fails closed if a
valid current proof is unavailable.

## Install and rollback

The supplied `install_startup.py` uses the current user's startup folder,
registry entry and existing wait task. Run it from the source directory with the
existing Python installation, with Companion fully exited. It verifies backups
before changing registrations and preserves them under the stable runtime folder.
The installation records the exact original settings hash and shortcut copies;
only the `AutoStart` JSON boolean is patched. No elevation is requested.

For rollback, fully exit Companion and run:

```powershell
C:\Python314\python.exe "$env:USERPROFILE\Documents\Codex\jarvis-os-runtime\install_startup.py" --undo
```

Undo restores the original startup entries and original `AutoStart` boolean while
preserving other current settings. It refuses to overwrite a replaced JARVIS
shortcut, a new Run value or a conflicting original shortcut. Runtime code and
backups remain available for review; nothing is recursively deleted.

## Acceptance boundary

On 18 November 2026, the installed launcher completed an unattended stopped-stack
test in 376.2 seconds. Ollama, authenticated Gateway, OpenJarvis health/catalogue,
three real read-only adapter calls, ACP initialization, paired online Node and
OpenCode desktop passed. Companion needed the launcher's one owned-process retry;
no operator reconnect or extra app launch was used. A subsequent native
`device.status` call succeeded. Four protected host configurations and the active
isolated Gateway configuration remained unchanged. Thirteen tests passed.

Earlier failed attempts are retained in the master execution log. The bounded
Companion retry is recovery, not proof of a permanent native package repair.
An actual Windows reboot/sign-in has **not** been performed for this startup
installation; its logon trigger remains pending acceptance.

Unit/protocol tests and an unattended stopped-stack launch are necessary checks.
They do not prove Windows logon execution. Mark reboot readiness VERIFIED only
after an actual computer restart and sign-in reaches all ready connections
without prompts, reconnect clicks, extra launches or agent intervention. Save
the result and relevant actual checks in the sole master execution log.
