# 依赖: pip install fastapi uvicorn httpx
import os
from pathlib import Path
import httpx
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI()

KEY = os.environ.get("WEREAD_API_KEY", "")
GATEWAY = "https://i.weread.qq.com/api/agent/gateway"


@app.get("/", response_class=HTMLResponse)
async def root():
    return Path(__file__).with_name("index.html").read_text("utf-8")


@app.post("/api/weread")
async def proxy(req: Request):
    if not KEY:
        raise HTTPException(500, "WEREAD_API_KEY 未配置，请先 export WEREAD_API_KEY=xxx")
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
    uvicorn.run(app, host="127.0.0.1", port=8000)
