import importlib.util
import json
import pathlib
import subprocess
import sys
import unittest
from unittest.mock import patch


MODULE_PATH = pathlib.Path(__file__).with_name("openjarvis_readonly_mcp_adapter.py")
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

    def test_stdio_initialize_uses_mcp_framing(self):
        body = json.dumps({"jsonrpc": "2.0", "id": 7, "method": "initialize"}).encode()
        framed = f"Content-Length: {len(body)}\r\n\r\n".encode() + body
        process = subprocess.Popen(
            [sys.executable, str(MODULE_PATH)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        assert process.stdin is not None and process.stdout is not None
        process.stdin.write(framed)
        process.stdin.flush()
        headers = {}
        while True:
            line = process.stdout.readline()
            if line in (b"\r\n", b"\n"):
                break
            key, value = line.decode().split(":", 1)
            headers[key.lower()] = value.strip()
        reply = json.loads(process.stdout.read(int(headers["content-length"])))
        process.stdin.close()
        process.wait(timeout=5)
        process.stdout.close()
        process.stderr.close()
        self.assertEqual(reply["id"], 7)
        self.assertEqual(reply["result"]["serverInfo"]["name"], "jarvis-openjarvis-readonly")


if __name__ == "__main__":
    unittest.main()

