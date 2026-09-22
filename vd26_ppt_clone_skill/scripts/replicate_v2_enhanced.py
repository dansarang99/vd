"""
replicate_v2_enhanced.py
1:1 정밀 검증 피드백을 100% 반영하여 C-Level 임팩트와 비주얼 완성도를 극대화한 2차 완성형 슬라이드
"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_second_generation_master():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    # 1. 딥 옵시디언 배경
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = RGBColor(8, 12, 20)

    # 2. 카테고리 뱃지
    badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.55), Inches(2.8), Inches(0.35))
    badge.fill.solid()
    badge.fill.fore_color.rgb = RGBColor(16, 26, 46)
    badge.line.color.rgb = RGBColor(59, 130, 246)
    badge.line.width = Pt(1.5)
    tf_b = badge.text_frame
    tf_b.text = "⚡ NEXT-GEN ENTERPRISE AI"
    tf_b.paragraphs[0].font.size = Pt(9.5)
    tf_b.paragraphs[0].font.bold = True
    tf_b.paragraphs[0].font.color.rgb = RGBColor(96, 165, 250)
    tf_b.paragraphs[0].alignment = PP_ALIGN.CENTER

    # 3. 강화된 C-Level 헤드라인
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.05), Inches(11.7), Inches(1.0))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = "엔터프라이즈 AI의 상용화 병목을 해소하는 통합 에이전틱 인프라"
    p_t.font.name = "Pretendard"
    p_t.font.size = Pt(29)
    p_t.font.bold = True
    p_t.font.color.rgb = RGBColor(255, 255, 255)

    p_sub = tf_t.add_paragraph()
    p_sub.text = "데이터 사일로 제거와 지능형 오케스트레이션으로 전사 AI ROI를 10배 가속화합니다."
    p_sub.font.size = Pt(13)
    p_sub.font.color.rgb = RGBColor(148, 163, 184)

    # 4. 고도화된 3열 카드 (가운데 카드 Hero Accent 적용)
    cards = [
        {
            "badge": "DEPLOYMENT SPEED",
            "num": "10x",
            "unit": "FASTER",
            "title": "모델 배포 주기 단축",
            "tags": ["#CI/CD자동화", "#실시간서빙"],
            "desc": "기존 수개월 소요되던 프로덕션 배포 주기를 단 3일 이내로 혁신",
            "is_hero": False
        },
        {
            "badge": "COST EFFICIENCY ★",
            "num": "64%",
            "unit": "TCO DOWN",
            "title": "인프라 운영 비용 절감",
            "tags": ["#GPU가상화", "#동적오케스트레이션"],
            "desc": "유휴 컴퓨팅 자원 제로화 및 인퍼런스 캐싱으로 서버 비용 절감",
            "is_hero": True  # 주인공 카드!
        },
        {
            "badge": "COMPLIANCE & SEC",
            "num": "99.99%",
            "unit": "SLA UPTIME",
            "title": "금융권 무결성 보안",
            "tags": ["#RBAC접근통제", "#데이터계보추적"],
            "desc": "SOC2 및 GDPR 규제를 완벽 준수하는 엔터프라이즈 제로트러스트 체계",
            "is_hero": False
        }
    ]

    card_width = Inches(3.64)
    card_height = Inches(4.5)
    card_top = Inches(2.25)
    card_gap = Inches(0.39)
    start_x = Inches(0.8)

    for i, c in enumerate(cards):
        cx = start_x + i * (card_width + card_gap)
        
        # Hero 카드일 경우 살짝 상단으로 돌출(-0.12인치) 및 하이라이트 보더
        c_top = card_top - (Inches(0.12) if c["is_hero"] else Inches(0))
        c_height = card_height + (Inches(0.24) if c["is_hero"] else Inches(0))

        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, c_top, card_width, c_height)
        card.fill.solid()
        
        if c["is_hero"]:
            card.fill.fore_color.rgb = RGBColor(22, 34, 58)  # 더 밝은 딥 블루
            card.line.color.rgb = RGBColor(59, 130, 246)      # 강렬한 블루 네온
            card.line.width = Pt(2.0)
        else:
            card.fill.fore_color.rgb = RGBColor(14, 20, 32)
            card.line.color.rgb = RGBColor(35, 48, 70)
            card.line.width = Pt(1.0)

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = Inches(0.35)
        ctf.margin_right = Inches(0.35)
        ctf.margin_top = Inches(0.35)

        # 1. 상단 미니 뱃지
        p_badge = ctf.paragraphs[0]
        p_badge.text = c["badge"]
        p_badge.font.size = Pt(9.5)
        p_badge.font.bold = True
        p_badge.font.color.rgb = RGBColor(59, 130, 246) if not c["is_hero"] else RGBColor(96, 165, 250)

        # 2. 빅 넘버 & 유닛
        p_num = ctf.add_paragraph()
        p_num.text = c["num"]
        p_num.font.name = "Pretendard"
        p_num.font.size = Pt(50 if c["is_hero"] else 44)
        p_num.font.bold = True
        p_num.font.color.rgb = RGBColor(255, 255, 255)

        p_unit = ctf.add_paragraph()
        p_unit.text = c["unit"]
        p_unit.font.size = Pt(11)
        p_unit.font.bold = True
        p_unit.font.color.rgb = RGBColor(16, 185, 129) if c["is_hero"] else RGBColor(59, 130, 246)

        # 3. 타이틀
        p_title = ctf.add_paragraph()
        p_title.text = "\n" + c["title"]
        p_title.font.size = Pt(15)
        p_title.font.bold = True
        p_title.font.color.rgb = RGBColor(255, 255, 255)

        # 4. 기술 태그 (피드백 반영: 가독성 극대화)
        p_tags = ctf.add_paragraph()
        p_tags.text = " ".join(c["tags"])
        p_tags.font.size = Pt(10)
        p_tags.font.bold = True
        p_tags.font.color.rgb = RGBColor(96, 165, 250)

        # 5. 핵심 요약문
        p_desc = ctf.add_paragraph()
        p_desc.text = c["desc"]
        p_desc.font.size = Pt(11.5)
        p_desc.font.color.rgb = RGBColor(148, 163, 184)

    output_path = "slide_v2_master_enhanced.pptx"
    prs.save(output_path)
    print(f"[+] 2차 고도화 완성: {output_path}")

if __name__ == "__main__":
    build_second_generation_master()
