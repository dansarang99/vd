# [VD-05] vd05_hwpx_skill 한글(HWPX) & PSST 사업계획서 자동화 스킬 PowerShell 설정기
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host "   [VD-05] vd05_hwpx_skill 한글(HWPX) & PSST 사업계획서 환경 설정기" -ForegroundColor Cyan
Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host ""

Write-Host "[1/3] Python 실행 환경을 확인합니다..." -ForegroundColor Yellow
$py = Get-Command python -ErrorAction SilentlyContinue
if (-not $py) {
    Write-Host "[오류] Python이 설치되어 있지 않거나 PATH에 등록되지 않았습니다." -ForegroundColor Red
    Write-Host "https://www.python.org/downloads/ 에서 Python 3.10 이상을 설치해 주세요."
    exit 1
}
python --version
Write-Host "[성공] Python이 확인되었습니다." -ForegroundColor Green
Write-Host ""

Write-Host "[2/3] 필수 의존성 패키지(lxml 등)를 설치합니다..." -ForegroundColor Yellow
pip install -r "$PSScriptRoot\requirements.txt"
Write-Host ""

Write-Host "[3/3] HWPX 템플릿 및 산출물 무결성 검증..." -ForegroundColor Yellow
python "$PSScriptRoot\scripts\verify_hwpx.py" "$PSScriptRoot\templates\01_초기창업패키지_사업계획서_표준양식.hwpx"
python "$PSScriptRoot\scripts\verify_hwpx.py" "$PSScriptRoot\templates\02_공공기관_기본보고서_양식.hwpx"
python "$PSScriptRoot\scripts\verify_hwpx.py" "$PSScriptRoot\result\[001]_2026_초기창업패키지_사업계획서_완성본.hwpx"

Write-Host ""
Write-Host "==============================================================================" -ForegroundColor Green
Write-Host " 설치 및 무결성 검증 완료! vd05_hwpx_skill 준비 완료." -ForegroundColor Green
Write-Host "==============================================================================" -ForegroundColor Green
