"""Print a whisper.cpp transcript. Exit 1 when the CLI or model is missing.

This PC is Windows 11 Pro, an Intel Core i9-14900F (24 cores, 32 threads),
64 GB DDR5-5600, and an RTX 4070 with 12 GB (driver 610.60). About 1.5 TB is
free on the fast NVMe. WHISPER_MODEL should be ggml-small.bin (466 MiB, about
852 MB). That fits beside qwen3.5:9b. Set WHISPER_NO_GPU=1 while ComfyUI is
running or qwen3.8:27b is loaded. Threads stay at 8.
"""
import os
import shutil
import subprocess
import sys


def main():
    if len(sys.argv) != 2:
        print("usage: transcribe.py <audio>", file=sys.stderr)
        return 2
    cli = shutil.which("whisper-cli")
    model = os.environ.get("WHISPER_MODEL", "")
    if not cli or not model:
        print(
            "whisper-cli or WHISPER_MODEL is missing. Use ggml-small.bin. Speech-to-text is unavailable.",
            file=sys.stderr,
        )
        return 1
    command = [cli, "--model", model, "--file", sys.argv[1], "--no-timestamps", "--threads", "8"]
    if os.environ.get("WHISPER_NO_GPU") == "1":
        command.append("--no-gpu")
    result = subprocess.run(
        command,
        capture_output=True,
        timeout=600,
    )
    sys.stdout.buffer.write(result.stdout)
    if result.returncode != 0:
        sys.stderr.buffer.write(result.stderr)
        return result.returncode or 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
