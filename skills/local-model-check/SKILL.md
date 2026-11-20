---
name: local-model-check
description: Check loopback Ollama for qwen3.5:9b, the 4B fallback, and which model is loaded. Use when a reply is missing or slow.
---

Read the three loopback endpoints separately. One failure must not hide the others.

```powershell
$base = 'http://127.0.0.1:11434/api'
(Invoke-RestMethod "$base/version" -TimeoutSec 5).version
(Invoke-RestMethod "$base/tags" -TimeoutSec 5).models | Select-Object name, size
(Invoke-RestMethod "$base/ps" -TimeoutSec 5).models | Select-Object name, size_vram, expires_at
```

Report whether the port answered, whether `qwen3.5:9b` is present, and whether `qwen3.5:4b` is present. Name the loaded model. Empty residency after idle time is normal. The primary tag is `qwen3.5:9b`. Use `qwen3.5:4b` only when the 9B tag is absent or ComfyUI is using the GPU. `qwen3.8:27b` does not fit this 12 GB GPU.

These calls only read the service. If the port is closed, say Ollama is not running and point at the model section of README.md. Leave pulls and restarts for a separate user request.
