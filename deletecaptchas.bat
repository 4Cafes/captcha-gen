@echo off
cd /d "%~dp0"

REM 
if exist captchas (
    del /f /q "captchas\*.*" 2>nul
    rmdir /s /q captchas
    mkdir captchas
)

echo All captchas in the folder have been deleted.
pause
