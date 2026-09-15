"""
main.py
완주로컬푸드 Opal & Antigravity Cowork 마스터 자동화 엔드투엔드 파이프라인
"""

import os
import sys
import io
import argparse
import datetime
import pandas as pd

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass


from opal_connector import fetch_or_generate_sales
from eda_engine import run_eda, generate_executive_markdown
from visualizer import generate_all_charts
from dashboard_generator import generate_html_dashboard

def execute_pipeline(api_key=None, output_dir=None, target_hour=None):
    """
    완주로컬푸드 통합 자동화 파이프라인 1회 전체 실행
    """
    if output_dir is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        output_dir = os.path.join(base_dir, "result")
    os.makedirs(output_dir, exist_ok=True)

    print("\n=======================================================")
    print("[vd17] 완주로컬푸드 Opal & Antigravity 파이프라인 가동")
    print(f"[실행 시각] {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=======================================================")

    # 1. Google Opal & API 데이터 수집/생성
    print("\n[단계 1/4] 데이터 수집 및 Opal Blueprint 생성 중...")
    df, csv_path, blueprint_path = fetch_or_generate_sales(
        api_key=api_key, output_dir=output_dir, target_hour=target_hour
    )

    # 2. 자동 탐색적 데이터 분석(EDA) 수행
    print("\n[단계 2/4] 실시간 탐색적 데이터 분석(EDA) 수행 중...")
    eda_results = run_eda(df)
    s = eda_results['summary']
    print(f"  - 당일 총매출: {s['total_revenue']:,}원")
    print(f"  - 당일 총판매량: {s['total_quantity']:,}개")
    print(f"  - 1위 매장: {s['top_store_name']} ({s['top_store_share']}%)")
    print(f"  - 1위 품목: {s['top_item_name']}")

    # C-Level 마크다운 보고서 저장
    md_path = os.path.join(output_dir, "executive_summary.md")
    generate_executive_markdown(eda_results, md_path)

    # 3. 4대 고해상도 경영진 차트 렌더링
    print("\n[단계 3/4] 300 DPI 고해상도 경영진 비즈니스 차트 렌더링 중...")
    charts = generate_all_charts(eda_results, output_dir)

    # 4. 실시간 글래스모피즘 웹 대시보드 렌더링
    print("\n[단계 4/4] 반응형 글래스모피즘 실시간 웹 대시보드 빌드 중...")
    dashboard_path = os.path.join(output_dir, "latest_report.html")
    generate_html_dashboard(eda_results, charts, dashboard_path)

    print("\n=======================================================")
    print("[파이프라인 완료] 모든 산출물이 성공적으로 생성되었습니다.")
    print(f"1. 실시간 데이터 CSV: {csv_path}")
    print(f"2. Google Opal Blueprint: {blueprint_path}")
    print(f"3. 4대 분석 차트: {os.path.join(output_dir, 'charts')}")
    print(f"4. C-Level 브리핑 요약: {md_path}")
    print(f"5. 실시간 웹 대시보드: {dashboard_path}")
    print("=======================================================\n")

    return {
        "status": "SUCCESS",
        "csv": csv_path,
        "blueprint": blueprint_path,
        "markdown": md_path,
        "dashboard": dashboard_path,
        "eda": eda_results
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wanju Local Food Opal & Antigravity Pipeline")
    parser.add_argument("--api-key", type=str, default=None, help="Public Data Portal Service Key")
    parser.add_argument("--output-dir", type=str, default=None, help="Output directory path")
    parser.add_argument("--hour", type=int, default=None, help="Target hour for simulation (9-20)")
    args = parser.parse_args()

    execute_pipeline(api_key=args.api_key, output_dir=args.output_dir, target_hour=args.hour)
