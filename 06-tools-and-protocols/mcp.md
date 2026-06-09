# MCP 模型上下文协议

> 最后更新：2026-06-09
> 数据来源：`data/tools.yaml` 自动生成

---

## 📡 MCP：AI 工具的标准化协议

MCP (Model Context Protocol) 是 Anthropic 提出的**AI 工具集成标准**，已成为行业事实标准。

| 你的情况 | 推荐方案 | 理由 |
|---------|---------|------|
| **开发 [MCP](https://modelcontextprotocol.io) 服务器** | [FastMCP](https://github.com/PrefectHQ/fastmcp) | 25.5K Stars，Pythonic 方式 |
| **找现成 [MCP](https://modelcontextprotocol.io)** | [awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers) / [Smithery](https://smithery.ai) | 88.7K Stars / 最大 [MCP](https://modelcontextprotocol.io) 市场 |
| **文件系统** | [MCP Filesystem Server](https://github.com/modelcontextprotocol/servers) | 官方参考实现 |
| **代码管理** | [GitHub MCP Server](https://github.com/github/github-mcp-server) | 30.5K Stars，官方出品 |
| **浏览器自动化** | Playwright [MCP](https://modelcontextprotocol.io) | 33.6K Stars，微软出品 |
| **文档拉取** | [Context7 MCP](https://github.com/upstash/context7-mcp) | 57K Stars，实时文档 |
| **SaaS 集成** | Notion/Slack/Linear/[Sentry MCP](https://github.com/getsentry/sentry-mcp) | 各 SaaS 官方出品 |
| **[MCP](https://modelcontextprotocol.io) 客户端** | [CodePilot](https://github.com/op7418/CodePilot) / [5ire](https://github.com/nanbingxyz/5ire) | 桌面 AI 助手 |

> [!TIP]
> **MCP 已成为 2026 年的事实标准**
> OpenAI、Anthropic、Google、微软都已支持 MCP。如果你在开发 AI 工具，优先考虑 MCP 兼容。

---

## 📋 MCP 生态总览

<!-- 以下内容由脚本自动生成，请勿手动修改 -->
<!-- AUTOGEN_START -->

### 📡 协议

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [MCP (Model Context Protocol)](https://modelcontextprotocol.io) | Anthropic 提出的模型上下文协议，已成为 AI 工具集成的行业绝对标准 | mcp, tool-calling, open-source | 统一的跨平台工具集成标准<br>几千个活跃的开源 MCP Servers<br>主流 IDE (Cursor/Cline) 和框架均已支持<br>2025 年 OpenAI Agents SDK 新增 MCP 支持 |
| [A2A (Agent-to-Agent Protocol)](https://github.com/google/A2A) | Google 提出的 Agent 间通信协议，实现不同框架 Agent 的互操作 | mcp, agent, google | Google 提出的 Agent 互操作协议<br>不同框架 Agent 间通信<br>与 MCP 互补 (MCP 连接工具，A2A 连接 Agent) |

### 🔌 MCP 服务器

#### 🔥 热门项目 (50K+ Stars)

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [n8n MCP Server](https://github.com/n8n-io/n8n) | n8n 工作流自动化 MCP 服务器，191K Stars，面向技术团队 | automation, mcp, open-source | 191K Stars<br>工作流自动化<br>面向技术团队 |
| [MarkItDown MCP](https://github.com/microsoft/markitdown) | 微软出品的文件转 Markdown MCP 服务器，支持 PDF/Office/HTML | mcp, microsoft, open-source | 147K Stars<br>微软出品<br>PDF/Office→Markdown |
| [awesome-mcp-servers (punkpeye)](https://github.com/punkpeye/awesome-mcp-servers) | MCP 服务器精选集合，最全面 | mcp, open-source | 88.7K Stars<br>最全面<br>MCP 精选 |
| [MCP Filesystem Server](https://github.com/modelcontextprotocol/servers) | MCP 官方文件操作服务器，提供安全的沙盒化文件读写、搜索和目录导航 | mcp, open-source | 85K Stars（官方服务器合集）<br>文件读写/搜索<br>沙盒权限控制 |
| [MCP Memory Server](https://github.com/modelcontextprotocol/servers) | MCP 官方知识图谱服务器，为 AI 提供跨会话持久记忆 | mcp, open-source | 知识图谱持久记忆<br>实体/关系存储<br>官方参考实现 |
| [MCP Sequential Thinking](https://github.com/modelcontextprotocol/servers) | 结构化多步推理 MCP 服务器，支持分支/修正/验证，让推理过程可见可审计 | mcp, open-source | 结构化推理<br>分支/修正/验证<br>推理可审计 |
| [Brave Search MCP](https://github.com/modelcontextprotocol/servers) | Brave Search MCP 服务器，隐私优先的实时网页/新闻搜索 | mcp, open-source | 实时网页搜索<br>新闻/本地搜索<br>隐私优先 |
| [Docker MCP](https://github.com/modelcontextprotocol/servers) | Docker 管理 MCP 服务器，容器/镜像/卷/网络操作 | mcp, open-source | 容器管理<br>镜像构建<br>Docker Compose |
| [Postgres MCP](https://github.com/modelcontextprotocol/servers) | PostgreSQL 直连 MCP 服务器，Schema 探索/SQL 查询/性能分析 | mcp, open-source | PostgreSQL 直连<br>Schema 探索<br>只读安全模式 |
| [Scrapling MCP](https://github.com/D4Vinci/Scrapling) | 智能网页抓取 MCP 服务器，自适应反检测/智能选择器 | mcp, open-source | 62K Stars<br>智能抓取<br>反检测 |
| [Context7 MCP](https://github.com/upstash/context7-mcp) | 实时拉取最新官方库文档注入 LLM 上下文，消除 API 幻觉 | mcp, open-source | 57K Stars<br>实时文档拉取<br>消除 API 幻觉 |

#### ⭐ 活跃项目 (10K-50K Stars)

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [Chrome DevTools MCP](https://github.com/anthropics/chrome-devtools-mcp) | Chrome 开发者工具 MCP 服务器，实时调试/性能分析/DOM 操作 | mcp, open-source | 43K Stars<br>实时调试<br>DOM 操作 |
| [Firecrawl MCP](https://github.com/mendableai/firecrawl-mcp-server) | 网页抓取/搜索/结构化提取 MCP 服务器，支持持久化浏览器会话 | mcp, open-source | 35K Stars<br>网页抓取<br>结构化提取 |
| [PostHog MCP](https://github.com/PostHog/posthog-mcp) | PostHog 产品分析 MCP 服务器，事件追踪/功能标志/用户洞察 | data-analysis, mcp, open-source | 34.9K Stars<br>产品分析<br>事件追踪 |
| [GitHub MCP Server](https://github.com/github/github-mcp-server) | GitHub 官方 MCP 服务器 | mcp, coding-assistant, open-source | 30.5K Stars<br>GitHub 官方<br>MCP 服务器 |
| [FastMCP](https://github.com/PrefectHQ/fastmcp) | 构建 MCP 服务器的快速 Pythonic 方式 | mcp, coding-assistant, langchain | 25.5K Stars<br>Pythonic 方式<br>快速构建 MCP |
| [Headroom](https://github.com/chopratejas/headroom) | 压缩工具输出/日志/RAG 块，节省 Token | mcp, cost-effective | 18.9K Stars<br>压缩工具输出<br>节省 Token |
| [Chroma MCP](https://github.com/chroma-core/chroma-mcp) | ChromaDB 向量数据库 MCP 服务器，语义搜索/嵌入存储 | mcp, open-source, rag | 向量数据库<br>语义搜索<br>嵌入存储 |
| [Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) | Figma MCP 服务器，为 AI 编码代理提供设计上下文 | mcp, content-creation | Figma MCP 服务器<br>设计上下文<br>15K Stars |
| [MCP GitHub Server](https://github.com/github/github-mcp-server) | GitHub 官方 MCP 服务器，支持 Issue/PR/代码搜索/Actions 工作流 | mcp, microsoft | GitHub 官方维护<br>Issue/PR/Actions<br>代码搜索 |
| [mcp-chrome](https://github.com/hangwin/mcp-chrome) | Chrome MCP 服务器，浏览器扩展形式 | mcp, vscode-extension | Chrome MCP 服务器<br>浏览器扩展<br>12K Stars |

#### 🆕 新兴项目 (<10K Stars)

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [Supabase MCP](https://github.com/supabase-community/supabase-mcp) | Supabase 官方 MCP 服务器，数据库读写/Schema 管理/存储操作 | mcp, open-source | Supabase 官方<br>数据库读写<br>存储操作 |
| [Vercel MCP](https://github.com/vercel/vercel-mcp-server) | Vercel 官方 MCP 服务器，部署管理/项目配置/日志查看 | mcp, open-source | Vercel 官方<br>部署管理<br>日志查看 |
| [awesome-mcp-servers (appcypher)](https://github.com/appcypher/awesome-mcp-servers) | MCP 服务器精选列表，最全面 | mcp, open-source | 5.6K Stars<br>最全面<br>MCP 精选 |
| [Notion MCP](https://github.com/makenotion/notion-mcp-server) | Notion 官方 MCP 服务器，支持读写页面/数据库/搜索工作区 | mcp, open-source | Notion 官方<br>页面/数据库读写<br>工作区搜索 |
| [Sentry MCP](https://github.com/getsentry/sentry-mcp) | Sentry 官方 MCP 服务器，搜索错误/堆栈追踪/趋势分析，辅助生产调试 | enterprise, mcp, open-source | Sentry 官方<br>错误追踪<br>生产调试 |
| [awesome-mcp-servers (wong2)](https://github.com/wong2/awesome-mcp-servers) | MCP 服务器精选列表，社区维护 | mcp, open-source | 4.1K Stars<br>社区维护<br>MCP 精选 |
| [Stripe MCP](https://github.com/stripe/stripe-mcp) | Stripe 官方 MCP 服务器，支付/客户/订阅管理 | enterprise, mcp, open-source | Stripe 官方<br>支付管理<br>订阅操作 |
| [Cloudflare MCP](https://github.com/cloudflare/mcp-server-cloudflare) | Cloudflare 官方 MCP 服务器，Workers/KV/R2/DNS 管理 | mcp, open-source | Cloudflare 官方<br>Workers/KV/R2<br>边缘计算 |
| [Home Assistant MCP](https://github.com/home-assistant/core) | Home Assistant 智能家居 MCP 服务器，设备控制/自动化/场景触发 | automation, mcp, open-source | 智能家居<br>设备控制<br>自动化场景 |
| [Slack MCP](https://github.com/zencoderio/mcp-server-slack) | Slack 工作区 MCP 服务器，支持消息读写/频道管理/文件上传 | mcp, open-source | 消息读写<br>频道管理<br>文件上传 |
| [AWS Documentation MCP](https://github.com/awslabs/mcp) | AWS 官方文档 MCP 服务器，搜索/阅读 AWS 服务文档和最佳实践 | enterprise, mcp, open-source | AWS 官方<br>文档搜索<br>最佳实践 |
| [Linear MCP](https://github.com/linear-app/linear-mcp) | Linear 官方 MCP 服务器，Issue/项目/路线图全操作 | mcp, open-source | Linear 官方<br>Issue 管理<br>路线图操作 |
| [awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | Claude Code 插件精选列表，Composio 出品 | mcp, open-source, openai-compatible | 1.7K Stars<br>Composio 出品<br>Claude 插件 |

### 📱 MCP 客户端

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [CodePilot](https://github.com/op7418/CodePilot) | 多模型 AI Agent 桌面客户端 | mcp, desktop, agentic | 6K Stars<br>桌面客户端<br>多模型支持 |
| [5ire](https://github.com/nanbingxyz/5ire) | 跨平台桌面 AI 助手，MCP 客户端 | mcp, desktop, chat | 5.2K Stars<br>跨平台桌面<br>MCP 客户端 |
| [Witsy](https://github.com/Kochava-Studios/witsy) | 桌面 AI 助手/通用 MCP 客户端 | mcp, desktop, openai-compatible | 2K Stars<br>桌面 AI 助手<br>通用 MCP |

### 🏪 MCP 市场

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [Microsoft MCP Catalog](https://github.com/microsoft/mcp) | 微软官方 MCP 服务器目录 | mcp, microsoft | 3.3K Stars<br>微软官方<br>MCP 服务器目录 |
| [Smithery](https://smithery.ai) | MCP 服务器市场，一键安装/发现/连接社区 MCP 服务器 | mcp, open-source | MCP 服务器市场<br>一键安装<br>社区发现 |
| [Glama MCP Registry](https://glama.ai/mcp/servers) | 可搜索的 MCP 服务器目录与注册中心 | mcp, open-source | 服务器目录<br>搜索注册<br>社区驱动 |

<!-- AUTOGEN_END -->
<!-- 以上内容由脚本自动生成 -->

---

## 🏛️ MCP 生态架构

```
┌─────────────────────────────────────────────────────┐
│                    MCP 客户端                        │
│  (Claude, ChatGPT, Cursor, Windsurf, Hermes Agent)  │
└─────────────────────┬───────────────────────────────┘
                      │ MCP 协议
┌─────────────────────┴───────────────────────────────┐
│                    MCP 服务器                        │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐            │
│  │ Playwright│ │  GitHub  │ │  Slack   │  ...       │
│  │   MCP    │ │   MCP    │ │   MCP    │            │
│  └──────────┘ └──────────┘ └──────────┘            │
└─────────────────────────────────────────────────────┘
```

## 💡 MCP vs Function Calling

| 维度 | MCP | Function Calling |
|------|-----|------------------|
| **标准化** | ✅ 行业标准 | ❌ 各厂商不同 |
| **可复用** | ✅ 跨平台 | ❌ 绑定厂商 |
| **生态** | 快速增长 | 成熟 |
| **适用场景** | 工具集成 | 简单调用 |

> [!TIP]
> **MCP 的核心优势**
> 1. **标准化**：一次开发，到处使用
> 2. **可复用**：MCP 服务器可以在任何支持 MCP 的客户端使用
> 3. **社区驱动**：awesome-mcp-servers 已有数百个服务器

## ⚡ 极简实战：在 IDE 中配置 MCP (祛魅)

很多人觉得“协议”高深莫测，其实对开发者来说，使用 MCP 极其简单。

以目前最火的 **Cline** 或 **Cursor** 为例，你只需要打开它的 `mcp_settings.json`（或在设置界面），添加几行配置，你的 AI 就能立刻拥有读写本地数据库的能力：

```json
{
  "mcpServers": {
    "sqlite-server": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-sqlite",
        "/absolute/path/to/your/database.sqlite"
      ]
    }
  }
}
```
*就这么简单！无需写任何网络通信代码，你的 AI 现在可以直接回答“帮我查一下数据库里最近的 10 个订单”。*

## 📚 MCP 资源

| 资源 | Stars | 说明 | 链接 |
|------|-------|------|------|
| **awesome-mcp-servers (punkpeye)** | 88.7K | MCP 精选集合 | github.com/punkpeye/awesome-mcp-servers |
| **awesome-mcp-servers (appcypher)** | 5.6K | MCP 精选列表 | github.com/appcypher/awesome-mcp-servers |
| **awesome-claude-plugins** | 1.7K | Claude 插件精选 | github.com/ComposioHQ/awesome-claude-plugins |
| **MCP 官方文档** | - | 协议规范 | modelcontextprotocol.io |
| **MCP Registry** | 6.9K | 社区服务器注册表 | github.com/modelcontextprotocol/registry |

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
