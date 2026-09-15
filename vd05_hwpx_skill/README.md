# [VD-05] vd05_hwpx_skill — 한글(HWPX) & PSST 사업계획서 자동화 스킬

[![VD Series](https://img.shields.io/badge/VD%20Series-vd05-blue.svg)](https://github.com/dansarang99/vd)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://www.python.org/)
[![OWPML Standard](https://img.shields.io/badge/OWPML-KS%20X%206101-orange.svg)](https://www.hancom.com)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg)]()

> **대한민국 공공기관 표준 전자문서(HWPX/OWPML) 및 2026 정부지원사업(PSST) 사업계획서 완전 자동 생성 & 무결성 검증 엔진**  
> 이현구 교수의 OWPML 강의 자산을 바탕으로, **(AX)창업기술 대표 이한규**가 실무 오류 해결책과 2026년도 초기창업패키지 표준 규격을 접목하여 완성한 VD 시리즈 공식 마스터 스킬입니다.

---

## 🌟 주요 특징 (Core Highlights)

1. **한컴오피스 "파일이 손상되었습니다" 원천 차단 (공식 템플릿 블루프린트 구조)**
   - 파이썬으로 백지에서 조립 시 발생하는 `<hp:secPr>`(용지 규격, 구역 속성) 및 필수 메타데이터 누락 버그를 완벽 해결
   - 한컴오피스 공식 표준 서식(`02_공공기관_기본보고서_양식.hwpx`)을 원천 베이스로 채택하여 안전한 인-플레이스(In-Place) 치환 수행
2. **2026 초기창업패키지 / 예비창업패키지 (PSST) 원클릭 빌더**
   - 중소벤처기업부 및 창업진흥원 최신 4대 평가 영역(**Problem, Solution, Scale-up, Team**) 표준 서식 지원
   - 표지, 목차, 대제목, 소제목, 세부 본문 불릿 포인트 자동 맵핑
3. **한컴오피스 '글씨 겹침 버그' 100% 원천 차단**
   - 텍스트 수정 시 구버전 줄바꿈 캐시가 남아 글자가 겹쳐 인쇄되는 한글의 고질적 결함을 `clear_layout_cache.py`로 완벽 해결
   - 한글 프로그램이 문서를 열 때 행 높이와 줄바꿈 위치를 스스로 최적 계산하도록 조치
4. **OWPML 국제 표준 및 ZIP 압축 규약 완벽 준수**
   - 한컴오피스가 파일을 거부하지 않도록 `mimetype` 무압축(`ZIP_STORED`) 첫 번째 항목 배치 원칙 준수
   - `<hh:idMappings>`의 태그 개수와 실제 선언 개수 일치 보장
5. **동적 표 확장 엔진 ("붕어빵 틀 기법")**
   - 가변적인 데이터(사업비 집행 계획, 일정표 등)를 정합성 깨짐 없이 확장하는 `<hp:tbl>` 자동 생성기
6. **사전 배포 게이트키퍼 (`verify_hwpx.py`)**
   - 파일 생성 후 사용자에게 전달하기 전, ZIP 구조, XML 유효성, 표 병합 범위, 이미지 무결성을 자동 전수 검사하여 합격(`PASS`) 보장

---

## 🚀 빠른 시작 (Quick Start)

### 1. 1-클릭 환경 설치 (Windows)
`setup_vd05.bat`를 더블 클릭하거나 명령 프롬프트에서 실행합니다:
```cmd
setup_vd05.bat
```
*(또는 PowerShell 환경인 경우 `.\setup_vd05.ps1` 실행)*

### 2. 초기창업패키지 사업계획서 생성
```bash
python scripts/psst_builder.py
```
- 실행 즉시 `templates/01_초기창업패키지_사업계획서_표준양식.hwpx` 및 `result/[001]_2026_초기창업패키지_사업계획서_완성본.hwpx`가 생성됩니다.

### 3. 산출물 무결성 검증
```bash
python scripts/verify_hwpx.py result/[001]_2026_초기창업패키지_사업계획서_완성본.hwpx
```

---

## 📂 폴더 구조 (Directory Structure)

```text
vd05_hwpx_skill/
├── SKILL.md                  # AI 에이전트 지침서 (Agent Protocol)
├── README.md                 # 본 문서
├── requirements.txt          # 의존성 라이브러리 목록
├── setup_vd05.bat            # 윈도우 원클릭 설치기
├── setup_vd05.ps1            # PowerShell 설치기
├── scripts/
│   ├── hwpx_engine.py        # HWPX 코어 생성 및 XML 치환 엔진
│   ├── psst_builder.py       # 2026 초창패/예창패 사업계획서 생성기
│   ├── table_builder.py      # 붕어빵 틀 기법 기반 동적 표 생성기
│   ├── clear_layout_cache.py # linesegarray 레이아웃 캐시 제거기
│   ├── autofit_table_rows.py # 표 높이 및 제목표 정규화 스크립트
│   ├── verify_hwpx.py        # OWPML 무결성 최종 검증기
│   └── result_manager.py     # 산출물 [001]~[999] 번호 자동 관리자
├── templates/
│   ├── 01_초기창업패키지_사업계획서_표준양식.hwpx
│   └── 02_공공기관_기본보고서_양식.hwpx
├── prompts/                  # 5대 표준 실습 프롬프트
│   ├── 01_2026_초기창업패키지_사업계획서_작성.md
│   ├── 02_예비창업패키지_사업계획서_작성.md
│   ├── 03_공공기관_기본보고서_작성.md
│   ├── 04_동적표_생성_및_데이터_채우기.md
│   └── 05_HWPX_서식_오류진단_및_캐시정리.md
├── jupyternotebook/
│   └── 01_HWPX_기초부터_사업계획서_완성까지.ipynb
└── result/                   # 최종 생성된 HWPX 문서 저장소
```

---

## 💬 AI 에이전트 대화 예시

AI 어시스턴트(Claude Code, Codex, Antigravity 등)에 다음과 같이 자연어로 요청할 수 있습니다:

> *"vd05 스킬을 사용해서 2026년도 초기창업패키지 사업계획서 하나 작성해줘. 아이템명은 'AI 기반 시니어 디지털 케어 가이드북'이고 대표자는 (AX)창업기술 이한규 대표야. 표 양식과 4대 영역(Problem, Solution, Scale-up, Team)을 알차게 채워서 HWPX로 만들어주고 verify까지 통과시켜줘."*

---

## 📜 라이선스 및 크레딧

- **원천 기술 자산**: 이현구 교수 OWPML 교육 자료 및 기본 스크립트
- **기획 및 고도화**: (AX)창업기술 대표 이한규 (2026 PSST 표준화 및 오류 해결 알고리즘 패키징)
- 본 패키지는 **VD 시리즈(vd01~vd99)**의 공식 모듈로 등록되어 연구, 강의, 창업 현장에서 자유롭게 활용할 수 있습니다.
