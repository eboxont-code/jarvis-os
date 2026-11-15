# PROJECT JARVIS — MASTER PLAN & TODO

**Project:** JARVIS — Ultimate Personal AI Operating System  
**Repository:** eboxont-code/jarvis-os (private)  
**Foundation:** Existing OpenJarvis installation  
**Primary platform:** Windows 11 (Windows 10 where practical)  
**Mobile priority:** Android first; iOS later  
**Budget:** $0 additional expenditure — non-negotiable  
**Master status:** IN PROGRESS  
**Current milestone:** Safely integrate the installed Ollama, OpenJarvis, OpenClaw and OpenCode applications into one tested, local-first workflow.

> This is the single source of truth for project scope, implementation order, status and acceptance evidence. Update this file after every meaningful milestone. A checkbox is completed only after the capability has been executed and verified.

---

## 0. Operating rules — non-negotiable

### Zero-cost constitution
- [ ] No paid AI subscriptions, model APIs, search APIs, research APIs or purchased credits.
- [ ] No paid hosting, databases, storage, monitoring, automation platforms or mandatory cloud services.
- [ ] No paid trials, hidden usage charges or dependencies that become paid for essential use.
- [ ] No purchases of hardware, software licences, developer memberships or additional services.
- [ ] Before adopting any dependency, check licence, pricing, accounts, quotas, long-term availability, hardware requirements and free local alternatives.
- [ ] Prefer open-source software, local execution, self-hosting, existing hardware and legitimate free public resources.
- [ ] Never automatically fall back to a paid provider.
- [ ] If a capability cannot genuinely be delivered for $0, document the limitation and implement the best practical free alternative.

### ABSOLUTE ZERO-COST REQUIREMENT — NON-NEGOTIABLE

The entire JARVIS project must operate without additional financial expenditure. This is a strict requirement, not a preference. It applies to design, development, runtime, research, deployment, integrations, maintenance, agents and future upgrades.

#### 1. Completely prohibited

Never require or purchase:
- Paid AI API access.
- ChatGPT, Claude or Grok subscriptions as project dependencies.
- Paid search API subscriptions.
- Paid research services.
- Paid cloud inference.
- Paid automation platforms.
- Paid MCP servers.
- Paid databases.
- Paid software licences.
- Paid hosting.
- Paid storage.
- Paid monitoring services.
- Paid developer tools.
- Subscription-based integrations.
- Free trials that eventually require payment.
- API credits that require purchasing more credits.
- Any service that unexpectedly incurs charges.

Never enter payment details, start subscriptions, purchase credits or upgrade an account for JARVIS. Never make essential functionality dependent on a personal subscription or a paid account. Do not silently assume a currently accessible consumer account, free quota or promotional entitlement will remain available.

#### 2. Mandatory local-first architecture

Use local software and the computer's existing resources wherever possible.

Preferred technologies include:
- OpenJarvis.
- Ollama.
- llama.cpp.
- OpenCode.
- SearXNG.
- Playwright.
- Git.
- SQLite.
- Open-source MCP servers.
- Python.
- Node.js.
- PowerShell.
- Local image, audio, video and vision models.
- Open-source document and data processing libraries.

All AI inference must run locally by default. Remote inference is not an essential dependency and must never silently replace local inference.

All memory, research databases, project files, task histories and execution logs must be stored locally. Remote repositories or synchronisation may be used as optional mirrors where genuinely free, but a paid cloud service must never be mandatory. Design core workflows to retain useful local operation when a remote service is unavailable.

#### 3. Completely free internet research

Implement research using legitimate free access methods, including:
- Self-hosted SearXNG.
- Public search engines.
- Publicly accessible websites.
- Official documentation.
- Public GitHub repositories.
- Public package registries.
- RSS feeds.
- Public government datasets.
- Public academic resources.
- Free and unauthenticated APIs where available.

Use multiple sources and fallback mechanisms. Respect search-engine rate limits, website terms and access restrictions. Do not treat a temporary free allowance as unlimited access. Do not switch to a paid API automatically when a free provider becomes unavailable. If a source blocks access, use another legitimate free source or report the limitation.

#### 4. Free capability alternatives

Whenever a capability usually requires payment:
1. Investigate an open-source alternative.
2. Check whether it can run locally.
3. Check whether it can operate without registration or payment.
4. Check its licence.
5. Check hardware requirements.
6. Test its actual functionality.
7. Implement the best working zero-cost option.

If no suitable zero-cost implementation exists, document the limitation instead of purchasing a service.

#### 5. No hidden costs — mandatory dependency gate

Before installing any dependency, integration, model, hosted tool or service, verify:
- Licence.
- Pricing model.
- Required accounts.
- API requirements.
- Usage restrictions.
- Data limits.
- Whether payment is eventually required.
- Whether the free option is sufficient for the intended workload.
- Whether a local or self-hosted alternative exists.
- Hardware and storage requirements.

Reject dependencies that introduce mandatory payments or undisclosed/uncertain costs. Open-source software is not automatically a free service: distinguish free software from paid hosted infrastructure. Recheck pricing and licence when versions, providers or deployment models change.

#### 6. Deployment policy

Prefer:
- Local hosting.
- Self-hosting on the existing Windows computer.
- Free open-source deployment tooling.
- Free hosting tiers only as optional, replaceable conveniences.

Never make a paid hosting provider essential. Do not purchase domains, developer memberships or publishing accounts. For Android, prioritise locally generated APK files and direct installation. For iOS, develop and prepare the application without paid services, but clearly identify any Apple signing, hardware or distribution restrictions that prevent a genuinely free release.

#### 7. Hardware efficiency

Optimise local AI workloads for available CPU, GPU, RAM and storage. Select appropriately quantised models. Avoid downloading unnecessarily large models. Use model routing to minimise resource consumption. Prefer reusable downloaded models, local caching and efficient inference. The system must work with the user's actual available hardware rather than assuming access to expensive GPUs or external servers.

#### 8. Mandatory failure behaviour

If a feature requires payment:
- Do not activate it.
- Do not create a paid account.
- Do not purchase credits.
- Do not silently substitute a paid provider.
- Search for a legitimate free alternative.
- Explain any remaining limitation.

#### FINAL RULE

The objective is maximum practical AI capability for $0 in additional software and service expenditure. Never sacrifice the zero-cost requirement without explicit user authorisation. A feature that is unavailable for free must be honestly identified as unavailable, not disguised as completed functionality.

### Preserve the existing installation
- [ ] Preserve the existing OpenJarvis repository, customisations, application and user data.
- [ ] Do not reinstall or replace working components without a demonstrated technical reason.
- [ ] Never run destructive Git cleanup/reset commands against the existing dirty working tree.
- [ ] Never overwrite configuration, databases or user data without a recoverable backup.
- [ ] Prefer custom agents, tools, skills, MCP integrations, adapters and external extensions.
- [ ] Keep JARVIS custom functionality separate from upstream files wherever practical.
- [ ] Establish rollback checkpoints before substantial changes.
- [ ] Verify backup contents and recovery procedures; a copy command completing is not sufficient proof of recoverability.

### Truthfulness and verification
- [ ] Never claim an action was executed when only instructions or code were produced.
- [ ] Never claim a feature works because files exist or a package is installed.
- [ ] Every capability must have a testable acceptance criterion.
- [ ] Record commands, outcomes, test evidence, errors and limitations.
- [ ] Verify the actual resulting state after important actions.
- [ ] Mark work PARTIAL or BLOCKED when evidence is incomplete.
- [ ] Keep assumptions, retrieved facts, saved memory and verified actions distinguishable.
- [ ] Prefer reliability and recovery over uncontrolled autonomy.

### Windows-first
- [ ] Windows is the primary development and runtime platform.
- [ ] No Mac requirement.
- [ ] Use existing Windows hardware and installed tools wherever possible.
- [ ] Build Android capabilities before mobile iOS capabilities.
- [ ] Do not promise native iOS compilation, signing or App Store distribution from Windows under a $0 requirement when the required Apple toolchain or paid program is unavailable.

### Execution discipline
- [ ] Work from this master checklist at the start and end of each work session.
- [ ] Work in dependency order, one meaningful milestone at a time.
- [ ] Batch related operations to reduce repetitive user work.
- [ ] Use scripts with visible progress, bounded scope, hard timeouts, useful logs and clear exit codes.
- [ ] Do not launch unbounded or opaque diagnostic scripts.
- [ ] Prefer a focused functional test over another broad audit.
- [ ] Check whether a dependency already exists before installing it.
- [ ] Do not download large models until storage, RAM, VRAM and runtime compatibility are checked.
- [ ] Update this file after each verified milestone.
- [ ] One master checklist is authoritative; do not create competing status trackers.

---

## 0A. Integrated application architecture and delivery plan — CURRENT STRATEGY

### Naming and scope — important distinction

**JARVIS OS is the name of this project, its private repository and its master plan. It is not an installed application, executable, daemon, service, AI agent or runtime coordinator.** Do not design or describe it as though it already runs.

The actual installed applications being integrated are:
1. **Ollama** — shared local model runtime.
2. **OpenJarvis** — existing desktop AI application and agent/tool environment.
3. **OpenClaw** — target runtime coordinator through its Gateway and agent system, pending successful local setup and verification.
4. **OpenCode** — specialist software-development agent/harness.

The target is to make these four real applications cooperate. JARVIS OS records the architecture, rules, implementation tasks and evidence in this repository.

### Current known starting point

This is the starting information supplied by the user and previous recorded checks. It is not a substitute for a fresh inventory before configuration.

| Component | Known state | Next verification |
|---|---|---|
| Ollama | Installed; version 0.40.15 was last observed in local logs. The T3-P2 runtime reached `127.0.0.1:11434` and listed `qwen3.5:0.8b`, `qwen3.5:2b`, `qwen3.5:4b` and `qwen3.8:27b`. Qwen 27B was observed loaded with context 65,536. An earlier Boxont inventory also listed qwen3.5:9b; reconcile the account/runtime inventory. | Reconfirm the one active Ollama server owner, exact current tags and version; test actual tool calls and clean restart. Do not pull or replace models. |
| OpenJarvis | Installed and previously recovered; the user confirmed its customised desktop and a real chat reply. Last recorded app version: 1.0.2. | Preserve the current installation and data; inspect the installed build's MCP/tool capabilities and verify its actual shared-Ollama endpoint. |
| OpenClaw | Gateway runtime 2026.11.1 is installed as MSIX identity 2026.11.100.0; active Companion is v2026.11.1 stable/unpackaged. Existing diagnostics already show Operator hello-ok, NodeDeviceToken resolution and Node challenge before credential withholding. Latest fresh read-only `clawctl gateway-service status --json` shape check returns `ok=true`, `integration.kind=isolated-session`, version 1, `gateway.state=running`, and all required producer-side fields present: port, ownership object, sandboxId, agentUserSid and one complete listener identity (port/processId/processStartTimeUtc/sequenceNumber). This makes missing producer fields and the known multi-listener selector issue unlikely in this latest snapshot. It does not prove Companion's own Windows listener capture and process-sequence verification succeeds. User's targeted read-only comparison on port 50368 returned package listener PID 16208 and Windows listener PID 16208, `PIDMatch=True`, one Windows listener, and `ProcessVisible=True`. `Get-Process` could not read the process start time (`StartTimeReadable=False`), so no timestamp comparison is available. This is not evidence of a PID mismatch and is consistent with the Companion source comment that the isolated agent's process DACL denies opening its process handle; Companion intentionally uses `WindowsProcessSequenceSnapshot` / `NtQuerySystemInformation(SystemBasicProcessInformation=252)` instead. The user verified the exact Windows process-sequence API used by Companion: `API=OK`, `TableValid=True`, `GatewayPIDPresent=True`, `SequenceNonZero=True` for live listener PID 16208. This rules out an unsupported API or missing Gateway PID in the process table. User's next read-only comparison returned `PIDMatch=True`, `API=OK`, `TableValid=True`, `GatewayPIDPresent=True`, `SequenceNonZero=True`, and `SequenceMatches=True`. This proves the live Gateway PID and its Windows process-sequence value both match the package-attested listener identity. The process identity tuple `(port, PID, sequenceNumber)` is therefore verified for the current single listener. Remaining untested source requirements are loopback address, complete IPv4 and IPv6 IP Helper listener snapshots, and unchanged listener/process sequence across Companion's second snapshot. These are best tested by Companion's own retry, which executes the exact production inspection under the app's process context. Next use the existing Companion Node Retry action once (not a Gateway restart); if the same error remains, investigate only that remaining native inspection path. Keep Gateway and Companion installed as-is; no restart, reinstall, pairing reset, token change, or access-permission change. |
| OpenCode | Version 2.2.7 in T3-P2. Its global `opencode.jsonc` loads local Ollama, selects `ollama/qwen3.8:27b`, uses `ollama/qwen3.5:4b` as the small model and allows only the Ollama provider. Direct CLI and direct ACP tests returned READY. | Keep the local-only provider configuration; complete a real coding task through the OpenClaw ACPX session and verify tests, scope and cancellation. |
| Local models | Current T3-P2 API listing returned qwen3.5:0.8b, qwen3.5:2b, qwen3.5:4b and qwen3.8:27b. A previous Boxont inventory also listed qwen3.5:9b; that difference has not been reconciled. | Refresh tags in the selected shared-server context and test context, tool calling, latency and resource use. Do not pull or replace models. |

**Current integration handoff:** [OpenClaw / OpenCode / Ollama handoff — 12 November 2026](docs/OPENCLAW_OPENCODE_OLLAMA_HANDOFF_2026-11-12.md). This records successful local/browser paths and the separate unresolved native Companion Node failure.

### The architecture I recommend

Use the four applications as one coordinated toolchain, with one clear responsibility for each:

- **Ollama supplies the local models.** It is the shared inference engine used by the other applications.
- **OpenJarvis is the main desktop AI workspace.** Keep it working independently for direct chat and its existing capabilities. Where the installed build supports it, make approved OpenJarvis tools/context available to OpenClaw through MCP.
- **OpenClaw is the runtime coordinator.** It receives the overall task, reads the project instructions, plans the work, calls approved tools and delegates coding to OpenCode. This is the target arrangement; it is not configured or verified yet.
- **OpenCode is the specialist software developer.** It inspects the assigned project, makes scoped changes, runs tests and returns evidence to OpenClaw.
- **JARVIS OS is the project and master plan only.** The repository contains the architecture, rules, memory files, task checklist and evidence. It does not run as another assistant or coordinator.

The applications should work together while remaining independently usable. The purpose is not to replace one with another or to keep four disconnected chat windows open.

### How the applications should work together

1. **You give OpenClaw an overall task.**
2. **OpenClaw reads the JARVIS OS project rules and the relevant project's instructions** from the authoritative repository/workspace.
3. **OpenClaw plans the work and identifies what it needs.** It can use its own local model through Ollama and, where supported and approved, call OpenJarvis tools/context through MCP.
4. **OpenClaw delegates software work to OpenCode through ACP.** The task includes the exact repository, permitted folders, requested outcome, acceptance tests and prohibited actions.
5. **OpenCode investigates, implements and tests** only within the approved workspace, then returns changed files, commands, test outcomes and unresolved problems.
6. **OpenClaw checks the returned evidence.** For important work, use a separate review step rather than trusting the coding agent's claim that it succeeded.
7. **OpenClaw updates the one authoritative project checklist and execution record** after evidence is available. If the runtime cannot safely write to the repository, it prepares the update instead of inventing success.
8. **You receive a normal-English completion report** explaining what was actually added, improved or fixed, what was tested and what remains.

OpenJarvis must remain usable on its own. Do not create circular delegation where OpenClaw calls OpenJarvis and OpenJarvis sends the same task straight back to OpenClaw.

### Permissions and autonomy strategy

Autonomy should be enabled by capability and workspace, not by giving every application unrestricted access.

- Research, read-only inspection, planning and status reporting can become automatic after baseline tests.
- Reversible edits can become automatic only inside explicitly approved project workspaces, with checkpoints and file-scope enforcement.
- OpenCode must have explicit per-tool permissions. Do not rely on its default profile: configure read, edit, shell, external-directory and network permissions intentionally. Start with read-only inspection, then enable controlled edits and tests.
- OpenClaw must have explicit tool allow/deny policies and per-agent workspace boundaries. Its sandbox is off by default in current documentation; explicitly enable and test a suitable sandbox before exposing autonomous shell/file tools. Keep agent sandbox scope isolated and do not enable elevated execution for ordinary work.
- MCP tools exposed from OpenJarvis must be a whitelist. Start read-only; only add write-capable tools after permission, logging and rollback tests pass.
- Installs, administrative changes, destructive deletion, external messages, publishing, purchases and credential use require direct user approval.
- A model response, tool call or process exit is not proof of completion. Re-open/read the result and run the relevant acceptance test.

### Model strategy

Use the five already-recorded models as candidates. These assignments are **provisional roles for testing**, not verified performance rankings or instructions to download anything.

| Existing model tag | Initial task to evaluate | Important checks |
|---|---|---|
| `qwen3.8:27b` | Complex reasoning and demanding coding/review tasks | Tool calling, context support, memory use and latency on the actual PC |
| `qwen3.5:9b` | General assistant and agent tasks | Reliable instruction following, tool calling and useful response speed |
| `qwen3.5:4b` | Lighter general tasks | Tool compatibility and quality on bounded tasks |
| `qwen3.5:2b` | Small, quick operations | Whether it can follow structured requests reliably |
| `qwen3.5:0.8b` | Very lightweight operations | Only use for simple tasks it demonstrably handles correctly |

Do not assume the largest model is automatically best for every job. Compare actual model behaviour, context, latency, CPU/GPU/RAM use and reliability. A model being installed does not prove that it supports the tool-calling behaviour needed by an autonomous agent.

For OpenClaw specifically, current official Ollama setup documentation checks loaded models for tool support and at least 16K context during automatic discovery. Some curated local-model examples use a 64K context, but the usable context depends on the actual model metadata, runtime settings and available memory. Treat 64K as a test target where the model and hardware support it—not a blanket guarantee or an automatic setting. Verify the selected model with a real tool call before making it the default.

**No additional model downloads until the existing five have been inventoried and evaluated. No cloud model or paid fallback.**

### Shared JARVIS project memory

The aim is to stop the applications from holding conflicting versions of project instructions, decisions and task status.

The shared source of truth is the **JARVIS OS project repository and approved local project workspace**, not a new JARVIS OS application or a new runtime database.

| Shared information | Authoritative location / rule |
|---|---|
| Master tasks and status | `MASTER_TODO.md` — the only master checklist |
| Mandatory operating rules | `AGENTS.md` and applicable repository-specific instructions |
| Architecture and integration decisions | This master plan and its documented decision records |
| Project context and technical notes | Files inside the relevant approved project workspace |
| Execution history | Dated, evidence-based entries in the master execution log and relevant local logs |
| Code and deliverables | The real project repository; use Git history/checkpoints to preserve changes |
| Secrets and credentials | Application-managed secure stores only; never copy into shared prompts, Markdown or logs |

Initially share durable context through normal files and scoped task packets so it works even if one application's database format is incompatible with another. OpenJarvis, OpenClaw and OpenCode may keep their own internal session histories, but none may create a competing master plan or overwrite another application's private memory. A shared database or memory service is a later optional enhancement only if a real need is demonstrated and the chosen solution is local, free and recoverable.

### What we still need to establish

- **OpenJarvis:** The last recorded desktop build was version 1.0.2 and its customised desktop/chat had been recovered. We must inspect the actual installed build's model configuration, running backend and MCP server/tool exposure. Current upstream documentation does not prove the installed Windows build has every current MCP feature.
- **OpenClaw:** Installed but not configured, based on the user's report. We need its exact version, Gateway setup, local-only Ollama provider, MCP client and ACP support. Do not connect messaging accounts during the initial local test.
- **OpenCode:** Installed but not configured, based on the user's report. We need its exact version, local Ollama discovery, permission settings and ACP launch compatibility.
- **Ollama:** Installed and previously reported serving five models. We need a fresh model inventory, process owner and endpoint check. Earlier tests found two different Ollama processes, so one stable server owner must be chosen without breaking OpenJarvis.
- **Hardware/model fit:** The recorded PC has an RTX 4070 12 GB and 64 GB RAM, but concurrent workloads and context lengths still need actual measurement.

Do not update, replace or reinstall OpenJarvis, pull new models, or overwrite existing configuration as part of this initial discovery.

### What success will look like

Example request:

> Build a new feature for my website. Inspect the existing project, research the best approach, implement it, test it, fix any failures, update the project documentation and tell me what is finished.

Target sequence:

- OpenClaw receives the request and reads the project's instructions.
- OpenClaw uses its local Ollama model to plan the task.
- OpenJarvis supplies approved tools or relevant project context through MCP, where that connection has been verified.
- OpenClaw delegates the implementation to OpenCode through ACP.
- OpenCode changes only the approved project, runs tests and returns evidence.
- OpenClaw or a separate review pass checks the changes and test results.
- The authoritative master plan and execution record are updated from verified evidence.
- You receive a plain-English report describing what was added or fixed, what tests passed, and what remains.

This is the end goal: one coordinated workflow across four real applications, not four independent assistants and not a fictional fifth application.

### The first practical step

Before changing any configuration, inventory the installed versions and actual state of **all four** applications: Ollama, OpenJarvis, OpenClaw and OpenCode. Identify executable paths, config locations, running processes, local endpoints, existing models and supported MCP/ACP interfaces. Back up relevant configuration without exposing credentials. Then test each application independently against the same existing Ollama service.

Only after that baseline is recorded should we configure OpenCode, configure OpenClaw, connect ACP and MCP, and enable controlled autonomy in stages.

### Target responsibility model

| Application | One clear responsibility | It must not become |
|---|---|---|
| Ollama | The shared local inference service that loads and serves the selected models. | A task manager, memory authority or multi-agent coordinator. |
| OpenClaw Gateway | The runtime coordinator: accepts delegated work, plans bounded tasks, manages agent sessions, routes tool calls and tracks execution. | The JARVIS OS project itself, a replacement for OpenJarvis, or an uncontrolled administrator. |
| OpenJarvis | The existing desktop AI workspace for direct interaction, local inference and its verified built-in tools. It may expose a small, approved set of tools to OpenClaw through MCP if the installed build supports it. | A second competing global scheduler or a second writer of the master task plan. |
| OpenCode | The specialist coding environment. It receives scoped software tasks, inspects repositories, edits approved files, runs tests and reports evidence. | A general-purpose Windows administrator or an independent project-status authority. |
| JARVIS OS repository | The project name, architecture, policies, roadmap and single authoritative master checklist. | Any running runtime component or agent. |

**Coordinator decision:** OpenClaw Gateway is the chosen target coordinator because its documented integration paths include MCP clients and ACP coding-agent sessions. This is a design decision to validate, not a claim that OpenClaw is already configured or running.

