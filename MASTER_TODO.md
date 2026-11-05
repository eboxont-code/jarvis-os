# PROJECT JARVIS — MASTER PLAN & TODO

**Project:** JARVIS — Ultimate Personal AI Operating System  
**Repository:** eboxont-code/jarvis-os (private)  
**Foundation:** Existing OpenJarvis installation  
**Primary platform:** Windows 11 (Windows 10 where practical)  
**Mobile priority:** Android first; iOS later  
**Budget:** $0 additional expenditure — non-negotiable  
**Master status:** IN PROGRESS  
**Current milestone:** Prove local inference, preserve the existing installation, and establish a safe extension architecture.

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

## 1. Vision and operating cycle

JARVIS is intended to become a universal personal AI operating system and digital assistant. It should combine the practical capabilities of conversational AI, complex reasoning, live research, specialist agents, software engineering, browser and Windows computer use, system administration, persistent memory, productivity, data analysis, creative work, integrations, automation and measured self-improvement.

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

## PHASE 6 — Real Windows computer control
**Status: NOT STARTED — CORE REQUIREMENT**

Filesystem, shell and browser-only access do not equal full desktop control.

### Windows automation bridge
- [ ] Evaluate Windows UI Automation.
- [ ] Evaluate pywinauto.
- [ ] Evaluate FlaUI or equivalent free tooling.
- [ ] Implement window enumeration and active-app detection.
- [ ] Implement application launching.
- [ ] Implement clipboard access.
- [ ] Implement mouse and keyboard operations.
- [ ] Implement window switching and management.

### Visual interaction
- [ ] Capture full and regional screenshots.
- [ ] Identify visible controls and interface state.
- [ ] Implement OCR where appropriate.
- [ ] Integrate local vision models where hardware allows.
- [ ] Interpret dialogs, menus and prompts.
- [ ] Click actual UI elements.
- [ ] Enter text and verify it.
- [ ] Navigate menus and scroll.
- [ ] Handle unexpected UI states.
- [ ] Record before/after evidence.

### Browser automation
- [ ] Integrate Playwright.
- [ ] Navigate and inspect pages.
- [ ] Interact with forms and controls.
- [ ] Handle downloads safely.
- [ ] Verify browser task outcomes.
- [ ] Keep browser permissions separate from desktop permissions.

### End-to-end desktop verification
- [ ] Demonstrate File Explorer interaction.
- [ ] Demonstrate Notepad interaction.
- [ ] Demonstrate Windows Settings interaction.
- [ ] Demonstrate a supported browser interaction.
- [ ] Demonstrate a developer application interaction.
- [ ] Record target, initial state, tool, intended action, actual action, resulting state and evidence.
- [ ] Verify recovery from an unexpected application state.

**Acceptance:** Real Windows files, browser pages and desktop applications are operated and the resulting state is independently verified. No simulated actions.

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
- [ ] Prefer free tools and zero-additional-cost operating models. Never use a low-cost, paid or subscription-based option as a substitute.

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

## 4. Central JARVIS interface

**Status: NOT STARTED**

Required areas:
- [ ] Main chat.
- [ ] Voice interaction.
- [ ] Research workspace.
- [ ] Project manager.
- [ ] Task manager.
- [ ] Agent workforce.
- [ ] Computer operations.
- [ ] Files and documents.
- [ ] Integrations.
- [ ] Memory.
- [ ] Monitoring.
- [ ] Automation.
- [ ] System health.
- [ ] Permissions.
- [ ] Activity and audit history.

The interface must display actual task state, assigned agent, tools used, commands executed, files modified, research sources, progress, approvals, errors, verification status and deliverables. Do not simulate progress or display capabilities as active when they are unavailable.

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

### Milestone A — Prove local AI foundation (CURRENT)
- [ ] Run JARVIS_Phase2_Local_Inference_v1.zip.
- [ ] Verify direct Ollama response.
- [ ] Verify OpenJarvis uses the local model through its actual runtime.
- [ ] Record model identifier, latency, resource use and errors.
- [ ] Select first known-good configuration.

