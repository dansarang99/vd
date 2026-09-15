@echo off
chcp 65001 > nul
cls
echo ==============================================================================
echo       [BJ JANG] vd16_bjjang_remake 프레젠테이션 자동화 스킬 환경 설정기
echo ==============================================================================
echo.
echo [1/3] Python 실행 환경을 확인합니다...
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [오류] Python이 설치되어 있지 않거나 환경변수 PATH에 등록되지 않았습니다.
    echo https://www.python.org/downloads/ 에서 Python 3.10 이상을 설치할 때
    echo 반드시 'Add python.exe to PATH' 체크박스를 선택해 주세요!
    pause
    exit /b 1
)

python --version
echo [성공] Python이 확인되었습니다.
echo.

echo [2/3] 필수 의존성 패키지(python-pptx, edge-tts 등)를 설치합니다...
pip install -r "%~dp0requirements.txt"
if %ERRORLEVEL% neq 0 (
    echo [경고] pip 설치 중 일부 오류가 발생했을 수 있습니다. 로그를 확인해 주세요.
) else (
    echo [성공] 라이브러리 설치가 완료되었습니다.
)
echo.

echo [3/3] 비제이짱 스킬 무결성 및 사전 검사(preflight)를 실행합니다...
python "%~dp0scripts\preflight.py"
echo.
echo ==============================================================================
echo  설치가 완료되었습니다! 이제 AI 에이전트(Claude Code, Codex, Antigravity 등)에서
echo  "비제이짱 강의 템플릿으로 AI 자동화 실무 PPT 만들어줘" 처럼 자연어로 지시해 보세요!
echo ==============================================================================
pause
