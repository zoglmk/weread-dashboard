@echo off
cd /d "%~dp0"

if not exist ".env" (
    echo 未找到 .env 文件，请先配置 API Key：
    echo   1. 复制 .env.example 为 .env
    echo   2. 用记事本编辑 .env，填入你的 WEREAD_API_KEY
    pause
    exit /b 1
)

echo 检查依赖...
pip install -q -r requirements.txt

echo 书房启动中... 请打开浏览器访问 http://localhost:8000
python server.py
pause
