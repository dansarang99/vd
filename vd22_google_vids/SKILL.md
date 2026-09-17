---
name: ai-video-pipeline
description: "특정 주제와 기획 아이디어를 입력받아 (1)주요 등장인물 캐릭터 생성 (2)캐릭터 시트(다양한 자세/표정) 생성 (3)기승전결 N장면 줄거리(시놉시스) 생성 (4)각 장면별 시나리오 연출 확장 (5)각 장면별 용도별 5대 대본(이미지, 비디오, TTS 나레이션, 자막, 효과음 및 돌발대사)을 체계적으로 생성하는 AI 비디오 제작 마스터 파이프라인. Google Flow, Google Vids, Vrew, CapCut, Filmora, Runway, Midjourney 등 AI 영상 및 대본 제작 요청 시 반드시 활성화하여 사용할 것."
---

# AI 비디오 제작 스토리보드 & 5대 마스터 대본 파이프라인 (AI Video Pipeline)

이 스킬은 **특정 주제와 기획 아이디어**를 입력받았을 때, 직관적이고 체계적인 5단계 파이프라인을 거쳐 **최종 5대 제작 대본(이미지, 동영상, 나레이션, 자막, 효과음/돌발대사)**을 완벽하게 산출하는 영상 기획·제작 표준 프로토콜입니다.

산출된 대본은 **Google Flow, Google Vids, Vrew, CapCut, Wondershare Filmora, Runway Gen-3, Luma Dream Machine, Kling, Midjourney** 등에서 원스톱으로 즉시 사용할 수 있습니다.

---

## 🎯 핵심 5단계 파이프라인 워크플로우

```
[사용자 입력: 주제 & 기획 아이디어]
        │
        ▼
[1단계] 주인공 및 주요 등장인물 캐릭터(1~N) 생성 (비주얼 DNA & 외형 프롬프트)
        │
        ▼
[2단계] 캐릭터 시트(다각도 턴어라운드 + 핵심 감정 표정 4~6종) 생성
        │
        ▼
[3단계] 기승전결 N장면 줄거리(시놉시스) 구성 (시간 배분 & 감정선)
        │
        ▼
[4단계] 각 장면별 시나리오 연출 확장 (시공간, 구도, 행동/제스처, 템포)
        │
        ▼
[5단계] 각 장면별 용도별 5대 마스터 대본 일괄 생성 (가장 중요!)
        ├── 🖼️ Track 1. 이미지 생성용 대본 (영문 프롬프트)
        ├── 🎥 Track 2. 동영상 생성용 대본 (카메라 무빙 & 모션)
        ├── 🎙️ Track 3. 나레이션용 대본 (TTS 구연동화 호흡)
        ├── 📝 Track 4. 자막용 대본 (가독성 1~2줄)
        └── 🔊 Track 5. 사운드 디자인 (돌발 대사, SFX, BGM 무드)
```

---

## 📋 단계별 상세 실행 가이드라인

### [1단계] 주인공 및 주요 등장인물 캐릭터(1~N) 생성
등장인물 간의 대비와 영상 전체의 시각적 일관성(Visual Consistency)을 보장하기 위한 캐릭터 설계도입니다.
- **캐릭터 프로필**: 이름, 역할, 성격, 시그니처 소품/의상, 체형, 색상 팔레트
- **Master Character Prompt (영문)**: AI 이미지 생성기(Midjourney, Imagen 3, Flux 등)에서 고정적으로 사용할 마스터 프롬프트
- **고정 앵커 키워드(Visual DNA)**: 이후 장면마다 캐릭터가 변형되지 않도록 고정하는 3~5개 영문 키워드 묶음

### [2단계] 캐릭터 시트(다양한 자세/표정) 생성
일관된 모델을 기반으로 다양한 각도와 표정을 확보하는 기준 이미지 프롬프트입니다.
- **Turnaround Sheet Prompt (영문)**: 순백색 배경(Clean white background), 전신(Full body), 정면(Front), 3/4 측면(3/4 View), 완전 측면(Profile), 후면(Back view) 턴어라운드
- **Expression Sheet Prompt (영문)**: 4~6종 핵심 감정 표정 (자신만만, 결의/집중, 놀람/경악, 편안한 낮잠/안도, 기쁨/환호 등)
- **일관성 유지 옵션 가이드**: Midjourney `--cref [이미지URL] --cw 100` 및 Imagen/Flux 고정 앵커 기법 안내

