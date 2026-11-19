# Assistant capabilities and acceptance checks

These 20 requirements extend the [OpenClaw roadmap](../REQUIREMENTS.md). OpenClaw coordinates the work from the local PC. Named providers are candidates. Before adopting one, verify its supported interface, account permissions and ongoing zero-cost operation. Each row describes a setup prerequisite and a practical test using sample data.

Apply the [dependency review](DEPENDENCY_REVIEW.md) before selecting any provider. The local implementation must remain free to operate. Hosted brand names below identify optional interoperability targets. Enable an operation only after verifying its free entitlement and maintained interface.

## Installation status on 19 November 2026

OpenClaw's Gateway successfully called key-free web search, Memory Wiki status and Workboard statistics. The [local productivity skill](../skills/local-productivity/SKILL.md) is eligible for the main agent. Its Windows Gateway Python environment passed sample file and calculation tests. Those tests ran directly inside the Gateway environment. A model-driven chat turn invoking the skill remains to be verified.

| # | Area | Installed or tested | Remaining dependency or test |
|---|---|---|---|
| 1 | Email | Thunderbird and the OpenClaw IMAP watcher are installed. | Authorise the selected mailboxes privately. Test read, draft, monitoring and send permissions separately. A desktop login alone does not connect the watcher. |
| 2 | Calendar and contacts | Generated and parsed a sample ICS event and vCard. | Provider calendar and contact permissions, sync and invitation approval. |
| 3 | App building | Local OpenCode and WordPress Playground CLI are installed. | Test an end-to-end build against a selected project. A hosted builder needs its own account. |
| 4 | Code and repositories | Git and GitHub CLI are installed. | Authorise the intended identity for GitHub CLI and verify a scoped OpenClaw coding task. |
| 5 | Hosting | Caddy returned HTTP 200 with the expected content from a disposable loopback site. | Select a target before a real deployment and rollback test. |
| 6 | Databases | Both the SQLite CLI and the Gateway runtime passed sample queries. | Authorise a project database and verify read-only access. |
| 7 | Domains and WordPress | Local WordPress Playground installed and its CLI opened. | An authorised site and registrar are needed for DNS, renewal and migration checks. |
| 8 | Error tracking | Jaeger installed. Windows application error logs were readable. | Instrument a selected app and verify a trace, release and alert. |
| 9 | Spreadsheets and documents | Created and reopened XLSX, DOCX, PPTX and PDF samples. LibreOffice separately exported a PDF. | Verify a full reporting task from OpenClaw Chat and authorise any cloud sharing. |
| 10 | Design and media | Krita and Kdenlive installed. Pillow passed a PNG round trip and FFmpeg processed a synthetic clip. | Verify a finished edit and evaluate local generative models separately. |
| 11 | Social | Public research is available through web search. | Select a supported platform and authorise the account for private operations. |
| 12 | Vault | KeePassXC installed. | Private vault setup and a dummy-credential autofill approval test. |
| 13 | Computer and browser | Gateway-local files work. Native Windows control and browser plugins are present. | Companion reported a Gateway ownership inspection failure during reconnect. The paired Windows Node was offline at the last check. |
| 14 | Research | Installed the official DuckDuckGo plugin for this Gateway version. An authenticated OpenClaw search returned two results. A local unit conversion passed. | Verify live provider-specific rates, travel, prices and approved booking flows. |
| 15 | Calls and messaging | Windows Phone Link is available. | Phone pairing, device permissions and a verified zero-cost route for calls or messages. |
| 16 | Meetings | Browser-based meeting access is an integration candidate. | Select the meeting service, authorise an invited test call and verify consent-based notes. |
| 17 | Automation | OpenClaw returned the local scheduler inventory. | Verify firing, pause/resume and missed-run recovery using a disposable routine. |
| 18 | Memory and skills | The main agent catalogued local-productivity as eligible. The Gateway answered wiki_status. | Verify recall and rule revocation across two native chat sessions. |
| 19 | Multiple agents | Workboard answered a live statistics request. | Specialist agents remain removed at the operator's request. |
| 20 | Phone | Windows Phone Link and KDE Connect are installed. | Complete device pairing and verify each supported permission. Desktop pairing alone does not register an OpenClaw iOS node. |

