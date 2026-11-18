# OpenJarvis front-door bridge — 18 November 2026

This is dated implementation and execution evidence. **MASTER_TODO.md remains the sole priority/status authority.** Read its complete latest version and root AGENTS.md before continuing. Do not infer current readiness from this document or old chat history.


## Start here when continuing with another AI

This document is a dated execution/handoff record, not a second status tracker. Read the complete latest [AGENTS.md](../AGENTS.md), [MASTER_TODO.md](../MASTER_TODO.md) and [JARVIS_BOOT.md](../JARVIS_BOOT.md) on main first. Then read this whole record, [startup/rollback](AUTOSTART_READINESS.md), [autostart continuation](CONTINUATION_HANDOFF_2026-11-18_AUTOSTART.md) and the original handoffs required by the user: [18 November](CONTINUATION_HANDOFF_2026-11-18.md), [12 November](OPENCLAW_OPENCODE_OLLAMA_HANDOFF_2026-11-12.md), [read-only MCP](OPENJARVIS_READONLY_MCP_ADAPTER.md). Older instructions about waiting indefinitely for an official repair are superseded by the current master/user instruction; preservation, zero spend and exact-action approval boundaries still apply.

**Last completed implementation checkpoint:** [81e87ac](https://github.com/eboxont-code/jarvis-os/commit/81e87ac124e8c542fc1eb9d53ec5d7c49b0a5f5b). All33 committed files were fetched from main and compared exactly after publication. This handoff-only follow-up does not rerun health tests or change the computer. Treat all process IDs/health timestamps below as historical.

**Exact next master item:** the unchecked PARTIAL item beginning **Startup acceptance: Make the four installed applications automatically connected and ready after Windows sign-in** in Integration Phase H. Resume its fresh read-only diagnosis first. Latest recorded Node probe was ready=false, while the bounded coding bridge passed. Do not rebuild the bridge, replay its failing fixtures, start another coordinator, rerun installers or enable the plugin again.

### First actions on the original Windows computer

1. Confirm authenticated access to this private repository/main and actual authorised Windows access. A GitHub link transfers instructions/source, not computer access, GitHub credentials or blanket authority. If either access is absent, state which is missing; never fabricate machine checks.
2. Collect current boot time, running process identities, listeners8000/11434/18789 and native qualified Gateway ownership proof. Read the existing runtime's startup-last.json and runtime-health.json privately; compare boot IDs, heartbeat age and actual watchdog process. The last snapshot's watchdog22932 is not a reusable target PID.
3. Verify native OpenJarvis GUI attachment, local health and model inventory; preserve all conversations. Verify current isolated-account identity before using the recorded T3-P2 paths. Do not display raw configurations, environment values, command lines containing credentials or private job prompts.
4. Inspect bridge jobs for unfinished state, owned Code processes and jobs/unsettled.json. If shutdown is uncertain, stop submitting work and verify it; never delete claims/latches to retry.
5. Use only the existing reviewed read-only probe after confirming its file/source and current account. These commands do not start/restart apps or submit inference. The qualified launcher currently is:

```powershell
$jarvisClawctl = "$env:LOCALAPPDATA\Microsoft\WindowsApps\OpenClawFoundation.OpenClawGateway_rfcbke2p71se2\clawctl.exe"
& $jarvisClawctl gateway-service status --json
& $jarvisClawctl pwsh --command '& C:\Python314\python.exe C:\Users\T3-P2\Shared\jarvis-startup-20261118\isolated_readiness_probe.py health'
& $jarvisClawctl pwsh --command '& C:\Python314\python.exe C:\Users\T3-P2\Shared\jarvis-startup-20261118\isolated_readiness_probe.py node'
& $jarvisClawctl pwsh --command '& C:\Python314\python.exe C:\Users\T3-P2\Shared\jarvis-startup-20261118\isolated_readiness_probe.py connections'
```

The connections probe initialises/closes the existing ACP protocol and calls exactly three read-only adapter tools; it does not create a coding session or run a model. If the account/path/installed command differs or is absent, inventory the supported installation; do not fabricate missing files or override runtime paths. Report selected safe status facts, not raw credentials/configuration.

6. Diagnose the current Node failure from supported native ownership/status metadata. Preserve the successful coding bridge. If a repair needs another Gateway/Companion restart, active configuration change, install, reset, elevation or security change, prepare the concrete reversible action and request the required exact approval before execution. Do not recycle consumed approval.
7. After any specifically approved repair, rerun the relevant Node/native checks and ensure the coding bridge remains intact. Final startup acceptance requires a real normal Windows restart/sign-in and fresh evidence, with no agent intervention/reconnect/extra app launch during the acceptance observation. Do not reboot automatically from this handoff. The next AI must obtain the user's agreement before initiating a reboot that could interrupt work, or wait for the user to restart.
8. Mark the selected master item WORKING before project code changes; run relevant checks, update its actual status/live row and dated execution log, synchronise main and read it back. Keep one meaningful task active and MASTER_TODO as the sole status authority.

### Approval ledger and limits

- The port50368 →18789 move was specifically approved and completed. Do not revert into the reserved range.
- Enabling the reviewed1e887a5 local delegate and **one** supported Gateway stop/start was specifically approved and completed. The plugin is already enabled; that restart authorisation is consumed.
- The user removed the blanket wait-for-official-repair rule. This permits investigating a supported fix now; it is not a grant for token/pairing/ACL/security resets, arbitrary runtime overrides, elevated/destructive work or paid fallbacks.
- No new spending, cloud inference, subscriptions, credits, model/package downloads or upgrades are authorised. The16K alias references existing local weights only.
- Preserve original OpenJarvis checkout/customisations/config/data/models/installations and all existing backups. No broad global shell, external-directory or Windows-control grant was added.
- The runtime bridge cannot write GitHub automatically. A separately authorised operator/AI updates the master. The older prompt controller has not passed live prompt-loading acceptance.

### Source and evidence map

| Purpose | Repository source / existing local evidence |
|---|---|
| Front-door routing/auth boundary | [frontdoor.py](../runtime/frontdoor/frontdoor.py), [bootstrap](../runtime/frontdoor/backend_bootstrap.py), host runtime/frontdoor manifest |
| Authenticated native Gateway delegate | [plugin](../runtime/frontdoor/claw-plugin/index.mjs), [reviewed enable helper](../runtime/frontdoor/enable_native_plugin.py); already enabled, do not replay |
| Owned job/timeout/cancellation and native receipt verification | [gateway_job.py](../runtime/frontdoor/gateway_job.py), private Shared/jobs records |
| Installed Code ACP and guarded coding task | [acp_client.py](../runtime/frontdoor/acp_client.py), [code_server.py](../runtime/frontdoor/code_server.py) |
| Owned project boundaries and test verifier | [projects.py](../runtime/frontdoor/projects.py), [verify_project.py](../runtime/frontdoor/verify_project.py), private projects/invoice-live with protected hashes |
| Existing-weight context alias | [prepare_code_model.py](../runtime/frontdoor/prepare_code_model.py); already created, refuses existing alias |
| Login startup, backend watchdog and native checks | [start_ai_stack.py](../runtime/start_ai_stack.py), [openjarvis_watchdog.py](../runtime/openjarvis_watchdog.py), [read-only probe](../runtime/isolated_readiness_probe.py) |
| Actual success/cancel/failure details and backups | Rest of this record plus dated MASTER_TODO execution log; full private job inputs/config/backups are not uploaded |

For a simple working usage example, type in OpenJarvis: **Use OpenCode to test project invoice-live with the permitted verifier and return actual test counts.** This is an inference task, so do not run it during the first read-only inventory or an unattended reboot observation. Coding requests are confined to bridge-owned projects. Ordinary leading greetings/questions stay native Jarvis; other model-coordinator requests remain slower/unreliable. Do not promise unrestricted task planning or full Windows desktop control.


## Latest verified execution — approved native delegate enabled

The user explicitly approved enabling the reviewed local plugin in commit `1e887a5` and one supported Gateway stop/start. That approval was used once. The private pre-plugin byte backup remains inside the isolated profile. The supported offline config patch preserved existing agents, models and authentication. Native Gateway ownership/listener proof on18789 and authenticated `jarvis.frontdoor.status` passed; only then was `native-delegate.enabled` created. A finished/noncoding job was rejected live as inactive without starting Code.

**Actual four-app GUI acceptance passed:** OpenJarvis request → authenticated native OpenClaw `jarvis.frontdoor.code` → installed OpenCode ACP → existing local Ollama → same OpenJarvis assistant message. Private job `2698f37fb1444a43ab3b5e84c3242552` fixed invoice tax subtraction to addition in owned project invoice-live. Baseline had3 tests/2 failures. Only src/math.py changed; native Code edit and the exact permitted verifier exit0 were recorded. Independent verification passed3/3,0 failures,0 errors; protected files matched. Gateway acknowledged its owned worker exit, ACP exited, completion_reason=bridge_verified. Actual GUI displayed the passing file/count receipt in167.0s (Code161.2s). This route is deterministic native Gateway delegation; it does not claim autonomous Claw model planning or Windows desktop control.

The performance fix is project-scoped. A supported Ollama local alias `jarvis-code-qwen27b:16k` reuses the existing qwen3.8:27b weight blob with num_ctx16384. Four original model digests were unchanged; no weights/package/model were downloaded. Actual Code residency confirmed16,384. New owned project configs select only local Ollama, request thinking off, bound output/context metadata and disable the separate title agent. The global isolated Code document matched its pre-tuning document exactly; host protected config/source/EXE hashes matched. OpenAI-compatible request options alone had not reduced actual65K residency. Official context-alias reference: https://docs.ollama.com/api/openai-compatibility (setting local context size). The alias helper initially flagged the expected parent_model metadata difference; read-back confirmed identical physical FROM blob and16K, and verification now compares physical details/blob rather than requiring an unchanged parent label. Do not rerun creation over an existing alias or download a missing source.

**Active-Code Stop passed:** job e4fcf89c3cff48078e21d2771e1dccf4 had started Code/created its native session when GUI Stop was pressed. UI returned idle at22.7s; worker result cancelled/shutdown_confirmed=true, owned ACP exited, no unfinished jobs/unsettled latch. Protected project files remained intact and independent3/3 still passed. A subsequent ordinary greeting returned JARVIS_POST_CANCEL_OK via original OpenJarvis in11.7s. This proves cancellation/recovery for this owned job; it is not a crash/reboot test.

Sixty-three Python checks, eight native-plugin Node tests and source compilation pass. Fresh final checks: Jarvis health ok/actual watchdog healthy; native Gateway proof passes; retained three MCP tools plus Code ACP initialize/local-only checks pass; native Companion Node remains not ready. Full Windows control and actual reboot/sign-in readiness remain incomplete.

## Historical dispatch and timeout evidence — retained

Before the approved activation, model-driven Claw routing timed out before Code dispatch. A bridge-only jarvis-local provider requested16K/thinking off for the same physical27B; actual16K was confirmed but model tool discovery remained unreliable. Direct tools.invoke probes returned not_found; no security/tool policy was broadened. The native candidate's59 Python/8 Node mock tests and pending-approval statements were the checkpoint in1e887a5, not current readiness. The exact approval was subsequently supplied and used as recorded above.

After activation, first native GUI job2d17e62a8d234eb49158c70237a3ba7b reached Code but made no edit before300s; failed GUI receipt311.6s. Next job9ce825aa335548e599553e79e80e9f8f changed invoice-final/src/math.py but did not complete the native verifier before300s; GUI correctly failed with partial file evidence305.6s. These projects/results are preserved, not reset/rebroken. Native records also show an alternate shell command denied. Missing verification never counts as success; later reporting retains the worker's deadline reason alongside verification_reason.

Earlier v3 model-route job8cf02fa17c6042a4bbf5b6c7801d7add was stopped from the GUI at582.5s, cancelled/no Code start/no unsettled latch. Alias16K coordinator job0205f11fc92c4a3e96b1135d1d245058 still exhausted its677.6s GUI deadline before Code dispatch. `/local ` then returned JARVIS_LOCAL_ESCAPE_OK in9.4s. These failures motivated bypassing extra manager inference for explicit coding actions; they were not erased by the later passing native run.

## User goal and boundaries

The user wants one input surface: type in OpenJarvis, have OpenClaw coordinate, use OpenCode for coding when needed, and return verified results to the same chat. This supersedes the prior ordering that put reboot acceptance first. It does not authorise spending, cloud fallback, model/package downloads, unrestricted shell/filesystem access, credential exposure or security/pairing resets.

The user separately approved moving the existing Gateway from Windows-reserved port 50368 to available port 18789, updating matching local connections and starting the existing Gateway/Companion. No port exclusions, security settings, tokens or pairing were changed. The native Companion contract problem remains a separate acceptance item; a working coding bridge does not establish full Windows desktop control.

## Current machine layout — recheck before use

- Host checkout/backend: `%USERPROFILE%\OpenJarvis`, existing `.venv\Scripts\python.exe` (3.13). Desktop1.0.5: `%LOCALAPPDATA%\OpenJarvis\openjarvis-desktop.exe`.
- Runtime owner: `%USERPROFILE%\Documents\Codex\jarvis-os-runtime`; existing Python314 and login shortcut JARVIS AI Stack. The earlier project/prompt controller is distinct and its acceptance remains separate.
- Host addon: `jarvis-os-runtime\frontdoor\frontdoor.py`, `backend_bootstrap.py`, adjacent non-secret `frontdoor.json` with the current qualified clawctl path and Shared root.
- Current isolated account: T3-P2, Shared root `C:\Users\T3-P2\Shared\jarvis-frontdoor-20261118`. Verify the account through the qualified installed clawctl status before assuming it still exists.
- Gateway/MSIX2026.11.1/2026.11.100.0; supported qualified alias is under `%LOCALAPPDATA%\Microsoft\WindowsApps\OpenClawFoundation.OpenClawGateway_rfcbke2p71se2\clawctl.exe`.
- OpenCode worker2.2.7: use the **existing configured ACP command** read in memory from the isolated OpenClaw `plugins.entries.acpx.config.agents.opencode.command`. Do not invent a runtime path or download a missing one. Host desktop2.2.6 is a separate existing app/profile.
- Existing Ollama0.40.16 on loopback11434, four original models plus the local context alias. The coordinator uses existing qwen3.8:27b; Code uses the no-download16K local alias described above. The four original models remain intact.

## Flow and permissions

1. The project bootstrap wraps the original OpenJarvis app factory and replaces only its existing `/v1/chat/completions` callable. Existing app middleware, auth and route dependencies remain. No new changes to the preserved source checkout were needed for this bridge.
2. Leading ordinary greetings/questions use the original OpenJarvis route and selected model. `/local ` explicitly chooses it. Explicit coding actions go once through the enabled authenticated native Gateway endpoint without extra manager inference. Other bridge text uses one restricted jarvis-frontdoor coordinator; that model-driven tool route remains slow/unreliable. Requests containing client tools retain their original route. This bounded lexical router is not a general semantic intent planner; original Jarvis knowledge/tool/memory access is not granted to the coordinator.
3. Each request has a unique private job ID. Model-coordinator requests use a fresh unique Gateway session and bounded frontend conversation history; the desktop supplies no stable conversation ID. Thus separate chats never share a hash-derived session accidentally.
4. The coordinator has exactly these effective MCP tools: `openjarvis-readonly__openjarvis_health`, `openjarvis-readonly__openjarvis_models`, `openjarvis-readonly__openjarvis_runtime_status`, `jarvis-code__code_task`. Native shell/files/web/messaging/delegation tools are absent. The retained status server is unchanged.
5. The coding tool requires the active job nonce, an explicit coding request and an unused single coding claim. Its project argument is a validated slug under the owned `projects` directory. It has no arbitrary cwd/command/path/provider arguments.
6. OpenCode runs through its existing ACP executable, with a project-local deny-by-default policy: edits only src/tests/README, no external directory or credential files, and one exact Python verifier command. Acceptance fixtures additionally protect their tests. No global OpenCode permissions or cloud providers were enabled.
7. The verifier checks protected hashes, parses a restricted pure-Python subset before execution, and applies normal-user Windows process/memory/CPU limits plus a parent timeout. This is **not** a general operating-system sandbox. Broader runtime/import/file/network requirements are permission-blocked.
8. Completion uses native persisted OpenCode model/tool records, an exact allowed verifier exit0 and independent tests, not assistant prose. Adapter revision3 runs export/verification in the outer Gateway worker, outside the active ACP callback. It signals Code to stop after native verifier+independent proof, closes its owned ACP process, rechecks final evidence, and stops its own coordinator narration before returning the receipt. This is deliberate verified completion, not a claim of a natural assistant end-turn. Failed turns preserve partial evidence when available; missing evidence is labelled not recorded.
9. Real progress and the receipt stream back to the same OpenJarvis assistant message. No OpenClaw tool calls Jarvis chat again. No second coordinator runs while Code owns that bridge task's inference.
10. GUI Stop/disconnect creates this job's cancel marker. The worker aborts only its own Gateway run, confirms shutdown and checks the owned Code receipt/process. Unknown shutdown creates an unsettled latch; new work is refused. Persistent unfinished job records and a coding OS file lock prevent duplicates across backend recovery. Never delete a latch/claim merely to retry.

Operational jobs include local prompts and are **private**. Never publish job inputs, full active configs, diagnostic ZIPs or private backups. These are operational receipts, not another project tracker. The runtime has no automatic GitHub writer; the operator updates the sole master.

## Changes and backups

The root MASTER_TODO bridge item was marked WORKING and read back at `ed5029832c94d6bc082920e56c3b53426dcffe80` before implementation.

The Gateway originally could not bind: Windows excluded50360–50459, including50368. A supported start reproduced EACCES. Under explicit approval, only `gateway.port` changed to18789 with a byte-verified backup retained privately at `.openclaw\openclaw.before-port-18789-20261118.json`. All other values matched. Companion's saved loopback URL was already18789 and was preserved. Startup native-proof checks/tests now expect18789. A real native ownership/listener proof passed afterward.

The agent/MCP registration used the installed supported config-patch CLI after dry-run validation. The first proposed allow+alsoAllow combination was rejected before write and corrected to a restrictive allowlist. The CLI canonicalised implicit defaults: existing main-agent fields were preserved, its standard existing workspace became explicit, and ownership/system-agent/heartbeat/talk routing fields became explicit. This was recorded rather than falsely claiming byte equality. No existing field was removed. The private pre-agent backup stays inside the isolated profile as `openclaw.before-jarvis-frontdoor.json`.

Coordinator-only model parameters request num_ctx16384 and think=false. The scoped patch passed dry-run/application and verified existing main-agent/global-model data unchanged; private pre-context backup is retained. Do not claim all Ollama requests now use16K: the shared runtime also serves existing configurations, and observed residency can return to65K. Initial real coordinator GUI reply took156.9s; speed is not established by the configuration alone.

The existing source connector-status repair remains preserved. The watchdog's fixed child-only IPv4 Ollama environment remains. Watchdog launch now selects the project bootstrap only when its adjacent manifest exists, and inventory recognises its validated venv serving child. Normal native desktop attach is preserved; no bypass or second backend is introduced.

Host runtime backups are under `jarvis-os-runtime\backups\port-18789-20261118`, `frontdoor-20261118` and dated `frontdoor-refresh-*` directories. Activation pauses only the project watchdog, preserves the desktop, stops only exact validated backend processes, and rolls back if health fails. Do not replay one-time helpers blindly on another computer.

## Execution evidence and limitations

The latest accepted GUI execution is recorded above. Earlier failed attempts remain visible:

- Direct installed OpenCode ACP component: bridge-smoke changed only src/math.py; three independent tests passed; native local Ollama provider, edit and permitted verifier exit0 recorded; protected files retained and owned ACP process exited.
- Initial coordinator probe was slow and cancelled; native session status killed/hasActiveRun=false was subsequently verified.
- Actual OpenJarvis GUI ordinary bridge probe returned JARVIS_FRONTDOOR_OK,156.9s, with no tools.
- First complete GUI invoice-calculator request reached Code and made the edit. Native records subsequently showed permitted verifier exit0 and a denied extra shell command, but ACP narration exceeded300s. The original failure receipt and GUI failure420.1s remain preserved. Revision1 omitted partial evidence and the old displayed none/not-run text was not proof of no changes; later reporting labels missing evidence correctly.
- Revision2's invoice-recovery attempt loaded revision2, edited only src/math.py and reached a permitted verifier exit0, but an export/verification inside the active callback timed out. Its failed receipt with partial file evidence is preserved. Outer-worker execution of the same independent verification subsequently passed3/3 in about3s; revision3 moves those checks outside the active callback rather than increasing or ignoring the deadline.
- Post-boot runtime restoration did not pass the native Companion Node gate after its one launcher-owned retry. Do not call the entire stack/reboot acceptance verified from backend health or this coding task.

## Observation-first continuation and rollback

The bounded four-app front-door acceptance is complete. Next eligible master work remains observation-first actual sign-in/startup acceptance, with native Companion Node still failing; do not repeat the plugin restart approval or silently reset Companion. Read current master first. Then confirm fresh Windows boot time, current processes/listeners, native Gateway proof, Jarvis health/GUI, current watchdog heartbeat and bridge job/latch state. Historical ready snapshots are not a new-boot pass. Do not run installers, reset/re-pair, change security or launch duplicate workers to resume.

When changing addon code, first verify no bridge job is active. Run the existing-environment unit tests, preserve a private runtime backup, deploy the matching files and restart only the authorised owned backend/watchdog. A new unique Gateway session must load the revised MCP server; confirm adapter_revision3/completion_reason in an actual receipt, rather than assuming a copied file refreshed a warm process.

To disable routing, after verified task shutdown and approval for the backend lifecycle change, preserve/rename the addon manifest and relaunch the original venv CLI through the watchdog. Restore the previous watchdog from its verified private backup if required. Keep all addon code, projects, chats and backups. Restore only the newly added agent/MCP entries through a reviewed config patch if requested; do not overwrite the whole active config with an old backup.

Do **not** restore port50368 while Windows still reserves it. A supported port migration must update matching startup/native checks and preserve current credentials/pairings.

Another AI needs authenticated private-repository access and an authorised computer tool to inspect this machine. A GitHub link supplies the handoff, not automatic machine access or permission to repeat lifecycle/config changes.
