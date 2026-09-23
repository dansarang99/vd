# -*- coding: utf-8 -*-
"""
==============================================================================
[2026 Antigravity] 온라인 쇼핑 자동 수집 & AI 분석 마스터 오케스트레이터
==============================================================================
키워드 하베스팅 ➔ 시장성 분석 ➔ 엑셀 보고서 편찬 ➔ 인터랙티브 대시보드 팝업
모든 과정을 하나의 파이프라인으로 통합 지휘합니다.
"""

import os
import sys
import json
import time

sys.stdout.reconfigure(encoding='utf-8')

# 내부 모듈 임포트
from keyword_harvester import NaverKeywordHarvester, CATEGORIES
from market_analyzer import MarketAnalyzer
from excel_generator import ExcelReportGenerator
from dashboard_generator import DashboardGenerator

def run_pipeline(target_categories=None, top_n=10, auto_open_browser=True):
    start_time = time.time()
    print("=" * 78)
    print(" [2026 Antigravity] 온라인 쇼핑 황금키워드 자동 수집 및 분석 가동")
    print("=" * 78)
    
    os.makedirs("result", exist_ok=True)
    
    if target_categories is None:
        target_categories = [
            "디지털/가전", "스포츠/레저", "패션의류", 
            "생활/건강", "식품", "가구/인테리어"
        ]
        
    harvester = NaverKeywordHarvester()
    analyzer = MarketAnalyzer()
    excel_gen = ExcelReportGenerator()
    dash_gen = DashboardGenerator()
    
    # -----------------------------------------------------------------
    # Step 1: 실시간 네이버 데이터랩 키워드 수집
    # -----------------------------------------------------------------
    print(f"\n[*] [Step 1/4] 네이버 쇼핑 실시간 베스트 키워드 수집 중...")
    print(f"    - 대상 카테고리: {', '.join(target_categories)}")
    
    raw_keywords = []
    category_map = {}
    
    for cat in target_categories:
        print(f"    > [{cat}] 실시간 랭킹 수집 중...")
        # 전체 랭킹
        ranks = harvester.fetch_rankings(category_name=cat, count=top_n)
        raw_keywords.extend(ranks)
        category_map[cat] = [r["keyword"] for r in ranks]
        
        # 30대 남성/여성 타깃 추가 수집
        female_ranks = harvester.fetch_rankings(category_name=cat, age="30대", gender="여성", count=5)
        male_ranks = harvester.fetch_rankings(category_name=cat, age="30대", gender="남성", count=5)
        raw_keywords.extend(female_ranks)
        raw_keywords.extend(male_ranks)
        
    print(f"[+] 총 {len(raw_keywords)}개 타깃 키워드 데이터 수집 완료!")
    
    # -----------------------------------------------------------------
    # Step 2: 시장성 및 경쟁 강도 다차원 분석
    # -----------------------------------------------------------------
    print(f"\n[*] [Step 2/4] 통계적 EDA 및 시장성(황금스코어, 가격대, 경쟁도) 분석 중...")
    analyzed_keywords = []
    detailed_items_all = []
    
    # 중복 키워드 방지 캐시
    cache = {}
    
    for kw_entry in raw_keywords:
        kw = kw_entry["keyword"]
        if kw not in cache:
            eda_res = analyzer.analyze_keyword(kw)
            cache[kw] = eda_res
            for it in eda_res.get("items", [])[:5]:
                it_copy = dict(it)
                it_copy["keyword"] = kw
                detailed_items_all.append(it_copy)
                
        eda_res = cache[kw]
        merged = dict(kw_entry)
        merged.update({
            "total_products": eda_res["total_products"],
            "avg_price": eda_res["avg_price"],
            "median_price": eda_res["median_price"],
            "recommended_price": eda_res["recommended_price"],
            "comp_grade": eda_res["comp_grade"],
            "golden_score": eda_res["golden_score"]
        })
        analyzed_keywords.append(merged)
        
    # 황금스코어 기준 내림차순 정렬
    analyzed_keywords.sort(key=lambda x: x["golden_score"], reverse=True)
    
    # -----------------------------------------------------------------
    # Step 3: 고급 엑셀 보고서 생성
    # -----------------------------------------------------------------
    excel_path = "result/naver_golden_keywords_2026.xlsx"
    print(f"\n[*] [Step 3/4] 다중 시트 서식 엑셀 보고서 컴파일 중 ({excel_path})...")
    excel_gen.generate(analyzed_keywords, category_map, detailed_items_all, excel_path)
    
    # -----------------------------------------------------------------
    # Step 4: 인터랙티브 반응형 HTML5 대시보드 생성
    # -----------------------------------------------------------------
    dash_path = "result/dashboard.html"
    print(f"\n[*] [Step 4/4] Chart.js 인터랙티브 반응형 웹 대시보드 컴파일 중 ({dash_path})...")
    dash_gen.generate(analyzed_keywords, dash_path)
    
    elapsed = round(time.time() - start_time, 2)
    print("\n" + "=" * 78)
    print(f" [✔] 파이프라인 완료! 총 소요시간: {elapsed}초")
    print(f"     1) 엑셀 보고서  : {os.path.abspath(excel_path)}")
    print(f"     2) 웹 대시보드  : {os.path.abspath(dash_path)}")
    print("=" * 78)
    
    if auto_open_browser:
        print("[*] 기본 웹 브라우저에서 대시보드를 자동으로 엽니다...")
        os.system(f'start "" "{os.path.abspath(dash_path)}"')

if __name__ == "__main__":
    run_pipeline()