## Capability checklist

| # | Capability | Setup and acceptance check |
|---|---|---|
| 1 | Email | Authorise each selected inbox separately (e.g. Gmail, Outlook, iCloud or Hostinger). Search and summarise a thread with a PDF invoice, save a reply in the correct mailbox, and test labels, sorting, archive, trash and spam/promotion cleanup on sample mail. Monitor bills, verification notices, job replies and selected senders. Keep codes out of summaries. Apply the send and deletion rules below. |
| 2 | Calendar and contacts | Connect an authorised Google, Outlook or iCloud calendar and address book. Resolve a test contact, find a free slot, then create, move and cancel a test event. Verify booking-link management if a service such as Calendly is connected. Ask before changes that affect other people. |
| 3 | App builders | Select the account and existing Lovable, Replit or equivalent project. Compare project history and revision with the linked repository, detect an active build and wait for it before submitting a prompt. Verify the result in the same project. Automatic approvals cover build plans only. Secret access, payment and publishing fall outside that permission. |
| 4 | Code and repositories | Scope GitHub or another provider to selected repositories. Read commits, branches, PRs, issues and CI. Test lint, build and tests before pushing a fix, merging a clean PR or closing a superseded PR with a note. Honour main-branch protection. Prohibit force pushes, resets and history rewrites. Use local OpenCode for large jobs. A separately authorised remote worker requires a zero-cost environment and a scoped handoff. |
| 5 | Hosting and deployment | Connect a selected host such as Vercel, Railway, Render or Firebase. Trace a deployment from commit to build logs, runtime errors and live revision. Test the approval flow for environment variables, domain changes, redeploy and rollback. Redact values from evidence. |
| 6 | Databases | With a read-only role, list projects and tables, identify the database used by a running site, run a sample SELECT and review security and performance advisories. Require explicit approval for migrations, schema changes and destructive SQL. Verify against disposable data. |
| 7 | Domains, DNS and web hosting | Connect the selected registrar or hosting panel. Inspect mail, verification and site records, renewals, expiry, billing, SSL, site health, speed and errors. Test a domain connection, WordPress update/security check and host migration on a test site. Confirm DNS and production changes before applying them. |
| 8 | Error tracking | Connect a zero-cost error tracker such as a self-hosted instance. Trigger a sample crash, locate its stack trace, identify the release and verify delivery of a test alert. |
| 9 | Spreadsheets, documents and files | Produce an editable spreadsheet with formulas and charts, a tracker, document, PDF and slide deck. Extract sample data from a PDF, table and image. Reopen and update a saved report or dashboard from a persistent local library. Test optional Sheets, Docs, Drive, OneDrive or Dropbox access, approved sharing and email delivery separately. |
| 10 | Design and media | Verify local image generation and editing, then produce a short video with edited footage, narration, captions and music. Test an optional design-tool import/export (e.g. Figma, Canva, Picsart or Adobe) where free access allows it. Use free assets and locally generated graphics. Purchased design credits conflict with the project budget. |
| 11 | Social media | Search public posts, profiles, trends and news where public access permits. Separately authorise the user's account to read its timeline, bookmarks and DMs. Preview the exact post or DM and obtain approval before sending. |
| 12 | Vault and secure input | Use a password manager such as Bitwarden or 1Password if eligible, with approval per login. Test masked entry and autofill using dummy credentials, address, contact and test-card data. Keep passwords, card numbers, codes, tokens and keys out of chat, screenshots and logs. Use private input or user handoff for 2FA. Bind purchase approval to the specific order. |
| 13 | Computer and browser | Use the paired Windows node for persistent scripts, tool installation and PDF, CSV, spreadsheet, Word, slide, chart and ZIP output. Test an isolated signed-in browser profile across two jobs using a sample application or settings form. Pause before final submission unless authorised. Hand CAPTCHA and passkey challenges to the user. Obtain approval each time for commands or transfers on a personal computer. A persistent remote computer is optional and subject to the zero-cost gate. |
| 14 | Research and shopping | Compare current products, prices, hotels, flights and restaurants, and retrieve hours, maps, weather and news. Record source and retrieval time for changing facts. Check currency, time-zone and unit conversions and calculations. Preview the complete order or booking and obtain explicit confirmation. |
| 15 | Phone and messaging | Where an authorised zero-cost calling interface exists, test a call to a consenting recipient before calling a business. Relay a live question to the user and return the approved answer. Draft SMS and app messages, preview recipient and content, then obtain approval to send. |
| 16 | Meetings and team chat | With an invited test meeting on Meet, Zoom or Teams, verify joining, permitted note-taking and posting in meeting chat when requested. Check participant consent before capture or transcription. Test Slack, Teams, Otter or Fireflies separately if selected and eligible. |
| 17 | Automation | Create a one-off reminder, a recurring routine at a specified local time, and an email, GitHub or webhook trigger. Verify the time zone, deduplication and recovery after restart. List, edit, pause, resume and run a routine on demand. Scheduled runs inherit the same approval rules. |
| 18 | Memory and skills | Save a standing preference, an approval rule with its scope, and a reusable step-by-step playbook locally. Retrieve them in a new authorised assistant session. Change or revoke a rule and verify the next run sees the update. Keep secrets in the vault. |
| 19 | Multiple agents | Assign one owner per job, send a scoped task or rule update to another assistant, and review its authorised task conversation and result. Demonstrate usage reporting per assistant and routine. Keep unrelated private chats outside the handoff. |
| 20 | Phone integration | Pair an authorised phone and check OS permissions for calendar, contacts, reminders, alarms, smart-home controls and location individually. Verify each supported function with a test action and confirm that revoking access takes effect. Record platform-specific limits. |

