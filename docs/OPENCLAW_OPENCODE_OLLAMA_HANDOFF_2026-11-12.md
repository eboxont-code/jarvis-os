# OpenClaw / OpenCode / Ollama integration handoff — 12 November 2026

**Project:** JARVIS OS  
**Repository:** `eboxont-code/jarvis-os`  
**Purpose:** Preserve the verified Windows integration state and the exact unresolved blocker so a later session can resume without repeating the discovery work.  
**Status:** PARTIAL — browser ACP path works; native Windows Companion Node handoff remains blocked.

> This is a technical handoff note, not a second task checklist. `MASTER_TODO.md` remains the sole source of truth for milestone and task status.

## 1. Executive summary

The local model path and the browser-based OpenClaw-to-OpenCode ACP path have been demonstrated with a real `READY` response. The Windows Companion's separate native Node connection is still failing. Do not describe the entire four-application integration as complete.

The current split is:

| Component / path | Observed state |
|---|---|
| Ollama local endpoint | Reachable at `127.0.0.1:11434` from the isolated T3-P2 runtime |
| Qwen 27B local inference | Passed a direct OpenCode prompt and returned `READY` |
| OpenCode ACP server | Initialization and `session/new` succeeded; the model selector advertised all four local tags |
| OpenClaw browser Control UI → ACPX → OpenCode → Ollama | Fresh browser chat ACP session returned `READY` |
| Native Windows Companion Gateway / Operator | Gateway and Operator displayed connected in the app |
| Native Windows Companion Node | Error; credential handoff blocked before Node credentials were sent |
| OpenClaw → OpenJarvis MCP | Not configured or verified |
| Full disposable coding task through OpenClaw ACP | Not yet completed in this integration session |

## 2. Environment and installed versions

### Windows and local Gateway

- OS: Windows 11 Pro, build `26300`, 64-bit. A later registry check reported UBR `9711`.
- OpenClaw Gateway runtime: `2026.11.1`.
- Installed Gateway MSIX package version: `2026.11.100.0`.
- Gateway endpoint: `ws://127.0.0.1:50368/`.
- Gateway process: Node.js, observed PID `25904` during the latest status checks.
- Gateway service state: `running`; port `50368`; recovery `configured`.
- Gateway contract fields: `isolated-session` version `1`; ownership present; sandbox identity present; Windows account identity present; one owned listener; listener port matches `50368`; process ID present; start time parses; sequence number present.
- A live Windows TCP snapshot showed one listener at `127.0.0.1:50368` owned by PID `25904`.
- `clawctl status --json` and `clawctl gateway-service status --json` both reported the Gateway running on port `50368` with ownership present.
- `clawctl companion prepare --check --json` returned schema `1`, `ok=true`, integration `isolated-session v1`, port `50368`, and a configured token. Only the boolean presence was recorded; the token value was not copied.

### Companion package identity discrepancy

The running desktop app's **App info** screen showed:

- App name: OpenClaw Windows Companion
- Version: `v2026.11.1`
- Build date: 7 November 2026
- Runtime: .NET 10.0.14 / WinUI 3 / Windows App SDK 2.6.4
- Architecture: x64
- Update channel: stable
- Install type: `Unpackaged (developer)`

The Windows installed-apps listing separately showed an entry named OpenClaw Companion version `2026.9.8-1`.

These observations suggest an older registered install entry may coexist with the newer unpackaged/developer app that was running, but the active executable path has **not** yet been matched to the registered uninstall entry. Do not uninstall either copy until the running process path and package identity are confirmed.

### OpenCode in the isolated T3-P2 runtime

- OpenCode CLI version: `2.2.7`.
- Global config file: `%USERPROFILE%\.config\opencode\opencode.jsonc`.
- Configured primary model: `ollama/qwen3.8:27b`.
- Configured small model: `ollama/qwen3.5:4b`.
- Enabled provider allowlist: `ollama` only.
- Ollama base URL in OpenCode: `http://127.0.0.1:11434/v1`.
- OpenCode's model listing in this account showed:
  - `ollama/qwen3.5:0.8b`
  - `ollama/qwen3.5:2b`
  - `ollama/qwen3.5:4b`
  - `ollama/qwen3.8:27b`
