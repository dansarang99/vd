---
name: vd05_hwpx_skill
description: >
  한글(HWPX) 문서 생성 및 2026년도 초기창업패키지/예비창업패키지 PSST 사업계획서 자동 빌더 스킬 (vd05).
  정부지원사업(초창패, 예창패), 공공기관 보고서, 표준 공문서 HWPX(OWPML) 포맷을 생성 및 편집합니다.
  한컴오피스 '글씨 겹침 현상'의 원인인 linesegarray 레이아웃 캐시 제거, mimetype 무압축 규약,
  동적 표 확장(붕어빵 틀 기법), 그리고 100% 무결성 검증 파이프라인(verify_hwpx)을 제공합니다.
---

# Autonomous HWPX & PSST Business Plan Engine (vd05_hwpx_skill)

> **[VD-05] 대한민국 공공기관 표준 전자문서(HWPX/OWPML) 및 정부지원사업 사업계획서(PSST) 전자동 생성 엔진**  
> - **기초 기술 자산**: 이현구 교수의 HWPX(OWPML) 아키텍처 강의 및 스크립트 기반  
> - **실무 고도화 및 사업계획서 패키징**: (AX)창업기술 대표 이한규 (2026 초기창업패키지 표준 규격 탑재)

---

## 1. 개요 및 핵심 해결 과제 (Why vd05?)

파이썬 및 AI 에이전트로 HWPX(한글 표준 XML 문서)를 다룰 때 발생하는 3대 치명적 결함을 완벽히 해결한 패키지입니다:

1. **파일 손상 방지 ("파일이 손상되었습니다 / 알 수 없는 오류입니다") [★ 핵심 황금률]**:
   - **원인 규명**: 파이썬으로 백지(raw XML 문자열)에서 HWPX를 조립하면, 한컴오피스가 페이지 규격을 읽기 위해 필수적으로 요구하는 **`<hp:secPr>`(용지 여백, 인쇄 방향, 구역 설정 태그)** 및 `settings.xml`, `manifest.xml`, `container.rdf`, `Preview/` 등의 시스템 필수 메타데이터가 누락되어 한컴오피스가 "파일이 손상되었습니다"라며 문서를 강제 거부합니다.
   - **완벽한 해법**: 한컴오피스가 직접 생성한 **공식 정식 템플릿(`report-template.hwpx` / `02_공공기관_기본보고서_양식.hwpx`)을 절대 원천 베이스(Base Blueprint)**로 삼아, 내부의 표지·목차·본문 단락을 안전하게 인-플레이스(In-Place) 치환합니다.
   - `mimetype` 파일은 반드시 ZIP 아카이브의 **첫 번째 항목(First Entry)**이어야 하며, **무압축(ZIP_STORED, 0% 압축)**으로 저장되어야 합니다.
   - `Contents/header.xml` 내의 `charPrCnt`, `borderFillCnt` 등의 선언 개수가 실제 태그 개수와 1:1로 일치해야 합니다.
2. **글씨 겹침 현상(Font Overlap Bug) 100% 제거**:
   - 한글 프로그램은 텍스트 줄바꿈 좌표를 `<hp:linesegarray>`에 캐싱합니다.
   - 파이썬으로 텍스트를 수정하면 글자 수가 변해도 옛 캐시가 남아있어 늘어난 글자가 마지막 줄 위에 겹쳐 인쇄되는 버그가 발생합니다.
   - 본 스킬은 문서 전체의 레이아웃 캐시를 안전하게 스트립(`clear_layout_cache.py`)하여 한글 프로그램이 문서를 열 때 줄 배치를 스스로 재계산하게 만듭니다.
3. **가변 표(Table) 동적 확장 ("붕어빵 틀 기법")**:
   - 표의 행 수가 가변적인 예산 내역, 일정표 등을 생성할 때, 헤더 행과 데이터 셀의 XML 서식 틀을 복제하여 정합성을 유지합니다.

---

## 2. 핵심 디렉토리 및 도구 체계

