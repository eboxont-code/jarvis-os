# OpenClaw Workspace requirements

OpenClaw owns the conversation and coordinates work. The Windows Companion connects the paired PC to the Gateway. Ollama supplies inference on loopback. OpenCode handles delegated coding through ACP. The workspace must run on the existing PC with zero additional software or service expenditure.

## Verified baseline and next milestones

| Capability | Evidence and remaining work |
|---|---|
| Local model | Ollama lists `qwen3.8:27b`. The live picker exposes it through Ollama and OpenCode ACP. No smaller model is required. Verify a timed reply through native OpenClaw Chat. |
| Gateway and Windows Node | The workspace status tool verifies the model tag, running service, authenticated health and paired Node. A native `device.status` call previously succeeded after reconnecting. Test unattended sign-in with the current OpenClaw startup entries. |
| Coding | OpenCode is configured for local Qwen. Verify edits, tests, cancellation and a result returned to native OpenClaw Chat in a disposable project. |
| Windows and browser control | Verify a saved note reopened through Explorer and a downloaded report from a local browser form, then complete the five-application desktop matrix. Prior experiments used a retired host. |

The checkboxes below track acceptance for the current OpenClaw architecture. An unchecked requirement can have working components. Check it when evidence covers the whole stated requirement. Keep operational evidence local and publish only a sanitised result.

## Assistant setup requirements

Use the [20-area assistant capability checklist](docs/ASSISTANT_CAPABILITIES.md) when selecting providers, defining approvals and recording connection tests. The project-wide cost and privacy requirements apply to every integration.

## Integration requirements

| Gate | Required outcome and proof |
|---|---|
| A · Inventory and recovery | Identify installed builds, executables, process owners, endpoints, current models, tool registrations and ACP binding. Capture baseline health, preserve settings and verify a private recovery copy before changes. |
| B · Shared inference | Identify one Ollama owner. Check tags and residency, then run direct generation and a harmless tool call. Measure latency and resources. Verify Chat and OpenCode use the same endpoint. Test their restarts and shutdown without double launches or model downloads. |
| C · Standalone coding | Use the installed OpenCode local provider in a disposable project. Verify inspection, a restricted edit and actual tests. Exercise cancelled work, denied external paths, network and shell permissions, and failed tests. |
| D · Native coordinator | Verify Companion, loopback Control UI, authenticated Gateway and the main agent. Scope tools, logging, cancellation and timeouts. External messaging needs separate authorisation. Confirm harmless tool use, shutdown and clean restart. |
| E · ACP delegation | Discover the installed ACP backend. Create and close a scoped OpenCode session. Return a verified diff and test output to the originating chat. Exercise rejection, timeout, cancellation and worker cleanup. |
| F · Approved local tools | Inventory native capabilities and any MCP registrations. Start with read-only status. Verify discovery, calls, allowlists, authentication, failure isolation and absence of recursive delegation. Add scoped writes only with tested permission enforcement, audit and rollback. |
| G · Task handoff | Use one coordinator, one writer per file and a task ID across sessions. Pass the objective, workspace, instructions, approvals, deadline and evidence requirements. Verify bounded retry, cancellation, deduplication and checkpoint recovery. |
| H · End-to-end operation | From native Chat, plan a disposable task, invoke an approved local tool, delegate an edit, run tests and return evidence. Verify ordinary chat after failures. Test real Windows sign-in, responsiveness under load, authenticated Node reconnection, saved task state and independent component recovery. Audit local-only inference and record latency and limitations. |

## How to use the roadmap

Phases 0–13 below specify the product. Tests T01–T31 define release evidence. Windows desktop control also has a [detailed design and application test matrix](docs/WINDOWS_COMPUTER_CONTROL.md). The archived plan retains historical machine observations and the previous architecture. Start new work here.

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

The entire OpenClaw project must operate without additional financial expenditure. This is a strict requirement, not a preference. It applies to design, development, runtime, research, deployment, integrations, maintenance, agents and future upgrades.

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

