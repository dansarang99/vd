#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Slide HTML Renderer (Headless Browser)
Renders HTML slide templates into 1920x1080 high-resolution PNG images using
local Headless Chrome or Edge on Windows, macOS, or Linux.
"""

import sys
import os
import glob
import argparse
import subprocess
from typing import List, Optional

def find_browser_executable() -> Optional[str]:
    # Common locations across OS
    candidates = []

    if sys.platform.startswith("win"):
        candidates = [
            os.path.expandvars(r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"),
            os.path.expandvars(r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"),
            os.path.expandvars(r"%LocalAppData%\Google\Chrome\Application\chrome.exe"),
            os.path.expandvars(r"%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"),
            os.path.expandvars(r"%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"),
            os.path.expandvars(r"%LocalAppData%\Microsoft\Edge\Application\msedge.exe"),
        ]
    elif sys.platform == "darwin":  # macOS
        candidates = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
            "/Applications/Chromium.app/Contents/MacOS/Chromium",
        ]
    else:  # Linux
        candidates = [
            "/usr/bin/google-chrome",
            "/usr/bin/chromium-browser",
            "/usr/bin/chromium",
            "/usr/bin/google-chrome-stable",
            "/snap/bin/chromium",
        ]

    for path in candidates:
        if os.path.exists(path):
            return path

    # Try PATH resolution
    for name in ["chrome", "google-chrome", "msedge", "chromium"]:
        try:
            result = subprocess.run(["where" if sys.platform.startswith("win") else "which", name],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip().splitlines()[0]
        except Exception:
            pass

    return None

def render_html_to_png(html_path: str, output_png: str, browser_path: str, width: int = 1920, height: int = 1080) -> bool:
    abs_html = os.path.abspath(html_path)
    abs_png = os.path.abspath(output_png)

    # In case HTML refers to file:// URLs, use path directly
    url = f"file:///{abs_html.replace(os.sep, '/')}"

    cmd = [
        browser_path,
        "--headless",
        "--disable-gpu",
        f"--window-size={width},{height}",
        "--hide-scrollbars",
        f"--screenshot={abs_png}",
        url
    ]

    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return os.path.exists(abs_png)
    except subprocess.CalledProcessError as e:
        print(f"[!] Error rendering {html_path}: {e}", file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(
        description="Render HTML slide templates into 1920x1080 PNG images using Headless Chrome or Edge."
    )
    parser.add_argument("-i", "--input", required=True, help="Path to an HTML slide file or directory containing .html slides.")
    parser.add_argument("-o", "--output-dir", default=".", help="Directory to save rendered PNG images.")
    parser.add_argument("--width", type=int, default=1920, help="Viewport width in pixels (default: 1920).")
    parser.add_argument("--height", type=int, default=1080, help="Viewport height in pixels (default: 1080).")
    parser.add_argument("--browser", default=None, help="Custom path to browser executable (Chrome/Edge/Chromium).")

    args = parser.parse_args()

    browser = args.browser or find_browser_executable()
    if not browser or not os.path.exists(browser):
        print("[!] Error: Could not find Google Chrome or Microsoft Edge. Please specify path via --browser.", file=sys.stderr)
        sys.exit(1)

    print(f"[*] Using Browser Engine: {browser}")

    os.makedirs(args.output_dir, exist_ok=True)

    if os.path.isdir(args.input):
        html_files = sorted(glob.glob(os.path.join(args.input, "*.html")))
    elif os.path.isfile(args.input):
        html_files = [args.input]
    else:
        print(f"[!] Error: Input path not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    if not html_files:
        print(f"[!] No HTML files found in: {args.input}")
        sys.exit(0)

    print(f"[*] Found {len(html_files)} slide(s) to render at {args.width}x{args.height}...")

    success_count = 0
    for idx, html_file in enumerate(html_files):
        base_name = os.path.splitext(os.path.basename(html_file))[0]
        out_png = os.path.join(args.output_dir, f"{base_name}.png")

        print(f"    [{idx+1:02d}/{len(html_files):02d}] Rendering {base_name}.html -> {base_name}.png")
        if render_html_to_png(html_file, out_png, browser, args.width, args.height):
            success_count += 1

    print(f"\n[+] Rendering completed: {success_count}/{len(html_files)} slides rendered successfully to '{args.output_dir}'.")

if __name__ == "__main__":
    main()
