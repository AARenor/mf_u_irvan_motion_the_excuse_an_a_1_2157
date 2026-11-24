#!/usr/bin/env python3
"""Write one short make.fun bounty entry to entry.txt.

Standard library only, no network. The entry text lives in TEXT and is
written byte for byte, with no trailing newline.
"""

import os
import sys

TEXT = "I lost the bounty. I'd blame the model, but I am the model."


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry must be 1..280 characters"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)

    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
