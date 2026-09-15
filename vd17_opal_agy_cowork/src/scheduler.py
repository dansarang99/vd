"""
scheduler.py
완주로컬푸드 실시간 데이터 자동 갱신 및 1시간 주기 업그레이드 스케줄러 데몬
"""

import os
import sys
import io
import time
import shutil
import argparse
import datetime

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass


from main import execute_pipeline

def run_scheduler(interval_seconds=3600, max_cycles=None, turbo=False):
    """1시간 주기 자동화 스케줄러 루프"""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(base_dir, "result")
    history_dir = os.path.join(output_dir, "history")
    os.makedirs(history_dir, exist_ok=True)

    if turbo:
        interval_seconds = 10
        print("\n[TURBO MODE] 시연 및 강의 검증용 10초 주기 터보 모드로 동작합니다.")

    print("\n=======================================================")
    print("[vd17 스케줄러 데몬] 1시간 주기 자동 업그레이드 엔진 가동")
    print(f"갱신 주기: {interval_seconds}초 ({interval_seconds/60:.1f}분)")
    print("=======================================================\n")

    cycle_count = 0
    simulated_hour = 9

    try:
        while True:
            cycle_count += 1
            now = datetime.datetime.now()
            print(f"\n>>> [사이클 #{cycle_count}] 실행 시작: {now.strftime('%Y-%m-%d %H:%M:%S')} (가상 시각: {simulated_hour:02d}:00)")

            # 1. 파이프라인 1회 실행
            result = execute_pipeline(output_dir=output_dir, target_hour=simulated_hour)

            # 2. 히스토리 아카이빙 (버전별 보존)
            timestamp_str = now.strftime("%Y%m%d_%H%M%S")
            hist_csv = os.path.join(history_dir, f"sales_{timestamp_str}_H{simulated_hour:02d}.csv")
            hist_html = os.path.join(history_dir, f"report_{timestamp_str}_H{simulated_hour:02d}.html")

            if os.path.exists(result['csv']):
                shutil.copy2(result['csv'], hist_csv)
            if os.path.exists(result['dashboard']):
                shutil.copy2(result['dashboard'], hist_html)

            print(f"[아카이브 보존] {hist_html}")
            print(f"[성공] 사이클 #{cycle_count} 완료. 다음 주기까지 {interval_seconds}초 동안 대기합니다.")

            # 다음 시간대로 시뮬레이션 전진
            simulated_hour += 1
            if simulated_hour > 20:
                simulated_hour = 9

            if max_cycles and cycle_count >= max_cycles:
                print(f"\n[종료] 지정된 최대 사이클 수({max_cycles}회)에 도달하여 스케줄러를 안전하게 종료합니다.")
                break

            # 대기
            time.sleep(interval_seconds)

    except KeyboardInterrupt:
        print("\n[중단] 사용자에 의해 스케줄러가 정상 중단되었습니다.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wanju Local Food Hourly Scheduler Daemon")
    parser.add_argument("--interval", type=int, default=3600, help="Interval in seconds (default: 3600)")
    parser.add_argument("--max-cycles", type=int, default=None, help="Stop after N cycles (optional)")
    parser.add_argument("--turbo", action="store_true", help="Run in fast 10-second demo mode")
    args = parser.parse_args()

    run_scheduler(interval_seconds=args.interval, max_cycles=args.max_cycles, turbo=args.turbo)
