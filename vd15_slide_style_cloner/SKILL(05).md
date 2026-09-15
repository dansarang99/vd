---
name: slide-style-cloner
description: "Reverse engineer and clone executive presentation styles from any reference PDF or PPTX slide deck, extract DESIGN.md, STYLE.md, and PROMPT.md, and generate brand-new, high-fidelity executive presentation slides matching that exact aesthetic. Features the Proactive Diagnostic Protocol: intelligently diagnoses deck scale (e.g. recommending 1:1.5 / 15 slides for a 10-slide ref), detects missing quantitative charts, proactively offers and executes Exploratory Data Analysis (EDA) on user CSVs or official Public Data (data.go.kr / KOSIS), and autonomously completes the entire PPTX/PDF deck. Use whenever the user provides a reference PDF or PPTX deck, says '이 슬라이드 스타일로 만들어줘', '슬라이드 스타일 복제', 'EDA 분석해서 그래프 넣어줘', '공공데이터 반영해서 슬라이드 만들어줘', or wants McKinsey/BCG-caliber executive presentations."
---

# Slide Style Cloner — Autonomous Executive Presentation & EDA Factory (Iteration 05)

`slide-style-cloner`는 단순한 템플릿 복제 도구가 아닙니다. 사용자가 **"레퍼런스 슬라이드 원본 + 신규 주제"**를 제시했을 때, 수동적인 명령 대기에서 벗어나 **(1) 전문가적 분량 진단 및 추천(예: 10장 ➔ 1:1.5/15장 제안)**과 **(2) 고급 그래프 결핍 진단 및 공공데이터 탐색적 분석(EDA) 능동 제안**을 수행하고, 승인 시 **단 한 번에 완성된 PPTX & PDF를 납품**하는 엔터프라이즈 프레젠테이션 컨설팅 스킬입니다.

---

## 🏛️ 지능형 컨설팅 진단 & 자율 완주 워크플로우

```
[사용자 입력: 레퍼런스 슬라이드 + 신규 주제 (+ 선택적 지침)]
                                │
                                ▼
========================================================================
Step 0: 전문가 진단 및 능동 제안 (Intelligent Diagnostic Intake)
  - 레퍼런스 분석: 슬라이드 장수(N), 폰트 위계, 색상 토큰, 정량 차트 유무 파악
  - 사용자에게 2가지 핵심 진단 및 제안을 선제 제시:
  
    ① [분량 진단] 주제의 내러티브 깊이를 고려한 최적 분량 추천
       "원본은 10장이지만, 요청하신 주제의 내러티브(현황 진단 ➔ 핵심 전략 ➔ 거버넌스 ➔ 로드맵)를
        설득력 있게 전달하려면 1:1.5(15장) 구성이 가장 적합할 것 같습니다. 이대로 진행할까요?"
        
    ② [데이터/차트 결핍 진단 및 EDA 능동 제안]
       "현재 원본 자료는 텍스트 위주로 정량적 실증 지표(고급 그래프)가 다소 부족합니다.
        관련 데이터(CSV)를 직접 올려주시겠습니까, 아니면 제가 공공데이터포털(data.go.kr) 등에서
        주제에 부합하는 공공데이터를 직접 수집하여 '탐색적 데이터 분석(EDA)'을 수행한 후,
        그 시각화 차트와 핵심 통계를 PPT 적재적소에 넣어드릴까요?"

  * 예외: 사용자가 이미 프롬프트에 구체적 장수/데이터를 지정했거나 /goal로 원클릭 완주를 지시한 경우,
    추가 질문 없이 최적의 진단 조건으로 즉시 Step 1으로 직행!
========================================================================
                                │ (사용자 승인: "네, 15장으로 해주고 공공데이터 EDA도 넣어주세요")
                                ▼
========================================================================
Step 1: 공공데이터 수집 & 탐색적 데이터 분석 (Public Data & EDA)
  - 로컬 `upload/` 폴더 또는 `scripts/fetch_public_data.py`를 통해 공공데이터(data.go.kr) 확보
  - `scripts/eda_analyzer.py` 실행:
    * 판다스 기반 통계 분석 (시계열 추세, 증감률, 카테고리 비중, 이상치 정제)
    * 덱의 디자인 시스템 팔레트(Deep Navy, Coral, Teal)와 일치하는 1080p 고해상도 차트 생성
    * C-Suite 의사결정용 3대 핵심 정량 발견점(Key Insights) 자동 도출
========================================================================
                                │
                                ▼
========================================================================
Step 2: 내러티브 아키텍처 기획 (/plan)
  - 승인된 분량(예: 1:1.5 / 15장)에 맞춰 `scripts/plan_deck.py` 실행
  - 1번부터 15번까지 7대 아키타입(A1~A7) 1:1 매핑 명세(`deck_spec.json`) 수립
  - EDA 차트 전용 슬라이드(A7) 및 실측 지표를 담은 Metric 4-Card(A4) 배치 확정
========================================================================
                                │
                                ▼
========================================================================
Step 3: 일괄 빌드 및 자율 완주 (/goal)
  - `scripts/build_expanded_deck.py` 실행 ➔ 1920x1080 HTML 슬라이드 일괄 생성
  - `scripts/render_slides.py` 실행 ➔ Chrome/Edge 헤드리스 1080p PNG 캡처
  - `scripts/export_deck.py` 실행 ➔ 1080p PDF 및 16:9 와이드스크린 편집 가능 PPTX 빌드
  - 무결성 검증 후 최종 파일 경로 및 요약 브리핑 보고
========================================================================
                                │
                                ▼
[최종 납품: .pptx 및 .pdf 다운로드 링크 + EDA 데이터 분석 브리핑]
```

