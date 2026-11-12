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

### Existing diagnostics review — no repeated export required

The Library already contains openclaw-diagnostics-20261112-004308.txt, generated 12 November 2026 at 00:43 +10. This is the bundle to use; do not ask the user to reopen Diagnostics or generate another export.

The bundle's Connection Event Timeline proves this sequence:

1. The Operator completes hello-ok; the Gateway returns the device token with operator.admin and operator.pairing scopes, and the WebSocket connects.
2. The separate Node credential source resolves as identity.NodeDeviceToken (IsBootstrap=False, Status=Resolved, no fallback).
3. The Node client is created, its service is present, and it attaches 7 capabilities / 26 commands.
4. The Node WebSocket connects and receives the Gateway connect.challenge.
5. Companion then blocks the credential handoff with: The installed Gateway MSIX does not expose Companion's isolated-session contract. Credentials were not sent. It retries once and remains in Error.

This excludes a simple missing-token, bad-token-resolution, or basic TCP-reachability explanation. The Node reaches the Gateway challenge; credentials are withheld because the package/ownership preflight has not been accepted.

The bundle's 9 November native setup log also records:
- clawctl companion prepare --check --json exited 0.
- clawctl gateway-service status --json exited 0, but Companion's summary repeatedly said gateway running, session unreported, readiness unreported.
- The Gateway listener was independently verified on port 50368 (PID 26416 in that earlier attempt).
- openclaw.exe config validate --json returned valid: true, with no warnings.
- A package-managed Gateway stop/start was performed in that setup attempt; do not repeat it as a generic troubleshooting step.

The current screenshots are later than that bundle and show a different, more generic message: Gateway ownership inspection failed. Credentials were not sent. Current Companion source (IsolatedGatewayRuntime.cs, InspectAsync) catches several inspection failures (InvalidOperationException, IOException, Win32Exception, COMException, UnauthorizedAccessException, TimeoutException), logs only the exception type, and replaces the detail with that generic UI text. Therefore the screenshot confirms the ownership-inspection path is failing, but does not reveal which exception or response field caused it.

### Current upstream source and matching report

1. Companion parser requirements: current NativeGatewayPackageClient.StatusAsync invokes clawctl gateway-service status --json, requires integration metadata, a running gateway.state, gateway.port, an ownership object with sandboxId and agentUserSid, an ownership listeners array, and each listener's port, processId, processStartTimeUtc, and sequenceNumber. Missing or wrong fields cause validation exceptions. This is a much narrower contract than merely having a running Gateway or successful WebSocket challenge.

2. Known packaging selector defect remains on current main: current openclaw-windows-packaging Program.cs selects the status port only if result.Record.ObservedPorts contains exactly one entry (lines 1095–1097; fetched main blob d9fd53f295d636cc8b9568d432bf1fc4cf9b42d0). With multiple observed ports, the command result has no selected port, and ClawCtlJson cannot serialize full ownership tied to that port. The Companion parser then rejects the later gateway-service status response. This is a source-supported failure path, but the user's separate manual snapshot reported one listener and Port=50368, SandboxIdPresent=True, AgentSidPresent=True, ListenerCount=1, valid process start time and sequence. Therefore the multi-listener selector bug is a strong candidate to compare, not a confirmed explanation for this machine. A TCP listener count outside the isolated session is not automatically the same thing as the package's ObservedPorts set.

3. Upstream issue #1691 has an unusually close report (11 November): reporter uses Gateway MSIX 2026.11.100.0 / payload 2026.11.1 and Companion v2026.11.1 (also tested Store Companion 2026.11.102.0), with the same installed Gateway MSIX does not expose contract / Credentials were not sent message. They report integration.kind=isolated-session, version 1, and running state but no gateway.port and no ownership in clawctl status --json / gateway-service status --json; clawctl companion prepare --check --json still returns a port. They could not inspect listener count from the human account. This strongly matches the installed-version pair and symptom, but is another user's report, not direct proof of the exact local response.

4. Upstream issue #2020: the current Companion's generic unsupported-contract message can also be emitted when the initial integration probe succeeds but a later lifecycle response is missing a required field, has the wrong type, or has a schema/command mismatch. The top-level clawctl status --json passing does not validate the later gateway-service status response. The local diagnostic bundle does not contain the raw package JSON returned to Companion, and the later manual presence summary conflicts with the possibility that gateway.port / ownership were missing in that same invocation. Do not assume the multi-listener explanation without reconciling which exact command context returned the fields.

