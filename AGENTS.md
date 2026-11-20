# Working on OpenClaw Workspace

OpenClaw owns the main conversation. Ollama runs local inference. OpenCode is the optional ACP coding backend. The Windows PC is a fresh install: nothing described in this repository is installed, enabled, connected, configured, paired, running, or done. Follow the fresh-install guide in README.md, then use REQUIREMENTS.md as the feature and acceptance checklist. Read both before selecting a task. Record verification against the OpenClaw stack after each step is actually completed. Treat legacy/jarvis-os as an archive of a wiped install. Ignore its version numbers, pairing notes, and account names.

Keep changes independent of a particular Windows username. If the Gateway runs in an isolated session, the main user must have write access to the Gateway config. Without that write access, CLI writes hang with "file lock timeout". Use supported OpenClaw commands for live checks. Keep device identifiers, credentials, saved profiles, model weights and chat histories out of commits. Changes to the status tool should preserve its read-only behavior and nonzero exit on failure.

Keep the workspace rules: zero additional cost, local first, Ollama only, and no paid cloud inference.
