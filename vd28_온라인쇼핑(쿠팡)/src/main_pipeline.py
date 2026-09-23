# -*- coding: utf-8 -*-
"""
==============================================================================
🚀 2026 쿠팡 실시간 쇼핑 마켓 인텔리전스 엔드투엔드 파이프라인
기획 및 지식재산권자: (AX)창업기술 이한규 대표
모노레포 저장소: https://github.com/dansarang99/vd (vd28_온라인쇼핑(쿠팡))
==============================================================================
"""
import sys
import importlib

# [001] 메인 인텔리전스 모듈 동적 로드 및 실행
module_001 = importlib.import_module("[001]_쿠팡_실시간_쇼핑_인텔리전스_분석")

if __name__ == "__main__":
    kw = sys.argv[1] if len(sys.argv) > 1 else "캠핑의자"
    module_001.run_pipeline(keyword=kw)