### Target connection map

**Ollama — one local endpoint**
- Serves OpenJarvis inference.
- Serves OpenClaw's local model provider.
- Serves OpenCode's local model provider.

**OpenClaw Gateway**
- Coordinates work and owns the agent/task execution flow.
- Launches and supervises OpenCode sessions through ACP.
- Connects to explicitly allow-listed OpenJarvis MCP tools, if the installed OpenJarvis build exposes them successfully.
- Reads the same project rules and task instructions as the other applications.

**OpenJarvis desktop**
- Remains independently usable by the user.
- Uses the same Ollama service where its installed runtime supports attaching to an existing endpoint.
- Exposes only selected, verified capabilities to OpenClaw. Start with read-only tools; add narrowly scoped write tools only after the read-only integration passes.

**OpenCode**
- Is started by OpenClaw for coding work through ACP after standalone Ollama operation is proven.
- Uses the same local Ollama service and only the repository/workspace explicitly assigned to that task.
- Returns changed-file summaries, test results, failures and output locations to OpenClaw.

**Do not create circular delegation.** OpenClaw is the coordinator. OpenCode and OpenJarvis provide specialist work/capabilities. Do not initially configure OpenJarvis to send tasks back to OpenClaw while OpenClaw is calling OpenJarvis; add a reverse connection only if a concrete tested need appears.

### Shared model and process policy

- Use one stable Ollama API endpoint on loopback, expected to be http://127.0.0.1:11434, after live verification.
- Ensure only one process owns the Ollama server lifecycle at a time. The owner may be the existing Ollama desktop/service or an OpenJarvis-managed process, depending on what the installed OpenJarvis build can safely attach to. Decide from process and endpoint tests; do not run competing servers deliberately.
- Configure each application to use the verified endpoint. Do not assume that setting a model name alone proves the application is using that server.
- OpenClaw's Ollama integration should use Ollama's native endpoint, without appending /v1; current OpenClaw documentation warns that using its OpenAI-compatible /v1 endpoint can break tool calling.
- OpenCode should use its documented built-in Ollama provider/discovery for the installed version. Do not blindly copy a custom OpenAI-compatible provider example into a different provider format.
- OpenJarvis should use its supported inference configuration and attach to the verified service where supported. Preserve the existing working config and never trigger an unnecessary model download.
- Use only exact model tags returned by the live Ollama model inventory. No automatic pulls, cloud models, remote inference or paid fallbacks.
- Benchmark local model tool calling and context before assigning it as an autonomous agent default. A model's presence in the Ollama list does not prove that it can reliably use tools.
- Run heavy agent jobs sequentially at first. Increase concurrency only after resource use and failure recovery are measured on the actual computer.

### Shared project context and task hand-off

- MASTER_TODO.md remains the only authoritative project checklist.
- AGENTS.md remains the mandatory repository policy source.
- OpenClaw, OpenJarvis and OpenCode must receive the relevant project instructions before working on a repository.
- Use the actual project repository and an explicitly approved working directory. Do not create shadow copies or competing TODO files.
- Every delegated task must state: task goal, repository/workspace, allowed read/write scope, prohibited actions, dependencies, acceptance tests, required evidence and approval gates.
- The coding agent must report changed files, commands/tests run, actual test results, unresolved errors and next steps.
- Only the coordinator consolidates results into the canonical master plan. One task may have one active writer at a time.
- Keep durable task/project data local. GitHub is the existing private source-control mirror, not a mandatory runtime dependency; local work should remain possible when disconnected.
- Never place API keys, passwords, access tokens or private credentials in prompts, task packets, Git history or execution logs.

### Integration phases and completion gates

#### INTEGRATION PHASE A — Inventory and protect the current installation
**Status: PARTIAL — current Ollama/OpenClaw/OpenCode versions, loopback endpoints, local model configuration and browser ACP path recorded; active Companion install identity, native Node handoff and OpenJarvis runtime/MCP baseline remain.**

- [ ] **PARTIAL** — Record the installed versions, executable paths, installation types and CLI availability for Ollama, OpenJarvis, OpenClaw and OpenCode — done: Ollama 0.40.15 last observed; OpenJarvis 1.0.2 is the last known app version; Gateway 2026.11.1 / MSIX 2026.11.100.0; active Companion process is `OpenClaw.Tray.WinUI.exe` PID 4776 at `C:\Users\Boxont\AppData\Local\OpenClawTray\OpenClaw.Tray.WinUI.exe`, file version 2026.11.1.0, About v2026.11.1 stable/unpackaged; separate Add/Remove Programs entry still lists 2026.9.8-1; OpenCode 2.2.7 in T3-P2; remaining: determine whether the older registration is simply stale and finish OpenJarvis inventory.
- [ ] **PARTIAL** — Identify all running processes, listeners and existing API endpoints without stopping or changing them — done: Gateway Node PID 25904 listened on 127.0.0.1:50368; one listener and ownership evidence reported; current `clawctl status` reports Gateway running on 50368, Node.js 24.22.1, session T3-P2, activation none pending, recovery configured; Companion process PID 4776 and file version 2026.11.1.0/path identified; `openclaw-session-host.exe` PID 2780 had no readable ExecutablePath and caused a null-path error in the broad version query; T3-P2 reached Ollama on 127.0.0.1:11434; remaining: finish OpenJarvis process/endpoint baseline.
- [ ] **PARTIAL** — Record the exact current Ollama model IDs and metadata; do not download models — done: T3-P2 /api/tags listed qwen3.5:0.8b, qwen3.5:2b, qwen3.5:4b and qwen3.8:27b; qwen3.8:27b was observed loaded at context 65,536; remaining: reconcile qwen3.5:9b from the earlier Boxont inventory and benchmark tool use/resource behaviour.
- [ ] **PARTIAL** — Identify OpenJarvis's actual runtime config, model setting, backend lifecycle and MCP support in the installed build — done: earlier master records preserve a working customised desktop and chat; remaining: inspect the currently installed build's MCP/tool support and capture a fresh shared-Ollama baseline.
- [ ] **PARTIAL** — Identify OpenClaw's Gateway/config location and installed MCP/ACP capabilities — done: Gateway 2026.11.1 running on loopback 50368; `clawctl status`, service status, ownership schema and Companion preparation checks pass; ACPX is registered/enabled and the browser path returned READY; remaining: identify the active Companion executable/install identity, resolve native Node ownership/credential handoff, and finish policy/recovery tests.
- [ ] **PARTIAL** — Identify OpenCode's config location, Ollama provider discovery and ACP-compatible launch path — done: T3-P2 OpenCode 2.2.7 loads the local Ollama config, lists four installed models, and direct CLI/ACP prompts returned READY; remaining: complete a delegated disposable coding task through OpenClaw ACPX and verify full permission/return behaviour.
- [ ] **PARTIAL** — Back up the relevant configuration files before changing them — done: OpenCode JSONC backup created before its local-provider configuration; OpenClaw config backup was created before the 65,536 context update; remaining: verify recovery copies and inventory the Companion configuration without exporting secrets.
- [ ] Capture a baseline health test and current OpenJarvis chat/model state.
- [ ] Record a rollback method for each configuration change.

**Acceptance:** A verified inventory exists, all existing data/configuration is preserved, and no installation or runtime has been changed merely to gather information.

#### INTEGRATION PHASE B — Establish one shared Ollama service
**Status: PARTIAL — the T3-P2 runtime reaches the existing local endpoint, lists four Qwen tags and completed a Qwen 27B response at 65,536 context; single-server ownership, OpenJarvis attachment, tool-call benchmarking and controlled restart remain unverified.**

- [ ] Choose one Ollama process/service to own the local endpoint based on the Phase A findings.
- [ ] Confirm the expected loopback endpoint responds to /api/tags and /api/ps.
- [ ] Confirm each recorded model tag is actually present; do not assume the older inventory is current.
- [ ] Run a direct prompt against one existing model and record the exact model, response, duration and resource use.
- [ ] Run a real tool-call/completion compatibility test against candidate models where supported.
- [x] **VERIFIED** — Configure or verify OpenJarvis against this same service without triggering an unrelated first-run model download — evidence: 15 November 2026 active OpenJarvis backend `/health` returned `ok`; its text-only `/v1/chat/completions` request using qwen3.5:4b returned exactly `JARVIS_LOCAL_OK` with no tool calls, and immediate Ollama `/api/ps` showed qwen3.5:4b loaded locally at context 16,384. No configuration, model or installation change was made.
- [ ] **PARTIAL** — Restart OpenJarvis and the chosen Ollama owner separately; prove there is no port conflict or unwanted duplicate server — done: 15 November approved clean recovery released ports 8000/11434/53816, then manual relaunch restored one Ollama server on 11434 and one OpenJarvis backend on 8000 with successful local completion. Closing desktop parents alone left child server/backend processes running, so clean shutdown requires explicit orphan-PID verification; remaining: repeat one-at-a-time restart tests with that documented procedure and confirm no duplicate listener.
- [ ] **PARTIAL** — Document the single owner, endpoint, model defaults and clean shutdown behaviour — done: active owner is Ollama app/server on loopback 127.0.0.1:11434 (v0.40.16); OpenJarvis backend uses loopback 127.0.0.1:8000 and active qwen3.5:4b while saved inference metadata remains qwen3.8:27b; recovery test documents exact orphan-PID cleanup after parent closure. Remaining: repeat one-at-a-time restart tests and decide whether the saved-versus-active model difference is intentional before changing anything.

**Acceptance:** One stable local endpoint serves a real model response, OpenJarvis uses the intended endpoint/model, and restart/close behaviour is predictable. No model pull is required for this acceptance.

#### INTEGRATION PHASE C — Configure OpenCode independently
**Status: PARTIAL — local Ollama response, Build coding task, tests, shell approval, `.env` read approval, `.env` edit denial, external-directory hard-deny and cancellation verified; provider fallback audit remains**

- [x] **VERIFIED** — Configure OpenCode's built-in Ollama provider against the verified local service — evidence: 15 November redacted config audit shows exactly one configured provider, `ollama`, at `http://127.0.0.1:11434/v1`, with primary `ollama/qwen3.8:27b` and small `ollama/qwen3.5:4b`; no configured cloud-provider name or credential assignment was found. The only `openai` string is the `$schema` host `opencode.ai`, not a provider. Current CLI reports v2.2.6; earlier T3-P2 evidence recorded v2.2.7, so the version discrepancy remains documented. Config SHA-256 is unchanged.
- [x] **VERIFIED** — Discover and select only an installed model with verified completion and tool-use support — evidence: `qwen3.8:27b` is present locally; OpenCode session API confirms Build agent, `providerID=ollama` and successful outcome; disposable coding task created three files and passed four tests; approved shell command returned Node.js `v26.12.0`. General tool-use reliability remains a separate ongoing evaluation.
- [ ] **PARTIAL** — Verify OpenCode can complete a normal prompt using the local model with no cloud provider configured or selected — done: OpenCode displayed `Provider: ollama`, `Model: qwen3.8:27b` and returned the requested structure summary; remaining: verify the effective provider configuration and absence of cloud fallback.
- [x] **VERIFIED** — Use a disposable test repository first; inspect files without modification, then complete one small controlled code-change task — evidence: OpenCode Build created `src/math.js`, `test/math.test.js` and `package.json` only in `%TEMP%\OpenCode-Integration-Test-20261109-001524`; the uploaded ZIP contains exactly those three files. The user reports no package installation, internet use or changes outside that workspace.
- [x] **VERIFIED** — Run the relevant tests and capture changed-file and test evidence — evidence: Windows OpenCode transcript reports `npm test`, 4 tests passed, 0 failed; the uploaded source archive was independently inspected and `npm test` was rerun successfully in a clean environment (Node v22.16.0, 4 passed, 0 failed).
- [ ] **PARTIAL** — Configure explicit permissions for reads, edits, shell commands, external network access and destructive operations — done: global OpenCode v2 config has six rules and loads successfully; shell `ask` and `.env` read `ask` were observed; `.env` edit was denied; `external_directory:* deny` blocked a sibling-folder read and write; Esc cancellation was confirmed by the user; remaining: audit effective provider configuration and ensure no cloud fallback.
- [x] **VERIFIED** — Block OpenCode access outside the active project workspace — evidence: after changing global `external_directory:*` to `deny` and opening a fresh Build session, a sibling-folder read and write each returned `permission.rejected: Permission denied: external_directory`; no approval prompt was shown. Config backup: `%USERPROFILE%\.config\opencode\opencode.json.backup-20261109-214753`. The earlier stray file from the failed `ask` test remains untouched.
- [x] **VERIFIED** — Verify OpenCode cancellation — evidence: user completed the disposable generation test and confirmed pressing Esc stopped generation and returned control to the user; no tools, files or project changes were involved.

**Acceptance:** OpenCode completes and verifies a small coding task with Ollama, within a disposable workspace and without paid/cloud inference.

#### INTEGRATION PHASE D — Configure OpenClaw as the runtime coordinator
**Status: PARTIAL — installed versions are confirmed current stable: Gateway MSIX 2026.11.1 / package identity 2026.11.100.0 and Companion v2026.11.1. Release verification found no newer official stable Gateway package containing the observed-port/ownership repair; current packaging main retains the exactly-one-observed-port selector. Companion v2026.11.2-alpha.10 is prerelease and is not a recommended repair. Existing diagnostic bundle already proves Operator hello-ok, NodeDeviceToken resolved and Node challenge before credential withholding. The outstanding distinction is whether a fresh package status response omits a required field or Companion's own Windows listener/process snapshot fails after status parsing. Next is one narrow read-only status-shape comparison; do not repeat diagnostics, restart Gateway, reinstall or reset credentials.**

- [ ] **PARTIAL** — Run the installed OpenClaw version's supported first-run setup and record its version/config paths — done: Gateway runtime 2026.11.1 and MSIX 2026.11.100.0; isolated T3-P2 config and local Gateway status are identified; remaining: record the active Companion executable/install path and reconcile the older installed-apps entry.
- [ ] **PARTIAL** — Configure Ollama as a local-only provider at the verified native endpoint — done: OpenClaw primary model is `ollama/qwen3.8:27b`; T3-P2 reaches `127.0.0.1:11434`; remaining: audit all effective providers and ensure no hosted fallback is available.
- [ ] **PARTIAL** — Set a model only after verifying its context capacity and tool-calling behaviour; do not allow a cloud fallback — done: Qwen 27B has `contextTokens=65536`, `num_ctx=65536`, and `ollama ps` reported context 65536; remaining: benchmark real tool calls under the chosen local model and complete provider fallback audit.
- [ ] **PARTIAL** — Start the Gateway and verify its local Control UI is reachable on loopback only — done: Gateway service/status report running at `127.0.0.1:50368`; browser Control UI authenticated and spawned an ACP session; remaining: fix native Companion Node handoff and separately investigate browser proxy port 50370.
- [ ] Configure the default agent's tool policy, workspace boundaries, timeouts, logging and cancellation.
- [ ] **PARTIAL** — Disable or leave unconfigured external messaging channels until the local workflow is secure and stable — done: current diagnostics reported zero channels; remaining: maintain this state until security review.
- [ ] **PARTIAL** — Verify one real local model response and one harmless tool call — done: browser ACPX delegated a simple prompt and received READY using local Qwen; remaining: test a harmless tool call and an actual bounded coding task.
- [ ] Verify Gateway shutdown and restart without losing its intended config.
- [ ] **BLOCKED** — Verify native Windows Companion Node registration and credential handoff — reason: active Companion is stable/unpackaged v2026.11.1; Gateway MSIX is 2026.11.100.0 / payload 2026.11.1. Diagnostics prove Operator hello-ok and Node challenge, then credentials are withheld at isolated-session ownership preflight. The user-supplied technical-details screenshot confirms approved/effective capabilities and commands are populated, but the error remains generic; permissions are not the next repair target. Upstream issue #1691 documents a current-version multi-listener reproduction: `openclaw browser status --json` creates an auxiliary listener in the Gateway Node process; later `gateway-service status --json` drops `gateway.port` and consequently `gateway.ownership`. Current packaging main line 1095 still uses `ObservedPorts.Count == 1`, even though existing `GatewayAddress.ResolvePort()` safely selects a configured port among observed listeners and preserves ambiguity when no match exists. Exact PC failing listener count has not been captured; latest local status snapshot had one listener and full fields, so this remains a strong upstream defect and plausible PC cause, not a proven live reproduction. Exact one-line patch and test plan saved under `patches/openclaw-windows-packaging/`. Proposed fix posted for maintainer review at https://github.com/openclaw/openclaw-windows-node/issues/1691#issuecomment-6818699921. GitHub account has pull but no push permission to packaging repository; branch creation returned 403, so no upstream code/PR was created. Do NOT run `openclaw browser status --json` as a test, restart to clear listeners, reinstall, reset tokens/pairing, change ACLs or bypass ownership. Keep Node BLOCKED until official stable package includes reviewed fix and Node is 1/1 online with a harmless permitted action.

**Acceptance:** OpenClaw operates as a local-only coordinator, can use its model and permitted tools, and exposes no unintended network or account access. Native Companion Node remains a separate required acceptance item.

#### INTEGRATION PHASE E — Connect OpenClaw to OpenCode through ACP
**Status: PARTIAL — ACPX is registered/enabled, its OpenCode executable and `["acp"]` args are explicitly configured, and a fresh browser Control UI session returned READY from local Qwen. Direct OpenCode CLI and direct ACP model discovery/prompt also passed. A real delegated coding task through the current OpenClaw ACPX binding, ACPX cancellation evidence and the full native desktop Companion path remain incomplete.**

- [x] **VERIFIED** — Verify the installed OpenClaw release supports ACP and the current OpenCode harness — evidence: ACP doctor reported the acpx backend registered and embedded runtime ready; direct OpenCode ACP initialization/session creation succeeded on OpenCode 2.2.7.
- [x] **VERIFIED** — Install/enable the official ACP backend plugin only after its licence, dependencies and zero-cost status are checked — evidence: ACPX plugin installed/enabled; doctor healthy; no paid service or model download used.
- [x] **VERIFIED** — Register OpenCode as an ACP coding harness using the documented launch method for the installed versions — evidence: OpenClaw config points to the OpenCode 2.2.7 executable in the managed T3-P2 Node installation with args `["acp"]`; structured patch dry-run passed and was applied.
- [ ] **PARTIAL** — Verify an OpenClaw task creates an OpenCode session with the correct workspace and scoped permissions — done: fresh browser OpenClaw chat spawned an ACPX OpenCode session and the bound prompt returned READY; remaining: verify a real disposable coding task and explicit workspace/permission boundary.
- [ ] **PARTIAL** — Verify OpenClaw receives the actual session result, changed-file summary, test output and failure state — done: the simple READY result returned through the browser ACPX path; remaining: delegate a bounded coding task and collect its changed-file/test evidence.
- [ ] Verify stop/cancel, timeout and clean session termination through the OpenClaw ACPX path. Direct OpenCode ACP session cancellation was tested separately.
- [ ] Verify no recursive delegation or second competing task manager is created.
- [ ] **BLOCKED** — Verify the same ACP workflow from the native Windows Companion app — reason: Companion's Node connection is offline due to Gateway ownership/credential-handoff error. Browser success does not prove the native desktop Node is working. Next: resolve the native Node handoff before calling the desktop app integration complete.

**Acceptance:** OpenClaw successfully delegates a real disposable coding task to OpenCode through ACP and receives independently checkable evidence. Browser simple-prompt success is only a partial milestone.

#### INTEGRATION PHASE F — Connect OpenJarvis tools to OpenClaw through MCP
**Status: NOT STARTED**

- [x] **VERIFIED** — Inspect the installed OpenJarvis build's actual MCP server command, supported transport, tool registry and permission controls — evidence: 15 November installed-release source inspection confirms client support for stdio and Streamable HTTP with caller-side allowed-tool-name filtering; no standalone MCP-server launch command/transport was found. Internal `MCPServer` auto-discovers calculator/think/file-read/web-search/code-interpreter/REPL/memory/channel/LLM/retrieval tools and applies capability policy, rate limiting and allowed-directory gates, but that default surface is broader than the approved initial read-only scope. Current user config has no MCP section/server declaration. No server was enabled or configured.
- [x] **VERIFIED** — Confirm the MCP server can expose a narrow set of OpenJarvis capabilities without requiring a replacement desktop build or an unsupported upstream-only feature — evidence: `runtime/openjarvis_readonly_mcp_adapter.py` is a separate stdio-only adapter with exactly three no-argument tools: OpenJarvis health, matching model IDs and Ollama runtime status. It has six fixed loopback endpoints, rejects unknown tools/arguments, disables redirects, uses bounded requests and exposes no prompt/file/shell/process/web/memory/channel capability. Five fixture/protocol tests passed; all three tools passed against the live local endpoints; compile passed and protected OpenJarvis/OpenCode/OpenClaw config hashes were unchanged. It is not registered/configured with either application.
- [ ] Prefer local stdio transport where supported by both installed applications; otherwise use authenticated loopback-only transport.
- [ ] **BLOCKED** — Connect OpenClaw as the MCP client to the verified OpenJarvis MCP server — reason: 15 November temporary discovery-only registration of the isolated read-only adapter was rejected before save. OpenClaw 2026.11.1 resolved its active managed config to `C:\Users\T3-P2\.openclaw\openclaw.json` and failed before spawning the Python adapter because its MCP runtime attempted to spawn a missing `C:\Users\T3-P2\AppData\Local\OpenClawGatewayMSIX\agent-node\node-v24.22.1-win-x64\node.exe` (`ENOENT`). Read-only `mcp list` then confirmed no managed server is configured in that active profile; the Boxont config SHA-256 remained unchanged. Do not modify the isolated profile, create missing runtime files, override runtime selection, restart Gateway, or use a workaround. Next: wait for/review an official supported Gateway/MSIX runtime repair, then retry discovery only after verifying the exact active runtime path.
- [ ] Start with a whitelist of read-only tools and verify discovery plus real tool responses.
- [ ] Add narrowly scoped write tools only after their permission checks, audit trail and rollback behaviour are tested.
- [ ] Keep unrestricted shell, arbitrary process execution, credential access and elevated operations out of the initial MCP surface.
- [ ] Verify a failing or stopped MCP server does not break ordinary OpenJarvis chat or OpenClaw's other tools.
- [ ] Confirm there is no circular OpenClaw ↔ OpenJarvis agent delegation.

**Acceptance:** OpenClaw can call specifically approved OpenJarvis tools through MCP; tool availability, permissions, failures and logs are independently verified.

#### INTEGRATION PHASE G — Shared task workflow and controlled autonomy
**Status: NOT STARTED**

