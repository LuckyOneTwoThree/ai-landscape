# Workflow Automation

> Last Updated: 2026-06-08
> Data Source: Automatically generated from `data/frameworks.yaml`

---

## ⚙️ Workflow Automation: What Do You Really Need?

| Your Situation | **Recommended Platform** | Reason |
| --------- | **---------** | ------ |
| **Open Source / Private Deployment** | **[n8n](https://n8n.io)** | 65K Stars, AI-native nodes |
| **AI Agent + MCP** | **[Activepieces](https://github.com/activepieces/activepieces)** | 400+ MCP servers |
| **Simple Automation / Non-Technical** | **[Zapier](https://zapier.com)** | 7000+ apps, easiest to use |
| **Complex Workflows / Visual** | **[Make](https://make.com)** | 1500+ apps, powerful orchestration |
| **Developers / Scripting** | **[Windmill](https://windmill.dev)** | Multi-language scripting, code-first |

> [!TIP]
> **n8n is the best choice in 2026**
> n8n has deeply integrated AI-native nodes, supporting Agents, RAG, and MCP, while maintaining 400+ app integrations. If you are not sure what to choose, start with n8n.

---

## 📋 Workflow Automation Platforms Overview

<!-- AUTOGEN_START -->

| Name | Description | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [n8n](https://n8n.io) | Open-source workflow automation platform, deeply integrated with AI-native nodes, 400+ integrations | workflow, automation, self-hosted, agent | 400+ integration nodes<br>AI-native nodes and seamless API docking<br>Running on 1.4 million machines<br>70K+ Stars |
| [Activepieces](https://github.com/activepieces/activepieces) | Open-source AI Agent & MCP & workflow automation platform, 400+ MCP servers | workflow, mcp, agent, open-source | 22.6K Stars<br>400+ MCP servers<br>Open-source [Zapier](https://zapier.com) alternative |
| [Windmill](https://windmill.dev) | Developer-oriented automation platform, supports multi-language scripting | workflow, automation, coding-assistant, self-hosted | Supports Python/TS/Go/Bash scripts<br>Alternative to Airflow/[n8n](https://n8n.io)<br>Developer-oriented |
| [Make (formerly Integromat)](https://www.make.com) | Visual workflow automation platform, 1500+ app integrations | workflow, automation, enterprise | Visual scenario builder<br>1500+ app integrations<br>AI module integration<br>Enterprise-grade stability |
| [Zapier](https://zapier.com) | Automation platform with the largest user base, 7000+ apps, natural language Zaps creation | workflow, automation, low-code | 7000+ app integrations<br>Natural language Zaps creation<br>AI by [Zapier](https://zapier.com)<br>Largest user base |

<!-- AUTOGEN_END -->

---

## 🏛️ Two Major Camps

### 🔵 Open-Source Type: Data In Your Own Hands

| Platform | Stars | Core Advantage | Who It's For |
| ------ | ------- | --------- | -------- |
| [**n8n**](https://n8n.io) | 65K | AI-native nodes, 400+ integrations | General automation |
| [**Activepieces**](https://github.com/activepieces/activepieces) | 22.6K | 400+ MCP servers, open-source [Zapier](https://zapier.com) alternative | AI Agent automation |
| [**Windmill**](https://windmill.dev) | 12K | Developer-oriented, multi-language scripting | Developers |

### 🟢 Commercial SaaS Type: Out-of-the-Box

| Platform | Core Advantage | Who It's For |
| ------ | --------- | -------- |
| [**Zapier**](https://zapier.com) | 7000+ apps, natural language creation | Non-technical users |
| [**Make**](https://make.com) | 1500+ apps, powerful orchestration | Complex workflows |

## 💡 Platform Comparison

| Dimension | [n8n](https://n8n.io) | [Activepieces](https://github.com/activepieces/activepieces) | [Zapier](https://zapier.com) | [Make](https://make.com) |
| ------ | ----- | -------------- | -------- | ------ |
| **Open Source** | ✅ | ✅ | ❌ | ❌ |
| **AI Integration** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **MCP Support** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ❌ | ❌ |
| **App Integrations** | 400+ | 400+ | 7000+ | 1500+ |
| **Learning Curve** | Medium | Low | Low | Medium |
| **Pricing** | Free self-hosted | Free self-hosted | From $20/month | From $9/month |

## 🔄 Typical Workflows

**AI Agent Automation** (n8n + MCP):
```
Trigger (Webhook/Cron)
  ↓
AI Agent Node (LLM + Tool Calling)
  ↓
MCP Server (GitHub/Slack/Database)
  ↓
Result Processing (Formatting/Filtering)
  ↓
Output (Webhook/Email/Database)
```

**Data Processing Automation** (n8n + RAG):
```
Data Source (API/Database/File)
  ↓
Document Parsing (PDF/HTML)
  ↓
Embedding + Vector Store
  ↓
RAG Retrieval + LLM Generation
  ↓
Result Output (API/Database)
```

---

> **Update Frequency**: Updated quarterly
> **Automation**: Run `python scripts/build_docs.py` to re-render tables from YAML.