- `opencode debug config` from the OpenClaw workspace loaded the same global config file and the same model/provider settings; the workspace did not reveal a conflicting project config.
- Direct command `opencode run --model ollama/qwen3.8:27b ...` returned `READY`.
- Direct ACP `initialize` succeeded. `session/new` succeeded and advertised all four models, with `ollama/qwen3.8:27b` selected by default.
- A diagnostic prompt initially encountered an already-active ACP prompt; the diagnostic session was explicitly cancelled, and a subsequent prompt completed with `READY`.

### OpenClaw model and ACPX configuration

- Default OpenClaw model: `ollama/qwen3.8:27b`.
- Qwen 27B model configuration was updated to `contextTokens=65536` and `params.num_ctx=65536`.
- A subsequent `ollama ps` showed `qwen3.8:27b` loaded with context `65536`, runner `llamacpp`, and a reported size of approximately 21 GB. No new model was downloaded.
- ACPX was installed/enabled; the ACP doctor reported the backend registered and the embedded ACP runtime ready.
- ACPX's OpenCode agent command was explicitly set to the OpenCode executable under the Gateway MSIX-managed Node installation, with arguments `["acp"]`. The command setting succeeded; the args array was validated with a dry run and applied through `openclaw config patch`.
- After closing the previous ACP session and spawning a new one from the browser Control UI, the prompt `Reply with exactly READY. Do not use tools.` returned `READY`. This verifies a simple browser-based OpenClaw → ACPX → OpenCode → local Ollama path.

## 3. Native Companion Node failure — unresolved

The desktop Companion's Connection page showed:

- Native Gateway `ws://127.0.0.1:50368/`: Connected.
- Operator: Connected.
- Node mode: enabled.
- Windows Node: Error / offline; diagnostics reported `0/1` nodes online.
- Approved/effective Node capabilities included browser, camera, canvas, device, local inference, screen and system; the capability/permission UI showed the configured capabilities rather than a disabled Node toggle.

Two error wordings were observed at different points:

1. `The installed Gateway MSIX does not expose Companion's isolated-session contract. Update the Gateway MSIX, then retry setup. Credentials were not sent.`
2. `Gateway ownership inspection failed. Check the installed Gateway package and retry. Credentials were not sent.`

The diagnostics bundle generated at `2026-11-12 00:43 +10:00` reported:

- Companion control connection: Connected.
- Gateway version: `2026.11.1`, update status current.
- Gateway URL/port: `50368`.
- Gateway runtime: Node process on port `50368`.
- Node inventory: Windows Node offline, approval state approved.
- Browser proxy host: port `50370` not listening.
- Connection timeline: Operator authentication reached `hello-ok`; the separate Node connection received a `connect.challenge`; the credential handoff was then blocked by the isolated-session/ownership inspection check. The Node credentials were not sent.

The app's technical-details panel also showed approved/effective commands and permissions; this is not evidence that the Node connection completed. The browser Dashboard and native desktop Companion must be treated as separate interface paths.

### Checks that already passed

- Gateway service status: running on port `50368`.
- Overall `clawctl status`: running on port `50368`.
- Gateway status JSON: `isolated-session v1`, ownership present, one listener.
- Detailed ownership summary: sandbox identity and agent SID present; listener port matches; PID present; timestamp parse valid; sequence present.
- Companion preparation check: `ok=true`, port `50368`, token present.
- Windows build `26300` is above the process-identity API minimum discussed during investigation (`26100.4770`).
- Live TCP listener: one listener at `127.0.0.1:50368`, PID `25904`.

An attempted Windows process-owner/start-time comparison was inconclusive: the CIM owner query returned no owner, and one process-time conversion failed. Those outputs must **not** be recorded as proof of an account/SID mismatch. Later checks confirmed the Gateway-reported PID existed and that the listener used the expected port.

### Important interpretation