5. PR #2114 remains open / needs changes: it changes the Companion decoder and error presentation to name the exact clawctl operation and missing/rejected field while still withholding credentials and avoiding re-probes. It reports synthetic-response unit tests and full local test runs, but no real Gateway MSIX or shipped Companion end-to-end verification. Its review requires new user-facing text to go through native localization resources. It is a diagnostic/classification improvement, not a fix for the packaging-side missing-port defect. Do not install its branch or treat it as a released repair.

### Next step and user burden

- No further diagnostics export, screenshot, version check, Gateway restart, reinstall, token reset, pairing reset, or ownership bypass is needed at this stage.
- Continue by tracking the producer-side Gateway package fix and the Companion diagnostic-classification fix, and compare official stable release artifacts against the current main source before recommending any upgrade.
- Only request a single narrow, non-secret status-output comparison if it is necessary to reconcile the existing manual field-presence checks with the failing Companion inspection. Do not ask the user to repeat the full diagnostic workflow.
- Keep native Node BLOCKED until the desktop app shows Node 1/1 online and a harmless permitted native Node action succeeds.

**Outcome:** the exact failure stage is narrowed: the Node reaches Gateway challenge, but Companion refuses to release its Node credential because isolated-session ownership preflight is failing. The exact local rejected field/exception remains unproven. The correct next move is upstream contract/diagnostic work, not another user-facing round of basic diagnostics.

## 12. Diagnostic bundle and upstream failure-path comparison — 12 November 2026

The full interpretation and source comparison are recorded above. Key results:

- Existing Library diagnostics already proves the Operator hello-ok and Node challenge path; no repeat export is required.
- The NodeDeviceToken resolves before the challenge. The handoff is denied only after the challenge because the Companion's isolated-session ownership preflight fails.
- The setup log already includes a package-managed Gateway stop/start and confirms the Gateway listener and configuration validity. Do not repeat it.
- The current UI's generic Gateway ownership inspection failed message is emitted by Companion's IsolatedGatewayRuntime.InspectAsync catch path, which collapses several inspection/validation exceptions and logs only exception type.
- Current parser requires gateway.port and full ownership/listener process identity. Current packaging main selects the port only when the observed-port set contains exactly one entry. This is a confirmed upstream source defect for multi-listener status, but the user's one-listener manual snapshot with ownership fields present means it is not yet proven to be the precise local cause.
- Upstream issue #1691 has a 11 November report using the same exact Gateway MSIX 2026.11.100.0 and Companion v2026.11.1 pair with the same error and missing gateway.port/ownership. Issue #2020 records the broader generic-error classification defect.
- PR #2114 would name the failed operation and rejected field while retaining credential withholding; it is still open, blocked on localization review, and has not been tested with a real Gateway MSIX or shipped Companion.
- No user action now: do not request another diagnostics export, screenshot, version check, Gateway restart, reinstall, token reset or pairing reset. Keep native Node blocked and continue upstream producer/consumer fix verification.

## 13. Official release check — 12 November 2026

A fresh release/source check was completed after reviewing the existing diagnostics. No supported stable package update is presently available for this machine.

- Gateway packaging releases: the latest published stable release page is v2026.11.1-msix.0, released 5 November 2026. It packages OpenClaw 2026.11.1 and its numeric MSIX identity is 2026.11.100.0 — exactly the installed Gateway package. The listed release changes concern Hyper-V checks and staged-package dependency resolution, not the observed-port/ownership status selection. There is no later stable Gateway MSIX on the published releases page.
- Companion releases: stable v2026.11.1 was promoted 7 November 2026, matching the active Companion. v2026.11.2-alpha.10 is explicitly a prerelease (8 November); do not recommend it as a repair.
- Current packaging main still uses the exactly-one-observed-port selection in Program.cs (fetched blob d9fd53f295d636cc8b9568d432bf1fc4cf9b42d0): `ObservedPorts is { Count: 1 }`. README documents that running ownership is included only when a single port and its isolated-session listener identities are observed. Therefore the multi-listener status omission is a known upstream failure mode, but it remains unproven on this PC because the user's earlier manual command reported one listener and ownership/listener identity fields present.
- Targeted GitHub search found no open packaging PR explicitly matching ObservedPorts. Recent packaging main commits concern restart handoffs, beta releases, diagnostics context and fixture/test changes; none of the inspected current Program.cs lines change the selected-port rule.
- Companion PR #2114 remains open, labelled waiting on author, with a review request to localize its new user-facing detail. It would make a malformed later response identify the exact operation/field while continuing to withhold credentials; it does not repair the packaging source or prove this PC's precise failure.

### Decision

Do not update/reinstall Gateway or Companion now: installed versions already match the latest stable releases, and no stable Gateway MSIX with the suspected selector repair is published. Do not sideload the newer Companion alpha, install PR #2114, restart Gateway again, or reset tokens/pairing.

