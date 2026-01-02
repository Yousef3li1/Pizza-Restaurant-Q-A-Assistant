# PowerShell script to run the Pizza Restaurant Q&A Assistant
$ErrorActionPreference = "Stop"

Write-Host "Starting Pizza Restaurant Q&A Assistant..." -ForegroundColor Green
Write-Host ""

# Set encoding
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$env:PYTHONIOENCODING = "utf-8"

# Try different Python paths
$pythonPaths = @(
    "C:\Users\LEGION\AppData\Local\Programs\Python\Python313\python.exe",
    "venv\Scripts\python.exe",
    "python.exe",
    "python"
)

$pythonFound = $false
foreach ($pythonPath in $pythonPaths) {
    if (Get-Command $pythonPath -ErrorAction SilentlyContinue) {
        Write-Host "Using Python: $pythonPath" -ForegroundColor Yellow
        & $pythonPath main.py
        $pythonFound = $true
        break
    }
}

if (-not $pythonFound) {
    Write-Host "Error: Could not find Python executable" -ForegroundColor Red
    Write-Host "Please ensure Python is installed and in your PATH" -ForegroundColor Red
    exit 1
}