The Gateway's TCP listener, status fields and Companion preparation response are present and valid in the checks above. The remaining failure is later in the native Companion Node authorization/ownership-inspection handoff. The current evidence does not establish that reinstalling the same Gateway MSIX, changing ports, regenerating credentials, changing permissions or re-pairing the Node will fix it.

## 4. OpenClaw automations observed

The browser Automations page showed two active automations; neither was changed:

- `Heartbeat (main)`: every 30 minutes.
- `Memory Dreaming Promotion`: cron `0 3 * * *`.

Keep these existing schedules unchanged while troubleshooting the Companion connection.

## 5. Configuration changes made during this session

These are the changes that were actually applied, not merely proposed:

1. In the T3-P2 OpenCode profile, created/updated `opencode.jsonc` with local Ollama primary model `ollama/qwen3.8:27b`, small model `ollama/qwen3.5:4b`, provider allowlist `["ollama"]`, and local Ollama base URL `http://127.0.0.1:11434/v1`. A backup named `opencode.jsonc.backup-20261111-205320` was created first.
2. In OpenClaw's model registry, set Qwen 27B `contextTokens` and Ollama `num_ctx` to `65536`. A backup copy of `openclaw.json` named `openclaw.json.before-context-65536-20261111.bak` was requested before these settings were changed.
3. In OpenClaw ACPX config, set the OpenCode command to the verified OpenCode executable path and applied args `["acp"]` using a structured config patch. The dry-run validation succeeded before the patch was applied.
4. Closed the old failed ACP session and created fresh sessions for testing. The latest browser ACP session returned `READY`.

No Gateway MSIX or Companion package was installed, upgraded, downgraded or removed during this troubleshooting sequence. No Ollama models were pulled or deleted. No pairing/token reset was performed. No credentials, tokens, device IDs, private SIDs, raw settings files or unredacted diagnostic payloads are included in this handoff.

## 6. What is verified vs. what is still incomplete

### Verified

- OpenCode 2.2.7 in T3-P2 discovers the local Ollama models.
- Direct OpenCode CLI local inference with Qwen 27B returned `READY`.
- Direct OpenCode ACP initialization and session creation exposed the local model catalogue.
- OpenClaw's browser Control UI successfully spawned OpenCode via ACPX and received `READY` from the local model.
- OpenClaw Gateway and Operator control connection are reachable on port `50368`.
- Qwen 27B is configured and has been observed loaded with 65,536 context.
- No additional spending or model downloads were needed.

### Not verified / blocked

- Native Windows Companion Node connection (currently offline; credential handoff blocked).
- Whether the active unpackaged Companion `2026.11.1` and the older installed-apps entry `2026.9.8-1` are two separate active installations.
- Why the native Companion reports ownership-inspection failure despite the CLI contract/status fields passing.
- Whether browser proxy port `50370` is required for any specific Dashboard feature or is a separate optional capability.
- A real OpenClaw-delegated coding task through ACPX with changed files, tests and returned evidence.
- OpenJarvis MCP connectivity to OpenClaw.
- Full four-application end-to-end acceptance and restart/recovery acceptance.

## 7. Exact next actions

1. **Resolve Companion executable/install identity first.** From normal Windows PowerShell, inspect only the running OpenClaw Companion process name, PID and executable path. Compare that executable path with the registered `OpenClaw Companion 2026.9.8-1` uninstall entry and the App info screen showing active `v2026.11.1` / `Unpackaged (developer)`. Do not uninstall either copy until the active process and registered package are unambiguously mapped.
2. **Capture fresh native Companion diagnostics after one controlled Node reconnect attempt.** Use Diagnostics → Connection event timeline and Recent log. Preserve the precise ownership-inspection rejection and its preceding status/handshake events. Do not share tokens or raw settings.
3. **Compare the running package and Gateway contract against the official Windows packaging release/issue tracker.** Only apply an official package update if a newer compatible package or explicit upstream fix is confirmed. Do not reinstall the same package speculatively.
4. **Retest the native desktop path.** Require Gateway connected, Operator connected, Node `1/1` online and a safe Node operation to succeed from the desktop app. The browser ACP `READY` result does not substitute for this.
5. **Complete one disposable coding task through ACPX.** Verify workspace scope, changed files, test output, result return, cancellation and no cloud/paid fallback.
6. Continue to inspect the installed OpenJarvis MCP surface and complete the separate OpenClaw → OpenJarvis MCP test only after its installed-build support is confirmed.

