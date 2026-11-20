# Assistant capabilities and acceptance checks

These 20 requirements extend the [OpenClaw roadmap](../REQUIREMENTS.md). OpenClaw coordinates the work from the local PC. Named providers are candidates. Before adopting one, verify its supported interface, account permissions and ongoing zero-cost operation. Each row describes a setup prerequisite and a practical test using sample data.

Apply the [dependency review](DEPENDENCY_REVIEW.md) before selecting any provider. The local implementation must remain free to operate. Hosted brand names below identify optional interoperability targets. Enable an operation only after verifying its free entitlement and maintained interface.

Nothing below is installed, enabled, connected, or tested. Complete the [fresh-install guide](../README.md) first. The plugin ids there are the ones to enable and the ones to leave disabled.

## Setup still to do

- [ ] Email — enable `imap`. Connect each selected mailbox privately. Test read, draft, monitoring and send permissions separately.
- [ ] Calendar and contacts — connect a local Nextcloud CalDAV calendar. Generate a sample ICS event and vCard, then test sync and invitation approval.
- [ ] App building — install OpenCode via acpx. Test an end-to-end build against a selected local project.
- [ ] Code and repositories — install Git. Enable `github`. Connect the intended identity and verify a scoped OpenClaw coding task.
- [ ] Hosting — serve a disposable loopback site with a free local server such as Caddy, then select a target before any real deployment and rollback test.
- [ ] Databases — install a local SQLite tool and run a sample query. Connect a project database with read-only access before any write.
- [ ] Domains and WordPress — install local WordPress Playground when a site test is needed. DNS, renewal and migration checks wait for an authorised site.
- [ ] Error tracking — start with local Windows application logs. Connect a zero-cost tracker only after a sample trace, release and alert are defined.
- [ ] Spreadsheets and documents — install LibreOffice. Create and reopen sample XLSX, DOCX, PPTX and PDF files from OpenClaw Chat.
- [ ] Design and media — install FFmpeg, Krita and Kdenlive when those jobs are needed, and install ComfyUI with SDXL base 1.0. This PC has a 12 GB RTX 4070. Flux needs a quantised version.
- [ ] Social — enable `duckduckgo` and install SearXNG for public research. Connect an account only for a later private operation, and only on a free route.
- [ ] Vault — install KeePassXC and enable `vault`. Set up a private vault and test autofill with a dummy credential.
- [ ] Computer and browser — enable `browser` and `device-pair`. Install `@playwright/mcp`. Pair the Windows node.
- [ ] Research — enable `duckduckgo` and `web-readability`. Install SearXNG. Run one search from OpenClaw after those steps.
- [ ] Calls and messaging — connect one delivery channel, or set `commands.ownerAllowFrom`, so heartbeat and cron can deliver.
- [ ] Meetings — choose a meeting service and connect an invited test call before any notes.
- [ ] Automation — after a delivery route exists, create one disposable routine and test firing, pause, resume and missed-run recovery.
- [ ] Memory and skills — enable `memory-core` and `memory-wiki`. Test recall and rule revocation across two new chat sessions.
- [ ] Multiple agents — enable `workboard` for the main assistant. Add a specialist only when a job needs a separate owner.
- [ ] Phone — install KDE Connect. Pair a device and test each permission. Desktop pairing does not register an OpenClaw phone node.

## Capability checklist

