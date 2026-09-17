@echo off
chcp 65001 > nul
title [vd23] 04. Antigravity 전역 스킬 등록
echo ======================================================================
echo  Antigravity 및 Gemini CLI 전역 스킬 폴더에 vd23 스킬을 등록합니다.
echo ======================================================================
set TARGET_DIR=%USERPROFILE%\.gemini\config\skills\vd23-google-opal-builder
if not exist "%TARGET_DIR%" mkdir "%TARGET_DIR%"
copy /Y "%~dp0\..\SKILL.md" "%TARGET_DIR%\SKILL.md"
echo.
echo ======================================================================
echo  [V] 전역 스킬 등록이 완료되었습니다!
echo  설치 경로: %TARGET_DIR%\SKILL.md
echo  이제 언제든지 Antigravity 대화창에서 본 스킬을 호출할 수 있습니다.
echo ======================================================================
pause
