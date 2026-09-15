#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Public Data Hub & Retriever (공공데이터포털 및 오픈데이터 연동 엔진)
Locates, retrieves, and catalogs official public datasets (data.go.kr, KOSIS, ECOS, Local CSVs)
matching the presentation topic to empower data-grounded executive storytelling.
"""

import sys
import os
import glob
import json
import argparse
from typing import Dict, Any, List

# Curated catalog of major Korean public datasets and thematic sources
PUBLIC_DATA_DIRECTORY = {
    "부동산": {
        "agency": "한국부동산원 / 국토교통부",
        "portal": "공공데이터포털 (data.go.kr)",
        "datasets": ["전국 주택 매매/전세 수급동향", "공동주택 실거래가 상세정보", "아파트 분양 및 입주물량 통계"]
    },
    "인재": {
        "agency": "고용노동부 / 한국고용정보원",
        "portal": "공공데이터포털 및 고용정보시스템 (WorkNet)",
        "datasets": ["직종별 사업체 채용동향", "청년·시니어 고용률 추이", "산업별 디지털·AI 인력 수급 실태조사"]
    },
    "경제": {
        "agency": "한국은행 (ECOS) / 통계청 (KOSIS)",
        "portal": "국가통계포털 (kosis.kr)",
        "datasets": ["소비자물가지수(CPI) 및 생산자물가지수", "기준금리 및 시장금리 변동 추이", "기업경기실사지수(BSI)"]
    },
    "클라우드": {
        "agency": "한국지능정보사회진흥원 (NIA) / 과학기술정보통신부",
        "portal": "공공데이터포털 (data.go.kr)",
        "datasets": ["국내 공공 및 민간 클라우드 도입 현황", "인공지능(AI) 산업 실태조사", "디지털 정부 데이터 연계 현황"]
    },
    "환경": {
        "agency": "산림청 / 환경부",
        "portal": "공공데이터포털 (data.go.kr)",
        "datasets": ["국립자연휴양림 및 100대 명산 숲길 정보", "탄소중립 배출량 및 에너지 통계", "국립공원 탐방객 통계"]
    }
}

def search_local_and_public_data(topic: str, search_dir: str = "upload") -> Dict[str, Any]:
    matched_local_files = []
    
    # Check local files first
    if os.path.exists(search_dir):
        for f in glob.glob(os.path.join(search_dir, "*.*")):
            ext = os.path.splitext(f)[1].lower()
            if ext in [".csv", ".xlsx", ".json"]:
                matched_local_files.append({
                    "path": f,
                    "file_name": os.path.basename(f),
                    "size_kb": round(os.path.getsize(f) / 1024, 1)
                })

    # Find thematic recommendation
    recommendations = []
    for key, info in PUBLIC_DATA_DIRECTORY.items():
        if key in topic:
            recommendations.append(info)

    if not recommendations:
        recommendations.append(PUBLIC_DATA_DIRECTORY["경제"])

    return {
        "query_topic": topic,
        "local_available_files": matched_local_files,
        "recommended_public_sources": recommendations,
        "data_grounding_ready": len(matched_local_files) > 0
    }

def main():
    parser = argparse.ArgumentParser(description="Find and catalog public datasets for the given topic.")
    parser.add_argument("-t", "--topic", required=True, help="Presentation topic keyword.")
    parser.add_argument("-d", "--search-dir", default="upload", help="Local directory to scan for CSVs.")
    parser.add_argument("-o", "--output", default=None, help="Save summary to JSON.")

    args = parser.parse_args()
    res = search_local_and_public_data(args.topic, search_dir=args.search_dir)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(res, f, ensure_ascii=False, indent=2)
        print(f"[+] Saved public data catalog to: {args.output}")
    else:
        print(json.dumps(res, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
