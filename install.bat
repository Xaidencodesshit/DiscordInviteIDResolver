@echo off

python -c "import requests" 2>nul
IF %ERRORLEVEL% NEQ 0 (
    REM Install requests library
    pip install requests
)

start main.py
