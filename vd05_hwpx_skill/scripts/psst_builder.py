#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
2026 PSST Government Grant Business Plan Generator (psst_builder.py)
Builds 100% compliant 초기창업패키지 / 예비창업패키지 standard HWPX business plans.
"""

from __future__ import annotations

import zipfile
from pathlib import Path
from typing import Dict, Any, Optional

from hwpx_engine import escape_xml_text, strip_linesegarray


def build_psst_hwpx(
    output_path: str | Path,
    doc_title: str = "2026년도 초기창업패키지(일반형) 사업계획서",
    item_name: str = "{{창업아이템명}}",
    ceo_name: str = "{{대표자}}",
    category: str = "{{신청분야}}",
    gov_fund: str = "{{정부지원금}}",
    self_fund: str = "{{자기부담금}}",
    period: str = "{{협약기간}}",
    problem_text: str = "{{문제인식_내용}}",
    solution_text: str = "{{실현가능성_내용}}",
    scaleup_text: str = "{{성장전략_내용}}",
    team_text: str = "{{팀구성_내용}}"
) -> Path:
    """
    Builds an official 4-part PSST business plan HWPX document with valid OWPML schema.
    """
    out_file = Path(output_path).resolve()
    out_file.parent.mkdir(parents=True, exist_ok=True)

    mimetype_val = "application/hwp+zip"
    container_val = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><ocf:container xmlns:ocf="urn:oasis:names:tc:opendocument:xmlns:container"><ocf:rootfiles><ocf:rootfile ocf:full-path="Contents/content.hpf" ocf:media-type="application/hwp+zip"/></ocf:rootfiles></ocf:container>'''
    version_val = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><hh:version xmlns:hh="http://www.hancom.co.kr/hwpml/2011/head" major="5" minor="0" micro="0" buildNumber="0" os="1" xmlVersion="1.0"/>'''
    hpf_val = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?><opf:package xmlns:opf="http://www.idpf.org/2007/opf" version="2.0" unique-identifier="BookId"><opf:metadata><dc:title xmlns:dc="http://purl.org/dc/elements/1.1/">{escape_xml_text(doc_title)}</dc:title><dc:language xmlns:dc="http://purl.org/dc/elements/1.1/">ko</dc:language></opf:metadata><opf:manifest><opf:item id="header" href="header.xml" media-type="application/xml"/><opf:item id="section0" href="section0.xml" media-type="application/xml"/></opf:manifest><opf:spine><opf:itemref idref="header"/><opf:itemref idref="section0"/></opf:spine></opf:package>'''

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
<hh:charProperties itemCnt="4">
<hh:charPr id="0" height="1000" textColor="#000000"><hh:fontRef hangul="0" latin="0" hanja="0" japanese="0" other="0" symbol="0" user="0"/></hh:charPr>
<hh:charPr id="1" height="1000" textColor="#000000" bold="1"><hh:fontRef hangul="0" latin="0" hanja="0" japanese="0" other="0" symbol="0" user="0"/></hh:charPr>
<hh:charPr id="2" height="1600" textColor="#003366" bold="1"><hh:fontRef hangul="0" latin="0" hanja="0" japanese="0" other="0" symbol="0" user="0"/></hh:charPr>
<hh:charPr id="3" height="1200" textColor="#004085" bold="1"><hh:fontRef hangul="0" latin="0" hanja="0" japanese="0" other="0" symbol="0" user="0"/></hh:charPr>
</hh:charProperties>
<hh:tabProperties itemCnt="1"><hh:tabPr id="0"/></hh:tabProperties>
<hh:paraProperties itemCnt="3">
<hh:paraPr id="0" align="left"><hh:lineSpacing type="percent" value="160" unit="percent"/></hh:paraPr>
<hh:paraPr id="1" align="center"><hh:lineSpacing type="percent" value="130" unit="percent"/></hh:paraPr>
<hh:paraPr id="2" align="left"><hh:margin><hh:left value="5" unit="pt"/><hh:right value="5" unit="pt"/></hh:margin><hh:lineSpacing type="percent" value="150" unit="percent"/></hh:paraPr>
</hh:paraProperties>
<hh:styles itemCnt="1"><hh:style id="0" type="para" name="바탕글" engName="Normal" paraPrIDRef="0" charPrIDRef="0"/></hh:styles>
</hh:refList>
<hh:docPr><hh:idMappings fontfaceCnt="1" borderFillCnt="3" charPrCnt="4" tabPrCnt="1" paraPrCnt="3" styleCnt="1"/></hh:docPr>
</hh:head>'''

    # Table: 4 rows summary
    tbl_xml = f'''
<hp:tbl id="1" zOrder="0" numberingType="none" textWrap="square" textFlow="bothSides" lock="0" dropCapstyle="none" pageBreak="0" repeatHeader="0" rowCnt="4" colCnt="4" cellSpacing="0" borderFillIDRef="2">
<hp:sz width="42520" widthRelTo="absolute" height="11200" heightRelTo="absolute" protect="0"/>
<hp:pos treatAsChar="1"/><hp:inMargin left="0" right="0" top="0" bottom="0"/>
<hp:tr>
<hp:tc name="" header="0" hasMargin="1" protect="0" editable="0" dirty="0" borderFillIDRef="2">
<hp:cellMargin left="500" right="500" top="300" bottom="300"/><hp:subList id="0" textDirection="0" lineWrap="break" vertAlign="center" linkListIDRef="0">
<hp:p id="0" paraPrIDRef="1" styleIDRef="0"><hp:run charPrIDRef="1"><hp:t>창업아이템명</hp:t></hp:run></hp:p></hp:subList>
<hp:cellAddr colAddr="0" rowAddr="0"/><hp:cellSpan colSpan="1" rowSpan="1"/><hp:cellSz width="9000" height="2800"/>
</hp:tc>
<hp:tc name="" header="0" hasMargin="1" protect="0" editable="0" dirty="0" borderFillIDRef="3">
<hp:cellMargin left="500" right="500" top="300" bottom="300"/><hp:subList id="0" textDirection="0" lineWrap="break" vertAlign="center" linkListIDRef="0">
<hp:p id="0" paraPrIDRef="2" styleIDRef="0"><hp:run charPrIDRef="0"><hp:t>{escape_xml_text(item_name)}</hp:t></hp:run></hp:p></hp:subList>
<hp:cellAddr colAddr="1" rowAddr="0"/><hp:cellSpan colSpan="3" rowSpan="1"/><hp:cellSz width="33520" height="2800"/>
</hp:tc>
</hp:tr>
<hp:tr>
<hp:tc name="" header="0" hasMargin="1" protect="0" editable="0" dirty="0" borderFillIDRef="2">
<hp:cellMargin left="500" right="500" top="300" bottom="300"/><hp:subList id="0" textDirection="0" lineWrap="break" vertAlign="center" linkListIDRef="0">
<hp:p id="0" paraPrIDRef="1" styleIDRef="0"><hp:run charPrIDRef="1"><hp:t>대표자 성명</hp:t></hp:run></hp:p></hp:subList>
<hp:cellAddr colAddr="0" rowAddr="1"/><hp:cellSpan colSpan="1" rowSpan="1"/><hp:cellSz width="9000" height="2800"/>
</hp:tc>
<hp:tc name="" header="0" hasMargin="1" protect="0" editable="0" dirty="0" borderFillIDRef="3">
<hp:cellMargin left="500" right="500" top="300" bottom="300"/><hp:subList id="0" textDirection="0" lineWrap="break" vertAlign="center" linkListIDRef="0">
<hp:p id="0" paraPrIDRef="2" styleIDRef="0"><hp:run charPrIDRef="0"><hp:t>{escape_xml_text(ceo_name)}</hp:t></hp:run></hp:p></hp:subList>
<hp:cellAddr colAddr="1" rowAddr="1"/><hp:cellSpan colSpan="1" rowSpan="1"/><hp:cellSz width="12260" height="2800"/>
</hp:tc>
<hp:tc name="" header="0" hasMargin="1" protect="0" editable="0" dirty="0" borderFillIDRef="2">
<hp:cellMargin left="500" right="500" top="300" bottom="300"/><hp:subList id="0" textDirection="0" lineWrap="break" vertAlign="center" linkListIDRef="0">
<hp:p id="0" paraPrIDRef="1" styleIDRef="0"><hp:run charPrIDRef="1"><hp:t>신청 분야</hp:t></hp:run></hp:p></hp:subList>
<hp:cellAddr colAddr="2" rowAddr="1"/><hp:cellSpan colSpan="1" rowSpan="1"/><hp:cellSz width="9000" height="2800"/>
</hp:tc>
<hp:tc name="" header="0" hasMargin="1" protect="0" editable="0" dirty="0" borderFillIDRef="3">
<hp:cellMargin left="500" right="500" top="300" bottom="300"/><hp:subList id="0" textDirection="0" lineWrap="break" vertAlign="center" linkListIDRef="0">
<hp:p id="0" paraPrIDRef="2" styleIDRef="0"><hp:run charPrIDRef="0"><hp:t>{escape_xml_text(category)}</hp:t></hp:run></hp:p></hp:subList>
<hp:cellAddr colAddr="3" rowAddr="1"/><hp:cellSpan colSpan="1" rowSpan="1"/><hp:cellSz width="12260" height="2800"/>
</hp:tc>
</hp:tr>
<hp:tr>
<hp:tc name="" header="0" hasMargin="1" protect="0" editable="0" dirty="0" borderFillIDRef="2">
<hp:cellMargin left="500" right="500" top="300" bottom="300"/><hp:subList id="0" textDirection="0" lineWrap="break" vertAlign="center" linkListIDRef="0">
<hp:p id="0" paraPrIDRef="1" styleIDRef="0"><hp:run charPrIDRef="1"><hp:t>정부지원금</hp:t></hp:run></hp:p></hp:subList>
<hp:cellAddr colAddr="0" rowAddr="2"/><hp:cellSpan colSpan="1" rowSpan="1"/><hp:cellSz width="9000" height="2800"/>
</hp:tc>
<hp:tc name="" header="0" hasMargin="1" protect="0" editable="0" dirty="0" borderFillIDRef="3">
<hp:cellMargin left="500" right="500" top="300" bottom="300"/><hp:subList id="0" textDirection="0" lineWrap="break" vertAlign="center" linkListIDRef="0">
<hp:p id="0" paraPrIDRef="2" styleIDRef="0"><hp:run charPrIDRef="0"><hp:t>{escape_xml_text(gov_fund)}</hp:t></hp:run></hp:p></hp:subList>
<hp:cellAddr colAddr="1" rowAddr="2"/><hp:cellSpan colSpan="1" rowSpan="1"/><hp:cellSz width="12260" height="2800"/>
</hp:tc>
<hp:tc name="" header="0" hasMargin="1" protect="0" editable="0" dirty="0" borderFillIDRef="2">
<hp:cellMargin left="500" right="500" top="300" bottom="300"/><hp:subList id="0" textDirection="0" lineWrap="break" vertAlign="center" linkListIDRef="0">
<hp:p id="0" paraPrIDRef="1" styleIDRef="0"><hp:run charPrIDRef="1"><hp:t>자기부담금</hp:t></hp:run></hp:p></hp:subList>
<hp:cellAddr colAddr="2" rowAddr="2"/><hp:cellSpan colSpan="1" rowSpan="1"/><hp:cellSz width="9000" height="2800"/>
</hp:tc>
<hp:tc name="" header="0" hasMargin="1" protect="0" editable="0" dirty="0" borderFillIDRef="3">
<hp:cellMargin left="500" right="500" top="300" bottom="300"/><hp:subList id="0" textDirection="0" lineWrap="break" vertAlign="center" linkListIDRef="0">
<hp:p id="0" paraPrIDRef="2" styleIDRef="0"><hp:run charPrIDRef="0"><hp:t>{escape_xml_text(self_fund)}</hp:t></hp:run></hp:p></hp:subList>
<hp:cellAddr colAddr="3" rowAddr="2"/><hp:cellSpan colSpan="1" rowSpan="1"/><hp:cellSz width="12260" height="2800"/>
</hp:tc>
</hp:tr>
<hp:tr>
<hp:tc name="" header="0" hasMargin="1" protect="0" editable="0" dirty="0" borderFillIDRef="2">
<hp:cellMargin left="500" right="500" top="300" bottom="300"/><hp:subList id="0" textDirection="0" lineWrap="break" vertAlign="center" linkListIDRef="0">
<hp:p id="0" paraPrIDRef="1" styleIDRef="0"><hp:run charPrIDRef="1"><hp:t>협약 기간</hp:t></hp:run></hp:p></hp:subList>
<hp:cellAddr colAddr="0" rowAddr="3"/><hp:cellSpan colSpan="1" rowSpan="1"/><hp:cellSz width="9000" height="2800"/>
</hp:tc>
<hp:tc name="" header="0" hasMargin="1" protect="0" editable="0" dirty="0" borderFillIDRef="3">
<hp:cellMargin left="500" right="500" top="300" bottom="300"/><hp:subList id="0" textDirection="0" lineWrap="break" vertAlign="center" linkListIDRef="0">
<hp:p id="0" paraPrIDRef="2" styleIDRef="0"><hp:run charPrIDRef="0"><hp:t>{escape_xml_text(period)}</hp:t></hp:run></hp:p></hp:subList>
<hp:cellAddr colAddr="1" rowAddr="3"/><hp:cellSpan colSpan="3" rowSpan="1"/><hp:cellSz width="33520" height="2800"/>
</hp:tc>
</hp:tr>
</hp:tbl>'''

    def make_paragraphs(text: str, start_id: int) -> list[str]:
        lines = text.strip().split("\n")
        res = []
        for i, line in enumerate(lines):
            res.append(f'<hp:p id="{start_id + i}" paraPrIDRef="2" styleIDRef="0"><hp:run charPrIDRef="0"><hp:t>{escape_xml_text(line)}</hp:t></hp:run></hp:p>')
        return res

    p1_xmls = make_paragraphs(problem_text, 6)
    p2_xmls = make_paragraphs(solution_text, 100)
    p3_xmls = make_paragraphs(scaleup_text, 200)
    p4_xmls = make_paragraphs(team_text, 300)

    sec_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<hs:sec xmlns:hs="http://www.hancom.co.kr/hwpml/2011/section" xmlns:hp="http://www.hancom.co.kr/hwpml/2011/paragraph">
<hp:p id="0" paraPrIDRef="1" styleIDRef="0"><hp:run charPrIDRef="2"><hp:t>■ {escape_xml_text(doc_title)}</hp:t></hp:run></hp:p>
<hp:p id="1" paraPrIDRef="0" styleIDRef="0"><hp:run charPrIDRef="0"><hp:t></hp:t></hp:run></hp:p>
<hp:p id="2" paraPrIDRef="0" styleIDRef="0"><hp:run charPrIDRef="0">{tbl_xml}</hp:run></hp:p>
<hp:p id="3" paraPrIDRef="0" styleIDRef="0"><hp:run charPrIDRef="0"><hp:t></hp:t></hp:run></hp:p>
<hp:p id="4" paraPrIDRef="0" styleIDRef="0"><hp:run charPrIDRef="3"><hp:t>1. 문제 인식 (Problem)</hp:t></hp:run></hp:p>
<hp:p id="5" paraPrIDRef="0" styleIDRef="0"><hp:run charPrIDRef="1"><hp:t> 1-1. 창업아이템의 개발 배경 및 필요성</hp:t></hp:run></hp:p>
{"".join(p1_xmls)}
<hp:p id="90" paraPrIDRef="0" styleIDRef="0"><hp:run charPrIDRef="0"><hp:t></hp:t></hp:run></hp:p>
<hp:p id="91" paraPrIDRef="0" styleIDRef="0"><hp:run charPrIDRef="3"><hp:t>2. 실현 가능성 (Solution)</hp:t></hp:run></hp:p>
<hp:p id="92" paraPrIDRef="0" styleIDRef="0"><hp:run charPrIDRef="1"><hp:t> 2-1. 창업아이템의 핵심 기능 및 차별성</hp:t></hp:run></hp:p>
{"".join(p2_xmls)}
<hp:p id="190" paraPrIDRef="0" styleIDRef="0"><hp:run charPrIDRef="0"><hp:t></hp:t></hp:run></hp:p>
<hp:p id="191" paraPrIDRef="0" styleIDRef="0"><hp:run charPrIDRef="3"><hp:t>3. 성장 전략 (Scale-up)</hp:t></hp:run></hp:p>
<hp:p id="192" paraPrIDRef="0" styleIDRef="0"><hp:run charPrIDRef="1"><hp:t> 3-1. 비즈니스 모델(수익화) 및 시장 진입 계획</hp:t></hp:run></hp:p>
{"".join(p3_xmls)}
<hp:p id="290" paraPrIDRef="0" styleIDRef="0"><hp:run charPrIDRef="0"><hp:t></hp:t></hp:run></hp:p>
<hp:p id="291" paraPrIDRef="0" styleIDRef="0"><hp:run charPrIDRef="3"><hp:t>4. 팀 구성 (Team)</hp:t></hp:run></hp:p>
<hp:p id="292" paraPrIDRef="0" styleIDRef="0"><hp:run charPrIDRef="1"><hp:t> 4-1. 대표자 및 핵심 팀원의 보유 역량</hp:t></hp:run></hp:p>
{"".join(p4_xmls)}
</hs:sec>'''

    with zipfile.ZipFile(out_file, "w") as z:
        z.writestr("mimetype", mimetype_val, compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml", container_val.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("version.xml", version_val.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("Contents/content.hpf", hpf_val.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("Contents/header.xml", header_xml.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("Contents/section0.xml", sec_xml.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)

    return out_file


if __name__ == "__main__":
    import sys
    if sys.platform == "win32":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    base_dir = Path(__file__).resolve().parent.parent
    templates_dir = base_dir / "templates"
    result_dir = base_dir / "result"
    templates_dir.mkdir(parents=True, exist_ok=True)
    result_dir.mkdir(parents=True, exist_ok=True)

    # 1. Create Template (with placeholders)
    tmpl_path = templates_dir / "01_초기창업패키지_사업계획서_표준양식.hwpx"
    build_psst_hwpx(
        output_path=tmpl_path,
        doc_title="2026년도 초기창업패키지(일반형) 사업계획서",
        item_name="{{창업아이템명}}",
        ceo_name="{{대표자}}",
        category="{{신청분야}}",
        gov_fund="{{정부지원금}}",
        self_fund="{{자기부담금}}",
        period="{{협약기간}}",
        problem_text="[문제인식 개요]\n- 대상 문제 및 해결 필요성을 기술하십시오.\n- 기존 시장의 한계 및 디지털 정보격차 현황",
        solution_text="[실현가능성 개요]\n- 창업아이템의 핵심 개발 내용 및 추진 계획을 기술하십시오.\n- 주요 기술적 차별성 및 구현 방안",
        scaleup_text="[성장전략 개요]\n- 비즈니스 모델(수익화) 및 시장 진입 계획을 기술하십시오.\n- 국내외 판로 개척 및 자금 조달 계획",
        team_text="[팀구성 개요]\n- 대표자 및 팀원의 보유 역량과 역할을 기술하십시오.\n- 기술 개발 및 사업화 전담 인력 구성 현황"
    )
    print(f"✅ Created Template: {tmpl_path.name}")

    # 2. Create Filled Sample Document
    res_path = result_dir / "[001]_2026_초기창업패키지_사업계획서_완성본.hwpx"
    build_psst_hwpx(
        output_path=res_path,
        doc_title="2026년도 초기창업패키지(일반형) 사업계획서",
        item_name="시니어 디지털 케어를 위한 실버 세대 맞춤형 AI 전자책 & 인터랙티브 가이드 플랫폼",
        ceo_name="이한규 ((AX)창업기술)",
        category="AI / 에듀테크 / 시니어 케어",
        gov_fund="70,000,000원",
        self_fund="30,000,000원 (현금 10,000,000원 / 현물 20,000,000원)",
        period="2026.05.01 ~ 2027.02.28 (10개월)",
        problem_text="■ 1-1. 창업아이템의 개발 동기 및 필요성\n"
                     "  - 대한민국 초고령화 사회 진입에 따른 시니어 층의 디지털 정보 격차(Digital Divide) 심화\n"
                     "  - 스마트폰, 모바일 뱅킹, 무인 키오스크 등 일상 필수 디지털 환경에서의 소외 현상 지속 발생\n"
                     "  - 기존 종이 교재는 작은 폰트와 난해한 기술 용어로 인해 시니어의 자기주도 학습 한계 봉착\n\n"
                     "■ 1-2. 목표 시장의 미충족 수요(Unmet Needs) 분석\n"
                     "  - 60대 이상 시니어 세대의 82.4%가 대화형/시각 중심의 쉬운 디지털 교육 콘텐츠 필요성 응답\n"
                     "  - 지자체 및 평생학습관의 시니어 디지털 강사 인력 부족으로 1:1 맞춤형 피드백 제공 불가능",
        solution_text="■ 2-1. 창업아이템의 핵심 기능 및 구현 방안\n"
                      "  - 실버 세대 특화 대화형 음성 AI 인터랙티브 전자책 엔진(HWPX 기반 가이드 뷰어 연동)\n"
                      "  - 큰 글씨(Large Font UI, 가독성 최적화), 쉬운 우리말 용어 순화 번역 모듈 탑재\n"
                      "  - 키오스크/금융앱 화면을 직접 터치해보며 학습하는 단계별 가상 시뮬레이터 내장\n\n"
                      "■ 2-2. 경쟁 기술 대비 차별적 우위성\n"
                      "  - 단순 텍스트 e-Book 대비 학습 완료율 3.8배 향상, 질문 응답 대기시간 1초 이내 달성\n"
                      "  - OWPML(HWPX) 표준 서식과의 완벽한 호환을 통해 공공기관 교육 표준 교안으로 즉시 채택 가능",
        scaleup_text="■ 3-1. 비즈니스 모델(BM) 및 수익화 전략\n"
                     "  - B2G: 전국 250개 시·군·구 지자체 평생학습관 및 노인종합복지관 대상 기관 라이선스 공급\n"
                     "  - B2B: 시니어 케어 전문 기업 및 요양·간병 플랫폼 대상 AI 콘텐츠 임베디드 API 공급\n"
                     "  - B2C: 프리미엄 디지털 케어 구독 서비스(월 9,900원) 및 가정용 스마트 태블릿 패키지 판매\n\n"
                     "■ 3-2. 연도별 매출 및 시장 진입 로드맵\n"
                     "  - 2026년(1차년도): 수도권 30개 거점 복지관 시범 도입 및 공공 조달 등록 (매출 3.5억원)\n"
                     "  - 2027년(2차년도): 전국 거점망 확대 및 시니어 헬스케어 결합 서비스 론칭 (매출 12억원)\n"
                     "  - 2028년(3차년도): 글로벌 K-실버 에듀테크 수출(동아시아 초고령 국가) (매출 30억원 달성)",
        team_text="■ 4-1. 대표자 및 핵심 인력 역량\n"
                  "  - 대표자(이한규): (AX)창업기술 대표, 기술 기반 창업 15년 및 시니어 에듀테크 기획 총괄\n"
                  "  - AI 총괄 CTO: 생성형 AI 모델 파인튜닝 및 음성 STT/TTS 파이프라인 개발 8년 경력\n"
                  "  - 서비스 기획/디자인: 실버 세대 UX/UI 및 공공기관 웹 접근성(A11y) 인증 프로젝트 6년 경력\n\n"
                  "■ 4-2. 파트너십 및 네트워크 현황\n"
                  "  - 주요 시니어 복지재단 및 평생교육협회와의 업무협약(MOU) 기체결\n"
                  "  - 클라우드 인프라 및 생성형 AI 기술 지원 파트너십 구축 완료"
    )
    print(f"✅ Created Sample Result: {res_path.name}")
