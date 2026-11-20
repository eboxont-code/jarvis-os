# Tool decisions

Checked 2026-11-20. Nothing is installed. [README.md](../README.md) is the list you enable. This file is why.

This PC is Windows 11 Pro, an Intel Core i9-14900F (24 cores, 32 threads), 64 GB DDR5-5600, and an RTX 4070 with 12 GB (driver 610.60). About 1.5 TB is free on the fast NVMe.

## Model

| Tag | On disk | Settings | Decision |
|---|---|---|---|
| `qwen3.5:9b` | 6.6–7.6 GB | `num_ctx` 32768, `num_gpu` 999, `keep_alive` 30m | Chat. Every layer on the GPU. [Library](https://ollama.com/library/qwen3.5:9b) |
| `qwen3.5:4b` | 3.3–4.0 GB | `num_ctx` 16384, `num_gpu` 0, `num_thread` 8, `keep_alive` 5m | Chat while ComfyUI holds the GPU. If the 9B tag is missing and ComfyUI is stopped, use `num_ctx` 32768 and `num_gpu` 999 instead. [Library](https://ollama.com/library/qwen3.5:4b) |
| `qwen3.8:27b` | about 18 GB | `num_ctx` 8192, `num_gpu` -1, `num_thread` 8, `keep_alive` 5m | Optional deep thinking. Ollama fills the 12 GB GPU and spills the rest into the 64 GB RAM. A few tokens per second. Not for chat. Not while ComfyUI is running. [Library](https://ollama.com/library/qwen3.8:27b) |

`num_gpu` 999 requests every layer. `num_gpu` -1 is Ollama's dynamic split. `num_gpu` 0 keeps the model in RAM. One loaded model: `OLLAMA_NUM_PARALLEL=1`, `OLLAMA_MAX_LOADED_MODELS=1`. `OLLAMA_MODELS` may point at the second NVMe. Confirm tools and at least 16K context with `/api/show` before the 9B tag is primary. Stable OpenClaw on this date is [2026.11.6](https://github.com/openclaw/openclaw/releases/tag/v2026.11.6).

## One tool per job

| Job | Keep | Leave unused |
|---|---|---|
| Inference | `ollama` | `openai`, `google`, `xai`, `anthropic`, `qwen`, `lmstudio`, `vllm`, `sglang`, `llama-cpp`, `omlx`, and the other paid provider ids in README |
| Coding | `acpx` agent `opencode` | `opencode` provider, `opencode-go`, Codex, Claude, Copilot, Cursor, Grok |
| Search | `searxng` | `duckduckgo` and other hosted search plugins |
| Page text | `web-readability` | A second reader |
| Page DOM | Playwright MCP | A second browser-automation server |
| Sign-in | `browser` | — |
| Desktop | `cua-computer` (`computer`) | pywinauto, FlaUI, and cloud computer sessions |
| Speech to text | `whisper-cli` with `ggml-small` (466 MiB, about 852 MB) | `ggml-medium` and larger beside the LLM or ComfyUI; Deepgram, OpenAI, Groq, and other hosted audio providers |
| Speech | `tts-local-cli` | `azure-speech`, `elevenlabs`, `microsoft`, `deepgram` |
| Images | `comfy` local, SDXL base 1.0 fp16, 1024×1024, batch 1, `--normalvram` | `fal`, `kie`, `runway`, Comfy cloud, `--highvram`, a second checkpoint, full-precision Flux |
| Recall | `memory-core` | `active-memory` |
| Pages | `memory-wiki` | — |
| Tasks | `workboard` | A second tracker |
| Mail watch | `imap` | A desktop mail client |
| Secrets | User-typed on the provider page | `vault`, `onepassword` |
| Node | `device-pair` | `linux-node`, `canvas` |

`cua-computer` is the bundled Windows computer provider. Enable it. The old disable list treated it as a duplicate. It is the desktop tool.

`vault` stays off because it expects HashiCorp Vault, which this agent does not call.

SDXL base 1.0 fp16 is the image default ([model card](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0)): 1024×1024, batch 1, 20–30 steps, `--normalvram`, one checkpoint. Unload Ollama first. A Flux checkpoint is allowed only as a GGUF Q4 or Q5 after that unload. [ComfyUI provider](https://docs.openclaw.ai/providers/comfy). Whisper `ggml-small` may share the GPU with `qwen3.5:9b` only. CPU offload and whisper use 8 threads on this 24-core CPU.

## Not verified from this session

- A live `openclaw plugins enable` on Windows. The syntax is the published CLI: one id, and `clawhub:` installs.
- A live `/api/ps` reading for `qwen3.5:9b` at `num_ctx` 32768. The published file size fits in 12 GB. Confirm `size_vram` after the first load on this PC.
- Whether `/api/show` on the pulled 9B tag advertises tools. Do not keep it as primary if it does not.
- The `clawctl.exe` path inside `tools/check_workspace.py`. It targets the Store Gateway package name already in that file.