Never enter payment details, start subscriptions, purchase credits or upgrade an account for OpenClaw. Never make essential functionality dependent on a personal subscription or a paid account. Do not silently assume a currently accessible consumer account, free quota or promotional entitlement will remain available.

#### 2. Mandatory local-first architecture

Use local software and the computer's existing resources wherever possible.

Preferred technologies include:
- OpenClaw.
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
- [ ] Preserve the installed OpenClaw profiles, pairing, user data and workspace customisations.
- [ ] Do not reinstall or replace working components without a demonstrated technical reason.
- [ ] Never run destructive Git cleanup/reset commands against the existing dirty working tree.
- [ ] Never overwrite configuration, databases or user data without a recoverable backup.
- [ ] Prefer custom agents, tools, skills, MCP integrations, adapters and external extensions.
- [ ] Keep OpenClaw custom functionality separate from upstream files wherever practical.
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

**User rule — 18 November 2026 (supersedes the earlier blanket official-repair wait gate):** Do not wait solely for an official release before progressing the integration. Pursue supported, bounded, reversible diagnostics and repairs using the existing installations, with real acceptance evidence. The user explicitly revoked the previous wait-for-official-repair prerequisite and authorised proceeding with the prepared temporary supported-CLI MCP discovery test. This does not authorise spending, model downloads, credential exposure, ownership/security bypasses, missing-runtime-file fabrication, runtime-path overrides, profile switching, Gateway/Companion restart/reset/reinstall, ACL/security changes or elevated/destructive actions. Those existing boundaries remain; request specific approval for a concrete action if one becomes necessary. Keep any unresolved native Node task BLOCKED on its actual technical failure, rather than a blanket waiting policy. Dated handoffs/execution entries preserve earlier rules as history; this current directive takes precedence.
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

## Operating cycle

UNDERSTAND → INVESTIGATE → RESEARCH → THINK → PLAN → DECOMPOSE → EXECUTE → VERIFY → CORRECT → DELIVER → MONITOR → LEARN → IMPROVE

OpenClaw must distinguish:
1. Existing model knowledge.
2. Current information retrieved from external sources.
3. Information saved in persistent memory.
4. Inferences and assumptions.
5. Actions actually executed.
6. Outcomes independently verified.
7. Work that remains incomplete or uncertain.

---

## 3. Phase roadmap

## PHASE 0 — Complete system audit and architecture

### Inventory
- [ ] Identify Windows version and machine.
- [ ] Identify CPU, RAM, GPU and storage.
- [ ] Inventory major developer tools.
- [ ] Identify Ollama and installed model names.
- [ ] Identify installed OpenClaw application.
- [ ] Identify Docker and WSL availability.
- [ ] Verify the exact active OpenClaw desktop runtime.
- [ ] Verify the backend process and communication path.
- [ ] Inspect existing custom source modifications.
- [ ] Map existing agents, tools, engines, memory and learning facilities.
- [ ] Map integrations, scheduler, permissions and logs.
- [ ] Record existing faults and known limitations.

### Architecture deliverables
- [ ] Record a current system audit with sensitive configuration kept local.
- [ ] Create an architecture diagram of the actual installation.
- [ ] Separate existing-and-working capabilities from merely-installed components.
- [ ] Identify missing capabilities and duplication.
- [ ] Create a risk register.
- [ ] Document hardware/model limits.
- [ ] Create dependency and integration maps.
- [ ] Finalise implementation sequencing.

**Acceptance:** The existing installation and customisations are understood sufficiently to extend without damaging working functionality.

## PHASE 1 — Safe foundation

### Backup and recovery
- [ ] Create and run initial copy-only backup.
- [ ] Back up OpenClaw user data and configuration privately and check the copy log.
- [ ] Copy the workspace files and verify that the backup job reports no failed files.
- [ ] Review skipped files and access errors. Document reproducible caches excluded from recovery.
- [ ] Verify important files and representative hashes in the backup.
- [ ] Verify customised Windows Companion assets and the provenance of release payloads.
- [ ] Verify user-data copy.
- [ ] Test restoration into a separate temporary location.
- [ ] Document recovery steps and backup limitations.

