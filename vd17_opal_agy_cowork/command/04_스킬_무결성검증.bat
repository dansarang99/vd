@echo off
chcp 65001 > nul
title [vd17] Opal & Antigravity 스킬 무결성 검증기
echo =======================================================
echo  [vd17] 스킬 무결성 및 자동화 엔진 검증 테스트
echo =======================================================
echo.
echo [1/3] 단일 파이프라인 무결성 테스트...
python src\main.py
if errorlevel 1 (
    echo [FAIL] src\main.py 실행 실패!
    pause
    exit /b 1
)

echo.
echo [2/3] 터보 스케줄러 2사이클 검증...
python src\scheduler.py --turbo --max-cycles 2
if errorlevel 1 (
    echo [FAIL] src\scheduler.py 실행 실패!
    pause
    exit /b 1
)

echo.
echo [3/3] 산출물 존재 확인...
if not exist "result\latest_sales.csv" ( echo [FAIL] CSV 누락 & pause & exit /b 1 )
if not exist "result\latest_report.html" ( echo [FAIL] 대시보드 누락 & pause & exit /b 1 )
if not exist "result\executive_summary.md" ( echo [FAIL] C-Level 요약 누락 & pause & exit /b 1 )
if not exist "result\opal_app_blueprint.json" ( echo [FAIL] Blueprint 누락 & pause & exit /b 1 )
if not exist "result\charts\01_top_items_revenue.png" ( echo [FAIL] 차트 1 누락 & pause & exit /b 1 )

echo.
echo =======================================================
echo  [ALL PASS] vd17 모든 모듈 및 산출물 무결성 검증 통과!
echo =======================================================
pause
