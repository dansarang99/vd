---
name: slide-style-cloner
description: "Reverse engineer and clone executive presentation styles from any input PDF or PPTX slide deck, extract DESIGN.md, STYLE.md, and PROMPT.md, and generate brand-new, high-fidelity executive presentation slides matching that exact aesthetic. Features the Surgical In-Place Remake Protocol: preserving 100% of luxury 3D graphics/layouts while eliminating external brand logos, replacing mismatched stock photos with custom domain assets, and mapping full-length C-level narratives."
---

# Slide Style Cloner v2.0 (슬라이드 스타일 복제 및 정밀 리메이크 마스터 스킬)

> **핵심 철학 (Core Philosophy)**:  
> 레퍼런스 템플릿의 **압도적인 3D 그래픽, 세련된 컬러 스키마, 감각적인 카드 레이아웃을 100% 온전히 보존**하면서, 외주사 로고, 부자연스러운 외국인 스톡 사진, 억지 끼워맞춘 텍스트를 정밀하게 도려내고 실전 비즈니스 로직을 주입하는 **'정밀 수술형 슬라이드 복제(Surgical In-Place Remake)'** 전문 스킬입니다.

---

## 1. 안티패턴 및 주의사항 (What NOT to Do)

1. **절대 백지에서 새로 그리지 마십시오 (Anti-Blank Canvas)**:
   - 템플릿의 억지 틀을 피하겠다고 원본 템플릿 파일(.pptx)을 버리고 빈 캔버스에서 사각형 박스로 새로 그리면, 원본의 11MB짜리 고화질 3D 그래픽과 미학 에셋이 전부 날아가고 조잡한 관공서 상자 PPT가 됩니다.
2. **단순 텍스트 치환에 머물지 마십시오 (Anti-Blind Replacement)**:
   - 표지 상단에 벡터 도형(`GROUP`)으로 숨겨진 외주사(예스폼 등) 로고를 방치하지 마십시오.
   - 도메인과 맞지 않는 외국인 스톡 모델 사진이나 IT 사무실 사진을 그대로 두지 마십시오.

---

## 2. 4대 마스터 실행 프로토콜 (Surgical In-Place Remake Protocol)

```
[입력: 레퍼런스 PPTX (예스폼 등)] + [주제: 특허/사업계획서 PDF/TXT]
                           │
                           ▼
[Phase 1] 비주얼 & 벡터 구조 디컴포지션 (Decomposition)
  - 캔버스 해상도, 테마 컬러(XML), 폰트 스케일 파싱 -> [004]_DESIGN.md, [005]_STYLE.md 생성
  - 슬라이드 1(표지) 및 전체 슬라이드의 `GROUP` 도형 및 외부 하이퍼링크(`_rels`) 전수 스캔
                           │
                           ▼
[Phase 2] 외주 브랜드 흔적 0% 완전 박멸 (Vector Logo Purge)
  - 표지 상단의 벡터 로고 도형(예: `그룹 300`)을 찾아 `sp.getparent().remove(sp)`로 영구 삭제
  - `docProps/core.xml`, `app.xml` 메타데이터 내 외주사 정보를 신규 사명 및 IR팀으로 100% 치환
  - `slide1.xml.rels` 내 외부 상업용 하이퍼링크 관계 태그 영구 삭제
                           │
                           ▼
[Phase 3] 인-플레이스 미디어 1:1 정밀 교체 (In-Place Media Replacement)
  - 슬라이드의 마스크, 크기, 위치, 그림자를 1mm도 깨지 않고 유지
  - PPTX 압축 구조(`ppt/media/`) 내의 부자연스러운 스톡 사진을 바이트 레벨에서 1:1 교체:
    • 인력 소개(Slide 5): 세이지그린/네이비 톤의 공인 C-레벨 프로필 엠블럼 카드로 교체
    • 타겟 페르소나(Slide 8): 수요자 vs 공급자 듀얼 시너지 인포그래픽으로 교체
    • 솔루션 및 기능(Slide 12, 14, 15): 코어 엔진, 서비스 플로우, 원천특허 테크 카드로 교체
                           │
                           ▼
[Phase 4] 30장 완결형 실전 내러티브 매핑 (Full Narrative Mapping)
  - 원본 슬라이드의 시각적 계층(Action Title, Kicker, Metric, Body)에 1:1 매칭되는 실전 카피 주입
  - 줄바꿈이나 다중 단락으로 누락되던 미치환 플레이스홀더 문구를 전수 색출하여 100% 완결
                           │
                           ▼
[Phase 5] 표준 아카이브 패키징 및 번호 체계화 ([001] ~ [999])
  - `result/`, `images/`, `src/`, `jupyternotebook/` 4대 서브폴더 구성
  - 비교 검증을 위한 3대 PPT 버전(v1.0 초기치환 / v2.0 12장압축 / v3.0 최종마스터피스) 동시 보존
```

