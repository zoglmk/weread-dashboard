@echo off
cd /d "%~dp0"

if not exist ".env" (
    echo 未找到 .env 文件，请先配置 API Key：
    echo   1. 复制 .env.example 为 .env
    echo   2. 编辑 .env，填入你的 WEREAD_API_KEY
    pause
    exit /b 1
)

echo 书房启动中...
python server.py
pause
