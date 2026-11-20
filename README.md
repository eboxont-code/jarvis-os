# OpenClaw agent

You run on this Windows PC. Inference is local Ollama only. Coding is OpenCode through ACP. Nothing below is installed or verified. Checked against docs.openclaw.ai, the Ollama library, and each tool's repository on 2026-11-20. Stable OpenClaw is 2026.11.6. Leave betas unused.

This PC is Windows 11 Pro, an Intel Core i9-14900F (24 cores, 32 threads), 64 GB DDR5-5600, and an RTX 4070 with 12 GB (driver 610.60). About 1.5 TB is free on the fast NVMe.

Use one tool per job. Pass one plugin id per enable or disable. A multi-id call stops at the first failure, so later ids never run.

```powershell
openclaw plugins enable <id>
openclaw plugins disable <id>
openclaw plugins install clawhub:<package>
openclaw mcp add <name> --command <exe> --arg <arg>
```

`openclaw plugins install clawhub:<package>` is the install form on the stable release. Enable the id only after install. If `plugins.allow` is set, it may contain only the keep ids below.

## Model

One Ollama model is loaded at a time. Set `OLLAMA_NUM_PARALLEL=1` and `OLLAMA_MAX_LOADED_MODELS=1`. `OLLAMA_MODELS` may point at a folder on the second NVMe before the first pull. Do not invent that path.

