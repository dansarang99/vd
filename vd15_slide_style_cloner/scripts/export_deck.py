#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Slide Deck Exporter (PDF & PPTX)
Packages rendered high-resolution PNG slide images into:
1. A crisp, multi-page vector-wrapped 1080p PDF.
2. A 16:9 widescreen Microsoft PowerPoint (.pptx) presentation.
"""

import sys
import os
import glob
import argparse
from typing import List

def compile_pdf(image_paths: List[str], output_pdf_path: str):
    try:
        import fitz  # PyMuPDF
    except ImportError:
        raise ImportError("PyMuPDF is required for PDF packaging. Install via: pip install pymupdf")

    print(f"[*] Compiling {len(image_paths)} slides into PDF: {output_pdf_path}")
    doc = fitz.open()

    for idx, img_path in enumerate(image_paths):
        img_doc = fitz.open(img_path)
        pdf_bytes = img_doc.convert_to_pdf()
        img_pdf = fitz.open("pdf", pdf_bytes)
        doc.insert_pdf(img_pdf)
        img_doc.close()
        img_pdf.close()
        print(f"    [PDF] Injected slide {idx+1:02d}/{len(image_paths):02d}")

    os.makedirs(os.path.dirname(os.path.abspath(output_pdf_path)), exist_ok=True)
    doc.save(output_pdf_path)
    doc.close()
    print(f"[+] Successfully generated PDF: {output_pdf_path}")

def compile_pptx(image_paths: List[str], output_pptx_path: str, title: str = "Presentation"):
    try:
        from pptx import Presentation
        from pptx.util import Inches
    except ImportError:
        raise ImportError("python-pptx is required for PPTX packaging. Install via: pip install python-pptx")

    print(f"[*] Compiling {len(image_paths)} slides into PPTX (16:9 Widescreen): {output_pptx_path}")
    prs = Presentation()
    # 16:9 Widescreen standard: 13.333 x 7.5 inches (1920x1080 equivalent)
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]  # Blank layout

    for idx, img_path in enumerate(image_paths):
        slide = prs.slides.add_slide(blank_layout)
        slide.shapes.add_picture(img_path, 0, 0, width=prs.slide_width, height=prs.slide_height)
        print(f"    [PPTX] Added slide {idx+1:02d}/{len(image_paths):02d}")

    os.makedirs(os.path.dirname(os.path.abspath(output_pptx_path)), exist_ok=True)
    prs.save(output_pptx_path)
    print(f"[+] Successfully generated PPTX: {output_pptx_path}")

def main():
    parser = argparse.ArgumentParser(
        description="Package rendered PNG slides into high-resolution PDF and 16:9 PowerPoint (PPTX) files."
    )
    parser.add_argument("-i", "--input-dir", required=True, help="Directory containing rendered .png slide images.")
    parser.add_argument("-o", "--output-name", default="final_presentation", help="Base filename for exported files (without extension).")
    parser.add_argument("--format", choices=["all", "pdf", "pptx"], default="all", help="Output format: 'all', 'pdf', or 'pptx' (default: all).")
    parser.add_argument("--pattern", default="*.png", help="Glob pattern for selecting slide images (default: '*.png').")
    parser.add_argument("--title", default="Executive Slide Deck", help="Presentation title metadata.")

    args = parser.parse_args()

    if not os.path.isdir(args.input_dir):
        print(f"[!] Error: Input directory '{args.input_dir}' does not exist.", file=sys.stderr)
        sys.exit(1)

    image_paths = sorted(glob.glob(os.path.join(args.input_dir, args.pattern)))
    if not image_paths:
        print(f"[!] Error: No images matching pattern '{args.pattern}' found in '{args.input_dir}'.", file=sys.stderr)
        sys.exit(1)

    print(f"[*] Found {len(image_paths)} images to package.")

    out_base = args.output_name
    if out_base.lower().endswith(".pdf") or out_base.lower().endswith(".pptx"):
        out_base = os.path.splitext(out_base)[0]

    pdf_target = f"{out_base}.pdf"
    pptx_target = f"{out_base}.pptx"

    if args.format in ["all", "pdf"]:
        compile_pdf(image_paths, pdf_target)

    if args.format in ["all", "pptx"]:
        compile_pptx(image_paths, pptx_target, title=args.title)

    print(f"\n[SUCCESS] Packaging complete!")

if __name__ == "__main__":
    main()
