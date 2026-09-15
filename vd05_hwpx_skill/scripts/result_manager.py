#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Result Auto-Increment Manager (result_manager.py)
Manages output numbering [001]~[999] in result directory.
"""

from __future__ import annotations

import os
from pathlib import Path


def get_next_hwpx_filename(result_dir: str | Path, title_slug: str) -> Path:
    """
    Finds the next sequential [001]~[999] filename in the target directory.
    """
    rdir = Path(result_dir).resolve()
    rdir.mkdir(parents=True, exist_ok=True)

    existing_files = [f for f in rdir.glob("*.hwpx")]
    next_num = len(existing_files) + 1
    filename = f"[{next_num:03d}]_{title_slug}.hwpx"
    return rdir / filename
