---
name: slide-style-cloner
description: "Reverse engineer and clone executive presentation styles from any reference PDF or PPTX slide deck, extract DESIGN.md, STYLE.md, and PROMPT.md, and generate brand-new, high-fidelity executive presentation slides matching that exact aesthetic. Use whenever the user provides a reference PDF or PPTX deck, says '이 슬라이드 스타일로 만들어줘', '슬라이드 스타일 추출해줘', 'DESIGN.md STYLE.md PROMPT.md 추출', '슬라이드 디자인 복제', '발표자료 스타일 따와서 새로 만들어줘', or wants to produce McKinsey/BCG-caliber executive strategy decks on a new topic with expanded volume (2x~5x, 20~50+ slides) based on user-provided data/CSVs. Do NOT use for basic text edits to existing PPTX or simple one-off charts."
---

# Slide Style Cloner — Autonomous Executive Presentation Factory (Iteration 03)

`slide-style-cloner`는 사용자가 복잡한 기술적 개입 없이 **"레퍼런스 슬라이드 원본 + 신규 주제 및 희망 분량 + 참고자료(CSV/문서)"**만 제시하면, 에이전트가 자율적으로 스타일을 복제하고 내용을 2~5배(20~50+장)로 대폭 확장하여 최고급 경영 전략 슬라이드 덱(PPTX & PDF)을 완성해 내는 엔터프라이즈급 프레젠테이션 생성 스킬입니다.

---

## 🎯 사용자 경험 원칙 (Zero-Friction Rule)

사용자는 오직 3가지만 자연어로 전달합니다:
1. **레퍼런스 파일**: "이 PDF(또는 PPTX) 디자인 스타일로 맞춰줘."
2. **신규 주제 & 분량**: "주제는 [OOO]이고, 기존보다 2~5배 늘려 [25~50장] 규모의 종합 덱으로 만들어줘."
3. **참고자료/데이터(선택)**: "첨부한 [보고서 텍스트]와 [데이터.csv] 지표를 실제 슬라이드에 반영해줘."

에이전트는 이 요청을 받자마자 **기획 ➔ 데이터 추출 ➔ 일괄 렌더링 ➔ 최종 PPTX/PDF 납품**까지 전 과정을 백그라운드에서 원스톱으로 처리합니다.

---

## 📈 2~5배 대용량 확장 공식 (Massive Expansion Architecture)

사용자가 20~50장의 방대한 분량을 요구할 때, 슬라이드는 항상 다음 **4대 파트(Multi-Part) 체계**로 체계적 확장합니다:
- **INTRO & OPENING (Slide 01~03)**: Cover, Opening Key Question 3-Card, Agenda
- **PART 1: 패러다임 전환 및 현실 진단 (Slide 04~09)**: Dark Divider, Metric 4-Card (CSV 수치 실증), Inquiry 3-Card, Process Flow, 2x2 Matrix
- **PART 2: 핵심 전략 및 기술 아키텍처 (Slide 10~17)**: Dark Divider, Core Pillars, Metric 4-Card, Modern Pipeline Flow, Tech Matrix
- **PART 3: 조직 역량 및 거버넌스/리스크 관리 (Slide 18~25)**: Dark Divider, Trust Pillars, Autonomous Governance Flow, ROI Metrics, Risk Matrix
- **PART 4: 실행 로드맵 및 경영진 결단 (Slide 26~30+)**: Dark Divider, Immediate Actions, 18-Month Roadmap, C-Level Checklist, Closing Vision

---

## 🛠️ 번들 스크립트 도구함 (Internal Script Arsenal)

| 스크립트 | 역할 | 실행 예시 |
|:---|:---|:---|
| `scripts/extract_style.py` | PDF/PPTX 디자인 토큰 및 폰트 추출 | `python scripts/extract_style.py -i ref.pdf -o result/style.json` |
| `scripts/parse_data.py` | 사용자 CSV 데이터 요약 통계 추출 | `python scripts/parse_data.py -i data.csv -o result/data_summary.json` |
| `scripts/build_expanded_deck.py` | 20~50+ 슬라이드 일괄 빌드 및 PDF/PPTX 출력 | `python scripts/build_expanded_deck.py -c deck_spec.json -o result/deck/` |
| `scripts/render_slides.py` | Headless Chrome/Edge 1920x1080 렌더러 | `python scripts/render_slides.py -i html/ -o png/` |
| `scripts/export_deck.py` | PNG들을 묶어 1080p PDF 및 16:9 PPTX 생성 | `python scripts/export_deck.py -i png/ -o output_name` |