```text
vd05_hwpx_skill/
├── SKILL.md                  # 본 지침서 (AI 에이전트 실행 프로토콜)
├── README.md                 # 사용자 및 강사용 매뉴얼
├── requirements.txt          # lxml 등 의존성 목록
├── setup_vd05.bat            # 1-클릭 윈도우 환경 설치기
├── setup_vd05.ps1            # PowerShell 설치기
├── scripts/
│   ├── hwpx_engine.py        # OWPML 코어 엔진 (XML 이스케이프, 안전 치환, 패키징)
│   ├── psst_builder.py       # 2026 초기창업패키지 사업계획서 전용 빌더
│   ├── table_builder.py      # 붕어빵 틀 기법 기반 동적 <hp:tbl> 생성기
│   ├── clear_layout_cache.py # linesegarray 레이아웃 캐시 전면 제거기
│   ├── autofit_table_rows.py # 표 셀 높이 자동 맞춤 및 제목표 정규화
│   ├── verify_hwpx.py        # OWPML 스키마 및 무결성 최종 검증기 (Gatekeeper)
│   └── result_manager.py     # 산출물 [001]~[999] 자동 번호 매김 관리자
├── templates/
│   ├── 01_초기창업패키지_사업계획서_표준양식.hwpx # 표준 4대 영역 PSST 템플릿
│   └── 02_공공기관_기본보고서_양식.hwpx          # 공공기관 표준 기안서/보고서 템플릿
├── prompts/                  # 5대 표준 실습 프롬프트
│   ├── 01_2026_초기창업패키지_사업계획서_작성.md
│   ├── 02_예비창업패키지_사업계획서_작성.md
│   ├── 03_공공기관_기본보고서_작성.md
│   ├── 04_동적표_생성_및_데이터_채우기.md
│   └── 05_HWPX_서식_오류진단_및_캐시정리.md
├── jupyternotebook/
│   └── 01_HWPX_기초부터_사업계획서_완성까지.ipynb # 강의 실습용 주피터 노트북
└── result/                   # 최종 완성 HWPX 문서 저장소
```

---

## 3. PSST 사업계획서 4대 핵심 구조 (2026년 공통 표준)

모든 창업패키지 사업계획서는 다음 4개 항목을 충실히 반영해야 합니다:

| 항목 | 영문 명칭 | 세부 기술 내용 |
|---|---|---|
| **1. 문제 인식** | **Problem** | 창업아이템의 개발 동기, 기존 시장의 한계점, 해결하고자 하는 사회적/기술적 문제 |
| **2. 실현 가능성** | **Solution** | 창업아이템의 핵심 기능, 경쟁사 대비 차별성, 시제품 제작 및 기술 구현 방안 |
| **3. 성장 전략** | **Scale-up** | 비즈니스 모델(수익화 BM), 마케팅 및 시장 진입(B2G/B2B/B2C), 연도별 매출 로드맵 |
| **4. 팀 구성** | **Team** | 대표자 도메인 전문성, 핵심 팀원 역량, 외부 파트너십 및 지식재산권(특허) 현황 |

---

## 4. AI 에이전트 실행 프로토콜 (Step-by-Step)

사용자가 한글 문서나 사업계획서 생성을 요청할 때 다음 순서를 엄격히 준수하십시오:

### Step 1: 입력 데이터 수집 및 분석
- 사용자로부터 창업아이템명, 신청 기업, 대표자명, 지원금 규모, 문제의식, 솔루션 요약 등을 확인합니다.
- 부족한 정보가 있을 경우 기본값을 안전하게 가정하거나 사용자에게 질문합니다.

### Step 2: HWPX 문서 생성
- **초기창업패키지 / 예비창업패키지**:
  ```bash
  python scripts/psst_builder.py
  ```
  또는 파이썬 내부 호출:
  ```python
  from scripts.psst_builder import build_psst_hwpx
  from scripts.result_manager import get_next_hwpx_filename

  out_path = get_next_hwpx_filename("result", "2026_초기창업패키지_사업계획서_아이템명")
  build_psst_hwpx(output_path=out_path, ...)
  ```
- **공공기관 기안/보고서 양식 치환**:
  ```python
  from scripts.hwpx_engine import replace_in_hwpx

  replace_in_hwpx(
      template_hwpx="templates/02_공공기관_기본보고서_양식.hwpx",
      output_hwpx=out_path,
      replace_dict={"{{보고서제목}}": "...", "{{추진배경}}": "..."},
      clear_cache=True
  )
  ```

### Step 3: 레이아웃 캐시 정리 (필수 관문)
텍스트를 치환하거나 외부 템플릿을 수정한 경우 한컴오피스 글씨 겹침 방지를 위해 반드시 실행합니다:
```bash
python scripts/clear_layout_cache.py <생성된파일경로.hwpx>
```

### Step 4: 최종 무결성 검증 (Gatekeeper)
사용자에게 산출물을 안내하기 전 반드시 무결성 검사를 통과해야 합니다:
```bash
python scripts/verify_hwpx.py <생성된파일경로.hwpx>
```
- 출력에서 `→ PASS`가 확인되어야 완료로 인정됩니다.
- 만약 FAIL이 발생하면 XML 태그 닫힘, ZIP_STORED 여부 등을 즉시 수정 후 재검증하십시오.

---

## 5. 저작권 및 크레딧 표기 규정
- **원천 기술 출처**: 이현구 교수의 HWPX 아키텍처 강의를 바탕으로 합니다.
- **실무 고도화**: (AX)창업기술 대표 이한규에 의해 PSST 양식화 및 무결성 자동화 파이프라인으로 완성되었습니다.
- 모든 문서 및 생성물은 연구·교육·창업 목적으로 자유롭게 배포 및 활용 가능합니다.
