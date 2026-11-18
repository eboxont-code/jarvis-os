# Context-free continuation handoff — automatic four-app startup

> **Later 1.0.5 desktop repair:** read [the verified native attach repair](OPENJARVIS_DESKTOP_ATTACH_2026-11-18.md) after the complete latest master. The port conflict came from a two-second native health timeout versus Windows localhost fallback. Child-scoped IPv4, fast attach preflight and bounded catalogue retries now pass actual GUI chat/reopen and full runtime checks; earlier blocked/API-only statements remain historical. Actual new Windows reboot acceptance is still pending.

> **Later same-day backend repair:** the first actual reboot triggered startup, but OpenJarvis subsequently lost its listener. Read [the backend recovery implementation/evidence](OPENJARVIS_BACKEND_RECOVERY_2026-11-18.md) after the complete latest master. Current startup now launches an ongoing watchdog/backend before the desktop and verifies a real fresh heartbeat; backend-only automatic recovery preserves the GUI. The original startup sequence and pending-first-boot statements below are historical where superseded by that later record/master. The revised version still needs its own real Windows restart/sign-in acceptance. Do not reinstall/reset anything or treat an old ready snapshot as current health.

Recorded 18 November 2026, Australia/Brisbane. This is a dated technical handoff and evidence index, **not a TODO or status tracker**. Read the complete latest [AGENTS.md](../AGENTS.md), [MASTER_TODO.md](../MASTER_TODO.md) and [JARVIS_BOOT.md](../JARVIS_BOOT.md) first. The master alone decides current priority/status; later master evidence supersedes this snapshot.

## User objective and exact resume boundary

The user made this the first priority: after restarting Windows and signing in, **Ollama, OpenJarvis, OpenClaw Gateway/Companion and OpenCode must start with their saved connections ready, without manual reconnects or agent intervention**.

The ordered startup is installed. An unattended stopped-application-stack test passed in 376.2 seconds. **An actual Windows restart/sign-in has not been tested for this installation.** The last instruction to the user was: restart Windows, sign in normally, allow about seven minutes without opening/reconnecting apps, then reply “back”.

On continuation, do not open apps, run the launcher again, reconnect Companion, restart services or reinstall anything before collecting the first post-login evidence. Such intervention would invalidate unattended logon acceptance. Do not reboot the computer automatically. If the user has not rebooted, preserve the pending acceptance and report that specific remaining step.

## Entry points and implementation