---

## 3. 표준 폴더 및 파일 번호 체계 (`[001]` ~ `[999]`)

모든 복제 작업은 아래와 같은 표준 서브폴더 규격으로 정리하여 아카이빙합니다:

```
[템플릿식별자]/
├── result/               # 3대 PPTX 버전 및 디자인/스타일 명세서
│   ├── [001]_[프로젝트명]_IR_v1.0_초기단순치환본(30장).pptx
│   ├── [002]_[프로젝트명]_IR_v2.0_Executive압축본(12장).pptx
│   ├── [003]_[프로젝트명]_IR_v3.0_최종마스터피스(30장).pptx
│   ├── [004]_DESIGN.md
│   ├── [005]_STYLE.md
│   ├── [006]_PROMPT.md
│   ├── [007]_ref_style_analysis.json
│   ├── [008]_ref_shapes_detail.json
│   ├── [009]_ref_complete_text.json
│   └── [010]_검증_및_리메이크_완료_보고서.md
│
├── images/               # 슬라이드에 1:1 교체 삽입된 커스텀 고해상도 그래픽 에셋
│   ├── [001]_avatar_ceo.jpg
│   ├── [002]_avatar_cto.jpg
│   ├── [003]_avatar_coo.jpg
│   ├── [004]_avatar_cfo.jpg
│   ├── [005]_dual_persona.png
│   ├── [006]_tech_core_engine.jpg
│   ├── [007]_tech_service_flow.jpg
│   ├── [008]_tech_patents.jpg
│   └── [009]_tech_screen_ui.png
│
├── src/                  # 파이프라인 변환 및 생성 스크립트 모음
│   ├── [001]_remake_master_deck.py      (핵심 수술 및 미디어 교체 엔진)
│   ├── [002]_generate_custom_assets.py  (도메인 맞춤 이미지 생성기)
│   ├── [003]_generate_executive_deck.py (12장 퀵 피치덱 생성기)
│   └── [004]_verify_final_pptx.py       (무결성 및 잔재 검증기)
│
└── jupyternotebook/      # 셀 단위 인터랙티브 실행 및 파이프라인 검증 환경
    └── [001]_[프로젝트명]_스타일복제_파이프라인.ipynb
```

---

## 4. 검증 체크리스트 (Quality Audit Gate)

최종 릴리즈 전 반드시 아래 4대 무결성 기준을 통과해야 합니다:
1. **외주 브랜드 로고 잔재 0건**: ZIP 내 모든 XML/RELS 및 표지 그룹 도형 전수 검사 통과.
2. **미치환 플레이스홀더 0건**: "내용을 입력하세요", "세부내용", 불일치 도메인 용어 완전 소멸.
3. **사진 조화도 100%**: 외국인 스톡 모델 얼굴이 도메인 맞춤 에셋으로 완전 대체되었는가.
4. **원본 비주얼 보존율 100%**: 원본 템플릿의 3D 그래픽, 그림자, 카드 레이아웃이 훼손 없이 살아있는가.
