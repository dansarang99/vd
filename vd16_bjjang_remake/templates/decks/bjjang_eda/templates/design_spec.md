---
deck_id: bjjang_eda
kind: deck
native_structure_mode: structured
summary: 비제이짱 고급 EDA 데이터 분석 보고 덱 — 원천 데이터(CSV/Excel/API) 자동 탐색적 데이터 분석, 시그니처 차트, 상관관계 드라이버, 경영진 실행 로드맵 (7장)
canvas_format: ppt169
page_count: 7
primary_color: "#1E40AF"
defaults:
  mode: structured
  visual_style: data-journalism
  delivery_purpose: balanced
---

# BJ Jang Executive EDA Data Analysis Deck - Design Specification

> 비제이짱(BJ Jang) 데이터 분석 및 EDA(Exploratory Data Analysis) 전용 템플릿입니다.
> 원천 데이터셋을 직접 입력받아 20년차 분석가 수준의 통계 연산 및 고화질 시각화 차트를 결합한 7장 프레젠테이션을 자동 생성합니다.

## I. Template Overview

| Property | Description |
| --- | --- |
| **Template Name** | bjjang_eda |
| **Display Name** | 비제이짱 고급 EDA 데이터 분석 경영진 보고 템플릿 |
| **Use Cases** | 원천 데이터(CSV, Excel, DB, API) 기반 탐색적 데이터 분석, 월간/분기 실적 분석 보고, 경영진 의사결정 브리핑 |
| **Design Tone** | 데이터 저널리즘, 신뢰성, 정밀성, 고대비 비즈니스 팔레트 |
| **Theme Mode** | 슬레이트 오프화이트(`#F8FAFC`) + 딥 로열 블루 메인(`#1E40AF`) + 일렉트릭 블루 액센트(`#2563EB`) |

## II. 7 Key Slide Structure

1. **P01. Cover**: 리포트 명칭, 원천 데이터셋 파일명, 데이터 크기(행/열), 분석 일시, 분석가 프로필
2. **P02. Dataset Health**: 데이터 규모, 결측치율(Missing Rate), 중복값 검출, 변수 유형(수치/범주/시계열) 분류 카드
3. **P03. KPI Dashboard**: 핵심 비즈니스 지표(합계, 평균, 최대값, 변동계수) 대시보드 및 통계 요약
4. **P04. Trend Analysis**: 시계열 또는 인덱스에 따른 변동 추이, 이동평균선(MA), 급등락 구간 인사이트
5. **P05. Segment Breakdown**: 범주별 기여도 순위(Rank Bar Chart), 상위 집중도 및 롱테일 분석
6. **P06. Correlation & Drivers**: 상관관계 매트릭스 히트맵, 핵심 견인 인자(Key Drivers) 및 선행지표 도출
7. **P07. Strategic Actions**: 경영진 의사결정을 위한 3대 핵심 제언 (Next Action Roadmap)