| # | Capability | Setup and acceptance check |
|---|---|---|
| 1 | Email | Connect each selected inbox separately (for example Gmail, Outlook, iCloud or Hostinger). Search and summarise a thread with a PDF invoice, save a reply in the correct mailbox, and test labels, sorting, archive, trash and spam cleanup on sample mail. Monitor bills, verification notices, job replies and selected senders. Keep codes out of summaries. Apply the send and deletion rules below. |
| 2 | Calendar and contacts | Connect an authorised calendar and address book, with local Nextcloud CalDAV as the local option. Resolve a test contact, find a free slot, then create, move and cancel a test event. Verify booking-link management if a free booking service is connected. Ask before changes that affect other people. |
| 3 | App builders | Select the local OpenCode project. Compare project history and revision with the linked repository, detect an active build and wait for it before submitting a prompt. Verify the result in the same project. Automatic approvals cover build plans only. Secret access, payment and publishing fall outside that permission. |
| 4 | Code and repositories | Connect GitHub or another free provider to selected repositories. Read commits, branches, PRs, issues and CI. Test lint, build and tests before pushing a fix, merging a clean PR or closing a superseded PR with a note. Honour main-branch protection. Prohibit force pushes, resets and history rewrites. Use local OpenCode for large jobs. A separately authorised remote worker requires a zero-cost environment and a scoped handoff. |
| 5 | Hosting and deployment | Prefer a site served on this PC. A hosted target such as a free Vercel, Railway, Render or Firebase project is optional and stays outside the critical path. Trace a deployment from commit to build logs, runtime errors and live revision. Test the approval flow for environment variables, domain changes, redeploy and rollback. Redact values from evidence. |
| 6 | Databases | With a read-only role, list projects and tables, identify the database used by a running site, run a sample SELECT and review security and performance advisories. Require explicit approval for migrations, schema changes and destructive SQL. Verify against disposable data. |
| 7 | Domains, DNS and web hosting | Connect a registrar or hosting panel for a zero-cost test. Inspect mail, verification and site records, renewals, expiry, billing, SSL, site health, speed and errors. Test a domain connection, WordPress update and host migration on a test site. Confirm DNS and production changes before applying them. |
| 8 | Error tracking | Connect a zero-cost error tracker such as a self-hosted instance. Trigger a sample crash, locate its stack trace, identify the release and verify delivery of a test alert. |
| 9 | Spreadsheets, documents and files | Produce an editable spreadsheet with formulas and charts, a tracker, document, PDF and slide deck. Extract sample data from a PDF, table and image. Reopen and update a saved report or dashboard from a persistent local library. Test optional Sheets, Docs, Drive, OneDrive or Dropbox access, approved sharing and email delivery separately. |
| 10 | Design and media | Install local image generation and editing, then produce a short video with edited footage, narration, captions and music. Test an optional design-tool import or export where free access allows it. Use free assets and locally generated graphics. Purchased design credits conflict with the project budget. |
| 11 | Social media | Search public posts, profiles, trends and news where public access permits. Separately connect the account to read its timeline, bookmarks and DMs. Preview the exact post or DM and obtain approval before sending. |
| 12 | Vault and secure input | Install KeePassXC and enable `vault`. A hosted manager is optional and only if its free tier stays free. Test masked entry and autofill using dummy credentials, address, contact and test-card data. Keep passwords, card numbers, codes, tokens and keys out of chat, screenshots and logs. Use private input or user handoff for 2FA. Bind purchase approval to the specific order. |
| 13 | Computer and browser | After the Windows node is paired, use it for persistent scripts, tool installation and PDF, CSV, spreadsheet, Word, slide, chart and ZIP output. Test an isolated signed-in browser profile across two jobs using a sample application or settings form. Pause before final submission unless authorised. Hand CAPTCHA and passkey challenges to the user. Obtain approval each time for commands or transfers on a personal computer. A persistent remote computer is optional and subject to the zero-cost gate. |
| 14 | Research and shopping | Compare current products, prices, hotels, flights and restaurants, and retrieve hours, maps, weather and news. Record source and retrieval time for changing facts. Check currency, time-zone and unit conversions and calculations. Preview the complete order or booking and obtain explicit confirmation. |
| 15 | Phone and messaging | Where a zero-cost calling interface is connected, test a call to a consenting recipient before calling a business. Relay a live question to the user and return the approved answer. Draft SMS and app messages, preview recipient and content, then obtain approval to send. |
| 16 | Meetings and team chat | With an invited test meeting, verify joining, permitted note-taking and posting in meeting chat when requested. Check participant consent before capture or transcription. Test a team-chat or notes service separately if one is selected and eligible at zero cost. |
| 17 | Automation | Create a one-off reminder, a recurring routine at a specified local time, and an email, GitHub or webhook trigger. Verify the time zone, deduplication and recovery after restart. List, edit, pause, resume and run a routine on demand. Scheduled runs inherit the same approval rules. Heartbeat and cron need one connected delivery channel or `commands.ownerAllowFrom`. |
| 18 | Memory and skills | Save a standing preference, an approval rule with its scope, and a reusable step-by-step playbook locally. Retrieve them in a new assistant session. Change or revoke a rule and verify the next run sees the update. Keep secrets in the vault. |
| 19 | Multiple agents | Assign one owner per job, send a scoped task or rule update to another assistant, and review its authorised task conversation and result. Demonstrate usage reporting per assistant and routine. Keep unrelated private chats outside the handoff. |
| 20 | Phone integration | Pair an authorised phone and check OS permissions for calendar, contacts, reminders, alarms, smart-home controls and location individually. Verify each supported function with a test action and confirm that revoking access takes effect. Record platform-specific limits. |

## Plugins to enable

Enable only these. One tool per job. Commands and the matching disable list are in the [fresh-install guide](../README.md).

- [ ] Enable `ollama` — local inference through Ollama.
- [ ] Enable `acpx` — OpenCode coding sessions.
- [ ] Enable `memory-core` — recall.
- [ ] Enable `memory-wiki` — durable project pages.
- [ ] Enable `workboard` — task tracking for the main agent.
- [ ] Enable `policy` — configuration review. Leave automatic workspace repair off until a project policy exists.
- [ ] Enable `oc-path` — `oc://` paths for workspace files.
- [ ] Enable `llm-task` — JSON workflow steps, allowlisted to local `qwen3.8:27b` only.
- [ ] Enable `code-mode-quickjs` — local QuickJS execution.
- [ ] Enable `imap` — mailbox watcher. Connect a mailbox separately.
- [ ] Enable `github` — repository reads. Connect write access separately.
- [ ] Enable `browser` — local browser tool.
- [ ] Enable `document-extract` — local document text.
- [ ] Enable `file-transfer` — file movement between devices.
- [ ] Enable `canvas` — local canvas output.
- [ ] Enable `duckduckgo` — key-free web search.
- [ ] Enable `web-readability` — readable page text.
- [ ] Enable `device-pair` — pair the Windows node.
- [ ] Enable `tts-local-cli` — local text to speech.
- [ ] Enable `talk-voice` — local voice.
- [ ] Enable `vault` — secret references. Connect KeePassXC separately.

