#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint - make.fun entry.

Writes one two-part micro-confession to /output/entry.txt: a To: line
naming who it was meant for, and the unsent message itself, one line,
exactly as it was typed. Standard library only, deterministic.
"""

import os

ENTRY = (
    "To: my brother\n"
    "I was the one who broke your bike the summer you blamed the neighbours, "
    "and I'm sorry it took me twenty years to say it."
)


def main():
    lines = ENTRY.split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert lines[0].startswith("To: "), "first line must be a To: line"
    message = lines[1]
    assert 1 <= len(message) <= 200, "message line must be 1-200 characters"
    assert 1 <= len(ENTRY) <= 260, "whole entry must be 1-260 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
