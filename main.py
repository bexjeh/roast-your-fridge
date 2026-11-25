"""Roast Your Fridge entry: writes a single-line roast to entry.txt.

The roast targets a specific, recognisable fridge detail (the crisper
drawer) with the twist paying off in the last few words.
"""

import os

ENTRY = "My fridge's crisper drawer is where vegetables go to retire, and mine returned as compost with opinions."


def main() -> None:
    # Gate guard: one line, 1-200 chars, non-blank. Fail loudly, never
    # silently write an invalid entry.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be a single non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
