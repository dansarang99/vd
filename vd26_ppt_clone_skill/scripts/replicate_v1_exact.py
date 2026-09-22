"""
replicate_v1_exact.py
견본 슬라이드의 원문 텍스트와 레이아웃을 토씨 하나 틀리지 않고 100% 정밀 복제하는 스크립트
"""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_first_generation_replica():
    prs = Presentation()
    prs.slide_width = Inches(13.333)  # 1920px (16:9 Widescreen)
    prs.slide_height = Inches(7.5)     # 1080px

    slide = prs.slides.add_slide(prs.slide_layouts[6])  # 빈 슬라이드

    # 1. 배경 (Obsidian Dark: #0B0F19)
    background = slide.background
    fill = background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(11, 15, 25)

    # 2. 상단 카테고리 뱃지 ("ENTERPRISE AI ARCHITECTURE")
    badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.6), Inches(2.5), Inches(0.35))
    badge.fill.solid()
    badge.fill.fore_color.rgb = RGBColor(20, 30, 50)
    badge.line.color.rgb = RGBColor(59, 130, 246)
    badge.line.width = Pt(1)
    tf_b = badge.text_frame
    tf_b.text = "ENTERPRISE AI ARCHITECTURE"
    tf_b.paragraphs[0].font.size = Pt(9)
    tf_b.paragraphs[0].font.bold = True
    tf_b.paragraphs[0].font.color.rgb = RGBColor(59, 130, 246)
    tf_b.paragraphs[0].alignment = PP_ALIGN.CENTER

    # 3. 메인 타이틀 (토씨 하나 틀리지 않은 원문 100%)
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.1), Inches(11.7), Inches(0.8))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = "엔터프라이즈 AI의 상용화 병목을 해소하는 통합 에이전틱 인프라"
    p_t.font.name = "Pretendard"
    p_t.font.size = Pt(28)
    p_t.font.bold = True
    p_t.font.color.rgb = RGBColor(255, 255, 255)

    # 서브타이틀
    p_sub = tf_t.add_paragraph()
    p_sub.text = "데이터 사일로 제거와 실시간 모델 서빙을 통해 비즈니스 가치 실현 기간을 획기적으로 단축합니다."
    p_sub.font.size = Pt(13)
    p_sub.font.color.rgb = RGBColor(148, 163, 184)

    # 4. 3열 메트릭 카드 100% 동일 복제
    cards_data = [
        {
            "num": "10x",
            "unit": "Faster",
            "title": "모델 배포 파이프라인 가속",
            "desc": "자동화된 CI/CD 및 모니터링을 통해 개발부터 프로덕션 배포까지의 주기를 기존 수개월에서 수일로 단축합니다."
        },
        {
            "num": "64%",
            "unit": "TCO Down",
            "title": "인프라 운영 비용 절감",
            "desc": "동적 GPU 오케스트레이션과 인퍼런스 최적화를 적용하여 유휴 자원 낭비를 방지하고 비용을 극대화합니다."
        },
        {
            "num": "99.99%",
            "unit": "Reliability",
            "title": "금융권 수준의 엔터프라이즈 보안",
            "desc": "엔드투엔드 데이터 암호화, 역할 기반 권한 제어(RBAC), 데이터 계보 추적으로 규제 준수를 보장합니다."
        }
    ]

    card_width = Inches(3.64)
    card_height = Inches(4.3)
    card_top = Inches(2.3)
    card_gap = Inches(0.39)
    start_x = Inches(0.8)

    for i, c in enumerate(cards_data):
        cx = start_x + i * (card_width + card_gap)
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, card_top, card_width, card_height)
        card.fill.solid()
        card.fill.fore_color.rgb = RGBColor(18, 24, 38)
        card.line.color.rgb = RGBColor(40, 52, 75)
        card.line.width = Pt(1)

        ctf = card.text_frame
        ctf.word_wrap = True
        ctf.margin_left = Inches(0.35)
        ctf.margin_right = Inches(0.35)
        ctf.margin_top = Inches(0.4)

        # Big Metric Number
        p_num = ctf.paragraphs[0]
        p_num.text = c["num"]
        p_num.font.name = "Pretendard"
        p_num.font.size = Pt(44)
        p_num.font.bold = True
        p_num.font.color.rgb = RGBColor(59, 130, 246)

        # Unit Tag
        p_unit = ctf.add_paragraph()
        p_unit.text = c["unit"].upper()
        p_unit.font.size = Pt(11)
        p_unit.font.bold = True
        p_unit.font.color.rgb = RGBColor(16, 185, 129)

        # Card Title
        p_title = ctf.add_paragraph()
        p_title.text = "\n" + c["title"]
        p_title.font.size = Pt(15)
        p_title.font.bold = True
        p_title.font.color.rgb = RGBColor(255, 255, 255)

        # Card Description
        p_desc = ctf.add_paragraph()
        p_desc.text = c["desc"]
        p_desc.font.size = Pt(11)
        p_desc.font.color.rgb = RGBColor(148, 163, 184)

    output_path = "slide_v1_exact_replica.pptx"
    prs.save(output_path)
    print(f"[+] 1차 무결 복제 완료: {output_path}")

if __name__ == "__main__":
    build_first_generation_replica()
