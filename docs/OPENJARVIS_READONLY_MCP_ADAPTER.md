# OpenJarvis read-only MCP adapter — design boundary

**Scope:** technical design and verification record; `MASTER_TODO.md` is the sole status authority.

## 18 November 2026 transport and deployment correction

The original adapter incorrectly used LSP-style Content-Length headers. Standard MCP stdio requires one UTF-8 JSON-RPC message per newline ([official transport specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports)). The adapter now reads bounded newline messages and writes newline JSON. Seven regression tests pass, including real subprocess initialize/notification/discovery, malformed-frame recovery and oversized-frame rejection. Tests also resolve the repository's runtime source correctly.

A fresh OpenClaw discovery attempt from the Boxont Documents scratch directory failed with EPIPE. A supported `clawctl pwsh --command` read-only check established that the isolated account can run the existing `C:\Python314\python.exe` but cannot read that Boxont adapter path. The corrected adapter was therefore copied into the existing supported shared workspace at `C:\Users\T3-P2\Shared\jarvis-readonly-mcp-20261118\openjarvis_readonly_mcp_adapter.py`; no ACL, profile, managed Node runtime or Gateway/Companion change was made. Host and isolated account SHA-256 read-backs matched.

From that shared path, `openclaw mcp add` and `mcp probe --json` exited 0 and discovered exactly the three tool names with no diagnostics, prompt approval and 10-second timeouts. The temporary registration was removed; `mcp list` confirmed cleanup. All seven tests and a real stdio initialize/list/three-call sequence also passed under the isolated account, reaching the live OpenJarvis/Ollama services. This proves discovery and standalone isolated-account calls; a Gateway agent-routed call and persistent registration are separate acceptance evidence recorded in the master.

The user has revoked the blanket official-repair waiting gate and approved retaining the tested read-only connection. Follow the current master for registration state; historical dated handoffs do not override this newer directive.

## Why a separate adapter

The installed OpenJarvis release contains an internal `MCPServer`, but its default auto-discovery includes capabilities that are too broad for the initial integration surface, including code execution, REPL, web search, memory writes and channel sending. The installed release source also did not expose a standalone server launch command or transport for safely publishing a reduced subset.

OpenJarvis *as an MCP client* supports stdio and Streamable HTTP, but this project must not infer that the desktop build can safely act as a restricted MCP server. A separate adapter keeps the integration outside the preserved OpenJarvis checkout and avoids changing its settings.

## First implementation boundary

The first adapter must be a small local **stdio** MCP process in the JARVIS project workspace. It is not an HTTP listener, Windows service, scheduled task, background daemon, installer or replacement desktop build.

It may communicate only with these fixed loopback endpoints:

- `http://127.0.0.1:8000/health`
- `http://127.0.0.1:8000/v1/info`
- `http://127.0.0.1:8000/v1/models`
- `http://127.0.0.1:11434/api/version`
- `http://127.0.0.1:11434/api/tags`
- `http://127.0.0.1:11434/api/ps`

The adapter must reject any caller-supplied URL, host, port, path, shell command, file path, model prompt or tool payload.

## Initial tool whitelist

Only these tools may be implemented initially:

| Tool | Result | Prohibited behavior |
|---|---|---|
| `openjarvis_health` | OpenJarvis health plus the safe fields from `/v1/info`. | No chat completion, memory access, settings read/write or restart. |
| `openjarvis_models` | Model IDs from OpenJarvis and Ollama, marked only as matching or differing. | No model pull, delete, load request or configuration change. |
| `openjarvis_runtime_status` | Fixed-endpoint reachability, Ollama version and loaded-model name/context. | No process enumeration, port ownership, process termination or network access beyond the fixed loopback calls. |

The tools must return structured status/error data; they must not throw raw endpoint responses or log whole HTTP bodies. They must use short bounded timeouts and report unavailable services as a normal failure result.

## Hard exclusions

The first adapter must never expose:

- OpenJarvis's built-in MCP auto-discovery.
- Shell, PowerShell, REPL, code-interpreter, arbitrary process or Windows-control tools.
- File read/write, directory enumeration, database access or configuration access.
- Memory store/index/retrieve/search.
- Web search, HTTP requests to non-loopback destinations or browser control.
- Channel, message, email, calendar, contact or connector tools.
- Model prompting, chat completion, embedding, inference configuration or model lifecycle actions.
- Credentials, tokens, pairing data, logs, telemetry, raw process metadata or user content.

## Security and reliability requirements

- Bind no port; use MCP stdio only.
- Treat stdin requests as untrusted. Validate tool names and schema; reject unknown fields.
- Do not read environment variables other than an optional explicitly documented test-mode flag. Do not accept endpoint overrides.
- Use fixed 5-second or shorter endpoint timeouts.
- Redact errors to endpoint name, status class and bounded reason; never return headers or secrets.
- Emit an audit event containing tool name, timestamp, outcome and duration only.
- Exit cleanly on parent stdin closure. Do not restart OpenJarvis, Ollama, Gateway or Companion.
- Run under normal-user privilege only.

## Verification before configuration

Before the adapter is registered with any coordinator:

1. Unit-test input validation and all hard rejections.
2. Run it against local fixture responses, including timeouts and malformed JSON.
3. Launch it manually over stdio in an isolated workspace and verify that only the three whitelisted tools are listed.
4. With the existing applications running, verify all three tools return safe data and do not modify protected configuration hashes.
5. Stop the adapter and verify ordinary OpenJarvis chat and Ollama health remain unaffected.
6. Review its source and test logs independently.
7. Only then request explicit approval to add a temporary OpenClaw MCP configuration. Native Companion remains out of scope while its ownership/credential-handoff issue is blocked pending an official reviewed stable fix.

## Rollback

No runtime rollback is needed during the design stage. Once implemented, rollback is removing the adapter's temporary working directory/registration only after verification that no running child process remains. Do not modify or restore OpenJarvis, Ollama, Gateway or Companion files as part of adapter rollback.
