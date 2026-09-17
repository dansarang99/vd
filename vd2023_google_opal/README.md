# 🌐 Google Opal 자동화 앱 생성 프롬프트 빌더 (vd23)

> **장대표(BJ Jang)의 AI 실무 자동화 & 프레젠테이션 스킬 시리즈 No.23**  
> **(AX)창업지도사 & 스타트업 대표를 위한 Google Opal 워크플로우 마스터**  
> GitHub: [@dansarang99](https://github.com/dansarang99)

---

## 📖 소개 (Overview)

구글 랩스(Google Labs)의 **Google Opal(`https://opal.google`)**은 자연어로 설명만 하면 시각적인 AI 에이전트 워크플로우를 자동 구성해주는 혁신적인 도구입니다.

본 프로젝트(`vd23`)는 수강생들이 Google Opal에 접속했을 때, **좌측 입력창(Left Prompt Panel)**에 무엇을 적어야 할지 막막해하는 문제를 완벽하게 해결하기 위해 설계된 **'Opal 전용 앱 생성 프롬프트 빌더'**입니다.

사용자가 만들고 싶은 아이디어나 비즈니스 주제를 제시하면, Opal의 AI 컴파일러가 인식할 수 있는 **C-I-P-O-E (Context, Input, Pipeline, Output, Edge-cases)** 구조화 프롬프트를 즉시 제작해 줍니다.

---

## 🎯 핵심 기능 (Key Features)

1. **C-I-P-O-E 5대 아키텍처 자동 변환**:
   - 단순 한 줄 아이디어를 다단계 워크플로우 노드 그래프(Input -> Search -> Gemini Pro -> Markdown/Table -> Output)로 확장.
2. **창업지도사 10대 실무 앱 라이브러리**:
   - 린 캔버스, 정부지원사업(PSST), 경쟁사 배틀카드, 옴니채널 마케팅, VC 압박면접 등 즉시 시연 가능한 템플릿 내장.
3. **더블클릭 원클릭 실행 지원 (Windows)**:
   - `command/` 폴더 내 배치파일로 복잡한 터미널 명령어 없이 즉시 파이썬 도구 및 웹 UI 실행.
4. **강의용 인터랙티브 Streamlit GUI**:
   - 프로젝터 화면에 띄워두고 수강생들의 아이디어를 현장에서 실시간으로 Opal 프롬프트로 변환하여 시연 가능.

---

## 📁 디렉토리 구조 (Directory Layout)

```
vd23/
├── SKILL.md                          # Antigravity/Gemini 스킬 명세서 (YAML 표준)
├── README.md                         # 프로젝트 안내 및 강의 가이드
├── requirements.txt                  # 파이썬 의존성 패키지
├── command/                          # Windows 원클릭 실행 스크립트
│   ├── [000]_command.txt             # 전체 명령어 매뉴얼
│   ├── 01_환경설치_원클릭.bat         # 가상환경 및 라이브러리 설치
│   ├── 02_Opal프롬프트생성기_실행.bat # CLI 대화형 프롬프트 생성기 실행
│   ├── 03_Streamlit_웹앱_실행.bat     # 강의 시연용 로컬 웹 대시보드 구동
│   └── 04_스킬전역등록_원클릭.bat     # Antigravity 전역 스킬 폴더에 자동 등록
├── prompt/                           # 강의 및 실습용 마스터 프롬프트 교안
│   ├── [001]_Opal_컴파일러_구조화_가이드.md
│   ├── [002]_창업지도사_10대_자동화앱_프롬프트.md
│   └── [003]_수강생_실습_미션_시나리오.md
├── src/                              # 프롬프트 생성 파이썬 엔진
│   ├── __init__.py
│   ├── opal_prompt_builder.py        # C-I-P-O-E 구조화 핵심 로직
│   ├── cli.py                        # 대화형 CLI 인터페이스
│   └── app_streamlit.py              # 강의 시연용 Streamlit 웹 애플리케이션
├── templates/                        # Opal 좌측 창 복사용 텍스트 템플릿
│   ├── 01_lean_canvas_builder.txt
│   ├── 02_psst_grant_proposal.txt
│   ├── 03_competitor_analyzer.txt
│   ├── 04_omnichannel_content.txt
│   └── 05_vc_pitch_stress_tester.txt
├── jupyternotebook/                  # 수강생 단계별 실습 노트북
│   └── [001]_Google_Opal_프롬프트_마스터_실습.ipynb
└── result/                           # 생성된 프롬프트 결과물 저장소
    └── sample_generated_prompts.md
```

---

## 🚀 빠른 시작 (Quick Start)

### 방법 1: Windows 배치 파일로 실행 (권장)
1. `command/01_환경설치_원클릭.bat` 더블 클릭 (최초 1회 실행)
2. `command/03_Streamlit_웹앱_실행.bat` 더블 클릭 -> 브라우저에서 직관적으로 프롬프트 생성 및 복사

### 방법 2: 명령줄(CLI)에서 직접 실행
```bash
# 1. 의존성 설치
pip install -r requirements.txt

# 2. CLI 대화형 프롬프트 생성기 실행
python src/cli.py

# 3. 또는 강의 시연용 Streamlit 웹앱 실행
streamlit run src/app_streamlit.py
```

---

## 🧑‍🏫 강의 진행 시연 팁 (Instructional Tips)

1. **비교 시연 (Before vs After)**:
   - **Before**: 수강생들에게 *"스타트업 마케팅 챗봇 만들어줘"*라고 Opal에 넣게 한 뒤, 단순 1노드가 나오는 것을 보여줍니다.
   - **After**: 본 스킬(vd23)이 생성한 5단계 C-I-P-O-E 프롬프트를 복사하여 넣게 한 뒤, 입력 폼 + 웹 검색 + 다중 페르소나 + 테이블 대시보드 노드가 한눈에 펼쳐지는 것을 시각적으로 체감시킵니다.
2. **노드 튜닝 (우측 Inspector 패널)**:
   - 자동 생성된 노드 중 Gemini 추론 노드를 클릭하여 Model을 `Gemini 1.5 Pro`로 변경하고 Temperature를 조정하는 팁을 안내합니다.

---

## 📄 라이선스 (License)
- 본 스킬은 MIT License를 따르며, (AX)창업지도사 장대표의 고유 노하우를 바탕으로 제작되었습니다.
- 교육 및 비즈니스 현장에서 자유롭게 활용하실 수 있습니다.