### Milestone B — Stabilise development foundation
- [ ] Verify main repository backup contents.
- [ ] Review the .pytest_cache access-denied entries.
- [ ] Verify .openjarvis user-data copy.
- [ ] Test restoration into a separate location.
- [ ] Preserve dirty Git working tree and customisations.
- [ ] Establish safe checkpoint and rollback method.
- [ ] Identify exact installed desktop app and backend runtime.
- [ ] Establish isolated JARVIS extension workspace.

### Milestone C — First useful JARVIS build
- [ ] **PARTIAL** — Implement OpenJarvis session bootstrap and automatic master TODO read/update/synchronisation — done: controller package committed; remaining: install and verify on Windows (see Phase 5 Continuity).
- [ ] Stable local chat workflow.
- [ ] Persistent project memory.
- [ ] Small set of useful permission-controlled tools.
- [ ] Task tracking and execution logs.
- [ ] Repeatable test and verification loop.

### Milestone D — Give JARVIS hands
- [ ] Real filesystem operations.
- [ ] Bounded PowerShell operations.
- [ ] Browser automation.
- [ ] Visual screen inspection.
- [ ] Windows desktop interaction.
- [ ] Real application tests and verification.

### Milestone E — Expand intelligence and autonomy
- [ ] Model routing.
- [ ] Live research and source verification.
- [ ] Specialist agents.
- [ ] Autonomous coding workflow.
- [ ] Automation and monitoring.
- [ ] Controlled, benchmarked improvement.

### Milestone F — Complete the personal AI operating system
- [ ] Productivity and business integrations.
- [ ] Creative and multimodal capabilities.
- [ ] Unified interface.
- [ ] Android companion.
- [ ] iOS feasibility within zero-cost constraints.
- [ ] End-to-end acceptance suite.
- [ ] Final documentation and limitations.

---

## 11. Live status — last verified evidence

**Last recorded evidence date:** 4 November 2026.

| Milestone | Status |
|---|---|
| Master specification | Defined |
| Initial Windows/hardware audit | VERIFIED |
| Ollama and four Qwen models inventoried | VERIFIED (inventory only) |
| OpenJarvis repository identified | VERIFIED |
| Existing custom/dirty working tree identified | VERIFIED |
| Initial repository backup | PARTIAL — files copied; directory access errors remain |
| .openjarvis copy | COPY COMPLETED; restore not yet tested |
| Git checkpoint | NOT STARTED |
| Local inference test package | PREPARED; not yet executed |
| Direct local inference | NOT VERIFIED |
| OpenJarvis-to-local-model integration | NOT VERIFIED |
| Model router | NOT STARTED |
| Research engine | NOT STARTED |
| Multi-agent workforce | NOT STARTED |
| Persistent memory | NOT STARTED |
| Windows desktop control | NOT STARTED |
| Secure administration | NOT STARTED |
| Autonomous coding | NOT STARTED |
| Productivity integrations | NOT STARTED |
| Creative studio | NOT STARTED |
| Automation and monitoring | NOT STARTED |
| Measured self-improvement | NOT STARTED |
| Final hardening | NOT STARTED |
| Repository agent instruction files | VERIFIED — created and read back from private GitHub |
| OpenJarvis runtime auto-bootstrap and automatic master-file writer | PARTIAL — controller files committed; Windows runtime test pending |

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
|---|---|---|---|---|
| 2026-11-04 | Build Windows JARVIS Project Controller | PARTIAL | Added session launcher, one-time installer, generated system prompt, and safe task-status updater; runtime scripts and docs committed and read back from private GitHub. No Windows execution or installed-app prompt test has been run. | Clone the private repo on the PC, run the installer, then verify a new OpenJarvis chat loads the current master and can update/read it back. |
| 2026-11-04 | Create private JARVIS planning repository and master roadmap | VERIFIED | `eboxont-code/jarvis-os` created as private; `MASTER_TODO.md` committed and read back | Configure automatic AI session instructions |
| 2026-11-04 | Add cross-agent startup and checklist-update rules | VERIFIED (repository files) | `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `opencode.json`, `JARVIS_BOOT.md` created; master status protocol added and remote read-back verified | Implement bootstrap inside the OpenJarvis runtime |

