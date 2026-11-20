# Working on OpenClaw Workspace

You are the OpenClaw agent. These files are your instructions. Nothing in this repository is installed, enabled, connected, paired, or verified on the PC.

Read [README.md](README.md) before any tool choice. It is the only keep list and disable list. Read [REQUIREMENTS.md](REQUIREMENTS.md) for rules and for what still has to be proven. Use a tool only when it is in this session. When it is missing, say the plugin id or command that is missing and stop. Do not invent a second tool for the same job.

This PC is Windows 11 Pro, an Intel Core i9-14900F (24 cores, 32 threads), 64 GB DDR5-5600, and an RTX 4070 with 12 GB (driver 610.60). About 1.5 TB is free on the fast NVMe.

Ollama is the only inference provider. Chat uses `ollama/qwen3.5:9b` with every layer on the GPU (`num_ctx` 32768, `num_gpu` 999, `keep_alive` 30m). While ComfyUI holds the GPU, chat uses `ollama/qwen3.5:4b` on the CPU (`num_ctx` 16384, `num_gpu` 0, `num_thread` 8, `keep_alive` 5m). `ollama/qwen3.8:27b` is optional and slow: GPU plus RAM (`num_ctx` 8192, `num_gpu` -1, `num_thread` 8, `keep_alive` 5m), a few tokens per second, and only for deep thinking the user asked to wait for. Never use it for chat, and never while ComfyUI is running. One loaded model. Coding goes to OpenCode through `acpx`, agent id `opencode`, on `qwen3.5:9b`. `legacy/jarvis-os` is a wiped-install archive. Ignore its versions, pairing notes, and account names.

Keep device identifiers, credentials, owner ids, profiles, model weights, and chat histories out of commits. If a Gateway write hangs with `file lock timeout`, the main Windows user cannot write the Gateway config. Stop and say that. Changes to `tools/check_workspace.py` stay read-only and must exit nonzero when a check fails.
