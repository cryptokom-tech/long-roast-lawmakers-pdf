#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (1-320 characters, a single line) to
/output/entry.txt. The sentence roasts a lawmaker who chairs the
committee on digital sovereignty, wrote the law banning foreign apps,
and still turned his own bill into a PDF on a free website that uploads
it to a server in another country.

Stdlib only. Deterministic: the same bytes on every run.
"""

import os
import sys

LINE = (
    "He chairs the committee on digital sovereignty, wrote the law "
    "banning foreign apps, and turned his own bill into a PDF on a free "
    "website that uploads it to a server in another country."
)

MAX_CHARS = 320


def validate(text):
    """Return an error string, or None when the line is a valid entry."""
    if not text:
        return "entry is empty"
    if len(text) > MAX_CHARS:
        return "entry is %d characters, over the 320 limit" % len(text)
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if any(ord(ch) < 32 for ch in text):
        return "entry contains a control character"
    if text.count(".") != 1 or not text.endswith("."):
        return "entry must be exactly one sentence"
    return None


def main():
    error = validate(LINE)
    if error is not None:
        print("invalid entry: %s" % error, file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != LINE:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print("wrote %d characters to %s" % (len(LINE), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
