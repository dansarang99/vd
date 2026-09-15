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


def build_minimal_hwpx(output_hwpx: str | Path, doc_title: str, body_paragraphs: List[str]) -> Path:
    """
    Generates a 100% valid standalone HWPX file from scratch without external dependencies.
    """
    out_path = Path(output_hwpx).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)

    mimetype_content = "application/hwp+zip"
    container_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<ocf:container xmlns:ocf="urn:oasis:names:tc:opendocument:xmlns:container">
<ocf:rootfiles>
<ocf:rootfile ocf:full-path="Contents/content.hpf" ocf:media-type="application/hwp+zip"/>
</ocf:rootfiles>
</ocf:container>'''

    version_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<hh:version xmlns:hh="http://www.hancom.co.kr/hwpml/2011/head" major="5" minor="0" micro="0" buildNumber="0" os="1" xmlVersion="1.0"/>'''

    content_hpf = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<opf:package xmlns:opf="http://www.idpf.org/2007/opf" version="2.0" unique-identifier="BookId">
<opf:metadata>
<dc:title xmlns:dc="http://purl.org/dc/elements/1.1/">{escape_xml_text(doc_title)}</dc:title>
<dc:language xmlns:dc="http://purl.org/dc/elements/1.1/">ko</dc:language>
</opf:metadata>
<opf:manifest>
<opf:item id="header" href="header.xml" media-type="application/xml"/>
<opf:item id="section0" href="section0.xml" media-type="application/xml"/>
</opf:manifest>
<opf:spine>
<opf:itemref idref="header"/>
<opf:itemref idref="section0"/>
</opf:spine>
</opf:package>'''

    header_xml = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<hh:head xmlns:hh="http://www.hancom.co.kr/hwpml/2011/head" xmlns:hc="http://www.hancom.co.kr/hwpml/2011/core" version="1.0">
<hh:beginNum page="1" footnote="1" endnote="1" pic="1" tbl="1" equation="1"/>
<hh:refList>
<hh:fontfaces itemCnt="1">
<hh:fontface lang="hangul" fontCnt="1"><hh:font id="0" face="맑은 고딕" type="ttf"/></hh:fontface>
<hh:fontface lang="latin" fontCnt="1"><hh:font id="0" face="맑은 고딕" type="ttf"/></hh:fontface>
</hh:fontfaces>
<hh:borderFills itemCnt="3">
<hh:borderFill id="1" backSlash="0" slash="0" counterSlash="0"><hh:leftBorder type="none"/><hh:rightBorder type="none"/><hh:topBorder type="none"/><hh:bottomBorder type="none"/></hh:borderFill>
<hh:borderFill id="2" backSlash="0" slash="0" counterSlash="0">
<hh:leftBorder type="solid" width="0.12 mm" color="#000000"/><hh:rightBorder type="solid" width="0.12 mm" color="#000000"/><hh:topBorder type="solid" width="0.12 mm" color="#000000"/><hh:bottomBorder type="solid" width="0.12 mm" color="#000000"/>
<hh:fillBrush><hh:winBrush faceColor="#EAEEF3" hatchColor="#FF000000" alpha="0"/></hh:fillBrush>
</hh:borderFill>
<hh:borderFill id="3" backSlash="0" slash="0" counterSlash="0">
<hh:leftBorder type="solid" width="0.12 mm" color="#000000"/><hh:rightBorder type="solid" width="0.12 mm" color="#000000"/><hh:topBorder type="solid" width="0.12 mm" color="#000000"/><hh:bottomBorder type="solid" width="0.12 mm" color="#000000"/>
<hh:fillBrush><hh:winBrush faceColor="#FFFFFF" hatchColor="#FF000000" alpha="0"/></hh:fillBrush>
</hh:borderFill>
</hh:borderFills>
<hh:charProperties itemCnt="3">
<hh:charPr id="0" height="1000" textColor="#000000"><hh:fontRef hangul="0" latin="0" hanja="0" japanese="0" other="0" symbol="0" user="0"/></hh:charPr>
<hh:charPr id="1" height="1000" textColor="#111111" bold="1"><hh:fontRef hangul="0" latin="0" hanja="0" japanese="0" other="0" symbol="0" user="0"/></hh:charPr>
<hh:charPr id="2" height="1600" textColor="#003366" bold="1"><hh:fontRef hangul="0" latin="0" hanja="0" japanese="0" other="0" symbol="0" user="0"/></hh:charPr>
</hh:charProperties>
<hh:tabProperties itemCnt="1"><hh:tabPr id="0"/></hh:tabProperties>
<hh:paraProperties itemCnt="3">
<hh:paraPr id="0" align="left"><hh:lineSpacing type="percent" value="160" unit="percent"/></hh:paraPr>
<hh:paraPr id="1" align="center"><hh:lineSpacing type="percent" value="130" unit="percent"/></hh:paraPr>
<hh:paraPr id="2" align="left"><hh:margin><hh:left value="5" unit="pt"/><hh:right value="5" unit="pt"/></hh:margin><hh:lineSpacing type="percent" value="150" unit="percent"/></hh:paraPr>
</hh:paraProperties>
<hh:styles itemCnt="1"><hh:style id="0" type="para" name="바탕글" engName="Normal" paraPrIDRef="0" charPrIDRef="0"/></hh:styles>
</hh:refList>
<hh:docPr><hh:idMappings fontfaceCnt="1" borderFillCnt="3" charPrCnt="3" tabPrCnt="1" paraPrCnt="3" styleCnt="1"/></hh:docPr>
</hh:head>'''

    p_xmls = [
        f'<hp:p id="0" paraPrIDRef="1" styleIDRef="0"><hp:run charPrIDRef="2"><hp:t>■ {escape_xml_text(doc_title)}</hp:t></hp:run></hp:p>',
        '<hp:p id="1" paraPrIDRef="0" styleIDRef="0"><hp:run charPrIDRef="0"><hp:t></hp:t></hp:run></hp:p>'
    ]
    for idx, p in enumerate(body_paragraphs, 2):
        p_xmls.append(f'<hp:p id="{idx}" paraPrIDRef="0" styleIDRef="0"><hp:run charPrIDRef="0"><hp:t>{escape_xml_text(p)}</hp:t></hp:run></hp:p>')

    section0_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<hs:sec xmlns:hs="http://www.hancom.co.kr/hwpml/2011/section" xmlns:hp="http://www.hancom.co.kr/hwpml/2011/paragraph">
{"".join(p_xmls)}
</hs:sec>'''

    with zipfile.ZipFile(out_path, "w") as z:
        z.writestr("mimetype", mimetype_content, compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", container_xml.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("version.xml", version_xml.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("Contents/content.hpf", content_hpf.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("Contents/header.xml", header_xml.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("Contents/section0.xml", section0_xml.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)

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
            "1. 추진 배경 및 필요성",
            " - 행정 업무의 디지털 전환 가속화 및 초거대 AI 기반 공공 서비스 혁신 요구 증대",
            " - 서류 작업 및 민원 대응 프로세스 자동화를 통한 업무 효율성 50% 향상 목표",
            "2. 주요 추진 과제",
            " - OWPML(HWPX) 표준 기반 지능형 전자문서 자동 생성 시스템 도입",
            " - 부서별 맞춤형 보고서 작성 및 결재 보조 AI 어시스턴트 구축",
            "3. 향후 계획",
            " - 2026년 상반기 시범 운영 후 하반기 전 부서 확대 적용"
        ]
    )
    print(f"✅ Created Test Minimal Report: {test_out.name}")
