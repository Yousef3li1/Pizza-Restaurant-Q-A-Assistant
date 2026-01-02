@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Starting Pizza Restaurant Q&A Assistant...
echo.

REM Try to use system Python if venv has encoding issues
if exist "C:\Users\LEGION\AppData\Local\Programs\Python\Python313\python.exe" (
    "C:\Users\LEGION\AppData\Local\Programs\Python\Python313\python.exe" main.py
) else if exist "venv\Scripts\python.exe" (
    venv\Scripts\python.exe main.py
) else (
    python main.py
)

pause
