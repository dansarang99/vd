---
name: vd23_google_opal_builder
description: >
  장대표(BJ Jang)의 Google Opal 자동화 앱 생성 프롬프트 빌더 스킬 (vd23).
  구글 오팔(Google Opal, opal.google) 접속 시 좌측 입력창에 입력하여
  단 한 번의 프롬프트로 완벽한 다단계 워크플로우 노드 그래프(Input -> Search -> Gemini -> Transform -> Output)를
  자동 생성할 수 있도록 C-I-P-O-E 5대 아키텍처에 맞춘 최적화 메타 프롬프트를 생성해주는 AX 창업지도사 전문 스킬입니다.
---

# 🚀 Google Opal Automation App Prompt Crafter (vd23)

> **장대표(BJ Jang)의 AI 실무 자동화 스킬 시리즈 No.23**  
> **구글 오팔(Google Opal) 좌측 입력창 전용 자동화 앱 생성 프롬프트 엔지니어링 마스터**

---

## 📌 스킬 개요 및 핵심 목적

Google Opal(`https://opal.google`)은 사용자의 자연어 설명을 기반으로 노코드/로우코드 AI 에이전트 워크플로우를 자동 시각화 및 생성해주는 Google Labs의 차세대 플랫폼입니다.

그러나 일반 사용자가 좌측 입력창에 모호하게 요청(예: *"사업계획서 쓰는 챗봇 만들어줘"*)하면, Opal은 단순한 1단계 단일 챗봇 노드만 생성하여 강력한 워크플로우(다단계 분기, 웹 검색 연동, 표/차트 UI 렌더링 등)의 잠재력을 발휘하지 못합니다.

**이 스킬(vd23)은 사용자의 단순한 아이디어를 Opal의 컴파일러가 완벽한 노드 그래프로 이해할 수 있는 5대 구조화 프롬프트(Mega-Prompt)로 변환해 줍니다.**

---

## 🏗️ Google Opal 프롬프트 5대 표준 규격 (C-I-P-O-E Framework)

Opal 좌측 창에 입력할 프롬프트는 반드시 아래 5가지 블록을 갖추어야 합니다.

```
┌─────────────────────────────────────────────────────────────┐
│ 1. [Context & App Identity]  : 앱의 명확한 역할과 최종 비즈니스 목적 │
│ 2. [Input Schema]            : 수강생/사용자가 입력할 UI 입력 폼 필드 │
│ 3. [Node Pipeline Steps]     : 검증 -> 검색 -> Gemini 추론 -> 데이터 가공 │
│ 4. [Output UI Specification] : 대시보드 카드, 표, 액션 플랜 렌더링 방식 │
│ 5. [Edge Cases & Fallback]   : 입력값 누락 시 유도 질문 및 방어 로직 │
└─────────────────────────────────────────────────────────────┘
```

---

## 📋 표준 프롬프트 출력 포맷 (Opal 좌측 창 복사용)

스킬 호출 시 아래와 같은 정밀한 영문/한글 혼합 최적화 템플릿 형태로 출력합니다. (Opal의 엔진은 명확한 영문 키워드와 구체적인 한글 요구사항이 결합되었을 때 가장 안정적으로 노드를 배치합니다.)

