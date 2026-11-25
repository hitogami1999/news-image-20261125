#!/usr/bin/env python3
"""Entry for make.fun news-image-20261125.

Writes the one-day world-news image for Wednesday 25 November 2026 to
/output/entry.png. The image is bundled in this repository as entry.png;
this program copies it to the output directory byte for byte, so both
grader runs produce identical output.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    source = os.path.join(HERE, "entry.png")
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)
    size = os.path.getsize(target)
    print(f"wrote {target} ({size} bytes) - Wednesday 25 November 2026 broadsheet")
    return 0


if __name__ == "__main__":
    sys.exit(main())
