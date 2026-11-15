# OpenJarvis read-only MCP adapter — design boundary

**Status:** Design only. No adapter process, MCP server, OpenClaw configuration or OpenJarvis configuration has been enabled by this document.

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