### One remaining local discriminator — targeted and read-only

If another local result is needed, request only a safe summary of the current `clawctl gateway-service status --json` response. Print the integration kind/version, gateway state, whether gateway.port exists, whether ownership/sandboxId/agentUserSid exist, listener count, and whether each listener contains port/processId/processStartTimeUtc/sequenceNumber. Do not print any token, SID, sandbox ID value, URL, raw JSON, or credential. This distinguishes a missing producer response field from a later failure in Companion's own Windows listener/process snapshot. The previous manual presence summary was not timestamp-aligned with the latest Companion inspection, so a single fresh summary would close that gap.

No further full diagnostics export is needed. Preserve the current Node token and pairing. Keep native Node BLOCKED until 1/1 online and a harmless permitted native action succeeds.

## 14. Fresh Gateway contract shape passes — next isolate Companion's local Windows ownership proof (12 Nov 2026)

User ran the targeted, read-only `clawctl gateway-service status --json` shape check. It returned:

- `Ok=True`
- `Integration=isolated-session`
- `IntegrationVersion=1`
- `State=running`
- `PortPresent=True`
- `OwnershipPresent=True`
- `SandboxIdPresent=True`
- `AgentSidPresent=True`
- `ListenerCount=1`
- `ListenerFieldsComplete=True`

The command printed only booleans/counts, not token, SID value, sandbox ID value, or raw JSON. This is strong evidence that the current Gateway package response contains the required producer-side fields and that the current invocation is not losing its port due to the multiple-observed-port selector. It does not prove the Companion's independent Windows process/listener proof passes.

### Exact remaining Companion check in current source

`NativeGatewayPackageClient.StatusAsync` accepts the package shape above when the ownership object contains the process identities. `IsolatedGatewayRuntime.InspectSnapshot` then independently:

1. Calls `WindowsTcpListenerSnapshot.Capture()` and requires complete IPv4 and IPv6 listener tables.
2. Finds the live TCP listener(s) for the selected Gateway port and requires at least one.
3. Requires the package-attested Agent SID.
4. Calls `WindowsProcessSequenceSnapshot.Capture()` and requires a sequence number for every live listener PID.
5. Requires each listener to be loopback and the `(port, processId, sequenceNumber)` tuple to match a package-attested listener.
6. Captures the listener table and process sequences a second time and requires it to remain unchanged during verification.

The current UI's generic `Gateway ownership inspection failed` is emitted if an exception from this inspection escapes into `InspectAsync`; normal failed comparisons return more specific internal details, but the current catch hides exceptions such as `Win32Exception` and `COMException` behind generic UI text. Earlier CIM GetOwner / start-time calculations in the user's diagnostics were invalid/inconclusive; do not treat them as a proven SID mismatch or repeat those same calculations.

## 15. Listener PID matches; validate the Windows process-sequence API (12 November 2026)

User ran the targeted, read-only package-vs-Windows listener comparison for Gateway port 50368. It returned:

- Package-attested listener PID: 16208
- Windows TCP listener PID: 16208
- `PIDMatch=True`
- `WindowsListenerCount=1`
- `ProcessVisible=True`
- `StartTimeReadable=False`
- `StartTimeDifferenceSeconds=null`

This confirms the package-reported PID corresponds to the one live Windows listening socket. The result does not indicate a stale or mismatched PID. The PowerShell process start-time read was denied/unavailable, so no timestamp comparison can be made.

### Why the unreadable start time is not itself a failure

Current Companion source `WindowsProcessSequenceSnapshot.cs` explicitly says its SystemBasicProcessInformation approach provides a PID-reuse-proof identity without opening the isolated agent's process handle, because that handle's DACL denies access to Companion. The implementation calls `NtQuerySystemInformation` with information class 252, retries a bounded buffer on `STATUS_INFO_LENGTH_MISMATCH`, and reports unsupported Windows when the API returns `STATUS_INVALID_INFO_CLASS`. It parses the process table and obtains the process sequence number; it does not rely on `Get-Process.StartTime`.

Source: https://github.com/openclaw/openclaw-windows-node/blob/main/src/OpenClaw.Connection/NativeGateway/WindowsProcessSequenceSnapshot.cs

Microsoft documents `SystemBasicProcessInformation` as available starting with Windows 11 version 26100.4770; its sequence number is intended to detect PID reuse. The installed Windows build previously reported as 26300 is newer by base build number, but the exact API outcome still needs a live check rather than assumption.

