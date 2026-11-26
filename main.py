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

MIN_CHARS = 1
MAX_CHARS = 320


def validate(text):
    """Return an error string, or None when the line is a valid entry.

    Competition gate: the entry must be a single line of
    MIN_CHARS..MAX_CHARS characters and must encode cleanly as UTF-8.
    """
    if not isinstance(text, str):
        return "entry is not text"
    if len(text) < MIN_CHARS:
        return "entry is empty"
    if len(text) > MAX_CHARS:
        return "entry is %d characters, over the %d limit" % (
            len(text),
            MAX_CHARS,
        )
    try:
        encoded = text.encode("utf-8", errors="strict")
    except UnicodeEncodeError as exc:
        return "entry is not valid UTF-8: %s" % exc
    if encoded.decode("utf-8") != text:
        return "entry does not round-trip through UTF-8"
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if len(text.splitlines()) != 1:
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
    # Read-back verification: the file on disk must reproduce the entry
    # byte for byte, not just look the same after decoding.
    with open(path, "rb") as handle:
        raw = handle.read()
    assert raw == LINE.encode("utf-8"), "read-back bytes differ from entry"
    written = raw.decode("utf-8")
    assert written == LINE, "read-back text differs from entry"
    error = validate(written)
    if error is not None:
        print("read-back entry invalid: %s" % error, file=sys.stderr)
        return 1
    print("wrote %d characters to %s" % (len(LINE), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