### [3단계] 기승전결 N장면 줄거리(시놉시스) 구성
전체 러닝타임(예: 60초 숏폼은 4~6장면, 2~3분 롱폼은 8장면)에 맞춰 극적 텐션을 분배합니다.
- **기 (Introduction / 起)**: 세계관, 배경, 캐릭터 등장 및 대결/사건 성사
- **승 (Development / 承)**: 본격적인 전개, 격차 발생, 갈등 및 방심
- **전 (Climax / 轉)**: 예상치 못한 반전, 역전의 드라마, 결정적 위기/기회
- **결 (Resolution / 結)**: 결승선 통과, 갈등 봉합, 교훈적 여운 및 감동
*(각 장면당 시간 배분: 약 15~25초 권장)*

### [4단계] 각 장면별 시나리오 연출 확장 (Cinematic Direction)
각 장면에 대해 영화/애니메이션 연출 지문 4대 요소를 구체화합니다:
1. **시간 및 배경 환경 (Time & Space)**: 계절, 날씨, 조명(아침 햇살, 정오 뙤약볕, 석양 노을 등), 배경 사물
2. **카메라 샷 구도 (Cinematography)**: Wide shot, Low-angle, Extreme close-up, Tracking shot, Over-the-shoulder, Dutch angle 등
3. **캐릭터 행동 및 표정 연출 (Acting & Gesture)**: 동작의 시작과 끝, 시선 처리, 슬랩스틱이나 감정 표출
4. **분위기 및 템포 (Mood & Pacing)**: 긴장감, 유쾌함, 나태함, 다급함 등 호흡 속도

### [5단계] 각 장면별 용도별 5대 마스터 대본 생성 (Master Production Script)
모든 장면(Scene 1~N)에 대해 다음 5개 트랙을 **규격화된 서식**으로 통일하여 출력합니다.

```markdown
[ N장면 ] 🎬 Scene N : [장면 제목]

• 🖼️ [이미지용 대본] (Midjourney / Imagen 3 / Google Flow 호환)
  [Visual DNA 앵커] + [동작/상황] + [배경/조명] + [카메라 앵글] + [스타일] --ar 16:9 --v 6.0

• 🎥 [동영상용 대본] (Runway Gen-3 / Luma / Kling / Veo 2 호환)
  [카메라 무브먼트: Dolly/Pan/Tracking] + [피사체 모션 속도] + [환경 모션] + cinematic lighting

• 🎙️ [나레이션용 대본] (Google Vids / Vrew TTS 호환)
  "호흡 조절 쉼표와 감정 지시문이 포함된 자연스러운 한국어 구연동화/스토리텔링 대본 (2~3문장)"

• 📝 [자막용 대본] (CapCut / Vrew 화면 하단 자막)
  화면 가독성에 맞춘 1~2줄 핵심 문구 (20자 내외)

• 🔊 [사운드 디자인]
  - 💬 돌발 대사: 캐릭터 현장 대사/감탄사 (예: 토끼 - "어라? 지금 몇 시지?!")
  - 🎵 효과음(SFX): 구체적 폴리 사운드 (발자국, 바람 소리, 환호성 등)
  - 🎼 BGM: 장면 무드 및 추천 악기 구성 (예: 긴박한 카툰 체이스 오케스트라)
```

---

## 🛠️ 편집 툴 연동 안내 (Google Vids, Vrew, CapCut)

1. **Google Vids (vids.google.com)**
   - 영상 트랙: 무성으로 생성된 비디오 클립을 타임라인에 순서대로 배치
   - 대본(Script) 패널: `Track 3 (나레이션)`을 붙여넣고 한국어 AI 음성 생성
   - 텍스트 박스: 하단에 반투명 박스를 깔고 `Track 4 (자막)` 입력
   - 오디오 트랙: `Track 5 (SFX/돌발대사)` 및 BGM 추가 후 오디오 더킹(Ducking) 적용

2. **Vrew (vrew.voyagerx.com)**
   - `[텍스트로 비디오 만들기]` 선택 후 `Track 3 (나레이션)`을 전체 붙여넣기
   - AI 목소리와 자막이 자동 동기화되면, 배경 비디오 클립을 `Track 1/2` 결과물로 교체

3. **CapCut / Filmora**
   - 타임라인에 비디오 클립 배치
   - `Track 4 (자막)`을 텍스트 템플릿으로 적용하거나 SRT 자막 파일 임포트
   - 오디오 라이브러리 검색창에 `Track 5 (SFX)` 키워드를 검색하여 효과음 매칭

---

## 📁 파일 및 템플릿 참조 (100% 상대 경로)
- 워크플로우 상세 매뉴얼: `./workflows/01_pipeline_workflow.md`
- Google Vids 6~10단계 실전 가이드: `./workflows/02_google_vids_guide.md`
- 마스터 프롬프트 템플릿: `./templates/master_prompt_templates.md`
- 빈 대본 양식: `./templates/script_format_template.md`
- 토끼와 거북이 완성 예시: `./examples/rabbit_and_turtle_master.md`
- 자막 자동 변환 스크립트: `./scripts/export_to_srt.py`
