"""Check a Windows OpenClaw workspace without changing its configuration.

This PC is Windows 11 Pro, an Intel Core i9-14900F (24 cores, 32 threads),
64 GB DDR5-5600, and an RTX 4070 with 12 GB (driver 610.60). About 1.5 TB is
free on the fast NVMe. A pass requires qwen3.5:9b, the chat model that stays
fully on the GPU. qwen3.5:4b and qwen3.8:27b are optional and do not affect
this result.
"""
import json
import os
from pathlib import Path
import subprocess
import sys
import urllib.request


def cli_json(arguments, timeout=45):
    result = subprocess.run(arguments, capture_output=True, timeout=timeout, check=True)
    return json.loads(result.stdout.decode("utf-8-sig"))


def main():
    if sys.platform != "win32":
        print("This check requires Windows.")
        return 1
    ctl = Path(os.environ["LOCALAPPDATA"]) / "Microsoft/WindowsApps/OpenClawFoundation.OpenClawGateway_rfcbke2p71se2/clawctl.exe"
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

    def ollama():
        with opener.open("http://127.0.0.1:11434/api/tags", timeout=5) as response:
            return any(row.get("name") == "qwen3.5:9b" for row in json.load(response)["models"])

    def rpc(method):
        return cli_json([ctl, "pwsh", "--command", "openclaw gateway call " + method + " --json --timeout 15000"])

    def node_online():
        return any(n.get("paired") and n.get("connected") for n in rpc("node.list")["nodes"])

    checks = [
        ("Ollama has qwen3.5:9b", ollama),
        ("Gateway service running", lambda: cli_json([ctl, "gateway-service", "status", "--json"])["gateway"]["state"] == "running"),
        ("Authenticated Gateway health", lambda: rpc("health").get("ok") is True),
        ("Paired Windows Node online", node_online),
    ]
    passed = True
    for label, check in checks:
        try:
            ok = bool(check())
            detail = ""
        except (OSError, ValueError, KeyError, subprocess.SubprocessError) as error:
            ok = False
            detail = " (" + type(error).__name__ + ")"
        print(("PASS  " if ok else "FAIL  ") + label + detail, flush=True)
        passed = passed and ok
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