Source: https://learn.microsoft.com/en-us/windows/win32/api/winternl/nf-winternl-ntquerysysteminformation

### Next narrow, read-only check

Test whether `NtQuerySystemInformation(252)` succeeds in the user's 64-bit PowerShell process and whether the returned process table contains PID 16208 with a non-zero sequence number. Print only API status, table-validity, PID-present and sequence-nonzero booleans; do not print the sequence value, SID, sandbox ID, token, raw JSON or private paths. This will directly test the same OS primitive used by Companion.

No diagnostics export, Gateway restart, reinstall, token reset, pairing reset, config change, ACL change or permission workaround is justified. Keep native Node BLOCKED until the desktop app reports Node 1/1 online and a harmless permitted native action succeeds.


## 16. Windows process-sequence API succeeds; compare package and OS identity (12 November 2026)

User ran the targeted single-line read-only process table probe. Result:

`ListenerPID=16208; API=OK; TableValid=True; GatewayPIDPresent=True; SequenceNonZero=True`

This proves the user's 64-bit PowerShell process can call `NtQuerySystemInformation(252)`, parse a valid process table, find the live Gateway listener PID 16208 and read a non-zero process sequence number. The OS API is supported and functioning for the relevant PID. Combined with the previous `PIDMatch=True` result, the listener PID is consistent across the package attestation, Windows TCP ownership and Windows process table.

### Remaining identity comparison in current Companion source

Current `IsolatedGatewayRuntime.InspectSnapshot` checks every listener on the selected port for all of the following:

1. Both IPv4 and IPv6 TCP listener snapshots must be complete.
2. At least one listener must exist on the selected port.
3. Package status must attest a non-empty Agent SID.
4. Each live listener must be loopback.
5. The Windows process-sequence table must contain that listener PID.
6. The tuple `(port, processId, sequenceNumber)` must match an entry in the package-attested listener list.
7. A second TCP-listener and process-sequence snapshot must be complete, preserve the listener count/address/PID set, and preserve every PID's process sequence number.

The previous probe only verified that the OS sequence exists and is non-zero. It did not compare the actual sequence value with the package's `sequenceNumber`. Do not expose either sequence value to the user; the next targeted command should return only match booleans and listener counts.

Source: https://github.com/openclaw/openclaw-windows-node/blob/main/src/OpenClaw.Connection/NativeGateway/IsolatedGatewayRuntime.cs

### Current evidence state

- Gateway contract shape: passed (all required fields, one complete listener).
- Package PID vs Windows listener PID: passed (16208 == 16208; one listener).
- Windows sequence API: passed (valid table, PID present, non-zero sequence).
- Package sequence vs Windows sequence equality: not yet checked.
- IPv4/IPv6 listener table completeness and repeated-snapshot stability: not yet checked by a same-method local test.
- Companion Node remains BLOCKED until its UI reports 1/1 online and a harmless permitted native action succeeds.

No restart, reinstall, credential/token change, pairing reset, ACL change, elevation or broad diagnostics export is justified. The next user action is only the non-secret equality check described above.


## 17. Package and Windows process identity tuple matches (12 November 2026)

User ran the one-line, read-only sequence comparison against the current `clawctl gateway-service status --json` response and the Windows `NtQuerySystemInformation(252)` process table. It returned:

`PIDMatch=True; API=OK; TableValid=True; GatewayPIDPresent=True; SequenceNonZero=True; SequenceMatches=True`

Combined with the preceding checks:

- Gateway contract response contains all required fields and one complete package listener.
- Package listener PID and Windows TCP listener PID both equal 16208.
- Windows process table contains PID 16208.
- Windows process sequence is non-zero and exactly matches the package-attested `sequenceNumber`.

Therefore the central process identity tuple `(port, processId, sequenceNumber)` matches for the current listener. PID reuse, a missing process table entry, unsupported Windows sequence API, or a package-vs-OS sequence mismatch are not supported explanations for the current failure.

### Remaining Companion inspection conditions

Current `IsolatedGatewayRuntime.InspectSnapshot` also requires:
- complete IPv4 and IPv6 listener tables from the Windows IP Helper API;
- every listener on the chosen port to be loopback and match a package-attested PID/sequence tuple;
- a second listener snapshot with complete IPv4 and IPv6 tables, the same port listener count and address/PID set, and unchanged process sequence values.

These exact listener snapshot/address checks have not yet been independently validated by the user's command outputs. The generic UI error should not be attributed to them until tested; other code paths, lifecycle state and inspection timeout remain possible.

Source: https://github.com/openclaw/openclaw-windows-node/blob/main/src/OpenClaw.Connection/NativeGateway/IsolatedGatewayRuntime.cs

