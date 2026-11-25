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

# Grader default; overridable for local runs without touching the entry.
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main():
    lines = ENTRY.split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    assert lines[0].startswith("To: "), "first line must be a To: line"
    message = lines[1]
    assert message == message.strip(), "message line must not carry padding"
    assert not ENTRY.endswith("\n"), "entry must not end with a newline"
    assert 1 <= len(message) <= 200, "message line must be 1-200 characters"
    assert 1 <= len(ENTRY) <= 260, "whole entry must be 1-260 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "written entry must read back identical"


if __name__ == "__main__":
    main()
