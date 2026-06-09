# AI 应用构建器

> 最后更新：2026-06-08
> 数据来源：`data/frameworks.yaml` 自动生成

---

## 🏗️ 低代码 AI 构建：你到底需要什么？

| 你的情况 | 推荐平台 | 理由 |
|---------|---------|------|
| **快速搭建 AI Bot** | [Dify](https://dify.ai) / [Coze](https://www.coze.com) | 开箱即用，拖拽构建 |
| **知识库问答** | [FastGPT](https://fastgpt.in) / [DocsGPT](https://github.com/arc53/DocsGPT) | 国内友好，私有部署 |
| **可视化工作流** | [Flowise](https://flowiseai.com) / [Langflow](https://langflow.org) | 拖拽式，130+ 节点 |
| **全栈应用生成** | [Bolt.new](https://bolt.new) / [Lovable](https://lovable.dev) | 一句话生成完整应用 |
| **前端 UI 生成** | [v0 by [Vercel](https://vercel.com)](https://v0.dev) | 专注 [Next.js](https://nextjs.org) 组件 |
| **本地开源替代** | [Dyad](https://github.com/dyad-sh/dyad) | v0/[Lovable](https://lovable.dev) 的开源替代 |

> [!TIP]
> **开源 vs 商业的选择**
> - **快速验证 / 个人项目**：Dify（开源，144K Stars）或 Coze（免费额度大）
> - **企业级 / 私有部署**：Dify 自部署 或 FastGPT
> - **全栈应用生成**：Lovable（商业，体验最好）或 Dyad（开源，本地运行）

---

## 📋 AI 应用构建器总览

<!-- AUTOGEN_START -->

#### 🔥 热门项目 (50K+ Stars)

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [Dify](https://dify.ai) | 开源 LLM 应用开发与编排平台，支持 Agentic Workflow，开源领导者 | low-code, rag, workflow, mcp | 强大的可视化工作流编排<br>内置高级 RAG 引擎<br>MCP 全面支持与海量插件<br>132K+ Stars，开源领导者 |
| [Langflow](https://langflow.org) | 适用于 RAG 和多智能体 AI 应用的低代码构建器 | low-code, rag, agent | 可视化流程构建<br>与模型/API/数据库无关<br>Python 原生<br>148K+ Stars |

#### ⭐ 活跃项目 (10K-50K Stars)

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [Flowise](https://flowiseai.com) | 拖拽式 LLM 应用可视化构建平台，130+ 内置节点 | low-code | 零门槛拖拽构建 AI 应用<br>130+ 内置功能节点<br>100+ 支持模型<br>52K+ Stars |
| [FastGPT](https://fastgpt.in) | 开源知识库 AI 应用构建平台，国内用户友好 | low-code, rag, chinese | 知识库管理强<br>国内用户友好<br>自部署支持 |
| [Dyad](https://github.com/dyad-sh/dyad) | 本地开源 AI 应用构建器，v0/Lovable 的开源替代 | self-hosted, open-source, coding-assistant | 20.5K Stars<br>本地开源<br>v0/Lovable 替代 |
| [DocsGPT](https://github.com/arc53/DocsGPT) | 私有 AI 平台，支持 Agent、助手和企业搜索 | self-hosted, enterprise, search | 17.9K Stars<br>私有部署<br>企业级搜索 |
| [Botpress](https://botpress.com) | 对话机器人专精平台，多渠道部署 | chat, low-code, pipeline | 对话机器人专精<br>多渠道部署<br>集成知识库 |

#### 🆕 新兴项目 (<10K Stars)

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [Open Agent Builder](https://github.com/firecrawl/open-agent-builder) | Firecrawl 出品的可视化 AI Agent 工作流构建器 | content-creation, workflow, search | 2.3K Stars<br>Firecrawl 出品<br>可视化构建 |
| [Coze (扣子)](https://www.coze.com) | 字节跳动低代码 AI Bot 开发平台，强调插件生态和快速发布 | low-code, chat, mcp, chinese | 多人多 Agent 协作与项目空间<br>插件生态丰富 (600+)<br>快速发布到飞书/微信等社交平台<br>Coze Studio 开发环境 |
| [Bolt.new](https://bolt.new) | StackBlitz 浏览器端全栈 AI 应用构建器，WebContainer 驱动 | low-code, all-in-one | WebContainer 浏览器内模拟 Linux<br>支持多 JS 框架<br>代码完全可见可编辑<br>从提示词到可运行应用闭环 |
| [Lovable](https://lovable.dev) | 2026 年最火 AI 无代码应用构建平台，ARR 突破 4 亿美元 | low-code | 自然语言到完整应用<br>前端 UI 质量极高<br>ARR 突破 4 亿美元<br>估值 120 亿美元 |
| [v0 by Vercel](https://v0.dev) | Vercel 前端 AI 生成工具，专注产出干净的 Next.js 应用 | low-code, content-creation, coding-assistant | 专注前端生成<br>产出干净的 Next.js 应用<br>实时渲染预览<br>与 Vercel 部署生态深度集成 |

<!-- AUTOGEN_END -->

---

## 🏛️ 三大阵营

### 🔵 开源自部署型：数据在自己手里

| 平台 | Stars | 核心优势 | 适合谁 |
|------|-------|---------|--------|
| **Dify** | 144K | 开源领导者，Agentic Workflow | 企业级，私有部署 |
| **Langflow** | 55K | RAG + 多 Agent 低代码构建 | 开发者，RAG 场景 |
| **Flowise** | 38K | 拖拽式，130+ 内置节点 | 快速原型，可视化 |
| **FastGPT** | 28K | 国内用户友好，知识库专精 | 国内团队 |
| **Dyad** | 20.5K | 本地开源，v0/Lovable 替代 | 本地开发 |
| **DocsGPT** | 17.9K | 私有 AI 平台，企业搜索 | 企业级搜索 |

### 🟢 商业 SaaS 型：开箱即用

| 平台 | 核心优势 | 适合谁 |
|------|---------|--------|
| **Coze (扣子)** | 字节出品，插件生态丰富 | 国内用户，快速发布 |
| **Bolt.new** | 浏览器端全栈构建 | 快速原型 |
| **Lovable** | ARR 4 亿美元，最火无代码平台 | 非技术人员 |
| **v0 by Vercel** | 专注 Next.js 组件 | 前端开发者 |

### 🟡 专业对话型：Bot 构建专精

| 平台 | 核心优势 | 适合谁 |
|------|---------|--------|
| **Botpress** | 多渠道部署，对话机器人专精 | 客服，对话场景 |
| **Open Agent Builder** | Firecrawl 出品，可视化构建 | Agent 工作流 |

## 💡 平台对比

| 维度 | Dify | Flowise | Langflow | Coze |
|------|------|---------|----------|------|
| **开源** | ✅ | ✅ | ✅ | ❌ |
| **学习曲线** | 低 | 低 | 中 | 低 |
| **RAG 支持** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Agent 支持** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **插件生态** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **中文支持** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
