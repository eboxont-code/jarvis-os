> **Archived wiped install.** This file is not current setup. The Windows install it describes has been removed. Nothing here is installed, enabled, connected, configured, paired, running, or done. Checked boxes, version numbers, and pairing notes below are historical and do not apply. Follow the fresh-install guide in the repository root `README.md`, and use the root `REQUIREMENTS.md` as the checklist.

# OpenJarvis 1.0.5 desktop attach repair — 18 November 2026

This dated implementation/evidence handoff is not a project tracker.
Read the complete latest [master](../MASTER_TODO.md) and [agent instructions](../AGENTS.md).
The master alone controls priority, status and next actions.

## Reproduced cause

The API was healthy but the actual updated desktop was blocked on setup with
os10048 / port8000 unavailable. The owner was the project watchdog's preserved
backend, not an unidentified service. Earlier API-only reports did not prove
desktop readiness; that reporting error is retained in the master.

Read the actual released [desktop-v1.0.5 source](https://github.com/open-jarvis/OpenJarvis/blob/desktop-v1.0.5/frontend/src-tauri/src/lib.rs):
the native app supports attaching to an existing healthy backend, but uses a
two-second timeout for two health probes,500ms apart. A timeout falls through to
server startup; an existing listener then yields the bind error. Do not assume
the release intentionally forbids attach or kill a healthy service to hide this.

Measured with the existing installed OllamaEngine:
localhost health2.062/2.058/2.051 seconds; IPv4 loopback31/46/48ms.
The saved engine-host override was absent, so the supported OLLAMA_HOST child
environment setting applies. The measurements and release code identify a
Windows localhost/IPv6 fallback timing problem exceeding the native attach gate.

## Installed project-owned changes

- [Watchdog](../runtime/openjarvis_watchdog.py) copies its environment and sets
  OLLAMA_HOST=http://127.0.0.1:11434 only for its existing-venv backend child.
  No saved config, global environment, model selection, security or profile is
  changed. Explicit user configuration is not silently rewritten.
- [Startup](../runtime/start_ai_stack.py) requires two actual healthy API probes,
  each under one second, with the native500ms gap, before opening the desktop.
  A slow-but-healthy API cannot pass this gate. There is no setup-state bypass.
- Model-catalogue readiness now retries transient timeouts/mismatches within120s,
  instead of aborting the entire sequence after one cold three-second request.
- Backend inventory now includes the proven serving base-Python child of the
  exact checkout's venv shim. It checks purpose/port and parent relationships,
  and stops the verified leaf before the shim with PID/creation/path rechecks.
  Unrelated Python, different port owners and a live listener remain preserved.

The existing watchdog owns one backend; the stock1.0.5 desktop attaches normally.
No second backend, port reassignment, reinstall, updater, model download, paid
fallback or Gateway/Companion reset is used.

The unchanged earlier [connector-status source fix](OPENJARVIS_BACKEND_RECOVERY_2026-11-18.md)
remains applied. This repair changed project runtime/test files, not more of the
custom OpenJarvis checkout or the updated desktop binary.

## Actual acceptance evidence

-29 startup/watchdog tests pass, plus the existing real ASGI connector regression:
  30 checks total. New cases reject a healthy2.06s API, require both fast probes,
  recover after a catalogue timeout, keep child environment scoped, include the
  proven venv server child and preserve unrelated Python.
- Paused only the identified watchdog and stopped only verified backend18852/3840.
  An initial ownership assertion safely refused because old inventory omitted
  the serving venv child; fixed selection before stopping. New watchdog732
  recovered the backend with the child environment setting.
- Actual API samples after repair78–104ms; native attach preflight passes.
- Actual stock1.0.5 setup completed and Chat became visible. Sent one harmless
  prompt through the GUI; screenshot confirms separate assistant reply
  JARVIS_DESKTOP_ATTACH_OK using local qwen3.8:27b in9.4s.
- Closed and reopened the native desktop normally. The same backend PID26372
  kept the sole8000 listener. Reopened Chat restored the acceptance conversation
  and reply, with no setup/bind error. This is GUI evidence, not an API inference.
- Full revised runtime sequence passed148.5s: Jarvis25.4s, fresh watchdog34.4s,
  attach35.1s, catalogue36.6s, actual MCP/ACP38.4s. Companion's first Node handoff
  needed its one launcher-owned retry; paired online Node146.6s, OpenCode148.4s.
  Gateway/Ollama were adopted, not restarted. This is a partial-stack recovery
  test, not another actual Windows reboot.
- One paired connected Node and actual device.status exit0/ok verified;
  active isolated Gateway config unchanged. OpenCode visible landing screen
  shows local Ollama/Qwen27B. All four app executables are running.
- Post-reopen connector listing27 entries235ms; five concurrent health49–72ms.
  Source responsiveness patch hashe4df64bf… remains intact.

[Sanitized runtime evidence](evidence/desktop-attach-2026-11-18/startup.json)
and [current-health evidence](evidence/desktop-attach-2026-11-18/health.json)
are stored alongside this handoff. These are dated snapshots, not live guarantees.

## Configuration integrity and rollback

The saved inference file differs from the old15/18 November baseline, but its
last-write time13:16:10 precedes this repair. Its current confirmed model exists
locally; it was preserved rather than reverting a prior user/app choice.
Current SHA256:332373143c3ae54fe974fb98591229af363720023bebe925a1098d06f9391077.
The older verified inference backup remains intact. The other three protected
host settings hashes and isolated Gateway config match prior evidence.
Do not restore an old saved model merely because a historical hash differs.

Pre-repair runtime/test files are backed up as *.before under the authorised
Codex work/desktop-attach-repair folder. Copies were verified when deployed.
To roll back, deliberately stop the owned watchdog, verify the current runtime
against this commit, restore the matching runtime pair from that checkpoint,
and recover only the known backend. Reverting the IPv4/gate change can restore
the demonstrated timeout conflict; do not do it just to resume a session.
Existing installation.json/settings/task backups remain private and untouched.

## Continue without chat context

1. Read the complete latest master; do fresh read-only checks first.
2. Read runtime-health.json with actual watchdog PID/fresh timestamp and the
   startup snapshot. A green API is not proof that the desktop setup completed.
3. Inspect the actual OpenJarvis GUI for Chat/Dashboard and absence of setup or
   port errors, and verify one backend owner. Do not reset setup/storage or
   alter authentication to skip a failed native gate.
4. Confirm MCP/ACP, native online Node and OpenCode local provider; preserve all
   configurations/models/data and the single ordered Startup entry.
5. Exact next acceptance is a subsequent Windows restart/sign-in with this
   version, followed by fresh GUI/API/protocol checks without intervention.
   No new Windows reboot was performed during this repair. The native Companion
   still sometimes needs its bounded owned-client retry; no package fix claimed.
6. Update only the master with verified results and exact GitHub read-back.
