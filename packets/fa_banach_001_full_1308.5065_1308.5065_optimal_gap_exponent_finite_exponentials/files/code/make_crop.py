#!/usr/bin/env python3
"""Crop the rendered source page vertically while retaining full page width."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "tmp" / "source_page-22.png"
OUTPUT = ROOT / "figures" / "open_problem_crop.png"


def main() -> None:
    with Image.open(SOURCE) as image:
        width, height = image.size
        crop = image.crop((0, int(0.345 * height), width, int(0.84 * height)))
        crop.save(OUTPUT, dpi=(180, 180))
        print(f"wrote {OUTPUT} ({crop.width}x{crop.height})")


if __name__ == "__main__":
    main()
