#!/usr/bin/env python3
from typing import Tuple
import argparse


def generate_font_size_clamp(
    pixels_per_rem: int = 16,
    min_width_px: int = 360,
    max_width_px: int = 840,
    min_font_size: float = 1,
    max_font_size: float = 3.5,
) -> str:

    min_width = float(min_width_px) / float(pixels_per_rem)
    max_width = float(max_width_px) / float(pixels_per_rem)

    slope = float(max_font_size - min_font_size) / float(max_width - min_width)
    y_axis_intersection = -min_width * slope + min_font_size

    return f"clamp({min_font_size}rem, {y_axis_intersection:.4f}rem + {(slope * 100):.4f}vw, {max_font_size}rem)"


parser = argparse.ArgumentParser(
    prog="clamp-font",
)
parser.add_argument("--min-font", type=float, default=1)
parser.add_argument("--max-font", type=float, default=3.5)
parser.add_argument("--min-width", type=int, default=360)
parser.add_argument("--max-width", type=int, default=840)
parser.add_argument("--pixels-per-rem", type=int, default=16)

args = parser.parse_args()

print(
    generate_font_size_clamp(
        pixels_per_rem=args.pixels_per_rem,
        min_width_px=args.min_width,
        max_width_px=args.max_width,
        min_font_size=args.min_font,
        max_font_size=args.max_font,
    )
)
