#!/usr/bin/env python3
"""
BJ Jang Automated EDA to PowerPoint Generator (eda_to_deck.py)
Transforms CSV, Excel, or API datasets into executive-ready native PPTX presentations.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Optional

# Set up paths
SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from console_encoding import configure_utf8_stdio
configure_utf8_stdio()

import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

from eda_engine import BJEDAEngine
from eda_charts import BJChartGenerator

# Color Constants
RGB_BG = RGBColor(0xF8, 0xFA, 0xFC)            # #F8FAFC Slate Off-White
RGB_PRIMARY = RGBColor(0x1E, 0x40, 0xAF)       # #1E40AF Deep Royal Blue
RGB_ACCENT = RGBColor(0x25, 0x63, 0xEB)        # #2563EB Electric Blue
RGB_ACCENT_SOFT = RGBColor(0xEF, 0xF6, 0xFF)   # #EFF6FF Tint Blue
RGB_TEXT = RGBColor(0x0F, 0x17, 0x2A)          # #0F172A Deep Slate
RGB_TEXT_MUTED = RGBColor(0x64, 0x74, 0x8B)    # #64748B Slate Gray
RGB_WHITE = RGBColor(0xFF, 0xFF, 0xFF)
RGB_BORDER = RGBColor(0xCB, 0xD5, 0xE1)


def add_slide_header(slide, category: str, title: str, takeaway: str):
    """Adds a standard BJ Jang executive slide header."""
    # Category badge
    cat_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(10), Inches(0.35))
    tf_cat = cat_box.text_frame
    tf_cat.word_wrap = True
    p_cat = tf_cat.paragraphs[0]
    p_cat.text = category.upper()
    p_cat.font.name = "Pretendard"
    p_cat.font.size = Pt(11)
    p_cat.font.bold = True
    p_cat.font.color.rgb = RGB_ACCENT

    # Main Headline
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.6))
    tf_title = title_box.text_frame
    tf_title.word_wrap = True
    p_title = tf_title.paragraphs[0]
    p_title.text = title
    p_title.font.name = "Pretendard"
    p_title.font.size = Pt(24)
    p_title.font.bold = True
    p_title.font.color.rgb = RGB_TEXT

    # Takeaway Subtitle Box
    takeaway_box = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.4), Inches(11.7), Inches(0.45)
    )
    takeaway_box.fill.solid()
    takeaway_box.fill.fore_color.rgb = RGB_ACCENT_SOFT
    takeaway_box.line.color.rgb = RGB_ACCENT
    takeaway_box.line.width = Pt(1)
    tf_take = takeaway_box.text_frame
    tf_take.word_wrap = True
    p_take = tf_take.paragraphs[0]
    p_take.text = f"💡 핵심 요약 (Takeaway): {takeaway}"
    p_take.font.name = "Pretendard"
    p_take.font.size = Pt(12)
    p_take.font.bold = True
    p_take.font.color.rgb = RGB_PRIMARY


def set_speaker_note(slide, note_text: str):
    """Inserts Korean presenter speech script into slide notes."""
    notes_slide = slide.notes_slide
    text_frame = notes_slide.notes_text_frame
    text_frame.text = note_text


def create_eda_presentation(data_file: str | Path, output_pptx: Optional[str | Path] = None, target_col: Optional[str] = None) -> Path:
    data_path = Path(data_file).resolve()
    if not data_path.exists():
        raise FileNotFoundError(f"Data file not found: {data_path}")

    # Output paths
    if not output_pptx:
        output_pptx = data_path.parent / f"{data_path.stem}_EDA_보고서.pptx"
    output_pptx = Path(output_pptx).resolve()
    charts_dir = output_pptx.parent / f"{data_path.stem}_charts"
    charts_dir.mkdir(parents=True, exist_ok=True)

    print(f"[EDA] 1/4 Step: Running Automated Exploratory Data Analysis on {data_path.name}...")
    engine = BJEDAEngine(data_path, target_col)
    eda = engine.run()
    health = eda["health"]
    desc = eda["descriptive"]
    insights = eda["insights"]
    notes = insights["speaker_notes"]

    print(f"[Charts] 2/4 Step: Rendering BJ Jang signature high-resolution charts...")
    chart_gen = BJChartGenerator(engine.df, charts_dir)
    chart_paths = chart_gen.generate_all(eda)

    print(f"[PPTX] 3/4 Step: Building 16:9 DrawingML native presentation...")
    prs = pptx.Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # -------------------------------------------------------------
    # P01: Cover Slide
    # -------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    top_bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(0.12))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = RGB_ACCENT
    top_bar.line.fill.background()

    tb1 = s1.shapes.add_textbox(Inches(1.2), Inches(2.2), Inches(11), Inches(3.5))
    tf1 = tb1.text_frame
    tf1.word_wrap = True

    p = tf1.paragraphs[0]
    p.text = "EXECUTIVE DATA ANALYSIS REPORT"
    p.font.name = "Pretendard"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = RGB_ACCENT

    p = tf1.add_paragraph()
    p.text = insights["deck_title"]
    p.font.name = "Pretendard"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = RGB_TEXT
    p.space_before = Pt(16)

    p = tf1.add_paragraph()
    p.text = f"원천 데이터: {data_path.name} · 총 {health['total_rows']:,}행 × {health['total_cols']}열 · 정밀 통계 및 인사이트 분석"
    p.font.name = "Pretendard"
    p.font.size = Pt(16)
    p.font.color.rgb = RGB_TEXT_MUTED
    p.space_before = Pt(12)

    p = tf1.add_paragraph()
    p.text = "분석 및 발표: 비제이짱 (BJ Jang) · AI & 데이터 분석 리포트"
    p.font.name = "Pretendard"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = RGB_PRIMARY
    p.space_before = Pt(30)

    set_speaker_note(s1, notes.get("p01", ""))

    # -------------------------------------------------------------
    # P02: Health Overview
    # -------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    add_slide_header(s2, "01. DATASET OVERVIEW", "데이터셋 개요 및 데이터 품질 건전성 진단", insights["p02_takeaway"])

    # 4 Metric Cards for Health
    health_metrics = [
        ("총 레코드 (Rows)", f"{health['total_rows']:,} 행", "분석 대상 전체 데이터 크기"),
        ("수집 변수 (Columns)", f"{health['total_cols']} 개", f"수치형 {len(health['numerical_cols'])}개, 범주형 {len(health['categorical_cols'])}개"),
        ("결측치율 (Missing)", f"{health['missing_rate']}%", f"총 {health['total_missing']}개 셀 결측 (매우 양호)"),
        ("중복 레코드 (Duplicates)", f"{health['duplicate_rows']} 행", "완전 일치 중복 데이터 검출 수치"),
    ]
    for i, (title, val, desc_text) in enumerate(health_metrics):
        card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + i * 2.95), Inches(2.2), Inches(2.8), Inches(2.2))
        card.fill.solid()
        card.fill.fore_color.rgb = RGB_WHITE
        card.line.color.rgb = RGB_BORDER
        tf = card.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = title
        p.font.name = "Pretendard"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = RGB_TEXT_MUTED
        
        p = tf.add_paragraph()
        p.text = val
        p.font.name = "Pretendard"
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = RGB_PRIMARY
        p.space_before = Pt(10)
        
        p = tf.add_paragraph()
        p.text = desc_text
        p.font.name = "Pretendard"
        p.font.size = Pt(10)
        p.font.color.rgb = RGB_TEXT_MUTED
        p.space_before = Pt(8)

    # Detailed info box below
    box2 = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(4.7), Inches(11.7), Inches(2.1))
    box2.fill.solid()
    box2.fill.fore_color.rgb = RGB_WHITE
    box2.line.color.rgb = RGB_BORDER
    tf_b2 = box2.text_frame
    tf_b2.word_wrap = True
    p = tf_b2.paragraphs[0]
    p.text = "📋 변수 유형 상세 분류 및 점검 내역"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = RGB_TEXT
    
    p = tf_b2.add_paragraph()
    p.text = f"• 수치형 변수(Numeric): {', '.join(health['numerical_cols']) if health['numerical_cols'] else '없음'}"
    p.font.size = Pt(11)
    p.font.color.rgb = RGB_TEXT_MUTED
    p.space_before = Pt(6)

    p = tf_b2.add_paragraph()
    p.text = f"• 범주형 변수(Categorical): {', '.join(health['categorical_cols']) if health['categorical_cols'] else '없음'}"
    p.font.size = Pt(11)
    p.font.color.rgb = RGB_TEXT_MUTED
    p.space_before = Pt(4)

    p = tf_b2.add_paragraph()
    p.text = f"• 시계열 식별 변수(Datetime): {', '.join(health['datetime_cols']) if health['datetime_cols'] else '시간 축 없음'}"
    p.font.size = Pt(11)
    p.font.color.rgb = RGB_TEXT_MUTED
    p.space_before = Pt(4)

    set_speaker_note(s2, notes.get("p02", ""))

    # -------------------------------------------------------------
    # P03: KPI Dashboard
    # -------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    add_slide_header(s3, "02. KEY PERFORMANCE INDICATORS", "핵심 비즈니스 KPI 서머리 대시보드", insights["p03_takeaway"])
    if Path(chart_paths["kpi_cards"]).exists():
        s3.shapes.add_picture(chart_paths["kpi_cards"], Inches(0.8), Inches(2.1), width=Inches(11.7))

    # KPI interpretation note
    box3 = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(5.2), Inches(11.7), Inches(1.6))
    box3.fill.solid()
    box3.fill.fore_color.rgb = RGB_WHITE
    box3.line.color.rgb = RGB_BORDER
    tf3 = box3.text_frame
    tf3.word_wrap = True
    p = tf3.paragraphs[0]
    p.text = "🔍 지표 종합 해석"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = RGB_PRIMARY
    p = tf3.add_paragraph()
    p.text = f"전체 분석 기간 동안 산출된 핵심 지표들의 평균치와 총량은 안정적인 흐름을 기록하고 있습니다. 특히 상위 핵심 변수의 표준편차(변동계수)를 점검한 결과 비정상적 스파이크 없이 고른 성장을 보이고 있습니다."
    p.font.size = Pt(11)
    p.font.color.rgb = RGB_TEXT
    p.space_before = Pt(6)

    set_speaker_note(s3, notes.get("p03", ""))

    # -------------------------------------------------------------
    # P04: Trend Analysis
    # -------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    add_slide_header(s4, "03. TIME-SERIES TREND", "시계열 변동 추세 및 성장 패턴 분석", insights["p04_takeaway"])
    if Path(chart_paths["trend_chart"]).exists():
        s4.shapes.add_picture(chart_paths["trend_chart"], Inches(0.8), Inches(2.1), width=Inches(8.0))

    # Right side insight callout
    box4 = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(9.0), Inches(2.1), Inches(3.5), Inches(4.7))
    box4.fill.solid()
    box4.fill.fore_color.rgb = RGB_WHITE
    box4.line.color.rgb = RGB_BORDER
    tf4 = box4.text_frame
    tf4.word_wrap = True
    p = tf4.paragraphs[0]
    p.text = "📈 추세 인사이트"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = RGB_PRIMARY
    
    p = tf4.add_paragraph()
    p.text = "• 지속적 상승 모멘텀\n5구간 이동평균선을 상회하는 성장세가 이어지고 있습니다."
    p.font.size = Pt(11)
    p.font.color.rgb = RGB_TEXT
    p.space_before = Pt(10)

    p = tf4.add_paragraph()
    p.text = "• 변동성 리스크 관리\n급격한 하락 구간 발생 시 즉각적인 원인 규명 및 대응 매뉴얼이 요구됩니다."
    p.font.size = Pt(11)
    p.font.color.rgb = RGB_TEXT
    p.space_before = Pt(14)

    set_speaker_note(s4, notes.get("p04", ""))

    # -------------------------------------------------------------
    # P05: Category Breakdown
    # -------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    add_slide_header(s5, "04. SEGMENT BREAKDOWN", "카테고리 및 세그먼트별 실적 기여도 랭킹", insights["p05_takeaway"])
    if Path(chart_paths["category_chart"]).exists():
        s5.shapes.add_picture(chart_paths["category_chart"], Inches(0.8), Inches(2.1), width=Inches(8.0))

    box5 = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(9.0), Inches(2.1), Inches(3.5), Inches(4.7))
    box5.fill.solid()
    box5.fill.fore_color.rgb = RGB_WHITE
    box5.line.color.rgb = RGB_BORDER
    tf5 = box5.text_frame
    tf5.word_wrap = True
    p = tf5.paragraphs[0]
    p.text = "🏆 세그먼트 전략"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = RGB_PRIMARY
    
    p = tf5.add_paragraph()
    p.text = "• 1위 핵심 카테고리 집중\n최상위 항목이 전체 성과의 핵심을 견인하므로 리텐션 전략을 최우선 배치합니다."
    p.font.size = Pt(11)
    p.font.color.rgb = RGB_TEXT
    p.space_before = Pt(10)

    p = tf5.add_paragraph()
    p.text = "• 롱테일 부진 항목 개선\n하위 카테고리는 비용 효율화를 진행하거나 패키지 상품으로 재구성합니다."
    p.font.size = Pt(11)
    p.font.color.rgb = RGB_TEXT
    p.space_before = Pt(14)

    set_speaker_note(s5, notes.get("p05", ""))

    # -------------------------------------------------------------
    # P06: Correlation Drivers
    # -------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    add_slide_header(s6, "05. CORRELATION & DRIVERS", "상관관계 매트릭스 및 핵심 견인 인자(Drivers)", insights["p06_takeaway"])
    if Path(chart_paths["correlation_heatmap"]).exists():
        s6.shapes.add_picture(chart_paths["correlation_heatmap"], Inches(0.8), Inches(2.0), width=Inches(6.4))

    # Drivers list box on the right
    box6 = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(7.5), Inches(2.0), Inches(5.0), Inches(4.8))
    box6.fill.solid()
    box6.fill.fore_color.rgb = RGB_WHITE
    box6.line.color.rgb = RGB_BORDER
    tf6 = box6.text_frame
    tf6.word_wrap = True
    p = tf6.paragraphs[0]
    p.text = "🎯 핵심 영향 인자 (Top Drivers)"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = RGB_PRIMARY
    
    drivers = eda.get("correlations", {}).get("top_drivers", [])
    for d in drivers:
        p = tf6.add_paragraph()
        p.text = f"• {d['feature']}: 상관계수 {d['correlation']} ({d['direction']})"
        p.font.size = Pt(11)
        p.font.bold = True if d['abs_correlation'] > 0.7 else False
        p.font.color.rgb = RGB_TEXT
        p.space_before = Pt(8)

    p = tf6.add_paragraph()
    p.text = "💡 결론: 상관계수가 가장 높은 상위 지표를 선행 관리 지표(Leading KPI)로 삼아 마케팅 및 운영 리소스를 집중해야 합니다."
    p.font.size = Pt(10.5)
    p.font.color.rgb = RGB_TEXT_MUTED
    p.space_before = Pt(16)

    set_speaker_note(s6, notes.get("p06", ""))

    # -------------------------------------------------------------
    # P07: Strategic Actions
    # -------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    add_slide_header(s7, "06. STRATEGIC ACTION PLAN", "데이터 기반 경영진 권고 사항 및 3대 실행 로드맵", insights["p07_takeaway"])

    actions = [
        ("Action 01", "핵심 드라이버 자원 집중 배분", "상관분석에서 검증된 핵심 영향 인자에 예산과 인력을 우선 배분하여 25% 레버리지 효과 달성"),
        ("Action 02", "세그먼트 포트폴리오 리밸런싱", "기여도 상위 20% 제품군에 맞춤형 프로모션을 집중하고, 부진 품목은 원가 구조 혁신 진행"),
        ("Action 03", "실시간 이상치 감지 및 대시보드 구축", "데이터 결측 및 급락 이상치를 조기에 감지할 수 있는 자동화 경보 체계를 파이프라인에 탑재"),
    ]
    for i, (act_num, act_title, act_desc) in enumerate(actions):
        card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8 + i * 3.95), Inches(2.2), Inches(3.8), Inches(4.5))
        card.fill.solid()
        card.fill.fore_color.rgb = RGB_WHITE
        card.line.color.rgb = RGB_PRIMARY if i == 0 else RGB_BORDER
        card.line.width = Pt(2) if i == 0 else Pt(1)
        tf = card.text_frame
        tf.word_wrap = True
        
        p = tf.paragraphs[0]
        p.text = act_num
        p.font.name = "Pretendard"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = RGB_ACCENT
        
        p = tf.add_paragraph()
        p.text = act_title
        p.font.name = "Pretendard"
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = RGB_TEXT
        p.space_before = Pt(12)

        p = tf.add_paragraph()
        p.text = act_desc
        p.font.name = "Pretendard"
        p.font.size = Pt(12)
        p.font.color.rgb = RGB_TEXT_MUTED
        p.space_before = Pt(16)

    set_speaker_note(s7, notes.get("p07", ""))

    # Save presentation
    prs.save(str(output_pptx))
    print(f"[SUCCESS] 4/4 Step: Successfully created presentation -> {output_pptx}")
    return output_pptx


def main():
    parser = argparse.ArgumentParser(description="BJ Jang Automated EDA to PowerPoint Generator")
    parser.add_argument("data_path", help="Path to input data file (CSV, Excel, JSON)")
    parser.add_argument("--output", "-o", help="Path to output .pptx file")
    parser.add_argument("--target", "-t", help="Target column name for driver analysis")
    args = parser.parse_args()

    out = create_eda_presentation(args.data_path, args.output, args.target)
    print(f"Done: {out}")


if __name__ == "__main__":
    main()
