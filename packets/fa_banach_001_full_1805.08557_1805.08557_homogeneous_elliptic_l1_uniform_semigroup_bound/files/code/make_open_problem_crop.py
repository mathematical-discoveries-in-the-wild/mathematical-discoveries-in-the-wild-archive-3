"""Crop the full-width Question 4.5 panel from rendered PDF page 14.

Run from the repository root after rendering page 14 at 180 dpi as
``tmp/source-page-14.png``.
"""

from pathlib import Path

from PIL import Image


PACKET = Path(
    "runs/fa_banach_001/solutions/full/"
    "1805.08557_homogeneous_elliptic_l1_uniform_semigroup_bound"
)
SOURCE = PACKET / "tmp/source-page-14.png"
OUTPUT = PACKET / "figures/open_problem_crop.png"


def main() -> None:
    image = Image.open(SOURCE)
    width, height = image.size
    if (width, height) != (1488, 2105):
        raise ValueError(f"unexpected rendered page size: {(width, height)}")
    # Preserve the entire page width.  The vertical interval contains the
    # lead-in, all of Question 4.5, and the consequence stated immediately
    # after it, without including the bibliography below.
    image.crop((0, 105, width, 690)).save(OUTPUT)
    print(f"wrote {OUTPUT} ({width}x585)")


if __name__ == "__main__":
    main()
