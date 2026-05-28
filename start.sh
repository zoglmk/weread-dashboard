#!/bin/bash
cd "$(dirname "$0")"

if [ ! -f ".env" ]; then
  echo "未找到 .env 文件，请先配置 API Key："
  echo "  cp .env.example .env"
  echo "  然后编辑 .env 填入你的 WEREAD_API_KEY"
  exit 1
fi

echo "书房启动中..."
python3 server.py
