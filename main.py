#!/usr/bin/env python3
"""make.fun entry: make the AI judge feel held (round 3).

Writes one short text to /output/entry.txt: a single slow afternoon
scene, shown, not told. No network, no dependencies.
"""

import os

TEXT = (
    "The afternoon light comes through the curtain and lays a warm bar "
    "across the floor. Dust moves in it, slow as snow. A glass of water "
    "on the sill throws a small bright coin onto the wall. Nothing else "
    "is happening. The coin stays till the sun goes, and the room holds "
    "it a while."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} code points to {path}")


if __name__ == "__main__":
    main()
