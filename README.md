# 书房 · WeRead Dashboard

个人微信读书数据可视化网站，本地运行，无需部署。

![书房预览](https://img.shields.io/badge/Python-3.8+-blue) ![License](https://img.shields.io/badge/license-MIT-green)

## 功能

- **总览**：年度阅读时长、天数、偏好分类等统计
- **书架**：封面网格，按分类筛选，查看书籍详情（简介、评分、字数）
- **笔记 · 列表**：有笔记的书按划线数排序，点击查看全部划线与想法
- **笔记 · 碎片**：所有划线和想法混合成「散落纸张」卡片墙
  - 卡片 3D 浮动动画，有大有小随机倾斜
  - 点击卡片翻转查看书籍详情
  - 聚光灯：随机弹出一张卡片到屏幕中央展示
  - 排队气泡：卡片随机冒出小气泡说悄悄话
- **搜索**：在书城搜索书籍
- 深色 / 亮色主题切换
- 数据本地缓存（24 小时），手动刷新按钮

## 前置条件

### 1. 获取微信读书 API Key

本项目使用微信读书 Agent API Gateway，需要申请 API Key（格式：`wrk-xxxxxxxx`）。

> API Key 绑定你的微信读书账号，请勿泄露。

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

需要 Python 3.8+。

## 使用

**Mac / Linux**
```bash
export WEREAD_API_KEY=wrk-xxxxxxxx
python3 server.py
```

**Windows（CMD）**
```cmd
set WEREAD_API_KEY=wrk-xxxxxxxx
python server.py
```

**Windows（PowerShell）**
```powershell
$env:WEREAD_API_KEY="wrk-xxxxxxxx"
python server.py
```

启动后打开浏览器访问 http://localhost:8000

> 每次打开新终端都需要重新设置环境变量。如需持久化，Mac 写入 `~/.zshrc`，Windows 在系统设置里配置用户环境变量。

## 技术栈

- **后端**：Python + FastAPI（单文件代理，保护 API Key 不暴露到前端）
- **前端**：Alpine.js + Tailwind CSS（CDN，无需构建）
- **字体**：Fraunces + Instrument Sans（Google Fonts）

## 项目结构

```
wx_read/
├── server.py      # FastAPI 后端，代理微信读书 API 请求
├── index.html     # 前端单文件 SPA
├── requirements.txt
└── README.md
```

## 安全说明

API Key 通过环境变量传入，仅在后端使用，不会出现在前端代码或浏览器请求中。

## License

MIT
