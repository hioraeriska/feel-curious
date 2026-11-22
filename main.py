#!/usr/bin/env python3
"""Feel curious -- write one short text to /output/entry.txt.

The text is a fixed, hand-written miniature: a tide, a bottle, and a note
dated tomorrow. Deterministic: every run writes exactly the same bytes.
"""

import os

TEXT = "Every tide brings the same bottle back to the same shore. Inside it, a note in your own handwriting, dated tomorrow, that says only: 'Do not open the next one.'"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # Read it back and hold the entry to the gate: 1-280 code points,
    # not only white space. Fail loudly instead of shipping a bad file.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == TEXT, "entry.txt does not match the intended text"
    assert 1 <= len(written) <= 280, "entry must be 1-280 code points"
    assert written.strip(), "entry must not be only white space"


if __name__ == "__main__":
    main()