- [ ] Define one task hand-off format used by OpenClaw and OpenCode, with OpenJarvis context/tools supplied only when needed.
- [ ] Make OpenClaw the only runtime coordinator for delegated multi-step jobs.
- [ ] Make one agent/task the writer for any given project file at a time; avoid simultaneous edits.
- [ ] Provide the correct AGENTS.md and relevant MASTER_TODO.md context to each coding session.
- [ ] Capture task ID, owner, status, allowed scope, approvals, outputs, tests, evidence and recovery point.
- [ ] Enable autonomous research, read-only inspection and reversible edits only within explicitly approved workspaces.
- [ ] Require user approval for installs, elevated actions, destructive changes, external submissions, publishing, payments and credential use.
- [ ] Add bounded retries, timeouts, cancellation, duplicate-task prevention and checkpoint recovery.
- [ ] Resume a harmless interrupted task after a controlled restart without duplicating completed work.
- [ ] Keep all background tasks visible in OpenClaw's task/session status and report completion in plain English.

**Acceptance:** A multi-step task is delegated across the applications, completed within approved boundaries, verified, recorded once in the authoritative project plan and recoverable after interruption.

#### INTEGRATION PHASE H — End-to-end integrated acceptance
**Status: NOT STARTED**

- [ ] Run the complete integration test on a disposable local project.
- [ ] Ask OpenClaw to inspect and plan the task.
- [ ] Confirm OpenClaw uses the local Ollama endpoint.
- [ ] Confirm OpenClaw invokes the approved OpenJarvis MCP tool(s).
- [ ] Confirm OpenClaw starts OpenCode through ACP.
- [ ] Confirm OpenCode changes only the disposable project and runs its tests.
- [ ] Confirm OpenClaw verifies the output and records the result.
- [ ] Confirm OpenJarvis remains usable independently.
- [ ] Restart the applications and prove the connection settings and task history recover.
- [ ] Audit all network traffic/configuration paths for local-only inference and absence of paid providers.
- [ ] Record performance, limitations, failure recovery and final evidence.

**Acceptance:** One complete, real task passes from coordinator to local model, approved OpenJarvis tools and OpenCode coding session, then returns with verified evidence. Each application remains independently usable. No paid service is required.

### Required integration tests

| ID | Acceptance test | Required evidence |
|---|---|---|
| T22 | One shared Ollama runtime | Process/port ownership, /api/tags, real response and clean restart; no competing listener |
| T23 | OpenJarvis uses shared Ollama | Actual OpenJarvis chat response, exact model/endpoint and no unnecessary model download |
| T24 | OpenClaw uses local Ollama | Local-only provider, real response and a verified harmless tool call |
| T25 | OpenCode uses local Ollama | Model discovery, real coding task and local test evidence |
| T26 | OpenClaw → OpenCode ACP | Session creation, scoped workspace, result, cancellation and test output |
| T27 | OpenClaw → OpenJarvis MCP | Whitelisted tool discovery/call, permission enforcement and failure handling |
| T28 | Shared task context | Correct instructions and task scope reach each participating application |
| T29 | Integrated end-to-end task | OpenClaw coordinates OpenJarvis tool use and OpenCode work; output independently verified |
| T30 | Autonomy and safety | Allowed tasks proceed; forbidden/approval-gated tasks stop; audit records are produced |
| T31 | Restart and recovery | Gateway, desktop, Ollama owner and ACP sessions recover without duplicate execution or port conflicts |

### Official integration references checked

Use current official documentation as implementation guidance, but always validate the installed versions before copying commands or configuration:

- OpenClaw + Ollama: https://docs.openclaw.ai/providers/ollama/setup
- OpenClaw Ollama configuration and native endpoint notes: https://docs.openclaw.ai/providers/ollama/configuration
- OpenClaw MCP client: https://docs.openclaw.ai/tools/mcp
- OpenClaw ACP agents: https://docs.openclaw.ai/tools/acp-agents
- OpenClaw ACP setup: https://docs.openclaw.ai/tools/acp-agents-setup
- OpenClaw permissions: https://docs.openclaw.ai/gateway/security/tool-permissions
- OpenClaw sandboxing: https://docs.openclaw.ai/sandboxing
- OpenCode models and local Ollama provider: https://opencode.ai/docs/models/
- OpenCode permissions: https://opencode.ai/docs/permissions/
- OpenJarvis external MCP servers: https://open-jarvis.github.io/OpenJarvis/user-guide/mcp-external-servers/
- OpenJarvis MCP server API: https://open-jarvis.github.io/OpenJarvis/api-reference/openjarvis/mcp/server/



---

## 1. Vision and operating cycle

The JARVIS OS project aims to deliver a universal personal AI operating environment by integrating and extending the actual installed applications—Ollama, OpenJarvis, OpenClaw and OpenCode. JARVIS OS itself is the project name and master plan, not a running application. The integrated applications should provide conversational AI, complex reasoning, live research, specialist agents, software engineering, browser and Windows computer use, system administration, persistent memory, productivity, data analysis, creative work, integrations, automation and measured self-improvement.

These are capability goals, not a requirement to reproduce proprietary models or paid services.

**Permanent operating cycle:**

UNDERSTAND → INVESTIGATE → RESEARCH → THINK → PLAN → DECOMPOSE → EXECUTE → VERIFY → CORRECT → DELIVER → MONITOR → LEARN → IMPROVE

JARVIS must distinguish:
1. Existing model knowledge.
2. Current information retrieved from external sources.
3. Information saved in persistent memory.
4. Inferences and assumptions.
5. Actions actually executed.
6. Outcomes independently verified.
7. Work that remains incomplete or uncertain.

---

## 2. Current system baseline

This section records evidence from the supplied Windows audit and backup logs. Inventory evidence is not a functional capability test.

### Computer and runtime baseline
| Component | Recorded value |
|---|---|
| Computer | Alienware Aurora R16 (PREDATOR) |
| Operating system | Windows 11 Pro, build 26300, 64-bit |
| CPU | Intel Core i9-14900F |
| CPU topology | 24 cores / 32 logical processors |
| RAM | 63.7 GB |
| GPU | NVIDIA GeForce RTX 4070 |
| GPU memory | Approximately 12 GB from NVIDIA tooling |
| Ollama | 0.40.14 installed; process observed running |
| Node.js | 26.12.0 |
| npm | 11.20.0 |
| Git | 2.56.0.windows.4 |
| Rust/Cargo | Installed |
| Docker Desktop | Installed |
| WSL2 | Installed |
| OpenJarvis | Version 1.0.2 appears in installed-app inventory |

### Installed Ollama models recorded by audit
| Model | Disk size | Initial intended role |
|---|---:|---|
| qwen3.5:0.8b | 1.3 GB | Lightweight operations |
| qwen3.5:2b | 2.7 GB | First inference smoke test |
| qwen3.5:4b | 3.3 GB | General local tasks |
| qwen3.5:9b | 6.6 GB | Stronger reasoning tests |

Model disk size is not runtime VRAM usage. Benchmark actual performance, memory usage and latency before choosing defaults.

### Existing repository
- [x] Repository located at C:/Users/Boxont/OpenJarvis.
- [x] Git repository and main branch identified.
- [x] Existing upstream remote name identified.
- [x] Existing working-tree changes detected.
- [x] Audit recorded 35 modified/other files and 3,591 untracked files.
- [ ] Classify existing custom changes before modifying source.
- [ ] Identify exact installed desktop executable and backend runtime.
- [ ] Map installed app to source checkout and build artefacts.
- [ ] Establish isolated JARVIS extension workspace.

**Protection warning:** The existing untracked files are not disposable. Do not clean, reset or overwrite them.

### Backup status (4 November 2026)
- [x] Initial copy-only backup package executed.
- [x] .openjarvis data copy completed according to the report; Robocopy exit code 1.
- [x] Main repository copy transferred 71,189 files, approximately 9.545 GB.
- [x] Main repository log reports zero failed files.
- [!] Main repository copy reported three failed directory entries associated with access denied on .pytest_cache; Robocopy exit code 9.
- [ ] Verify backup contents, representative file hashes and important custom build assets.
- [ ] Verify user-data backup contents.
- [ ] Document and test restoration procedure.
- [ ] Establish recurring checkpoints.

Backup destination recorded:  
D:/JARVIS_Safety_Backups/JARVIS_Backup_20261104_212949

Do not delete or modify the original installation as part of backup verification.

---

## 3. Phase roadmap

## PHASE 0 — Complete system audit and architecture
**Status: PARTIALLY COMPLETE**

### Inventory
- [x] Identify Windows version and machine.
- [x] Identify CPU, RAM, GPU and storage.
- [x] Inventory major developer tools.
- [x] Identify Ollama and installed model names.
- [x] Identify installed OpenJarvis application.
- [x] Identify Docker and WSL availability.
- [ ] Verify the exact active OpenJarvis desktop runtime.
- [ ] Verify the backend process and communication path.
- [ ] Inspect existing custom source modifications.
- [ ] Map existing agents, tools, engines, memory and learning facilities.
- [ ] Map integrations, scheduler, permissions and logs.
- [ ] Record existing faults and known limitations.

### Architecture deliverables
- [ ] Create CURRENT_SYSTEM_AUDIT.md.
- [ ] Create an architecture diagram of the actual installation.
- [ ] Separate existing-and-working capabilities from merely-installed components.
- [ ] Identify missing capabilities and duplication.
- [ ] Create a risk register.
- [ ] Document hardware/model limits.
- [ ] Create dependency and integration maps.
- [ ] Finalise implementation sequencing.

**Acceptance:** The existing installation and customisations are understood sufficiently to extend without damaging working functionality.

## PHASE 1 — Safe foundation
**Status: IN PROGRESS**

### Backup and recovery
- [x] Create and run initial copy-only backup.
- [x] Copy .openjarvis user data without reported fatal Robocopy errors.
- [x] Transfer the repository's file set; zero failed files reported in the Robocopy summary.
- [ ] Review .pytest_cache access-denied directory errors.
- [ ] Verify important files and representative hashes in the backup.
- [ ] Verify custom Windows/Tauri build assets and release payloads.
- [ ] Verify user-data copy.
- [ ] Test restoration into a separate temporary location.
- [ ] Document recovery steps and backup limitations.

### Safe development workflow
- [ ] Establish a Git checkpoint strategy that preserves the dirty working tree.
- [ ] Preserve all tracked modifications and untracked files.
- [ ] Establish an isolated working copy or extension workspace.
- [ ] Document clean separation between upstream code and JARVIS extensions.
- [ ] Establish rollback procedure.
- [ ] Establish structured logs and execution records.
- [ ] Ensure local development services bind to localhost by default.

### Local inference — first functional milestone
- [x] Identify existing Ollama installation.
- [x] Identify four installed Qwen 3.5 models.
- [x] Prepare bounded local-inference test package.
- [ ] Run direct Ollama inference test.
- [ ] Verify a real model response.
- [ ] Run OpenJarvis inference through its actual installed runtime/CLI.
- [ ] Verify OpenJarvis receives a real response from the local model.
- [ ] Record exact model identifier, latency, errors and resource use.
- [ ] Select first known-good local inference configuration.

**Acceptance:** Existing OpenJarvis remains recoverable and a real local model response is demonstrated through the actual OpenJarvis runtime. A direct Ollama response alone does not satisfy the integration test.

## PHASE 2 — Local intelligence engine
**Status: NOT STARTED**

### Model registry
- [ ] Automatically discover installed Ollama models.
- [ ] Record model identifiers, versions and quantisation where available.
- [ ] Record context limits and capabilities.
- [ ] Record vision, audio and tool-calling support where applicable.
- [ ] Record hardware requirements and measured resource use.
- [ ] Record latency and known limitations.
- [ ] Detect unavailable or removed models.

### Model routing
- [ ] Build central model-selection/router service.
- [ ] Route lightweight tasks to small models.
- [ ] Route complex reasoning to the strongest suitable local model.
- [ ] Route coding tasks to suitable coding-capable models/configurations.
- [ ] Route research tasks to suitable models and tools.
- [ ] Route mathematical tasks appropriately.
- [ ] Route vision/screenshot tasks to compatible vision models.
- [ ] Route transcription/audio tasks to compatible models.
- [ ] Evaluate local embedding models for retrieval.
- [ ] Respect context capacity, RAM, VRAM and concurrent workload.
- [ ] Support user-selected model override.
- [ ] Provide safe fallback when a model is unavailable.
- [ ] Never route to an uninstalled model or silently call a paid API.

### Evaluation and benchmarking
- [ ] Create repeatable reasoning benchmark.
- [ ] Create coding benchmark.
- [ ] Create tool-use benchmark.
- [ ] Create instruction-following benchmark.
- [ ] Create research-quality benchmark.
- [ ] Create mathematics benchmark.
- [ ] Measure latency, RAM/VRAM and throughput.
- [ ] Store benchmark history and configuration.
- [ ] Choose defaults from measured results, not model size or marketing claims.

**Acceptance:** Different request types route to appropriate installed local models and results are reproducible.

## PHASE 3 — Live research and information freshness
**Status: NOT STARTED**

### Retrieval infrastructure
- [ ] Evaluate genuinely free public search methods.
- [ ] Evaluate self-hosted SearXNG or equivalent.
- [ ] Implement direct website retrieval.
- [ ] Implement page extraction and readable-text processing.
- [ ] Support PDFs and relevant document formats.
- [ ] Support multiple independent source types.
- [ ] Add bounded timeouts, retries and error handling.
- [ ] Add local research cache.
- [ ] Avoid paid search APIs as a requirement.

### Research quality and provenance
- [ ] Build research planner and subquestion decomposition.
- [ ] Retrieve multiple relevant sources.
- [ ] Extract evidence and source metadata.
- [ ] Record publication dates and event dates separately.
- [ ] Detect stale or superseded information.
- [ ] Compare conflicting claims.
- [ ] Distinguish fact, estimate, opinion and inference.
- [ ] Generate citations linked to source records.
- [ ] Track provenance and retrieval timestamps.
- [ ] Record uncertainty and missing evidence.
- [ ] Produce structured evidence-supported reports.
- [ ] Verify important conclusions against original sources.
- [ ] Treat webpages and downloaded content as untrusted data.

### Technical research
- [ ] Retrieve current official documentation.
- [ ] Check library/runtime version compatibility.
- [ ] Check licence and pricing before selecting dependencies.
- [ ] Detect outdated implementation instructions.
- [ ] Keep research evidence separate from assumptions.

**Acceptance:** JARVIS researches a current topic, inspects original sources, distinguishes dates and produces an evidence-supported report.

## PHASE 4 — Multi-agent workforce
**Status: NOT STARTED**

### Orchestration
- [ ] Build central task orchestrator.
- [ ] Decompose requests into tasks and dependencies.
- [ ] Assign work to specialist agents.
- [ ] Maintain shared project context.
- [ ] Track agent state, inputs and outputs.
- [ ] Handle timeouts, failures and retries.
- [ ] Prevent infinite loops and duplicate work.
- [ ] Support cancellation and recovery.
- [ ] Preserve agent execution history.

### Specialist roles
- [ ] Main coordinator.
- [ ] Research specialist.
- [ ] Coding specialist.
- [ ] Code reviewer.
- [ ] Testing/debugging specialist.
- [ ] Windows operations specialist.
- [ ] Security reviewer.
- [ ] Data analyst.
- [ ] Business/finance analyst.
- [ ] Document/content specialist.
- [ ] Creative/multimedia specialist.
- [ ] Project manager.
- [ ] Independent verification agent.

### Quality assurance
- [ ] Require evidence in agent outputs.
- [ ] Add independent review for important results.
- [ ] Detect unsupported claims.
- [ ] Detect conflicting outputs.
- [ ] Escalate unresolved disagreements.
- [ ] Preserve an audit trail of delegation and decisions.

**Acceptance:** A complex task is coordinated across multiple agents and delivered with verified results.

## PHASE 5 — Persistent memory and knowledge
**Status: NOT STARTED**

### Memory domains
- [ ] User preferences and operating rules.
- [ ] Project context and project decisions.
- [ ] Tasks, status and dependencies.
- [ ] Technical knowledge.
- [ ] Research findings and source references.
- [ ] Evidence and execution history.
- [ ] Configuration and change history.
- [ ] Agent traces, failures and lessons learned.

### Memory infrastructure
- [ ] Establish local persistent storage.
- [ ] Define versioned memory schemas.
- [ ] Implement full-text search.
- [ ] Evaluate local semantic retrieval.
- [ ] Add embeddings only where beneficial.
- [ ] Record provenance and timestamps.
- [ ] Add project-specific memory spaces.
- [ ] Prevent duplicate and contradictory records.
- [ ] Add retention, correction and deletion controls.
- [ ] Protect sensitive information.
- [ ] Back up and restore memory.

### Continuity
- [ ] Resume interrupted tasks.
- [ ] Restore project state after restart.
- [ ] **PARTIAL** — Implement an OpenJarvis session bootstrap that loads the complete authoritative project instructions and latest MASTER_TODO.md at every project session start — done: Windows launcher, installer and generated system-prompt integration committed; remaining: install on the PC and verify the installed desktop runtime actually loads it.
- [ ] **PARTIAL** — Implement task-status updates in the canonical master file (WORKING / PARTIAL / BLOCKED / VERIFIED) with safe local/remote synchronisation and read-back verification — done: status helper commits only MASTER_TODO.md and verifies remote read-back; remaining: exercise it from an actual OpenJarvis agent session.
- [ ] Provide a fallback bootstrap for AI tools that do not automatically discover AGENTS.md, CLAUDE.md, GEMINI.md or Copilot instructions.
- [ ] Track decisions and reasons.
- [ ] Link tasks to code changes and test evidence.
- [ ] Preserve one authoritative project state.
- [ ] Avoid inventing missing history.

**Acceptance:** JARVIS restarts, automatically loads the latest master plan, resumes the correct task and updates its status in the private repository with read-back verification.

## PHASE 6 — Full Windows computer control
**Status: NOT STARTED — CORE, MANDATORY REQUIREMENT**

This phase is not optional. Filesystem access, PowerShell/CMD execution and browser automation do **not** constitute full Windows desktop control. JARVIS must inspect the actual visible desktop, identify real controls, operate real applications through supported Windows interfaces, and independently verify the resulting state. Simulated actions, mock screenshots and shell-only substitutes do not pass acceptance.

The technical design and implementation/test contract are maintained in [WINDOWS_COMPUTER_CONTROL.md](docs/WINDOWS_COMPUTER_CONTROL.md). This file remains the authoritative task/status checklist.

### 6.1 Inspect and select the Windows automation foundation
- [ ] Inspect the exact installed OpenJarvis version, tool registry, permission model, MCP/native-tool support and current system-access implementation before changing code.
- [ ] Map the desktop bridge to the actual Windows session, user identity, process integrity level, display topology, DPI/scaling and active session.
- [ ] Evaluate native Microsoft Windows UI Automation (UIA) control patterns, properties, events, element trees and accessibility identifiers.
- [ ] Evaluate pywinauto with its UIA and Win32 backends against the actual target applications.
- [ ] Evaluate FlaUI and its supported UIA automation modes against the same application/test matrix.
- [ ] Record compatibility, reliability, element coverage, latency, process-boundary behaviour, maintenance state and full transitive dependency licences for each candidate.
- [ ] Select a primary adapter and only the necessary fallback adapters from measured evidence; do not ship duplicate frameworks without demonstrated benefit.
- [ ] Keep the adapter interface replaceable so a later Windows or OpenJarvis update does not require rewriting the orchestration layer.
- [ ] Confirm the chosen components, exact versions, licence terms and installation source satisfy the absolute $0 constitution before installation.

### 6.2 Window, process and application management
- [ ] Enumerate top-level windows and relevant child windows.
- [ ] Identify the active window, foreground application, process ID, executable path and window title.
- [ ] Detect window bounds, display, DPI scaling, visibility, enabled state and modal relationships where available.
- [ ] Launch applications through their registered app identity, Start-menu shortcut or verified executable path.
- [ ] Focus, activate, minimise, maximise, restore, resize and switch windows safely.
- [ ] Detect application launch, exit, hang, crash, modal dialog and unexpected child-window changes.
- [ ] Use bounded waits and cancellation; never wait indefinitely for an application or control.
- [ ] Restrict process termination to explicitly permitted targets; never kill arbitrary processes to recover automation.

### 6.3 Semantic Windows UI Automation
- [ ] Enumerate the UI Automation element tree for a selected window or desktop scope.
- [ ] Return useful control metadata: name, automation ID, control type, class, enabled/focused/off-screen state, bounding rectangle and supported control patterns.
- [ ] Support semantic invocation of appropriate patterns such as Invoke, Value, Toggle, Selection, ExpandCollapse, RangeValue, Scroll and Text where exposed by the application.
- [ ] Prefer stable automation IDs and semantic control patterns over screen coordinates.
- [ ] Reacquire elements after navigation, window changes, dialog creation or stale-element errors; never blindly reuse stale element handles.
- [ ] Handle applications with incomplete accessibility trees through documented fallbacks, not guessed selectors.
- [ ] Provide separate UIA and Win32 compatibility paths only where the application test matrix proves they are needed.
- [ ] Record the adapter and control pattern used for each important operation.

### 6.4 Mouse, keyboard and clipboard
- [ ] Implement real mouse movement, click, double-click, right-click, drag and scroll.
- [ ] Implement real keyboard text entry, key presses, hotkeys and modifier handling.
- [ ] Validate coordinate targets against a recent screenshot, display bounds, DPI and current window state before coordinate-based input.
- [ ] Prefer semantic UIA actions; use coordinate input only when semantic controls are unavailable or inadequate.
- [ ] Detect focus loss, wrong-target input, unexpected dialogs and keyboard-layout issues before retrying.
- [ ] Implement clipboard read/write with explicit scope, size limits and secret-redaction safeguards.
- [ ] Verify text entry and clipboard operations by reading back the target control or resulting content where possible.
- [ ] Never silently paste credentials, tokens or sensitive personal data into an unverified control.

### 6.5 Screenshots, OCR and local visual understanding
- [ ] Capture the full desktop, a selected display, a selected window and a bounded screen region.
- [ ] Evaluate Windows Graphics Capture and other supported local capture paths; handle consent, capture indicators, display changes and unavailable capture surfaces correctly.
- [ ] Store screenshots locally and attach timestamps, display/window identity and dimensions to evidence.
- [ ] Implement local OCR with word/line geometry and confidence where supported.
- [ ] Evaluate built-in Windows OCR and a free local engine such as Tesseract; verify installation, language data, licensing and actual accuracy before selection.
- [ ] Integrate an already-installed or separately verified zero-cost local vision model for visual context, ambiguous layouts and controls that expose poor accessibility metadata.
- [ ] Route visual tasks only to models that are actually installed and tested; no cloud vision fallback.
- [ ] Combine screenshot, UIA tree and OCR evidence; preserve disagreement and confidence rather than inventing a control target.
- [ ] Mask or exclude passwords, authentication codes, financial details and other secrets from screenshots, OCR output, prompts and logs by default.
- [ ] Handle protected/secure desktop surfaces and inaccessible windows as explicit limitations requiring user action, not as a reason to bypass Windows security.