### Next action

Run one bounded, read-only check of two IP Helper TCP-listener snapshots and two process-sequence snapshots for the current Gateway port, returning only completeness, loopback, package identity and stability booleans. No credentials, SID, sandbox ID, sequence values or raw JSON should be printed.

Do not restart Gateway, reinstall either package, reset pairing/tokens, edit ACLs or grant elevated permissions. Native Node remains BLOCKED until Companion shows Node 1/1 online and a harmless permitted native action succeeds.


## 18. Use Companion's own retry to run the final production listener proof (12 November 2026)

After the user's latest check, the Gateway package and Windows agree on the complete listener process identity tuple:

`PIDMatch=True; API=OK; TableValid=True; GatewayPIDPresent=True; SequenceNonZero=True; SequenceMatches=True`

The current source's remaining `InspectSnapshot` requirements are complete IPv4 and IPv6 IP Helper listener tables, loopback-only listener addresses, and a stable second listener/process-sequence snapshot. Rather than adding another external PowerShell reproduction (which cannot prove the exact result inside the active Companion process), the next functional test should be the existing Companion Node Retry action once. It will invoke the real production inspection path with the current package status, Windows listener snapshots and process sequence tables.

This is not a Gateway restart, reinstall or pairing/token reset. If retry succeeds, verify the Companion UI shows Node 1/1 online and then run one harmless permitted native Node action. If the same error persists, record the exact UI message and keep Node BLOCKED; do not weaken the ownership proof or bypass credential withholding.

Current evidence:
- Contract shape: pass.
- Package PID == Windows TCP listener PID: pass (16208).
- Windows process sequence API: pass.
- Package sequence == Windows process sequence: pass.
- Loopback / IPv4+IPv6 completeness / second snapshot stability: not independently proven; Companion Retry is the authoritative end-to-end test.


## 19. Upstream diagnostic PR CI and review status (12 November 2026)

A fresh read of upstream PR [#2114](https://github.com/openclaw/openclaw-windows-node/pull/2114), issue [#2020](https://github.com/openclaw/openclaw-windows-node/issues/2020), and the PR's GitHub Actions results adds the following status:

- PR #2114 is still **open and unmerged** at head `865a61892a6132a7876840c4de8e01767076c808`. It changes Companion's decoder/error surface so a malformed later Gateway response can identify the `clawctl` operation and rejected field, rather than falsely implying the initial isolated-session contract is absent. It retains credential withholding and does not re-probe to explain the error.
- CodeQL for the PR head completed successfully (run `43051640502`). The Build and Test workflow (run `43051640650`) failed its required CI gate. The Core/CLI job and Tray/setup/integration job passed; the fast-validation job passed.
- Three WSL end-to-end jobs failed before exercising their target scenarios because the CI runner could not resolve the Ubuntu 24.04 download server: `Wsl/InstallDistro/WININET_E_NAME_NOT_RESOLVED`. The Setup and Connect E2E job reported 24 of 71 tests failed because the shared E2E setup fixture could not provision its fresh WSL distro. Revocation-recovery and network-recovery E2E jobs hit the same WSL provisioning failure. This is evidence of an environment/provisioning blocker in those jobs, not evidence that the focused decoder tests failed; it still means the overall Build and Test workflow and CI gate are red.
- The latest PR review still has one P2 finding: localize the new user-facing error/recovery text through the native `.resw` resource owner. The PR's own evidence also says real Gateway MSIX behavior, shipped Companion rendering, and native/WSL end-to-end behavior are not verified.
- This is a **diagnostic-classification proposal, not a connectivity repair or supported release**. Do not install the PR branch, sideload it, or change the user's installed packages based on it. Issue #2020 confirms the old generic error may conceal a later malformed response; it does not identify this PC's exact rejected field.

### Local evidence and decision unchanged

The user's latest read-only checks still show a running Gateway on port 50368, complete isolated-session contract fields and one listener; the package and Windows listener PID match (16208), and the Windows process sequence matches the package-attested sequence. The existing diagnostic bundle still establishes Operator `hello-ok`, resolved NodeDeviceToken, Node challenge received, then credential withholding by Companion's ownership preflight. No evidence identifies the precise failing field or proves that the upstream multi-listener producer defect is occurring in the same failing invocation.

**Next action:** no further local command, export, restart, reinstall, token/pairing reset, ACL change or ownership bypass is justified. Keep native Node marked BLOCKED. Wait for a reviewed/localized diagnostic fix and, separately, a producer-side Gateway packaging fix to reach an official stable release; then verify the actual installed packages and require Node 1/1 plus a harmless permitted native action before closing this item.
