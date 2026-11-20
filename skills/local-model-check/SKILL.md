---
name: local-model-check
description: Check Ollama for qwen3.5:9b on the GPU and the optional qwen3.8:27b offload. Use when a reply is missing or the GPU is busy.
---

This PC is Windows 11 Pro, an Intel Core i9-14900F (24 cores, 32 threads), 64 GB DDR5-5600, and an RTX 4070 with 12 GB (driver 610.60). About 1.5 TB is free on the fast NVMe.

Read the three loopback endpoints separately. One failure must not hide the others.

```powershell
$base = 'http://127.0.0.1:11434/api'
(Invoke-RestMethod "$base/version" -TimeoutSec 5).version
(Invoke-RestMethod "$base/tags" -TimeoutSec 5).models | Select-Object name, size
(Invoke-RestMethod "$base/ps" -TimeoutSec 5).models | Select-Object name, size, size_vram, expires_at
```

Report whether the port answered and whether `qwen3.5:9b` and `qwen3.8:27b` are present. Name the loaded model. These are the only two tags. For `qwen3.5:9b`, `size_vram` must cover the loaded model (`num_ctx` 32768, `num_gpu` 999, `keep_alive` 30m). If the GPU is busy, queue chat and other LLM work until it is free.

`qwen3.8:27b` is optional. Settings are `num_ctx` 8192, `num_gpu` -1, `num_thread` 8, and `keep_alive` 5m. It splits across the 12 GB GPU and the 64 GB RAM and runs at a few tokens per second. Use it only for deep thinking the user will wait for. Never for ordinary chat, and never while ComfyUI is running. While it is loaded, queue other chat and LLM work.

Empty residency after idle time is normal. These calls only read the service. If the port is closed, say Ollama is not running and point at the model section of README.md. Leave pulls and restarts for a separate user request.