## 8. Resume commands and shell context

The two Windows shells are different and must not be confused:

- Normal host shell: `PS C:\Users\<user>>` — `clawctl` commands run here.
- Isolated OpenClaw shell: `[openclaw T3-P2] ...>` — `openclaw`, `node`, `npm` and the T3-P2 OpenCode installation run here; `clawctl` is not on its PATH.

Useful read-only checks already proven:

- Normal host shell: `clawctl status`
- Normal host shell: `clawctl gateway-service status --json`
- Normal host shell: `clawctl companion prepare --check --json`
- Isolated shell: `opencode --version`
- Isolated shell: `opencode models`
- Isolated shell: `opencode debug config`
- Isolated shell: `ollama ps`

Keep commands as single-line PowerShell commands for this user. Do not print or paste gateway auth tokens, device tokens, API keys, SIDs or raw credential stores into the repository or chat.

---

**Handoff outcome:** The local model path and browser ACP proof are preserved. The immediate blocker for the native Windows app is the Companion's separate Node ownership/credential-handoff check, not the working browser ACP path. Resume at **Exact next action 1** above.


## 9. Continuation checkpoint — 12 November 2026, 09:59 AEST

This section records the later Windows checks and the additional OpenJarvis repair/build evidence supplied after the initial handoff. It supplements the earlier findings; it does not close the native Companion blocker.

### Latest Windows / Gateway checks

- Windows: Windows 11 Pro, version `10.0.26300`, build `26300`, 64-bit. The earlier registry query reported UBR `9711`.
- `Get-AppxPackage` filtered to `OpenClawFoundation.OpenClaw*` returned only `OpenClawFoundation.OpenClawGateway`, package version `2026.11.100.0`, full package name `OpenClawFoundation.OpenClawGateway_2026.11.100.0_x64__rfcbke2p71se2`.
- The separately observed Add/Remove Programs entry remains OpenClaw Companion version `2026.9.8-1`.
- The running Companion App Info screen had shown `v2026.11.1`, build date 7 November 2026, install type `Unpackaged (developer)`. The active process executable path has **not** yet been matched to the registered `2026.9.8-1` entry. Do not uninstall either copy until that mapping is established.
- The Gateway continues to report `running`, port `50368`, `isolated-session` integration version `1`, and ownership present.
- `clawctl status --json` returned `State=running`, `Port=50368`, `OwnershipPresent=True`, `Integration=isolated-session`, `Version=1`.
- `clawctl gateway-service status --json` returned schema `1`, command `gateway-service status`, Gateway launch version `1`, attempt ID present and valid GUID format, ownership present, sandbox ID present, account SID field present, and exactly one owned listener.
- The detailed listener check returned port `50368`, PID `25904`, valid start-time parse and sequence number. Windows TCP inspection independently showed exactly one loopback listener: `127.0.0.1:50368`, owned by PID `25904`.
- `clawctl companion prepare --check --json` returned schema `1`, `ok=true`, integration `isolated-session v1`, companion port `50368`, and token configured. Only the boolean presence was recorded; token contents were not displayed or saved.
- A Windows process-owner/start-time comparison using CIM was inconclusive: the owner query returned an empty value and process start-time conversion failed on one attempt. These results are **not** evidence of an SID mismatch. A later `Get-Process -Id 25904` did find a running `node` process, and Windows' TCP table showed it listening on the expected port.
- The Companion Connection page still showed Gateway and Operator connected, Node mode enabled, but the Windows Node in Error/offline state. The technical-details page displayed approved/effective capabilities (browser, camera, canvas, device, local inference, screen and system); this proves configured permissions, not a live Node connection.
- The reported Node error remains `Gateway ownership inspection failed` / earlier `The installed Gateway MSIX does not expose Companion's isolated-session contract`; credentials were not sent. Diagnostics showed `0/1` Nodes online. Gateway/Operator reachability and the browser ACP path must not be mistaken for successful native Node registration.
- One Gateway restart was attempted during troubleshooting, but it did not resolve the Companion Node error. The Gateway was subsequently verified running again. Do not repeat restarts, reset pairing or regenerate credentials without a specific evidence-based reason.

