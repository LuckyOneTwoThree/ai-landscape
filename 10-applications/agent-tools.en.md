# 🤖 Autonomous Agent Tools

> Last updated: 2026-06-09
> This document catalogs AI Agent tools centered around autonomous execution. Difference from IDE-class tools: No IDE required, the Agent autonomously plans and executes tasks in a closed loop.

---

## 🔍 Agent Tools vs IDE Tools

| Dimension | **IDE-Class Cursor/Cline** | Agent Tools (This Page) |
| ----------- | **--------------------------** | ------------------------- |
| 🖥️ Interaction Mode | **IDE-embedded, human-AI collaboration** | Terminal/Cloud, Agent autonomous execution |
| 📦 Requires IDE | **✅ Yes** | ❌ No |
| ⚡ Execution Mode | **Autocomplete + Agent assistance** | Fully autonomous closed loop |
| 🎯 Representatives | **Cursor, Windsurf, Cline** | [Claude Code](https://www.anthropic.com/product/claude-code), [Codex](https://openai.com), [Devin](https://www.cognition.ai/devin) |

---

## 🧭 Agent Tool Selection Compass

| Your Situation | **Recommended Tool** | Rationale |
| ---------------- | **------------------** | ----------- |
| 🖥️ **Terminal Developer**.chat) | **[Claude Code](https://www.anthropic.com/product/claude-code) / [Aider](https://aider.chat)** | CLI native, global project understanding |
| ☁️ **Cloud Asynchronous Coding**.chat) | **[OpenAI Codex](https://chatgpt.com/codex) / [Devin](https://www.cognition.ai/devin)** | Cloud sandbox, doesn't pollute local env |
| 👔 **Full Office Scenarios**.chat) | **[WorkBuddy](https://www.codebuddy.cn/work/)** | Not limited to programming, covers all office tasks |
| 🆓 **[Open Source](https://[aider](https://aider.chat) & Free**.chat) | **[Aider](https://aider.chat) / [Hermes Agent](https://hermes-agent.nousresearch.com)** | Fully [open source](https://[aider](https://aider.chat)](https://[aider](https://aider.chat).chat), multiple models available |
| 🚀 **Fully Autonomous Delivery**.chat) | **[Devin](https://www.cognition.ai/devin) 3.0** | Isolated environment, SOLO mode |
| 🌐 **[Browser](https://[aider](https://aider.chat) Automation**.chat) | **[browser-use](https://github.com/browser-use/browser-use)](https://github.com/[browser](https://[aider](https://aider.chat)](https://[aider](https://aider.chat).chat)-use/[browser](https://[aider](https://aider.chat)](https://[aider](https://aider.chat).chat)-use)** | 97K [Stars](https://[aider](https://aider.chat), AI [browser](https://[aider](https://aider.chat)](https://[aider](https://aider.chat).chat) control |
| 🧠 **[Self-Evolving](https://[aider](https://aider.chat) Agent**.chat) | **[Hermes Agent](https://hermes-agent.nousresearch.com)** | 188K [Stars](https://[aider](https://aider.chat), automatically creates skills |
| 🔬 **Deep Research**.chat) | **[DeerFlow](https://github.com/bytedance/deer-flow)** | ByteDance, multi-agent collaboration |

> [!TIP]
> **Hermes Agent is the most popular open-source Agent of 2026**
> 188K Stars, self-evolution capabilities (automatically creates skills from experience), three-tier memory system, full-platform message gateway support.

---

## 📋 Agent Tools Overview

<!-- 以下内容由脚本自动生成，请勿手动修改 -->
<!-- AUTOGEN_START -->

#### 🆓 Open Source Projects

| Name | Description | Tags | Highlights |
| ------ | ------------- | ------ | ------------ |
| [Hermes Agent](https://hermes-agent.nousresearch.com) | Nous Research open-source self-evolving AI Agent, persistent memory + automatic skill creation + multi-platform message gateway | agent, autonomous, open-source, memory, mcp | 188K Stars, most popular open-source Agent in 2026<br>Self-evolution: Automatically creates skills from experience and continuously improves<br>Three-tier memory: Persistent memory + FTS5 chat search + Honcho user modeling<br>Full-platform message gateway: Telegram/Discord/Slack/WhatsApp/Signal/CLI<br>Free switching between multiple models, 200+ models supported<br>Cron scheduled automation + Sub-agent delegated parallelism |
| [AutoGPT](https://agpt.co) | Pioneer of open-source autonomous AI Agent platforms, completes complex tasks autonomously without human intervention | agent, autonomous, open-source | 183K Stars, the founding father of autonomous Agents<br>Autonomous breakdown and execution of complex tasks without turn-by-turn human intervention<br>Obvious advantage in long-running task scenarios<br>Complete platform architecture of Forge/Backend/Frontend<br>Massive plugin and extension ecosystem |
| [Claw Code](https://claw-code.codes) | Open-source AI coding Agent rewritten in Rust, a clean-room implementation of [Claude Code](https://www.anthropic.com/product/claude-code) architecture, fastest growing in GitHub history | coding, agent, cli-tool, open-source, autonomous | 167K Stars, fastest to break 100K stars in GitHub history<br>Rewritten in Rust, extremely fast and low memory<br>Clean-room implementation of [Claude Code](https://www.anthropic.com/product/claude-code) architecture<br>Multi-agent orchestration + MCP protocol support<br>Cross-platform CLI |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | Google open-source terminal AI Agent, free access to Gemini 2.5 Pro + 1M Token context | coding, agent, cli-tool, google, open-source | 100K Stars, official Google open-source<br>Free access to Gemini 2.5 Pro (60 requests/minute, 1000 requests/day)<br>1M Token context window<br>Terminal coding/debugging/file operations<br>MCP tool extension support |
| [browser-use](https://github.com/browser-use/browser-use) | Most popular AI browser automation framework, allowing Agents to directly control browsers to complete complex web tasks | agent, browser, open-source, automation | 93K Stars, #1 in AI browser automation<br>Supports multiple LLM backends<br>Dual mode: DOM interaction + visual understanding<br>Multi-tab management and automatic form filling<br>Ecosystem integration with [OpenClaw](https://docs.openclaw.ai)/[Claude Code](https://www.anthropic.com/product/claude-code) |
| [DeerFlow](https://github.com/bytedance/deer-flow) | ByteDance open-source deep research multi-agent framework, driven by LangGraph, supports sub-agent collaboration | agent, open-source, deep-research, chinese | GitHub Trending champion project<br>Produced by ByteDance, SuperAgent architecture<br>LangGraph-driven multi-agent collaboration<br>Deep research capabilities<br>Dynamic sub-agent scheduling |
| [CowAgent](https://github.com/zhayujie/CowAgent) | Open-source super AI assistant, task planning + execution, Agent Harness | agent, automation | 45K Stars<br>Task planning<br>Agent Harness |
| [Cherry Studio](https://cherry-ai.com) | AI productivity desktop system, 300+ assistants and autonomous Agents, unified multi-model access | agent, cross-platform, desktop, open-source, mcp | 43K Stars, desktop AI productivity tool<br>300+ built-in assistants and autonomous Agents<br>Free switching between multiple models (OpenAI/Claude/Gemini/DeepSeek, etc.)<br>Local API server + Agent mode<br>MCP tool integration |
| [Open Interpreter](https://openinterpreter.com) | Open-source local code interpreter, lets LLMs run code locally to complete arbitrary tasks | agent, cli-tool, open-source, on-device | 42K Stars, local code execution<br>Supports Python/JavaScript/Shell and other languages<br>Runs locally, no file size or time limits<br>Open-source alternative to OpenAI Code Interpreter<br>Can access the internet, utilizing any package or library |
| [AstrBot](https://github.com/AstrBotDevs/AstrBot) | Open-source AI Agent assistant, multi-platform integration, supports plugin extensions | agent, cross-platform, mcp | 34K Stars<br>Multi-platform integration<br>Plugin extensions |
| [Aider](https://aider.chat) | Open-source terminal AI pair programming assistant, Git-native design, multi-model backend | coding, cli-tool, coding-assistant, open-source, agentic | Git-native design, automatically commits every modification<br>Multi-model backend (Claude/GPT/Gemini/DeepSeek)<br>43K+ Stars<br>Fully open-source and free |
| [Goose](https://goose-docs.ai) | Block open-source extensible AI Agent, autonomously completes complex engineering tasks, Desktop+CLI+API tri-mode | agent, open-source, automation, cross-platform | Produced by Block (formerly Square), 27K+ Stars<br>Builds projects from scratch, writes and executes code, debugging<br>Desktop app + CLI + API three modes<br>Any LLM backend<br>Rich tool extension ecosystem |
| [OpenManus](https://github.com/OpenManus/OpenManus) | Open-source Manus alternative | agent, open-source, multimodal | Open-source Manus alternative<br>Multi-agent collaboration<br>Community-driven |
| [BabyAGI](https://github.com/yoheinakajima/babyagi) | Earliest task-driven autonomous Agent, automatically manages task queues based on goal decomposition | agent, autonomous, open-source | 22K Stars, task-driven Agent pioneer<br>Decomposes goals into subtasks for automatic execution<br>Dynamic priority adjustment<br>Context-aware task creation<br>Concept initiator of autonomous Agents |
| [Trigger.dev](https://github.com/triggerdotdev/trigger.dev) | Fully managed deployment platform for AI Agents and workflows | automation, workflow, serverless | 15.2K Stars<br>Fully managed deployment<br>AI Agent workflows |
| [Letta (MemGPT)](https://letta.com) | Open-source long-term memory Agent framework, giving LLMs persistent state | agent, open-source, memory | Agent long-term memory framework<br>Persistent state management<br>Custom tool integration<br>MemGPT paper implementation |
| [OpenAI Codex](https://chatgpt.com/codex) | OpenAI cloud-based programming Agent, open-source CLI + Cloud sandbox, automatically submits PRs | coding, agent, cloud-only, openai-compatible, autonomous | Codex CLI open-source + Codex Cloud sandbox<br>Isolated cloud execution, automatically submits PRs<br>Parallel multi-tasking<br>6 role-specific plugins<br>5M+ weekly active users |
| [OpenClaw](https://docs.openclaw.ai) | Open-source personal AI Agent platform, skills/memory/multi-channel messaging/Dreaming | agent, open-source, mcp | Personal AI Agent platform<br>Skills + Memory + Dreaming<br>Multi-channel messaging integration<br>Canvas/A2UI visualization |
| [Ruflo](https://github.com/ruvnet/ruflo) | [Claude Code](https://www.anthropic.com/product/claude-code) multi-agent orchestration platform, 100+ specialized Agents + Swarm intelligence coordination | agent, open-source, mcp | [Claude Code](https://www.anthropic.com/product/claude-code) multi-agent orchestration layer<br>100+ specialized Agents collaboration<br>Swarm orchestration + self-learning memory<br>RAG vector memory integration<br>Enterprise-grade security + MCP integration |
| [Sweep AI](https://sweep.dev) | AI automatically converts GitHub Issues to Pull Requests, autonomous coding fixes + full testing | coding, agent, automation | Automatically converts GitHub Issues to PRs<br>Autonomous coding to fix bugs and implement features<br>JetBrains IDE plugin<br>Open-source and free |

#### ☁️ Commercial Products

| Name | Description | Tags | Highlights |
| ------ | ------------- | ------ | ------------ |
| [Claude Code](https://www.anthropic.com/product/claude-code) | Anthropic terminal autonomous programming Agent, based on Claude Opus 4.7, global project understanding and closed-loop execution | coding, agent, cli-tool, autonomous, anthropic | Terminal CLI autonomous execution, no IDE required<br>Global project understanding and closed-loop iteration<br>MCP/Skills/Hooks extensions<br>Git Worktree parallel development<br>Computer Use capabilities |
| [Devin](https://www.cognition.ai/devin) | Cognition autonomous AI software engineer, has independent Shell/IDE/browser, SOLO mode fully autonomous delivery | coding, agent, autonomous, all-in-one | Autonomous AI software engineer<br>Independent Shell/IDE/browser environment<br>[Devin](https://www.cognition.ai/devin) 3.0 SOLO mode + Vibe Coding<br>Starting from $20/month<br>Cognition valuation $26 billion |
| [WorkBuddy](https://www.codebuddy.cn/work/) | Tencent Cloud full-scenario desktop office Agent, can control WeChat/browser/Office, integrates CodeBuddy programming capabilities | agent, collaboration, chinese, enterprise, desktop | Full-scenario desktop office Agent<br>Can control WeChat/browser/Office<br>Integrates CodeBuddy programming capabilities<br>Enterprise edition Agent Suite<br>Deep adaptation to domestic office ecosystem |
| [Manus](https://manus.im) | Universal AI Agent, capable of executing complex tasks | agent, multimodal, automation | Universal AI Agent<br>Capable of executing complex tasks<br>Multi-tool collaboration |
| [Google Antigravity](https://kiro.dev/blog/antigravity/) | Google Agent development platform, evolved from IDE to complete Agent platform, driven by Gemini 3.5 | coding, agent, google, autonomous | Antigravity 2.0: Evolved from IDE plugin to standalone Agent desktop application<br>Driven by Gemini 3.5, Manager Surface dynamic sub-agent coordination<br>JSON Hooks + Cron scheduled tasks + Asynchronous sub-agents<br>Antigravity CLI (replaces Gemini CLI)<br>Full-stack verification of Editor+Terminal+Browser |
| [Google Jules](https://jules.google.com) | Google autonomous coding Agent, driven by Gemini 3 Pro, cloud VM autonomous execution | coding, agent, google, autonomous | Driven by Gemini 3 Pro<br>Cloud VM autonomous execution<br>Deep GitHub integration<br>Auto planning/implementation/PR submission |
| [Conductor](https://www.conductor.build) | Model-neutral multi-Agent coordination UI, connects [Codex](https://openai.com)/[Claude Code](https://www.anthropic.com/product/claude-code) and other coding Agents | agent, automation | Model-neutral, connects multiple underlying Agents<br>Isolated workspaces unified interface<br>Multi-Agent parallel advancement<br>Suitable for complex project coordination |
| [Qoder](https://qoder.com) | Alibaba AI Agent programming platform, requirement-driven development + intelligent context engine + autonomous desktop | coding, agent, chinese, china-based | AI Agent programming platform by Alibaba<br>Requirement-driven development (not code-first)<br>Intelligent context engine automatically perceives projects<br>Ask mode + Agent mode<br>QoderWork team collaboration edition |

<!-- AUTOGEN_END -->
<!-- 以上内容由脚本自动生成 -->

---

## 💡 Tool Comparison

| Dimension | Hermes Agent | [Claude Code](https://www.anthropic.com/product/claude-code) | Codex | [Devin](https://www.cognition.ai/devin) | [Aider](https://aider.chat) |
| ----------- | -------------- | ------------- | ------- | ------- | ------- |
| ⭐ [**Stars**](https://[aider](https://aider.chat).chat) | 188K | - | - | - | 43K |
| 🆓 [**Open Source**](https://[aider](https://aider.chat).chat) | ✅ | ❌ | Partial | ❌ | ✅ |
| 🧠 [**Self-Evolving**](https://[aider](https://aider.chat).chat) | ✅ | ❌ | ❌ | ❌ | ❌ |
| 💾 [**Persistent Memory**](https://[aider](https://aider.chat).chat) | ✅ | ❌ | ❌ | ❌ | ❌ |
| ☁️ [**Cloud Execution**](https://[aider](https://aider.chat).chat) | ❌ | ❌ | ✅ | ✅ | ❌ |
| 🌐 [**Browser**](https://[aider](https://aider.chat).chat) | ✅ | ✅ | ❌ | ✅ | ❌ |
| 💰 [**Pricing**](https://[aider](https://aider.chat).chat) | Free | $20/mo | $20/mo | $500/mo | Free |

---

> **Update Frequency**: Monthly updates.
> **Automation**: Run `python scripts/build_docs.py` to re-render tables from YAML.
