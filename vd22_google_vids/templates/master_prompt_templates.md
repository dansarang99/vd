# 🎨 마스터 프롬프트 작성 공식 & 템플릿 가이드

각 AI 생성 도구(Midjourney, Flux, Google Imagen 3, Runway, Luma, Google Vids, Suno 등)의 특성에 맞춘 최적화 프롬프트 작성 공식입니다.

---

## 1. 이미지 생성 프롬프트 공식 (Midjourney, Imagen 3, Flux, Flow)

```text
[스타일 렌더러] + [고정 캐릭터 앵커 Visual DNA] + [동작 및 자세] + [환경 및 소품] + [조명 및 분위기] + [카메라 렌즈 및 구도] + [파라미터]
```

### 필수 키워드 라이브러리:
- **스타일**: `Pixar and Disney 3D animation style`, `highly detailed 3D render`, `Unreal Engine 5 render`, `octane render`
- **조명**: `cinematic morning sunlight`, `volumetric god rays`, `golden hour sunset lighting`, `soft dappled shadows`
- **화질/해상도**: `8k resolution`, `raytracing`, `hyper-detailed texture`
- **비율 파라미터**: 
  - 유튜브 롱폼 / PC: `--ar 16:9`
  - 유튜브 쇼츠 / 틱톡 / 릴스: `--ar 9:16`

---

## 2. 비디오 생성 모션 프롬프트 공식 (Runway Gen-3, Luma, Kling, Veo 2)

```text
[카메라 무브먼트] + [피사체 주요 모션] + [배경 환경 요소의 움직임] + [빛 및 셔터 템포]
```

### 카메라 무브먼트 키워드:
- **Dolly In / Out**: `Slow smooth dolly in towards character's face`
- **Tracking / Follow**: `Ground-level fast tracking shot following the runner from behind`
- **Pan / Tilt**: `Camera pans smoothly from the sleeping rabbit to the walking tortoise`
- **Crane / Arc**: `Crane shot elevating from ground to high angle`, `Arc camera rotation circling subject`
- **Rack Focus**: `Rack focus from blurry foreground subject to sharp background subject`

---

## 3. TTS / 나레이션 대본 작성 팁 (Google Vids, Vrew, Typecast, ElevenLabs)

- **호흡 조절**: 쉼표(`,`)를 적극적으로 사용하여 인공지능 성우의 어색한 연속 발음을 방지합니다.
- **문장 길이**: 한 문장이 너무 길어지지 않도록 15~25음절 내외로 간결하게 끊어줍니다.
- **감정 지시문**: 구글 Vids TTS에서는 톤(Tone) 옵션에서 `Warm Storyteller` 또는 `Cheerful`을 선택하고, Vrew에서는 자막 분할 기능을 활용합니다.

---

## 4. 자막(Captions) 작성 규칙 (Vrew, CapCut)

- **줄바꿈 규칙**: 1회 표시당 최대 2줄, 한 줄당 최대 18~20자 이내.
- **키워드 강조**: 감탄사, 의성어/의태어, 핵심 단어에 눈에 띄는 색상이나 따옴표 적용.
- **가독성 확보**: 영상 배경이 복잡할 경우 반드시 반투명 백그라운드 바 또는 텍스트 외곽선(Stroke) 적용.

---

## 5. 사운드 디자인(SFX & BGM) 큐시트

- **돌발 대사 (Ad-lib)**: 장면의 생동감을 위해 3~5초 이내의 톡톡 튀는 감탄사 배치.
- **SFX 영문 검색 키워드**:
  - `Whoosh`, `Wind blow`, `Running steps`, `Footsteps on gravel`, `Cartoon snoring`, `Boing jump`, `Cheering crowd`, `Confetti pop`
- **BGM 무드 설정**:
  - 밝은 시작: `Playful, Pizzicato Strings, BPM 110`
  - 긴박한 질주: `Fast Tempo, Orchestral Snare, Cinematic Chase, BPM 140`
  - 평온한 인내: `Warm Acoustic Guitar, Peaceful Melody, BPM 85`
  - 감동의 승리: `Triumphant Full Orchestra, Brass Fanfare, Emotional Strings`
