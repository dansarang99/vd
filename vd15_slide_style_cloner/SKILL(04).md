---
name: slide-style-cloner
description: "Reverse engineer and clone executive presentation styles from any reference PDF or PPTX slide deck, extract DESIGN.md, STYLE.md, and PROMPT.md, and generate brand-new, high-fidelity executive presentation slides matching that exact aesthetic. Features the Triple Slash Protocol (/grill-me intake alignment -> /plan storyline architecture -> /goal non-stop autonomous execution) supporting 1:1 exact structural cloning (default) up to 1:2~1:5 massive expansion (20~50+ slides) grounded in user data/CSVs. Use whenever the user provides a reference PDF or PPTX deck, says '이 슬라이드 스타일로 만들어줘', '슬라이드 스타일 복제', '1:1 복제', '슬라이드 분량 늘려줘', '/grill-me', '/plan', '/goal', or wants to produce McKinsey/BCG-caliber executive strategy decks on a new topic. Do NOT use for basic text edits to existing PPTX or simple one-off charts."
---

# Slide Style Cloner — Autonomous Executive Presentation Factory (Iteration 04)

`slide-style-cloner`는 사용자가 레퍼런스 슬라이드(PDF/PPTX)와 신규 주제를 제시했을 때, **단 한 번의 프롬프트로 최종 PPTX 및 PDF 완성까지 완주**할 수 있도록 설계된 엔터프라이즈 프레젠테이션 자동화 스킬입니다.

본 스킬은 **`/grill-me` (사전 조율 인터뷰) ➔ `/plan` (내러티브 아키텍처 기획) ➔ `/goal` (중단 없는 자율 완주)**의 트리플 슬래시 방법론을 내장하여, 사용자와의 불필요한 핑퐁 대화 없이 완벽한 결과물을 보장합니다.

---

## ⚡ 트리플 슬래시 실행 프로토콜 (Triple Slash Protocol)

```
[사용자 입력: 레퍼런스 슬라이드 + 신규 주제 (+ 선택적 CSV / 참고자료)]
                                │
                                ▼
========================================================================
Phase 0: /grill-me 사전 조율 (Pre-Flight Alignment)
  - 레퍼런스 분석: 원본 슬라이드 수(N장), 지배적 색상, 폰트 위계 파악
  - 사전에 핵심 선택지를 제시하여 즉시 조건 확정:
      ① 분량 선택: [1:1 기본](N장) / [1:2 심층](2N장) / [1:3 전략](3N장) / [1:4~5 마스터](4~5N장)
      ② 추가 데이터 여부: CSV 실측 데이터 연동 / 텍스트 보고서 / 자료 없음 (AI 자체 리서치)
      ③ 타깃 청중: C-Level 임원 보고용 (기본) / 실무 프로젝트 제안 / 투자 IR 피치
  * 단, 사용자가 이미 프롬프트에 배율/데이터를 명시했거나 /goal로 원클릭 지시를 내린 경우,
    질문 없이 최적의 기본값으로 즉시 Phase 1로 직행!
========================================================================
                                │
                                ▼
========================================================================
Phase 1: /plan 내러티브 아키텍처 기획 (Deck Architecture Planning)
  - 확정된 배율(1:1 ~ 1:5)에 맞춰 `scripts/plan_deck.py` 실행
  - 1번부터 N번 슬라이드까지 6대 아키타입(A1~A6) 1:1 매핑 테이블 수립
  - 슬라이드별 핵심 Kicker, 타이틀, 실측 데이터 슬롯, 결론 테이크어웨이 명세화
  - `deck_spec.json` 생성 완료
========================================================================
                                │
                                ▼
========================================================================
Phase 2: /goal 중단 없는 자율 완주 (Autonomous Execution & Packaging)
  - 에이전트가 백그라운드에서 전 과정을 멈춤 없이 연속 실행:
    1. CSV 데이터가 제공된 경우: `scripts/parse_data.py`로 핵심 통계 지표 자동 추출
    2. 일괄 슬라이드 빌드: `scripts/build_expanded_deck.py`로 10~50+ 슬라이드 HTML 일괄 생성
    3. 초고해상도 렌더링: `scripts/render_slides.py`로 1920x1080 Headless 브라우저 PNG 캡처
    4. 멀티포맷 패키징: `scripts/export_deck.py`로 1080p 다중 페이지 PDF & 16:9 PPTX 빌드
    5. 슬라이드 누락 및 레이아웃 무결성 자동 검증
========================================================================
                                │
                                ▼
[납품: 검증 완료된 최종 .pptx 및 .pdf 다운로드 링크 + 슬라이드 구성 브리핑 보고서]
```