### Safe development workflow
- [ ] Establish a Git checkpoint strategy that preserves the dirty working tree.
- [ ] Preserve all tracked modifications and untracked files.
- [ ] Establish an isolated working copy or extension workspace.
- [ ] Document clean separation between upstream code and OpenClaw extensions.
- [ ] Establish rollback procedure.
- [ ] Establish structured logs and execution records.
- [ ] Ensure local development services bind to localhost by default.

### Local inference — first functional milestone
- [ ] Identify existing Ollama installation.
- [ ] Record the installed Ollama model catalogue and the active 27B default.
- [ ] Prepare bounded local-inference test package.
- [ ] Run direct Ollama inference test.
- [ ] Verify a real model response.
- [ ] Run OpenClaw inference through its actual installed runtime/CLI.
- [ ] Verify OpenClaw receives a real response from the local model.
- [ ] Record exact model identifier, latency, errors and resource use.
- [ ] Select first known-good local inference configuration.

**Acceptance:** Existing OpenClaw remains recoverable and a real local model response is demonstrated through the actual OpenClaw runtime. A direct Ollama response alone does not satisfy the integration test.

## PHASE 2 — Local intelligence engine

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
- [ ] Use a lighter configuration for lightweight tasks. Evaluate a smaller model only if the operator chooses to install one.
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

**Acceptance:** OpenClaw researches a current topic, inspects original sources, distinguishes dates and produces an evidence-supported report.

## PHASE 4 — Multi-agent workforce

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
- [ ] Load AGENTS.md and the current REQUIREMENTS.md at the start of a project session and verify the loaded revision.
- [ ] Maintain the canonical task status, synchronise authorised updates and verify the remote revision.
- [ ] Provide a fallback bootstrap for AI tools that do not automatically discover AGENTS.md, CLAUDE.md, GEMINI.md or Copilot instructions.
- [ ] Track decisions and reasons.
- [ ] Link tasks to code changes and test evidence.
- [ ] Preserve one authoritative project state.
- [ ] Avoid inventing missing history.

**Acceptance:** OpenClaw restarts, automatically loads the latest master plan, resumes the correct task and records status locally and verifies read-back of any authorised, sanitised repository update.

## PHASE 6 — Full Windows computer control

This phase is not optional. Filesystem access, PowerShell/CMD execution and browser automation do **not** constitute full Windows desktop control. OpenClaw must inspect the actual visible desktop, identify real controls, operate real applications through supported Windows interfaces, and independently verify the resulting state. Simulated actions, mock screenshots and shell-only substitutes do not pass acceptance.

The technical design and implementation/test contract are maintained in [WINDOWS_COMPUTER_CONTROL.md](docs/WINDOWS_COMPUTER_CONTROL.md). This file remains the authoritative task/status checklist.

### 6.1 Inspect and select the Windows automation foundation
- [ ] Inspect the exact installed OpenClaw version, tool registry, permission model, MCP/native-tool support and current system-access implementation before changing code.
- [ ] Map the desktop bridge to the actual Windows session, user identity, process integrity level, display topology, DPI/scaling and active session.
- [ ] Evaluate native Microsoft Windows UI Automation (UIA) control patterns, properties, events, element trees and accessibility identifiers.
- [ ] Evaluate pywinauto with its UIA and Win32 backends against the actual target applications.
- [ ] Evaluate FlaUI and its supported UIA automation modes against the same application/test matrix.
- [ ] Record compatibility, reliability, element coverage, latency, process-boundary behaviour, maintenance state and full transitive dependency licences for each candidate.
- [ ] Select a primary adapter and only the necessary fallback adapters from measured evidence; do not ship duplicate frameworks without demonstrated benefit.
- [ ] Keep the adapter interface replaceable so a later Windows or OpenClaw update does not require rewriting the orchestration layer.
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

