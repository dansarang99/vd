@echo off
chcp 65001 > nul
echo ==============================================================================
echo       [BJ JANG] vd17_opal_agy_cowork 환경설정 및 의존성 설치
echo ==============================================================================
python -m pip install --quiet --upgrade pandas matplotlib requests
python "%~dp0..\src\verify.py"
pause