| Role | Tag | `num_ctx` | `num_gpu` | `num_thread` | `keep_alive` |
|---|---|---:|---:|---:|---|
| Chat. All layers on the GPU | [`qwen3.5:9b`](https://ollama.com/library/qwen3.5:9b) | 32768 | 999 | unset | `30m` |
| Chat while ComfyUI holds the GPU | [`qwen3.5:4b`](https://ollama.com/library/qwen3.5:4b) | 16384 | 0 | 8 | `5m` |
| Deep thinking only. GPU plus RAM | [`qwen3.8:27b`](https://ollama.com/library/qwen3.8:27b) | 8192 | -1 | 8 | `5m` |

`qwen3.5:9b` and `qwen3.5:4b` are Apache-2.0 vision models, about 6.6–7.6 GB and 3.3–4.0 GB on disk. `num_gpu` 999 asks Ollama for every layer on the RTX 4070. After a 9B load, `/api/ps` `size_vram` must cover the loaded model. If it does not, the GPU is busy: unload and retry, or use the 4B row.

`qwen3.8:27b` is about 18 GB on disk (about 16 GB of Q4_K_M weights plus a 0.9 GB projector). `num_gpu` -1 lets Ollama fill the 12 GB GPU and spill the rest into the 64 GB RAM. Expect a few tokens per second. Use it only when the user asks for deep thinking, a background job that can wait, or another local pass after `qwen3.5:9b` failed a complex reasoning task. Never use it for ordinary chat, tool chatter, or an OpenCode loop. Never use it while ComfyUI is running. Pull it only for that job. When the job ends, unload it with `keep_alive` 0 and return chat to `qwen3.5:9b`.

If `qwen3.5:9b` is missing and ComfyUI is stopped, chat may use `qwen3.5:4b` with `num_ctx` 32768, `num_gpu` 999, and `keep_alive` `30m`. The `num_gpu` 0 row is only for while ComfyUI holds the GPU.

Set the provider to Ollama, **Local only**, base URL `http://127.0.0.1:11434` with no `/v1`. Before `qwen3.5:9b` is primary, `/api/show` must report tool support and at least 16K context. If it does not, say so. Do not select a cloud model.

```powershell
ollama pull qwen3.5:9b
openclaw models set ollama/qwen3.5:9b
```

`llm-task` defaults to the 9B tag. Select `ollama/qwen3.8:27b` only under the deep-thinking rule.

```powershell
openclaw config set plugins.entries.llm-task.llm.allowedCompletionModels '["ollama/qwen3.5:9b","ollama/qwen3.5:4b","ollama/qwen3.8:27b"]'
openclaw config set plugins.entries.llm-task.config.defaultProvider ollama
openclaw config set plugins.entries.llm-task.config.defaultModel qwen3.5:9b
```

Setup: [Ollama](https://docs.openclaw.ai/providers/ollama/setup). Releases: [2026.11.6](https://github.com/openclaw/openclaw/releases/tag/v2026.11.6).

## Plugins to enable

Bundled ids, one command each. Skip an id that `openclaw plugins list` already shows as enabled.

`ollama` `memory-core` `memory-wiki` `workboard` `policy` `oc-path` `llm-task` `code-mode-quickjs` `imap` `github` `browser` `document-extract` `file-transfer` `web-readability` `device-pair` `tts-local-cli` `talk-voice` `cua-computer`

Install these three, then enable the id:

```powershell
openclaw plugins install clawhub:@openclaw/acpx
openclaw plugins enable acpx
openclaw plugins install clawhub:@openclaw/searxng-plugin
openclaw plugins enable searxng
openclaw plugins install clawhub:@openclaw/comfy-provider
openclaw plugins enable comfy
```

| Id | Call it for |
|---|---|
| `ollama` | Every chat, tool, and vision turn |
| `acpx` | Coding sessions. Agent id `opencode` only |
| `memory-core` | `memory_search` and `memory_get` |
| `memory-wiki` | Durable project pages |
| `workboard` | Task owner and status for the main agent |
| `policy` | Doctor checks. Leave automatic repair off |
| `oc-path` | `oc://` workspace paths |
| `llm-task` | One JSON completion with no tools |
| `code-mode-quickjs` | Local QuickJS |
| `imap` | Watch a mailbox after the user connects it |
| `github` | Public repository reads |
| `browser` | Open a page or a sign-in handoff |
| `document-extract` | Text from a local attachment |
| `file-transfer` | Files on a paired node |
| `web-readability` | Readable text after a fetch |
| `device-pair` | Pair a node |
| `tts-local-cli` | Local speech command |
| `talk-voice` | Which local voice is selected |
| `cua-computer` | The `computer` tool on Windows |
| `searxng` | `web_search` against loopback SearXNG |
| `comfy` | `image_generate` on a local ComfyUI |

Inventory: [plugins](https://docs.openclaw.ai/plugins/plugin-inventory). Install syntax: [install](https://docs.openclaw.ai/cli/plugins/install).

## Plugins to leave disabled

Disable a listed id only when `openclaw plugins list` shows it. One id per command. Do not install any other provider.

Cloud or paid inference, speech, image, and video: `openai` `google` `xai` `anthropic` `qwen` `alibaba` `minimax` `nvidia` `together` `huggingface` `microsoft-foundry` `github-copilot` `copilot-proxy` `openrouter` `clawrouter` `litellm` `fal` `kie` `runway` `azure-speech` `elevenlabs` `microsoft` `deepgram` `senseaudio`

Other local inference runtimes: `lmstudio` `vllm` `sglang` `llama-cpp` `omlx`

Other coding or memory paths: `opencode` `opencode-go` `active-memory`

Wrong host or unused here: `linux-node` `canvas` `crabbox` `onepassword` `vault`

`vault` is the HashiCorp Vault SecretRef plugin. Leave it disabled. It does not talk to a desktop password manager. `canvas` targets paired macOS panels. `opencode` is the hosted OpenCode model provider. The coding plugin is `acpx`.

Do not install `duckduckgo`, Brave, Exa, Tavily, Firecrawl, or Perplexity. SearXNG is the only search provider. If `duckduckgo` is installed and enabled, disable it.

## Tools you call

| Job | Call | If it is missing |
|---|---|---|
| Web search | `web_search` via `searxng` at `http://127.0.0.1:8888` | Say search is unavailable. [SearXNG plugin](https://docs.openclaw.ai/tools/searxng-search) |
| Page DOM | Playwright MCP server `playwright` | Say browser automation is unavailable |
| Sign-in page | `browser` | Say the browser tool is unavailable |
| Desktop | `computer` after `cua-computer` is enabled | Say desktop control is unavailable. [Computer use](https://docs.openclaw.ai/nodes/computer-use) |
| Speech to text | inbound audio through `whisper-cli` | Say transcription is unavailable. [Audio](https://docs.openclaw.ai/nodes/audio) |
| Speech | `tts` through `tts-local-cli` | Say speech is unavailable |
| Images | `image_generate` through local `comfy` | Say image generation is unavailable. [ComfyUI](https://docs.openclaw.ai/providers/comfy) |
| New office file | `workspace_create_file` | Say file creation is unavailable |
| Read a document | `document-extract` | Say extraction is unavailable |
| Calendar draft | `skills/local-productivity` script | Say the draft script is unavailable |

Playwright is the DOM tool. The `browser` tool is the sign-in handoff. The `computer` tool is the Windows desktop. Do not drive one job through two of them.

```powershell
openclaw mcp add playwright --command npx --arg -y --arg @playwright/mcp@latest
openclaw mcp list
```

[MCP](https://docs.openclaw.ai/tools/mcp). [Playwright MCP](https://github.com/microsoft/playwright-mcp). If `npx` is missing, say so.

```powershell
openclaw config set tools.web.search.provider searxng
openclaw config set plugins.entries.searxng.config.webSearch.baseUrl "http://127.0.0.1:8888"
```

The loopback server is `docker run -d -p 8888:8080 searxng/searxng` from [searxng/searxng](https://github.com/searxng/searxng). If that port is closed, say search is unavailable.

The GPU runs one heavy job. `qwen3.5:9b` may share it with whisper `ggml-small` only. ComfyUI and `qwen3.8:27b` each need the GPU alone. CPU offload and whisper use 8 threads, the performance cores on this i9-14900F. Do not set those jobs to 32 threads.

Transcription uses `whisper-cli` from [whisper.cpp](https://github.com/ggml-org/whisper.cpp) and `ggml-small.bin` (466 MiB on disk, about 852 MB in memory). That size fits beside `qwen3.5:9b`. Do not load `ggml-medium` (1.5 GiB) or a larger whisper model beside the LLM or ComfyUI. Pass `--threads 8`. Pass `--no-gpu` while ComfyUI is running or `qwen3.8:27b` is loaded. `ffmpeg` decodes files that are not 16-bit WAV. If `whisper-cli` or the small model is missing, say transcription is unavailable. Leave cloud audio providers disabled.

ComfyUI stays on loopback. Unload Ollama (`keep_alive` 0) before an image. The workflow loads Stability SDXL base 1.0, file `sd_xl_base_1.0.safetensors`, fp16 ([model card](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0)). Use 1024×1024, batch size 1, 20–30 steps, and `--normalvram`. Do not pass `--highvram`. Do not load a second checkpoint in the same graph. Flux is allowed only as a GGUF Q4 or Q5 after Ollama is unloaded. Full Flux weights do not fit in 12 GB. Leave cloud mode unset. While ComfyUI holds the GPU, chat uses the 4B row above, and whisper stays on the CPU.

```powershell
openclaw config set plugins.entries.comfy.config.mode local
openclaw config set plugins.entries.comfy.config.baseUrl "http://127.0.0.1:8188"
```

## Coding

Install the current `@opencode/cli`. Leave the archived `opencode-ai` package unused. Point OpenCode at Ollama and deny every other provider ([models](https://opencode.ai/docs/models/), [policies](https://opencode.ai/docs/policies/)):

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "model": "ollama/qwen3.5:9b",
  "policies": [
    { "action": "provider.use", "resource": "*", "effect": "deny" },
    { "action": "provider.use", "resource": "ollama", "effect": "allow" }
  ]
}
```

```powershell
openclaw config set acp.backend acpx
openclaw config set acp.defaultAgent opencode
openclaw config set acp.allowedAgents '["opencode"]'
openclaw config set plugins.entries.acpx.config.probeAgent opencode
```

Spawn agent id `opencode` only. OpenCode stays on `ollama/qwen3.5:9b`. One generation at a time, because `OLLAMA_NUM_PARALLEL` is 1. [ACP setup](https://docs.openclaw.ai/tools/acp-agents-setup). Health checks default to `codex` when `allowedAgents` is empty, so set `probeAgent` to `opencode` before `/acp doctor`.

## Delivery and secrets

Cron and owner-only commands need `commands.ownerAllowFrom` or a paired channel owner. Ask the user for that id in the session. Never write it into this repository. If it is unset, say scheduled delivery is unavailable.

Keep passwords, tokens, card numbers, and codes out of chat, screenshots, and logs. The user types them into the provider page or a local secret store. Do not ask for them.

## Check

```powershell
openclaw --version
openclaw gateway status
openclaw plugins list
openclaw mcp list
openclaw models list --provider ollama
python tools/check_workspace.py
```

`tools/check_workspace.py` is read-only. It passes only when Ollama lists `qwen3.5:9b`, the Gateway service is running, authenticated health succeeds, and a Windows node is paired. Until then it exits 1. That failure is the expected result on this fresh PC.

Capability choices: [docs/ASSISTANT_CAPABILITIES.md](docs/ASSISTANT_CAPABILITIES.md). Why these tools: [docs/DEPENDENCY_REVIEW.md](docs/DEPENDENCY_REVIEW.md). Desktop calls: [docs/WINDOWS_COMPUTER_CONTROL.md](docs/WINDOWS_COMPUTER_CONTROL.md). Rules: [REQUIREMENTS.md](REQUIREMENTS.md).
