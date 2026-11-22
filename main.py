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


if __name__ == "__main__":
    main()