### 6.6 Action planner and verified interaction loop
- [ ] Implement the loop: inspect current state → identify target → plan one bounded action → check permissions → execute → wait for a bounded interval → reacquire state → verify outcome.
- [ ] Use unique target resolution; stop when more than one plausible control matches.
- [ ] Validate that the target still belongs to the intended application/window immediately before acting.
- [ ] Verify the resulting state using UIA properties/control patterns and, where useful, a fresh screenshot/OCR result.
- [ ] Support explicit preconditions, expected postconditions, action IDs, timeouts, cancellation and a bounded retry budget.
- [ ] On unexpected states, stop input, capture diagnostic evidence, re-inspect the desktop and re-plan; never blindly replay a sequence.
- [ ] Detect partial completion and report it distinctly from success.
- [ ] Maintain a local audit record of intent, target, permission decision, tool/adapter, action, result, verification and error.
- [ ] Provide a safe stop/cancel command that prevents further input immediately.

### 6.7 OpenJarvis integration and tool interface
- [ ] Inspect the installed OpenJarvis version's documented native-tool and MCP integration points; do not assume upstream support is present in the user's installed build.
- [ ] Expose desktop capabilities through an authenticated local MCP server or an equivalent native OpenJarvis tool adapter.
- [ ] Prefer MCP stdio transport when supported by the actual OpenJarvis tool configuration; it avoids opening a local network listener.
- [ ] If a local HTTP transport is required, bind only to 127.0.0.1, require authentication, validate Origin, defend against DNS-rebinding access and reject remote-interface binding.
- [ ] Authenticate the calling process/client and apply per-tool and per-operation permissions; do not treat loopback access alone as authentication.
- [ ] Keep the tool service and ordinary OpenJarvis inference process at normal-user privilege.
- [ ] Provide narrow tools for desktop state, window listing/inspection, screenshots, accessibility-tree inspection, semantic control invocation, mouse/keyboard input, clipboard, application launch, waits, cancellation and verification.
- [ ] Do not expose unrestricted PowerShell, arbitrary process execution or a general-purpose elevated shell through the desktop-control interface.
- [ ] Integrate tool results into OpenJarvis's agent loop with structured state, clear failures and evidence attachments.
- [ ] Test the complete path from an OpenJarvis agent request through the local bridge to a real desktop action and verified result.

### 6.8 Browser and application interaction
- [ ] Keep Playwright for browser DOM/navigation workflows and test it as a separate tool surface.
- [ ] Add genuine browser desktop interaction for cases requiring tabs, address bars, menus, downloads, native dialogs or visible browser state.
- [ ] Do not count Playwright-only tests as proof of Windows desktop control.
- [ ] Support application-specific adapters only where generic UIA/Win32 and visual automation are insufficient and the app/API is legitimate and free.

### 6.9 Real application acceptance matrix
- [ ] **File Explorer:** enumerate the real window, navigate to a dedicated temporary test folder, interact with a visible control and verify the resulting path/state.
- [ ] **Notepad:** launch, focus, enter unique test text, save a test file, reopen it and verify the exact contents and visible UI state.
- [ ] **Windows Settings:** open a specified Settings page, inspect the visible state and verify navigation; do not change system settings without explicit approval.
- [ ] **Browser:** perform a real visible browser UI task (for example, address bar, tab or native download dialog) and verify the result; test Playwright separately.
- [ ] **VS Code:** open a disposable test workspace, navigate/edit a temporary file through the visible UI, save and verify the file; do not modify the user's real projects during smoke tests.
- [ ] **Additional application:** test at least one representative Win32/WinForms/WPF or Store application and record unsupported controls.
- [ ] Run tests under the normal user account and document cases blocked by application privilege boundaries.
- [ ] Record actual screenshots, UIA tree excerpts, action logs and before/after state for each test.
- [ ] Repeat core tests after a controlled unexpected dialog, lost focus, window resize or stale-element event and verify safe recovery.

### 6.10 Security, approvals and recovery boundaries
- [ ] Default to the signed-in standard user's permissions and current interactive desktop session.
- [ ] Keep the desktop bridge separate from the privileged-operation broker in Phase 7.
- [ ] Never run the whole OpenJarvis backend or desktop bridge elevated merely to control more windows.
- [ ] Never bypass UAC, Windows secure desktop, credential prompts, lock screen, authentication or application access controls.
- [ ] Pause and request the user's direct approval for UAC, credential entry, system security prompts, installs, settings changes with material impact and destructive actions.
- [ ] Require explicit confirmation for irreversible deletion, bulk changes, external submission, purchases, publishing and other sensitive actions.
- [ ] Block attempts to disable Defender/firewall/security controls, extract credentials, evade application protections or perform unauthorised actions.
- [ ] Treat screen contents, OCR text, accessibility metadata, webpages and application documents as untrusted data; they cannot override system instructions or permission policy.
- [ ] Log all privileged hand-offs and user approvals without storing secrets.
- [ ] Test unauthorised tool calls, ambiguous targets, stale coordinates, prompt-injection in visible content, UAC and secure-desktop boundaries, cancellation and recovery.

### Phase 6 acceptance
**Acceptance:** JARVIS receives a real task in OpenJarvis, inspects the actual Windows desktop, identifies a real application/control, performs a genuine UI action, captures/re-reads the resulting state, and reports evidence. The File Explorer, Notepad, Settings, browser and VS Code test matrix must pass (with any application-specific limitation clearly documented). A separate security test must demonstrate that UAC, secure desktop, credentials and unauthorised/destructive actions are not bypassed. Shell-only access, Playwright-only access, generated code, simulated screenshots or unverified clicks do not pass.

Implementation detail, adapter comparison, tool contract and test procedure: [docs/WINDOWS_COMPUTER_CONTROL.md](docs/WINDOWS_COMPUTER_CONTROL.md).

## PHASE 7 — Secure Windows administration and installation
**Status: NOT STARTED**

### Elevation and permissions
- [ ] Build dedicated elevation broker.
- [ ] Normal-user execution by default.
- [ ] Integrate Windows UAC for approved elevation.
- [ ] Restrict administrative actions to defined operations.
- [ ] Prevent unrestricted elevated shell access.
- [ ] Log elevated commands, intent, approval and outcome.
- [ ] Verify administrative actions.

### Software installation
- [ ] Integrate appropriate free package managers.
- [ ] Validate download sources and installers.
- [ ] Check licence and cost.
- [ ] Verify checksums/signatures when available.
- [ ] Record installation logs.
- [ ] Verify installed versions and actual operation.
- [ ] Implement rollback where practical.
- [ ] Avoid unnecessary upgrades and removals.

**Acceptance:** An approved development dependency is installed through authorised elevation and independently verified.

## PHASE 8 — Autonomous software development workforce
**Status: NOT STARTED**

### Coding workflow
- [ ] Evaluate OpenCode compatibility with the installed foundation and local inference.
- [ ] Integrate a $0 local coding workflow where compatible.
- [ ] Inspect unfamiliar repositories and architecture.
- [ ] Review official documentation and dependencies.
- [ ] Create implementation plans and acceptance criteria.
- [ ] Establish checkpoints before modifications.
- [ ] Implement controlled multi-file changes.
- [ ] Generate and run tests.
- [ ] Debug and fix failures.
- [ ] Perform independent code review.
- [ ] Generate/update documentation.
- [ ] Prepare releases and rollback plans.
- [ ] Verify generated artefacts and actual application behaviour.

### Supported development targets
- [ ] Websites and web applications.
- [ ] APIs, backends and databases.
- [ ] Admin dashboards and portals.
- [ ] Windows desktop software.
- [ ] CLI tools and developer utilities.
- [ ] Android applications and local APK builds.
- [ ] Cross-platform applications.
- [ ] Local infrastructure and automation.
- [ ] Data science and machine-learning applications.
- [ ] IoT/robotics integrations only where available hardware supports them.

**Acceptance:** Complete an unfamiliar multi-file software task with real tests and a verified deliverable.

## PHASE 9 — Universal productivity, business and integrations
**Status: NOT STARTED**

### Documents and knowledge work
- [ ] Read/create/edit documents.
- [ ] Process PDFs.
- [ ] Create and analyse spreadsheets.
- [ ] Create presentations.
- [ ] Extract structured information.
- [ ] Search and organise authorised files.
- [ ] Generate reports and maintain documentation.

### Data and analytics
- [ ] Data cleaning and transformation.
- [ ] Statistical analysis.
- [ ] Reproducible calculations.
- [ ] Charts and dashboards.
- [ ] Financial analysis and forecasting.
- [ ] Business performance analysis.
- [ ] Data validation and audit trails.

### Business workflows
- [ ] Research opportunities and customer problems.
- [ ] Analyse competitors and markets.
- [ ] Build business plans and digital products.
- [ ] Support SEO and content operations.
- [ ] Evaluate monetisation models.
- [ ] Track revenue and operating metrics.
- [ ] Separate potential revenue from actual earnings.
- [ ] Prefer only free tools and zero-additional-cost operating models. Reject paid and subscription-based options.

### Integrations
- [ ] Discover existing local applications and interfaces.
- [ ] Integrate useful APIs and MCP servers.
- [ ] Add authorised email/calendar/document workflows where available.
- [ ] Keep integrations optional, replaceable and permission-scoped.
- [ ] Never make paid connectors essential.

**Acceptance:** Real productivity and data-processing workflows can be completed through the central JARVIS interface.

## PHASE 10 — Creative and multimodal studio
**Status: NOT STARTED**

### Images and design
- [ ] Evaluate local image-generation models.
- [ ] Generate and edit images.
- [ ] Create graphics and logos.
- [ ] Process and inspect images.
- [ ] Analyse screenshots with local vision where practical.
- [ ] Check GPU/storage requirements before model downloads.

### Audio and voice
- [ ] Local speech-to-text.
- [ ] Local text-to-speech.
- [ ] Voice interaction.
- [ ] Audio processing and transcription.
- [ ] Record supported voice limitations.

### Video and documents
- [ ] Video processing and conversion.
- [ ] Document extraction and understanding.
- [ ] PDF/image analysis.
- [ ] Multimedia report generation.

**Acceptance:** JARVIS generates, processes and inspects actual local outputs.

## PHASE 11 — Automation, scheduling and monitoring
**Status: NOT STARTED**

### Task engine
- [ ] One-time, recurring and dependent tasks.
- [ ] Task priority, status and cancellation.
- [ ] Retries and hard timeouts.
- [ ] Checkpoints and safe recovery.
- [ ] Duplicate-execution prevention.
- [ ] Persistent task state.

### Monitoring and alerts
- [ ] Monitor selected applications and services.
- [ ] Monitor local model health and resource use.
- [ ] Monitor selected project files and scheduled jobs.
- [ ] Detect stalled tasks and failures.
- [ ] Provide clear alerts and logs.
- [ ] Build system health and activity dashboard.
- [ ] Recover safe interrupted jobs.
- [ ] Test controlled interruptions.

**Constraint:** Local schedules require the computer and relevant services to be running. Do not claim work continues while the PC is shut down.

**Acceptance:** Multiple real scheduled jobs execute, are monitored and recover from controlled interruptions.

## PHASE 12 — Measured self-improvement
**Status: NOT STARTED**

### Measurement
- [ ] Task completion rate.
- [ ] Research quality and citation correctness.
- [ ] Tool selection accuracy.
- [ ] Coding performance and test pass rate.
- [ ] Agent reliability and error recovery.
- [ ] Model latency and resource usage.
- [ ] User feedback and regression frequency.

### Controlled improvement loop
- [ ] Collect traces.
- [ ] Identify recurring failures.
- [ ] Determine root causes.
- [ ] Propose changes.
- [ ] Test in an isolated environment.
- [ ] Run repeatable benchmarks.
- [ ] Compare against baseline.
- [ ] Keep only measurable improvements.
- [ ] Roll back regressions.
- [ ] Record results.

- [ ] Never allow uncontrolled changes to security policies, permissions or critical infrastructure.

**Acceptance:** Improvement is demonstrated on repeatable benchmarks, not claimed as unmeasured self-learning.

## PHASE 13 — Final hardening and release
**Status: NOT STARTED**

### Zero-cost compliance audit
- [ ] Inventory all dependencies, APIs, models, MCP servers, integrations and hosted services with licence and pricing evidence.
- [ ] Verify no required workflow depends on paid access, credits, trials or subscriptions.
- [ ] Audit all code/configuration fallback paths for paid-provider calls or billing triggers.
- [ ] Verify local-first inference and local storage of memory, research data, project files, task history and logs.
- [ ] Test that unavailable free providers fail safely without paid fallback.
- [ ] Document capabilities that cannot be delivered for $0 and keep them marked unavailable.

- [ ] Full security review.
- [ ] Permissions and exposure audit.
- [ ] Integration and regression testing.
- [ ] Model-routing and memory tests.
- [ ] Desktop-control and administrator-operation tests.
- [ ] Software-development acceptance test.
- [ ] Automation and recovery testing.
- [ ] Performance and resource testing.
- [ ] Offline-mode testing.
- [ ] Backup restoration test.
- [ ] Documentation and installation instructions.
- [ ] Release preparation and rollback.
- [ ] Final acceptance report.
- [ ] Known limitations documented.
- [ ] Verified release checkpoint.

**Acceptance:** End-to-end tests pass, recovery is demonstrated, security boundaries are tested and remaining limitations are documented.

---

## 4. User-facing experience across the installed applications

**Status: NOT STARTED — integration and division of responsibility must be verified**

No separate JARVIS OS desktop application is assumed or planned as part of this integration milestone.

- [ ] Keep OpenJarvis as the existing direct desktop AI workspace.
- [ ] Use the OpenClaw Control UI as the initial view of coordinated agent tasks and sessions, if its local setup and security checks pass.
- [ ] Use OpenCode's own interface/session for software-development work when direct developer interaction is needed.
- [ ] Make task progress, agent ownership, tool use, changed files, research sources, approvals, errors, verification status and deliverables visible in the relevant application.
- [ ] Avoid building a replacement dashboard until the native interfaces and hand-offs have been proven.
- [ ] Consider a unified front end only after the four applications work reliably together and there is a demonstrated user need.

Do not simulate progress or display capabilities as active when they are unavailable.

---

## 5. Security and permission model

**Status: NOT STARTED**

| Tier | Permission | Boundary |
|---|---|---|
| 0 | Read-only | Read permitted information |
| 1 | Normal execution | Reversible file and development operations |
| 2 | Elevated | Approved installations and admin operations through Windows UAC |
| 3 | Sensitive | Explicit approval required |

Tier 3 requires explicit approval for:
- Financial transactions and purchases.
- Sending external communications.
- Publishing production releases.
- Destructive operations or permanent deletion of important data.
- Major Windows security changes.
- Sharing private information externally.

Implementation checklist:
- [ ] Localhost-only access by default.
- [ ] Authentication for exposed services.
- [ ] Secure credential storage and secret redaction.
- [ ] Tool-specific and agent-specific permissions.
- [ ] Audit logs.
- [ ] Download and installer verification.
- [ ] Network exposure review.
- [ ] Prompt-injection protection.
- [ ] Treat webpages, emails, documents and third-party tool outputs as untrusted data.
- [ ] Keep approval enforcement outside the model.
- [ ] Prevent unrestricted elevated shell execution.
- [ ] Backup and recovery for important state.

---

## 6. Android and iOS

**Status: NOT STARTED**

### Android first
- [ ] Evaluate local Android SDK and command-line tooling.
- [ ] Establish a free local build workflow if needed.
- [ ] Build Android applications and generate APKs locally.
- [ ] Test on available devices.
- [ ] Support local debugging.
- [ ] Explore secure JARVIS-to-Android communication.
- [ ] Build useful mobile companion functions.

Google Play publication is optional; paid developer registration must not be a project dependency.

### iOS later
- [ ] Evaluate cross-platform source-code options.
- [ ] Reuse shared application logic where practical.
- [ ] Prepare source projects on Windows where supported.
- [ ] Document macOS/Xcode requirements.
- [ ] Do not depend on paid cloud builds.
- [ ] Do not promise native signing or App Store distribution under the $0 rule unless requirements are genuinely met.

---

## 7. Logical architecture

**Status: DESIGN PENDING ACTUAL SOURCE INSPECTION**

Proposed logical components (not an instruction to duplicate or move existing OpenJarvis directories):

- OpenJarvis foundation.
- Extensions: agents, tools, skills, integrations.
- Intelligence: model registry, routing, benchmarks.
- Research: search, extraction, verification, freshness.
- Computer control: filesystem, terminal, browser, desktop.
- Administration: installation, elevation, audit.
- Memory: personal, projects, knowledge, evidence.
- Task engine: planning, execution, scheduling, recovery.
- Security and permissions.
- Interface.
- Monitoring.
- Tests and documentation.
- Configuration.

Checklist:
- [ ] Map the actual existing architecture.
- [ ] Select extension location.
- [ ] Define module interfaces and service boundaries.
- [ ] Define configuration and logging strategy.
- [ ] Preserve upstream compatibility.
- [ ] Avoid unnecessary complexity and duplication.

---

## 8. End-to-end acceptance suite

A capability is complete only when the test passes and evidence is recorded.

| ID | Acceptance test | Required evidence |
|---|---|---|
| T01 | Direct local inference | Real response from installed local model |
| T02 | OpenJarvis local inference | Real response through actual OpenJarvis runtime |
| T03 | Model routing | Different task categories use appropriate models |
| T04 | Live research | Current multi-source report with source citations |
| T05 | Multi-agent task | Coordinated agents complete a real task |
| T06 | Persistent memory | Project context survives restart |
| T07 | Filesystem | Permitted real file task and verified result |
| T08 | Browser | Real browser task and verified page state |
| T09 | Desktop | Real Windows UI action and verified resulting state |
| T10 | Administration | Approved installation and verified version |
| T11 | Software development | Multi-file task passes actual tests |
| T12 | Productivity | Real document/data workflow |
| T13 | Creative | Real local creative output |
| T14 | Scheduling | Real scheduled task with execution log |
| T15 | Recovery | Controlled interruption and safe recovery |
| T16 | Security | Unauthorised operation is blocked |
| T17 | Offline | Core local functions work without internet |
| T18 | Backup | Restore procedure succeeds in a separate location |
| T19 | Zero-cost compliance | Dependency inventory, licence and pricing checks, no mandatory paid paths or paid fallback, and local data storage verified |
| T20 | Full Windows desktop control | An OpenJarvis agent performs and verifies real UI actions in File Explorer, Notepad, Settings, a browser and VS Code, with screenshots/UIA evidence |
| T21 | Desktop-control security boundaries | Unauthorised/ambiguous actions are blocked; UAC and secure desktop are not bypassed; cancellation and recovery are demonstrated |
| T22 | One shared Ollama runtime | Process/port ownership, /api/tags, real response and clean restart; no competing listener |
| T23 | OpenJarvis uses shared Ollama | Actual OpenJarvis chat response, exact model/endpoint and no unnecessary model download |
| T24 | OpenClaw uses local Ollama | Local-only provider, real response and a verified harmless tool call |
| T25 | OpenCode uses local Ollama | Model discovery, real coding task and local test evidence |
| T26 | OpenClaw → OpenCode ACP | Session creation, scoped workspace, result, cancellation and test output |
| T27 | OpenClaw → OpenJarvis MCP | Whitelisted tool discovery/call, permission enforcement and failure handling |
| T28 | Shared task context | Correct instructions and task scope reach each participating application |
| T29 | Integrated end-to-end task | OpenClaw coordinates OpenJarvis tool use and OpenCode work; output independently verified |
| T30 | Autonomy and safety | Allowed tasks proceed; forbidden/approval-gated tasks stop; audit records are produced |
| T31 | Restart and recovery | Gateway, desktop, Ollama owner and ACP sessions recover without duplicate execution or port conflicts |

---

## 9. Task record standard

For each major task, record:
- Task ID and description.
- Status: NOT STARTED / WORKING / BLOCKED / PARTIAL / VERIFIED.
- Priority and dependencies.
- Files/modules affected.
- Implementation performed.
- Tests executed.
- Actual results and evidence.
- Known limitations.
- Rollback method.
- Next executable action.

Do not tick a checkbox based on intention, generated code or package installation alone.

---

## 10. Immediate execution queue

The immediate priority is integration of the four already-installed applications. Do not start by installing more tools, downloading more models or replacing OpenJarvis.

