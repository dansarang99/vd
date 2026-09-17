@echo off
chcp 65001 > nul
title [vd23] 02. Google Opal 프롬프트 생성기 CLI
cd /d "%~dp0\..\src"
python cli.py
pause
