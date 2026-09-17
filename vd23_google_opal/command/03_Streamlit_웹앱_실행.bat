@echo off
chcp 65001 > nul
title [vd23] 03. Google Opal 프롬프트 빌더 웹 대시보드
cd /d "%~dp0\..\src"
echo ======================================================================
echo  Google Opal 프롬프트 빌더 Streamlit 웹앱을 구동합니다...
echo  잠시 후 브라우저가 자동으로 열립니다.
echo ======================================================================
streamlit run app_streamlit.py
pause
