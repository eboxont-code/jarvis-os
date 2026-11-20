# Free and maintained software review

Software to install for a fresh OpenClaw workspace on Windows. Nothing in this review is installed, enabled, or connected yet. Follow the [fresh-install guide](../README.md). This review covers the core runtime, the roadmap's local tool candidates, and all 20 capability areas. Archived material under `legacy/jarvis-os/` is outside the active stack.

Rules for every row: zero additional cost, local first, Ollama only, and no paid cloud inference.

## Install these

| Component | Install | Notes |
|---|---|---|
| OpenClaw | Latest stable, 2026.11.5 or newer | Windows Companion or the PowerShell installer, then `openclaw gateway install`. Confirm with `openclaw --version`. [Install](https://docs.openclaw.ai/install/) · [Windows](https://docs.openclaw.ai/platforms/windows/) · [Core releases](https://github.com/openclaw/openclaw/releases) · [Windows releases](https://github.com/openclaw/openclaw-windows-node/releases) |
| Ollama | Current stable build | Local inference on this PC. [Releases](https://github.com/ollama/ollama/releases) |
| Model | `ollama pull qwen3.8:27b` | The only inference model for chat and OpenCode. [Model and licence](https://ollama.com/library/qwen3.8:27b) |
| OpenCode | Current `@opencode/cli`, through acpx | `openclaw plugins install @openclaw/acpx`, then enable `acpx`. Point it at local Ollama only. Leave `opencode-ai` and `opencode-go` unused. [Publisher instructions](https://opencode.ai/product) · [ACP setup](https://docs.openclaw.ai/tools/acp-agents-setup) |

If Windows Hub runs the Gateway in an isolated session, give the main Windows user write access to the Gateway config. Without that write access, CLI writes hang with `file lock timeout`.

- [ ] Install OpenClaw 2026.11.5 or newer and the Gateway service.
- [ ] Install Ollama and pull `qwen3.8:27b`.
- [ ] Install OpenCode via acpx and leave cloud providers unset.
- [ ] Enable the keep-list plugins and disable the paid or duplicate plugins in the fresh-install guide.
- [ ] Run `openclaw gateway status`, `openclaw plugins list`, and `openclaw mcp list`.

The read-only status tool `python tools/check_workspace.py` is for after those steps. It checks the model tag, Gateway service, authenticated health and a paired Windows node. Expect it to fail until those pieces are installed and paired.

## Upstream activity

GitHub repository metadata below is an upstream snapshot from 18 November 2026, not a local inventory. Stars measure interest and provide a tie-breaker. Before installing any candidate, recheck its maintained branch, compatible release, security notices and the exact licence. Exclude archived, superseded and unsupported projects.

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

Reject the archived [opencode-ai/opencode repository](https://github.com/opencode-ai/opencode). The maintained coding agent comes from [Anomaly](https://github.com/anomalyco/opencode). Install OpenCode through acpx, and leave `opencode-go` disabled. FlaUI shows a longer interval since its last push than pywinauto. Keep both as candidates until release support and Windows application coverage are checked on this PC.

## Decisions for the 20 requested capabilities

These are the zero-cost routes to install or connect. They are still to do.

| # | Capability | Zero-cost route and limits |
|---|---|---|
| 1 | Email | Use supported mailbox protocols or free API access to an authorised free inbox. Enable `imap`. Exclude paid mailbox provisioning and verify attachment and monitoring quotas. |
| 2 | Calendar and contacts | Connect local CalDAV and CardDAV with a local Nextcloud instance. Hosted booking links remain optional. |
| 3 | App building | Build projects locally with OpenCode and Git. A builder account needs demonstrably free repeat builds. |
| 4 | Code and repositories | Local Git and OpenCode are the default. Use GitHub for repository operations within the free plan. Run builds locally. Exclude metered runners and cloud agents. |
| 5 | Hosting and deploys | Serve on this PC. A free service that sleeps or loses files cannot satisfy persistent hosting. Render documents both behaviours. [Free compute limits](https://render.com/docs/free) |
| 6 | Databases | Use local SQLite where suitable. Hosted SQL needs an explicit zero-cost quota and a tested local recovery path. |
| 7 | Domains, DNS and hosting | Test locally with local names and WordPress. Registration, renewal and paid host migration services are excluded. A domain is optional. |
| 8 | Error tracking | Begin with local logs and release IDs. Evaluate a local error tracker after checking its distribution licence and storage requirements. |
| 9 | Documents and files | Install local LibreOffice and use a persistent local directory. Cloud sharing requires workload-specific quota and permission checks. |
| 10 | Design and media | Install local ComfyUI with SDXL base 1.0, and install FFmpeg. This PC has a 12 GB RTX 4070. Flux needs a quantised version. Check model, asset, font and codec rights separately. Exclude paid credits. |
| 11 | Social media | Use public pages or supported, free, authorised APIs. Mastodon is a candidate for compatible accounts. Paid API-only operations are unavailable. |
| 12 | Vault and logins | Install local KeePassXC and enable `vault`, with per-login approval. Exclude paid vault features and test with dummy data. |
| 13 | Computer and browser | Pair the Windows node, use native UI Automation, and install local Playwright MCP (`@playwright/mcp`). A hosted computer is outside the baseline. |
| 14 | Research and shopping | Install local SearXNG (Docker) and use free public sources, plus the `duckduckgo` plugin. Use local calculation and conversion tools. Paid feeds and search APIs are excluded. |
| 15 | Calls and messaging | Draft locally. Connect one delivery channel or set `commands.ownerAllowFrom` so heartbeat and cron can deliver. Calls to telephone numbers and SMS stay out until their exact route has verified zero charges. |
| 16 | Meetings and team chat | Evaluate local Jitsi for controlled meetings. Joining a third-party meeting, capturing audio or sending chat requires a supported free interface and permission. |
| 17 | Automation | Use local scheduling and a persistent task store. Accept events via supported free interfaces. Test restart recovery and missed runs. |
| 18 | Memory and skills | Enable `memory-core` and `memory-wiki`. Store preferences, skills and revocations locally in versioned files or SQLite. Leave `active-memory` disabled. |
| 19 | Multiple agents | Use local OpenClaw and one ACP worker sharing Ollama. Measure concurrency on this PC. Paid inference or agent orchestration is excluded. |
| 20 | Phone integration | Install KDE Connect. Local Home Assistant is a later candidate for supported devices. Test location, alarms and permissions individually. Exclude subscriptions, new hardware and paid relays. |

## Free local tools still to add

- [ ] Install Playwright MCP (`@playwright/mcp`) and register it as a local stdio server.
- [ ] Install SearXNG with Docker.
- [ ] Install whisper.cpp.
- [ ] Install ComfyUI and download SDXL base 1.0. On this 12 GB RTX 4070, Flux needs a quantised version.
- [ ] Install KeePassXC.
- [ ] Install FFmpeg.
- [ ] Install LibreOffice.
- [ ] Connect Nextcloud CalDAV.
- [ ] Install KDE Connect.

## Hosted provider screening

These services appeared in the capability suggestions. None is required for local operation. The links below are official provider references. A public page cannot establish billing settings, actual workload or connector access. Before enabling a particular operation, verify the enduring free entitlement, API eligibility, storage and usage ceilings, hard stop at quota, and absence of a payment requirement. Reject trial-only access, automatic overages and any route whose cost remains uncertain.

| Provider and source | Review outcome |
|---|---|
| [Gmail](https://developers.google.com/workspace/gmail/api/reference/quota) | Provider page reached. Exact operation and account entitlement unverified. |
| [Outlook, OneDrive, Teams](https://www.microsoft.com/en-us/microsoft-365/buy/compare-all-microsoft-365-products) | Pricing terms could not be verified from the retrieved page. Hold. |
| [iCloud](https://support.apple.com/en-us/108047) | Provider page reached. Exact operation and account entitlement unverified. |
| [Hostinger Mail and hosting](https://www.hostinger.com/pricing) | Provider page reached. Exact operation and account entitlement unverified. |
| [Calendly](https://calendly.com/pricing) | Provider page reached. Exact operation and account entitlement unverified. |
| [Replit](https://replit.com/pricing) | Provider page reached. Exact operation and account entitlement unverified. |
| [GitHub](https://github.com/pricing) | Free repository hosting can be used. Connect assistant access separately. Metered compute, storage and premium products are outside the approved workflow. |
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

At selection, before installation or upgrade, and whenever a provider changes terms, compare the candidate build with the publisher's supported stable channel. Record the date, release, licence, cost evidence and any relevant advisory. Prefer actively maintained open-source tools with strong adoption. Hold a candidate if the evidence is missing. After an update, repeat the relevant acceptance checks and record rollback instructions before marking it current.

## Local integrations still to install

- [ ] Ollama — install it, pull `qwen3.8:27b`, and enable the `ollama` plugin. Ask for one sample reply on loopback.
- [ ] acpx — install `@openclaw/acpx`, enable `acpx`, and point OpenCode at local Ollama only. A coding handoff from chat is a separate test.
- [ ] Memory Core and Memory Wiki — enable `memory-core` and `memory-wiki`. Test recall after the Gateway is up.
- [ ] Browser — enable `browser`. Open one page from chat.
- [ ] IMAP — enable `imap`. Connect a mailbox before any read or watch test.
- [ ] Vault — enable `vault` and install KeePassXC. A dummy-secret lookup is a separate test.
- [ ] Playwright MCP — install `@playwright/mcp` and confirm it with `openclaw mcp list`.
- [ ] SearXNG — install it with Docker on loopback. Enable `duckduckgo` as the bundled search plugin. Add no second hosted search provider.
- [ ] whisper.cpp — install it and transcribe one local sample.
- [ ] ComfyUI — install it and download SDXL base 1.0. On this 12 GB RTX 4070, use a quantised Flux build if Flux is required.
