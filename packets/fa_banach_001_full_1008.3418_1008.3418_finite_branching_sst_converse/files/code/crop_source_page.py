#!/usr/bin/env python3
"""Crop the full-width question region from rendered page 5."""

from pathlib import Path

from PIL import Image


HERE = Path(__file__).resolve().parent
PACKET = HERE.parent
source = PACKET / "tmp" / "pdfs" / "source_page_5.png"
target = PACKET / "figures" / "open_problem_crop.png"

with Image.open(source) as image:
    # Retain the complete page width and enough context to show Theorem 2.2,
    # its conclusion, and the full two-line converse question.
    crop = image.crop((0, 175, image.width, 1225))
    crop.save(target)

print(f"wrote {target} ({crop.width}x{crop.height})")