---

## 📋 분량 선택 메뉴 (Expansion Ratio Menu)

| 모드 | 배율 | 분량 예시 (원본 10장 기준) | 핵심 구성 및 권장 용도 |
|:---:|:---:|:---:|:---|
| **[기본] 1:1 정밀 복제** | **1:1** | **10장** (원본 동일) | **원본의 슬라이드 장수와 6대 아키타입 순서를 1:1 그대로 승계**.<br>빠른 보고서 작성, 디자인 리뉴얼, 콤팩트한 주제 변경에 최적. |
| **1:2 심층 분석형** | **1:2** | **20장** (2배 분량) | 핵심 주장마다 **실증 데이터(Metric 4-Card) 및 세부 비교(Inquiry)** 슬라이드를 1장씩 보강.<br>임원 보고용 세부 근거 자료 보강에 최적. |
| **1:3 전략 체계형** | **1:3** | **30장** (3배 분량) | **4대 파트 체계(진단 ➔ 전략 ➔ 거버넌스 ➔ 로드맵)**로 내러티브를 전면 확대.<br>경영진 전략 특강 및 핵심 프로젝트 제안서에 최적. |
| **1:4~5 종합 마스터형**| **1:4~5**| **40~50장** (4~5배 분량) | 제공된 **CSV 실측 데이터 전수 분석, 5단계 상세 프로세스, C-Level 체크리스트** 총망라.<br>전사 종합 전략 보고서, 이사회 제출용 마스터 덱에 최적. |

---

## 📐 6대 핵심 슬라이드 아키타입 (Slide Archetypes)

1. **Cover (A1)**: 소프트 틴트 배경 + 대형 오가닉 원형 그래픽 + Kicker + 2줄 메인 타이틀 + 작성자 메타데이터
2. **Inquiry 3-Card (A2)**: 3개 균등 화이트 카드 + Q1~Q3 원형 배지 + 굵은 질문문 + 하단 인용/시사점 배너
3. **Dark Divider (A3)**: 딥 네이비 배경 + 화이트 64px 타이틀 + 3대 챕터 요약 불릿
4. **Metric 4-Card (A4)**: 4개 카드 분할 + 96px 초대형 실측 숫자(Hero Metric) + 하단 전폭 딥 네이비 결론 배너
5. **Process Flow (A5)**: 4~5단계 가로형 카드 + 연결 화살표 + 핵심 병목/전환 단계 딥 네이비 반전 하이라이트
6. **Quadrant Matrix (A6)**: 2x2 좌표축 + 위험/핵심 영역 살구색 하이라이트 + 우측 2단 인사이트 사이드바

---

## 🛠️ 번들 스크립트 도구함 (Internal Script Arsenal)

| 스크립트 | 역할 | 실행 예시 |
|:---|:---|:---|
| `scripts/extract_style.py` | PDF/PPTX 디자인 토큰 및 장수(N) 파악 | `python scripts/extract_style.py -i ref.pdf -o result/style.json` |
| `scripts/parse_data.py` | CSV 데이터 요약 통계 1초 추출 | `python scripts/parse_data.py -i data.csv -o result/data_summary.json` |
| `scripts/plan_deck.py` | 1:1~1:5 배율 기반 슬라이드 구성표 자동 기획 | `python scripts/plan_deck.py -t "주제" -r 3 -b 10 -o result/deck_spec.json` |
| `scripts/build_expanded_deck.py` | 10~50+ 슬라이드 일괄 빌드 및 PPTX/PDF 출력 | `python scripts/build_expanded_deck.py -c deck_spec.json -o result/deck/` |
| `scripts/render_slides.py` | Headless Chrome/Edge 1920x1080 렌더러 | `python scripts/render_slides.py -i html/ -o png/` |
| `scripts/export_deck.py` | PNG들을 묶어 1080p PDF 및 16:9 PPTX 생성 | `python scripts/export_deck.py -i png/ -o output_name` |
