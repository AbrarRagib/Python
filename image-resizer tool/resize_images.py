#!/usr/bin/env python3
"""Resize images with smart_resize for OCR; save as PNG."""

from __future__ import annotations

import argparse
import logging
import math
import sys
from pathlib import Path

from PIL import Image

SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".gif",
    ".tiff",
    ".tif",
    ".webp",
    ".jfif",
    ".pjpeg",
    ".pjp",
}

DEFAULT_FACTOR = 28
DEFAULT_MIN_PIXELS = 640_000
DEFAULT_MAX_PIXELS = 2_822_400
MEGAPIXEL = 1_000_000


def round_by_factor(value: float, factor: int) -> int:
    return round(value / factor) * factor


def floor_by_factor(value: float, factor: int) -> int:
    return math.floor(value / factor) * factor


def ceil_by_factor(value: float, factor: int) -> int:
    return math.ceil(value / factor) * factor


def smart_resize(
    height: int,
    width: int,
    factor: int = 28,
    min_pixels: int = 640_000,
    max_pixels: int = 2_822_400,
) -> tuple[int, int]:
    if max(height, width) / min(height, width) > 200:
        raise ValueError(
            f"absolute aspect ratio must be smaller than 200, got "
            f"{max(height, width) / min(height, width)}"
        )
    h_bar = max(factor, round_by_factor(height, factor))
    w_bar = max(factor, round_by_factor(width, factor))
    if h_bar * w_bar > max_pixels:
        beta = math.sqrt((height * width) / max_pixels)
        h_bar = max(factor, floor_by_factor(height / beta, factor))
        w_bar = max(factor, floor_by_factor(width / beta, factor))
    elif h_bar * w_bar < min_pixels:
        beta = math.sqrt(min_pixels / (height * width))
        h_bar = ceil_by_factor(height * beta, factor)
        w_bar = ceil_by_factor(width * beta, factor)
        if h_bar * w_bar > max_pixels:
            beta = math.sqrt((h_bar * w_bar) / max_pixels)
            h_bar = max(factor, floor_by_factor(h_bar / beta, factor))
            w_bar = max(factor, floor_by_factor(w_bar / beta, factor))
    return h_bar, w_bar


def megapixels(width: int, height: int) -> float:
    return (width * height) / MEGAPIXEL


def is_image_file(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS


def process_image(
    input_path: Path,
    output_path: Path,
) -> tuple[int, int, int, int, float, float, str]:
    with Image.open(input_path) as image:
        image = image.convert("RGB")
        old_width, old_height = image.size
        old_mp = megapixels(old_width, old_height)

        new_height, new_width = smart_resize(old_height, old_width)

        old_pixels = old_width * old_height
        new_pixels = new_width * new_height

        if new_width == old_width and new_height == old_height:
            action = "converted"
            output_image = image
        else:
            action = "upscaled" if new_pixels > old_pixels else "downscaled"
            output_image = image.resize(
                (new_width, new_height), Image.Resampling.LANCZOS
            )

        new_mp = megapixels(new_width, new_height)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_image.save(output_path, format="PNG", optimize=True)

    return old_width, old_height, new_width, new_height, old_mp, new_mp, action


def process_images(
    input_dir: Path,
    output_dir: Path,
) -> tuple[int, int]:
    image_files = sorted(
        path for path in input_dir.iterdir() if is_image_file(path)
    )

    processed = 0
    skipped = 0

    for image_path in image_files:
        output_path = output_dir / f"{image_path.stem}.png"
        try:
            old_w, old_h, new_w, new_h, old_mp, new_mp, action = process_image(
                image_path, output_path
            )
        except Exception as exc:
            logging.warning("Skipping unreadable file %s: %s", image_path.name, exc)
            skipped += 1
            continue

        logging.info(
            "%s %s: %dx%d (%.2f MP) -> %dx%d (%.2f MP) -> %s",
            action.capitalize(),
            image_path.name,
            old_w,
            old_h,
            old_mp,
            new_w,
            new_h,
            new_mp,
            output_path,
        )
        processed += 1

    return processed, skipped


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Resize images with smart_resize for OCR. "
            "Aspect ratio is preserved; output is saved as PNG."
        )
    )
    parser.add_argument(
        "-i", "--input-dir",
        type=Path,
        default=Path("images"),
        help="Directory containing source images (default: images)",
    )
    parser.add_argument(
        "-o", "--output-dir",
        type=Path,
        default=Path("output"),
        help="Directory for resized PNG files (default: output)",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable debug logging",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    input_dir = args.input_dir.resolve()
    output_dir = args.output_dir.resolve()

    if not input_dir.is_dir():
        logging.error("Input directory does not exist: %s", input_dir)
        return 1

    logging.info("Input: %s", input_dir)
    logging.info("Output: %s", output_dir)
    logging.info(
        "Using smart_resize (factor=%d, min_pixels=%d, max_pixels=%d)",
        DEFAULT_FACTOR,
        DEFAULT_MIN_PIXELS,
        DEFAULT_MAX_PIXELS,
    )

    processed, skipped = process_images(
        input_dir=input_dir,
        output_dir=output_dir,
    )

    logging.info("Done. Resized %d image(s), skipped %d.", processed, skipped)
    return 0


if __name__ == "__main__":
    sys.exit(main())