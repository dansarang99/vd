@echo off
chcp 65001 > nul
title [vd17] Opal & Antigravity Cowork 환경설정 및 의존성 설치
echo =======================================================
echo  [vd17] 비제이짱 완주로컬푸드 Opal 자동화 환경설정
echo =======================================================
echo.
echo [1/3] Python 환경 확인 중...
python --version
if errorlevel 1 (
    echo [ERROR] Python이 설치되어 있지 않거나 PATH에 등록되지 않았습니다.
    pause
    exit /b 1
)

echo.
echo [2/3] 필수 라이브러리(pandas, matplotlib, requests) 확인 및 설치...
python -m pip install --quiet --upgrade pandas matplotlib requests

echo.
echo [3/3] 파이프라인 무결성 1회 테스트...
python src\main.py

echo.
echo =======================================================
echo  [완료] vd17 환경 설정 및 초기화가 성공적으로 완료되었습니다!
echo  결과 확인: result\latest_report.html 을 브라우저로 여세요.
echo =======================================================
pause
