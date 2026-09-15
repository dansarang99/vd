"""
verify.py
[vd17] Opal & Antigravity Cowork 스킬 사전 무결성 검증 스크립트 (Preflight & Integrity Checker)
"""

import os
import sys
import io
import time

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

from main import execute_pipeline
from scheduler import run_scheduler

def run_verification():
    print("==============================================================================")
    print("      [BJ JANG] vd17_opal_agy_cowork 스킬 사전 무결성 검증 (Preflight)")
    print("==============================================================================")

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    result_dir = os.path.join(base_dir, "result")

    # 1. 단일 파이프라인 1회 테스트
    print("\n[1/3] 단일 파이프라인 무결성 테스트 실행...")
    res = execute_pipeline(output_dir=result_dir)
    if res['status'] != 'SUCCESS':
        print("[FAIL] execute_pipeline 실패!")
        return False
    print("  -> 단일 파이프라인 정상 통과!")

    # 2. 터보 스케줄러 2사이클 검증
    print("\n[2/3] 터보 스케줄러 2사이클 검증 실행...")
    run_scheduler(interval_seconds=2, max_cycles=2, turbo=True)
    print("  -> 스케줄러 자동 갱신 및 아카이빙 정상 통과!")

    # 3. 필수 산출물 파일 검사
    print("\n[3/3] 필수 산출물 무결성 전수 검사...")
    required_files = [
        os.path.join(result_dir, "latest_sales.csv"),
        os.path.join(result_dir, "latest_report.html"),
        os.path.join(result_dir, "executive_summary.md"),
        os.path.join(result_dir, "opal_app_blueprint.json"),
        os.path.join(result_dir, "charts", "01_top_items_revenue.png"),
        os.path.join(result_dir, "charts", "02_store_share_donut.png"),
        os.path.join(result_dir, "charts", "03_hourly_sales_trend.png"),
        os.path.join(result_dir, "charts", "04_price_volume_matrix.png")
    ]

    for rf in required_files:
        if not os.path.exists(rf):
            print(f"[FAIL] 필수 산출물 누락: {rf}")
            return False
        print(f"  [OK] {os.path.basename(rf)} ({os.path.getsize(rf):,} bytes)")

    print("\n==============================================================================")
    print("  [ALL PASS] vd17_opal_agy_cowork 모든 모듈 및 산출물 무결성 검증 완료!")
    print("==============================================================================\n")
    return True

if __name__ == '__main__':
    success = run_verification()
    sys.exit(0 if success else 1)