---

## 📋 유연한 분량 추천 가이드 (Scale Recommendation Benchmarks)

에이전트는 원본 장수($N$) 대비 다음 기준을 참고하여 가장 설득력 있는 최적 분량을 제안합니다:

| 추천 배율 | 명칭 | 슬라이드 수 예시 (원본 10장 기준) | 추천 시나리오 및 내러티브 구성 |
|:---:|:---:|:---:|:---|
| **1:1** | 정밀 복제형 | **10장** (원본 동일) | 원본과 동일한 호흡. 콤팩트한 임원 보고, 빠른 디자인 리뉴얼에 최적. |
| **1:1.2 ~ 1:1.5** | **전략 보강형 (추천)** | **12 ~ 15장** (1.2~1.5배) | 원본 흐름에 **공공데이터 EDA 차트 슬라이드(A7) + 세부 거버넌스 2~3장**을 전략적으로 추가한 가장 이상적인 분량. |
| **1:2** | 심층 분석형 | **20장** (2배 확장) | 각 챕터마다 실측 통계(A4)와 비교 분석(A2)을 1장씩 보강하여 탄탄한 근거 확보. |
| **1:3 ~ 1:5** | 종합 마스터형 | **30 ~ 50장** (대용량 확장) | 4대 파트 체계(진단 ➔ 아키텍처 ➔ 거버넌스 ➔ 로드맵) 전면 전개 및 전사 마스터 보고용. |

---

## 📐 7대 핵심 슬라이드 아키타입 (7 Slide Archetypes)

1. **A1: Cover Slide (표지)**: 소프트 틴트 배경 + 대형 오가닉 원형 그래픽 + Kicker + 2줄 메인 타이틀 + 작성자 메타데이터
2. **A2: Inquiry 3-Card (질문 카드)**: 3개 균등 화이트 카드 + Q1~Q3 원형 배지 + 굵은 질문문 + 하단 인용 배너
3. **A3: Dark Divider (섹션 간지)**: 딥 네이비 배경 + 화이트 64px 타이틀 + 3대 챕터 요약 불릿
4. **A4: Metric 4-Card (지표 통계)**: 4개 카드 분할 + 96px 초대형 실측 숫자(Hero Metric) + 하단 전폭 딥 네이비 결론 배너
5. **A5: Process Flow (프로세스 체브론)**: 4~5단계 가로형 카드 + 연결 화살표 + 핵심 전환 단계 딥 네이비 반전
6. **A6: Quadrant Matrix (사분면 매트릭스)**: 2x2 좌표축 + 위험/핵심 영역 살구색 하이라이트 + 우측 2단 인사이트 사이드바
7. **A7: EDA Data Visualizer (심층 데이터 시각화)**: 좌측 1080p 고해상도 공공데이터 차트 + 우측 3대 핵심 정량 발견점 사이드바 + 하단 테이크어웨이

