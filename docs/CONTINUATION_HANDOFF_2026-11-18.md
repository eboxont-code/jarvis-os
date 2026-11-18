# JARVIS Continuation Handoff — 2026-11-18

> **Historical snapshot — superseded for current continuation.** Read the complete current [master](../MASTER_TODO.md), then [the later autostart continuation handoff](CONTINUATION_HANDOFF_2026-11-18_AUTOSTART.md). The official-repair wait gate, unregistered MCP and ENOENT-only block below are earlier evidence, not current instructions. The user revoked the blanket wait gate; real MCP/ACP/native checks and an unattended stopped-stack startup subsequently passed. Actual Windows reboot/sign-in acceptance remains governed by the latest master. The original record below is preserved intact as history.

> **Purpose:** allow a new authorised AI session to continue the JARVIS project without relying on private chat history.
>
> **Authority:** [MASTER_TODO.md](../MASTER_TODO.md) remains the sole project plan and status authority. This document is a dated evidence and handoff record, not a competing checklist. Follow [AGENTS.md](../AGENTS.md) first.

## Mandatory safe session start

1. Confirm the repository is `eboxont-code/jarvis-os` and refresh `main`.
2. Read the **complete current** `AGENTS.md`, `MASTER_TODO.md`, and relevant linked documentation. Do not treat this dated handoff as newer authority.
3. Perform fresh, read-only checks of process, endpoint, model, and config state. Do not assume a process, port, or local workspace from this record still exists.
4. Select only the next eligible master task, mark it **WORKING** before changing project code, and leave no stale WORKING item at the end.
5. Preserve the zero-additional-spend rule and all protected installations/data/configuration. Record actual results, including failures, in the master execution log and read back the remote update.

## Non-negotiable boundaries

- $0 additional spend: no paid service, subscription, trial, credits, cloud inference, paid model/API/search service, or paid fallback.
- Do not download models, reinstall/reset/update OpenJarvis, reset/re-pair Gateway or Companion, change tokens, ACLs, security settings, or perform elevated/destructive actions without explicit user approval.
- Preserve all existing OpenJarvis custom source, settings, data, models, installation, and backups.
- The native OpenClaw Companion Node ownership/credential-handoff defect is **BLOCKED pending an official reviewed stable fix**. Do not use an alpha/pre-release, fabricate a missing runtime, override its path, change profiles, restart/reinstall/reset Gateway or Companion, or attempt a workaround.
- Do not write secrets, API keys, tokens, passwords, or private credentials to Git history, prompts, logs, or this document.

## GitHub anchor

At the start of this handoff, the remote master file was read at:

- `MASTER_TODO.md` blob SHA: `7e3e2e4a54636bca53cdcfe4460fa9dde7cf9c95`
- Last preceding evidence commit: `aeda4917bc2e4ea74b37ec2dc8679eed7a88809c` (direct local Ollama inference evidence)

Relevant recorded commits:

| Commit | Recorded outcome |
|---|---|
| `d9fef8b` | OpenJarvis recovery test verified |
| `4c873e0` | Read-only OpenJarvis MCP adapter verified |
| `8d82aba` | OpenClaw MCP discovery documented as blocked |
| `5ec65ab` | OpenCode local provider audit recorded |
| `06e2066` | Initial local model tool-call evidence |
| `a82e5ea` | qwen3.8:27b tool-call reliability evidence |
| `aeda491` | Direct Ollama local inference evidence |

## Verified local evidence at last observation

### Ollama and models

- Ollama endpoint: `http://127.0.0.1:11434`, loopback only; observed version `0.40.16`.
- Exact tags returned by the last `/api/tags` check: `qwen3.5:0.8b`, `qwen3.5:2b`, `qwen3.5:4b`, `qwen3.8:27b`.
- The previously seen `qwen3.5:9b` tag was not present in that later inventory and remains an unresolved inventory discrepancy; do not pull it.
- Direct `/api/chat` against `qwen3.5:4b` returned `DIRECT_OLLAMA_OK` in 5.75 seconds. No tool was executed.
- `qwen3.5:4b` advertises tools, but an inert tool-call prompt ended with `EOF`. It is **not** the tool-call default.
- `qwen3.8:27b` completed three inert calculator-schema calls with exact arguments: `2+3` (22.40 s cold), `7+8` (6.16 s), and `9+6` (4.28 s). Those tests only generated arguments; no tool execution occurred.
- Recorded hardware was an RTX 4070 with 12.282 GB VRAM. The 27b model used about 11.36–11.42 GB. Run heavy local jobs sequentially.

### OpenJarvis

- Backend was observed on `127.0.0.1:8000`; health returned `ok`.
- `/v1/info` reported active model `qwen3.5:4b`, agent `simple`, engine `multi`.
- Saved inference metadata still names `qwen3.8:27b`; this mismatch was observed only and intentionally not changed.
- OpenJarvis chat-completions with the 4b model returned `JARVIS_LOCAL_OK`, then `JARVIS_RECOVERY_OK` after the approved recovery test. Neither response made a tool call.
- Supported client-side MCP transports found in installed source: stdio and Streamable HTTP, with an allow-list filter. No existing MCP server section/registration was found in the active config.
- The built-in internal MCP surface was broad (including file, web, code, REPL, memory, and channel capabilities), so it is not an acceptable first exposed surface.

