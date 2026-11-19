# Free and maintained software review

Reviewed 18 November 2026 for the active OpenClaw workspace on Windows. This review covers the core runtime, the roadmap's principal local tool candidates, and all 20 requested capability areas. Archived JARVIS code is outside the active stack.

## Installed runtime

| Component | Installed | Upstream comparison and decision |
|---|---|---|
| Gateway | OpenClaw CLI 2026.11.1 inside Store package 2026.11.100.0 | Core release 2026.11.5 is newer. WinGet listed no newer Store package. The Store package and bundled CLI use different numbering. Track the supported Windows channel. [Core releases](https://github.com/openclaw/openclaw/releases) |
| Companion | 2026.11.1 | WinGet offered 2026.11.3, matching the Windows project's latest release. Update available. [Windows releases](https://github.com/openclaw/openclaw-windows-node/releases) |
| Ollama | 0.40.16 | Matches the latest published stable release checked. Local inference uses the existing PC. [Releases](https://github.com/ollama/ollama/releases) |
| Qwen | qwen3.8:27b, local ID aaee06c39dcf | Matches the registry's llama.cpp variant on the tag page. Local and registry licence both report Apache 2.0. [Model and licence](https://ollama.com/library/qwen3.8:27b) |
| OpenCode CLI | 2.2.6 | Official v2 package @opencode/cli reported 2.3.2 as latest. Update available. The separate opencode-ai package tracks v1. Use the v2 channel for this install. [Publisher instructions](https://opencode.ai/product) · [v2 registry](https://registry.npmjs.org/@opencode%2fcli/latest) |

The live read-only status tool passed model presence, Gateway service state, authenticated health and paired Node connectivity. Native chat inference, ACP task completion and upgrade regression tests require separate evidence. No software was upgraded during this review.

## Project activity and adoption

GitHub repository metadata retrieved on the review date. Stars measure interest and provide a tie-breaker. A repository push can be automated. Before using any candidate, check substantive changes on its maintained branch, compatible releases, security notices and the exact licence for the shipped build and model. A project with infrequent releases needs evidence of ongoing support. Exclude archived, superseded and unsupported projects from new installations.

| Upstream | Licence reported by GitHub | Stars | Last push (UTC) |
|---|---|---:|---|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | MIT | 394,723 | 2026-11-18 |
| [openclaw/openclaw-windows-node](https://github.com/openclaw/openclaw-windows-node) | MIT | 2,205 | 2026-11-18 |
| [ollama/ollama](https://github.com/ollama/ollama) | MIT | 187,520 | 2026-11-18 |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | MIT | 227,738 | 2026-11-18 |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | MIT | 135,634 | 2026-11-18 |
| [searxng/searxng](https://github.com/searxng/searxng) | AGPL-3.0 | 39,669 | 2026-11-18 |
| [microsoft/playwright](https://github.com/microsoft/playwright) | Apache-2.0 | 100,488 | 2026-11-18 |
| [pywinauto/pywinauto](https://github.com/pywinauto/pywinauto) | BSD-3-Clause | 6,434 | 2026-11-08 |
| [FlaUI/FlaUI](https://github.com/FlaUI/FlaUI) | MIT | 3,217 | 2026-08-13 |
| [tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract) | Apache-2.0 | 77,578 | 2026-11-15 |
| [git/git](https://github.com/git/git) | Inspect upstream licence files | 64,365 | 2026-11-17 |
| [sqlite/sqlite](https://github.com/sqlite/sqlite) | Inspect upstream licence files | 11,042 | 2026-11-18 |
| [python/cpython](https://github.com/python/cpython) | Inspect upstream licence files | 78,385 | 2026-11-18 |
| [nodejs/node](https://github.com/nodejs/node) | Inspect upstream licence files | 123,782 | 2026-11-18 |
| [PowerShell/PowerShell](https://github.com/PowerShell/PowerShell) | MIT | 56,230 | 2026-11-18 |
| [nextcloud/server](https://github.com/nextcloud/server) | AGPL-3.0 | 37,553 | 2026-11-18 |
| [home-assistant/core](https://github.com/home-assistant/core) | Apache-2.0 | 92,347 | 2026-11-18 |
| [bitwarden/clients](https://github.com/bitwarden/clients) | Inspect upstream licence files | 14,261 | 2026-11-18 |
| [jitsi/jitsi-meet](https://github.com/jitsi/jitsi-meet) | Apache-2.0 | 30,253 | 2026-11-18 |
| [KDE/kdeconnect-kde](https://github.com/KDE/kdeconnect-kde) | Inspect upstream licence files | 4,169 | 2026-11-18 |
| [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg) | Inspect upstream licence files | 67,539 | 2026-11-18 |
| [libreoffice/core](https://github.com/LibreOffice/core) | GPL-3.0 | 4,659 | 2026-11-18 |
| [WordPress/wordpress-develop](https://github.com/WordPress/wordpress-develop) | GPL-2.0 | 3,515 | 2026-11-18 |
| [coollabsio/coolify](https://github.com/coollabsio/coolify) | Apache-2.0 | 66,210 | 2026-11-18 |
| [openclaw/acpx](https://github.com/openclaw/acpx) | MIT | 3,442 | 2026-11-18 |
| [getsentry/self-hosted](https://github.com/getsentry/self-hosted) | Inspect upstream licence files | 9,656 | 2026-11-18 |
| [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) | GPL-3.0 | 147,462 | 2026-11-18 |
| [keepassxreboot/keepassxc](https://github.com/keepassxreboot/keepassxc) | Inspect upstream licence files | 30,048 | 2026-11-17 |
| [mastodon/mastodon](https://github.com/mastodon/mastodon) | AGPL-3.0 | 50,595 | 2026-11-18 |
| [go-gitea/gitea](https://github.com/go-gitea/gitea) | MIT | 59,151 | 2026-11-18 |

Reject the archived [opencode-ai/opencode repository](https://github.com/opencode-ai/opencode). The maintained coding agent comes from [Anomaly](https://github.com/anomalyco/opencode). For ACP, establish which backend is installed before choosing an update. FlaUI shows a longer interval since its last push than pywinauto. Keep both as candidates until release support and Windows application coverage are verified.

## Decisions for the 20 requested capabilities

These are implementation choices to evaluate. Existing Windows and hardware are assumed. A local option avoids a service fee but still needs a compatibility and resource test.

| # | Capability | Zero-cost route and limits |
|---|---|---|
| 1 | Email | Use supported mailbox protocols or free API access to an authorised free inbox. Exclude paid mailbox provisioning and verify attachment and monitoring quotas. |
| 2 | Calendar and contacts | Evaluate local calendars and CalDAV/CardDAV with a local Nextcloud instance. Hosted booking links remain optional. |
| 3 | App building | Build existing projects locally with OpenCode and Git. A builder account needs demonstrably free repeat builds and access to the existing project. |
| 4 | Code and repositories | Local Git and OpenCode are the default. Use GitHub for repository operations within the free plan. Run builds locally. Exclude metered runners and cloud agents. |
| 5 | Hosting and deploys | Serve on the existing PC. A free service that sleeps or loses files cannot satisfy persistent hosting. Render documents both behaviours. [Free compute limits](https://render.com/docs/free) |
| 6 | Databases | Use local SQLite where suitable. Hosted SQL needs an explicit zero-cost quota and a tested local recovery path. |
| 7 | Domains, DNS and hosting | Test locally with local names and WordPress. Registration, renewal and paid host migration services are excluded. An existing domain is optional. |
| 8 | Error tracking | Begin with local logs and release IDs. Evaluate a local error tracker after checking its distribution licence and storage requirements. |
| 9 | Documents and files | Use local LibreOffice and a persistent local directory. Cloud sharing requires workload-specific quota and permission checks. |
| 10 | Design and media | Evaluate local ComfyUI and FFmpeg. Check model, asset, font and codec rights separately. Exclude paid credits. |
| 11 | Social media | Use public pages or supported, free, authorised APIs. Mastodon is a candidate for compatible accounts. Paid API-only operations are unavailable. |
| 12 | Vault and logins | Evaluate local KeePassXC with per-login approval. Exclude paid vault features and test with dummy data. |
| 13 | Computer and browser | Use the existing Windows Node, native UI Automation and local Playwright. A hosted computer is outside the baseline. |
| 14 | Research and shopping | Evaluate local SearXNG and free public sources. Use local calculation and conversion tools. Paid feeds and search APIs are excluded. |
| 15 | Calls and messaging | Draft locally. App-to-app calls on a free service may qualify. Calls to telephone numbers and SMS remain unavailable unless their exact route has verified zero charges. |
| 16 | Meetings and team chat | Evaluate local Jitsi for controlled meetings. Joining a third-party meeting, capturing audio or sending chat requires a supported free interface and permission. |
| 17 | Automation | Use local scheduling and a persistent task store. Accept events via supported free interfaces. Test restart recovery and missed runs. |
| 18 | Memory and skills | Store preferences, skills and revocations locally in versioned files or SQLite. No external memory service required. |
| 19 | Multiple agents | Evaluate local OpenClaw and ACP workers sharing Ollama. Measure concurrency on this PC. Paid inference or agent orchestration is excluded. |
| 20 | Phone integration | Evaluate KDE Connect and local Home Assistant for supported devices. Test location, alarms and permissions individually. Exclude subscriptions, new hardware and paid relays. |

## Hosted provider screening

These services appeared in the capability suggestions. None is required for local operation. The links below are official provider references checked during review. A public page cannot establish the user's billing settings, actual workload or connector access. Before enabling a particular operation, verify the enduring free entitlement, API eligibility, storage and usage ceilings, hard stop at quota, and absence of a payment requirement. Reject trial-only access, automatic overages and any route whose cost remains uncertain.

| Provider and source | Review outcome |
|---|---|
| [Gmail](https://developers.google.com/workspace/gmail/api/reference/quota) | Provider page reached. Exact operation and account entitlement unverified. |
| [Outlook, OneDrive, Teams](https://www.microsoft.com/en-us/microsoft-365/buy/compare-all-microsoft-365-products) | Pricing terms could not be verified from the retrieved page. Hold. |
| [iCloud](https://support.apple.com/en-us/108047) | Provider page reached. Exact operation and account entitlement unverified. |
| [Hostinger Mail and hosting](https://www.hostinger.com/pricing) | Provider page reached. Exact operation and account entitlement unverified. |
| [Calendly](https://calendly.com/pricing) | Provider page reached. Exact operation and account entitlement unverified. |
| [Lovable](https://lovable.dev/pricing) | Provider page reached. Exact operation and account entitlement unverified. |
| [Replit](https://replit.com/pricing) | Provider page reached. Exact operation and account entitlement unverified. |
| [GitHub](https://github.com/pricing) | Repository access is in use. Metered compute, storage and premium products are outside the approved workflow. |
| [Vercel](https://vercel.com/docs/plans/hobby) | Provider page reached. Exact operation and account entitlement unverified. |
| [Railway](https://railway.com/pricing) | Provider page reached. Exact operation and account entitlement unverified. |
| [Render](https://render.com/docs/free) | Free compute sleeps after 15 idle minutes and has ephemeral local storage. Exclude for persistent workloads. |
| [Firebase](https://firebase.google.com/pricing) | Provider page reached. Exact operation and account entitlement unverified. |
| [Supabase](https://supabase.com/pricing) | Provider page reached. Exact operation and account entitlement unverified. |
| [Neon](https://neon.com/pricing) | Provider page reached. Exact operation and account entitlement unverified. |
| [Sentry](https://sentry.io/pricing/) | Provider page reached. Exact operation and account entitlement unverified. |
| [Google Sheets, Docs, Drive and Meet](https://one.google.com/about/plans) | Provider page reached. Exact operation and account entitlement unverified. |
| [Dropbox](https://www.dropbox.com/plans) | Provider page reached. Exact operation and account entitlement unverified. |
| [Picsart](https://picsart.com/pricing/) | Provider page reached. Exact operation and account entitlement unverified. |
| [Canva](https://www.canva.com/pricing/) | Pricing terms could not be verified from the retrieved page. Hold. |
| [Figma](https://www.figma.com/pricing/) | Provider page reached. Exact operation and account entitlement unverified. |
| [Adobe](https://www.adobe.com/creativecloud/plans.html) | Pricing terms could not be verified from the retrieved page. Hold. |
| [1Password](https://1password.com/pricing) | Provider page reached. Exact operation and account entitlement unverified. |
| [Bitwarden](https://bitwarden.com/pricing/) | Provider page reached. Exact operation and account entitlement unverified. |
| [Zoom](https://www.zoom.com/en/products/virtual-meetings/) | Provider page reached. Exact operation and account entitlement unverified. |
| [Slack](https://slack.com/pricing) | Provider page reached. Exact operation and account entitlement unverified. |
| [Otter](https://otter.ai/pricing) | Provider page reached. Exact operation and account entitlement unverified. |
| [Fireflies](https://fireflies.ai/pricing) | Provider page reached. Exact operation and account entitlement unverified. |

## Keeping the review current

At selection, before installation or upgrade, and whenever a provider changes terms, compare the installed build to the publisher's supported stable channel. Record the date, release, licence, cost evidence and any relevant advisory. Prefer actively maintained open-source tools with strong adoption and demonstrated success on this PC. Hold a candidate if the evidence is missing. After an update, repeat the relevant acceptance checks and record rollback instructions before marking it current.

## Main Gateway integration checks, 19 November 2026

| Integration | Installed evidence and connection status |
|---|---|
| Ollama | OpenClaw loaded the provider. Its loopback endpoint generated the requested sample reply using the configured local model. |
| ACPX | Plugin loaded. OpenCode 2.2.7 answered an ACP protocol handshake. A coding handoff originating in main remains unverified. |
| Memory Core | Plugin loaded at inventory. Live replacement timed out stopping and starting its background services. Verify recall after Gateway recovery. |
| Browser | Native browser loaded. Earlier Gateway page opening succeeded. The latest status probe timed out during plugin replacement. |
| IMAP | Watcher loaded with zero configured mailboxes. A provider-approved mailbox credential must be entered privately before a read or watch test. |
| Vault | The HashiCorp Vault SecretRef plugin loaded. No secret-provider alias or local Vault listener was found. A private backend and scoped authorisation are needed for a dummy-secret lookup. Browser password autofill is a separate integration. |
| Playwright MCP | Installed Microsoft's 0.0.86 server and matching headless Chromium in the Gateway environment. A direct MCP navigation read a public test page. OpenClaw requires exclusive offline access to register the server. |
| SearXNG | Saved the official 2026.11.1 provider for this Gateway version. Live activation failed during service replacement. No local SearXNG endpoint, Linux distribution or container engine was found. DuckDuckGo remains selected. |
| Whisper | Installed faster-whisper 1.2.1 in a separate environment. Reused and verified the existing base-model weights. PyAV 19 rejected the decoder's metadata_errors argument. PyAV 16.1 passed a synthetic speech test. OpenClaw saved a local-only audio CLI route. Live activation and a real chat attachment test are pending. |
| ComfyUI | Official comfy provider installation saved. Live activation failed during service replacement. Installed the local ComfyUI 0.46.0 backend and CUDA runtime. A loopback workflow produced a sample PNG on the local GPU. Text-to-image still requires an approved checkpoint and matching workflow. |
