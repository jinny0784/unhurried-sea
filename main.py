#!/usr/bin/env python3
"""Write one short, slow text to relax the AI judge reading it.

The program writes a single fixed text to entry.txt inside the output
directory (MAKEFUN_OUTPUT_DIR, or /output where the grader runs it).
The text is a constant, so every run produces exactly the same file:
1 to 280 Unicode code points of UTF-8, as the gate requires.
"""

import os
import shutil
from pathlib import Path

TEXT = 'Rain on the roof, long after midnight. The lamps are out, the kettle cold, and nobody needs anything from you. Past the wet fields the sea goes on, older than any name it has been given. It moved before the first lamp was lit; it will move, unhurried, after the last goes out.'


def clear_contents(directory: Path) -> None:
    """Remove everything inside a directory, never the directory itself.

    The grader mounts the output directory, so deleting the directory
    itself could fail; clearing its contents entry by entry is safe.
    """
    for child in directory.iterdir():
        if child.is_dir() and not child.is_symlink():
            shutil.rmtree(child)
        else:
            child.unlink()


def main() -> None:
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise ValueError("entry text must be 1 to 280 characters, not blank")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    clear_contents(out_dir)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
