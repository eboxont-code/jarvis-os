# OpenClaw Workspace

A local Windows AI workspace. OpenClaw is the assistant, Ollama serves one local model on the same PC, and OpenCode is the coding backend through ACP. This PC is a fresh install. Nothing in this guide is installed, enabled, connected, configured, paired, or running yet.

The rules for every step are in [REQUIREMENTS.md](REQUIREMENTS.md): zero additional cost, local first, Ollama only, and no paid cloud inference.

## Fresh install

Work through these steps in order on Windows. Leave each box unchecked until that step is finished on the PC.

### 1. Install OpenClaw

Install the latest stable OpenClaw, **2026.11.5 or newer**.

- [ ] Install OpenClaw Companion from the latest stable [Windows Hub release](https://github.com/openclaw/openclaw-windows-node/releases) (`OpenClawCompanion-Setup-x64.exe`), or install the CLI:

~~~powershell
iwr -useb https://openclaw.ai/install.ps1 | iex
openclaw --version
~~~

- [ ] Confirm `openclaw --version` prints 2026.11.5 or newer.
- [ ] Install the Gateway service:

~~~powershell
openclaw gateway install
~~~

Windows Hub can run the native Gateway in an isolated session, separate from the interactive Windows user. Give the main Windows user write access to that Gateway config. An isolated session that keeps the config to itself makes CLI writes hang with `file lock timeout`.

Install notes: [Windows](https://docs.openclaw.ai/platforms/windows/) and [Install](https://docs.openclaw.ai/install/). Release list: [openclaw/openclaw](https://github.com/openclaw/openclaw/releases).

### 2. Install Ollama and pull the local model

- [ ] Install Ollama from [ollama.com/download](https://ollama.com/download).
- [ ] Pull the local model `qwen3.8:27b`:

~~~powershell
ollama pull qwen3.8:27b
~~~

- [ ] Enable the Ollama provider for this Gateway, local only, and select `qwen3.8:27b`:

~~~powershell
openclaw onboard
~~~

In onboarding, choose Ollama and **Local only**. The model page is [qwen3.8:27b](https://ollama.com/library/qwen3.8:27b). Provider notes: [Ollama setup](https://docs.openclaw.ai/providers/ollama/setup).

### 3. Install OpenCode via acpx

- [ ] Install the current OpenCode v2 CLI, package `@opencode/cli`. Publisher notes: [opencode.ai/product](https://opencode.ai/product).
- [ ] Install the ACP backend `@openclaw/acpx` (enable it with the keep list in the next step):

~~~powershell
npm install -g @opencode/cli
openclaw plugins install @openclaw/acpx
~~~

- [ ] Point OpenCode at local Ollama only (`http://127.0.0.1:11434`) and the model `qwen3.8:27b`. Leave every cloud provider unset.

Use the maintained `@opencode/cli` package. Leave the archived `opencode-ai` package uninstalled, and leave the `opencode-go` plugin disabled in the next step. ACP notes: [ACP agents setup](https://docs.openclaw.ai/tools/acp-agents-setup).

### 4. Enable only the plugins to keep

Keep one tool per job. Enable the plugins in the first list. Leave the plugins in the second list disabled: they are paid providers or duplicates of a plugin already in the keep list.

`openclaw plugins enable` and `openclaw plugins disable` accept several ids and stop at the first failure. Start the Gateway again after these changes so they load. If `plugins.allow` is set, list only the keep ids.

- [ ] Enable `ollama`
- [ ] Enable `acpx`
- [ ] Enable `memory-core`
- [ ] Enable `memory-wiki`
- [ ] Enable `workboard`
- [ ] Enable `policy`
- [ ] Enable `oc-path`
- [ ] Enable `llm-task`
- [ ] Enable `code-mode-quickjs`
- [ ] Enable `imap`
- [ ] Enable `github`
- [ ] Enable `browser`
- [ ] Enable `document-extract`
- [ ] Enable `file-transfer`
- [ ] Enable `canvas`
- [ ] Enable `duckduckgo`
- [ ] Enable `web-readability`
- [ ] Enable `device-pair`
- [ ] Enable `tts-local-cli`
- [ ] Enable `talk-voice`
- [ ] Enable `vault`

~~~powershell
openclaw plugins enable ollama acpx memory-core memory-wiki workboard policy oc-path llm-task code-mode-quickjs imap github browser document-extract file-transfer canvas duckduckgo web-readability device-pair tts-local-cli talk-voice vault
~~~

Leave these disabled (paid or duplicate):

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

~~~powershell
openclaw plugins disable openai google xai anthropic alibaba minimax nvidia together huggingface microsoft-foundry github-copilot copilot-proxy opencode-go openrouter clawrouter litellm lmstudio vllm sglang fal kie runway azure-speech elevenlabs microsoft deepgram senseaudio active-memory cua-computer linux-node
~~~

### 5. Add the free local tools

Add these on the same PC. Each one is still to install or connect. Skip a second tool that does the same job as one already in this list.

- [ ] Install the Playwright MCP server `@playwright/mcp` and register it as a local stdio MCP server.
- [ ] Install SearXNG with Docker and serve it on loopback. Project: [searxng/searxng](https://github.com/searxng/searxng).
- [ ] Install whisper.cpp. Project: [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp).
- [ ] Install ComfyUI and download SDXL base 1.0. Project: [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI). This PC has a 12 GB RTX 4070. Flux needs a quantised version.
- [ ] Install KeePassXC for the local vault. Project: [keepassxc](https://github.com/keepassxreboot/keepassxc).
- [ ] Install FFmpeg. Project: [FFmpeg](https://github.com/FFmpeg/FFmpeg).
- [ ] Install LibreOffice. Project: [LibreOffice](https://github.com/LibreOffice/core).
- [ ] Connect a local Nextcloud CalDAV calendar. Project: [nextcloud/server](https://github.com/nextcloud/server).
- [ ] Install KDE Connect. Project: [kdeconnect-kde](https://github.com/KDE/kdeconnect-kde).

### 6. Connect one delivery channel or set commands.ownerAllowFrom

Heartbeat and cron need one owner route before they can deliver. Store the owner id on the PC. Keep it out of this repository.

- [ ] Connect one delivery channel and allow the owner identity on that channel, or set `commands.ownerAllowFrom` to that owner identity:

~~~powershell
openclaw config set commands.ownerAllowFrom '["channel:OWNER"]'
~~~

Replace `channel:OWNER` with the real channel and owner id while editing the local config.

### 7. Verify

- [ ] Check the Gateway, the plugin lists, and the MCP servers:

~~~powershell
openclaw gateway status
openclaw plugins list
openclaw mcp list
~~~

`openclaw plugins list` should show the keep list enabled and the paid or duplicate list disabled. `openclaw mcp list` should show the local MCP servers added above, including `@playwright/mcp` once that step is done.

## Features and requirements

The [active roadmap](REQUIREMENTS.md) covers all 14 delivery phases, integration gates A–H and acceptance tests T01–T31. Those items are still to do.

The [assistant capability checklist](docs/ASSISTANT_CAPABILITIES.md) covers 20 areas, including email, hosting, secure input and phone integration. Each entry is a setup step and an acceptance check.

The [dependency review](docs/DEPENDENCY_REVIEW.md) lists the software to install, upstream projects and zero-cost options for all 20 capability areas.

## After the guide

Open **OpenClaw Chat**, or open Companion and choose the **main** agent. The model to select is **qwen3.8:27b**. The Ollama entry in the model picker is the direct chat. The OpenCode (ACP) entry uses the same local model for a coding session.

This repository contains a read-only status tool. It needs Python 3 on Windows, the OpenClaw Gateway package with its qualified clawctl alias, and Ollama on its default loopback port. Run it from the repository root in PowerShell after the install steps that those checks depend on:

~~~powershell
python tools/check_workspace.py
~~~

The tool checks that Ollama lists `qwen3.8:27b`, that the Windows Gateway service is up, that authenticated Gateway health succeeds, and that a Windows node is paired and connected. It prints one result per check and returns exit code 1 if any check fails. Until those steps are done, a failing check is the expected result. The tool does not change configuration. To test inference, send a short prompt in OpenClaw Chat and wait for its answer.

Pair the Windows node from Companion when Gateway setup asks for it. Approve the new device request from the Gateway host. A passing status check only shows connectivity. Model downloads, live credentials, chat histories, and machine-specific configuration stay on the local PC.

## Project history

The previous project's tracked files are preserved under `legacy/jarvis-os/` as an archive of a wiped install. Its launchers, version numbers, pairing notes, and installation instructions are retired. Use this guide and [REQUIREMENTS.md](REQUIREMENTS.md).