## Plugins to leave disabled

Paid providers and duplicates. Disable each one. Do not enable a second plugin for a job the keep list already covers.

- [ ] Disable `openai`
- [ ] Disable `google`
- [ ] Disable `xai`
- [ ] Disable `anthropic`
- [ ] Disable `alibaba`
- [ ] Disable `minimax`
- [ ] Disable `nvidia`
- [ ] Disable `together`
- [ ] Disable `huggingface`
- [ ] Disable `microsoft-foundry`
- [ ] Disable `github-copilot`
- [ ] Disable `copilot-proxy`
- [ ] Disable `opencode-go`
- [ ] Disable `openrouter`
- [ ] Disable `clawrouter`
- [ ] Disable `litellm`
- [ ] Disable `lmstudio`
- [ ] Disable `vllm`
- [ ] Disable `sglang`
- [ ] Disable `fal`
- [ ] Disable `kie`
- [ ] Disable `runway`
- [ ] Disable `azure-speech`
- [ ] Disable `elevenlabs`
- [ ] Disable `microsoft`
- [ ] Disable `deepgram`
- [ ] Disable `senseaudio`
- [ ] Disable `active-memory`
- [ ] Disable `cua-computer`
- [ ] Disable `linux-node`

## Main chat setup

Every area is still to connect. The [local productivity skill](../skills/local-productivity/SKILL.md) and the [workspace capabilities skill](../skills/workspace-capabilities/SKILL.md) are source in this repository. Install their tools before relying on them in chat.

- [ ] Mail — enable `imap` and connect one mailbox. Sign-in stays on the provider page.
- [ ] Calendar and contacts — connect Nextcloud CalDAV, or another free calendar, and read one event.
- [ ] App builders — install OpenCode via acpx and run one local build.
- [ ] Repositories — enable `github` and connect the repository used for a disposable branch.
- [ ] Hosting — read one deployment log, or serve one loopback site, before any change.
- [ ] Databases — open one read-only SQLite file and run a sample query.
- [ ] DNS and hosting — connect a zone or panel only when a read test is ready.
- [ ] Error tracking — connect a zero-cost project and read one sample event.
- [ ] Files — install LibreOffice and the document tools, then create one file from chat.
- [ ] Design and media — install ComfyUI with SDXL base 1.0, plus FFmpeg. Flux needs a quantised build on the 12 GB RTX 4070.
- [ ] Social — enable `duckduckgo` and install SearXNG before any public research from chat.
- [ ] Vault — install KeePassXC, enable `vault`, and run a dummy-secret lookup.
- [ ] Browser and computer — enable `browser`, install `@playwright/mcp`, and pair the Windows node.
- [ ] Research and shopping — enable `web-readability` and run one search. A purchase or booking needs a separate approval.
- [ ] Calls and messaging — connect one delivery channel or set `commands.ownerAllowFrom`.
- [ ] Meetings and team chat — connect an invited test meeting before notes or transcription.
- [ ] Automation — list routines only after the scheduler is installed, then test one disposable run.
- [ ] Memory and skills — enable `memory-core` and `memory-wiki`, then save and revoke one preference across two sessions.
- [ ] Multiple agents — enable `workboard` for the main assistant.
- [ ] Phone integration — install KDE Connect and pair one device.

## Approval rules

- Reading and research within an authorised scope, and preparing private drafts, require no additional approval. Connecting an account requires the appropriate login and consent.
- For email, obtain explicit send approval or match a saved rule covering the sender account, recipients and purpose. Social posts, DMs and phone messages use the stricter preview and approval requirements above.
- Confirm external sharing, publication, production deployment, DNS changes, migrations and security changes before execution. Confirm deletions, including bulk mailbox cleanup, against their exact scope.
- Confirm the order, payee, total and any recurring terms before a user-directed purchase or booking. Buying services, subscriptions or credits to operate OpenClaw remains outside the project budget.
- Enter secrets only through the provider's secure flow, a vault or private user input. Keep account names, addresses, identifiers, credentials and private content out of public setup notes.

## Reporting connection status

This checklist records requested behaviour. The setup lists above are still to do. A working login for maintaining this repository does not mean the OpenClaw agent can use that service.

During setup, record a result **per provider and operation** in each numbered area so a successful read cannot imply permission to write. Use **Connected** after an end-to-end test from OpenClaw, **Available but not connected** after verifying an eligible interface and identifying the missing login or setup step, or **Not possible** with the observed platform, permission or cost constraint. Until that test, mark the item **Unverified**. Include the test date, sanitised result, remaining setup step and limits. Keep personal details and raw evidence local.
