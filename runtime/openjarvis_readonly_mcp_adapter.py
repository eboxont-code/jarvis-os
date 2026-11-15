#!/usr/bin/env python3
"""A deliberately small, local-only read-only MCP adapter for OpenJarvis.

This program is not registered by OpenJarvis or OpenClaw.  It speaks MCP's
stdio framing protocol and permits only fixed loopback status queries.
"""

from __future__ import annotations

import json
import sys
import time
import urllib.error
import urllib.request
from typing import Any, Callable


PROTOCOL_VERSION = "2025-11-25"
TIMEOUT_SECONDS = 5
MAX_RESPONSE_BYTES = 1_000_000

OPENJARVIS_HEALTH = "http://127.0.0.1:8000/health"
OPENJARVIS_INFO = "http://127.0.0.1:8000/v1/info"
OPENJARVIS_MODELS = "http://127.0.0.1:8000/v1/models"
OLLAMA_VERSION = "http://127.0.0.1:11434/api/version"
OLLAMA_TAGS = "http://127.0.0.1:11434/api/tags"
OLLAMA_PS = "http://127.0.0.1:11434/api/ps"


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):  # type: ignore[no-untyped-def]
        return None


_OPENER = urllib.request.build_opener(NoRedirect())


def audit(tool: str, outcome: str, duration_ms: int) -> None:
    print(
        json.dumps({"event": "openjarvis_readonly_mcp", "tool": tool,
                    "outcome": outcome, "duration_ms": duration_ms}),
        file=sys.stderr,
        flush=True,
    )


def get_json(url: str) -> dict[str, Any]:
    """Fetch a fixed loopback endpoint, returning only JSON object responses."""
    request = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with _OPENER.open(request, timeout=TIMEOUT_SECONDS) as response:
            body = response.read(MAX_RESPONSE_BYTES + 1)
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as error:
        raise RuntimeError("endpoint_unavailable") from error
    if len(body) > MAX_RESPONSE_BYTES:
        raise RuntimeError("response_too_large")
    try:
        decoded = json.loads(body.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise RuntimeError("invalid_json") from error
    if not isinstance(decoded, dict):
        raise RuntimeError("unexpected_response")
    return decoded


def safe_call(name: str, action: Callable[[], dict[str, Any]]) -> dict[str, Any]:
    started = time.monotonic()
    try:
        result = action()
    except RuntimeError as error:
        audit(name, str(error), int((time.monotonic() - started) * 1000))
        return {"available": False, "reason": str(error)}
    audit(name, "ok", int((time.monotonic() - started) * 1000))
    return {"available": True, **result}


def health() -> dict[str, Any]:
    return safe_call(
        "openjarvis_health",
        lambda: {
            "health": get_json(OPENJARVIS_HEALTH).get("status"),
            "runtime": {
                key: get_json(OPENJARVIS_INFO).get(key)
                for key in ("model", "agent", "engine")
            },
        },
    )


def model_ids(value: dict[str, Any]) -> list[str]:
    candidates = value.get("data", value.get("models", []))
    if not isinstance(candidates, list):
        return []
    result: list[str] = []
    for item in candidates:
        if isinstance(item, dict):
            name = item.get("id", item.get("name"))
            if isinstance(name, str):
                result.append(name)
    return sorted(set(result))


def models() -> dict[str, Any]:
    def query() -> dict[str, Any]:
        openjarvis = model_ids(get_json(OPENJARVIS_MODELS))
        ollama = model_ids(get_json(OLLAMA_TAGS))
        return {
            "openjarvis_models": openjarvis,
            "ollama_models": ollama,
            "matching": openjarvis == ollama,
        }

    return safe_call("openjarvis_models", query)


def runtime_status() -> dict[str, Any]:
    def query() -> dict[str, Any]:
        loaded = get_json(OLLAMA_PS).get("models", [])
        safe_loaded: list[dict[str, Any]] = []
        if isinstance(loaded, list):
            for item in loaded:
                if isinstance(item, dict):
                    safe_loaded.append({
                        key: item.get(key)
                        for key in ("name", "context_length")
                    })
        return {"ollama_version": get_json(OLLAMA_VERSION).get("version"),
                "loaded_models": safe_loaded}

    return safe_call("openjarvis_runtime_status", query)


TOOLS = {
    "openjarvis_health": {
        "description": "Read fixed-loopback OpenJarvis health and safe runtime fields.",
        "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
        "handler": health,
    },
    "openjarvis_models": {
        "description": "Compare only model identifiers reported by fixed-loopback services.",
        "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
        "handler": models,
    },
    "openjarvis_runtime_status": {
        "description": "Read Ollama version and loaded model names/context from fixed-loopback endpoints.",
        "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
        "handler": runtime_status,
    },
}


def result(request_id: Any, payload: dict[str, Any]) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": request_id, "result": payload}


def error(request_id: Any, code: int, message: str) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": request_id,
            "error": {"code": code, "message": message}}


def handle(request: dict[str, Any]) -> dict[str, Any] | None:
    request_id = request.get("id")
    method = request.get("method")
    if method == "notifications/initialized":
        return None
    if method == "initialize":
        return result(request_id, {
            "protocolVersion": PROTOCOL_VERSION,
            "serverInfo": {"name": "jarvis-openjarvis-readonly", "version": "0.1.0"},
            "capabilities": {"tools": {}},
        })
    if method == "tools/list":
        return result(request_id, {"tools": [
            {"name": name, "description": spec["description"], "inputSchema": spec["inputSchema"]}
            for name, spec in TOOLS.items()
        ]})
    if method == "tools/call":
        params = request.get("params")
        if not isinstance(params, dict):
            return error(request_id, -32602, "invalid_params")
        name = params.get("name")
        arguments = params.get("arguments", {})
        if name not in TOOLS or not isinstance(arguments, dict) or arguments:
            return error(request_id, -32602, "tool_or_arguments_not_allowed")
        data = TOOLS[name]["handler"]()
        return result(request_id, {"content": [{"type": "text", "text": json.dumps(data, sort_keys=True)}],
                                   "isError": not data["available"]})
    return error(request_id, -32601, "method_not_found")


def read_message(stream: Any) -> dict[str, Any] | None:
    headers: dict[str, str] = {}
    while True:
        line = stream.readline()
        if not line:
            return None
        if line in (b"\r\n", b"\n"):
            break
        key, separator, value = line.decode("ascii").partition(":")
        if not separator:
            raise ValueError("invalid_header")
        headers[key.lower()] = value.strip()
    length = int(headers.get("content-length", "-1"))
    if length < 0 or length > MAX_RESPONSE_BYTES:
        raise ValueError("invalid_content_length")
    payload = stream.read(length)
    parsed = json.loads(payload.decode("utf-8"))
    if not isinstance(parsed, dict):
        raise ValueError("invalid_request")
    return parsed


def write_message(stream: Any, payload: dict[str, Any]) -> None:
    body = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    stream.write(f"Content-Length: {len(body)}\r\n\r\n".encode("ascii"))
    stream.write(body)
    stream.flush()


def main() -> int:
    while True:
        try:
            request = read_message(sys.stdin.buffer)
        except (ValueError, UnicodeDecodeError, json.JSONDecodeError):
            write_message(sys.stdout.buffer, error(None, -32700, "parse_error"))
            continue
        if request is None:
            return 0
        response = handle(request)
        if response is not None:
            write_message(sys.stdout.buffer, response)


if __name__ == "__main__":
    raise SystemExit(main())