- [Autostart behavior and rollback](AUTOSTART_READINESS.md)
- [Ordered startup worker](../runtime/start_ai_stack.py)
- [Read-only isolated readiness probe](../runtime/isolated_readiness_probe.py)
- [Reversible normal-user installer](../runtime/install_startup.py)
- [Thirteen startup tests](../runtime/test_start_ai_stack.py)
- [Existing three-tool adapter design](OPENJARVIS_READONLY_MCP_ADAPTER.md)
- [Adapter implementation](../runtime/openjarvis_readonly_mcp_adapter.py)
- [Earlier controlled/manual recovery procedure](RESTART_RECOVERY.md)
- Master implementation/evidence commit: [3b7a4ec](https://github.com/eboxont-code/jarvis-os/commit/3b7a4eccc3a657ce6064fde202e8fef3957567bb). Source/docs were read back remotely through 297c332 before that master update.

The old [18 November handoff](CONTINUATION_HANDOFF_2026-11-18.md) and [12 November handoff](OPENCLAW_OPENCODE_OLLAMA_HANDOFF_2026-11-12.md) preserve historical failure evidence. Their blanket official-repair wait gate, unregistered-MCP statement and ENOENT-only continuation boundary have been superseded by the current master. Do not revive those obsolete gates.

## Observed installation map — recheck, do not assume

| Component | Last verified location |
|---|---|
| Stable startup workspace | C:\Users\Boxont\Documents\Codex\jarvis-os-runtime |
| Startup shortcut | %APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\JARVIS AI Stack.lnk |
| Shortcut target / argument | C:\Python314\pythonw.exe / quoted stable-workspace start_ai_stack.py |
| Existing Python | C:\Python314\python.exe and pythonw.exe |
| Ollama desktop | C:\Users\Boxont\AppData\Local\Programs\Ollama\ollama app.exe |
| OpenJarvis desktop | C:\Users\Boxont\AppData\Local\OpenJarvis\openjarvis-desktop.exe |
| Companion | C:\Users\Boxont\AppData\Local\OpenClawTray\OpenClaw.Tray.WinUI.exe |
| OpenCode desktop | C:\Users\Boxont\AppData\Local\Programs\ai.opencode.desktop\OpenCode.exe |
| Qualified official CLI | C:\Users\Boxont\AppData\Local\Microsoft\WindowsApps\OpenClawFoundation.OpenClawGateway_rfcbke2p71se2\clawctl.exe |
| Last isolated Shared workspace | C:\Users\T3-P2\Shared |
| Installed isolated startup probe | Shared\jarvis-startup-20261118\isolated_readiness_probe.py |
| Existing approved MCP adapter | Shared\jarvis-readonly-mcp-20261118\openjarvis_readonly_mcp_adapter.py |
| Runtime snapshot | stable-workspace\startup-last.json |
| Private installation/rollback bookkeeping | stable-workspace\installation.json and backups\dated-folder |
| Local safe evidence/deliverables | C:\Users\Boxont\Documents\Codex\2026-11-18\github-plugin-github-openai-curated-remote\outputs\JARVIS-Autostart |

The current manifest contains installed paths. Inspect only needed metadata, never dump active configs/bookkeeping or backups. Determine the actual isolated session using the official CLI; do not hard-code an old profile if it changes. Preserve every installation and both OpenCode account contexts.

The runtime uses existing Python plus built-in Windows PowerShell 5 for narrow process inventory. Codex's bundled PowerShell 7 is **not** a runtime dependency. Do not add an execution-policy bypass.

## What was changed on the PC

One normal-user Startup shortcut owns the ordered app startup. Original Ollama/Companion Startup links were copied and hash-verified, then moved out of Startup into retained backups. The duplicate Companion HKCU Run value was privately backed up and removed. The old scheduled task “OpenClaw Companion - Wait for Gateway” was exported and disabled. Companion's AutoStart boolean changed true to false so it cannot recreate a competing startup owner; every other setting was semantically unchanged.

The official “OpenClaw Gateway …” logon task remains enabled. No Gateway/Companion token, pairing, ACL, security setting, profile, runtime path or permission expansion was changed. The four protected host application configurations and active isolated Gateway configuration remained unchanged. Backups are local and must stay private.

Do not rerun the installer on this PC: it intentionally refuses an existing installation record. Do not undo/reinstall startup merely to inspect it. Rollback is documented in AUTOSTART_READINESS.md, requires Companion fully exited, and must be deliberate and authorised.

## Sequence and recovery boundaries

1. Adopt/start existing Ollama; wait for local API and confirm saved OpenJarvis model plus existing 4B fallback are installed. Never pull a model.
2. Adopt the official Gateway logon start; request at most one supported start if stopped. Validate real native isolated-session contract, selected port50368, listener identity and launch receipt, then authenticated Gateway health.
3. Adopt/start OpenJarvis; require health on8000 and matching Ollama catalogue.
4. Check exact retained three-tool MCP registration, real adapter initialize/list/all-three calls, local-only provider and OpenCode ACP initialize protocol1. Close the owned ACP probe.
5. Recheck real native proof, start existing Companion --background, and require its existing paired Node online. If its first handoff fails, retry **only the exact Companion Popen child owned by this launcher once**, after current native ownership proof passes. Never restart preexisting/replacement apps or Gateway as automatic recovery. No credential/ownership bypass.
6. Validate host OpenCode provider is local Ollama only and open its existing desktop.

An OS-held lock prevents duplicate workers. Calls/waits are bounded, and overall ready stays false until every phase passes. The safe snapshot has only booleans, phase/error codes and elapsed times. It is operational evidence, not project status.

The launcher sends no inference/agent prompts and creates no ACP coding task at login. The existing Gateway can independently resume an old main-session recovery turn; this behavior was not changed. Do not cancel unrelated work or assume an idle model without inspection.

The packaging defect around multiple observed listeners is **not permanently fixed**. Native admission still fails closed on incomplete proof. The successful owned-Companion retry is bounded recovery, not a patched native security contract.

## Recorded tests and failure history

All attempts started with the relevant application/service ports closed and exactly one worker launch. No operator reconnect/extra app launch/model prompt was used during an attempt.

| Attempt | Actual result |
|---|---|
| [1](evidence/autostart-2026-11-18/attempt-1.json) | Failed at1.0s on empty WindowsPS process-inventory JSON. Corrected array serialization and added an actual Windows inventory regression test. |
| [2](evidence/autostart-2026-11-18/attempt-2.json) | Ollama/Gateway/OpenJarvis/catalogue passed; MCP/ACP budget failed380.8s. Later diagnostic failed mcp_protocol while existing bytes verifier passed. Exact transient cause unproven. Explicit newline UTF-8 byte input, safe failure stages and240s warm-up now used. |
| [3](evidence/autostart-2026-11-18/attempt-3.json) | Passed through MCP/ACP/native proof; Companion operator connected but Node handoff refused. Node deadline failed419.1s. A later normal retry of the exact owned Companion restored Node without Gateway restart. |
| [4](evidence/autostart-2026-11-18/attempt-4.json) | Passed376.2s: Ollama4.5, Gateway proof118.8, authenticated196.5, OpenJarvis243.1, models243.7, MCP/ACP246.7, native admission247.4, paired online Node364.3, OpenCode/complete376.2. One automatic owned Companion retry began343.8s; no manual recovery. |

Thirteen tests and Python compilation passed. Final independent read-only checks confirmed Gateway50368/one owned listener, exactly one paired connected Node, real native device.status exit0/ok, unchanged active isolated config and all four protected host config hashes. OpenJarvis restored Chat/history; OpenCode displayed its local Ollama/Qwen27B selector. Worker exited normally. No reboot/sign-in inference can be drawn from this stopped-stack test.

The wider project already has actual three-tool Gateway MCP calls, scoped ACP coding/failure/permission/cancellation/timeout checks and an assisted useful local status report. Details are in the master execution log; they do not establish broad autonomy, runtime-wide permissions or full Windows desktop control. Larger coding generation reliability, interrupted-task recovery, extra-listener admission, original OpenJarvis listener loss, global OpenCode policy and full traffic/desktop matrix remain separate unfinished work.

## First post-reboot checks — observation before repair

Use real authorised Windows tooling; GitHub access alone cannot inspect this PC.

1. Record fresh last boot time, current sign-in/session and time. Read the safe startup snapshot. Confirm its timestamp belongs to this new boot/sign-in; an old ready=true is not a pass. Check whether the exact startup worker is still running before considering another launch.
2. Observe installed app processes/visible windows and fixed loopback health/catalogue without starting/reconnecting anything. About seven minutes was measured, not guaranteed; use the recorded phase deadlines rather than an infinite wait.
3. Using the **current qualified official CLI**, inspect native Gateway status and authenticated health, and node.list (report only counts/connection booleans). Require one paired connected Node and valid actual ownership proof.
4. Check current exact MCP whitelist/timeouts/local-only bindings. The installed probe's health/connections/node phases are read-only; connections performs actual three adapter calls and a short ACP initialize, then closes its own subprocess. Run only after the startup worker has finished to avoid interfering with its startup sequence.
5. Verify GUI readiness and a harmless native device.status request, summarizing booleans/exit codes only. Do not expose device details, tokens, node identifiers or config values.
6. Compare protected config hashes against the pre-start baseline; preserve private backups. Confirm one JARVIS shortcut, disabled duplicate wait task/Run/links, and enabled official Gateway task.
7. Update only the relevant master checkbox/phase/live rows and dated execution log with actual reboot evidence; push and exact read-back. Mark VERIFIED only if this real boot/sign-in reached all gates without extra launches/reconnects/operator recovery.

Safe initial PowerShell observations:

~~~powershell
(Get-CimInstance Win32_OperatingSystem).LastBootUpTime
Get-Content -LiteralPath "$env:USERPROFILE\Documents\Codex\jarvis-os-runtime\startup-last.json" -Raw
Get-CimInstance Win32_Process |
  Where-Object { $_.Name -eq 'pythonw.exe' -and $_.CommandLine -like '*jarvis-os-runtime*start_ai_stack.py*' } |
  Select-Object ProcessId, CreationDate
~~~

If failure occurs, preserve the snapshot first; document the exact failed phase and inspect narrowly redacted evidence. A stale snapshot, missing startup trigger or offline Node is not success. Make only a concrete, reversible repair within the user's existing authorisation; seek specific approval if the necessary action exceeds it.

## Authority and approvals for a new agent

The user revoked “wait solely for an official repair”; pursue supported bounded diagnostics now. That does not grant a blanket security/ownership bypass. Prior explicit whole-app restart permission supported the recorded controlled tests; installed autostart specifically allows its one owned-client retry. This handoff is not standing permission for future broad restarts, reboot/sign-out, resets, reinstall/update, missing-runtime creation, runtime-path/profile overrides, security/ACL changes, pending file-command expansion, destructive/elevated work or paid services.

Preserve all existing OpenJarvis custom source/settings/models/data/installations/backups. No downloads, paid/cloud fallbacks, new subscriptions or costs. Never publish active config, installation.json, original settings/task backups, histories, raw logs, secrets or device payloads. Only sanitized phase evidence is included here.

If GitHub or local tools are unavailable, state exactly which verification is unavailable; never substitute fabricated success. No previous chat context is required: retrieve these linked files plus the latest entire master and continue its exact next eligible task.
