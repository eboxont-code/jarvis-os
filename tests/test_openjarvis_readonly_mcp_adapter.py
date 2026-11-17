import importlib.util
import io
import json
import pathlib
import subprocess
import sys
import unittest
from unittest.mock import patch


MODULE_PATH = pathlib.Path(__file__).with_name("openjarvis_readonly_mcp_adapter.py")
if not MODULE_PATH.exists():
    MODULE_PATH = pathlib.Path(__file__).resolve().parents[1] / "runtime" / MODULE_PATH.name
SPEC = importlib.util.spec_from_file_location("adapter", MODULE_PATH)
adapter = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(adapter)


class AdapterTests(unittest.TestCase):
    def request(self, method, request_id=1, **params):
        return adapter.handle({"jsonrpc": "2.0", "id": request_id, "method": method, "params": params})

    def test_tool_list_is_exact_read_only_whitelist(self):
        response = self.request("tools/list")
        tools = response["result"]["tools"]
        self.assertEqual([tool["name"] for tool in tools], [
            "openjarvis_health", "openjarvis_models", "openjarvis_runtime_status"
        ])

    def test_arguments_and_unknown_tools_are_rejected(self):
        self.assertEqual(self.request("tools/call", name="openjarvis_health", arguments={"url": "https://bad"})["error"]["message"], "tool_or_arguments_not_allowed")
        self.assertEqual(self.request("tools/call", name="shell", arguments={})["error"]["message"], "tool_or_arguments_not_allowed")

    @patch.object(adapter, "get_json")
    def test_model_comparison_uses_only_safe_identifiers(self, get_json):
        get_json.side_effect = [
            {"data": [{"id": "qwen3.5:4b"}, {"id": "qwen3.8:27b"}]},
            {"models": [{"name": "qwen3.8:27b"}, {"name": "qwen3.5:4b"}]},
        ]
        response = self.request("tools/call", name="openjarvis_models", arguments={})
        body = response["result"]["content"][0]["text"]
        self.assertIn('"matching": true', body)
        self.assertNotIn("token", body)

    @patch.object(adapter, "get_json", side_effect=RuntimeError("endpoint_unavailable"))
    def test_endpoint_failure_is_returned_as_safe_tool_error(self, _get_json):
        response = self.request("tools/call", name="openjarvis_health", arguments={})
        self.assertTrue(response["result"]["isError"])
        self.assertIn("endpoint_unavailable", response["result"]["content"][0]["text"])

    def test_stdio_initialize_and_discovery_use_newline_json(self):
        requests = [
            {"jsonrpc": "2.0", "id": 7, "method": "initialize"},
            {"jsonrpc": "2.0", "method": "notifications/initialized"},
            {"jsonrpc": "2.0", "id": 8, "method": "tools/list"},
        ]
        process = subprocess.run(
            [sys.executable, str(MODULE_PATH)],
            input=b"".join(json.dumps(request).encode() + b"\n" for request in requests),
            capture_output=True,
            timeout=5,
            check=True,
        )
        replies = [json.loads(line) for line in process.stdout.splitlines()]
        self.assertEqual([reply["id"] for reply in replies], [7, 8])
        self.assertEqual(replies[0]["result"]["serverInfo"]["name"], "jarvis-openjarvis-readonly")
        self.assertEqual([tool["name"] for tool in replies[1]["result"]["tools"]], list(adapter.TOOLS))
        self.assertNotIn(b"Content-Length", process.stdout)

    def test_stdio_bad_frame_does_not_consume_next_request(self):
        process = subprocess.run(
            [sys.executable, str(MODULE_PATH)],
            input=b'not-json\n{"jsonrpc":"2.0","id":9,"method":"tools/list"}\n',
            capture_output=True, timeout=5, check=True,
        )
        replies = [json.loads(line) for line in process.stdout.splitlines()]
        self.assertEqual(replies[0]["error"]["code"], -32700)
        self.assertEqual(replies[1]["id"], 9)

    def test_oversized_frame_is_rejected_and_next_frame_preserved(self):
        stream = io.BytesIO(b"x" * (adapter.MAX_RESPONSE_BYTES + 1) + b'\n{"id":10}\n')
        with self.assertRaisesRegex(ValueError, "message_too_large"):
            adapter.read_message(stream)
        self.assertEqual(adapter.read_message(stream), {"id": 10})


if __name__ == "__main__":
    unittest.main()
