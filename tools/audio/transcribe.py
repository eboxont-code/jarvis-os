"""Print a whisper.cpp transcript. Exit 1 when the CLI or model is missing."""
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
            "whisper-cli or WHISPER_MODEL is missing. Speech-to-text is unavailable.",
            file=sys.stderr,
        )
        return 1
    result = subprocess.run(
        [cli, "--model", model, "--file", sys.argv[1], "--no-timestamps"],
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
