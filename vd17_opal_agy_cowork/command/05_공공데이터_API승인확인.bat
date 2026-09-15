@echo off
chcp 65001 > nul
title [vd17] 공공데이터포털 오픈API 승인 상태 점검
python "%~dp0..\src\check_api_status.py"
pause
