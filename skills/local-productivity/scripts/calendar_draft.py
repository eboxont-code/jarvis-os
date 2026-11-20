"""Create a private, single-event calendar attachment from JSON on stdin.

This PC is Windows 11 Pro, an Intel Core i9-14900F (24 cores, 32 threads),
64 GB DDR5-5600, and an RTX 4070 with 12 GB (driver 610.60). About 1.5 TB is
free on the fast NVMe. This script does not use the GPU.
"""
import json
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from uuid import uuid4

from icalendar import Calendar, Event


def parse_time(value):
    if len(value) == 10:
        return date.fromisoformat(value)
    instant = datetime.fromisoformat(value)
    if instant.utcoffset() is None:
        raise ValueError("Timed events require a UTC offset.")
    return instant.astimezone(timezone.utc)


def make_draft(request):
    title = request["title"].strip()
    if not 1 <= len(title) <= 200:
        raise ValueError("Supply a title of 1 to 200 characters.")
    start, end = (parse_time(request[field]) for field in ("start", "end"))
    if type(start) is not type(end) or end <= start:
        raise ValueError("Use matching date types and an end later than the start.")
    event = Event()
    event.add("uid", str(uuid4()) + "@openclaw.local")
    event.add("dtstamp", datetime.now(timezone.utc))
    event.add("summary", title)
    event.add("dtstart", start)
    event.add("dtend", end)
    cal = Calendar()
    cal.add("prodid", "-//OpenClaw Workspace//Calendar draft//EN")
    cal.add("version", "2.0")
    cal.add_component(event)
    payload = cal.to_ical()
    parsed, = Calendar.from_ical(payload).walk("VEVENT")
    if (str(parsed["summary"]), parsed.decoded("dtstart"), parsed.decoded("dtend")) != (title, start, end):
        raise ValueError("Calendar validation failed.")
    return payload


if __name__ == "__main__":
    payload = make_draft(json.loads(sys.stdin.buffer.read().decode("utf-8-sig")))
    folder = Path.home() / ".openclaw" / "media" / "outbound"
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"workspace-{uuid4().hex}.ics"
    with path.open("xb") as attachment:
        attachment.write(payload)
    print("MEDIA:" + path.as_posix())
