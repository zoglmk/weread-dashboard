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

前往微信读书 Skill 开放平台申请：

**https://weread.qq.com/r/weread-skills**

登录后可获取 API Key（格式：`wrk-xxxxxxxx`），同时也可以在这里查看和管理其他 Skill 技能。

> API Key 绑定你的微信读书账号，请勿泄露，不要提交到 Git。

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

需要 Python 3.8+。

### 3. 配置 API Key（一次性）

```bash
cp .env.example .env
# 编辑 .env，将 wrk-xxxxxxxx 替换为你的真实 API Key
```

## 启动

**Mac / Linux**
```bash
bash start.sh
```

**Windows**

双击 `start.bat`，或在终端执行：
```cmd
start.bat
```

启动后打开浏览器访问 http://localhost:8000

> API Key 只需在 `.env` 里配置一次，之后每次直接运行启动脚本即可。`.env` 文件已被 `.gitignore` 排除，不会被提交到 Git。

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
