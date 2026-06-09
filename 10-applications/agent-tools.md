# 🤖 自主 Agent 工具

> 最后更新：2026-06-09
> 本文件收录以自主执行为核心的 AI Agent 工具，与 IDE 类工具的区别：无需 IDE，Agent 自主规划并闭环执行任务。

---

## 🔍 Agent 工具 vs IDE 工具

| 维度 | IDE 类 (Cursor/Cline) | Agent 工具 (本页) |
|------|----------------------|-------------------|
| 🖥️ 交互方式 | IDE 内嵌，人机协作 | 终端/云端，Agent 自主执行 |
| 📦 是否需要 IDE | ✅ 是 | ❌ 否 |
| ⚡ 执行模式 | 补全 + Agent 辅助 | 全自主闭环 |
| 🎯 代表 | Cursor, Windsurf, Cline | Claude Code, Codex, Devin |

---

## 🧭 Agent 工具选型罗盘

| 你的情况 | 推荐工具 | 理由 |
|---------|---------|------|
| 🖥️ **终端开发者** | **Claude Code** / **Aider** | CLI 原生，全局工程理解 |
| ☁️ **云端异步编码** | **OpenAI Codex** / **Devin** | 云端沙盒，不污染本地 |
| 👔 **全办公场景** | **WorkBuddy** | 不限于编程，覆盖全办公 |
| 🆓 **开源免费** | **Aider** / **Hermes Agent** | 完全开源，多模型可选 |
| 🚀 **全自主交付** | **Devin 3.0** | 独立环境，SOLO 模式 |
| 🌐 **浏览器自动化** | **browser-use** | 97K Stars，AI 浏览器操控 |
| 🧠 **自我进化 Agent** | **Hermes Agent** | 188K Stars，自动创建技能 |
| 🔬 **深度研究** | **DeerFlow** | 字节跳动，多 Agent 协同 |

> [!TIP]
> **Hermes Agent 是 2026 年最火的开源 Agent**
> 188K Stars，自我进化能力（从经验中自动创建技能），三层记忆系统，全平台消息网关支持。

---

## 📋 Agent 工具总览

<!-- 以下内容由脚本自动生成，请勿手动修改 -->
<!-- AUTOGEN_START -->

