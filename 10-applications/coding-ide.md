# 💻 AI 编程 IDE

> 最后更新：2026-06-09
> 数据来源：`data/applications.yaml` 自动生成

---

## 🧭 AI 编程 IDE 选型罗盘

| 你的情况 | 推荐 IDE | 理由 |
|---------|---------|------|
| 🎯 **VS Code 用户，想要最强 AI** | **Cursor** | Composer 多文件修改 + Tab 补全，最强 AI 原生 IDE |
| 🧠 **JetBrains 用户** | **JetBrains AI** / **Continue** | 原生集成 / 开源 MCP 支持 |
| 🔒 **隐私优先，不想代码上传** | **Tabnine** | 气隙隔离部署，零代码保留 |
| ☁️ **AWS 生态开发者** | **Amazon Kiro** / **Q Developer** | Spec 驱动 + AWS 深度集成 |
| 🔍 **Google 生态开发者** | **Gemini Code Assist** | 百万 Token 上下文，Android Studio 原生 |
| 🆓 **想要开源免费方案** | **Cline** / **Continue** | 完全开源，MCP 支持 |
| 🇨🇳 **中文场景，国内模型** | **通义灵码** / **Trae** | Qwen3 / 豆包驱动，中文优化 |
| 🏢 **企业级，跨仓库理解** | **Sourcegraph Cody** / **Augment Code** | 跨仓库搜索 + 深度上下文 |
| 🌐 **浏览器端开发** | **Replit** | 全自动构建部署，内置数据库 |

> [!TIP]
> **Cursor 是 2026 年 AI 编程 IDE 的标杆**
> Composer 模式可以自动跨文件修改，Tab 补全延迟低于 100ms，完美适配 Claude Opus 4 和 GPT-5.5。如果你想要最强的 AI 编程体验，Cursor 是首选。

> [!NOTE]
> 纯 Agent 类工具 (Claude Code, Codex, Devin, Aider) 已移至 [🤖 自主 Agent 工具](./agent-tools.md)

---

## 📋 AI 编程 IDE 总览

<!-- 以下内容由脚本自动生成，请勿手动修改 -->
<!-- AUTOGEN_START -->

