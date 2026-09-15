@echo off
chcp 65001 > nul
title [vd17] 완주로컬푸드 실시간 파이프라인 1회 즉시 실행
echo =======================================================
echo  [vd17] 완주로컬푸드 실시간 파이프라인 1회 실행
echo =======================================================
echo.
python src\main.py
echo.
echo [결과 열기] 실시간 대시보드(latest_report.html)를 기본 브라우저로 엽니다...
start "" "result\latest_report.html"
echo.
pause
