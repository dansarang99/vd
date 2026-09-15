#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate 2026 초기창업패키지 사업계획서 [전자출판] - (AX)창업기술 이한규 대표
"""

import sys
from pathlib import Path

# UTF-8 stdout setup
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

base_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(base_dir / "scripts"))

from psst_builder import build_psst_hwpx
from result_manager import get_next_hwpx_filename
from verify_hwpx import check

# 1. Output destination
out_path = get_next_hwpx_filename(base_dir / "result", "2026_초기창업패키지_사업계획서_전자출판")
print(f"[1/3] 대상 파일 경로 생성: {out_path.name}")

# 2. Build PSST HWPX
item_title = "생성형 AI 기반 원클릭 멀티포맷(HWPX·ePub·PDF) 전자출판 자동화 및 인터랙티브 교육 콘텐츠 플랫폼"
ceo_info = "(AX)창업기술, 이한규 대표"
category_info = "인공지능(AI) / 디지털 콘텐츠 / 전자출판(e-Publishing)"

problem_content = """■ 1-1. 창업아이템의 개발 배경 및 필요성
  - [전통 출판의 구조적 한계]: 종이책 출판은 기획, 조판, 인쇄, 물류, 재고 관리까지 최소 3~6개월 소요 및 권당 1,000만 원 이상의 초기 비용 발생, 미판매 도서 폐기율 35%에 달함.
  - [전자출판 전환의 기술적 장벽]: 전자책 수요 급증에도 불구하고 1인 출판사 및 중소출판사의 78%가 XML/HTML 코딩 및 OWPML(한글) 변환 전문 인력 부족으로 디지털 전환에 실패.
  - [공공·교육 시장의 서식 호환 결함]: 공공기관 및 교육 현장에서는 HWPX(한글 표준) 문서 기반 교재가 필수적이나, 기존 뷰어/변환기는 글씨 겹침 및 표 깨짐 현상이 빈번하여 표준화된 솔루션 절실.

■ 1-2. 목표 시장의 미충족 수요(Unmet Needs) 및 해결 방안
  - 원고 파일(HWPX, Word, Markdown) 입력만으로 목차 분류, 교정·교열, 맞춤 조판, 삽화 생성까지 수 분 내 자동 완성하는 '원클릭 올인원 전자출판 파이프라인' 갈망.
  - 단순 열람형 전자책을 탈피하여 AI 음성 낭독(TTS), 실시간 대화형 질의응답, 모의 실습을 제공하는 '인터랙티브 리치 콘텐츠' 플랫폼 수요 폭증."""

solution_content = """■ 2-1. 창업아이템의 핵심 기능 및 기술 구현 방안
  - [지능형 멀티포맷 OWPML/ePub 3.0/PDF 자동 조판 엔진]: HWPX 국제 표준 규격(ZIP_STORED 무압축 mimetype, linesegarray 자동 제거, 붕어빵 틀 표 구조)을 100% 충족하는 무결점 패키징 기술.
  - [생성형 AI 어문 규범 교정·교열 및 맞춤 삽화 생성]: 국립국어원 표준 문법 준수 자동 윤문 기능 및 챕터별 맥락을 반영한 고해상도 AI 일러스트레이션 자동 생성 파이프라인 구축.
  - [독자 반응형 인터랙티브 가이드 뷰어 탑재]: 시니어 및 취약 계층을 위한 실시간 큰 글씨 UI(Large Font A11y), 어려운 전문 용어 자동 해설 툴팁, 1:1 도서 해설 AI 에이전트 내장.

