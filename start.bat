@echo off
title CAPTCHA Generator Setup

echo Installing required Python libraries...
pip install captcha
pip install time

echo.
echo Do you want to start generator?
set /p response="Y/N : "

if /i "%response%"=="Y" (
    echo.
    echo Launching generator!
    timeout /t 1 >nul
    python gen.py
) else (
    echo Exiting program. Goodbye!
    exit
)