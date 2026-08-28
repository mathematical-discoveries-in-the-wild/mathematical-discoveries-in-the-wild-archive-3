#!/usr/bin/env python3
"""Crop the full-width conjecture region from rendered source page 11."""

from pathlib import Path

from PIL import Image


HERE = Path(__file__).resolve().parent
PACKET = HERE.parent
source = PACKET / "tmp" / "pdfs" / "source_page_11.png"
target = PACKET / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    # Keep the complete page width and the entire conjecture, including both
    # numbered conditions.  The surrounding sentence is retained as context.
    crop = image.crop((0, 610, image.width, 1045))
    crop.save(target)

print(f"wrote {target} ({crop.width}x{crop.height})")
