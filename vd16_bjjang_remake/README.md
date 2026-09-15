# 🚀 BJ Jang Presentation Master (`vd16_bjjang_remake`)

> **"PowerPoint에서 모든 도형과 텍스트를 직접 클릭해 수정할 수 있는 진짜 네이티브 PPTX 자동화 스킬"**  
> AI 에이전트(Claude Code, Codex, Antigravity 등)와 함께 채팅 한 번으로 고품격 비즈니스·강의 슬라이드를 완성합니다.

[![Output](https://img.shields.io/badge/output-native%20PPTX%20(DrawingML)-217346)](#)
[![Font](https://img.shields.io/badge/font-Pretendard-1E40AF)](#)
[![Brand](https://img.shields.io/badge/brand-BJ%20Jang%20Signature-2563EB)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 1. 이게 뭔가요? (1분 핵심 요약)

기존 AI 슬라이드 도구들은 슬라이드를 **통째로 하나의 큰 그림(이미지)으로 만들어 텍스트 수정이 불가능**하거나, **조악한 사각형 박스에 텍스트만 채워 넣는 한계**가 있었습니다.

`vd16_bjjang_remake`는 웹 표준 벡터 그래픽인 **SVG(Scalable Vector Graphics)**를 AI가 직접 픽셀 단위로 정밀하게 설계하고, 이를 PowerPoint의 자체 그래픽 언어인 **DrawingML 네이티브 개체**로 변환합니다.

* ✅ **PowerPoint 완벽 호환**: 모든 도형, 텍스트 상자, 선, 아이콘을 파워포인트에서 직접 클릭하여 수정 가능
* ✅ **한글 폰트 Pretendard 완벽 내장**: 폰트 깨짐이나 줄바꿈 어색함 없는 프로급 한글 타이포그래피
* ✅ **14종 전문 다이어그램 엔진 내장**: 아키텍처, 쿼드런트, 시퀀스, 타임라인 등 복잡한 구조도 자동 코딩
* ✅ **발표자 스피커 노트(대본) 자동 생성**: 발표자가 1초도 버벅이지 않도록 슬라이드 하단 메모란에 1분 발표 대본 자동 작성
* ✅ **완전 독립형 단일 패키지**: 외부 의존성 없이 이 폴더 하나만 복사하면 어디서나 즉시 실행

---

## 🎨 2. 비제이짱 시그니처 5대 덱 템플릿

자연어로 템플릿 이름을 말하기만 하면, AI가 목적에 맞는 최적의 구조와 레이아웃을 자동 적용합니다:

| 템플릿 ID | 템플릿 명칭 | 주요 용도 및 특징 |
| :--- | :--- | :--- |
| **`bjjang_eda`** 🌟 | **고급 EDA 데이터 분석 덱 (NEW)** | 원천 데이터(CSV/Excel/API) 자동 분석, 4대 고화질 차트, 상관관계 드라이버, 경영진 보고용 7장 덱 |
| **`bjjang_lecture`** | **강의 및 교육 교안 덱** | 3단 개념 분해 카드, 4단계 실습 가이드 레이아웃, Takeaway 핵심 요약, 질의응답 장표 기본 제공 |
| **`bjjang_proposal`** | **정부지원 및 비즈니스 제안서 덱** | 추진 배경, 12개월 마일스톤 간트차트, 추진 체계 조직도, 3개년 정량적 기대효과 및 ROI 지표 |
| **`bjjang_ir`** | **스타트업 IR 피치덱** | 문제-해결 구조, TAM/SAM/SOM 시장 규모 3중 동심원, 비즈니스 모델 캔버스, MoM 트랙션 성장 그래프 |
| **`bjjang_tech_ai`** | **AI 및 테크 아키텍처 덱** | 다중 에이전트 파이프라인 흐름도, 클라우드 시스템 블록도, 프론트-백엔드 시퀀스, 4계층 기술 스택 |


---

## 🛠️ 3. 초간단 원클릭 설치 가이드 (Windows)

수강생 분들이 복잡한 환경 설정 없이 1분 만에 설치할 수 있도록 원클릭 배치 파일을 제공합니다.

1. **Python 3.10 이상 설치**:
   - [python.org](https://www.python.org/downloads/)에서 설치 시 반드시 **`Add python.exe to PATH`**를 체크하세요.
2. **원클릭 설치 실행**:
   - 폴더 내 **`setup_bjjang.bat`** 파일을 더블클릭합니다.
   - 필수 라이브러리(`python-pptx`, `edge-tts` 등)가 자동 설치되고 사전 검증(Preflight)이 수행됩니다.

---

## 💬 4. 실전 사용 프롬프트 예시

AI 에이전트 채팅창에 자연어로 요청하세요:

### 예시 A. 강의 교안 제작
> "비제이짱 강의 템플릿(bjjang_lecture)으로 '직장인을 위한 실전 AI 업무 자동화' 5장 슬라이드 만들어줘. 각 장마다 1분 분량 발표 대본도 메모란에 채워줘."

### 예시 B. 스타트업 IR 피치덱
> "비제이짱 IR 템플릿(bjjang_ir)으로 AI 기반 자동 번역 B2B SaaS 기업의 시드 투자유치용 10장 피치덱을 만들어줘."

### 예시 C. 기존 PPT 성형 (1:1 리메이크)
> "projects/input.pptx 파일의 내용은 100% 유지하면서, 비제이짱 시그니처 블루 스타일로 1:1 예쁘게 리메이크해줘."

---

## 📂 5. 폴더 구조 및 아키텍처

```
vd16_bjjang_remake/
├── SKILL.md                 # 스킬 두뇌 및 오케스트레이터 정의서
├── README.md                # 강의 및 수강생용 종합 가이드 (본 파일)
├── setup_bjjang.bat         # 윈도우 원클릭 환경 설치기
├── setup_bjjang.ps1         # 파워쉘 설치 스크립트
├── requirements.txt         # 파이썬 의존 라이브러리 목록
├── scripts/                 # SVG -> DrawingML PPTX 변환 및 검증 엔진
├── workflows/               # 단계별 실행 지침서 (신규 생성, 리메이크, 검증 등)
├── templates/
│   ├── brands/              # 비제이짱 시그니처 브랜드 (bjjang) 및 글로벌 브랜드
│   ├── decks/               # 4대 시그니처 덱 (lecture, proposal, ir, tech_ai)
│   └── icons/               # 12,000+ 벡터 아이콘 라이브러리
├── diagram-design/          # 14대 전문 다이어그램 엔진 레퍼런스
├── assets/fonts/Pretendard/ # Pretendard 폰트 팩 번들
└── prompts/                 # 실습용 원클릭 프롬프트 모음 10선
```

---

## 📜 6. 라이선스 및 저작권 고지 (License & Attribution)

* 이 스킬은 [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) (MIT License) 및 **장피엠(Jang PM, byungjunjang)**님의 한국어 커스터마이징 오픈소스를 기반으로 제작되었습니다.
* **비제이짱(BJ Jang)**의 강의 콘텐츠 및 실무 환경에 맞춰 4대 시그니처 템플릿, 발표자 스피커 노트 자동화, 통합 단일 패키지 구조, 원클릭 윈도우 설치기가 새롭게 추가·리메이크되었습니다.
* 원 저작자들의 MIT 라이선스 규정을 준수하며, 누구나 자유롭게 학습, 강의, 상업적 활용 및 2차 리메이크가 가능합니다.
