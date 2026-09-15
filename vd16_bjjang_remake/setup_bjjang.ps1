# ==============================================================================
#       [BJ JANG] vd16_bjjang_remake 프레젠테이션 자동화 스킬 환경 설정기 (PowerShell)
# ==============================================================================
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Clear-Host

Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host "      [BJ JANG] vd16_bjjang_remake 프레젠테이션 자동화 스킬 환경 설정기" -ForegroundColor Cyan
Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host ""

# 1. Python 확인
Write-Host "[1/3] Python 실행 환경을 확인합니다..." -ForegroundColor Yellow
$py = Get-Command python -ErrorAction SilentlyContinue
if (-not $py) {
    Write-Host "[오류] Python이 설치되어 있지 않거나 환경변수 PATH에 등록되지 않았습니다." -ForegroundColor Red
    Write-Host "https://www.python.org/downloads/ 에서 Python 3.10 이상을 설치해 주세요."
    exit 1
}
python --version
Write-Host "[성공] Python이 정상적으로 감지되었습니다." -ForegroundColor Green
Write-Host ""

# 2. 필수 패키지 설치
Write-Host "[2/3] 필수 의존성 패키지(python-pptx, edge-tts 등)를 설치합니다..." -ForegroundColor Yellow
pip install -r "$PSScriptRoot\requirements.txt"
if ($LASTEXITCODE -eq 0) {
    Write-Host "[성공] 필수 라이브러리 설치가 완료되었습니다." -ForegroundColor Green
} else {
    Write-Host "[경고] 일부 라이브러리 설치 중 경고가 발생했습니다." -ForegroundColor DarkYellow
}
Write-Host ""

# 3. Preflight 실행
Write-Host "[3/3] 사전 환경 점검(Preflight)을 실행합니다..." -ForegroundColor Yellow
python "$PSScriptRoot\scripts\preflight.py"
Write-Host ""
Write-Host "==============================================================================" -ForegroundColor Cyan
Write-Host "  설치가 완료되었습니다! 에이전트에서 비제이짱 템플릿으로 슬라이드를 생성해 보세요." -ForegroundColor Cyan
Write-Host "==============================================================================" -ForegroundColor Cyan
