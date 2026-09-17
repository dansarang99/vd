# 📘 [교안 001] Google Opal 컴파일러 작동 원리 및 프롬프트 구조화 가이드

> **장대표(BJ Jang)의 AI 실무 자동화 시리즈 (vd23)**  
> **Google Opal 좌측 프롬프트 입력창을 마스터하는 5대 공식**

---

## 1. Google Opal이란 무엇인가?

Google Opal(`https://opal.google`)은 구글 랩스(Google Labs)에서 공개한 **"자연어 기반 다단계 에이전틱 워크플로우 빌더(Natural Language to Agentic Workflow Builder)"**입니다.

과거에는 Zapier, Make, 또는 LangChain/LangGraph와 같이 복잡한 블록을 마우스로 일일이 끌어다 놓거나 파이썬 코드를 작성해야 했습니다. 하지만 Opal은 **왼쪽 프롬프트 창에 원하는 앱의 워크플로우를 문장으로 서술하면, AI 컴파일러가 스스로 판단하여 중앙 캔버스에 최적의 노드 그래프(Graph)를 배치**해 줍니다.

---

## 2. 왜 일반적인 프롬프트로는 실패하는가?

### ❌ 흔히 하는 실수 (Bad Practice):
```text
"스타트업 마케팅 콘텐츠 만들어주는 AI 앱 만들어줘."
```
- **결과**: Opal은 단순히 `[Input 텍스트]` ➡️ `[단일 Gemini 노드]` ➡️ `[Output 텍스트]` 형태의 1차원 챗봇 노드만 하나 생성합니다.
- **문제점**:
  - 입력 필드가 무엇인지(인스타? 블로그? 타깃?) 구분이 안 됨.
  - 다채널 분기 처리(Branching)가 되지 않음.
  - 출력물이 단순 줄글로 나와서 실무에 바로 쓸 수 없음.

### ⭕ Opal 최적화 메타 프롬프트 (Best Practice):
```text
Create an automated multi-step workflow app named "Omni-Channel Content Factory".
[App Goal & Persona] ...
[User Input Elements] 1. Topic (Text Area), 2. Tone (Dropdown), 3. CTA (Text) ...
[Workflow Pipeline Nodes] Node 1 (Validation) -> Node 2 (Channel Split) -> Node 3 (Parallel Drafting) ...
[Output UI & Format] Multi-Tab Dashboard with Copy Buttons ...
```
- **결과**: Opal이 정확하게 **입력 폼(Dropdown, Textarea) ➡️ 데이터 정제 노드 ➡️ 4개 채널 병렬 Gemini 노드 ➡️ 탭 대시보드 뷰 노드**로 완벽한 오케스트레이션 파이프라인을 그려냅니다!

---

## 3. Opal 프롬프트 5대 아키텍처 공식 (C-I-P-O-E)

Opal 컴파일러가 가장 좋아하는 5대 블록 구조입니다:

### ① Context & App Identity (맥락과 정체성)
- 앱의 이름(영문 식별자 포함 권장)
- AI가 맡아야 할 구체적인 전문가 페르소나 (예: `Senior Venture Capitalist`, `Growth Marketer`)
- 앱이 해결하고자 하는 최종 비즈니스 임팩트

### ② User Input Elements (사용자 입력 폼 스키마)
- Opal은 `(Type: Short Text)`, `(Type: Long Text Area)`, `(Type: Single Select Dropdown [A, B, C])`, `(Type: File Upload)`라는 영문 키워드를 감지하여 그에 맞는 UI 위젯을 캔버스 첫머리에 배치합니다.

### ③ Workflow Pipeline Nodes (단계별 노드 파이프라인)
- 각 단계를 `Node 1`, `Node 2`, `Node 3` 형태로 넘버링합니다.
- 각 노드의 역할을 동사형으로 명시합니다:
  - `Inspect & Validate`: 유효성 검사 노드
  - `Search Grounding`: 구글 웹 검색 툴 노드
  - `Core AI Logic (Gemini 1.5 Pro)`: 심층 추론 노드
  - `Transform & Format`: 표/JSON 구조화 노드

### ④ Output UI & Format (결과 화면 구성)
- Opal의 뷰 컴포넌트에 어떤 카드를 띄울지 명시합니다.
- `Executive Pitch Card`, `Markdown Table Grid`, `Step-by-step Action Checklist` 등을 지정하면 시각적으로 정돈된 대시보드를 생성합니다.

### ⑤ Guardrails & Fallbacks (예외 처리)
- 필수 입력값이 비어있을 때 앱이 멈추지 않고 사용자에게 2가지 예시를 들어 되묻도록 유도하는 방어 프롬프트를 포함합니다.

---

## 4. Opal 인터페이스 200% 활용 강의 팁

1. **좌측 입력창 생성 (Creation Phase)**:
   - 본 스킬(`vd23`)로 생성한 프롬프트를 붙여넣고 `Generate` 또는 `Enter`를 누릅니다.
2. **중앙 캔버스 시각적 검증 (Visual Inspection)**:
   - 노드 간 화살표가 올바르게 연결되었는지 확인합니다.
3. **우측 인스펙터 미세 튜닝 (Refinement Phase)**:
   - 핵심 추론 노드를 클릭하고, 우측 속성 창에서 모델이 `Gemini 1.5 Flash`로 되어 있다면 실무용 심층 분석을 위해 `Gemini 1.5 Pro`로 변경합니다.
   - Temperature(창의성)를 분석형은 `0.2~0.4`, 마케팅/창작형은 `0.7~0.9`로 설정합니다.
4. **상단 Run/Preview 테스트**:
   - 실습생들과 함께 실제 데이터를 넣고 실행 버튼을 눌러 결과물이 실시간 렌더링되는 과정을 보여줍니다.