## Selected Windows Gateway plugins

On 19 November 2026, the installed OpenClaw 2026.11.1 plugin registry reported all seven entries below as loaded and zero repeated plugin IDs. These bundled plugins use the existing installation. This check establishes registration. Each workflow still needs its own functional test.

| Plugin | Roadmap use | Scope |
|---|---|---|
| Workboard | Task tracking and recovery | Tracks work items, ownership and completion evidence. Works with the main agent. |
| Memory Wiki | Durable project knowledge | Compiles reference pages. Memory Core continues to handle recall. |
| Policy | Configuration review | Adds workspace conformance checks to Doctor. Automatic workspace repair is disabled. A project policy is needed for project-specific checks. |
| OC Path | Documents and file workflows | Adds a CLI for addressing workspace files with oc:// references. File Transfer handles movement between devices. |
| LLM Task | Structured data extraction | Offers a JSON workflow step. The configured completion allowlist contains only the existing local Ollama Qwen model. |
| Code Mode QuickJS | Local computation | Supplies the QuickJS executor for Code Mode. Executor registration and a successful Code Mode job are separate checks. |
| IMAP | Incoming mail monitoring | Loads the mailbox watcher. No account was connected. Mailbox authorisation and sender rules are prerequisites for a live test. |

Browser, document extraction, GitHub public reading and ACP already have loaded plugins. The GitHub reader covers public documents and previews. Repository writes require separate access. MCP Events requires a public HTTPS callback in this build and was deferred.

## Main chat setup on 19 November 2026

The main assistant has a workspace-capabilities skill for choosing tools and applying the approval rules. Each row below describes the operation actually available or the setup still needed.

