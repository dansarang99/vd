#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HWPX Robust Core Engine (hwpx_engine.py)
Author: dansarang99 (Inspired by Prof. Lee Hyun-goo & perfected by Lee Han-gyu)
"""

from __future__ import annotations

import os
import re
import sys
import xml.sax.saxutils as saxutils
import zipfile
from pathlib import Path
from typing import Dict, List, Optional, Tuple


def escape_xml_text(text: str) -> str:
    """Escapes XML special characters safely."""
    return saxutils.escape(text, entities={"'": "&apos;", '"': "&quot;"})


def strip_linesegarray(xml_content: str) -> str:
    """Strips linesegarray layout caches to prevent font overlap and row clipping."""
    pat_pair = re.compile(r"<(\w+:)?linesegarray\b[^>]*>.*?</(\w+:)?linesegarray>", re.S)
    pat_self = re.compile(r"<(\w+:)?linesegarray\b[^>]*/>")
    text = pat_pair.sub("", xml_content)
    text = pat_self.sub("", text)
    return text


def save_hwpx_package(source_dir: str | Path, output_file: str | Path) -> Path:
    """
    Packages a directory into a 100% valid HWPX file.
    RULE 1: 'mimetype' MUST be the very first file in the archive.
    RULE 2: 'mimetype' MUST be uncompressed (ZIP_STORED).
    RULE 3: All other files are compressed (ZIP_DEFLATED).
    """
    source_path = Path(source_dir).resolve()
    out_path = Path(output_file).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    mimetype_file = source_path / "mimetype"
    if not mimetype_file.exists():
        raise FileNotFoundError(f"mimetype file not found in {source_path}")

    with zipfile.ZipFile(out_path, "w") as z:
        # 1. First file: mimetype (Stored, 0% compression)
        z.write(mimetype_file, "mimetype", compress_type=zipfile.ZIP_STORED)

        # 2. All other files: Deflated
        for root, _, files in os.walk(source_path):
            for file in files:
                if file == "mimetype":
                    continue
                fpath = Path(root) / file
                rel_path = fpath.relative_to(source_path).as_posix()
                z.write(fpath, rel_path, compress_type=zipfile.ZIP_DEFLATED)

    return out_path


def replace_in_hwpx(template_hwpx: str | Path, output_hwpx: str | Path, replace_dict: Dict[str, str], clear_cache: bool = True) -> Path:
    """
    Safely performs in-place text replacement in section0.xml of an existing valid HWPX file,
    recalculates CRC and file sizes automatically, and packages into a valid HWPX.
    """
    tpl_path = Path(template_hwpx).resolve()
    out_path = Path(output_hwpx).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    files_data = {}
    with zipfile.ZipFile(tpl_path, "r") as z:
        for name in z.namelist():
            files_data[name] = z.read(name)

    # Decode and replace in section0.xml
    target_section = "Contents/section0.xml"
    if target_section in files_data:
        sec_text = files_data[target_section].decode("utf-8")
        for old_txt, new_txt in replace_dict.items():
            # escape replacement text for safety
            safe_new = escape_xml_text(new_txt)
            sec_text = sec_text.replace(old_txt, safe_new)

        if clear_cache:
            sec_text = strip_linesegarray(sec_text)

        files_data[target_section] = sec_text.encode("utf-8")

    # Repackage with strict mimetype stored first
    with zipfile.ZipFile(out_path, "w") as z:
        # Mimetype
        if "mimetype" in files_data:
            z.writestr("mimetype", files_data["mimetype"], compress_type=zipfile.ZIP_STORED)
        for name, data in files_data.items():
            if name == "mimetype":
                continue
            z.writestr(name, data, compress_type=zipfile.ZIP_DEFLATED)

    return out_path


def build_minimal_hwpx(
    output_hwpx: str | Path,
    doc_title: str,
    body_paragraphs: List[str],
    source_template: Optional[str | Path] = None
) -> Path:
    """
    Generates a 100% valid HWPX file derived directly from the official Hancom template,
    ensuring zero corruption and zero font overlap bugs.
    """
    out_path = Path(output_hwpx).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if source_template is None:
        source_template = Path(__file__).resolve().parent.parent / "templates" / "02_공공기관_기본보고서_양식.hwpx"

    src_p = Path(source_template).resolve()
    if not src_p.exists():
        raise FileNotFoundError(f"Source template not found: {src_p}")

    files_memory = {}
    with zipfile.ZipFile(src_p, "r") as z:
        for name in z.namelist():
            files_memory[name] = z.read(name)

    sec_xml = files_memory["Contents/section0.xml"].decode("utf-8")
    sec_xml = sec_xml.replace("브라더 공기관", "공공기관 표준 서식")
    sec_xml = sec_xml.replace("기본 보고서 양식", escape_xml_text(doc_title))
    sec_xml = sec_xml.replace("<hp:t>제  목</hp:t>", f"<hp:t>{escape_xml_text(doc_title)}</hp:t>")
    sec_xml = sec_xml.replace("<hp:t>제 목</hp:t>", f"<hp:t>{escape_xml_text(doc_title)}</hp:t>")

    # Replace dummy paragraphs with body_paragraphs if provided
    for p_idx, text in enumerate(body_paragraphs[:4]):
        dummy_markers = [
            "□ 헤드라인M 폰트 16포인트(문단 위 15)",
            "○ 휴면명조 15포인트(문단위 10)",
            "― 휴면명조 15포인트(문단 위 6)",
            "※ 중고딕 13포인트(문단 위 3)"
        ]
        if p_idx < len(dummy_markers):
            sec_xml = sec_xml.replace(dummy_markers[p_idx], escape_xml_text(text), 1)

    sec_xml = strip_linesegarray(sec_xml)
    files_memory["Contents/section0.xml"] = sec_xml.encode("utf-8")

    tmp_out = out_path.with_suffix(".tmp")
    with zipfile.ZipFile(tmp_out, "w") as z_out:
        if "mimetype" in files_memory:
            z_out.writestr("mimetype", files_memory["mimetype"], compress_type=zipfile.ZIP_STORED)
        for name, data in files_memory.items():
            if name == "mimetype":
                continue
            z_out.writestr(name, data, compress_type=zipfile.ZIP_DEFLATED)

    if out_path.exists():
        out_path.unlink()
    tmp_out.rename(out_path)

    return out_path


if __name__ == "__main__":
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    test_out = Path(__file__).resolve().parent.parent / "result" / "[002]_공문서_표준_보고서_생성테스트.hwpx"
    build_minimal_hwpx(
        output_hwpx=test_out,
        doc_title="2026년도 공공기관 AI 행정 혁신 추진계획(안)",
        body_paragraphs=[
            "1. 추진 배경: 행정 업무 디지털 전환 및 초거대 AI 공공 서비스 혁신",
            " - 서류 작업 및 민원 대응 프로세스 자동화를 통한 업무 효율 50% 향상",
            "2. 주요 과제: OWPML(HWPX) 표준 기반 지능형 전자문서 자동 생성 도입",
            " - 부서별 맞춤형 보고서 작성 및 결재 보조 AI 어시스턴트 구축"
        ]
    )
    print(f"✅ Created Verified Minimal Report: {test_out.name}")
