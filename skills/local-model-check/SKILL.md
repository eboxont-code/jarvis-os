---
name: local-model-check
description: Diagnose slow or missing local OpenClaw replies by checking Ollama version, installed tags and model residency on this Windows Gateway.
---

Use this for a local model timeout, missing model or a quick inference-service check. Use the authorised local PowerShell tool in the Gateway environment. Read the three loopback endpoints separately so a failed check does not hide the others.

~~~powershell
$base = 'http://127.0.0.1:11434/api'
(Invoke-RestMethod "$base/version" -TimeoutSec 5).version
(Invoke-RestMethod "$base/tags" -TimeoutSec 5).models | Select-Object name, size
(Invoke-RestMethod "$base/ps" -TimeoutSec 5).models | Select-Object name, size_vram, expires_at
~~~

Report whether the endpoint answered, whether the workspace default qwen3.8:27b is installed, and which model is loaded. Empty residency can be normal after idle time. These reads verify service availability only. Report any failed request or unavailable tool. Leave downloads, settings and service restarts to a separate user request.
