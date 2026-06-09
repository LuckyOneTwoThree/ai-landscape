# 浏览器控制

> 最后更新：2026-06-08
> 数据来源：`data/tools.yaml` 自动生成

---

## 🧭 浏览器控制选型罗盘

| 你的情况 | 推荐工具 | 理由 |
| --------- | --------- | ------ |
| **复杂网页自动化（登录/填表/点击）** | [**Browser Use**](https://github.com/browser-use/browser-use) | 97K Stars，DOM 解析 + 视觉识别，功能最强 |
| **跨浏览器测试/自动化** | [**Playwright**](https://playwright.dev) | Microsoft 出品，Chromium/Firefox/WebKit 全支持 |
| **命令行自动化脚本** | [**Agent Browser**](https://github.com/vercel-labs/agent-browser) | [Vercel](https://vercel.com) 出品，CLI 形式，轻量易集成 |
| **Chrome 扩展形式** | [**Nanobrowser**](https://github.com/nanobrowser/nanobrowser) | 浏览器插件，无需额外安装，多 Agent 协作 |
| **绕过反爬/Cloudflare** | [**Camofox Browser**](https://github.com/jo-inc/camofox-browser) | 隐身无头浏览器，专门绕过反爬检测 |
| **视觉优先，截图+坐标** | [**Browser Agent**](https://github.com/magnitudedev/browser-agent) | 截图 + 坐标点击，适合通用 Agent |
| **系统级屏幕操控** | [**Anthropic / OpenAI Computer Use**](https://openai.com) | 不限于浏览器，可操控任意桌面应用 |

> [!TIP]
> **Browser Use 是 2026 年浏览器控制的最佳选择**
> 97K Stars，让 AI Agent 具备完整的浏览器自主操作能力。结合 Playwright 底层，支持登录、填表、点击等复杂操作，MCP Server 集成。

## ⚡ 极简实战：让 AI 自己上网 (以 Browser Use 为例)

在 2026 年，控制浏览器不需要手写繁琐的 XPath 或 CSS 选择器。视觉模型会自己“看”屏幕并点击。只需要不到 10 行代码：

```python
from browser_use import Agent
import asyncio

async def main():
    # 只要告诉它目标，它会自动打开浏览器，搜索、点击、甚至滚动页面
    agent = Agent(task="去 Github 搜索 AI Landscape 项目，找到排名前三的仓库并告诉我它们的名字")
    await agent.run()

asyncio.run(main())
```

---

## 📋 浏览器控制工具总览

<!-- 以下内容由脚本自动生成，请勿手动修改 -->
<!-- AUTOGEN_START -->

### 🌐 浏览器

| 名称 | 简介 | 标签 | 亮点 |
| ------ | ------ | ------ | ------ |
| [Browser Use](https://github.com/browser-use/browser-use) | 让大模型具备完整的浏览器自主操作能力，结合 [Playwright](https://playwright.dev) 等底层 | vscode-extension, automation, mcp | DOM 解析与视觉识别结合<br>大幅增强 Agent 的互联网交互能力<br>MCP Server 集成 |
| [Playwright](https://playwright.dev) | Microsoft 出品跨浏览器自动化框架，MCP Server 支持 | vscode-extension, automation, mcp | Microsoft 出品<br>跨浏览器 (Chromium/Firefox/WebKit)<br>MCP Server 支持<br>70K+ Stars |
| [Agent Browser](https://github.com/vercel-labs/agent-browser) | [Vercel](https://vercel.com) 出品的 AI Agent 浏览器自动化 CLI | vscode-extension, agent, automation, cloud-only | 35.5K Stars<br>[Vercel](https://vercel.com) 出品<br>浏览器自动化 CLI |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | 微软出品的 [Playwright](https://playwright.dev) MCP 服务器，AI 浏览器控制 | vscode-extension, mcp | 微软出品<br>[Playwright](https://playwright.dev) MCP 服务器<br>33K Stars |
| [Nanobrowser](https://github.com/nanobrowser/nanobrowser) | 开源 Chrome 扩展，AI 多 Agent 网页自动化 | vscode-extension, agent | Chrome 扩展<br>AI 多 Agent 网页自动化<br>13K Stars |
| [Stagehand](https://github.com/browserbase/stagehand) | AI 网页交互工具，让 Agent 自然语言操控网页 | vscode-extension, chat, automation | AI 网页交互<br>自然语言操控<br>TypeScript 原生 |
| [OpenBrowser](https://github.com/ntegrals/openbrowser) | 让 AI Agent 浏览网页的自主工具包 | vscode-extension, agent, autonomous | 9.5K Stars<br>自主浏览<br>AI Agent 工具包 |
| [Camofox Browser](https://github.com/jo-inc/camofox-browser) | 隐身无头浏览器，绕过 Cloudflare 等反爬 | vscode-extension, security | 6.5K Stars<br>隐身浏览器<br>绕过反爬 |
| [Browser Agent](https://github.com/magnitudedev/browser-agent) | 视觉优先的开源浏览器 Agent | vscode-extension, multimodal, agent | 4.1K Stars<br>视觉优先<br>浏览器 Agent |

### 🖥️ 计算机使用

| 名称 | 简介 | 标签 | 亮点 |
| ------ | ------ | ------ | ------ |
| [UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | 字节跳动开源的多模态 AI Agent 桌面应用 | agent, multimodal, desktop | 字节跳动开源<br>多模态 AI Agent<br>36K Stars |
| [Anthropic Computer Use](https://anthropic.com) | Claude 屏幕操作能力，系统级自主控制 | agent, [anthropic](https://openai.com) | 屏幕理解与操作<br>系统级自主控制<br>Claude 原生能力 |
| [OpenAI Computer Use](https://openai.com) | [GPT-5.5](https://openai.com) 内置计算机使用能力 | agent, openai-compatible | [GPT-5.5](https://openai.com) 原生支持<br>屏幕理解与操作<br>多模态驱动 |

<!-- AUTOGEN_END -->
<!-- 以上内容由脚本自动生成 -->

---

## 💡 工具对比

| 维度 | [Browser Use](https://github.com/browser-use/browser-use) | [Agent Browser](https://github.com/vercel-labs/agent-browser) | [Nanobrowser](https://github.com/nanobrowser/nanobrowser) | Camofox | [Browser Agent](https://github.com/magnitudedev/browser-agent) |
| ------ | ------------- | --------------- | ------------- | --------- | --------------- |
| **Stars** | 97K | 35.5K | 13K | 6.5K | 4.1K |
| **开源** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **学习曲线** | 中 | 低 | 低 | 中 | 低 |
| **功能强度** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **稳定性** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **适用场景** | 复杂自动化 | CLI 自动化 | 简单任务 | 反爬 | 视觉操控 |

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
