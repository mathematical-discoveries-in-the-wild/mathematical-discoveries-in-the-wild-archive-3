#!/usr/bin/env python3
"""Render source page 15 and crop the definition plus open question."""

from pathlib import Path
import shutil
import subprocess

from PIL import Image


PACKET = Path(__file__).resolve().parents[1]
SOURCE = PACKET / "source_paper.pdf"
TMP_PREFIX = PACKET / "tmp" / "source-page-15"
RENDERED = TMP_PREFIX.with_suffix(".png")
OUTPUT = PACKET / "figures" / "open_problem_crop.png"


def locate_pdftoppm() -> str:
    found = shutil.which("pdftoppm")
    if found:
        return found
    bundled = (
        Path.home()
        / ".cache/codex-runtimes/codex-primary-runtime/dependencies/bin/override/pdftoppm"
    )
    if bundled.exists():
        return str(bundled)
    raise FileNotFoundError("pdftoppm not found")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    TMP_PREFIX.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            locate_pdftoppm(),
            "-f",
            "15",
            "-l",
            "15",
            "-r",
            "180",
            "-png",
            "-singlefile",
            str(SOURCE),
            str(TMP_PREFIX),
        ],
        check=True,
    )
    with Image.open(RENDERED) as image:
        width, height = image.size
        if (width, height) != (1530, 1980):
            raise RuntimeError(f"unexpected render size: {(width, height)}")
        image.crop((0, 245, width, 735)).save(OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    main()