| # | Area | Status and remaining setup |
|---|---|---|
| 1 | Mail | Available but not connected. Gmail, Outlook and iCloud sign-in pages have dashboard widgets. Private sign-in and a mailbox read are required. IMAP monitoring requires separate authorisation. |
| 2 | Calendar and contacts | Available but not connected for browser access to calendar providers. Sign in and test an event read. Contact sync and booking links are unverified. |
| 3 | App builders | Unverified. Select an existing project and authorise its account, then verify project history, free build entitlement and linked repository before a build. |
| 4 | Repositories | Public reader registered. Private reads, writes and CI access from main are unverified. Authorise the repository and test a disposable branch. |
| 5 | Hosting | Unverified. An authorised project and a successful deployment-log read are needed before any approved deployment change. |
| 6 | Databases | Hosted access unverified. Supply an authorised read-only connection through private setup and verify a sample query. |
| 7 | DNS and hosting | Unverified. Authorise the relevant zone or hosting panel and test a read before requesting approval for changes. |
| 8 | Error tracking | Unverified. Select an eligible project and verify a sample event, release and alert. |
| 9 | Files | The installed workspace-files plugin returned a valid PDF in a direct tool test. All four formats passed content checks. Main Chat attachment delivery remains unverified because the Gateway reported startup inspection in progress. Cloud editing, storage and sharing require separate authorisation. |
| 10 | Design and media | Unverified. Local image processing libraries are present. Generative image, video, audio and design account workflows need specific tools and sample exports. |
| 11 | Social | Public web research is available where indexed. Private timeline, bookmarks and DMs require an authorised account and a separate test. |
| 12 | Vault | Unverified. A secure per-login handoff and masked test credential are prerequisites. Never paste secrets into the chat. |
| 13 | Browser and computer | Connected for browser page opening. Persistent signed-in sessions and access to personal computers are separate. Windows node ownership proof is unresolved. |
| 14 | Research and shopping | Connected for web search. Check availability on the source page. A purchase or booking needs separate approval. |
| 15 | Calls and messaging | Unverified. No tested free calling interface or authorised messaging channel. A draft can be prepared in chat. |
| 16 | Meetings and team chat | Unverified. An invited test meeting, consent and an authorised workspace are required. |
| 17 | Automation | Connected for listing routines. Scheduled delivery, restart recovery and provider event triggers need separate tests. |
| 18 | Memory and skills | Connected for Wiki access. Skills can be installed in main. Recall and revocation of a saved preference across fresh sessions need a separate test. |
| 19 | Multiple agents | Excluded by request. Workboard is available to the main assistant for tracking tasks. |
| 20 | iPhone integration | Unverified. Pair an authorised device and verify each exposed operation. Mail dashboard access provides no device permissions. |

## Approval rules

- Reading and research within an authorised scope, and preparing private drafts, require no additional approval. Connecting an account requires the appropriate login and consent.
- For email, obtain explicit send approval or match a saved rule covering the sender account, recipients and purpose. Social posts, DMs and phone messages use the stricter preview and approval requirements above.
- Confirm external sharing, publication, production deployment, DNS changes, migrations and security changes before execution. Confirm deletions, including bulk mailbox cleanup, against their exact scope.
- Confirm the order, payee, total and any recurring terms before a user-directed purchase or booking. Buying services, subscriptions or credits to operate OpenClaw remains outside the project budget.
- Enter secrets only through the provider's secure flow, a vault or private user input. Keep account names, addresses, identifiers, credentials and private content out of public setup notes.

## Reporting connection status

This checklist records requested behaviour. The dated installation table above records the operations tested so far. A working GitHub login for maintaining this repository, for example, does not establish that the OpenClaw agent can access GitHub.

During setup, record a result **per provider and operation** in each numbered area so a successful read cannot imply permission to write. Use **Connected** after an end-to-end test from OpenClaw, **Available but not connected** after verifying an eligible interface and identifying the missing login or setup step, or **Not possible** with the observed platform, permission or cost constraint. Until assessed, mark the item **Unverified**. Include the test date, sanitised result, remaining setup step and limits. Keep personal details and raw evidence local.
