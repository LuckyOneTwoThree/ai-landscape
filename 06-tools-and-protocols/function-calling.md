# 函数调用与工具集成

> 最后更新：2026-06-08
> 数据来源：`data/tools.yaml` 自动生成

---

## 🔧 函数调用：让 LLM 使用工具

函数调用的核心：**让 LLM 能够调用外部 API 和工具**。

| 你的情况 | 推荐方案 | 理由 |
| --------- | --------- | ------ |
| **原生 Function Calling** | OpenAI / Anthropic | LLM 内置工具调用 |
| **工具集成平台** | [Composio](https://composio.dev) / [ACI.dev](https://github.com/aipotheosis-labs/aci) | 200+ / 600+ 应用连接器 |
| **MCP 协议** | MCP Servers | 标准化工具协议 |
| **Agent 协议** | [ACP](https://github.com/i-am-bee/acp) / A2A | Agent 间通信 |

> [!TIP]
> **Composio 是工具集成的最佳选择**
> 15K Stars，200+ 应用连接器，一行代码接入。支持 GitHub、Slack、Jira 等主流工具。

---

## 📋 函数调用工具总览

<!-- 以下内容由脚本自动生成，请勿手动修改 -->
<!-- AUTOGEN_START -->

### 📡 协议

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [ACP](https://github.com/i-am-bee/acp) | AI Agent 通信开放协议 | mcp, agent, chat | 1K Stars<br>Agent 通信<br>开放协议 |
| [python-a2a](https://github.com/themanojdesai/python-a2a) | Python A2A 协议实现 | mcp, a2a, coding-assistant | 1K Stars<br>A2A 协议<br>Python 实现 |

### 🔧 内置工具

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [OpenAI Built-in Tools](https://openai.com) | OpenAI 官方内置工具集 (Web Search, File Search, Computer Use) | openai-compatible, tool-calling, search, agent | Web Search 联网搜索<br>File Search 文件检索<br>Computer Use 计算机操作<br>原生集成无需额外配置 |
| [Anthropic Tool Use](https://anthropic.com) | Claude 原生工具调用能力，支持 MCP | anthropic, tool-calling, mcp | Claude 原生工具调用<br>MCP 深度集成<br>Computer Use 能力 |

### 🔗 工具集成

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [Composio](https://composio.dev) | AI Agent 专用的工具集成平台，提供海量经过测试的连接器 | mcp, function-calling | 数百个高频应用认证与集成<br>开箱即用，高度兼容不同 Agent 框架<br>统一认证管理 |
| [Klavis AI](https://github.com/Klavis-AI/klavis) | MCP 集成平台，让 AI Agent 使用各种工具 | mcp, openai-compatible | 5.7K Stars<br>MCP 集成<br>AI Agent 工具 |
| [ACI.dev](https://github.com/aipotheosis-labs/aci) | 开源工具调用平台，连接 600+ 应用 | tool-calling, mcp, openai-compatible | 4.8K Stars<br>600+ 应用<br>工具调用平台 |
| [Toolhouse](https://toolhouse.ai) | AI Agent 工具云服务，一键安装工具集 | mcp, function-calling, cloud-only | 一键安装工具<br>SDK 集成<br>100+ 工具 |

<!-- AUTOGEN_END -->
<!-- 以上内容由脚本自动生成 -->

---

## 💡 工具对比

| 维度 | OpenAI Built-in | [Anthropic Tool Use](https://anthropic.com) | [Composio](https://composio.dev) | [ACI.dev](https://github.com/aipotheosis-labs/aci) |
| ------ | ----------------- | ------------------- | ---------- | --------- |
| **工具数量** | 3 个 | 自定义 | 200+ | 600+ |
| **MCP 支持** | ❌ | ✅ | ❌ | ❌ |
| **学习曲线** | 低 | 低 | 低 | 低 |
| **适用场景** | 搜索/文件/计算机 | 自定义工具 | 应用集成 | 应用集成 |

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