### OpenJarvis source/build evidence supplied separately

These records concern the existing local `C:\Users\Boxont\OpenJarvis` checkout and a separate temporary repair-build copy. They are included for continuity; they do **not** mean the OpenJarvis code or compiled desktop binaries were committed to this repository.

1. **Hidden-console patch attempt, 8 November 2026:** the repair log records backups of the existing Tauri source and desktop EXE, SHA-256 values `A728EB029A7CAD8C7658A982AAA55BEB798AAD79CB2668444CEF2DFC0CF25F4F` (source) and `085244CCEFF72B00AC05F50515036481C58B5640A03C04340C0BCF0DB6AF2D0C` (EXE). The attempted source patch added `CREATE_NO_WINDOW` to the shared managed child-process launcher (four call sites, affecting helper launches such as `uv.exe` and `ollama.exe`, not the desktop window). The first build attempt failed and the log says the original source was restored and verified.
2. **Second hidden-console attempt:** a second log shows the same backups and patch, then a Cargo offline build. A separate captured Cargo stdout file reports `Compiling openjarvis-desktop v1.0.2` followed by `Finished release profile [optimized] target(s) in 49.66s`. The available log set does not confirm a final installed executable hash, a successful launch of the patched executable, or a verified no-console runtime. Treat this as a successful Cargo compilation record only, not a verified repair/release.
3. **Separate repair build copy:** `OpenJarvis-Repair-493725251.log` records the frontend TypeScript/Vite stage succeeding (`3509 modules transformed`), but the native Rust build failed in `web_atoms v0.2.5` build script with Windows error code `5` (`Access is denied`). That attempt used a separate `C:\Users\Boxont\Desktop\OpenJarvis-Repair-Build-493725251` path and did not produce a verified installer. Do not conflate this with the normal OpenJarvis source checkout.
4. No new OpenJarvis installer or MSI was verified in these logs. The current local source tree is known to contain custom/dirty changes and must be preserved. No `git reset`, `git clean`, bulk staging, overwrite or forced push was performed in this session.

### Updated exact next actions

1. From normal Windows PowerShell, identify the **running Companion process only** (process name, PID and executable path). Use this single-line read-only command: `Get-CimInstance Win32_Process | Where-Object { $_.Name -match 'OpenClaw' } | Select-Object ProcessId,Name,ExecutablePath`. Compare the executable path with the registered `OpenClaw Companion 2026.9.8-1` uninstall entry and the App Info screen showing unpackaged/developer `v2026.11.1`. Do not remove either copy.
2. Capture one fresh Companion Connection event timeline and Recent log after a controlled Node reconnect attempt. Keep tokens, device credentials, SIDs and raw settings redacted.
3. Compare the active executable/package identity with the official Windows Node/Companion and Gateway MSIX release channels. Do not install a prerelease or reinstall the same Gateway package speculatively.
4. Retest native desktop registration: Gateway connected, Operator connected, Node online `1/1`, and one harmless permitted Node operation verified from the desktop app.
5. Only after the native path is understood, complete a disposable coding task through browser ACPX and verify files, tests, scope, return evidence and cancellation; then inspect the installed OpenJarvis MCP surface.
6. The local OpenJarvis source/build artefacts and their repair logs remain local evidence. They have **not** been committed as application source or binaries to `jarvis-os`; only this sanitized troubleshooting record is being synchronised here.

**Current outcome:** Gateway status and Companion preparation/ownership fields pass their read-only checks; native Companion Node credential handoff remains blocked. Local Qwen and browser ACPX proof remain separate verified paths.

## 10. Upstream issue and release cross-check — 12 November 2026

This section records public upstream evidence checked after the Windows snapshot above. It is diagnostic context, not proof that any one upstream defect is the cause on this PC.

### Related upstream reports

