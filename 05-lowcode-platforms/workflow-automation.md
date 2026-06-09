# 工作流自动化

> 最后更新：2026-06-08
> 数据来源：`data/frameworks.yaml` 自动生成

---

## ⚙️ 工作流自动化：你到底需要什么？

| 你的情况 | 推荐平台 | 理由 |
|---------|---------|------|
| **开源 / 私有部署** | [n8n](https://n8n.io) | 65K Stars，AI 原生节点 |
| **AI Agent + MCP** | [Activepieces](https://github.com/activepieces/activepieces) | 400+ MCP 服务器 |
| **简单自动化 / 非技术** | [Zapier](https://zapier.com) | 7000+ 应用，最易用 |
| **复杂工作流 / 可视化** | [Make](https://make.com) | 1500+ 应用，强大编排 |
| **开发者 / 脚本化** | [Windmill](https://windmill.dev) | 多语言脚本，代码优先 |

> [!TIP]
> **n8n 是 2026 年的最佳选择**
> n8n 已经深度整合 AI 原生节点，支持 Agent、RAG、MCP，同时保持了 400+ 应用集成。如果你不确定选什么，先用 n8n。

---

## 📋 工作流自动化平台总览

<!-- AUTOGEN_START -->

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [n8n](https://n8n.io) | 开源工作流自动化平台，深度整合 AI 原生节点，400+ 集成 | workflow, automation, self-hosted, agent | 400+ 集成节点<br>AI 原生节点与无缝 API 对接<br>运行在 140 万台机器上<br>70K+ Stars |
| [Activepieces](https://github.com/activepieces/activepieces) | 开源 AI Agent & MCP & 工作流自动化平台，400+ MCP 服务器 | workflow, mcp, agent, open-source | 22.6K Stars<br>400+ MCP 服务器<br>开源替代 Zapier |
| [Windmill](https://windmill.dev) | 开发者导向的自动化平台，支持多语言脚本 | workflow, automation, coding-assistant, self-hosted | 支持 Python/TS/Go/Bash 脚本<br>可替代 Airflow/n8n<br>开发者导向 |
| [Make (前 Integromat)](https://www.make.com) | 可视化工作流自动化平台，1500+ 应用集成 | workflow, automation, enterprise | 可视化场景构建器<br>1500+ 应用集成<br>AI 模块集成<br>企业级稳定性 |
| [Zapier](https://zapier.com) | 最大用户基数自动化平台，7000+ 应用，自然语言创建 Zaps | workflow, automation, low-code | 7000+ 应用集成<br>自然语言创建 Zaps<br>AI by Zapier<br>最大用户基数 |

<!-- AUTOGEN_END -->

---

## 🏛️ 两大阵营

### 🔵 开源型：数据在自己手里

| 平台 | Stars | 核心优势 | 适合谁 |
|------|-------|---------|--------|
| **n8n** | 65K | AI 原生节点，400+ 集成 | 通用自动化 |
| **Activepieces** | 22.6K | 400+ MCP 服务器，开源替代 Zapier | AI Agent 自动化 |
| **Windmill** | 12K | 开发者导向，多语言脚本 | 开发者 |

### 🟢 商业 SaaS 型：开箱即用

| 平台 | 核心优势 | 适合谁 |
|------|---------|--------|
| **Zapier** | 7000+ 应用，自然语言创建 | 非技术人员 |
| **Make** | 1500+ 应用，强大编排 | 复杂工作流 |

## 💡 平台对比

| 维度 | n8n | Activepieces | Zapier | Make |
|------|-----|--------------|--------|------|
| **开源** | ✅ | ✅ | ❌ | ❌ |
| **AI 集成** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **MCP 支持** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ❌ | ❌ |
| **应用集成** | 400+ | 400+ | 7000+ | 1500+ |
| **学习曲线** | 中 | 低 | 低 | 中 |
| **价格** | 免费自部署 | 免费自部署 | $20/月起 | $9/月起 |

## 🔄 典型工作流

**AI Agent 自动化**（n8n + MCP）：
```
触发器 (Webhook/Cron)
  ↓
AI Agent 节点 (LLM + 工具调用)
  ↓
MCP 服务器 (GitHub/Slack/数据库)
  ↓
结果处理 (格式化/过滤)
  ↓
输出 (Webhook/邮件/数据库)
```

**数据处理自动化**（n8n + RAG）：
```
数据源 (API/数据库/文件)
  ↓
文档解析 (PDF/HTML)
  ↓
Embedding + 向量存储
  ↓
RAG 检索 + LLM 生成
  ↓
结果输出 (API/数据库)
```

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