```text
Create an automated multi-step workflow app named "[앱 영문명 / 한글명]" for [타깃 사용자 페르소나].

[App Goal & Persona]
Act as an expert [전문가 역할, 예: Senior Startup Accelerator & AX Consultant].
The goal of this app is to [해결하려는 핵심 비즈니스 과제 및 최종 산출물].

[User Input Elements]
1. [입력필드 1]: (Type: Short Text / Long Text Area / Dropdown / File Upload) - [라벨 및 플레이스홀더]
2. [입력필드 2]: (Type: Single Select Dropdown) - [선택지 목록 예: A, B, C]
3. [입력필드 3]: (Type: Number / Date) - [설명]

[Workflow Pipeline Nodes]
- Node 1 (Input Validation): Inspect user inputs. If any mandatory field is missing, prompt user with friendly clarification.
- Node 2 (Grounding & Search): [필요시 Google Search 노드 연결하여 최신 시장 데이터/경쟁사 크롤링].
- Node 3 (Core AI Logic - Gemini 1.5 Pro): 
  Apply [핵심 분석 프레임워크, 예: PSST, Lean Canvas, 4P, SWOT].
  Perform step-by-step reasoning on the input data.
- Node 4 (Data Transformation & Synthesis): 
  Structure the output into a clean Markdown table, score evaluation (0-100), and prioritized recommendations.
- Node 5 (Presentation & Actions): 
  Render the final response in an interactive dashboard view with structured sections and copy/export triggers.

[Output UI & Format]
- Summary Header: Status badge, Key Metrics Card
- Analysis Section: Structured comparative tables and in-depth strategic advice
- Action Roadmap: 3-phase execution checklist (Week 1, Month 1, Quarter 1)

[Guardrails & Error Handling]
- Never output speculative financial advice without disclaimer.
- Maintain a highly professional, encouraging, and actionable consulting tone.
```

---

## 🎯 창업지도사(AX) 강의용 5대 대표 자동화 앱

| No | 앱 명칭 | 주요 입력 폼 | 워크플로우 구성 노드 | 기대 산출물 |
|:---:|:---|:---|:---|:---|
| **01** | **원클릭 린 캔버스 자동 완성기** | 아이템 설명, 타깃 고객, 수익 모델 | 입력 검증 -> 시장 세분화 -> 9대 항목 추론 -> 마크다운 테이블 | 스타트업 린 캔버스 표 + 30일 검증 로드맵 |
| **02** | **정부지원사업 PSST 사업계획서 빌더** | 창업 아이템, 핵심 기술, 지원 사업명 | 사업별 평가기준 매핑 -> 4개 파트(PSST) 심층 작성 -> 심사평가 체크리스트 | 1차 완성형 표준 사업계획서 초안 |
| **03** | **실시간 경쟁사 비교 배틀카드 분석기** | 자사 제품명/특징, 경쟁사 이름(2~3곳) | 구글 검색 연동 -> SWOT/포지셔닝 분석 -> 차별화 포인트 도출 | 4사분면 매트릭스 + 영업용 비교표 |
| **04** | **옴니채널 SNS 마케팅 콘텐츠 팩토리** | 제품 링크/소개글, 타깃 톤앤매너 | 텍스트 핵심 요약 -> 채널별(인스타/블로그/쇼츠/링크드인) 분기 작성 | 채널별 탭 대시보드 + 즉시 복사 스크립트 |
| **05** | **VC 투자심사역 압박면접 Q&A 시뮬레이터** | 사업 요약문/IR 텍스트, 투자 단계 | 투자자 페르소나 설정 -> 취약점 탐지 -> 10대 송곳 질문 및 방어 답변 생성 | 심사역 예상 질문지 + 모범 대응 매뉴얼 |

---

## 🛠️ 스킬 사용법 (How to Use)

사용자가 다음과 같이 요청할 때 이 스킬이 작동합니다:
- *"구글 Opal에서 쓸 [스타트업 시장조사] 앱 프롬프트 만들어줘"*
- *"Opal 왼쪽 입력창에 붙여넣을 프롬프트 생성해줘"*
- *"창업지도사 실습용으로 쓸 Opal 자동화 워크플로우 프롬프트 작성해줘"*

스킬은 입력을 분석한 후:
1. 적합한 C-I-P-O-E 규격 프롬프트를 텍스트 블록으로 깔끔하게 출력합니다.
2. Opal 접속 후 붙여넣는 절차와 생성된 노드 튜닝 팁(Inspector 설정법)을 함께 안내합니다.
