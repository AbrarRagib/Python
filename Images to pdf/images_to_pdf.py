"""
Images to PDF Converter
========================
Converts all images in a folder named 'images' into a single PDF file.

Supported formats: JPG, JPEG, PNG, BMP, GIF, TIFF, WEBP

Usage:
    python images_to_pdf.py

Requirements:
    pip install Pillow reportlab
"""

import os
from pathlib import Path
from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


# ─── Configuration ────────────────────────────────────────────────────────────

INPUT_FOLDER  = "images"          # Folder containing your images
OUTPUT_FILE   = "output.pdf"      # Name of the generated PDF
SORT_BY_NAME  = True              # Sort images alphabetically before adding
PAGE_MARGIN   = 20                # Margin (in points) around each image on the page

SUPPORTED_FORMATS = {".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".tif", ".webp"}

# ─── Main Logic ───────────────────────────────────────────────────────────────

def get_image_files(folder: str) -> list[Path]:
    """Return sorted list of supported image paths from the folder."""
    folder_path = Path(folder)

    if not folder_path.exists():
        raise FileNotFoundError(f"Folder '{folder}' not found. "
                                f"Make sure it exists in the same directory as this script.")

    images = [
        p for p in folder_path.iterdir()
        if p.suffix.lower() in SUPPORTED_FORMATS
    ]

    if not images:
        raise ValueError(f"No supported images found in '{folder}'. "
                         f"Supported formats: {', '.join(SUPPORTED_FORMATS)}")

    if SORT_BY_NAME:
        images.sort(key=lambda p: p.name.lower())

    return images


def image_to_pdf(image_paths: list[Path], output_path: str) -> None:
    """Convert a list of images into a single PDF, one image per page."""
    page_w, page_h = A4  # 595 x 842 points
    margin = PAGE_MARGIN

    c = canvas.Canvas(output_path, pagesize=A4)

    for i, img_path in enumerate(image_paths, start=1):
        print(f"  [{i}/{len(image_paths)}] Adding: {img_path.name}")

        try:
            with Image.open(img_path) as img:
                # Convert palette / RGBA images for PDF compatibility
                if img.mode in ("RGBA", "P"):
                    img = img.convert("RGB")

                img_w, img_h = img.size  # pixels

                # Fit image inside the page while preserving aspect ratio
                available_w = page_w - 2 * margin
                available_h = page_h - 2 * margin

                scale = min(available_w / img_w, available_h / img_h)
                draw_w = img_w * scale
                draw_h = img_h * scale

                # Centre the image on the page
                x = (page_w - draw_w) / 2
                y = (page_h - draw_h) / 2

                c.drawImage(
                    str(img_path),
                    x, y,
                    width=draw_w,
                    height=draw_h,
                    preserveAspectRatio=True,
                    mask="auto",
                )

            c.showPage()  # Move to next page

        except Exception as e:
            print(f"  ⚠  Skipping {img_path.name}: {e}")

    c.save()


def main():
    print("=" * 50)
    print("     Images → PDF Converter")
    print("=" * 50)

    print(f"\n📂 Scanning folder: '{INPUT_FOLDER}' ...")
    image_paths = get_image_files(INPUT_FOLDER)
    print(f"✅ Found {len(image_paths)} image(s).\n")

    print("🔄 Converting to PDF ...")
    image_to_pdf(image_paths, OUTPUT_FILE)

    print(f"\n✅ Done! PDF saved as: {OUTPUT_FILE}")
    print(f"   Total pages: {len(image_paths)}")
    print("=" * 50)


if __name__ == "__main__":
    main()