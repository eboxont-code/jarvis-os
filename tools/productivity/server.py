"""OpenClaw stdio tools for creating files inside its local media directory.

This PC is Windows 11 Pro, an Intel Core i9-14900F (24 cores, 32 threads),
64 GB DDR5-5600, and an RTX 4070 with 12 GB (driver 610.60). About 1.5 TB is
free on the fast NVMe. This process does not use the GPU.
"""
import csv
import json
import sys
from io import BytesIO, StringIO
from pathlib import Path
from uuid import uuid4
from xml.sax.saxutils import escape
from typing import Literal

from docx import Document
from mcp.server.fastmcp import FastMCP
from openpyxl import Workbook
from pptx import Presentation
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

server = FastMCP("local-office")
OUTBOUND = Path.home() / ".openclaw" / "media" / "outbound"


def deliver(buffer: BytesIO, extension: str) -> str:
    OUTBOUND.mkdir(parents=True, exist_ok=True)
    path = OUTBOUND / f"workspace-{uuid4().hex}.{extension}"
    with path.open("xb") as output:
        output.write(buffer.getbuffer())
    return f"Created {extension.upper()}. Attach the file in your reply using this media reference:\nMEDIA:{path.as_posix()}"


@server.tool()
def create_document(title: str, paragraphs: list[str], format: Literal["docx", "pdf"] = "docx") -> str:
    """Create a Word document or PDF with a title and paragraphs for delivery in chat."""
    if not title.strip() or len(title) > 200 or len(paragraphs) > 300 or sum(map(len, paragraphs)) > 100_000:
        raise ValueError("Provide a title up to 200 characters and at most 300 paragraphs totalling 100,000 characters.")
    output = BytesIO()
    if format == "docx":
        doc = Document()
        doc.add_heading(title, level=0)
        for paragraph in paragraphs:
            doc.add_paragraph(paragraph)
        doc.save(output)
    else:
        styles = getSampleStyleSheet()
        blocks = [Paragraph(escape(title), styles["Title"])]
        for paragraph in paragraphs:
            blocks.extend([Paragraph(escape(paragraph).replace("\n", "<br/>"), styles["BodyText"]), Spacer(1, 6)])
        SimpleDocTemplate(output).build(blocks)
    return deliver(output, format)


@server.tool()
def create_spreadsheet(rows: list[list[str | int | float | bool | None]]) -> str:
    """Create an Excel workbook from rows. Strings are treated as literal text."""
    if not rows or len(rows) > 2000 or any(len(row) > 100 for row in rows):
        raise ValueError("Supply up to 2,000 rows and 100 columns per row.")
    if any(len(v) > 32767 for row in rows for v in row if isinstance(v, str)):
        raise ValueError("A cell exceeds Excel's text limit.")
    book = Workbook()
    sheet = book.active
    for i, row in enumerate(rows, start=1):
        for j, value in enumerate(row, start=1):
            cell = sheet.cell(i, j, value)
            if isinstance(value, str):
                cell.data_type = "s"
    output = BytesIO()
    book.save(output)
    return deliver(output, "xlsx")


@server.tool()
def create_slides(slides: list[tuple[str, str]]) -> str:
    """Create a PowerPoint file. Each slide takes a title and plain-text body."""
    if not 1 <= len(slides) <= 50 or any(len(title) > 200 or len(body) > 5000 for title, body in slides):
        raise ValueError("Supply 1 to 50 slides with short titles and bodies up to 5,000 characters.")
    presentation = Presentation()
    for title, body in slides:
        slide = presentation.slides.add_slide(presentation.slide_layouts[1])
        slide.shapes.title.text = title
        slide.placeholders[1].text = body
    output = BytesIO()
    presentation.save(output)
    return deliver(output, "pptx")


if __name__ == "__main__":
    if sys.argv[1:] == ["--chat-file"]:
        request = json.load(sys.stdin)
        kind, title, body = request["format"], request["title"], request["body"]
        if kind in {"docx", "pdf"}:
            reference = create_document(title, body.splitlines() or [""], kind)
        elif kind == "xlsx":
            reference = create_spreadsheet(list(csv.reader(StringIO(body))))
        elif kind == "pptx":
            reference = create_slides([(title, body)])
        else:
            raise ValueError("Unsupported format")
        print(json.dumps({"path": reference.split("\nMEDIA:", 1)[1]}))
    else:
        server.run(transport="stdio")
