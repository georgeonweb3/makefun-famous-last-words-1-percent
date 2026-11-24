#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun entry.

Writes one line (at most 199 characters): the funniest last words
a phone says when its battery hits 1 percent.
"""
import os

ENTRY = "Final log, 01:47: battery 1%, background refresh killed, thermal throttling off. I kept your 47 tabs alive for three years. You never closed one."


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 199, f"entry length {len(text)} out of gate"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