1. **[openclaw-windows-node #1691 — Companion cannot connect: Gateway MSIX missing isolated-session contract](https://github.com/openclaw/openclaw-windows-node/issues/1691)** remains open and was updated on 11 November. Its discussion contains a source-supported multi-listener failure path: the Windows Gateway package's status selector can omit a configured Gateway port when more than one observed listener exists; the ownership block is then omitted, and Companion reports the generic missing-contract error. One later report in the same issue describes Gateway MSIX 2026.11.100.0 with both gateway.port and ownership missing. The issue discussion also contains a locally deployed development-package recovery, but that is not an official stable package fix.

   **Comparison with this PC:** the user's captured clawctl status --json reported State=running, Port=50368, and OwnershipPresent=True; clawctl gateway-service status --json reported one listener, port 50368, PID 25904, a valid process-start timestamp and sequence number; Windows TCP inspection independently showed one listener at 127.0.0.1:50368. Those observations do not reproduce the reported missing-port/multiple-listener state. They do not prove that every later Companion preflight response is valid.

2. **[openclaw-windows-node #2020 — Misleading missing-contract error hides native Gateway response validation failures](https://github.com/openclaw/openclaw-windows-node/issues/2020)** remains open. It documents that the same generic "does not expose the isolated-session contract" message can be emitted after the initial integration-contract probe succeeds, when a later lifecycle response is malformed or missing a required field. The issue specifically warns that top-level clawctl status --json does not exercise every later decoder. The exact rejected operation/field must therefore be captured; the generic error alone cannot distinguish an unsupported Gateway package from a later malformed response.

3. **[openclaw-windows-node PR #2114 — Gateway setup reports a missing contract when a package response is invalid](https://github.com/openclaw/openclaw-windows-node/pull/2114)** is open and has not been merged. Its proposed change reports the failing clawctl operation and missing/rejected field instead of incorrectly advising a Gateway MSIX update, while continuing to withhold credentials. The PR reports successful synthetic-response tests and local build/test runs, but explicitly does not verify a real Gateway MSIX, a shipped Companion UI, or a native/WSL end-to-end path. Its latest review requests a P2 change to localize the new user-facing text through the native resource system. Treat it as a diagnostic proposal, not an available user fix; do not install its branch or assume it repairs the underlying connection.

### Stable release identity cross-check

- The [Windows Gateway packaging releases](https://github.com/openclaw/openclaw-windows-packaging/releases) list v2026.11.1-msix.0, released 5 November 2026, with payload OpenClaw 2026.11.1 and x64 MSIX OpenClawGateway-2026.11.1-msix.0-x64.msix. Its numeric MSIX package identity corresponds to 2026.11.100.0, the Gateway package installed on this PC.
- The [Windows Companion releases](https://github.com/openclaw/openclaw-windows-node/releases) list stable v2026.11.1, released 7 November 2026. The same page also lists a newer v2026.11.2-alpha.10 prerelease; do not treat that alpha as a stable repair.
- Therefore, the Gateway package version 2026.11.100.0 is not evidence of an old Gateway payload: it is the package identity for the stable 2026.11.1 Gateway release. The running Companion's App Info also reported v2026.11.1 and "Current". The separate Add/Remove Programs record 2026.9.8-1 may be a leftover/other installation, but that is not yet proven. Do not describe the active Companion as outdated until its running executable path is mapped to the registered uninstall entry.

### Updated interpretation and next action

- Discard the earlier SIDMatches=False output: Windows returned a blank process owner and no readable process start time, so the comparison did not run successfully and is not evidence of an account/SID mismatch.
- The Gateway listener, base status and detailed ownership fields all passed the user's recorded checks. Do not repeat a Gateway restart, reinstall, token reset, pairing reset or credential change based on the generic message alone.
- **Next read-only Windows check:** run this while Companion is running: `Get-CimInstance Win32_Process | Where-Object { $_.Name -match 'OpenClaw' } | Select-Object ProcessId,Name,ExecutablePath`. Compare the active executable path with the App Info version and the registered 2026.9.8-1 uninstall record. This identifies which Companion build is actually running without changing either installation.
- After that identity check, capture a fresh Companion Connection timeline and Recent log for a single controlled Node reconnect attempt. Preserve the exact failed operation/field where available; redact tokens, SIDs, device identifiers, raw settings and private paths.
- Keep the native Node task **BLOCKED** until Gateway, Operator and Node are all connected (1/1) and a harmless permitted Node action succeeds from the native desktop app.

**Source boundaries:** the upstream issue reports and PR are evidence of plausible failure classes and current project work. They do not establish which class caused this PC's error. The local listener/status observations remain the stronger evidence about the state actually measured on this PC.

## 11. Active Companion executable and live UI state — 12 November 2026

### Active executable and version — verified from user-provided Windows output

The process/version query returned:

- OpenClaw.Tray.WinUI.exe, PID 4776.
- Executable: C:\Users\Boxont\AppData\Local\OpenClawTray\OpenClaw.Tray.WinUI.exe.
- File version: 2026.11.1.0.

The Companion About screenshot independently shows:

- App name: OpenClaw Windows Companion.
- Version: v2026.11.1.
- Build date: 7 November 2026.
- Runtime: .NET 10.0.14 / WinUI 3 / Windows App SDK 2.6.4.
- Architecture: x64.
- Windows: 10.0.26300.0.
- Update channel: stable.
- Install type: Unpackaged (developer).

This confirms the active desktop Companion is the stable 2026.11.1 build. The separate Add/Remove Programs entry 2026.9.8-1 is not proof that the older version is running; its relationship to the active unpackaged app remains unknown.

The broad process command also encountered Get-Item error "Cannot bind argument to parameter 'Path' because it is null" for openclaw-session-host.exe, PID 2780, whose ExecutablePath was blank. The PowerShell pipeline continued and returned the separate Companion executable and its version successfully. Treat the session-host path as unavailable, not as a Companion version failure.

### Fresh runtime status

The user's latest clawctl status output reports:

- Session: running.
- Agent: T3-P2.
- Shared folder: C:\Users\T3-P2\Shared.
- Runtime: Node.js 24.22.1.
- Gateway: running on port 50368.
- Activation: none pending.
- Recovery: configured.

### Companion UI state — native Node still failing

The latest screenshots show:

- Tray/status menu: Connection degraded · 127.0.0.1:50368.
- Node inventory: 0/1 node.
- Session count: 9 sessions; two sessions were visible in the menu (Main session and Direct message).
- About page: active stable v2026.11.1 as above.
- Connection page: overall status Connection degraded.
- Saved Native Gateway record: ws://127.0.0.1:50368/, paired via device token, UI status Connected.
- Operator: Reconnecting...
- Node mode: enabled, but Windows Node remains in error/offline state.
- Visible failure: Gateway ownership inspection failed. Check the installed Gateway package and retry. Credentials were not sent.
- The node capability chips displayed warnings for Browser control, Camera, Canvas, Screen capture and Share Windows Ollama. A warning badge is not proof that the corresponding capability is independently broken; the Node registration itself has not completed.

This means the active Companion version is no longer an open question, but the native Node ownership/credential-handoff failure remains. clawctl status reporting a running Gateway and the UI marking the saved Gateway record Connected do not prove that the separate Windows Node has registered.

### Next action

1. In the Companion, open Diagnostics.
2. Capture the Connection timeline and Recent log around one controlled Node reconnect attempt.
3. Share only the relevant error lines and event sequence. Redact tokens, device IDs, SIDs, credentials, raw settings and private paths.
4. Identify the exact failing preflight/operation/field before selecting a package or code repair.

Do not reinstall the Companion based only on the stale/unmapped 2026.9.8-1 Add/Remove Programs record. Do not restart or reinstall the Gateway, reset pairing/tokens, or weaken ownership checks based on the current evidence. Keep this task BLOCKED until the native UI shows Node 1/1 online and a harmless permitted Node action succeeds.

**Outcome:** The currently running Companion is verified as stable v2026.11.1; Gateway runtime reports running on port 50368; the desktop connection remains degraded and Windows Node is still offline. The process-path null error was limited to the separate session-host process and does not invalidate the Companion executable/version result.