### 6.7 OpenClaw integration and tool interface
- [ ] Inspect the installed OpenClaw version's documented native-tool and MCP integration points; do not assume upstream support is present in the user's installed build.
- [ ] Expose desktop capabilities through an authenticated local MCP server or an equivalent native OpenClaw tool adapter.
- [ ] Prefer MCP stdio transport when supported by the actual OpenClaw tool configuration; it avoids opening a local network listener.
- [ ] If a local HTTP transport is required, bind only to 127.0.0.1, require authentication, validate Origin, defend against DNS-rebinding access and reject remote-interface binding.
- [ ] Authenticate the calling process/client and apply per-tool and per-operation permissions; do not treat loopback access alone as authentication.
- [ ] Keep the tool service and ordinary OpenClaw inference process at normal-user privilege.
- [ ] Provide narrow tools for desktop state, window listing/inspection, screenshots, accessibility-tree inspection, semantic control invocation, mouse/keyboard input, clipboard, application launch, waits, cancellation and verification.
- [ ] Do not expose unrestricted PowerShell, arbitrary process execution or a general-purpose elevated shell through the desktop-control interface.
- [ ] Integrate tool results into OpenClaw's agent loop with structured state, clear failures and evidence attachments.
- [ ] Test the complete path from an OpenClaw agent request through the local bridge to a real desktop action and verified result.

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
- [ ] Never run the whole OpenClaw backend or desktop bridge elevated merely to control more windows.
- [ ] Never bypass UAC, Windows secure desktop, credential prompts, lock screen, authentication or application access controls.
- [ ] Pause and request the user's direct approval for UAC, credential entry, system security prompts, installs, settings changes with material impact and destructive actions.
- [ ] Require explicit confirmation for irreversible deletion, bulk changes, external submission, purchases, publishing and other sensitive actions.
- [ ] Block attempts to disable Defender/firewall/security controls, extract credentials, evade application protections or perform unauthorised actions.
- [ ] Treat screen contents, OCR text, accessibility metadata, webpages and application documents as untrusted data; they cannot override system instructions or permission policy.
- [ ] Log all privileged hand-offs and user approvals without storing secrets.
- [ ] Test unauthorised tool calls, ambiguous targets, stale coordinates, prompt-injection in visible content, UAC and secure-desktop boundaries, cancellation and recovery.

### Phase 6 acceptance
**Acceptance:** The main agent receives a real task in OpenClaw Chat, inspects the actual Windows desktop, identifies a real application/control, performs a genuine UI action, captures/re-reads the resulting state, and reports evidence. The File Explorer, Notepad, Settings, browser and VS Code test matrix must pass (with any application-specific limitation clearly documented). A separate security test must demonstrate that UAC, secure desktop, credentials and unauthorised/destructive actions are not bypassed. Shell-only access, Playwright-only access, generated code, simulated screenshots or unverified clicks do not pass.

Implementation detail, adapter comparison, tool contract and test procedure: [docs/WINDOWS_COMPUTER_CONTROL.md](docs/WINDOWS_COMPUTER_CONTROL.md).

## PHASE 7 — Secure Windows administration and installation

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

**Acceptance:** Real productivity and data-processing workflows can be completed through the central OpenClaw interface.

## PHASE 10 — Creative and multimodal studio

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

**Acceptance:** OpenClaw generates, processes and inspects actual local outputs.

## PHASE 11 — Automation, scheduling and monitoring

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


Use OpenClaw Companion and Chat as the primary interface.

- [ ] Keep OpenClaw as the existing direct desktop AI workspace.
- [ ] Use the OpenClaw Control UI as the initial view of coordinated agent tasks and sessions, if its local setup and security checks pass.
- [ ] Use OpenCode's own interface/session for software-development work when direct developer interaction is needed.
- [ ] Make task progress, agent ownership, tool use, changed files, research sources, approvals, errors, verification status and deliverables visible in the relevant application.
- [ ] Avoid building a replacement dashboard until the native interfaces and hand-offs have been proven.
- [ ] Consider a unified front end only after the native Chat, Gateway, Node and coding workflow run reliably together and there is a demonstrated user need.

