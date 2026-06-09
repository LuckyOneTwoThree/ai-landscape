# Browser Control

> Last Updated: 2026-06-08
> Data Source: Automatically generated from `data/tools.yaml`

---

## 🧭 Browser Control Selection Compass

| Your Situation | **Recommended Tool** | Reason |
| --------- | **---------** | ------ |
| **Complex Web Automation (Login/Forms/Clicks)** | **Browser Use** | 97K Stars, DOM parsing + visual recognition, most powerful |
| **Cross-Browser Testing/Automation** | **Playwright** | By Microsoft, full support for Chromium/Firefox/WebKit |
| **Command Line Automation Scripts** | **Agent Browser** | By [Vercel](https://vercel.com), CLI format, lightweight and easy to integrate |
| **Chrome Extension Format** | **Nanobrowser** | Browser plugin, no extra installation, multi-agent collaboration |
| **Bypass Anti-Bot/Cloudflare** | **Camofox Browser** | Stealth headless browser, designed to bypass anti-bot detection |
| **Vision-First, Screenshots + Coordinates** | **Browser Agent** | Screenshots + coordinate clicks, suitable for general Agents |
| **System-Level Screen Control** | **Anthropic / OpenAI Computer Use** | Not limited to browsers, can control any desktop application |

> [!TIP]
> **Browser Use is the best choice for browser control in 2026**
> 97K Stars, equips AI Agents with complete autonomous browser operation capabilities. Combined with the Playwright backend, it supports complex operations like login, form filling, and clicking, with MCP Server integration.

## ⚡ Minimalist Practice: Let AI Surf the Web Itself (Using Browser Use as an Example)

In 2026, controlling a browser doesn't require manually writing tedious XPath or CSS selectors. Vision models will "see" the screen and click on their own. It only takes less than 10 lines of code:

```python
from browser_use import Agent
import asyncio

async def main():
    # Just give it a goal, it will automatically open the browser, search, click, and even scroll the page
    agent = Agent(task="Go to Github to search for AI Landscape projects, find the top three repositories and tell me their names")
    await agent.run()

asyncio.run(main())
```

---

## 📋 Browser Control Tools Overview

<!-- 以下内容由脚本自动生成，请勿手动修改 -->
<!-- AUTOGEN_START -->

### 🌐 Browser

| Name | Description | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [Browser Use](https://github.com/browser-use/browser-use) | Equips LLMs with complete autonomous browser operation capabilities, combined with [Playwright](https://playwright.dev) and other backends | vscode-extension, automation, mcp | DOM parsing combined with visual recognition<br>Significantly enhances Agent's internet interaction capabilities<br>MCP Server integration |
| [Playwright](https://playwright.dev) | Cross-browser automation framework by Microsoft, MCP Server support | vscode-extension, automation, mcp | By Microsoft<br>Cross-browser (Chromium/Firefox/WebKit)<br>MCP Server support<br>70K+ Stars |
| [Agent Browser](https://github.com/vercel-labs/agent-browser) | AI [Agent browser](https://github.com/vercel-labs/agent-browser) automation CLI by [Vercel](https://vercel.com) | vscode-extension, agent, automation, cloud-only | 35.5K Stars<br>By [Vercel](https://vercel.com)<br>Browser automation CLI |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp) | [Playwright](https://playwright.dev) MCP server by Microsoft, AI browser control | vscode-extension, mcp | By Microsoft<br>[Playwright](https://playwright.dev) MCP server<br>33K Stars |
| [Nanobrowser](https://github.com/nanobrowser/nanobrowser) | Open-source Chrome extension, AI multi-agent web automation | vscode-extension, agent | Chrome extension<br>AI multi-agent web automation<br>13K Stars |
| [Stagehand](https://github.com/browserbase/stagehand) | AI web interaction tool, lets Agents control web pages with natural language | vscode-extension, chat, automation | AI web interaction<br>Natural language control<br>TypeScript native |
| [OpenBrowser](https://github.com/ntegrals/openbrowser) | Autonomous toolkit for AI Agents to browse the web | vscode-extension, agent, autonomous | 9.5K Stars<br>Autonomous browsing<br>AI Agent toolkit |
| [Camofox Browser](https://github.com/jo-inc/camofox-browser) | Stealth headless browser, bypasses anti-bot like Cloudflare | vscode-extension, security | 6.5K Stars<br>Stealth browser<br>Bypasses anti-bot |
| [Browser Agent](https://github.com/magnitudedev/browser-agent) | Vision-first open-source [browser Agent](https://github.com/magnitudedev/browser-agent) | vscode-extension, multimodal, agent | 4.1K Stars<br>Vision-first<br>[Browser Agent](https://github.com/magnitudedev/browser-agent) |

### 🖥️ Computer Use

| Name | Description | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | Multimodal AI Agent desktop application open-sourced by ByteDance | agent, multimodal, desktop | Open-sourced by ByteDance<br>Multimodal AI Agent<br>36K Stars |
| [Anthropic Computer Use](https://anthropic.com) | Claude screen operation capability, system-level autonomous control | agent, [anthropic](https://openai.com) | Screen understanding and operation<br>System-level autonomous control<br>Claude native capability |
| [OpenAI Computer Use](https://openai.com) | Built-in computer use capability in [GPT-5.5](https://openai.com) | agent, openai-compatible | [GPT-5.5](https://openai.com) native support<br>Screen understanding and operation<br>Multimodal driven |

<!-- AUTOGEN_END -->
<!-- 以上内容由脚本自动生成 -->

---

## 💡 Tool Comparison

| Dimension | [Browser Use](https://github.com/browser-use/browser-use) | [Agent Browser](https://github.com/vercel-labs/agent-browser) | [Nanobrowser](https://github.com/nanobrowser/nanobrowser) | Camofox | [Browser Agent](https://github.com/magnitudedev/browser-agent) |
| ------ | ------------- | --------------- | ------------- | --------- | --------------- |
| **Stars** | 97K | 35.5K | 13K | 6.5K | 4.1K |
| **Open Source** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Learning Curve** | Medium | Low | Low | Medium | Low |
| **Feature Strength** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Stability** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Use Cases** | Complex automation | CLI automation | Simple tasks | Anti-bot | Visual control |

---

> **Update Frequency**: Updated quarterly
> **Automation**: Run `python scripts/build_docs.py` to re-render tables from YAML.
