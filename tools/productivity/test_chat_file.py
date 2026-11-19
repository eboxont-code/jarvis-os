"""Exercise the JSON entry point used by OpenClaw's workspace file tool."""
import json
import os
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

from docx import Document
from openpyxl import load_workbook
from pptx import Presentation
from pypdf import PdfReader


class ChatFileTest(unittest.TestCase):
    def test_requested_formats_and_content(self):
        with TemporaryDirectory() as temp:
            environment = dict(os.environ, USERPROFILE=temp, HOME=temp)
            for kind in ("pdf", "docx", "xlsx", "pptx"):
                with self.subTest(kind=kind):
                    result = subprocess.run(
                        [sys.executable, Path(__file__).with_name("server.py"), "--chat-file"],
                        input=json.dumps(dict(format=kind, title="Sample", body="Alpha,Bravo")),
                        capture_output=True, text=True, env=environment, check=True, timeout=60,
                    )
                    path = Path(json.loads(result.stdout)["path"])
                    self.assertEqual(path.parent, Path(temp) / ".openclaw" / "media" / "outbound")
                    self.assertEqual(path.suffix, "." + kind)
                    if kind == "pdf":
                        self.assertIn("Alpha,Bravo", PdfReader(path).pages[0].extract_text())
                    elif kind == "docx":
                        self.assertEqual(Document(path).paragraphs[-1].text, "Alpha,Bravo")
                    elif kind == "xlsx":
                        book = load_workbook(path)
                        self.assertEqual(book.active["B1"].value, "Bravo")
                        book.close()
                    else:
                        self.assertEqual(Presentation(path).slides[0].placeholders[1].text, "Alpha,Bravo")


if __name__ == "__main__":
    unittest.main()