---

## 🛠️ 번들 스크립트 도구함 (Internal Script Arsenal)

| 스크립트 | 역할 | 실행 예시 |
|:---|:---|:---|
| `scripts/extract_style.py` | PDF/PPTX 디자인 토큰 및 장수(N) 파악 | `python scripts/extract_style.py -i ref.pdf -o result/style.json` |
| `scripts/fetch_public_data.py` | 공공데이터포털(data.go.kr) 등 오픈데이터 검색 및 매핑 | `python scripts/fetch_public_data.py -t "주택 부동산" -o result/public_data.json` |
| `scripts/eda_analyzer.py` | **CSV 탐색적 데이터 분석(EDA) & 1080p 차트 생성** | `python scripts/eda_analyzer.py -i data.csv -o result/eda/ -t "수급 추이"` |
| `scripts/plan_deck.py` | **유연한 배율(1:1.5 등) 및 EDA 슬라이드 자동 기획** | `python scripts/plan_deck.py -t "주제" -r 1.5 -b 10 -e result/eda/eda_summary.json` |
| `scripts/build_expanded_deck.py` | 10~50+ 슬라이드 일괄 빌드 & PPTX/PDF 자동 출력 | `python scripts/build_expanded_deck.py -c deck_spec.json -o result/deck/` |
| `scripts/render_slides.py` | Headless Chrome/Edge 1920x1080 고해상도 렌더러 | `python scripts/render_slides.py -i html/ -o png/` |
| `scripts/export_deck.py` | PNG들을 묶어 1080p PDF 및 16:9 와이드스크린 PPTX 생성 | `python scripts/export_deck.py -i png/ -o output_name` |

---

## 💬 사용자 대화 시나리오 예시

> **사용자**: *"이 10장짜리 부동산 특강 PPT 스타일로, '2026 주택 시장 전망과 주거 안정화 전략' 슬라이드 새로 만들어줘."*
>
> **에이전트**:
> 1. 원본을 분석합니다: 총 10장, 딥 네이비 & 코럴 톤, 정량 차트 부재.
> 2. 즉시 전문가적 진단 및 제안을 제시합니다:
>    > *"제시해주신 원본은 총 10장입니다. 분석 결과 다음과 같이 제안드립니다:*
>    >
>    > *1. **분량 제안**: 10장은 시장 진단과 공급/수급 정책, 실행 로드맵을 모두 다루기에 다소 빠듯하여, **1:1.5 배율인 15장 구성이 가장 설득력 있고 적합할 것 같습니다.** 그대로 진행할까요?*
>    > *2. **데이터 및 그래프 제안**: 현재 원본은 텍스트 중심이어서 정량적 실증 그래프가 부족합니다. **보유하신 CSV를 직접 올려주시겠습니까? 아니면 제가 공공데이터포털(data.go.kr)의 '전국 주택 매매수급동향' 실측 데이터를 가져와 '탐색적 데이터 분석(EDA)'을 수행한 후, 고해상도 수급 추이 차트와 핵심 통계를 슬라이드 적재적소에 넣어드릴까요?**"*
>
> **사용자**: *"좋아요. 15장으로 해주고, 공공데이터 수급동향 분석해서 차트 넣어주세요."*
>
> **에이전트**: 추가 질문 없이 즉시 **공공데이터 분석 ➔ 차트 생성 ➔ 15장 일괄 빌드 ➔ PPTX/PDF 납품**까지 원클릭으로 완주합니다.
