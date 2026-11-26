#!/usr/bin/env python3
"""Snooze Button Roast — make.fun entry.

Writes one line to /output/entry.txt: a one-line roast of an alarm clock
that rings at 6 AM on a Saturday, at most 200 characters. The house judge
reads the lines two at a time and keeps the funnier one.
"""

import os

ENTRY = (
    "Dear alarm clock: ringing at 6 a.m. on a Saturday isn't waking me up, "
    "it's a declaration of war from a machine that has never slept in."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text == text.strip(), "entry must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)} chars to /output/entry.txt")
    print(text)


if __name__ == "__main__":
    main()