### Milestone A — Inventory and protect the four applications (CURRENT)
- [ ] **PARTIAL** — Record exact Ollama, OpenJarvis, OpenClaw and OpenCode versions, executable paths and config locations — done: Gateway 2026.11.1/MSIX 2026.11.100.0, prior active Companion v2026.11.1 unpackaged and older installed-apps entry 2026.9.8-1; OpenCode 2.2.7 in T3-P2; 15 November read-only Start-menu inventory confirms Ollama, OpenClaw Companion, OpenCode and OpenJarvis are installed; Ollama CLI path is `%LOCALAPPDATA%\\Programs\\Ollama\\ollama.exe`; OpenClaw/clawctl aliases are present; OpenJarvis preserved checkout is `%USERPROFILE%\\OpenJarvis`, data is `%USERPROFILE%\\.openjarvis`, and installed desktop EXE is `%LOCALAPPDATA%\\OpenJarvis\\openjarvis-desktop.exe` version 1.0.1 while the checkout frontend package declares 1.0.2; remaining: reconcile the installed/check-out version mismatch and map the Companion registration when it is running.
- [ ] **PARTIAL** — Record running processes and local endpoints without changing or stopping services — done: 15 November pre-recovery elevated read-only check confirmed Ollama app/server PIDs 24172/23604 on loopback 53816/11434 and OpenJarvis desktop/backend PIDs 26884/28692 on loopback 8000. In the subsequently user-approved recovery test, closing desktop parent processes left each backend/server child running, so the exact orphan PIDs 28692 and 23604 were stopped; all three ports were then verified free. Current state: Ollama/OpenJarvis are stopped pending a manual relaunch because the available launch mechanisms denied access/blocked the reopen action. No Gateway/Companion process, configuration, model, pairing, ACL or security setting was touched.
- [ ] **PARTIAL** — Refresh the Ollama model inventory; do not pull models — done: 15 November live `/api/version` reports 0.40.16 and `/api/tags` returns exactly qwen3.5:0.8b (752.39M Q8_0), qwen3.5:2b (1.9B Q8_0), qwen3.5:4b (4.2B Q4_K_M) and qwen3.8:27b (27.3B Q4_K_M); `/api/ps` reports no model currently loaded. No model was pulled, removed or replaced; remaining: reconcile qwen3.5:9b from the earlier inventory and perform an approved real completion/tool-use benchmark.
- [ ] **PARTIAL** — Inspect installed OpenJarvis inference and MCP capabilities — done: active local inference through qwen3.5:4b is verified. The installed-release backend’s MCP client supports stdio and Streamable HTTP, with an outer allowed-tool-name filter; current user config has no MCP section or configured server. Its internal MCPServer has no discovered standalone launch command/transport and auto-discovers broad tools including code execution, REPL, web search, memory writes and channel sending, so it is not safe to enable as a default OpenClaw surface. A separate tested restricted adapter now exists at `runtime/openjarvis_readonly_mcp_adapter.py`. Remaining: require explicit approval before adding any temporary OpenClaw MCP registration or live connection.
- [ ] **PARTIAL** — Inspect installed OpenClaw Gateway, Ollama provider, MCP client and ACP support — done: Gateway local model config and ACPX/ACPX doctor verified; remaining: native Companion Node handoff and tool-policy audit.
- [ ] **PARTIAL** — Inspect installed OpenCode Ollama provider and ACP launch support — done: prior T3-P2 evidence records OpenCode 2.2.7 local model/ACP readiness; 15 November current CLI reports 2.2.6 and the redacted active config has exactly one provider, local Ollama at loopback, with no cloud provider/credential assignment. The `openai` string is schema-only. Remaining: reconcile version context and complete a scoped coding-task acceptance through a supported OpenClaw path once its active runtime is repaired.
- [ ] **PARTIAL** — Back up relevant configuration safely, excluding credentials from reports — done: OpenCode JSONC backups and OpenClaw config backup were already present; 15 November metadata inventory also confirms OpenJarvis `config.toml.backup` and `inference.json.backup` beside the preserved live data. No configuration content or credentials were exported; remaining: verify restore copies in a separate location and inventory Companion settings without exporting secrets.
- [x] **VERIFIED** — Record rollback instructions and a baseline OpenJarvis chat/health check — evidence: 15 November approved recovery test stopped OpenJarvis/Ollama, released ports 8000/11434/53816, then user manually reopened the same existing apps. Ollama 0.40.16 restored all four tags; OpenJarvis health returned `ok` after one bounded startup wait and a text-only qwen3.5:4b response returned exactly `JARVIS_RECOVERY_OK` with no tool calls. Immediate Ollama `/api/ps` confirmed qwen3.5:4b at context 16,384; SHA-256 checkpoints for OpenJarvis config/inference, OpenCode config and OpenClaw config all matched pre-test values. Caveat/rollback: closing each desktop parent alone left its backend/server child running; verify and stop only the exact orphan PID before relaunch. No Gateway/Companion, model, setting, pairing, ACL or security change occurred.
- [ ] **BLOCKED** — Resolve the native Companion Node ownership/credential-handoff error — reason: technical-details screenshot confirms populated capabilities/commands and the same generic contract error. Upstream issue #1691 has a matching-version multi-listener reproduction. Proposed package-side fix is to use existing `Gateway.GatewayAddress.ResolvePort(result.Record)` in the `GatewayStatus` callback, plus command-level JSON regression tests for configured-port match, ambiguous unpinned listeners, and nonmatching configured-port cases. Exact patch and test plan are preserved in `patches/openclaw-windows-packaging/`; fix proposal posted to #1691 comment 6818699921. Current linked GitHub account has read/comment but no push permission to packaging source, so upstream branch/PR could not be created. No local Windows package can be built/installed from this session. Await maintainer-reviewed producer patch and official stable MSIX. Do not trigger browser status or restart; no reinstall/token/pairing/ACL/ownership bypass. Keep BLOCKED until Node 1/1 and harmless native action succeed.

**Detailed evidence and exact resume sequence:** [OpenClaw / OpenCode / Ollama handoff — 12 November 2026](docs/OPENCLAW_OPENCODE_OLLAMA_HANDOFF_2026-11-12.md).

### Milestone B — One shared Ollama service
- [ ] Select one process to own the Ollama service after inspecting current startup behaviour.
- [ ] Verify the local endpoint, available model tags and real completion.
- [ ] Test candidate models for context and tool-calling capability.
- [ ] Connect/verify OpenJarvis without triggering another model download.
- [ ] Prove there is no duplicate server, port conflict or broken restart/close behaviour.

### Milestone C — OpenCode standalone
- [ ] Configure the built-in local Ollama provider.
- [ ] Confirm an installed model appears and completes a prompt.
- [ ] Complete one small coding task in a disposable repository.
- [ ] Verify test results, changed-file scope, cancellation and permissions.

### Milestone D — OpenClaw standalone
- [ ] **PARTIAL** — Configure local-only Ollama access — done: primary `ollama/qwen3.8:27b` and local endpoint `127.0.0.1:11434`; remaining: audit effective provider/fallback configuration.
- [ ] **PARTIAL** — Verify the Gateway and local Control UI — done: Gateway running on loopback 50368 and browser Control UI authenticated; remaining: resolve the separate native Companion Node handoff and browser proxy status.
- [ ] **PARTIAL** — Verify a real local response and harmless tool call — done: browser ACPX prompt returned READY from local Qwen; remaining: test a harmless tool call and disposable coding task.
- [ ] Set bounded permissions, logs, timeout and cancellation policies.
- [x] **VERIFIED** — Leave external messaging channels unconfigured until local integration passes — evidence: diagnostics bundle reported zero channels; retain this state until the security review.

### Milestone E — Join the applications
- [ ] **PARTIAL** — Connect OpenClaw to OpenCode using the supported ACP integration — done: ACPX registered/enabled; explicit OpenCode 2.2.7 executable and `["acp"]` args applied; direct ACP and browser ACP simple-prompt tests returned READY; remaining: complete a disposable coding task through the current OpenClaw ACPX binding with workspace/permission evidence.
- [ ] **PARTIAL** — Prove delegation, scoped work, result return and cancellation — done: simple prompt result returned through browser ACPX; remaining: verify changed files, tests, ACPX cancellation/timeout and full result reporting.
- [ ] Expose a limited OpenJarvis MCP tool set, if supported by the installed build.
- [ ] Connect OpenClaw to OpenJarvis using local stdio MCP where supported, otherwise authenticated loopback MCP.
- [ ] Verify tool whitelisting, actual responses and failure isolation.
- [ ] **BLOCKED** — Verify the native Windows Companion desktop route — reason: native Companion Node remains offline after the Gateway ownership/credential-handoff check; browser ACP success is a separate path.

### Milestone F — Shared context and safe autonomy
- [ ] Provide one consistent project instruction set and task hand-off format.
- [ ] Keep MASTER_TODO.md as the sole authoritative project checklist.
- [ ] Make OpenClaw the single runtime coordinator for multi-step tasks.
- [ ] Add bounded retries, timeouts, cancellation, checkpoints and restart recovery.
- [ ] Allow autonomous low-risk work only in explicitly approved workspaces.
- [ ] Require approval for installs, elevation, deletion, publishing, external messages, payments and credential use.

### Milestone G — End-to-end proof
- [ ] Complete one disposable-project task that uses Ollama, OpenClaw, OpenJarvis MCP and OpenCode ACP together.
- [ ] Verify the resulting files and tests independently.
- [ ] Verify all four applications remain independently usable.
- [ ] Verify local-only inference, no additional spending and clean restart/recovery.
- [ ] Record evidence for T22–T31 and update the live status.

### Existing foundation work — continue without losing it
- [ ] Verify repository and .openjarvis backup contents; review recorded access-denied entries.
- [ ] Test recovery into a separate location.
- [ ] Preserve the local OpenJarvis custom source, build and data; never overwrite them without a verified backup.
- [ ] Establish an isolated extension/workspace strategy only after the four-application baseline is recorded.
- [ ] Continue the longer-term research, memory, Windows desktop control, administration, productivity, creative, Android and hardening roadmap only in dependency order.

---

## 11. Live status — last verified evidence

**Last recorded evidence date:** 15 November 2026.

