#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI.

Writes a single joke pickup line, aimed at a robot / AI, to
/output/entry.txt. The line must be 1-200 characters of UTF-8 text.

The line leans on the transformer architecture itself: a transformer
model reads input with attention heads, so "you've got my attention"
becomes literal. It avoids the worn robot moves (batteries, charging,
rebooting) and lands setup + punch inside one breath.
"""

import os

# The pickup line. Setup: "Are you a transformer?" Punch: the model's
# own attention heads are the ones doing the looking -- "you've got my
# attention" turned literal, in the voice of a person talking to a model.
LINE = "Are you a transformer? Because you've got all my attention heads turning toward you."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 200


def build_line() -> str:
    """Return the entry line, validated against the gate."""
    line = LINE.strip()
    if not line:
        raise ValueError("entry line must not be empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry line is {len(line)} chars, over the 200 cap")
    # The file holds the line plus one trailing newline; the gate counts
    # the whole file, so the written bytes must fit the cap too.
    if len(line) + 1 > MAX_CHARS:
        raise ValueError("entry line plus its newline exceeds the 200 cap")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    return line


def main() -> None:
    line = build_line()
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")
    print(f"wrote {len(line)}-char entry to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
