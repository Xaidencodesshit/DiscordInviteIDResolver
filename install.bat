@echo off

python -c "import requests" 2>nul
IF %ERRORLEVEL% NEQ 0 (
    pip install requests
)

python main.py
