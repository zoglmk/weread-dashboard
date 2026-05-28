# 依赖: pip install fastapi uvicorn httpx
import os
from pathlib import Path
import httpx
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse


def _load_env():
    """从 .env 文件加载环境变量（不需要 python-dotenv）"""
    env_file = Path(__file__).with_name(".env")
    if not env_file.exists():
        return
    for line in env_file.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        os.environ.setdefault(key.strip(), val.strip().strip("\"'"))


_load_env()

app = FastAPI()

KEY = os.environ.get("WEREAD_API_KEY", "")
GATEWAY = "https://i.weread.qq.com/api/agent/gateway"


@app.get("/", response_class=HTMLResponse)
async def root():
    return Path(__file__).with_name("index.html").read_text("utf-8")


@app.post("/api/weread")
async def proxy(req: Request):
    if not KEY:
        raise HTTPException(
            500,
            "WEREAD_API_KEY 未配置。请在项目目录新建 .env 文件并写入：\nWEREAD_API_KEY=wrk-xxxxxxxx"
        )
    body = await req.json()
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.post(
            GATEWAY,
            json=body,
            headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
        )
    return JSONResponse(content=r.json(), status_code=r.status_code)


if __name__ == "__main__":
    import uvicorn
    print("书房启动中... 请打开浏览器访问 http://localhost:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