#### 🆓 开源项目

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [Hermes Agent](https://hermes-agent.nousresearch.com) | Nous Research 开源自进化 AI Agent，持久记忆+自动技能创建+多平台消息网关 | agent, autonomous, open-source, memory, mcp | 188K Stars，2026 年最火开源 Agent<br>自我进化：从经验中自动创建技能并持续改进<br>三层记忆：持久记忆+FTS5 对话搜索+Honcho 用户建模<br>全平台消息网关：Telegram/Discord/Slack/WhatsApp/Signal/CLI<br>多模型自由切换，200+ 模型支持<br>Cron 定时自动化 + 子 Agent 委派并行 |
| [AutoGPT](https://agpt.co) | 开源自主 AI Agent 平台先驱，无需人工干预自主完成复杂任务 | agent, autonomous, open-source | 183K Stars，自主 Agent 开山鼻祖<br>无需人工逐轮干预，自主拆解和执行复杂任务<br>长时间运行任务场景优势明显<br>Forge/Backend/Frontend 完整平台架构<br>庞大的插件和扩展生态 |
| [Claw Code](https://claw-code.codes) | Rust 重写的开源 AI 编码 Agent，Claude Code 架构的净室实现，GitHub 历史增速第一 | coding, agent, cli-tool, open-source, autonomous | 167K Stars，GitHub 史上最快破 10 万星<br>Rust 重写，极速低内存<br>Claude Code 架构净室实现<br>多 Agent 编排 + MCP 协议支持<br>跨平台 CLI |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | Google 开源终端 AI Agent，免费使用 Gemini 2.5 Pro + 1M Token 上下文 | coding, agent, cli-tool, google, open-source | 100K Stars，Google 官方开源<br>免费使用 Gemini 2.5 Pro（60 次/分钟、1000 次/天）<br>1M Token 上下文窗口<br>终端编码/调试/文件操作<br>MCP 工具扩展支持 |
| [browser-use](https://github.com/browser-use/browser-use) | 最热门的 AI 浏览器自动化框架，让 Agent 直接操控浏览器完成复杂网页任务 | agent, browser, open-source, automation | 93K Stars，AI 浏览器自动化第一<br>支持多种 LLM 后端<br>DOM 交互 + 视觉理解双模式<br>多标签页管理与表单自动填写<br>与 OpenClaw/Claude Code 生态联动 |
| [DeerFlow](https://github.com/bytedance/deer-flow) | 字节跳动开源深度研究多 Agent 框架，LangGraph 驱动，支持子代理协同 | agent, open-source, deep-research, chinese | GitHub Trending 冠军项目<br>字节跳动出品，SuperAgent 架构<br>LangGraph 驱动的多 Agent 协同<br>深度研究能力（Deep Research）<br>子代理动态调度 |
| [CowAgent](https://github.com/zhayujie/CowAgent) | 开源超级 AI 助手，任务规划+执行，Agent Harness | agent, automation | 45K Stars<br>任务规划<br>Agent Harness |
| [Cherry Studio](https://cherry-ai.com) | AI 生产力桌面系统，300+ 助手与自主 Agent，多模型统一接入 | agent, cross-platform, desktop, open-source, mcp | 43K Stars，桌面端 AI 生产力工具<br>300+ 预置助手与自主 Agent<br>多模型自由切换（OpenAI/Claude/Gemini/DeepSeek 等）<br>本地 API 服务器 + Agent 模式<br>MCP 工具集成 |
| [Open Interpreter](https://openinterpreter.com) | 开源本地代码解释器，让 LLM 在本地运行代码完成任意任务 | agent, cli-tool, open-source, on-device | 42K Stars，本地代码执行<br>支持 Python/JavaScript/Shell 等多语言<br>本地运行，无文件大小和时间限制<br>OpenAI Code Interpreter 的开源替代<br>可访问互联网，利用任何包或库 |
| [AstrBot](https://github.com/AstrBotDevs/AstrBot) | 开源 AI Agent 助手，集成多平台，支持插件扩展 | agent, cross-platform, mcp | 34K Stars<br>多平台集成<br>插件扩展 |
| [Aider](https://aider.chat) | 开源终端 AI 结对编程助手，Git 原生设计，多模型后端 | coding, cli-tool, coding-assistant, open-source, agentic | Git 原生设计，每次修改自动 commit<br>多模型后端 (Claude/GPT/Gemini/DeepSeek)<br>43K+ Stars<br>完全开源免费 |
| [Goose](https://goose-docs.ai) | Block 开源可扩展 AI Agent，自主完成复杂工程任务，桌面+CLI+API 三模式 | agent, open-source, automation, cross-platform | Block（原 Square）出品，27K+ Stars<br>从零构建项目、编写执行代码、调试<br>桌面应用 + CLI + API 三种模式<br>任意 LLM 后端<br>丰富的工具扩展生态 |
| [OpenManus](https://github.com/OpenManus/OpenManus) | 开源 Manus 替代方案 | agent, open-source, multimodal | 开源 Manus 替代<br>多 Agent 协作<br>社区驱动 |
| [BabyAGI](https://github.com/yoheinakajima/babyagi) | 最早的任务驱动自主 Agent，基于目标分解自动管理任务队列 | agent, autonomous, open-source | 22K Stars，任务驱动 Agent 先驱<br>目标分解为子任务自动执行<br>优先级动态调整<br>上下文感知的任务创建<br>自主 Agent 概念启蒙者 |
| [Trigger.dev](https://github.com/triggerdotdev/trigger.dev) | AI Agent 和工作流的全托管部署平台 | automation, workflow, serverless | 15.2K Stars<br>全托管部署<br>AI Agent 工作流 |
| [Letta (MemGPT)](https://letta.com) | 开源长期记忆 Agent 框架，让 LLM 拥有持久状态 | agent, open-source, memory | Agent 长期记忆框架<br>持久状态管理<br>自定义工具集成<br>MemGPT 论文实现 |
| [OpenAI Codex](https://chatgpt.com/codex) | OpenAI 云端编程 Agent，CLI 开源 + Cloud 云端沙盒，自动提交 PR | coding, agent, cloud-only, openai-compatible, autonomous | Codex CLI 开源 + Codex Cloud 云端沙盒<br>云端隔离执行，自动提交 PR<br>并行多任务<br>6 款角色专用插件<br>周活用户 500 万+ |
| [OpenClaw](https://docs.openclaw.ai) | 开源个人 AI Agent 平台，技能/记忆/多通道消息/Dreaming | agent, open-source, mcp | 个人 AI Agent 平台<br>技能+记忆+Dreaming<br>多通道消息集成<br>Canvas/A2UI 可视化 |
| [Ruflo](https://github.com/ruvnet/ruflo) | Claude Code 多智能体编排平台，100+ 专用 Agent + Swarm 群智协调 | agent, open-source, mcp | Claude Code 多智能体编排层<br>100+ 专业化 Agent 协同<br>Swarm 编排 + 自学习记忆<br>RAG 向量记忆集成<br>企业级安全 + MCP 集成 |
| [Sweep AI](https://sweep.dev) | AI 自动将 GitHub Issue 转为 Pull Request，自主编码修复+完整测试 | coding, agent, automation | GitHub Issue 自动转 PR<br>自主编码修复 Bug 和实现功能<br>JetBrains IDE 插件<br>开源免费 |

#### ☁️ 商业产品

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [Claude Code](https://www.anthropic.com/product/claude-code) | Anthropic 终端自主编程 Agent，基于 Claude Opus 4.7，全局工程理解与闭环执行 | coding, agent, cli-tool, autonomous, anthropic | 终端 CLI 自主执行，无需 IDE<br>全局工程理解与闭环迭代<br>MCP/Skills/Hooks 扩展<br>Git Worktree 并行开发<br>Computer Use 能力 |
| [Devin](https://www.cognition.ai/devin) | Cognition 自主 AI 软件工程师，拥有独立 Shell/IDE/浏览器，SOLO 模式全自主交付 | coding, agent, autonomous, all-in-one | 自主 AI 软件工程师<br>独立 Shell/IDE/浏览器环境<br>Devin 3.0 SOLO 模式 + Vibe Coding<br>$20/月起<br>Cognition 估值 260 亿美元 |
| [WorkBuddy](https://www.codebuddy.cn/work/) | 腾讯云全场景桌面办公 Agent，可操控微信/浏览器/Office，集成 CodeBuddy 编程能力 | agent, collaboration, chinese, enterprise, desktop | 全场景桌面办公 Agent<br>可操控微信/浏览器/Office<br>集成 CodeBuddy 编程能力<br>企业版 Agent Suite<br>深度适配国内办公生态 |
| [Manus](https://manus.im) | 通用 AI Agent，可执行复杂任务 | agent, multimodal, automation | 通用 AI Agent<br>可执行复杂任务<br>多工具协作 |
| [Google Antigravity](https://kiro.dev/blog/antigravity/) | Google Agent 开发平台，从 IDE 演进为完整 Agent 平台，Gemini 3.5 驱动 | coding, agent, google, autonomous | Antigravity 2.0：从 IDE 插件进化为独立 Agent 桌面应用<br>Gemini 3.5 驱动，Manager Surface 动态子 Agent 协调<br>JSON Hooks + Cron 定时任务 + 异步子 Agent<br>Antigravity CLI（取代 Gemini CLI）<br>编辑器+终端+浏览器全栈验证 |
| [Google Jules](https://jules.google.com) | Google 自主编码 Agent，Gemini 3 Pro 驱动，云端 VM 自主执行 | coding, agent, google, autonomous | Gemini 3 Pro 驱动<br>云端 VM 自主执行<br>GitHub 深度集成<br>自动规划/实现/提交 PR |
| [Conductor](https://www.conductor.build) | 模型中立的多 Agent 协调 UI，连接 Codex/Claude Code 等多个编码 Agent | agent, automation | 模型中立，连接多个底层 Agent<br>隔离工作区统一界面<br>多 Agent 并行推进<br>适合复杂项目协调 |
| [Qoder](https://qoder.com) | 阿里巴巴 AI Agent 编程平台，需求驱动开发+智能上下文引擎+自主桌面 | coding, agent, chinese, china-based | 阿里巴巴出品 Agent 编程平台<br>需求驱动开发（非代码优先）<br>智能上下文引擎自动感知项目<br>Ask 模式 + Agent 智能体模式<br>QoderWork 团队协作版 |

<!-- AUTOGEN_END -->
<!-- 以上内容由脚本自动生成 -->

---

## 💡 工具对比

| 维度 | Hermes Agent | Claude Code | Codex | Devin | Aider |
|------|--------------|-------------|-------|-------|-------|
| ⭐ **Stars** | 188K | - | - | - | 43K |
| 🆓 **开源** | ✅ | ❌ | 部分 | ❌ | ✅ |
| 🧠 **自我进化** | ✅ | ❌ | ❌ | ❌ | ❌ |
| 💾 **持久记忆** | ✅ | ❌ | ❌ | ❌ | ❌ |
| ☁️ **云端执行** | ❌ | ❌ | ✅ | ✅ | ❌ |
| 🌐 **浏览器** | ✅ | ✅ | ❌ | ✅ | ❌ |
| 💰 **价格** | 免费 | $20/月 | $20/月 | $500/月 | 免费 |

---

> **更新频率**：每月更新。
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
