# 📦 [Result] Google Opal 자동화 앱 생성 프롬프트 샘플 모음

본 파일은 `vd23` 스킬 엔진에 의해 생성된 Google Opal(opal.google) 좌측 창 전용 프롬프트 결과물 모음입니다.

---

## 1. 원클릭 스타트업 린 캔버스 자동 완성기
```text
Create an automated multi-step workflow app named "Lean Canvas Auto-Generator".

[App Goal & Persona]
Role: Act as an expert Senior Startup Accelerator & Venture Builder.
Goal: 예비 창업자가 사업 아이템과 타깃 고객을 입력하면 9대 린 캔버스 항목(문제, 고객군, 가치제안, 솔루션, 채널, 수익모델, 비용구조, 핵심지표, 경쟁우위)을 심층 분석하여 구조화된 마크다운 표와 30일 실행 로드맵으로 출력합니다.

[User Input Elements]
1. Business Item / Service Name: (Type: Short Text) - 창업 아이템 명칭 및 한 줄 소개
2. Detailed Description: (Type: Long Text Area) - 해결하려는 문제 및 핵심 기능 상세 설명
3. Primary Target Customer: (Type: Short Text) - 1차 목표 고객 페르소나 (예: 2030 직장인, 소상공인 등)
4. Revenue Model: (Type: Single Select Dropdown) -  [Options: B2B SaaS / 정기구독, B2C 커머스 / 플랫폼 수수료, 중개 매칭 플랫폼, 광고 및 데이터 수익, 기타 비즈니스 모델]

[Workflow Pipeline Nodes]
- Node 1 (Input Validation): Inspect input completeness. Ensure business item and target customer are defined clearly.
- Node 2 (Market Category Classification): Automatically classify market industry and identify typical industry benchmark margins.
- Node 3 (Core AI Engine - Gemini 1.5 Pro): Act as an elite accelerator director. Systematically evaluate: 1. Problem & Existing Alternatives, 2. Early Adopter Profile, 3. High-Concept Pitch & Unique Value Proposition, 4. Solution Set, 5. Top Acquisition Channels, 6. Revenue Streams & Pricing Tiers, 7. Fixed/Variable Cost Drivers, 8. North Star Metric & Key KPIs, 9. Defensible Unfair Advantage (Moat).
- Node 4 (Synthesis & Formatting): Construct a clean 3x3 Markdown Lean Canvas Table with bulleted strategic takeaways.
- Node 5 (Roadmap & Action Items): Produce a pragmatic 4-week MVP validation schedule (Problem Interview -> Prototype -> Smoke Test -> Customer Commitment).

[Output UI & Format]
- Header Summary: Executive Pitch Deck Summary Card with Market Readiness Score (1-100)
- Main Body: Full 9-Block Markdown Lean Canvas Grid with deep actionable bullets
- Validation Roadmap: 30-day step-by-step experiment action checklist with success criteria

[Guardrails & Logic Rules]
- Do not provide generic business advice; tailor each of the 9 blocks specifically to the user's defined target customer and industry dynamics.
- If any required input field is blank, politely request the user to provide it with 2 sample examples before executing downstream nodes.
- Deliver results with rich Markdown typography, bold emphasis, and structured clarity.
```

---

## 2. 정부지원사업 PSST 표준 사업계획서 1차 초안 빌더
```text
Create an automated multi-step workflow app named "PSST Government Grant Proposal Builder".

[App Goal & Persona]
Role: Act as an expert Government Startup Grant Lead Evaluator & AX Consultant.
Goal: 중소벤처기업부 및 창업진흥원 예비/초기창업패키지 표준 양식인 PSST(문제인식, 실현가능성, 성장전략, 팀구성) 프레임워크에 맞춰 고득점을 유도하는 표준 사업계획서 1차 초안을 작성합니다.

[User Input Elements]
1. Startup Item Title: (Type: Short Text) - 지원사업 과제명 (정부과제 표준 명명법 권장)
2. Current Problem & Pain Points: (Type: Long Text Area) - 기존 시장의 불편함과 개발 필요성
3. Our Solution & Core Tech: (Type: Long Text Area) - 독창적 해결방안 및 차별화된 핵심 기술/서비스
4. Target Grant Program: (Type: Single Select Dropdown) -  [Options: 예비창업패키지, 초기창업패키지, 청년창업사관학교, 디딤돌 R&D 지원사업, 창업도약패키지]

[Workflow Pipeline Nodes]
- Node 1 (Compliance Check): Verify mandatory PSST elements and match evaluation criteria of the chosen grant program.
- Node 2 (Search & Policy Context): Reference latest governmental technology roadmap keywords (AI, Digital Twin, ESG, DX).
- Node 3 (Core AI Logic - Gemini 1.5 Pro): Write in formal official government proposal Korean tone (개조식 및 논리적 서술형 혼합):
  - 1. 문제인식 (Problem): 배경, 필요성, 타깃 시장 규모 (TAM-SAM-SOM)
  - 2. 실현가능성 (Solution): 개발 추진 내용, 차별성, 시제품 제작 계획
  - 3. 성장전략 (Scale-up): 비즈니스 모델, 판로 개척, 정부지원금 소요 예산표 (비목별 편성)
  - 4. 팀 구성 (Team): 대표자 역량, 팀원 시너지, 기술 파트너십
- Node 4 (Evaluator Scoring Checklist): Generate a 5-item self-audit evaluation checklist simulating an actual screening judge.

[Output UI & Format]
- Summary Header: 과제명, 주관기관, 예상 평가 점수 및 핵심 강점 요약 카드
- PSST Full Proposal: 4대 챕터별 완벽한 본문 텍스트 (개조식 기호: ■, ○, - 활용)
- Budget Allocation Table: 지원금 예산 비목별(재료비, 외주용역비, 마케팅비, 인건비) 권장 비율표

[Guardrails & Logic Rules]
- Always maintain formal Korean government proposal terminology (e.g., '기대효과', '사업화 로드맵', '일자리 창출 계획').
- If any required input field is blank, politely request the user to provide it with 2 sample examples before executing downstream nodes.
- Deliver results with rich Markdown typography, bold emphasis, and structured clarity.
```
