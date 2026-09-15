@echo off
chcp 65001 > nul
cls
echo ==============================================================================
echo   [VD15] Slide Style Cloner v2.0 환경 설정기 (Windows One-Click Setup)
echo ==============================================================================
echo.
echo [1/2] Python 실행 환경을 확인합니다...
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [오류] Python이 설치되어 있지 않거나 환경변수 PATH에 등록되지 않았습니다.
    pause
    exit /b 1
)
python --version
echo [성공] Python이 확인되었습니다.
echo.

echo [2/2] 필수 라이브러리(python-pptx, PyMuPDF, Pillow 등)를 설치합니다...
pip install -r "%~dp0requirements.txt"
if %ERRORLEVEL% neq 0 (
    echo [경고] 라이브러리 설치 중 일부 경고가 발생했습니다.
) else (
    echo [성공] 라이브러리 설치가 완료되었습니다.
)
echo.
echo ==============================================================================
echo  설치가 완료되었습니다! 이제 AI 에이전트에서 "이 슬라이드 스타일 복제해줘"라고 지시하세요.
echo ==============================================================================
pause