### OpenCode

- CLI observed at `C:\Users\Boxont\AppData\Roaming\npm\opencode.ps1`; version reporting was `2.2.6` in the last direct check, while earlier project evidence records `2.2.7` in the T3-P2 session. Recheck rather than reconcile by modifying anything.
- `C:\Users\Boxont\.config\opencode\opencode.json` contained only the local Ollama provider at `http://127.0.0.1:11434/v1`, primary `qwen3.8:27b`, small model `qwen3.5:4b`; no configured cloud provider or cloud credential was found.
- A bounded text-only local prompt returned `OPENCODE_LOCAL_OK` with exit 0. It did not auto-approve tools, files, or network work.

### OpenClaw

- The official stable Windows Gateway release observed was `v2026.11.1-msix.0`; installed Gateway MSIX was `2026.11.100.0` / payload `2026.11.1`.
- A newer Companion build, `v2026.11.2-alpha.10`, was pre-release only and was not installed.
- The native Node issue remained open upstream as OpenClaw Windows Node issue #1691. Treat an official reviewed stable repair as the prerequisite for any retry.
- With explicit temporary-test approval, static CLI help showed `openclaw mcp add` supports stdio command/arguments/tool include/approval and supports probing/reload/unset.
- The attempted non-persistent discovery of the repository read-only adapter was rejected before saving because OpenClaw tried to spawn:
  `C:\Users\T3-P2\AppData\Local\OpenClawGatewayMSIX\agent-node\node-v24.22.1-win-x64\node.exe`
  and received `ENOENT`.
- The active OpenClaw CLI resolved `C:\Users\T3-P2\.openclaw\openclaw.json`, an isolated T3-P2 profile. A read-only `openclaw mcp list` reported no managed server config there. Do not modify that profile to bridge the gap.

## Protected-config integrity evidence

No config content or secret values were recorded. The following SHA-256 values matched before and after the relevant tests:

| Protected file | SHA-256 |
|---|---|
| `.openjarvis\config.toml` | `73D448AE162E8B6D33B319F303971F0F5E3DB74B2F734BA831314D2A2A3AAD06` |
| `.openjarvis\inference.json` | `DE507DB5CB2F8F85AEC55A73DFCAC5C75EAD9C4D11CC610E9C38CE7D80FE7098` |
| `.config\opencode\opencode.json` | `B667A1591505F8603DCF12B58848AC66E66CFD327830605D22373E4D87692B7C` |
| `.openclaw\openclaw.json` | `58F24CA747FF50319293B418B0C83164817C9CD653C265C8492400A7C440E921` |

## Read-only OpenJarvis MCP adapter

The repository contains a deliberately small, unregistered adapter:

- [Design and verification document](OPENJARVIS_READONLY_MCP_ADAPTER.md)
- `runtime/openjarvis_readonly_mcp_adapter.py`
- `tests/test_openjarvis_readonly_mcp_adapter.py`

Its boundary is intentionally strict: stdio only; fixed loopback endpoints; exactly three no-argument tools (`openjarvis_health`, `openjarvis_models`, and `openjarvis_runtime_status`); redirect refusal; five-second HTTP timeout; no prompt handling, files, shell, processes, web, memory, or channels. Fixture/protocol tests, Python compilation, and live calls to all three tools passed. It is **not registered** in any active application configuration.

## Approved recovery evidence

The user explicitly approved restarting only Ollama and OpenJarvis for a recovery test.

- Closing the OpenJarvis desktop parent left backend Python PID 28692 on port 8000; the exact orphan was stopped, the port was verified free, and the user manually reopened the app.
- Closing the Ollama app parent left `ollama.exe` PID 23604 on port 11434; the exact orphan was stopped, the port was verified free, and the user manually reopened the app.
- The controlling automation could not relaunch the apps; the user did. Health subsequently passed after 15 seconds.
- No Gateway/Companion restart, pairing, token, ACL, model, or security change occurred.

For any future approved restart, verify exact descendants/listeners and port release before launching. Closing a parent window alone is insufficient.

## Current safe continuation point

The direct OpenClaw-to-OpenJarvis MCP connection is **BLOCKED**. Do not retry it until an official reviewed stable fix resolves the Companion/Gateway native Node ownership/credential handoff issue.

Until then, the next eligible work is limited to the non-destructive inventory/integration work already listed in the current master plan, such as fresh read-only state verification and documentation/evidence maintenance. Any attempt to change application configuration, run a Gateway/Companion repair, or resume MCP discovery requires both an official stable upstream fix and user approval appropriate to the action.

## Local-workspace caution

A prior incomplete local clone at `C:\Users\Boxont\Documents\Codex\2026-11-15\referenced-chatgpt-conversation-this-is-an\work\jarvis-os` was intentionally preserved after the clone did not finish. It is not an authoritative checkout and must not be reused, repaired, or deleted without a fresh read-only inspection and user direction. The GitHub repository is the current authoritative project record.

## What this handoff records

This entry consolidates meaningful project actions, verification results, failed/blocked attempts, preservation checks, and approval boundaries from the preceding session. Routine chat messages and tool mechanics are intentionally omitted; the linked master execution log remains the chronological record.