#### 🆓 开源项目

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [Cline](https://github.com/cline/cline) | 在 VS Code 内部运行的开源全能自主编码 Agent | coding, agent, vscode-extension, open-source, mcp | 强大的全自动执行流水线<br>原生全面集成 MCP 协议扩展工具<br>完全开源 |
| [Tabby](https://github.com/TabbyML/tabby) | 自托管 AI 编码助手 | coding, self-hosted, agent | 33.6K Stars<br>自托管<br>AI 编码助手 |
| [Continue](https://continue.dev) | 开源 IDE AI 助手，支持本地模型 | coding, vscode-extension, open-source, on-device, mcp | 开源本地模型支持<br>MCP 集成<br>VS Code/JetBrains 扩展 |
| [CodeGeeX](https://codegeex.cn) | 智谱 AI 开源编程助手，GLM-5.1 驱动 | coding, chinese, open-source, china-based | GLM-5.1 驱动<br>开源<br>VS Code 集成 |
| [Kilo Code](https://kilo.ai) | 开源 AI 编程助手，跨 IDE/终端/浏览器/Slack 使用 | coding, open-source, agent | 跨 IDE/终端/浏览器/Slack<br>BYOK 自带密钥<br>模型选择自由<br>透明可控开源方案 |

#### ☁️ 商业产品

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [Cursor](https://cursor.com) | 当下最领先的 AI 原生代码编辑器，深度重塑编程体验 | coding, coding-assistant, agent | Composer 模式自动多文件修改<br>极速的 Tab 预测补全 (100ms 以内)<br>项目级理解与智能重构<br>完美适配最强代码模型 (Claude Opus 4/GPT-5.5) |
| [GitHub Copilot](https://github.com/features/copilot) | GitHub 推出的 AI 编程助手，Cloud Agent + 多模型 | coding, agent, agentic, cloud-only | {'Copilot Workspace': 'Issue 到 PR 一站式'}<br>Cloud Agent 云端随时唤起<br>多模型支持<br>VS Code/JetBrains 原生集成 |
| [Windsurf](https://codeium.com/windsurf) | Codeium 团队 AI 原生 IDE，Cascade 核心，后被 Cognition 收购 | coding, coding-assistant, agent, automation | Cascade 核心——理解整个代码库<br>AI 原生架构设计<br>被 Cognition 收购 (~2.5 亿美元)<br>与 Cursor 并列第一梯队 |
| [Augment Code](https://augmentcode.com) | 企业级 AI 编程助手，深度理解代码库上下文 | coding, enterprise, long-context | 企业级代码理解<br>深度上下文感知<br>VS Code/JetBrains 集成 |
| [Trae](https://trae.ai) | 字节跳动推出的 AI 原生 IDE | coding, coding-assistant, chinese, agent | 字节跳动出品<br>AI 原生 IDE<br>中文优化 |
| [通义灵码](https://tongyi.aliyun.com/lingma) | 阿里巴巴 AI 编程助手，Qwen3 驱动 | coding, chinese, china-based | Qwen3 驱动<br>中文优化<br>阿里生态集成 |
| [MarsCode](https://marscode.com) | 字节跳动 AI 编程助手，豆包模型驱动 | coding, chinese, china-based | 豆包模型驱动<br>字节生态集成 |
| [Amazon Kiro](https://kiro.dev) | Amazon Agentic IDE，Spec 驱动开发+Agent Hooks+AWS 深度集成 | coding, agent, enterprise | Spec 驱动开发（Spec Mode）<br>Agent Hooks 自动化工作流<br>AWS 深度集成（Lambda/DynamoDB/CloudFormation）<br>IDE + CLI 双模式 |
| [Amazon Q Developer](https://aws.amazon.com/q/developer) | AWS 生态 AI 编程助手，前身为 CodeWhisperer，深耕云开发 | coding, enterprise, cloud-only | AWS 生态完美优化（Lambda/DynamoDB/CloudFormation）<br>安全漏洞快速检测<br>基础设施优化建议<br>VS Code/JetBrains 集成 |
| [Gemini Code Assist](https://cloud.google.com/gemini/docs/codeassist) | Google AI 编程助手，Gemini 驱动，长上下文代码理解 | coding, google, long-context | Gemini 3 驱动，百万级 Token 上下文<br>单次提示分析庞大 GitHub 仓库<br>Android Studio 原生首选<br>GCP 部署优化 |
| [JetBrains AI](https://www.jetbrains.com/ai/) | JetBrains 全家桶内置 AI 助手，深度 IDE 集成 | coding, enterprise | IntelliJ/PyCharm/WebStorm 全系列集成<br>深度代码理解和重构<br>企业级安全合规<br>Koog 1.0 Agent 框架支持 |
| [Replit](https://replit.com) | 浏览器端 AI 开发平台，Replit Agent 可自动规划/构建/调试/部署 | coding, agent, cloud-only | 浏览器端完整开发环境<br>Replit Agent 全自动构建部署<br>内置 PostgreSQL 数据库<br>从想法到上线极速路径 |
| [Sourcegraph Cody](https://sourcegraph.com/cody) | 企业级代码智能平台，跨仓库搜索+AI 编码助手 | coding, enterprise, code-quality | 强大的跨仓库代码搜索<br>企业级代码智能平台<br>VS Code/JetBrains 集成<br>适合大型组织代码理解 |
| [Supermaven](https://supermaven.com) | 极速 AI 代码补全工具，百万 Token 上下文窗口 | coding, coding-assistant | 极速代码补全（百万 Token 上下文）<br>VS Code 集成<br>低延迟预测 |
| [Qodo (CodiumAI)](https://www.qodo.ai) | AI 代码质量与测试平台，深度单元测试生成+代码审查 | code-quality, coding | 深度单元测试自动生成<br>自动代码审查<br>防止回归错误<br>代码完整性分析 |
| [Tabnine](https://www.tabnine.com) | 隐私优先的 AI 编码助手，支持完全本地部署 | coding, self-hosted, on-device | 隐私优先，零代码保留<br>气隙隔离部署选项<br>本地推理能力<br>适合高合规企业 |

<!-- AUTOGEN_END -->
<!-- 以上内容由脚本自动生成 -->

---

## 💡 IDE 对比

| 维度 | Cursor | Windsurf | GitHub Copilot | JetBrains AI | Continue |
|------|--------|----------|----------------|--------------|----------|
| 🤖 **AI 原生** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| ⌨️ **Tab 补全** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| 📝 **多文件修改** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| 🔌 **MCP 支持** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| 🆓 **开源** | ❌ | ❌ | ❌ | ❌ | ✅ |
| 💻 **本地模型** | ❌ | ❌ | ❌ | ❌ | ✅ |

---

> **更新频率**：每月更新。
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
