# 🎓 VD (Visual Design & AI Presentation Master Series)

> **비제이짱(BJ Jang)의 AI 실무 자동화 & 프레젠테이션 마스터 강의 공식 스킬 저장소**  
> GitHub: [@dansarang99](https://github.com/dansarang99)

본 저장소는 `vd01`부터 `vd99`까지 총 100개의 실무 강의 모듈 중, **AI 에이전트(Claude Code, Codex, Antigravity 등)에 스킬(Skill)로 탑재하여 즉시 실무에 투입 가능한 엄선된 핵심 프레젠테이션 도구들**을 모아 체계적으로 관리하고 배포하는 공식 마스터 리포지토리입니다.

---

## 🏛️ Master Skills Catalog

| 모듈 ID | 스킬 명칭 | 핵심 기능 및 차별화 포인트 | 바로가기 |
| :---: | :--- | :--- | :---: |
| **`vd05`** | **HWPX & PSST Business Plan Engine** | **공공기관 표준 전자문서 & 정부지원사업(PSST) 자동화**<br>• 2026 초기창업패키지/예비창업패키지 PSST 4대 영역 자동 빌드<br>• 한컴오피스 글씨 겹침 버그(linesegarray) 100% 원천 차단<br>• mimetype 무압축 규약 및 붕어빵 틀 기법 동적 표 확장<br>• OWPML 스키마 무결성 사전 검증 게이트키퍼(verify_hwpx) | [🔗 폴더 이동](./vd05_hwpx_skill) |
| **`vd15`** | **Slide Style Cloner v2.0** | **정밀 수술형 슬라이드 복제(Surgical Remake)**<br>• 최고급 템플릿의 3D 럭셔리 그래픽/레이아웃 100% 보존<br>• 외주 브랜드 로고 및 하이퍼링크 완전 박멸<br>• C-Level 전략 내러티브 및 맞춤 미디어 인-플레이스 주입 | [🔗 폴더 이동](./vd15_slide_style_cloner) |
| **`vd16`** | **BJ Jang Presentation & EDA Master** | **원천 데이터 자동 EDA ➔ 네이티브 PPTX 자동화**<br>• CSV/Excel/API 데이터 자동 탐색적 분석(EDA) & 통계량 산출<br>• 비제이짱 시그니처 로열 블루 고화질 차트 4종 렌더링<br>• 16:9 DrawingML 파워포인트 개체별 100% 직접 편집 지원<br>• 슬라이드별 1분 통계 분석가 발표 대본(스피커 노트) 자동 주입 | [🔗 폴더 이동](./vd16_bjjang_remake) |
| **`vd22`** | **Google Flow & Vids AI Video Pipeline** | **5단계 파이프라인 & 5대 마스터 대본 자동화**<br>• 기획 아이디어 ➔ 캐릭터 ➔ 시트 ➔ 시놉시스 ➔ 5대 대본 일괄 생성<br>• 이미지, 비디오, 나레이션, 자막, 효과음 5개 트랙 분리 산출<br>• Google Flow, Google Vids, Vrew, CapCut 원스톱 연동<br>• 대본에서 SRT 자막 파일 자동 추출 파이썬 유틸리티 제공 | [🔗 폴더 이동](./vd22_google_vids) |

---

## 🚀 수강생 원클릭 설치 및 사용 가이드

모든 스킬 모듈은 **비개발자 수강생도 더블클릭 한 번으로 환경을 구축**할 수 있도록 통일된 원클릭 배치 파일(`setup_*.bat`)을 제공합니다.

### 1단계: 저장소 복제 (Git Clone)
```bash
git clone https://github.com/dansarang99/vd.git
cd vd
```

### 2단계: 원하는 스킬 모듈로 이동 후 원클릭 설치
* **`vd05` 한글(HWPX) & PSST 사업계획서 스킬 사용 시**:
  ```bash
  cd vd05_hwpx_skill
  # setup_vd05.bat 더블클릭 실행
  ```
* **`vd15` 슬라이드 스타일 복제 스킬 사용 시**:
  ```bash
  cd vd15_slide_style_cloner
  # setup_vd15.bat 더블클릭 실행
  ```
* **`vd16` 비제이짱 프레젠테이션 & EDA 스킬 사용 시**:
  ```bash
  cd vd16_bjjang_remake
  # setup_bjjang.bat 더블클릭 실행
  ```

---

## 💬 실전 호출 프롬프트 (Prompt Examples)

### [VD05] 2026 초기창업패키지 사업계획서 작성
```text
"vd05 스킬로 2026년도 초기창업패키지 사업계획서 HWPX 작성해줘. 
아이템명은 '시니어 AI 케어 전자책', 대표자는 '(AX)창업기술 이한규'야. 
Problem, Solution, Scale-up, Team 4대 영역과 요약표를 알차게 작성하고 검증까지 완료해줘."
```

### [VD15] 슬라이드 스타일 복제 & 리메이크
```text
"upload/reference_deck.pptx 파일의 럭셔리 3D 디자인을 분석해서, 
외주사 로고는 깔끔하게 삭제하고 '신규 AI 플랫폼 사업계획서' 내용으로 1:1 서지컬 리메이크해줘."
```

### [VD16] 원천 데이터 자동 EDA & 경영진 보고서
```text
"data/sample_sales_data.csv 파일 분석해줘. 
비제이짱 EDA 템플릿(bjjang_eda)으로 핵심 지표와 고화질 차트, 
발표 대본이 담긴 7장짜리 임원 보고용 PPT 만들어줘."
```

### [VD22] 구글 Flow & Vids 5단계 AI 비디오 대본 생성
```text
"'토끼와 거북이의 달리기 시합'을 주제로 ai-video-pipeline 스킬을 적용해줘.
1단계 캐릭터 생성부터 5단계 5대 대본(이미지, 동영상, 나레이션, 자막, 효과음)까지 표와 코드블록으로 완벽하게 작성해줘."
```

---

## 📜 라이선스 및 저작권 (License)
* 본 저장소의 모든 스킬은 오픈소스 기반(MIT License)의 윤리적 가이드라인을 준수하며, 비제이짱(BJ Jang)의 독창적인 실무 아키텍처와 한국어 최적화가 적용된 2차적 저작물입니다.
* 상업적 활용, 강의 교재 사용, 커뮤니티 재배포가 자유롭게 허용됩니다.