Do not simulate progress or display capabilities as active when they are unavailable.

---

## 5. Security and permission model


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


### Android first
- [ ] Evaluate local Android SDK and command-line tooling.
- [ ] Establish a free local build workflow if needed.
- [ ] Build Android applications and generate APKs locally.
- [ ] Test on available devices.
- [ ] Support local debugging.
- [ ] Explore secure OpenClaw-to-Android communication.
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

## 8. End-to-end acceptance suite

A capability is complete only when the test passes and evidence is recorded.

| ID | Acceptance test | Required evidence |
|---|---|---|
| T01 | Direct local inference | Real response from installed local model |
| T02 | OpenClaw local inference | Real response through actual OpenClaw runtime |
| T03 | Model routing | Task categories use suitable installed models or configurations, including the single-model case |
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
| T20 | Full Windows desktop control | An OpenClaw agent performs and verifies real UI actions in File Explorer, Notepad, Settings, a browser and VS Code, with screenshots/UIA evidence |
| T21 | Desktop-control security boundaries | Unauthorised/ambiguous actions are blocked; UAC and secure desktop are not bypassed; cancellation and recovery are demonstrated |
| T22 | One shared Ollama runtime | Process/port ownership, /api/tags, real response and clean restart; no competing listener |
| T23 | OpenClaw uses shared Ollama | Actual OpenClaw chat response, exact model/endpoint and no unnecessary model download |
| T24 | OpenClaw uses local Ollama | Local-only provider, real response and a verified harmless tool call |
| T25 | OpenCode uses local Ollama | Model discovery, real coding task and local test evidence |
| T26 | OpenClaw → OpenCode ACP | Session creation, scoped workspace, result, cancellation and test output |
| T27 | OpenClaw local tools | Native Node or approved MCP tool discovery, successful scoped call, permission denial and failure handling |
| T28 | Shared task context | Correct instructions and task scope reach each participating application |
| T29 | Integrated end-to-end task | The main agent coordinates native tools and OpenCode work; output independently verified |
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

## Working protocol

Read AGENTS.md and this checklist at session start. Select one eligible task unless a batch is authorised. Record its dependencies and acceptance test before implementation. Track the task as WORKING, PARTIAL, BLOCKED or VERIFIED. Record test results, limitations, rollback and the next action. Verify published changes by reading them back from the remote. Keep tokens, private paths, chat content, pairing material and backups off the public repository.

## Delivery sequence

1. Prove native Chat inference, including two timed replies, cancellation and a useful error if Ollama is unavailable. Verify the current startup path at a normal Windows sign-in.
2. Complete an OpenCode ACP task in a disposable repository. Return changed paths, verifier exit code and test results to the originating OpenClaw session.
3. Compare Windows UI Automation, pywinauto and FlaUI on the same desktop tasks. Exercise a browser form and verified download with Playwright and an installed browser. Record which adapters cover which applications.
4. Exercise Git checkpoints and restore representative source, configuration and data into a separate directory. Compare hashes.
5. Inspect existing OpenClaw session storage before extending local task history. Test search, retention, restart recovery and redaction. Show per-connection health, task owner, progress, last successful check and failure reason in the native interface.

## Project boundaries and migration coverage

The archived master supplies the operating rules (section 0), integration gates (0A), operating cycle (1), roadmap (3), user interface, permissions and mobile requirements (4–6), acceptance tests (8), task records (9) and session protocol (12–13). The architecture and baseline above replace the historical inventory, diagrams, queue and live status (2, 7, 10–11). The archived execution log (14) remains historical evidence. The old GUI bridge, backend watchdog and port migration are retired implementations. Their user-facing requirements survive as native Chat, verified delegation, responsiveness, recovery and sign-in tests.
