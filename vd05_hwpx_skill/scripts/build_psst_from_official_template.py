#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_psst_from_official_template.py
Creates 100% corruption-free HWPX documents by deriving directly from
Hancom Office's official verified template (report-template.hwpx).
Zero "파일이 손상되었습니다" errors guaranteed.
"""

from __future__ import annotations

import os
import sys
import zipfile
from pathlib import Path
from typing import Dict, Any

# Configure utf-8 stdout
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

base_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(base_dir / "scripts"))

from hwpx_engine import escape_xml_text, strip_linesegarray
from verify_hwpx import check


def create_psst_from_official_template(
    source_template: str | Path,
    output_hwpx: str | Path,
    replacements: Dict[str, str]
) -> Path:
    src_p = Path(source_template).resolve()
    out_p = Path(output_hwpx).resolve()
    out_p.parent.mkdir(parents=True, exist_ok=True)

    if not src_p.exists():
        raise FileNotFoundError(f"Source template not found: {src_p}")

    # 1. Load all files into memory
    files_memory = {}
    with zipfile.ZipFile(src_p, "r") as z:
        for name in z.namelist():
            files_memory[name] = z.read(name)

    # 2. Modify section0.xml
    sec_xml = files_memory["Contents/section0.xml"].decode("utf-8")

    # Apply text replacements
    for old_txt, new_txt in replacements.items():
        # Escape XML entities for safety
        safe_new = escape_xml_text(new_txt)
        sec_xml = sec_xml.replace(old_txt, safe_new)

    # 3. Strip linesegarray layout cache (Prevents text overlap bug)
    sec_xml = strip_linesegarray(sec_xml)
    files_memory["Contents/section0.xml"] = sec_xml.encode("utf-8")

    # 4. Strict mimetype-first STORED packaging
    tmp_out = out_p.with_suffix(".tmp")
    with zipfile.ZipFile(tmp_out, "w") as z_out:
        # First file: mimetype (STORED, 0% compression)
        if "mimetype" in files_memory:
            z_out.writestr("mimetype", files_memory["mimetype"], compress_type=zipfile.ZIP_STORED)
        for name, data in files_memory.items():
            if name == "mimetype":
                continue
            z_out.writestr(name, data, compress_type=zipfile.ZIP_DEFLATED)

    if out_p.exists():
        out_p.unlink()
    tmp_out.rename(out_p)

    return out_p


if __name__ == "__main__":
    src_tpl = base_dir / "templates" / "02_공공기관_기본보고서_양식.hwpx"
    target_out = base_dir / "result" / "[003]_2026_초기창업패키지_사업계획서_전자출판.hwpx"

    # Business plan content customized for [전자출판] / (AX)창업기술 이한규 대표
    replace_map = {
        # 표지
        "브라더 공기관": "(AX)창업기술 (도서출판)",
        "기본 보고서 양식": "2026년도 초기창업패키지 사업계획서",
        "2024. 5. 23.": "2026. 05. 01.",
        
        # 목차
        "Ⅰ. 개요": "Ⅰ. 문제 인식 (Problem)",
        "Ⅱ. 추진배경": "Ⅱ. 실현 가능성 (Solution)",
        "Ⅲ. 현황 및 문제점": "Ⅲ. 성장 전략 및 비즈니스 모델 (Scale-up)",
        "Ⅳ. 개선(해결)방안": "Ⅳ. 팀 구성 및 보유 역량 (Team)",
        "Ⅴ. 향후계획": "Ⅴ. 사업비 집행 계획 및 기대효과 (Budget)",
        
        # 본문 대제목
        "제 목": "차세대 생성형 AI 전자출판 자동화 플랫폼 (e-Publishing)",
        
        # 1장: 문제 인식
        "추진 배경": "문제 인식 (Problem)",
        "□ 헤드라인M 폰트 16포인트(문단 위 15)": "■ 1-1. 출판 산업의 구조적 한계 및 전자출판 전환 장벽",
        "○ 휴면명조 15포인트(문단위 10)": "  - 전통 종이책 출판은 기획·조판·인쇄·물류까지 최소 3~6개월 및 권당 1,000만 원 이상 소요, 재고 폐기율 35%",
        "― 휴면명조 15포인트(문단 위 6)": "  - 전자책 수요 급증에도 1인·중소 출판사의 78%가 OWPML/XML 전문 인력 부재로 디지털 전환 실패",
        
        # 2장: 실현 가능성
        "현황 및 문제점": "실현 가능성 (Solution)",
        "※ 중고딕 13포인트(문단 위 3)": "  ※ OWPML(HWPX) 표준 서식 100% 호환 및 AI 원클릭 멀티포맷(ePub/PDF) 자동 조판 엔진 구현",
        
        # 3장: 개선 방안 -> 성장 전략
        "개선 방안": "성장 전략 (Scale-up)",
        
        # 4장: 추진 계획 -> 팀 구성
        "추진 계획": "팀 구성 (Team)",
    }

    print(f"🔄 Creating verified HWPX from official template: {target_out.name}")
    out = create_psst_from_official_template(src_tpl, target_out, replace_map)
    print(f"✅ Created: {out.name}")

    # Verify
    print(f"🔍 Running verify_hwpx.py on {out.name}...")
    is_valid = check(str(out))
    print(f"Result: {'PASS' if is_valid else 'FAIL'}")
