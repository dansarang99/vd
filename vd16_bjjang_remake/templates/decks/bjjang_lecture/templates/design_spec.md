---
deck_id: bjjang_lecture
kind: deck
native_structure_mode: structured
summary: 비제이짱 강의 교안/교육 덱 — 3단 개념 카드, 단계별 실습 가이드, 핵심 요약, 질의응답
canvas_format: ppt169
page_count: 5
primary_color: "#1E40AF"
defaults:
  mode: instructional
  visual_style: swiss-minimal
  delivery_purpose: balanced
---

# BJ Jang Lecture & Workshop Deck - Design Specification

> 비제이짱(BJ Jang) 강의 및 워크숍 전용 슬라이드 템플릿 규격서입니다.
> 3단 개념 분해 카드, 실습 가이드 레이아웃, 핵심 요약(Takeaway) 장표를 표준 제공합니다.

## I. Template Overview

| Property | Description |
| --- | --- |
| **Template Name** | bjjang_lecture |
| **Display Name** | 비제이짱 강의 및 워크숍 교안 템플릿 |
| **Use Cases** | IT/AI 강의, 실무 워크숍, 사내 직무 교육, 웨비나 발표 자료 |
| **Design Tone** | 명확함, 직관성, 교육적 전달력 극대화, 고대비 가독성 |
| **Theme Mode** | 슬레이트 화이트(`#F8FAFC`) + 딥 네이비 텍스트 + 일렉트릭 블루 액센트(`#2563EB`) |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| **Format** | Standard 16:9 (`ppt169`) |
| **Dimensions** | 1280 × 720 px |
| **viewBox** | `0 0 1280 720` |
| **Page Margins** | 좌우 56px, 상단 52px, 하단 60px |
| **Content Area** | x=56, y=150, w=1168, h=500 |

## III. Color Palette (LOCKED)

- Background: `#F8FAFC`
- Surface (Card): `#FFFFFF`
- Surface Alt: `#F1F5F9`
- Text Primary: `#0F172A`
- Text Secondary: `#475569`
- Text Muted: `#94A3B8`
- Border: `#E2E8F0`
- Primary Brand: `#1E40AF`
- Accent (Focus): `#2563EB`
- Accent Soft: `#EFF6FF`
- Positive: `#059669`
- Warning: `#D97706`

## IV. Typography System (Pretendard)

- Title: `'Pretendard ExtraBold', Pretendard, sans-serif` (38–44px, weight 800)
- Takeaway / Subtitle: `'Pretendard SemiBold', Pretendard, sans-serif` (18–22px, weight 600, color `#2563EB`)
- Card Headline: `'Pretendard Bold', Pretendard, sans-serif` (20–24px, weight 700)
- Body: `Pretendard, sans-serif` (15–17px, weight 400, line-height 1.6)

## V. Slide Roster (5 Essential Pages)

1. `01_cover.svg`: 강의 대주제, 부제, 강사 프로필, 일시
2. `02_chapter.svg`: 모듈/챕터 전환 간지 (현재 단계 하이라이트)
3. `03_3cards_concept.svg`: 3대 핵심 개념 카드 분해 및 비교
4. `04_practice_guide.svg`: 4단계 실습 가이드 (Step 1 -> Step 2 -> Step 3 -> Step 4)
5. `05_takeaway_summary.svg`: 오늘 배운 내용 3줄 요약 + Q&A + 다음 강의 예고
