"""Transcribe one OpenClaw audio attachment using the local Whisper base model."""
from pathlib import Path
import sys

from faster_whisper import WhisperModel


if __name__ == "__main__":
    audio, = sys.argv[1:]
    model = WhisperModel(
        str(Path(__file__).with_name("model")),
        device="cpu", compute_type="int8", local_files_only=True,
    )
    segments, _ = model.transcribe(audio, beam_size=3)
    text = " ".join(segment.text.strip() for segment in segments).strip()
    sys.stdout.buffer.write((text + "\n").encode("utf-8"))
