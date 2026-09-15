@echo off
chcp 65001 > nul
echo ==============================================================================
echo       [(AX)창업기술 이한규 대표] vd17_opal_agy_cowork 환경설정 및 의존성 설치
echo ==============================================================================
python -m pip install --quiet --upgrade pandas matplotlib requests
python "%~dp0..\src\verify.py"
pause