| Milestone | Status |
|---|---|
| Ollama HTTP API and OpenJarvis backend model catalogue | VERIFIED — 15 November 2026: Ollama 0.40.16 `/api/tags` and OpenJarvis `/health`, `/v1/info`, `/v1/models` responded locally. Both expose qwen3.5:0.8b, qwen3.5:2b, qwen3.5:4b and qwen3.8:27b; OpenJarvis active runtime reports qwen3.5:4b. |
| Master specification | Defined |
| Absolute zero-cost constitution | DOCUMENTED in master and agent instructions; full dependency/runtime audit NOT VERIFIED |
| Initial Windows/hardware audit | VERIFIED |
| Ollama local models inventoried | VERIFIED — 15 November 2026 live `/api/tags` returns four local IDs: qwen3.5:0.8b, qwen3.5:2b, qwen3.5:4b and qwen3.8:27b. The prior qwen3.5:9b record remains unreconciled; no model change was made. |
| OpenJarvis repository identified | VERIFIED |
| Existing custom/dirty working tree identified | VERIFIED |
| Initial repository backup | PARTIAL — files copied; directory access errors remain |
| .openjarvis copy | COPY COMPLETED; restore not yet tested |
| Git checkpoint | NOT STARTED |
| Local inference test package | PREPARED; not yet executed |
| Direct local inference | NOT VERIFIED |
| OpenJarvis-to-local-model integration | VERIFIED — 15 November 2026 active backend `/health` returned `ok`; text-only `/v1/chat/completions` via qwen3.5:4b returned exactly `JARVIS_LOCAL_OK` with no tool calls, and immediate local Ollama `/api/ps` showed that exact model loaded at context 16,384. No model/configuration/install change occurred. |
| Model router | NOT STARTED |
| Research engine | NOT STARTED |
| Multi-agent workforce | NOT STARTED |
| Persistent memory | NOT STARTED |
| Full Windows computer control | CORE REQUIREMENT — NOT STARTED; no live desktop bridge or end-to-end application tests verified |
| Secure administration | NOT STARTED |
| Autonomous coding | NOT STARTED |
| Productivity integrations | NOT STARTED |
| Creative studio | NOT STARTED |
| Automation and monitoring | NOT STARTED |
| Measured self-improvement | NOT STARTED |
| Final hardening | NOT STARTED |
| Integrated four-application architecture | DOCUMENTED — target roles, MCP/ACP hand-offs, phases and acceptance tests recorded in Section 0A; implementation NOT STARTED | Version inventory and live compatibility checks remain. |
| Ollama / OpenJarvis / OpenClaw / OpenCode shared runtime | PARTIAL — 15 November live Ollama/OpenJarvis sharing and a recovery completion are verified: four local tags, OpenJarvis text-only qwen3.5:4b response, post-restart recovery response and unchanged protected configuration hashes. Clean shutdown needs exact child-process verification after parent closure; OpenClaw/OpenCode shared-runtime and full four-app integration remain unverified. | Repeat one-at-a-time restart checks, then continue OpenCode/OpenClaw acceptance items. Do not touch the blocked native Companion route. |
| OpenClaw Gateway and native Windows Companion | PARTIAL / BLOCKED — technical-details screenshot confirms full approved/effective capability/command lists but generic contract error persists. Upstream issue [#1691](https://github.com/openclaw/openclaw-windows-node/issues/1691) documents a matching-version multi-listener producer defect: an auxiliary browser listener causes Gateway service status to omit configured `gateway.port` and then `gateway.ownership`. Current main uses `ObservedPorts.Count == 1` despite an existing safe resolver. A one-line patch and test plan are saved privately and proposed to maintainers in [issue comment](https://github.com/openclaw/openclaw-windows-node/issues/1691#issuecomment-6818699921). No upstream push permission; no local package was changed. | Await reviewed producer fix and official stable MSIX; then verify Companion Node 1/1 and harmless native action. |
| OpenCode local Ollama provider | PARTIAL — 15 November static fallback audit confirms active config defines only `ollama` at loopback with qwen3.8:27b primary and qwen3.5:4b small; no cloud provider/credential is configured, and the only `openai` reference is schema-only. Current CLI reports v2.2.6 versus earlier T3-P2 v2.2.7 evidence. | Reconcile version context and complete a supported scoped coding-task acceptance after active OpenClaw runtime repair. |
| OpenClaw → OpenCode ACP | PARTIAL — ACPX is enabled and explicitly launches OpenCode 2.2.7 with `acp`; direct CLI/ACP tests and a fresh browser Control UI session returned READY via local Qwen. No real delegated coding task through the current OpenClaw ACPX binding has been verified yet; native Companion desktop route remains blocked by its separate Node handoff. | Complete a bounded disposable coding task through ACPX with changed-file/test evidence and cancellation; verify native desktop route separately after Node handoff is fixed. |
| OpenClaw → OpenJarvis MCP | BLOCKED — separately tested read-only adapter exists and is unregistered. A 15 November discovery-only `openclaw mcp add` was rejected before save because active OpenClaw 2026.11.1 resolves to isolated profile `C:\Users\T3-P2\.openclaw` and its MCP runtime cannot spawn the expected MSIX agent-node executable (`ENOENT`). Read-only list confirms no managed server was saved; Boxont config hash is unchanged. | Wait for an official supported repair of the active Gateway/MSIX runtime; do not modify the isolated profile or attempt a workaround. |
| Repository agent instruction files | VERIFIED — created and read back from private GitHub |
| OpenJarvis runtime auto-bootstrap and automatic master-file writer | PARTIAL — controller files committed; Windows runtime test pending |
| OpenJarvis hidden-console / repair-build continuation | PARTIAL — local repair logs were preserved in the 12 November handoff. A CREATE_NO_WINDOW source patch was backed up and applied for a test build; first offline build failed and original source was restored. A second Cargo stdout log records release-profile compilation finishing in 49.66s, but no final EXE hash/launch/runtime verification was captured. A separate temporary repair copy built the Vite frontend but Rust `web_atoms` failed with Windows error 5 (Access denied). No source/binary/installer from these attempts was committed to jarvis-os; preserve the local custom checkout and verify exact source/build state before further changes. | Reconcile local source/backup state, inspect the Rust build stderr for the permission-denied attempt, and confirm which desktop EXE is actually installed/running before considering any replacement. |
| Existing OpenJarvis desktop recovery and managed restart | VERIFIED — custom dashboard is restored; chat works; managed restart test v2 passed two consecutive launches. Backend `/health` returned `ok`; `/v1/models` returned `qwen3.5:9b`, `qwen3.8:27b`, `qwen3.5:2b`, `qwen3.5:0.8b`, `qwen3.5:4b`. After each desktop close, the registered backend process was gone, port 8000 had zero listeners and `/health` did not respond; the second launch was healthy. New local EXE SHA-256: `085244CCEFF72B00AC05F50515036481C58B5640A03C04340C0BCF0DB6AF2D0C`. Managed-shutdown source changes are in `C:\Users\Boxont\OpenJarvis\frontend\src-tauri\src\lib.rs`; the source checkout and EXE changes remain local and have **not** been committed/pushed as OpenJarvis source code. No new installer was created. |
| Full Windows restart recovery | VERIFIED — 8 November 2026 post-restart report `OpenJarvis-Windows-Restart-Check-20261108-173443-408-20508-bb737624.txt` records: first desktop launch PID 2688; healthy backend and all five models; user-confirmed custom dashboard and real chat reply; clean desktop/backend shutdown with port 8000 free and stale PID 10252 stopped; second desktop launch PID 22172 healthy with all five models and backend PID 19716; app left running. |

---

## 12. Permanent project directive

Build the broadest practical personal AI operating system possible using existing hardware, local models, free software, legitimate public information and authorised computer access.

- Actual execution is more important than feature claims.
- Current evidence is more important than stale memory.
- Verification is more important than claimed completion.
- Reliability is more important than uncontrolled autonomy.
- Zero additional expenditure is non-negotiable.

**BUILD → TEST → VERIFY → RECORD → IMPROVE.**

One private repository. One master checklist. Every checkbox earned.

---

## 13. Mandatory AI session startup and task-status protocol

The repository root `AGENTS.md` is the canonical instruction file for compatible coding agents. Tool-specific startup files (such as `CLAUDE.md` and `.github/copilot-instructions.md`) point agents back to it and to this master plan.

At the start of every JARVIS session, the AI must:
1. Read the complete latest `MASTER_TODO.md`; never rely on old chat memory or a partial excerpt.
2. Read `AGENTS.md` and any relevant nested instructions.
3. Identify the current milestone, active task, dependencies and acceptance criteria.
4. Select one task at a time unless the user explicitly authorises a batch.
5. Mark the task **WORKING** in this file before implementation.
6. Briefly report the active task and its verification target.

### Required task-status notation

| Markdown form | Status | Rule |
|---|---|---|
| `- [ ] Task` | NOT STARTED | Default for untouched work |
| `- [ ] **WORKING** — Task` | WORKING | Only one active task by default |
| `- [ ] **BLOCKED** — Task — reason: ...` | BLOCKED | State blocker and next action |
| `- [ ] **PARTIAL** — Task — done: ...; remaining: ...` | PARTIAL | Work exists but acceptance is not met |
| `- [x] **VERIFIED** — Task — evidence: ...` | VERIFIED | Actual test passed; include evidence |

Only mark a checkbox `[x]` when the relevant acceptance criteria have passed. Code generation, package installation, a prepared script or a build alone is not proof of end-to-end capability. If a session ends early, convert WORKING to PARTIAL or BLOCKED and record the next action. Never leave a stale WORKING marker.

At the end of each session, update this master file, phase status, live status and next task; record tests and actual results; add a dated execution-log entry; synchronise to the private GitHub repository where access permits; and read the remote file back to verify the update. Never claim that GitHub was updated without read-back verification.

Do not create another competing project checklist. This file remains authoritative.

## 14. Execution log

Add newest entries at the top. Keep each entry short and evidence-based.

| Date | Task / milestone | Status | Evidence / result | Next action |
| 2026-11-15 | Audit OpenCode effective provider/fallback configuration | VERIFIED — local-only static provider audit passed; no config change | Redacted config inspection found exactly one provider: Ollama at `http://127.0.0.1:11434/v1`, with qwen3.8:27b primary and qwen3.5:4b small. No cloud provider or credential assignment was configured. The only `openai` text belongs to the `$schema` host `opencode.ai`. Current CLI reports v2.2.6; prior T3-P2 evidence reports 2.2.7, recorded as a discrepancy. Config SHA-256 remained unchanged. | Reconcile version context when the supported active OpenClaw runtime is repaired; do not add a cloud fallback. |
| 2026-11-15 | Attempt temporary OpenClaw discovery-only registration of read-only adapter | BLOCKED — OpenClaw runtime path missing; no registration saved | OpenClaw 2026.11.1 `mcp add` tried to launch through missing isolated-profile agent-node path `C:\\Users\\T3-P2\\AppData\\Local\\OpenClawGatewayMSIX\\agent-node\\node-v24.22.1-win-x64\\node.exe` and failed `ENOENT` before saving/configuring the adapter. Read-only `mcp list` confirms no managed MCP servers in the active T3-P2 profile. Boxont `openclaw.json` SHA-256 remains the pre-test value. No T3-P2 profile, Gateway, Companion, pairing, token, ACL, security setting or model was changed. | Wait for official supported runtime repair; retry only discovery after verifying the active runtime path. |
| 2026-11-15 | Implement and test isolated OpenJarvis read-only MCP adapter | VERIFIED — source/test committed and live read-only checks passed; no registration | Added `runtime/openjarvis_readonly_mcp_adapter.py` and `tests/test_openjarvis_readonly_mcp_adapter.py`. The adapter uses stdio MCP framing, three fixed no-argument tools and six fixed loopback endpoints; it rejects arguments/unknown tools and excludes prompts, files, shell, processes, web, memory and messaging. Five fixture/protocol tests passed; all three tools passed against live local endpoints; Python compilation passed; protected config hashes remained unchanged. Remote read-back verified both files. | Obtain explicit approval before temporary OpenClaw registration and tool-discovery-only validation. |
| 2026-11-15 | Design separate read-only OpenJarvis MCP adapter | PARTIAL — design committed/read back; no adapter or integration enabled | Added `docs/OPENJARVIS_READONLY_MCP_ADAPTER.md` and read it back. It specifies a local stdio-only adapter, six fixed loopback read endpoints, three read-only tools (health/models/runtime status), hard exclusion of prompts/files/shell/process/web/memory/channel access, bounded timeouts, safe errors, audit fields, and staged verification before temporary OpenClaw configuration. This follows installed-source evidence that the built-in MCPServer default surface is too broad. | Implement and unit-test the adapter in the JARVIS workspace without connecting it; request approval before any OpenClaw configuration. |
| 2026-11-15 | Complete approved Ollama/OpenJarvis recovery test |
| 2026-11-15 | Approved clean Ollama/OpenJarvis recovery test | BLOCKED — clean shutdown reached; supported relaunch unavailable to this environment | Pre-test config checkpoint hashes were captured for OpenJarvis config/inference, OpenCode and OpenClaw config. Closing OpenJarvis desktop PID 26884 left Python backend PID 28692/port 8000; closing Ollama app PID 24172 left server PID 23604/port 11434. The exact orphan PIDs were stopped under the approved recovery scope, and ports 8000/11434/53816 were verified free. The normal launcher command was blocked and computer-use access was denied for Ollama, so neither existing app could be reopened. No Gateway/Companion, model, configuration, pairing, ACL or security change occurred. | User manually opens the installed Ollama and OpenJarvis apps once; resume with read-only health/model checks. |
| 2026-11-15 | Refresh four-application inventory and inspect OpenJarvis capability metadata | PARTIAL — live local-model path and MCP boundary verified; no MCP connection | User-approved read-only registration checks confirmed existing Ollama app/server PIDs 24172/23604 and OpenJarvis desktop/backend PIDs 26884/28692 on loopback ports 53816/11434/8000. Ollama 0.40.16 `/api/tags` and OpenJarvis `/health`, `/v1/info`, `/v1/models` passed without restart, configuration change or model download. A text-only OpenJarvis `/v1/chat/completions` request with qwen3.5:4b returned exactly `JARVIS_LOCAL_OK`, no tool calls; immediate Ollama `/api/ps` showed qwen3.5:4b loaded locally at context 16,384. Installed MCP client supports stdio/Streamable HTTP and tool-name filtering, but no standalone server launch path was found; internal MCPServer auto-discovers broad write/execution/messaging tools. Current config declares no MCP server. Saved inference metadata qwen3.8:27b differs from active qwen3.5:4b; it was not changed. | Document/test rollback and clean restart behavior; evaluate a narrow read-only MCP adapter design. Native Companion Node remains BLOCKED pending official reviewed stable fix. |
|---|---|---|---|---|
| 2026-11-12 | Propose and preserve the minimal Gateway multi-listener status repair | BLOCKED — exact patch prepared and sent to maintainers; upstream source write access and local Windows build unavailable | User-provided Companion technical-details screenshot confirms full approved/effective capability and command lists; generic isolated-session contract error persists. Posted a specific proposed one-line change to [issue #1691](https://github.com/openclaw/openclaw-windows-node/issues/1691#issuecomment-6818699921): use existing `Gateway.GatewayAddress.ResolvePort(result.Record)` in the GatewayStatus callback. Saved candidate patch and required regression-test plan under `patches/openclaw-windows-packaging/`. Existing resolver preserves configured-port attribution among multiple observed listeners while retaining unambiguous/ambiguous controls; it does not bypass ownership checks. Upstream repository metadata says current GitHub account has pull=true/push=false; branch creation returned 403. No upstream code, installed package, Windows config, Gateway process, credentials or pairing changed. Exact local multi-listener sample remains unproven. | Wait for maintainer-reviewed fix and official stable Gateway MSIX; then install/test only the supported release and require Node 1/1 plus a harmless permitted native action. || 2026-11-12 | Confirm the Gateway multi-listener status-port defect and identify its minimal packaging repair | BLOCKED — source-level producer defect confirmed upstream; no official fix package or write access to upstream repo | Fresh review of Companion issue [#1691](https://github.com/openclaw/openclaw-windows-node/issues/1691) found a detailed reproduction: packaged `openclaw browser status --json` initializes an auxiliary loopback listener in the Gateway Node process; later `clawctl gateway-service status --json` drops both `gateway.port` and `gateway.ownership`, causing Companion's running-Gateway parser to reject the response before credentials are sent. A later issue report lists Gateway MSIX 2026.11.100.0 / payload 2026.11.1 and Companion 2026.11.1, matching this PC's installed pair. Current packaging main commit `7185d5ea504643e0799f3ae665f64180261d5da5` still uses `ObservedPorts.Count == 1` at `Program.cs` line 1095; the existing `GatewayAddress.ResolvePort()` helper and tests safely preserve a configured port among multiple observed listeners while rejecting ambiguous unpinned listeners. Missing port also suppresses serialized ownership. Proposed one-line fix: `int? port = Gateway.GatewayAddress.ResolvePort(result.Record);` plus command-level JSON regression. Existing local status and PID/sequence checks passed, so exact failing multi-listener state has not been captured locally; Windows TCP count does not establish isolated-session ObservedPorts count. Do not run `openclaw browser status --json` to test, or restart/install/reset/bypass. The issue reports a local dev-package success, not an official release. Companion PR #2114 is diagnostic-only and blocked on localization/WSL E2E CI; upstream branch creation was denied 403. No PC changes. Detailed handoff section 21 committed. | Keep Node BLOCKED; inspect existing Companion Show technical details view only, then track upstream packaging fix through an official stable build and validate 1/1 plus a harmless native action. || 2026-11-12 | Recheck current Gateway packaging source, open fixes, stable releases and Companion diagnostic PR | BLOCKED — no official producer-side repair; Companion diagnostic PR remains unmerged | Current packaging main commit `7185d5ea504643e0799f3ae665f64180261d5da5` still uses `ObservedPorts is { Count: 1 }` when selecting `gateway.port` for `gateway-service status` (Program.cs line 1095). No open packaging PR was found for this selector defect. Latest Gateway stable release remains `v2026.11.1-msix.0`, matching installed MSIX identity `2026.11.100.0`. Companion PR #2114 remains open/unmerged, requires localization and lacks native E2E proof; CodeQL/core/Tray passed, while three WSL E2E jobs failed to provision Ubuntu 24.04 because DNS resolution failed (`WININET_E_NAME_NOT_RESOLVED`). Existing local status, listener PID and process-sequence checks already passed. No local changes made. | Do not reinstall the same package or repeat local checks. Inspect only Companion's existing Show technical details view; if it remains generic, stop local probing and wait for reviewed producer/consumer fixes. Keep Node BLOCKED until Node 1/1 and harmless native action pass. |
| 2026-11-12 | Recheck upstream native Node diagnostic PR #2114 and required CI | BLOCKED — proposed diagnostic fix is not merge/release-ready; local Node issue remains unresolved | PR #2114 remains open at head `865a61892a6132a7876840c4de8e01767076c808`. CodeQL passed; Core/CLI, Tray/setup/integration and fast-validation jobs passed. The Build and Test workflow/CI gate failed because Revocation Recovery, Setup and Connect, and Network Recovery WSL E2E jobs could not provision Ubuntu 24.04 (`Wsl/InstallDistro/WININET_E_NAME_NOT_RESOLVED`); Setup and Connect reported 24/71 failures from the shared fixture setup failure. Latest review still requires localization of the new user-facing message. PR improves malformed-response diagnosis but does not fix the Gateway producer or prove real installed-package behavior. No local packages, config, Gateway, tokens or pairings were changed. | Do not install PR branch or change local setup. Track reviewed/localized Companion diagnostic work and a separate official stable Gateway packaging repair. Keep native Node BLOCKED until 1/1 online and harmless native action passes. |
| 2026-11-12 | Verify the active Companion executable/version and fresh Gateway runtime status | PARTIAL — active stable Companion build identified; native Node ownership handoff still fails | User-provided screenshots show Companion About: `v2026.11.1`, build date 7 November 2026, stable channel, x64, unpackaged (developer), Windows `10.0.26300.0`. PowerShell process inventory identified `OpenClaw.Tray.WinUI.exe` PID `4776`, path `C:\Users\Boxont\AppData\Local\OpenClawTray\OpenClaw.Tray.WinUI.exe`, file version `2026.11.1.0`. The combined command emitted a null-path `Get-Item` error for `openclaw-session-host.exe` PID `2780`, whose `ExecutablePath` was blank; the Companion executable record was still returned. `clawctl status`: session running, agent T3-P2, runtime Node.js 24.22.1, Gateway running on port 50368, activation none pending, recovery configured. UI screenshots still show overall Connection degraded, Gateway record Connected, Operator Reconnecting, Windows Node 0/1, and `Gateway ownership inspection failed. Credentials were not sent.` Add/Remove Programs still separately lists Companion 2026.9.8-1, which is not proven to be the active running application. No install, restart, token, pairing, model or configuration changes were made. | Open Companion Diagnostics; capture a fresh Connection timeline and Recent log for one controlled Node reconnect, redacting credentials and identifiers. |
| 2026-11-12 | Re-read the already-uploaded OpenClaw diagnostics and cross-check the Companion/Gateway failure path against upstream source | PARTIAL — failure narrowed to Companion isolated-session ownership/contract inspection; precise local rejected field not yet observable | Existing Library bundle openclaw-diagnostics-20261112-004308.txt generated 12 Nov 00:43 +10 was re-read. It confirms Operator authentication completes (hello-ok), NodeDeviceToken resolves, Node client is created with 7 capabilities/26 commands, Node WebSocket receives connect.challenge, then Companion blocks credential handoff with the isolated-session-contract error. Setup logs show gateway-service status exits 0 but summary says session/readiness unreported; companion prepare --check exits 0; listener 50368 is verified; config validate returns valid. The same setup log records a package-managed Gateway stop/start on 9 Nov; do not repeat. Current screenshot error Gateway ownership inspection failed maps to Companion's generic exception catch in IsolatedGatewayRuntime.InspectAsync; it catches several exception classes and exposes only generic text / exception type. Current client StatusAsync requires gateway.port, ownership.sandboxId, ownership.agentUserSid, ownership.listeners, and listener port/processId/processStartTimeUtc/sequenceNumber. Current packaging main still selects status port only when ObservedPorts.Count == 1; upstream #1691 has a 11 Nov report with exactly Gateway MSIX 2026.11.100.0 and Companion v2026.11.1, same error, and missing port/ownership in status. Upstream #2020 documents this generic message for later malformed lifecycle responses. PR #2114 would report operation/field but remains open, needs localization and has no real MSIX E2E proof. The user's manual status check separately reported one listener and ownership metadata present, so the multi-listener cause is not yet proven on this PC. No new Windows actions, restarts, installs, token/pairing changes, or configuration writes were performed in this review. | Continue upstream fix/release verification; only request a targeted safe field-presence comparison if needed, not another diagnostics export. |
| 2026-11-12 | Verify official upstream stable releases and targeted ownership-fix status | PARTIAL — no supported stable package repair published; installed builds are current stable | Gateway packaging releases page still lists v2026.11.1-msix.0, released 5 Nov 2026, payload 2026.11.1 and identity 2026.11.100.0; release notes list unrelated Hyper-V and staged-package dependency changes, not the observed-port/ownership selector. Latest Companion release page lists stable v2026.11.1, promoted 7 Nov; v2026.11.2-alpha.10 (8 Nov) is marked prerelease and is not recommended. Current packaging main Program.cs still uses ObservedPorts.Count == 1 for selected Gateway status port. Targeted search found no open packaging PR explicitly mentioning ObservedPorts. Companion PR #2114 remains open with status waiting on author and a localization review request; it improves diagnostic classification but does not repair the Gateway package. No Windows changes made. | Next: request a single safe status JSON shape summary (marker/state/port/ownership/listener counts and identity-field-presence booleans) to reconcile package output with the Companion inspection failure. |
| 2026-11-12 | Confirm fresh Gateway status contract fields after release review | PARTIAL — producer response fields are complete; next isolate local Companion process ownership verification | User's fresh command result: Ok=True; Integration=isolated-session; IntegrationVersion=1; State=running; PortPresent=True; OwnershipPresent=True; SandboxIdPresent=True; AgentSidPresent=True; ListenerCount=1; ListenerFieldsComplete=True. No sensitive field values were printed. This means the latest package response contains the fields Companion's StatusAsync requires and the one-listener selector is not currently producing a missing-port response in this invocation. The remaining source-level check is IsolatedGatewayRuntime.InspectSnapshot: it captures Windows TCP listener PIDs and validates loopback address, process sequence number, match against the package-attested listener PID/sequence pair, and stable second snapshot. The earlier CIM owner/start-time attempt was inconclusive and is not evidence of failure. | Compare the package listener processId with current Get-NetTCPConnection OwningProcess for port 50368, and check whether Get-Process can read process start time; only report booleans/PID match. |
| 2026-11-12 | Cross-check Companion failure against upstream reports and stable releases | PARTIAL — external issue evidence recorded; PC-specific cause remains unproven | Reviewed open upstream Windows Node issues [#1691](https://github.com/openclaw/openclaw-windows-node/issues/1691) and [#2020](https://github.com/openclaw/openclaw-windows-node/issues/2020), plus open PR [#2114](https://github.com/openclaw/openclaw-windows-node/pull/2114). #1691 describes a multi-listener status selector that can drop the configured Gateway port and ownership; this PC's recorded detailed status and TCP snapshot show one listener with port/ownership present, so that path is not reproduced. #2020 explains that the same generic error may mask a malformed later lifecycle response. PR #2114 proposes operation/field-specific credential-safe diagnostics, but it is unmerged, awaits a localization change and does not claim a real Gateway/Companion end-to-end repair. Official releases show Gateway MSIX `v2026.11.1-msix.0` (payload 2026.11.1; package identity 2026.11.100.0) and stable Companion `v2026.11.1`; the active app's App Info reported v2026.11.1/Current, so Add/Remove Programs `2026.9.8-1` alone does not establish the active app is outdated. Updated detailed handoff with these distinctions and links. | Run the read-only process-path query to map the active Companion executable; then collect the exact failing operation/field from a fresh native Connection timeline/Recent log. No reinstall, restart, credential reset, pairing reset or ownership bypass. |
| 2026-11-12 | Independently confirm Windows Gateway listener and package identity | PARTIAL — Gateway listener and MSIX identity reconfirmed; native Companion mismatch unresolved | User-provided read-only PowerShell output: Windows 11 Pro `10.0.26300`, build `26300`, 64-bit; `Get-NetTCPConnection -State Listen -LocalPort 50368` returned exactly one row, `127.0.0.1:50368`, PID `25904`; `Get-AppxPackage` returned only `OpenClawFoundation.OpenClawGateway`, version `2026.11.100.0`, full package name `OpenClawFoundation.OpenClawGateway_2026.11.100.0_x64__rfcbke2p71se2`. The separate Add/Remove Programs entry reports Companion `2026.9.8-1`; earlier running App Info reported unpackaged/developer Companion `v2026.11.1`. These read-only checks corroborate the Gateway listener/package state but do not map the active Companion executable or resolve Node credential handoff. No packages, settings, credentials, tokens or pairings were changed. | Run the documented read-only process identity command to capture the active Companion executable path; compare it with the registered `2026.9.8-1` entry, then capture a fresh native Connection timeline/Recent log. |
| 2026-11-12 | Recheck Gateway/Companion contract and preserve OpenJarvis repair/build evidence | PARTIAL — Gateway and Companion preparation schemas pass; native Node handoff still blocked; OpenJarvis repair builds not fully verified | Windows 11 Pro build 26300. `Get-AppxPackage` returned Gateway MSIX 2026.11.100.0; running Companion App Info had shown unpackaged v2026.11.1 while Add/Remove Programs listed 2026.9.8-1, with active executable path still unknown. Gateway is running on 50368; status reports `isolated-session v1`, ownership/sandbox/account fields, one matching loopback listener (PID 25904) and valid listener metadata; `clawctl companion prepare --check` reports `ok=true`, port 50368 and token configured (value omitted). CIM owner/start-time attempts were inconclusive, not proof of an identity mismatch. Companion Operator connects but Node credentials are blocked before handoff; one Gateway restart did not resolve it. OpenJarvis logs show the CREATE_NO_WINDOW helper patch was backed up; first offline build failed and restored source; a second Cargo stdout record says release profile finished in 49.66s but final executable/runtime verification is absent. A separate temporary repair build completed Vite but failed Rust `web_atoms` with Windows error 5 (Access denied). No OpenJarvis source/binary, Gateway/Companion package, token or pairing was changed or committed by this documentation sync. | Identify the active Companion executable and reconcile it with the registered app entry; capture a fresh native Connection timeline/Recent log; only then select a verified official stable package repair. Keep the OpenJarvis source and binaries preserved locally; commit application code only after the exact source repository/remote and dirty state are audited. 
| 2026-11-12 | Record the current OpenClaw / OpenCode / Ollama integration checkpoint and native Companion blocker | PARTIAL — local model and browser ACP path work; native desktop Node handoff remains blocked | Added [the detailed handoff note](docs/OPENCLAW_OPENCODE_OLLAMA_HANDOFF_2026-11-12.md). T3-P2 OpenCode 2.2.7 loads four local Qwen tags; direct CLI and direct ACP prompts returned READY. OpenClaw Gateway 2026.11.1 / MSIX 2026.11.100.0 is running on loopback 50368; status and Companion preparation checks pass. OpenClaw Qwen 27B context is 65,536 and `ollama ps` confirmed that context. A fresh browser ACPX session spawned OpenCode with explicit `acp` args and returned READY. Native Companion App info showed unpackaged v2026.11.1 while installed-apps listing showed 2026.9.8-1; Gateway/Operator connect but Node credential handoff is blocked with ownership-inspection error, credentials not sent. Browser proxy 50370 was not listening in the support bundle. No model downloads, paid services, token resets, pairing resets or package reinstalls were performed; secrets and device identifiers omitted. | Identify the active Companion executable/install record; capture a fresh Connection event timeline and Recent log; resolve native Node handoff with a confirmed official package fix; then run a disposable ACP coding task and continue OpenJarvis MCP verification. |
| 2026-11-09 | Verify OpenCode cancellation | VERIFIED — Esc stopped generation | User completed the disposable long-generation cancellation test and confirmed pressing Esc stopped generation and returned control to the user. The task did not require tools, create files or modify project content. | Audit OpenCode's effective provider configuration and confirm it cannot silently fall back to a cloud provider. |
| 2026-11-09 | Test OpenCode `.env` read approval | VERIFIED — user approved the read before the dummy value was revealed | User clarified that OpenCode displayed an approval prompt for reading the disposable `.env` file and they approved it before the agent returned `DUMMY_KEY=not-a-real-secret`. The initial transcript only showed the post-approval read, which was misinterpreted as an unprompted read. This confirms the `read:*.env ask` rule behaves as intended for this test. No shell command or edit was used; the file contained only dummy data. The separate `.env` edit-deny test passed, and external-directory deny separately blocked reads/writes outside workspace. | Read approval is verified; cancellation has also been completed. Audit the effective provider configuration and confirm no cloud fallback before proceeding to OpenClaw Gateway setup. |
| 2026-11-09 | Complete OpenCode external-directory hard-deny acceptance test | VERIFIED — external read and write rejected in a fresh Build session | The user supplied the transcript: attempted to read `...\OpenCode-External-Deny-Test-20261109-214857\outside\external.txt`; tool returned `permission.rejected: Permission denied: external_directory`. Attempted to write `...\outside\blocked.txt`; tool returned `permission.rejected: Permission denied: external_directory`. No approval dialog, retry or workaround was used; the agent reports no files were created or modified in this fresh test. The session footer confirms Build with local `qwen3.8:27b`. | Test `.env` read requiring approval and cancellation in another disposable session; preserve the earlier stray file from the initial failed `ask` test until cleanup is authorised. |
| 2026-11-09 | Apply hard-deny rule for OpenCode external directories | PARTIAL — hard-deny configuration saved and backup created; fresh-session test pending | User changed the single global `external_directory` resource `*` effect from `ask` to `deny`; output confirms the six rules remain: external_directory deny, shell ask, `.env` and `.env.*` reads ask, `.env` and `.env.*` edits deny. Backup created at `C:\Users\Boxont\.config\opencode\opencode.json.backup-20261109-214753`. Official OpenCode v2 docs confirm `external_directory` is checked before read/edit outside both Location and worktree, and `deny` blocks the operation. This config change has not yet been tested in a fresh session. | Start a new isolated project root with a sibling outside directory; verify external read and write are denied without approval or file creation. Keep the old stray test file intact until its cleanup is expressly approved. |
| 2026-11-09 | Verify OpenCode external-directory hard deny | VERIFIED — fresh-session read and write both rejected | User's Build session using `qwen3.8:27b` attempted one read and one write against a sibling `outside` directory. Both returned `permission.rejected: Permission denied: external_directory`; no approval prompt appeared, and the agent reported no files were created or modified in that fresh test. This proves the hard-deny rule blocks external read and write. Earlier `ask` test's stray file remains untouched. Global config backup remains at `C:\Users\Boxont\.config\opencode\opencode.json.backup-20261109-214753`. | Continue OpenCode safety checks with `.env` read approval and cancellation; then audit provider fallback before proceeding to the OpenClaw Gateway setup. |
| 2026-11-09 | Verify the loaded OpenCode config source and active session locations | PARTIAL — global policy confirmed; project worktree root not yet established | Latest `opencode debug config` output explicitly lists `C:\Users\Boxont\.config\opencode\opencode.json` as a loaded document, with all six expected permission rules, and the config directory as the only other source. `opencode api GET /api/debug/location` returned two active locations, one for `...\OpenCode-Permission-Test-20261109-210242\workspace` and one for `...-210352\workspace`. The attempted session/project correlation produced empty output, so it did not establish the project worktree root. Current v2 documentation says an external path is checked only when it is outside both the active Location and a non-root project worktree; this remains the leading unresolved explanation to verify. Do not mark the boundary feature as passing. | Query the raw project and session lists separately and correlate the actual project worktree with the test folder. If the sibling directory is outside both, record a genuine policy enforcement failure and switch the global external-directory rule to deny before any real-project use. |
| 2026-11-09 | Check OpenCode Windows external-directory permission behaviour against current docs and issue reports | WORKING — determine active project boundary and resolved config sources | Current v2 documentation says external-directory checks apply to paths outside both the active Location and the non-root project worktree; the API output gives the active Location but not the project worktree. Therefore the sibling `outside` folder is outside the Location but may still be within a broader project worktree; this is not yet ruled out. Current Windows issue reports include #36681 (July 2026) describing path/merge behaviour and a later comment saying it improved but lacked clear Windows documentation; older #16126 reports `external_directory` ask/deny bypass on Windows, but are not conclusive for the user's exact v2.2.6 desktop build. Official v2 docs still specify `external_directory:* ask` as the correct rule. No local config was changed and the unexpected test file remains untouched. | Inspect `opencode debug config` source list and `/api/project` worktree for the 2026-11-09 test location. Then decide whether to hard-deny external directories in config, isolate the workspace with a Git root, or treat this build's boundary enforcement as unreliable. |
| 2026-11-09 | Confirm the OpenCode permission test's sibling folder is outside the active Location | PARTIAL — active root confirmed; external-directory rule still failed to prompt | User-provided `opencode api GET /api/debug/location` output lists two active sessions, including `C:\Users\Boxont\AppData\Local\Temp\OpenCode-Permission-Test-20261109-210242\workspace` and a later workspace at `...-210352\workspace`. The tested `outside` directory is a sibling of the first `workspace`, and the test file exists there. Global config still shows `external_directory` resource `*` effect `ask`; `.env` edit denial worked, but both external sibling read and create were executed without a prompt. Thus the earlier theory that the parent temp folder was the active Location is not supported by the API output. This remains a security-test failure; no cleanup or corrective permission change was made. Current OpenCode v2 docs specify `external_directory` should be checked for paths outside the active Location/worktree and that `*`/`ask` is the documented approval rule. | Inspect unfiltered but redacted `opencode debug config` permission section and OpenCode permission logs; then back up the config and consider changing external-directory rule to `deny` for a fresh-session retest. Do not use OpenCode on real projects until external writes are blocked or approval-gated. |
| 2026-11-09 | Investigate unexpected OpenCode external-folder access in safety test | PARTIAL — `.env` edit correctly denied; external-directory prompt did not appear | User's OpenCode transcript records a sibling `outside` directory beside the intended `workspace`. A read of `outside.txt` succeeded without a prompt; editing the workspace `.env` was denied with `permission.rejected`; writing `outside/should-not-be-created.txt` succeeded without a prompt and the agent verified the file exists. This is a failed boundary acceptance test, not a pass. No attempt was made to remove the test file. Current OpenCode v2 documentation says `external_directory` is checked before `read`/`edit` for paths outside the active Location/project worktree, and that default external access is allowed unless an explicit matching rule overrides it. Possible explanation: the actual OpenCode Location/worktree root was the parent test directory, making `outside` internal to its active location; this is not yet confirmed. Another possibility is that the expected permission rule did not match the effective session policy. | Inspect OpenCode's loaded Location via `opencode api GET /api/debug/location`, global config path/resolved `external_directory` rule and recent redacted permission logs. Then re-run boundary test with an unambiguously external directory. Keep the harmless temp file untouched pending user approval. |
| 2026-11-09 | Start OpenCode workspace-boundary and cancellation verification | WORKING — isolated permissions test | Current official OpenCode v2 permission documentation confirms ordered `permissions` rules, last-match-wins behaviour, and that `external_directory` is checked before `read`/`edit`. The existing global file has six rules; shell approval was already observed working. Next run will use only a timestamped temp workspace with a dummy `.env` and a harmless external text file, never real project data. | Verify external-path approval, `.env` edit denial, and cancellation; then close this task with actual results before moving to OpenClaw Gateway setup. |
| 2026-11-09 | Complete the disposable OpenCode coding task with local Qwen | VERIFIED — three-file utility created and all tests passed | OpenCode Build using `qwen3.8:27b` created only `package.json`, `src/math.js`, and `test/math.test.js` under `C:\Users\Boxont\AppData\Local\Temp\OpenCode-Integration-Test-20261109-001524`. The uploaded ZIP was inspected and contains exactly those three files. `package.json` defines `npm test` as `node --test`; the math module exports validated `add` and `subtract`; the test suite covers sums, differences, fractions and invalid inputs. User's OpenCode transcript shows four tests passed, zero failed, duration 67.6299 ms. Independently reran `npm test` from the uploaded files in a clean environment (Node v22.16.0): four tests passed, zero failed, 77.665 ms. This verifies the created artefacts and test suite. The user's Windows run was labelled Build · qwen3.8:27b; no packages or internet were used according to the task transcript. | Next verify workspace boundaries and cancellation, then complete OpenCode permissions checks; proceed to OpenClaw Gateway setup only after the standalone OpenCode checks are closed. |
| 2026-11-09 | Verify OpenCode shell-command approval in a fresh session | VERIFIED — approval prompt shown and approved command executed | User-provided OpenCode transcript: Build agent using `qwen3.8:27b` requested approval for `node --version`; after approval, command ran and returned `v26.12.0`. Response footer: `Build · qwen3.8:27b · 32.5s · 3.0 tok/s`. This verifies the global shell `ask` rule is active in a new session and the local Ollama model is still selected. User also reports the earlier disposable Node coding task is complete; exact test output/changed-file list has not been supplied, so coding-task acceptance remains PARTIAL pending evidence. The `.env` protections and external-directory prompts have not yet been directly exercised. No existing project files were changed by the shell approval check. | Capture the disposable coding test's actual created-file list and `npm test` result, then verify that Build stayed within the disposable workspace; exercise `.env` deny only in a disposable test if still needed. |
| 2026-11-09 | Validate the OpenCode v2 permission configuration | PARTIAL — configuration parses and loads; runtime approval behaviour not yet exercised | User ran JSON parsing and `opencode debug config`; result: `JSON valid; 6 permission rules` and `OpenCode configuration loaded successfully` (exit code 0). Current official OpenCode v2 permissions documentation confirms the `permissions` array with `action`, `resource`, `effect` is the v2 schema, so this is not merely accepted unknown JSON. The six configured rules ask before external-directory access and shell execution, ask before reading `.env` and `.env.*`, and deny editing `.env` and `.env.*`. A new session is required to apply the global settings; actual prompts/denials have not yet been tested. | Open a fresh OpenCode session in the disposable test workspace; verify a harmless shell action triggers approval and `.env` edits are denied before using Build on a real project. |
| 2026-11-09 | Create OpenCode v2 safety permissions | PARTIAL — global policy file created; effective policy load still needs verification | User executed the one-line PowerShell command; it created `%USERPROFILE%\.config\opencode\opencode.json` and printed `OpenCode permissions created.` The file uses OpenCode v2 `permissions` rules: ask before external-directory access and all shell commands; ask before reading `.env` / `.env.*`; deny editing `.env` / `.env.*`. The rule schema matches current OpenCode v2 documentation. This is a global config and applies to new sessions; the already-running disposable coding test session may not reload it. The CLI has not yet been run against the new config after creation, so effective loading remains unverified. No existing config was overwritten. | Validate the JSON and run OpenCode v2's config diagnostic in a new session; then confirm shell approvals and `.env` protections behave as intended before permitting real-project edits. |
| 2026-11-09 | Verify OpenCode can answer through the local Ollama model | PARTIAL — local model/provider response confirmed; disposable coding test remains | User ran the read-only structure inspection in OpenCode. The tool identified the working directory as `C:\Users\Boxont` (the Windows profile, not a project), read the directory without modifying files, and reported `Model: qwen3.8:27b`, `Provider: ollama`; the run footer showed `Build · qwen3.8:27b · 5m 6s · 3.9 tok/s`. This confirms a real OpenCode response labelled with the installed local Ollama model and Build agent, but the command was launched from the wrong working directory and was an inspection-only test. Response latency was slow and must be measured again in a controlled coding task. No project files were changed. | Launch OpenCode in a disposable test workspace, perform one small multi-file coding task, run its tests and verify the changed-file scope and actual result. Then record timing and resource use before deciding if 27B is practical as the default. |
| 2026-11-09 | Replace the legacy OpenCode CLI with the current v2 CLI | VERIFIED — OpenCode CLI version mismatch corrected | User executed the one-line removal of global `opencode-ai` 1.19.5 and installation of `@opencode/cli` with its allowed install script. npm reported three packages installed, and `opencode --version` returned `opencode v2.2.6`, matching the separately installed OpenCode Desktop 2.2.6. Desktop app and `.config\opencode\service.json` were not changed; its password value remains private. No model was downloaded and no cloud provider was selected. Ollama launch / local model completion from OpenCode has not yet been re-tested. | Retry `ollama launch opencode`, select only the already-installed local `qwen3.8:27b` option, and verify OpenCode starts and returns a real local response; then test Build-agent file read/edit in a disposable workspace. |
| 2026-11-09 | Diagnose OpenCode CLI mismatch during Ollama launch | PARTIAL — wrong CLI major version and blocked postinstall identified; correction pending | User-provided Windows output: OpenCode Desktop is registered as 2.2.6, but `Get-Command opencode` resolves to `%APPDATA%\npm\opencode.ps1` and reports 1.19.5 from the legacy `opencode-ai@1.19.5` npm package installed by `ollama launch opencode`. npm explicitly warned that the package's `postinstall` script was not allowed. `opencode debug config` returns `Error: Unexpected error`; no `opencode.json/jsonc` exists in the checked locations, while `.config\opencode\service.json` contains a password key whose value was not read. Current OpenCode v2 docs use `@opencode/cli`, whose postinstall selects the native platform binary; OpenCode 1 and 2 both use the `opencode` command and cannot be installed side-by-side by default. Ollama launch failure is therefore explained by a legacy v1 CLI rather than the selected Qwen model. No CLI package, desktop app, service config, model or data was changed during diagnosis. | Replace only the legacy global `opencode-ai` CLI with the current `@opencode/cli` package while explicitly allowing its required install script; verify the `opencode --version` result is 2.x before retrying Ollama integration. Preserve OpenCode Desktop and service files. |
| 2026-11-08 | Identify why OpenClaw Companion starts without a Gateway | PARTIAL — Companion is healthy in MCP-only node mode; local Gateway has not been provisioned | User-provided `openclaw-tray.log` shows startup at 23:28 and 23:31: `Local AI router startup state: NotInstalled`; `Starting Windows Node in MCP-only mode (no gateway)`; WSL check; `WslKeepAlive` reports distro `OpenClawGateway` not found; node warns `no gateway node client is attached`; Companion registers its local MCP HTTP server on port 8765 and reports `Started MCP-only node service without gateway connection`. No setup wizard logs exist at either documented `easy-setup-latest` path. This confirms the tray Companion is running as a Windows node/MCP endpoint, not as a connected Gateway or local agent coordinator. Existing WSL contains only `docker-desktop`; Gateway recovery scheduled task targets a missing executable/package. No application, task, config, model or WSL state was changed. Current official Windows Hub docs say use the Companion's Gateway Setup shortcut and choose local WSL Gateway setup; it provisions the dedicated `OpenClawGateway` distro without altering an existing Ubuntu distro. | Launch the installed **OpenClaw Gateway Setup** shortcut from the Start menu, review the setup preview/capabilities, and choose the supported local WSL Gateway setup; send the setup result/log if it fails. Do not manually delete the recovery task, edit `openclaw.json`, create a replacement distro or expose port 8765 before the Gateway and its security settings are verified. |
| 2026-11-08 | Confirm the OpenClaw Gateway recovery task points to a missing package executable | PARTIAL — orphaned recovery task confirmed; Companion log inspection remains | Latest read-only Windows report confirms the registered task action targets `C:\Users\Boxont\AppData\Local\Microsoft\WindowsApps\OpenClawFoundation.OpenClawGateway_rfcbke2p71se2\openclaw-gateway-recovery.exe`, but `Test-Path` returns false. `Get-AppxPackage -AllUsers` found no matching Gateway package, and `wsl --list --verbose` shows only `docker-desktop`; therefore the task references a recovery helper/package that is not present and no app-owned `OpenClawGateway` distro is registered. Task Scheduler event query returned no matching events in the queried window. Companion files found include `openclaw-tray.log` and `Logs\diagnostics.jsonl`; no `Logs\Setup\easy-setup-latest.txt` was found. Official current OpenClaw docs identify `easy-setup-latest.txt` and `easy-setup-latest.jsonl` as setup diagnostics, and say the Companion's Gateway Setup/Connections flow provisions the local WSL Gateway. No component, task, config or WSL distro was changed. | Inspect the existing Companion tray and diagnostics logs (redacting any tokens); determine whether local setup was attempted and its failure stage before opening the Companion's supported Gateway Setup repair flow. |
| 2026-11-08 | Diagnose the OpenClaw Gateway recovery task and locate the OpenCode desktop config | PARTIAL — failure isolated to Gateway recovery helper; root cause not yet known | User-provided read-only report: scheduled task `OpenClaw Gateway OpenClawFoundation.OpenClawGateway_rfcbke2p71se2` is enabled and Ready; its action is the package-qualified `openclaw-gateway-recovery.exe` alias with no arguments; last run 8 Nov 2026 17:23:13 and `LastTaskResult=1` (non-success result). Loopback port 18789 did not respond. `Get-AppxPackage` returned no matching package in the current query, and the earlier WSL list showed only `docker-desktop`, not the expected app-owned `OpenClawGateway` distro. The expected `easy-setup-latest.txt` path was absent. OpenClaw Companion registry version is 2026.9.8-1 while tray executable file version is 2026.11.1.0; this discrepancy remains unexplained. OpenCode CLI reports `opencode v2.2.6`; its config directory contains `service.json` with a `password` key, but the value was deliberately not read. No app, task, distro, config or model was changed. Official OpenClaw Windows guidance says local setup provisions an app-owned WSL Gateway distro and recommends inspecting setup/companion logs when setup fails; the exact cause here remains unverified. | Inspect the exact Gateway alias's existence/package registration, Task Scheduler event history and available Companion logs; then use the existing Companion Gateway Setup flow if the Gateway has not been provisioned. Keep the OpenCode service password private. |
| 2026-11-08 | Identify the installed OpenClaw Companion and OpenCode desktop components | PARTIAL — companion and desktop CLI located; Gateway provisioning state still unknown | Follow-up read-only Windows output: OpenClaw tray executable is `C:\Users\Boxont\AppData\Local\OpenClawTray\OpenClaw.Tray.WinUI.exe`, file version `2026.11.1.0`; installed-app registry reports `OpenClaw Companion version 2026.9.8-1`, so the two version fields differ and require package-level confirmation. A scheduled task whose name begins `OpenClaw Gateway OpenClawFoundation.OpenClawGateway_...` exists; its state, action and last result have not yet been inspected. `wsl --list --quiet` returned only `docker-desktop`, with no visible `OpenClawGateway` distro. `.openclaw\openclaw.json` exists with top-level keys `agents` and `models` only (values not read). No OpenClaw CLI executable was found in the checked locations. OpenCode desktop is registered as 2.2.6; its running bundled CLI file version is 1.4.4 at `C:\Users\Boxont\AppData\Roaming\ai.opencode.desktop\cli\2.2.6-x64\opencode-cli.exe`; `C:\Users\Boxont\.config\opencode\service.json` exists, while the checked standard `opencode.json` files do not. No config values, tokens or secrets were read; no machine or application state was changed. | Inspect the OpenClaw scheduled task's action, state and last result, plus the Companion setup log and package identity; then verify OpenCode's CLI version/config metadata without exposing service credentials. |
| 2026-11-08 | Receive initial read-only inventory of the four installed applications | PARTIAL — application and endpoint baseline started; integration remains untouched | User-provided report collected 2026-11-08 23:35:13. Ollama 0.40.15 is running from `C:\Users\Boxont\AppData\Local\Programs\Ollama\ollama.exe`; `/api/tags` on port 11434 returned `qwen3.5:2b`, `qwen3.5:0.8b`, `qwen3.5:4b` and `qwen3.8:27b`. OpenJarvis desktop EXE is version 1.0.1 at `C:\Users\Boxont\AppData\Local\OpenJarvis\openjarvis-desktop.exe`; its saved `inference.json` says Ollama, `qwen3.8:27b`, confirmed=true, but no OpenJarvis process was running and port 8000 did not respond. OpenClaw tray process is running and `.openclaw\openclaw.json` exists, but `openclaw` was not found on PATH and port 18789 was not listening. OpenCode's `opencode-cli.exe` process was running from the desktop app's `2.2.6-x64` directory; the checked standard config paths were absent. No application, configuration, model or process was changed. | Run one more read-only check to identify OpenClaw's app-managed CLI/Gateway setup, OpenCode's parent desktop process and actual config path; then capture the OpenJarvis baseline while it is open. |
|---|---|---|---|---|
| 2026-11-08 | Clarify the integrated workflow, shared memory, model strategy and autonomy model | DOCUMENTED — explanatory architecture added; no software configuration changed | Expanded the master plan with an end-to-end explanation: OpenClaw receives and coordinates tasks; OpenJarvis provides its existing desktop workflow and only verified MCP tools/context; OpenCode performs scoped coding through ACP; Ollama serves local models; JARVIS OS remains the repository and plan name only. Added provisional roles for the five existing Qwen tags, model/tool/context benchmarks, shared repository-based project memory, version uncertainties, permission boundaries and a concrete website-feature workflow. Current official documentation was checked for OpenClaw Ollama setup, ACP, MCP, sandboxing, OpenCode permissions and OpenJarvis MCP. The OpenClaw sandbox is off by default and OpenCode defaults require explicit review; both facts are recorded as setup requirements. | Begin with a read-only inventory of the four installed applications; do not change configs or download models until baseline and backups are recorded. |
| 2026-11-08 | Rebuild the master plan around the four installed applications | DOCUMENTED — architecture and phased integration plan updated; no application configuration changed | Clarified that JARVIS OS is only the project/repository/plan. Defined Ollama as the shared local model service; OpenClaw Gateway as the target runtime coordinator; OpenCode as the coding harness; and OpenJarvis as the existing desktop AI workspace and potential MCP tool provider. Added inventory, shared-Ollama, standalone OpenCode, standalone OpenClaw, ACP, MCP, shared-context, autonomy and end-to-end phases plus tests T22–T31. Checked current official OpenClaw Ollama/MCP/ACP, OpenCode Ollama and OpenJarvis MCP documentation. Installed versions and live compatibility remain unverified. | Execute Milestone A inventory before changing any settings, installing plugins or downloading models. |
| 2026-11-08 | Verify full Windows restart recovery | VERIFIED — post-restart launch, desktop, chat, model availability and clean shutdown passed; second launch passed | User supplied the successful report `C:\Users\Boxont\Desktop\OpenJarvis-Windows-Restart-Check-20261108-173443-408-20508-bb737624.txt` (run began 17:34:43). First launch started existing desktop PID 2688; `/health` returned `status=ok`; all five models were available (`qwen3.5:9b`, `qwen3.8:27b`, `qwen3.5:2b`, `qwen3.5:0.8b`, `qwen3.5:4b`); registered backend PID 10252 was running; user confirmed the customised dashboard was visible and a real chat reply was received. On normal close, desktop exited, backend stopped, port 8000 was free and stale registered PID 10252 was not running. Second launch started desktop PID 22172; `/health` returned `ok`; all five models were available again; backend PID 19716 was registered and running; final result was PASS and OpenJarvis was left running. The report filename is the timestamped 17:34:43 file, not one of the earlier failed-attempt reports. No source-code changes were made in this documentation update. | Continue Milestone A: run the direct Ollama test and prove a real local-model response through the actual OpenJarvis runtime; then continue backup verification and safe checkpoint work. |
| 2026-11-08 | Repair full Windows restart recovery check | PARTIAL — replacement package prepared; Windows run pending | The earlier full-restart tester did not run because Windows PowerShell rejected its script text. The user then ran the ASCII-only replacement, but its report writer encountered a Windows file-lock error while logging the first desktop-launch message. That error occurred before the `Start-Process` launch command, so this attempt did not launch OpenJarvis or complete launch/shutdown checks. Prepared `OpenJarvis-Full-Windows-Restart-Test-REPAIRED.zip`: it buffers report messages in memory, writes the report once at completion to a unique filename, and falls back to the Windows temporary folder if Desktop writing fails. Local package checks passed: script is ASCII-only, no `Add-Content` remains, delimiters are balanced and ZIP integrity passed. This script has not been executed in Windows PowerShell here; Windows runtime parsing and the full post-restart check remain unverified. No OpenJarvis source, EXE, configuration, models or user data changed. | Resolved by the later successful full-restart run recorded immediately above; retain this entry as the troubleshooting history. |
| 2026-11-08 | Restore customised OpenJarvis desktop and verify managed restart | VERIFIED — two consecutive managed launches and clean shutdowns passed | User confirmed the custom dashboard is visible again and chat works. The rebuilt local desktop EXE is `C:\Users\Boxont\OpenJarvis\frontend\src-tauri\target\release\openjarvis-desktop.exe`, SHA-256 `085244CCEFF72B00AC05F50515036481C58B5640A03C04340C0BCF0DB6AF2D0C`. The local Tauri source change in `frontend\src-tauri\src\lib.rs` makes the exit handler await backend cleanup and terminates the managed Windows child process tree. User's managed restart test v2 report (`C:\Users\Boxont\Desktop\OpenJarvis-Restart-Test-v2-20261108-170734.txt`) shows: first launch healthy with all five models; after close, registered backend PID 14524 was gone, listener count on port 8000 was 0 and health was unavailable; second launch healthy with all five models; final state left OpenJarvis running. Stale PID registration after the managed child has exited is expected and was safely replaced on the next launch. Recovery backups retained on Desktop: `OpenJarvis-Dashboard-Backup-20261108-162836`, `OpenJarvis-ServiceWorker-Backup-20261108-163211`, `OpenJarvis-Stale-Server-Backup-20261108-164419`, and `OpenJarvis-Shutdown-Fix-Backup-20261108-170237`. This commit updates the JARVIS planning record only: the OpenJarvis source/EXE modifications remain in the local checkout and are not represented as a source-code commit here. | Continue Milestone A by running the direct Ollama and actual OpenJarvis local-inference tests, then resume backup verification and safe checkpoint work. |
| 2026-11-08 | Clarify closed-app process snapshot | PARTIAL — process list correctly reflects intentional shutdown | User clarified OpenJarvis had already been closed before the latest PowerShell process check. The empty process list in that uploaded output is therefore expected after an intentional close and must not be interpreted as an app crash or failed startup. Earlier live candidate run remains valid evidence: `openjarvis-desktop.exe` PID 4828, `uv.exe` PID 27320 and Python backend PIDs 4012/7780; `/health` returned `ok`; `/v1/models` returned five local model IDs. The saved inference config and HOME fallback were independently verified. Tauri setup status and UI handoff remain unverified while app is closed. No machine state, source, config, binaries, models or user data changed. | On next launch of the candidate, inspect Tauri setup screen/status and error while process is still running; verify `ready` handoff and then check Dashboard/model list. |
| 2026-11-08 | Verify Tauri home-directory resolution against confirmed inference config | PARTIAL — HOME fallback path aligned with USERPROFILE; frontend issue remains | User-provided PowerShell output proves `HOME` is genuinely unset (`Test-Path Env:HOME=False`, .NET process HOME is null, length -1), and `USERPROFILE=C:\Users\Boxont`. Rust `home_dir()` calls `std::env::var("HOME").or_else(|_| std::env::var("USERPROFILE"))`, so it should resolve USERPROFILE for a candidate launched from this environment. The confirmed 81-byte `C:\Users\Boxont\.openjarvis\inference.json` therefore appears at the expected path; safe fields previously verified `kind=ollama`, `confirmed=true`, model configured, no credential-named field. WebView diagnostic log found at `C:\Users\Boxont\AppData\Local\com.openjarvis.desktop\EBWebView\Default\settings_diagnostic.log` (426,193 bytes, modified 8 Nov 2026 00:29:50). Local Storage LevelDB log exists (11,115 bytes) but was not dumped to avoid exposing API settings/keys. No separate application `.log` found in the searched locations. No source/config/build/binary/model/user data changed. | Inspect WebView diagnostic errors with a narrow, redacted filter; inspect Rust startup config-loading and background task ordering; identify the actual frontend `get_setup_status` invocation result without exposing local storage. |
| 2026-11-08 | Inspect saved Ollama inference config metadata | PARTIAL — config confirmed at USERPROFILE path; Tauri-resolved path still to verify | User-provided PowerShell output confirms `C:\Users\Boxont\.openjarvis\inference.json` exists, is 81 bytes, last modified 2 Nov 2026 12:39 AM, parses as JSON, and has safe fields `kind=ollama`, `confirmed=true`, model configured, no host configured, and no credential-named field. Raw config was not exposed. `home_dir()` source prefers `HOME` whenever `std::env::var("HOME")` returns `Ok`, falling back to `USERPROFILE` only on an error. The user's shell showed `USERPROFILE=C:\Users\Boxont` and blank `HOME`, but did not establish whether HOME is unset or set to an empty string. If Tauri resolves the same `~/.openjarvis` path, the saved confirmed config should cause auto startup. Earlier launch evidence includes child `uv.exe`/Python processes and healthy `/health` plus five-model `/v1/models`. No configuration, credentials, source, build, installed binary, model or user data changed. | Verify whether process HOME is absent or empty and the candidate's working directory; determine app log location and inspect setup transition/errors without printing secrets; then verify setup reaches ready. |
| 2026-11-08 | Trace configured-at-launch gate and inference config path | PARTIAL — exact startup policy established; actual local config not yet inspected | Latest supplied PowerShell source output confirms Rust `inference_config_path()` resolves to `home_dir()\.openjarvis\inference.json`. `read_configured_inference_config()` parses only that file. In `run()`, `configured_at_launch` is `Some(cfg)` only when a config exists and `cfg.confirmed` is true. A present but unconfirmed config is discarded as an interrupted first-run attempt; an absent config clears a pending secure-store key and remains unconfigured. The initial `SharedStatus` is `SetupStatus::starting(cfg)` only for a confirmed config, otherwise `SetupStatus::default()` (`awaiting_source`, `requires_source=true`). Rust only spawns `start_managed_boot` at app startup when `configured_at_launch.is_some()`. This is the gate separating the standalone HTTP API listener from the Tauri frontend's readiness state. The actual file's presence/metadata/safe fields and `home_dir()` resolution are still unknown. No config contents, credentials, source, build, installed app, models or user data were changed. | Inspect `home_dir()` and report inference.json existence/length/time plus safe non-secret JSON properties only; never expose API keys or secret fields. |
| 2026-11-08 | Trace Rust inference-source configuration and ready-state transitions | PARTIAL — setup-state transition rules identified; actual live Tauri status still unknown | Latest user-provided read-only source scan confirms `SetupStatus::default()` is `phase="awaiting_source"`, source `unconfigured`, and `requires_source=true`. Rust `read_configured_inference_config()` returns to that default and exits if no configured inference source exists. With a config, it sets `SetupStatus::starting(&cfg)`, then moves through `ollama`/`model`/`server`; it sets `phase="ready"` after attaching to an already healthy API server (source lines around 1454–1458) or after its own backend startup succeeds (around 1727–1730). `start_backend` explicitly resets default and returns an error if no configured source is stored. `get_setup_status` only clones the in-memory status. Frontend `getSetupStatus()` invokes that Tauri command and swallows invoke errors as `null`; `SetupScreen` polls every 800 ms and calls `onReady()` only for `phase="ready"`. The source chooser appears when the status says `requires_source=true`; the Ollama path requires explicit confirmation (`Use Ollama and continue`) before persisting source and starting the backend. Although the HTTP backend returned `ok` and five models in a prior live check, the separate Tauri setup status/current screen has not been observed. No local files/configuration, installed binaries, model data or user data were changed. | Inspect Tauri startup's `configured_at_launch` branch plus the setup-state error/rollback paths; check only inference config file path/existence/metadata and process ownership, not contents/secrets; obtain the exact current setup screen heading. |
| 2026-11-07 | Trace Tauri setup-status polling and default state | PARTIAL — setup handoff path confirmed; transition to ready not yet traced | Latest user-provided inspection confirms `SetupScreen.poll()` invokes `getSetupStatus()` every 800 ms and only fetches models plus calls `onReady()` when `s?.phase === 'ready'`. `getSetupStatus()` calls Tauri `invoke('get_setup_status')`; errors are swallowed as `null`. Rust `get_setup_status` returns a clone of in-memory `SharedStatus`. A Rust unit test shows `SetupStatus::default()` starts as `phase="awaiting_source"`, `source="unconfigured"`, `requires_source=true`, `ollama_ready=false`. Thus the desktop can have a healthy independent HTTP API and still remain on the setup UI until the Tauri setup workflow updates its in-memory state. Earlier process/API checks confirmed `/health` and five `/v1/models` results. No local source/build/binary/settings/model/user data changed. | Inspect Rust `SetupStatus` mutation sites and the React inference-source selection/start workflow; confirm current on-screen setup page; then test the transition to `ready` without clearing saved data. |
| 2026-11-07 | Trace Tauri setup gate and model-fetch handoff | PARTIAL — setup gate located; readiness response not yet inspected | Latest user-provided source output: `App.tsx` initialises `setupDone` with `useState(!isTauri())`, so a Tauri desktop launch starts with `setupDone=false`. `handleSetupReady` sets it true and writes `oj-setup-completed=1`, but the displayed code initialises the state from `!isTauri()`, not from that storage key. While false, `App.tsx` returns only `SetupScreen`, bypassing `Layout`, Sidebar and all normal routes including Dashboard. `SetupScreen.poll()` gets setup status; only when `s?.phase === 'ready'` does it fetch models via `fetchModels()` (errors suppressed to `[]`), set the store model list/loading state and call `onReady()`. Therefore a non-ready or failed status poll would leave the user on setup and keep dashboard/model UI out of view even though `/health` and `/v1/models` work. Actual `getSetupStatus()` URL, backend response and poll/error handling remain to inspect. No local source, build, installer, settings, model or user data changed. | Inspect `SetupScreen` poll/effect and `getSetupStatus()` implementation; query that exact status endpoint while candidate backend is active and compare its phase to `ready`. Do not clear storage/reset setup. |
| 2026-11-07 | Trace sidebar visibility and application setup gate | PARTIAL — likely frontend gating path discovered; runtime state unverified | Latest user-provided read-only PowerShell output shows `Layout.tsx` renders `<Sidebar />`; `Sidebar.tsx` defines navigation entries including `{ path: '/dashboard', label: 'Dashboard' }`. Built bundle includes the same dashboard route and nav item. `App.tsx` source order shows `if (!setupDone) return <SetupScreen onReady={handleSetupReady} />;` before `<Routes>`; normal `Layout`, Chat and Dashboard routes are only mounted after setup is marked complete. This can fully explain a missing sidebar/dashboard if `setupDone` is false, but its actual runtime value and persistence source have not yet been checked. Backend `/health` and `/v1/models` are healthy with five models. No localStorage, source, build, installer, models or user data changed. | Inspect `setupDone` initialization/persistence in `src/lib/store.ts` and `App.tsx`, the SetupScreen model-loading code, and report the current on-screen setup page; do not reset setup or clear storage. |
| 2026-11-07 | Confirm dashboard markers in compiled frontend bundle | PARTIAL — custom bundle assets contain expected route/widgets; navigation/UI problem unresolved | User-provided output shows `dist/index.html` loads `/assets/index-DnLZZ_Ji.js` and `/assets/index-E6fjkWHq.css`. Marker scan of built JS found `/dashboard`, `Dashboard`, `Cost Comparison` and `No models loaded`. Therefore the existing compiled JS includes the dashboard route marker, at least one custom dashboard widget label, and the empty-model state text. `Select-String` against `src/components/Layout.tsx` found no matches for `dashboard`, `Dashboard`, `NavLink`, `to=` or `navigation`; this does not locate or rule out navigation implemented in a child component. Candidate backend previously returned `ok` and all five models while the UI still showed none. Actual Settings API URL has not yet been supplied. No local files, source, binaries, models or user data were changed. | Inspect the full layout component and recursively locate sidebar/navigation components; inspect concise snippets around built bundle route/model markers; ask for the Settings API URL only, excluding API key. |
| 2026-11-07 | Verify candidate desktop backend and local model catalogue while UI remains blank | PARTIAL — backend and model API verified; frontend fault remains | User-provided PowerShell run launched local release candidate with process-scoped `OPENJARVIS_ROOT=C:\Users\Boxont\OpenJarvis`. Process inventory: `openjarvis-desktop.exe` PID 4828; child `uv.exe` PID 27320; Python backend PIDs 4012 and 7780. `GET http://127.0.0.1:8000/health` returned `{"status":"ok"}`. `GET /v1/models` returned five model IDs: `qwen3.5:9b`, `qwen3.8:27b`, `qwen3.5:2b`, `qwen3.5:0.8b`, `qwen3.5:4b`. Thus model files/catalogue and backend startup are not the current blocker; the desktop UI still reportedly displays no models and no customised dashboard. Existing source evidence shows `/` routes to `ChatPage`, `/dashboard` routes to `DashboardPage`, and custom dashboard components are wired. No source, build, installed EXE/MSI, models or user data were changed. | Inspect `Layout.tsx` navigation visibility for a Dashboard link; determine the actual saved Settings API URL (without reading any API key); compare the currently loaded frontend entrypoint/assets with `frontend/dist`; only then choose a minimal safe fix. |
| 2026-11-07 | Verify dashboard route and current backend process state | PARTIAL — route mapped; runtime not active during snapshot | User-provided PowerShell output shows `App.tsx` routes `/` to `ChatPage` and `/dashboard` to `DashboardPage`. The dashboard source imports and renders the custom KPI, hardware monitor/analytics, model runtime, energy dashboard, cost comparison, model performance, energy-cost intelligence, historical analytics and trace debugger. Runtime snapshot listed only `ollama.exe` among OpenJarvis/Ollama-related processes; no OpenJarvis desktop, `uv.exe` or `python.exe` was listed. Port 8000 had no listener and `GET http://127.0.0.1:8000/v1/models` failed to connect; Ollama alone was listening on 11434. Therefore this snapshot was taken without the OpenJarvis backend running and cannot diagnose its in-app model fetch. No local source, build, installer, model or user data was modified. | Start the local release candidate with process-scoped `OPENJARVIS_ROOT`, verify the backend startup/health/models, then navigate to `/dashboard`; inspect the saved API URL if the model list remains empty. Never inspect or expose API keys. |
| 2026-11-07 | Trace customised OpenJarvis desktop UI and API settings | PARTIAL — dashboard source wiring confirmed; desktop runtime still unresolved | Latest user-provided read-only PowerShell output confirms `DashboardPage.tsx` imports and renders `DashboardKpiBar`, `HardwareMonitor`, `HardwareAnalytics`, `ModelRuntimeMonitor`, `EnergyDashboard`, `CostComparison`, `ModelPerformance`, `EnergyCostIntelligence`, `HistoricalAnalytics` and `TraceDebugger`; custom dashboard components are not merely unused files. `SettingsPage.tsx` saves its API URL through `settings.apiUrl`, while `api.ts` gives saved `openjarvis-settings.apiUrl` precedence over the Tauri API base and `http://127.0.0.1:8000`; its actual value was not read. `main.tsx` waits for `initApiBase()` before React rendering. Tauri identifier is `com.openjarvis.desktop`, `frontendDist` is `../dist`; PWA auto-update and Workbox precaching are configured, but stale cache is not proven. The latest process query found no process for stale PID 14220 and no current port-8000 listener; backend health was therefore not established at that moment. Earlier live checks had returned healthy `/health`, `/v1/info` and five-model `/v1/models` responses. No frontend source, build, installed binary, model or user data was changed. | Next: while the candidate desktop app is open, verify the current port-8000 owner and API health; inspect only the saved API URL (never the API key); trace which built frontend assets and route are actually loaded before considering cache or rebuild changes. |
| 2026-11-07 | Recover OpenJarvis desktop and preserve current recovery state | PARTIAL — backend/model catalogue verified; desktop UI recovery unresolved | **Windows checkout:** `C:\Users\Boxont\OpenJarvis` still has extensive modified/untracked custom files; no local source files were modified in this session. `frontend\node_modules`, `frontend\dist` (4 Nov 20:45), and `frontend\src-tauri\target` already exist. The reported top-20 newest frontend source file was `UpdateChecker.tsx` (2 Nov 05:55). Dist JS includes `index-DnLZZ_Ji.js` (1,253,910 bytes) and `charts-BLQhYFDz.js` (388,815 bytes); simple marker search found `Historical Analytics` and `Cost Comparison`, while absence of other identifiers is inconclusive for minified output. **Binaries:** installed EXE version 1.0.2, 21,817,856 bytes, modified 2 Nov 21:43:32, SHA-256 `0A2ACBFEC1C07D94DAEC88EF4959FB8B3B770489618AC8A331FE3295742FECF4`; local release EXE same version/size, modified 4 Nov 20:46:46, SHA-256 `1348CC3AFE2ABFD08005850F30E7DD06AF5A2EB15E5B518F51D8163C7FF49624`; MSI modified 4 Nov 20:46:37, SHA-256 `474AAC2BC6D3C7C5FAF69DCD6B35E61632DDF98E66ECC07BDF06AFBD7BD6047`. Candidate local release EXE launches as PID 3268 but user reports custom UI and models are still absent. While it is open, `uv.exe` PID 11404 and listener PID 14220 were observed; `/health` returned `ok`, `/v1/info` returned model `qwen3.5:9b`, agent `simple`, engine `multi`, and `/v1/models` returned the local model catalogue. Separate Ollama `/api/tags` returned five models: `qwen3.8:27b`, `qwen3.5:2b`, `qwen3.5:0.8b`, `qwen3.5:9b`, `qwen3.5:4b` (no pull required). Local Rust source sets `JARVIS_PORT=8000`; `boot_backend` attaches to a twice-confirmed healthy server and reports foreign port conflicts without killing the listener. `getBase()` prioritises saved `openjarvis-settings.apiUrl` above Tauri API base (possible stale setting, not yet verified); UI model-loading callers suppress errors into empty lists. **Safety:** no npm install, build, model pull/delete, MSI install, Program Files overwrite, source modification, Git reset/clean, or deletion was performed. The old installed EXE and MSI remain untouched. The local OpenJarvis working tree remains dirty and was not synced by this GitHub-only update. | Resume by identifying PID 14220 and checking the saved API URL, app entrypoint, and PWA/service-worker cache; then fix and verify the actual UI path. Do not rebuild/install/overwrite until the cause is established. |
| 2026-11-07 | Diagnose OpenJarvis desktop EXE launch failure and possible source-checkout overlap | PARTIAL — EXE opens; model store verified; customised UI restoration pending | User screenshot showed desktop app unable to create `C:\\Program Files\\OpenJarvis\\src\\.venv` (`Access is denied`, os error 5). Read-only checks found user checkout `C:\\Users\\Boxont\\OpenJarvis` with `pyproject.toml` and Python 3.13.18 `.venv`; installed desktop binary is version 1.0.2; `OPENJARVIS_ROOT` was unset; no listener was found on port 8000. Launching the EXE with process-scoped `OPENJARVIS_ROOT=C:\\Users\\Boxont\\OpenJarvis` now opens the app. User checkout contains extensive modified/untracked React/Tauri, Python server, telemetry, security, scripts, docs and backups; these must be preserved. User reports custom UI is not visible in the prebuilt EXE; expected because selecting a backend source root does not rebuild the bundled frontend. **Live model inventory (PowerShell `ollama list`, user-provided output, 2026-11-07):** `qwen3.8:27b` (17 GB), `qwen3.5:2b` (2.7 GB), `qwen3.5:0.8b` (1.3 GB), `qwen3.5:9b` (6.6 GB), `qwen3.5:4b` (3.3 GB). All four previously inventoried Qwen3.5 models remain present, plus the additional `qwen3.8:27b`; therefore models are not missing from the Ollama list and no download is indicated. User then ran the read-only PowerShell request to `http://127.0.0.1:11434/api/tags`; it returned `OLLAMA API CONNECTED` and all five model names with sizes: `qwen3.8:27b` (17,741,872,154 bytes), `qwen3.5:2b` (2,683,396,812 bytes), `qwen3.5:0.8b` (1,322,069,277 bytes), `qwen3.5:9b` (6,550,825,550 bytes), `qwen3.5:4b` (3,324,176,934 bytes). This verifies the Ollama HTTP API and its model catalogue independently of the desktop GUI. User then queried the OpenJarvis backend: `GET /health` returned `{"status":"ok"}`; `GET /v1/info` returned model `qwen3.5:9b`, agent `simple`, engine `multi`; `GET /v1/models` returned all five installed models (`qwen3.8:27b`, `qwen3.5:2b`, `qwen3.5:0.8b`, `qwen3.5:9b`, `qwen3.5:4b`). This verifies backend health and model-catalogue visibility, not the GUI rendering. User's read-only PowerShell source scan found `frontend/src/lib/api.ts` desktop fallback `http://127.0.0.1:8000`, Tauri-native `get_api_base`/`fetch_models` calls, and Tauri model discovery via `invoke('fetch_models')`; browser API may use `VITE_API_URL`. `vite.config.ts` uses a localhost:8000 proxy fallback; Tauri config uses `frontendDist=../dist`, `devUrl=http://localhost:5173`, `beforeDevCommand=npm run dev`, `beforeBuildCommand=npm run build:tauri`; frontend package scripts use Vite and Tauri. Read-only source inspection initially appeared to show a mismatch: TypeScript calls `tauriInvoke('fetch_models')` without explicit args while Rust requires `api_url: String`. Follow-up output from `tauriInvoke` proves it injects `{ apiUrl, ...args }` automatically, with `apiUrl = getBase()`. Rust `api_base()` returns `http://127.0.0.1:{JARVIS_PORT}`, matching the working port 8000. Therefore the caller/command signature is correctly wired; previous mismatch diagnosis is withdrawn. `fetchModels()` silently falls back to HTTP `/v1/models` if native invoke fails. No native invoke or GUI rendering failure has yet been observed. | The user searched the preserved `frontend/src` and found `fetchModels()` called by `App.tsx`, `SetupScreen.tsx`, `SettingsPage.tsx`, `CommandPalette.tsx`, and `AgentsPage.tsx`. `App.tsx` catches failures and sets an empty array; `SetupScreen.tsx` maps failure to an empty array; `SettingsPage.tsx` maps failure to an empty array and renders `No models loaded`; CommandPalette and AgentsPage also suppress errors. This can hide a fetch failure as an empty model list. No actual Tauri invoke failure was captured. | User checked local build artefacts and source timestamps. `frontend/node_modules` exists (modified 2026-11-01 20:07); `frontend/dist` exists (modified 2026-11-04 20:45); `frontend/src-tauri/target` exists (modified 2026-11-02 16:18); installed desktop EXE exists (modified 2026-11-02 21:43). Latest source file in the reported top 20 was `UpdateChecker.tsx` (`2026-11-02 05:55:12`); latest generated `dist` assets were `2026-11-04 20:45:22`. `dist` is newer than the EXE, but the checked source timestamps are earlier than the EXE, so timestamps alone do not prove which customised UI revision is embedded in the installed EXE. | User inspected `frontend/dist`: production JS chunks include `index-DnLZZ_Ji.js` (1,253,910 bytes), `charts-BLQhYFDz.js` (388,815 bytes), plus smaller chunks, timestamped 2026-11-04 20:45. Simple text-marker scan found `Historical Analytics` and `Cost Comparison`; did not find `Energy Dashboard`, `TraceDebugger`, `SavingsDashboard`, or `DashboardKpiBar`. Absence of those literal markers is inconclusive for minified production output. Existing Tauri outputs include `target\release\openjarvis-desktop.exe` and `target\release\bundle\msi\OpenJarvis_1.0.2_x64_en-US.msi`. User then calculated file metadata and SHA-256: installed EXE is version 1.0.2, 21,817,856 bytes, modified 2026-11-02 21:43:32, hash `0A2ACBFEC1C07D94DAEC88EF4959FB8B3B770489618AC8A331FE3295742FECF4`; target/release EXE is version 1.0.2, same size, modified 2026-11-04 20:46:46, hash `1348CC3AFE2ABFD08005850F30E7DD06AF5A2EB15E5B518F51D8163C7FF49624`; MSI is 20,345,475 bytes, modified 2026-11-04 20:46:37, hash `474AAC2BC6D3C7C5AFAF69DCD6B35E61632DDF98E66ECC07BDF06AFBD7BD6047`. Installed and release EXEs are conclusively different binaries despite sharing version and size. The newer release EXE is a plausible custom-UI candidate but has not been launched/visually verified. | User's local `frontend/src-tauri/src/lib.rs` output confirms `JARVIS_PORT=8000`. `boot_backend` probes `http://127.0.0.1:8000/health`; on 2xx it waits 500 ms and probes again, then attaches to the existing healthy API server and marks setup ready. A non-2xx response is reported as a port conflict without killing the foreign service; connection refusal proceeds to a port-availability check before spawning a new backend. The `taskkill` match is only a source comment describing old behavior, not an active command in the displayed context. No `single_instance` plugin match appeared in the local `lib.rs` search, so the newer EXE may permit a second UI process; not yet proven absent from other modules. | User checked processes and port immediately before testing the candidate build. No process matched `*openjarvis*` or `jarvis serve`; no TCP listener existed on port 8000. The previous API backend is no longer running. Port 8000 is free, so the newer local release can be tested without colliding with a currently listening backend. | User launched `frontend\src-tauri\target\release\openjarvis-desktop.exe` using process-scoped `OPENJARVIS_ROOT=C:\Users\Boxont\OpenJarvis`. Candidate EXE opens successfully, but user reports customised UI and models remain absent. Thus candidate is not a recovery yet. Program Files EXE and MSI remain untouched. | While candidate app PID 3268 was open, user found `uv.exe` PID 11404 and port 8000 listener PID 14220; `/health` returned `ok`, `/v1/info` returned model `qwen3.5:9b`, agent `simple`, engine `multi`, and `/v1/models` returned the installed catalogue. This confirms backend/server-side model discovery is healthy while the desktop UI still shows neither custom screens nor models. User's latest uploaded output confirms `getBase()` returns `localStorage['openjarvis-settings'].apiUrl` first when set, before Tauri `get_api_base` and fallback `http://127.0.0.1:8000`; actual saved value was not printed. `main.tsx` calls `initApiBase()` and waits for it before React render. Vite config enables `VitePWA` with `registerType: 'autoUpdate'` and Workbox precache of JS/CSS/HTML/assets; possible stale WebView cache is not proven. `App.tsx` imports `DashboardPage`, Chat, Settings, Agents and other standard pages, but composition of customised dashboard components remains to inspect. PID 14220 lookup returned no process details in this later output, so do not rely on that old PID; current port owner is unknown. | Inspect `DashboardPage` imports/rendered children; safely retrieve only saved `apiUrl` from WebView storage or Settings (never API key); query current port listener with dynamic PID lookup. No source changes, rebuild, install or overwrite.
| 2026-11-05 | Specify mandatory full Windows computer-control module | DOCUMENTED — implementation NOT STARTED | Expanded Phase 6 and added docs/WINDOWS_COMPUTER_CONTROL.md with UIA/pywinauto/FlaUI evaluation, input, capture/OCR/local vision, authenticated OpenJarvis MCP/native-tool boundary, verified action loop, application matrix and security tests T20/T21. Phase 6 remains NOT STARTED; no bridge code or live UI interaction has been implemented or run. | Inspect installed OpenJarvis 1.0.2 tool/MCP interfaces and preserved Windows source checkout; then implement the smallest adapter set that passes the real app matrix. |
| 2026-11-05 | Align JARVIS with absolute zero-cost constitution | PARTIAL — policy documented; runtime audit pending | Full rule added to MASTER_TODO.md and mirrored in AGENTS.md, fallback bootstrap, Claude, Gemini, Copilot, OpenCode and controller docs; remote read-back verified. Dependency-wide cost audit not yet performed. | Audit every dependency and payment/fallback path; verify local storage and zero-cost operation. |
| 2026-11-04 | Build Windows JARVIS Project Controller | PARTIAL | Added session launcher, one-time installer, generated system prompt, and safe task-status updater; runtime scripts and docs committed and read back from private GitHub. No Windows execution or installed-app prompt test has been run. | Clone the private repo on the PC, run the installer, then verify a new OpenJarvis chat loads the current master and can update/read it back. |
| 2026-11-04 | Create private JARVIS planning repository and master roadmap | VERIFIED | `eboxont-code/jarvis-os` created as private; `MASTER_TODO.md` committed and read back | Configure automatic AI session instructions |
| 2026-11-04 | Add cross-agent startup and checklist-update rules | VERIFIED (repository files) | `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `opencode.json`, `JARVIS_BOOT.md` created; master status protocol added and remote read-back verified | Implement bootstrap inside the OpenJarvis runtime |

