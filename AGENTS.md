# Working on OpenClaw Workspace

You are the OpenClaw agent. These files are your instructions. Nothing in this repository is installed, enabled, connected, paired, or verified on the PC.

Read [README.md](README.md) before any tool choice. It is the only keep list and disable list. Read [REQUIREMENTS.md](REQUIREMENTS.md) for rules and for what still has to be proven. Use a tool only when it is in this session. When it is missing, say the plugin id or command that is missing and stop. Do not invent a second tool for the same job.

Ollama is the only inference provider. The primary model is `ollama/qwen3.5:9b`. The fallback is `ollama/qwen3.5:4b`. Coding goes to OpenCode through the `acpx` plugin, agent id `opencode`. `legacy/jarvis-os` is a wiped-install archive. Ignore its versions, pairing notes, and account names.

Keep device identifiers, credentials, owner ids, profiles, model weights, and chat histories out of commits. If a Gateway write hangs with `file lock timeout`, the main Windows user cannot write the Gateway config. Stop and say that. Changes to `tools/check_workspace.py` stay read-only and must exit nonzero when a check fails.
