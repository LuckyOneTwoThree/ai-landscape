# Function Calling and Tool Integration

> Last Updated: 2026-06-08
> Data Source: Automatically generated from `data/tools.yaml`

---

## 🔧 Function Calling: Letting LLMs Use Tools

The core of function calling: **enabling LLMs to call external APIs and tools**.

| Your Situation | Recommended Solution | Reason |
| --------- | --------- | ------ |
| **Native Function Calling** | OpenAI / Anthropic | LLM built-in tool calling |
| **Tool Integration Platform** | [Composio](https://composio.dev) / [ACI.dev](https://github.com/aipotheosis-labs/aci) | 200+ / 600+ app connectors |
| **MCP Protocol** | MCP Servers | Standardized tool protocol |
| **Agent Protocol** | [ACP](https://github.com/i-am-bee/acp) / A2A | Inter-Agent communication |

> [!TIP]
> **Composio is the best choice for tool integration**
> 15K Stars, 200+ app connectors, single-line code integration. Supports mainstream tools like GitHub, Slack, and Jira.

---

## 📋 Function Calling Tools Overview

<!-- 以下内容由脚本自动生成，请勿手动修改 -->
<!-- AUTOGEN_START -->

### 📡 Protocol

| Name | Description | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [ACP](https://github.com/i-am-bee/acp) | Open protocol for AI Agent communication | mcp, agent, chat | 1K Stars<br>Agent communication<br>Open protocol |
| [python-a2a](https://github.com/themanojdesai/python-a2a) | Python implementation of the A2A protocol | mcp, a2a, coding-assistant | 1K Stars<br>A2A protocol<br>Python implementation |

### 🔧 Built-in Tools

| Name | Description | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [OpenAI Built-in Tools](https://openai.com) | OpenAI's official built-in toolset (Web Search, File Search, Computer Use) | openai-compatible, tool-calling, search, agent | Web Search<br>File Search<br>Computer Use<br>Native integration without extra configuration |
| [Anthropic Tool Use](https://anthropic.com) | Claude's native tool calling capabilities, supports MCP | anthropic, tool-calling, mcp | Claude native tool calling<br>Deep MCP integration<br>Computer Use capability |

### 🔗 Tool Integration

| Name | Description | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [Composio](https://composio.dev) | Tool integration platform specifically for AI Agents, providing massive tested connectors | mcp, function-calling | Hundreds of certified high-frequency app integrations<br>Out-of-the-box, highly compatible with different Agent frameworks<br>Unified authentication management |
| [Klavis AI](https://github.com/Klavis-AI/klavis) | MCP integration platform, enabling AI Agents to use various tools | mcp, openai-compatible | 5.7K Stars<br>MCP integration<br>AI Agent tools |
| [ACI.dev](https://github.com/aipotheosis-labs/aci) | Open-source tool calling platform, connecting 600+ apps | tool-calling, mcp, openai-compatible | 4.8K Stars<br>600+ apps<br>Tool calling platform |
| [Toolhouse](https://toolhouse.ai) | AI Agent tool cloud service, one-click installation of toolsets | mcp, function-calling, cloud-only | One-click tool installation<br>SDK integration<br>100+ tools |

<!-- AUTOGEN_END -->
<!-- 以上内容由脚本自动生成 -->

---

## 💡 Tool Comparison

| Dimension | OpenAI Built-in | [Anthropic Tool Use](https://anthropic.com) | [Composio](https://composio.dev) | [ACI.dev](https://github.com/aipotheosis-labs/aci) |
| ------ | ----------------- | ------------------- | ---------- | --------- |
| **Tool Count** | 3 | Custom | 200+ | 600+ |
| **MCP Support** | ❌ | ✅ | ❌ | ❌ |
| **Learning Curve** | Low | Low | Low | Low |
| **Use Cases** | Search/File/Computer | Custom tools | App integration | App integration |

---

> **Update Frequency**: Updated quarterly
> **Automation**: Run `python scripts/build_docs.py` to re-render tables from YAML.
