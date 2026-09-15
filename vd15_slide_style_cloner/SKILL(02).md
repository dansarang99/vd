---
name: slide-style-cloner
description: "Reverse engineer and clone executive presentation styles from any reference PDF or PPTX slide deck, extract DESIGN.md, STYLE.md, and PROMPT.md, and generate brand-new, high-fidelity executive presentation slides matching that exact aesthetic. Use whenever the user provides a reference PDF or PPTX deck, says '이 슬라이드 스타일로 만들어줘', '슬라이드 스타일 추출해줘', 'DESIGN.md STYLE.md PROMPT.md 추출', '슬라이드 디자인 복제', '발표자료 스타일 따와서 새로 만들어줘', or wants to produce McKinsey/BCG-caliber executive strategy decks on a new topic. Do NOT use for basic text edits to existing PPTX or simple one-off charts."
---

# Slide Style Cloner — Enterprise Presentation Style Cloning & Authoring (Iteration 02)

`slide-style-cloner`는 임의의 레퍼런스 프레젠테이션(PDF 또는 PPTX)으로부터 시각적 디자인 언어를 정밀 역공학(Reverse Engineering)하여 독자적인 디자인 시스템(`DESIGN.md`, `STYLE.md`, `PROMPT.md`)을 구축하고, 이를 바탕으로 완전히 새로운 주제의 고품격 경영 전략 슬라이드 덱을 오차 없이 복제·생성하는 엔터프라이즈급 에이전트 스킬입니다.

---

## 1. 엔드투엔드 파이프라인 (End-to-End Pipeline)

```
[입력: 레퍼런스 PDF / PPTX]
       │
       ▼
Phase 1: 시각 메타데이터 추출 (Deterministic Extraction)
   - `scripts/extract_style.py` 실행
   - 폰트 위계, pt 크기, HEX 컬러 토큰, 캔버스 비율(16:9) JSON 추출
       │
       ▼
Phase 2: 디자인 시스템 마스터 가이드 구축 (System Synthesis)
   - `templates/`를 복제하여 `DESIGN.md`, `STYLE.md`, `PROMPT.md` 완성
   - 6대 아키타입 및 색상 변수 토큰 매핑
       │
       ▼
Phase 3: 슬라이드 구조 기획 및 아키타입 매핑 (Storyline Planning)
   - 신규 주제를 6대 핵심 슬라이드 패턴(Cover, Inquiry, Divider, Metric, Process, Matrix)에 1:1 매핑
   - 슬라이드별 핵심 메시지 및 Kicker, Takeaway 도출
       │
       ▼
Phase 4: 결정론적 HTML/CSS 생성 및 1080p 렌더링 (Generation & Rendering)
   - 1920x1080 고해상도 HTML 슬라이드 코드 생성
   - `scripts/render_slides.py` 실행 (Headless Chrome/Edge 기반 1920x1080 PNG 캡처)
       │
       ▼
Phase 5: 멀티포맷 패키징 및 납품 (Packaging & Export)
   - `scripts/export_deck.py` 실행
   - 1080p 벡터 래핑 다중 페이지 PDF 생성
   - 16:9 와이드스크린 네이티브 편집 가능 PPTX 생성
```

---

## 2. 6대 핵심 슬라이드 아키타입 (The 6 Archetypes)

1. **Cover Slide (A1)**: 소프트 틴트 배경 + 대형 오가닉 원형 그래픽 + Kicker + 2줄 메인 타이틀 + 작성자 메타데이터
2. **Inquiry 3-Card (A2)**: 3개 균등 화이트 카드 (`width: 550px`) + Q1~Q3 원형 배지 + 굵은 질문문 + 하단 인용 배너
3. **Dark Divider (A3)**: 딥 네이비 배경 + 화이트 64px 타이틀 + 코럴/틸 불릿 포인트 3개
4. **Metric 4-Card (A4)**: 4개 카드 분할 + 96px 초대형 숫자(Hero Metric) + 하단 전폭 딥 네이비 결론 배너
5. **Process Flow (A5)**: 4~5단계 가로형 카드 + 단계 연결 화살표 + 핵심 전환 단계 딥 네이비 반전 하이라이트
6. **Quadrant Matrix (A6)**: 1100px 2x2 좌표축 + 위험/핵심 영역 살구색 틴트 + 우측 580px 2단 인사이트 사이드바

---

## 3. 스크립트 실행 가이드 (CLI Reference)

- **스타일 메타데이터 추출**:
  ```bash
  python scripts/extract_style.py -i ref.pdf -o result/style.json -t result/thumbs/
  ```
- **HTML 슬라이드 렌더링**:
  ```bash
  python scripts/render_slides.py -i result/html_slides/ -o result/png_slides/
  ```
- **PDF 및 PPTX 원클릭 패키징**:
  ```bash
  python scripts/export_deck.py -i result/png_slides/ -o result/final_presentation --format all
  ```
