# Tool decisions

Checked 2026-11-20. Nothing is installed. [README.md](../README.md) is the list you enable. This file is why.

## Model

| Tag | Decision |
|---|---|
| `qwen3.5:9b` | Primary. Apache-2.0, vision, about 6.6–7.6 GB on disk. Fits a 12 GB RTX 4070 and leaves room for context. [Library](https://ollama.com/library/qwen3.5:9b) |
| `qwen3.5:4b` | Fallback. Same family and licence, about 3.3–4.0 GB. Use it when the 9B tag is absent or ComfyUI holds the GPU. [Library](https://ollama.com/library/qwen3.5:4b) |
| `qwen3.8:27b` | Rejected for this GPU. Real tag, about 18 GB on disk (about 16 GB of Q4_K_M weights plus a 0.9 GB projector). It cannot reside in 12 GB. [Library](https://ollama.com/library/qwen3.8:27b) |

Confirm tools and at least 16K context with `/api/show` before a tag becomes primary. OpenClaw discovery requires both. Stable OpenClaw on this date is [2026.11.6](https://github.com/openclaw/openclaw/releases/tag/v2026.11.6).

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
| Speech to text | `whisper-cli` | Deepgram, OpenAI, Groq, and other hosted audio providers |
| Speech | `tts-local-cli` | `azure-speech`, `elevenlabs`, `microsoft`, `deepgram` |
| Images | `comfy` local, SDXL base 1.0 | `fal`, `kie`, `runway`, Comfy cloud, full-precision Flux |
| Recall | `memory-core` | `active-memory` |
| Pages | `memory-wiki` | — |
| Tasks | `workboard` | A second tracker |
| Mail watch | `imap` | A desktop mail client |
| Secrets | User-typed on the provider page | `vault`, `onepassword` |
| Node | `device-pair` | `linux-node`, `canvas` |

`cua-computer` is the bundled Windows computer provider. Enable it. The old disable list treated it as a duplicate. It is the desktop tool.

`vault` stays off because it expects HashiCorp Vault, which this agent does not call.

SDXL base 1.0 is the image default ([model card](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0)). A Flux checkpoint is allowed only as a GGUF Q4 or Q5 that fits beside the desktop. [ComfyUI provider](https://docs.openclaw.ai/providers/comfy).

## Not verified from this session

- A live `openclaw plugins enable` on Windows. The syntax is the published CLI: one id, and `clawhub:` installs.
- The VRAM reading while `qwen3.5:9b` is loaded at 32K context. The decision uses the published file size, which fits. A loaded-context measurement is still required on the PC.
- Whether `/api/show` on the pulled 9B tag advertises tools. Do not keep it as primary if it does not.
- The `clawctl.exe` path inside `tools/check_workspace.py`. It targets the Store Gateway package name already in that file.
