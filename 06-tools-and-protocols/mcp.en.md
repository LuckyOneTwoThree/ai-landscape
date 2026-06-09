# Model Context Protocol (MCP)

> Last Updated: 2026-06-09
> Data Source: Automatically generated from `data/tools.yaml`

---

## 📡 MCP: The Standardized Protocol for AI Tools

MCP (Model Context Protocol) is an **AI tool integration standard** proposed by Anthropic, which has become the de facto industry standard.

| Your Situation | **Recommended Solution** | Reason |
| --------- | **---------** | ------ |
| **Developing an [MCP](https://modelcontextprotocol.io) Server** | **[FastMCP](https://github.com/PrefectHQ/fastmcp)** | 25.5K Stars, Pythonic approach |
| **Finding Ready-to-Use MCPs** | **[awesome-[[mcp](https://modelcontextprotocol.io)](https://modelcontextprotocol.io)-servers](https://github.com/appcypher/awesome-[[mcp](https://modelcontextprotocol.io)](https://modelcontextprotocol.io)-servers) / [Smithery](https://smithery.ai)** | 88.7K Stars / Largest [MCP](https://modelcontextprotocol.io) marketplace |
| **File System** | **[[[MCP](https://modelcontextprotocol.io)](https://modelcontextprotocol.io) Filesystem Server](https://github.com/modelcontextprotocol/servers)** | Official reference implementation |
| **Code Management** | **[[GitHub [[MCP](https://modelcontextprotocol.io)](https://modelcontextprotocol.io) Server](https://github.com/github/github-[[mcp](https://modelcontextprotocol.io)](https://modelcontextprotocol.io)-server)](https://github.com/github/github-[[mcp](https://modelcontextprotocol.io)](https://modelcontextprotocol.io)-server)** | 30.5K Stars, officially maintained |
| **Browser Automation** | **Playwright [[MCP](https://modelcontextprotocol.io)](https://modelcontextprotocol.io)** | 33.6K Stars, by Microsoft |
| **Documentation Fetching** | **[Context7 [[MCP](https://modelcontextprotocol.io)](https://modelcontextprotocol.io)](https://github.com/upstash/context7-[[mcp](https://modelcontextprotocol.io)](https://modelcontextprotocol.io))** | 57K Stars, real-time documentation |
| **SaaS Integration** | **Notion/Slack/Linear/[Sentry [[MCP](https://modelcontextprotocol.io)](https://modelcontextprotocol.io)](https://github.com/getsentry/sentry-[[mcp](https://modelcontextprotocol.io)](https://modelcontextprotocol.io))** | Official implementations by respective SaaS |
| **[MCP](https://modelcontextprotocol.io) Clients** | **[CodePilot](https://github.com/op7418/CodePilot) / [5ire](https://github.com/nanbingxyz/5ire)** | Desktop AI assistants |

> [!TIP]
> **MCP has become the de facto standard in 2026**
> OpenAI, Anthropic, Google, and Microsoft have all supported MCP. If you are developing AI tools, prioritize MCP compatibility.

---

## 📋 MCP Ecosystem Overview

<!-- 以下内容由脚本自动生成，请勿手动修改 -->
<!-- AUTOGEN_START -->

### 📡 Protocol

| Name | Description | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [MCP (Model Context Protocol)](https://modelcontextprotocol.io) | Model Context Protocol proposed by Anthropic, has become the absolute industry standard for AI tool integration | [mcp](https://modelcontextprotocol.io), tool-calling, open-source | Unified cross-platform tool integration standard<br>Thousands of active open-source [MCP](https://modelcontextprotocol.io) Servers<br>Mainstream IDEs (Cursor/Cline) and frameworks are supported<br>[OpenAI Agents SDK](https://platform.openai.com/docs/assistants/overview) added [MCP](https://modelcontextprotocol.io) support in 2025 |
| [A2A (Agent-to-Agent Protocol)](https://github.com/google/A2A) | Inter-Agent communication protocol proposed by Google, enabling interoperability of Agents across different frameworks | [mcp](https://modelcontextprotocol.io), agent, google | Agent interoperability protocol by Google<br>Communication between Agents of different frameworks<br>Complementary to [MCP](https://modelcontextprotocol.io) ([MCP](https://modelcontextprotocol.io) connects tools, [A2A](https://github.com/google/A2A) connects Agents) |

### 🔌 MCP Servers

#### 🔥 Trending Projects (50K+ Stars)

| Name | Description | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [n8n MCP Server](https://github.com/n8n-io/n8n) | [n8n](https://n8n.io) workflow automation [MCP](https://modelcontextprotocol.io) server, 191K Stars, oriented towards technical teams | automation, [mcp](https://modelcontextprotocol.io), open-source | 191K Stars<br>Workflow automation<br>Oriented towards technical teams |
| [MarkItDown MCP](https://github.com/microsoft/markitdown) | File to Markdown [MCP](https://modelcontextprotocol.io) server by Microsoft, supports PDF/Office/HTML | [mcp](https://modelcontextprotocol.io), microsoft, open-source | 147K Stars<br>By Microsoft<br>PDF/Office to Markdown |
| [awesome-mcp-servers (punkpeye)](https://github.com/punkpeye/awesome-mcp-servers) | Curated collection of [MCP](https://modelcontextprotocol.io) servers, the most comprehensive | [mcp](https://modelcontextprotocol.io), open-source | 88.7K Stars<br>Most comprehensive<br>Curated MCPs |
| [MCP Filesystem Server](https://github.com/modelcontextprotocol/servers) | Official [MCP](https://modelcontextprotocol.io) file operations server, provides secure sandboxed file read/write, search, and directory navigation | [mcp](https://modelcontextprotocol.io), open-source | 85K Stars (Official servers collection)<br>File read/write/search<br>Sandboxed permission control |
| [MCP Memory Server](https://github.com/modelcontextprotocol/servers) | Official [MCP](https://modelcontextprotocol.io) knowledge graph server, providing cross-session persistent memory for AI | [mcp](https://modelcontextprotocol.io), open-source | Knowledge graph persistent memory<br>Entity/relationship storage<br>Official reference implementation |
| [MCP Sequential Thinking](https://github.com/modelcontextprotocol/servers) | Structured multi-step reasoning [MCP](https://modelcontextprotocol.io) server, supports branching/revision/validation, making reasoning processes visible and auditable | [mcp](https://modelcontextprotocol.io), open-source | Structured reasoning<br>Branching/revision/validation<br>Auditable reasoning |
| [Brave Search MCP](https://github.com/modelcontextprotocol/servers) | [Brave Search MCP](https://github.com/modelcontextprotocol/servers) server, privacy-first real-time web/news search | [mcp](https://modelcontextprotocol.io), open-source | Real-time web search<br>News/local search<br>Privacy-first |
| [Docker MCP](https://github.com/modelcontextprotocol/servers) | Docker management [MCP](https://modelcontextprotocol.io) server, container/image/volume/network operations | [mcp](https://modelcontextprotocol.io), open-source | Container management<br>Image building<br>Docker Compose |
| [Postgres MCP](https://github.com/modelcontextprotocol/servers) | PostgreSQL direct connection [MCP](https://modelcontextprotocol.io) server, Schema exploration/SQL query/performance analysis | [mcp](https://modelcontextprotocol.io), open-source | PostgreSQL direct connection<br>Schema exploration<br>Read-only safe mode |
| [Scrapling MCP](https://github.com/D4Vinci/Scrapling) | Intelligent web scraping [MCP](https://modelcontextprotocol.io) server, adaptive anti-detection/smart selectors | [mcp](https://modelcontextprotocol.io), open-source | 62K Stars<br>Intelligent scraping<br>Anti-detection |
| [Context7 MCP](https://github.com/upstash/context7-mcp) | Real-time fetching of latest official library docs to inject into LLM context, eliminating API hallucinations | [mcp](https://modelcontextprotocol.io), open-source | 57K Stars<br>Real-time doc fetching<br>Eliminates API hallucinations |

#### ⭐ Active Projects (10K-50K Stars)

| Name | Description | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [Chrome DevTools MCP](https://github.com/anthropics/chrome-devtools-mcp) | [Chrome DevTools MCP](https://github.com/anthropics/chrome-devtools-mcp) server, real-time debugging/performance analysis/DOM operations | [mcp](https://modelcontextprotocol.io), open-source | 43K Stars<br>Real-time debugging<br>DOM operations |
| [Firecrawl MCP](https://github.com/mendableai/firecrawl-mcp-server) | Web scraping/search/structured extraction [MCP](https://modelcontextprotocol.io) server, supports persistent browser sessions | [mcp](https://modelcontextprotocol.io), open-source | 35K Stars<br>Web scraping<br>Structured extraction |
| [PostHog MCP](https://github.com/PostHog/posthog-mcp) | PostHog product analysis [MCP](https://modelcontextprotocol.io) server, event tracking/feature flags/user insights | data-analysis, [mcp](https://modelcontextprotocol.io), open-source | 34.9K Stars<br>Product analysis<br>Event tracking |
| [GitHub MCP Server](https://github.com/github/github-mcp-server) | Official [GitHub MCP server](https://github.com/github/github-mcp-server) | [mcp](https://modelcontextprotocol.io), coding-assistant, open-source | 30.5K Stars<br>Official GitHub<br>[MCP](https://modelcontextprotocol.io) Server |
| [FastMCP](https://github.com/PrefectHQ/fastmcp) | A fast Pythonic way to build [MCP](https://modelcontextprotocol.io) servers | [mcp](https://modelcontextprotocol.io), coding-assistant, langchain | 25.5K Stars<br>Pythonic way<br>Fast [MCP](https://modelcontextprotocol.io) building |
| [Headroom](https://github.com/chopratejas/headroom) | Compresses tool outputs/logs/RAG chunks to save Tokens | [mcp](https://modelcontextprotocol.io), cost-effective | 18.9K Stars<br>Tool output compression<br>Saves Tokens |
| [Chroma MCP](https://github.com/chroma-core/chroma-mcp) | ChromaDB vector database [MCP](https://modelcontextprotocol.io) server, semantic search/embedding storage | [mcp](https://modelcontextprotocol.io), open-source, rag | Vector database<br>Semantic search<br>Embedding storage |
| [Figma-Context-MCP](https://github.com/GLips/Figma-Context-MCP) | Figma [MCP](https://modelcontextprotocol.io) server, provides design context for AI coding agents | [mcp](https://modelcontextprotocol.io), content-creation | Figma [MCP](https://modelcontextprotocol.io) Server<br>Design context<br>15K Stars |
| [MCP GitHub Server](https://github.com/github/github-mcp-server) | Official [GitHub MCP server](https://github.com/github/github-mcp-server), supports Issue/PR/code search/Actions workflows | [mcp](https://modelcontextprotocol.io), microsoft | Officially maintained by GitHub<br>Issue/PR/Actions<br>Code search |
| [mcp-chrome](https://github.com/hangwin/mcp-chrome) | Chrome [MCP](https://modelcontextprotocol.io) server, browser extension format | [mcp](https://modelcontextprotocol.io), vscode-extension | Chrome [MCP](https://modelcontextprotocol.io) Server<br>Browser extension<br>12K Stars |

#### 🆕 Emerging Projects (<10K Stars)

| Name | Description | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [Supabase MCP](https://github.com/supabase-community/supabase-mcp) | Official [Supabase MCP](https://github.com/supabase-community/supabase-mcp) server, database read/write/Schema management/storage operations | [mcp](https://modelcontextprotocol.io), open-source | Official Supabase<br>Database read/write<br>Storage operations |
| [Vercel MCP](https://github.com/vercel/vercel-mcp-server) | Official [Vercel MCP](https://github.com/vercel/vercel-mcp-server) server, deployment management/project configuration/log viewing | [mcp](https://modelcontextprotocol.io), open-source | Official [Vercel](https://vercel.com)<br>Deployment management<br>Log viewing |
| [awesome-mcp-servers (appcypher)](https://github.com/appcypher/awesome-mcp-servers) | Curated list of [MCP](https://modelcontextprotocol.io) servers, most comprehensive | [mcp](https://modelcontextprotocol.io), open-source | 5.6K Stars<br>Most comprehensive<br>Curated MCPs |
| [Notion MCP](https://github.com/makenotion/notion-mcp-server) | Official [Notion MCP](https://github.com/makenotion/notion-mcp-server) server, supports reading/writing pages/databases/searching workspaces | [mcp](https://modelcontextprotocol.io), open-source | Official Notion<br>Page/database read/write<br>Workspace search |
| [Sentry MCP](https://github.com/getsentry/sentry-mcp) | Official [Sentry MCP](https://github.com/getsentry/sentry-mcp) server, search errors/stack traces/trend analysis, assisting production debugging | enterprise, [mcp](https://modelcontextprotocol.io), open-source | Official Sentry<br>Error tracking<br>Production debugging |
| [awesome-mcp-servers (wong2)](https://github.com/wong2/awesome-mcp-servers) | Curated list of [MCP](https://modelcontextprotocol.io) servers, community maintained | [mcp](https://modelcontextprotocol.io), open-source | 4.1K Stars<br>Community maintained<br>Curated MCPs |
| [Stripe MCP](https://github.com/stripe/stripe-mcp) | Official [Stripe MCP](https://github.com/stripe/stripe-mcp) server, payment/customer/subscription management | enterprise, [mcp](https://modelcontextprotocol.io), open-source | Official Stripe<br>Payment management<br>Subscription operations |
| [Cloudflare MCP](https://github.com/cloudflare/mcp-server-cloudflare) | Official [Cloudflare MCP](https://github.com/cloudflare/mcp-server-cloudflare) server, Workers/KV/R2/DNS management | [mcp](https://modelcontextprotocol.io), open-source | Official Cloudflare<br>Workers/KV/R2<br>Edge computing |
| [Home Assistant MCP](https://github.com/home-assistant/core) | Home Assistant smart home [MCP](https://modelcontextprotocol.io) server, device control/automation/scene triggering | automation, [mcp](https://modelcontextprotocol.io), open-source | Smart home<br>Device control<br>Automation scenes |
| [Slack MCP](https://github.com/zencoderio/mcp-server-slack) | Slack workspace [MCP](https://modelcontextprotocol.io) server, supports message read/write/channel management/file uploading | [mcp](https://modelcontextprotocol.io), open-source | Message read/write<br>Channel management<br>File uploading |
| [AWS Documentation MCP](https://github.com/awslabs/mcp) | Official [AWS documentation MCP](https://github.com/awslabs/mcp) server, search/read AWS service documentation and best practices | enterprise, [mcp](https://modelcontextprotocol.io), open-source | Official AWS<br>Documentation search<br>Best practices |
| [Linear MCP](https://github.com/linear-app/linear-mcp) | Official [Linear MCP](https://github.com/linear-app/linear-mcp) server, full operations on Issues/projects/roadmaps | [mcp](https://modelcontextprotocol.io), open-source | Official Linear<br>Issue management<br>Roadmap operations |
| [awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | Curated list of Claude Code plugins, by [Composio](https://composio.dev) | [mcp](https://modelcontextprotocol.io), open-source, openai-compatible | 1.7K Stars<br>By [Composio](https://composio.dev)<br>Claude plugins |

### 📱 MCP Clients

| Name | Description | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [CodePilot](https://github.com/op7418/CodePilot) | Multi-model AI Agent desktop client | [mcp](https://modelcontextprotocol.io), desktop, agentic | 6K Stars<br>Desktop client<br>Multi-model support |
| [5ire](https://github.com/nanbingxyz/5ire) | Cross-platform desktop AI assistant, [MCP](https://modelcontextprotocol.io) client | [mcp](https://modelcontextprotocol.io), desktop, chat | 5.2K Stars<br>Cross-platform desktop<br>[MCP](https://modelcontextprotocol.io) client |
| [Witsy](https://github.com/Kochava-Studios/witsy) | Desktop AI assistant/General [MCP](https://modelcontextprotocol.io) client | [mcp](https://modelcontextprotocol.io), desktop, openai-compatible | 2K Stars<br>Desktop AI assistant<br>General [MCP](https://modelcontextprotocol.io) |

### 🏪 MCP Marketplaces

| Name | Description | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [Microsoft MCP Catalog](https://github.com/microsoft/mcp) | Official Microsoft [MCP](https://modelcontextprotocol.io) server catalog | [mcp](https://modelcontextprotocol.io), microsoft | 3.3K Stars<br>Official Microsoft<br>[MCP](https://modelcontextprotocol.io) server catalog |
| [Smithery](https://smithery.ai) | [MCP](https://modelcontextprotocol.io) server marketplace, one-click install/discover/connect community [MCP](https://modelcontextprotocol.io) servers | [mcp](https://modelcontextprotocol.io), open-source | [MCP](https://modelcontextprotocol.io) server marketplace<br>One-click install<br>Community discovery |
| [Glama MCP Registry](https://glama.ai/mcp/servers) | Searchable [MCP](https://modelcontextprotocol.io) server directory and registry | [mcp](https://modelcontextprotocol.io), open-source | Server directory<br>Search & register<br>Community-driven |

<!-- AUTOGEN_END -->
<!-- 以上内容由脚本自动生成 -->

---

## 🏛️ MCP Ecosystem Architecture

```
┌─────────────────────────────────────────────────────┐
│                     MCP Clients                      │
│  (Claude, ChatGPT, Cursor, Windsurf, Hermes Agent)  │
└─────────────────────┬───────────────────────────────┘
                      │ MCP Protocol
┌─────────────────────┴───────────────────────────────┐
│                     MCP Servers                      │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐            │
│  │ Playwright│ │  GitHub  │ │  Slack   │  ...       │
│  │   MCP    │ │   MCP    │ │   MCP    │            │
│  └──────────┘ └──────────┘ └──────────┘            │
└─────────────────────────────────────────────────────┘
```

## 💡 MCP vs Function Calling

| Dimension | [MCP](https://modelcontextprotocol.io) | Function Calling |
| ------ | ----- | ------------------ |
| **Standardization** | ✅ Industry standard | ❌ Differs by vendor |
| **Reusability** | ✅ Cross-platform | ❌ Tied to vendor |
| **Ecosystem** | Rapidly growing | Mature |
| **Use Cases** | Tool integration | Simple calls |

> [!TIP]
> **Core Advantages of MCP**
> 1. **Standardization**: Develop once, use anywhere
> 2. **Reusability**: MCP servers can be used in any client that supports MCP
> 3. **Community-Driven**: awesome-mcp-servers already has hundreds of servers

## ⚡ Minimalist Practice: Configuring MCP in an IDE (Demystified)

Many people think "protocols" are profound and mysterious, but for developers, using MCP is extremely simple.

Take the currently popular **Cline** or **Cursor** as an example. You just need to open its `mcp_settings.json` (or go to the settings interface), add a few lines of configuration, and your AI will immediately gain the ability to read and write your local database:

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
*It's that simple! No network communication code to write. Your AI can now directly answer "Help me query the 10 most recent orders in the database."*

## 📚 MCP Resources

| Resource | Stars | Description | Link |
| ------ | ------- | ------ | ------ |
| [**awesome-mcp-servers (punkpeye)**](https://github.com/punkpeye/awesome-mcp-servers) | 88.7K | Curated [MCP](https://modelcontextprotocol.io) collection | github.com/punkpeye/awesome-[mcp](https://modelcontextprotocol.io)-servers |
| [**awesome-mcp-servers (appcypher)**](https://github.com/appcypher/awesome-mcp-servers) | 5.6K | Curated [MCP](https://modelcontextprotocol.io) list | github.com/appcypher/awesome-[mcp](https://modelcontextprotocol.io)-servers |
| [**awesome-claude-plugins**](https://github.com/ComposioHQ/awesome-claude-plugins) | 1.7K | Curated Claude plugins | github.com/ComposioHQ/[awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) |
| **[MCP](https://modelcontextprotocol.io) Official Documentation** | - | Protocol specifications | modelcontextprotocol.io |
| **[MCP](https://modelcontextprotocol.io) Registry** | 6.9K | Community server registry | github.com/modelcontextprotocol/registry |

---

> **Update Frequency**: Updated quarterly
> **Automation**: Run `python scripts/build_docs.py` to re-render tables from YAML.