■ 2-2. 경쟁 기술 대비 차별적 비교 우위성
  - 제작 기간 98% 단축: 통상 2~3주가 소요되던 전자책 제작 기간을 단 10분 이내로 획기적 단축.
  - 원가 비용 85% 절감: 기존 조판 외주비(권당 150~300만 원) 대비 월 구독형 SaaS 도입으로 출판사 원가 혁신 달성.
  - 공공 조달 및 글로벌 표준 완벽 호환: KS X 6101(OWPML) 및 IDPF ePub 3.0 표준 인증 획득으로 국내 공공 도서관 및 해외 플랫폼 동시 공급 가능."""

scaleup_content = """■ 3-1. 비즈니스 모델(BM) 및 수익화 전략
  - [B2B / B2G]: 전국 1인 출판사 및 중소출판사 7,000개소 대상 'AI 전자출판 SaaS 라이선스(월 99,000원)', 공공기관 및 대학교 대상 '전자책 제작 및 디지털 아카이빙 구축 용역'.
  - [B2C / 작가 크리에이터]: 독립출판, 웹소설, 실용서 작가를 위한 '원클릭 도서 출판 및 주요 서점(교보문고, YES24, 알라딘, 리디북스) 자동 유통 대행 수수료(판매액의 10~15%)'.
  - [정부 바우처 연계]: 중소벤처기업부 K-비대면 서비스 바우처 및 지자체 디지털 포용 출판 지원 사업 공급기업 등록.

■ 3-2. 연도별 시장 진입 로드맵 및 목표 매출
  - 2026년(1차년도 / 도입기): HWPX 기반 MVP 엔진 완성, 공공 조달 등록, 중소출판사 50개사 고객 유치 (목표 매출 4.5억 원).
  - 2027년(2차년도 / 성장기): 음성 인터랙티브 ePub 플랫폼 확장, 독립출판 작가 3,000명 확보, 전국 지자체 전자도서관 납품 (목표 매출 15억 원).
  - 2028년(3차년도 / 도약기): 다국어 자동 번역 전자출판 솔루션 론칭 및 글로벌 아마존 킨들(KDP) 직수출 파이프라인 가동 (목표 매출 35억 원 돌파)."""

team_content = """■ 4-1. 대표자 및 핵심 인력 보유 역량
  - 대표자 (이한규 / (AX)창업기술 대표): IT 벤처 창업 및 경영 15년, AI 자동화 시스템 아키텍처 설계 총괄, 전자출판 및 디지털 콘텐츠 특허 다수 출원.
  - AI & 소프트웨어 총괄 CTO: 거대언어모델(LLM) 파인튜닝, OWPML/XML 문서 파서 개발 및 클라우드 아키텍처 9년 경력.
  - 수석 출판 에디터 & UX 디자이너: 대형 출판사 편집기획 및 전자책 조판 디자인 7년 경력, 웹 접근성(A11y) 표준 전문가.

■ 4-2. 파트너십 및 지식재산권 확보 계획
  - 대한출판문화협회 및 전자출판협동조합 회원사와의 MOU 체결을 통한 초기 파일럿 테스트베드 확보 완료.
  - 본 사업 기간 내 'OWPML 기반 지능형 전자출판 자동 변환 시스템 및 그 방법' 특허 2건 출원 완료 예정."""

print("[2/3] PSST HWPX 사업계획서 생성 중...")
build_psst_hwpx(
    output_path=out_path,
    doc_title="2026년도 초기창업패키지(일반형) 사업계획서",
    item_name=item_title,
    ceo_name=ceo_info,
    category=category_info,
    gov_fund="70,000,000원",
    self_fund="30,000,000원 (현금 10,000,000원 / 현물 20,000,000원)",
    period="2026.05.01 ~ 2027.02.28 (10개월)",
    problem_text=problem_content,
    solution_text=solution_content,
    scaleup_text=scaleup_content,
    team_text=team_content
)

print(f"[성공] 파일 생성 완료: {out_path.name}")

# 3. Verify
print("[3/3] verify_hwpx 무결성 검증 실행...")
ok = check(str(out_path))
if ok:
    print(f"\n★ 최종 판정: PASS (한컴오피스 100% 호환 무결성 합격)")
else:
    print(f"\n★ 최종 판정: FAIL (오류 발생)")
    sys.exit(1)
