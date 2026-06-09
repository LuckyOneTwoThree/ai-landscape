# 语言大模型

> 最后更新：2026-06-08
> 数据来源：各主流厂商官方文档实时抓取 + `data/models.yaml` 自动生成

---

## 🧭 旗舰大模型选型罗盘

面对 2026 年爆发式增长的模型矩阵，单纯对比参数已失去意义。我们总结了针对不同落地场景的最佳实战选型建议：

| 业务场景 / 架构需求 | 闭源旗舰 (性能天花板) | 开源基座 (私有化) | 极速低成本选项 | 特殊维度与极客备选 |
|---------------------|-----------------------|-------------------|----------------|--------------------|
| **代码重构与系统设计** | **Claude Opus 4**<br>(全局重构最优) | **DeepSeek-V4-Pro**<br>**MiMo-V2.5-Pro** | Claude Sonnet 4<br>Qwen3-Coder | **Mistral Large 3**<br>(主打远程工作流集成) |
| **高频 Agent 与 API 调用** | **GPT-5.5 Instant** | **MiMo-V2.5**<br>**Qwen3-235B** | **DeepSeek-V4-Flash**<br>(每百万Token低于$0.1) | Gemini 3.5 Flash |
| **强逻辑推理与数学计算** | **o3** | **DeepSeek-V4-Pro** | Phi-4 | **DeepSeek-R1**<br>**MiMo-7B-RL** (端侧) |
| **超大规模文档与财报解析** | **Gemini 3.5 Pro** | **Llama 4 Scout (10M)** | Kimi K2-6 (长程优化) | Claude Sonnet 4 (1M) |
| **全模态交互与原生语音视觉** | **GPT-5.5 Pro** | **GLM-5.1**<br>**混元 HY3** | MiniMax M3 | - |

> [!TIP]
> **关于 1M+ 超长上下文的落地警示**
> 尽管模型厂商均标榜百万上下文，但在实际生产中，将全量代码丢入 Context 依然会引发"大海捞针"般的注意力衰减并消耗巨大 API 成本。**高级 RAG + 128K 窗口依然是构建企业级应用的最优解。**

---

## 📋 通用对话型模型总览

<!-- 以下内容由脚本自动生成，请勿手动修改 -->
<!-- AUTOGEN_START -->

### 🌏 海外模型

| 模型与版本 | 核心参数 (上下文/输出) | 价格 (入/出) | 核心亮点 | 部署方式 |
|------------|------------------------|--------------|----------|----------|
| 🌏 [GPT-5.5 Pro / Thinking<br>*(API: `gpt-5.5-pro-20260423`)*](https://openai.com) | **In**: 1M<br>**Out**: 128K | $5/$30 | 1M 上下文 + 128K 输出<br>Computer Use 原生支持<br>多级推理 (low/medium/high/xhigh) | ☁️ 商业 API / 闭源 |
| 🌏 [GPT-5.4](https://openai.com) | **In**: 128K<br>**Out**: 32K | $2/$8 | 高性价比编码模型<br>$2/MTok 输入 | ☁️ 商业 API / 闭源 |
| 🌏 [GPT-5.5 Instant<br>*(API: `gpt-5.5-instant-20260505`)*](https://openai.com) | **In**: 128K<br>**Out**: 32K | $0.4/$1.6 | 日常任务高频使用<br>极低延迟与推理成本 | ☁️ 商业 API / 闭源 |
| 🌏 [GPT-5.4-nano](https://openai.com) | **In**: 128K<br>**Out**: 32K | $0.1/$0.4 | 超低延迟<br>极低成本 | ☁️ 商业 API / 闭源 |
| 🌏 [Claude Opus 4.8<br>*(API: `claude-4-8-opus-20260528`)*](https://anthropic.com) | **In**: 1M<br>**Out**: 128K | $5/$25 | 1M 上下文 + 128K 输出<br>扩展+自适应推理<br>编码能力标杆 | ☁️ 商业 API / 闭源 |
| 🌏 [Claude Sonnet 4.6<br>*(API: `claude-4-6-sonnet-20260215`)*](https://anthropic.com) | **In**: 1M<br>**Out**: 64K | $3/$15 | 1M 上下文 + 64K 输出<br>性价比最高<br>开发者首选 | ☁️ 商业 API / 闭源 |
| 🌏 [Claude Haiku 4.5<br>*(API: `claude-4-5-haiku-20251022`)*](https://anthropic.com) | **In**: 200K<br>**Out**: 8K | $1/$5 | 200K 上下文<br>极低延迟<br>$1/$5 per MTok | ☁️ 商业 API / 闭源 |
| 🌏 [Gemini 3.5 Pro<br>*(API: `gemini-3.5-pro`)*](https://gemini.google.com) | **In**: 2M<br>**Out**: 128K | 未公布 | 2M 超长上下文<br>原生多模态与Deep Think | ☁️ 商业 API / 闭源 |
| 🌏 [Gemini 3.5 Flash<br>*(API: `gemini-3.5-flash`)*](https://gemini.google.com) | **In**: 1M<br>**Out**: 64K | 未公布 | 高频次Agent调用<br>高性价比多模态 | ☁️ 商业 API / 闭源 |
| 🌏 [Grok 4](https://x.ai) | **In**: 128K<br>**Out**: 32K | 未公布 | 实时全网搜索<br>Imagine API 图像生成<br>Voice API | ☁️ 商业 API / 闭源 |
| 🌏 [Cohere Command R3](https://cohere.com) | **In**: 128K<br>**Out**: 8K | $2.5/$10 | 最高效的 RAG 召回<br>Citation 原生支持<br>企业级 | ☁️ 商业 API / 闭源 |
| 🌏 [Mistral Vibe<br>*(API: `mistral-vibe`)*](https://mistral.ai) | **In**: 256K<br>**Out**: 8K | 商业调用定价 | 原生支持 Work Mode<br>专研远程编码集成<br>替代 Le Chat 成为主力 | ☁️ 商业 API / 闭源 |
| 🌏 [Llama 4 Maverick](https://ai.meta.com/llama/) | **In**: 1M<br>**Out**: 32K | 开源自部署 | 400B MoE<br>1M 上下文<br>多模态 | ✅ 开源可部署<br>`Llama 4` |
| 🌏 [Llama 4 Scout](https://ai.meta.com/llama/) | **In**: 10M<br>**Out**: 32K | 开源自部署 | 109B MoE<br>10M 超长上下文<br>vLLM 部署 | ✅ 开源可部署<br>`Llama 4` |
| 🌏 [Gemma 3](https://blog.google/technology/ai/) | **In**: 128K<br>**Out**: 8K | 开源自部署 | 1B-27B 多规格<br>128K 上下文<br>多模态 | ✅ 开源可部署<br>`Gemma` |
| 🌏 [Phi-4](https://azure.microsoft.com/en-us/products/phi) | **In**: 16K<br>**Out**: 16K | 开源自部署 | 14B 参数<br>数学推理极强<br>端侧部署 | ✅ 开源可部署<br>`MIT` |
| 🌏 [Mistral Large 3<br>*(API: `mistral-large-3`)*](https://mistral.ai) | **In**: 256K<br>**Out**: 8K | 开源自部署 | 675B MoE (41B 激活)<br>256K 超长上下文<br>原生多模态支持 | ✅ 开源可部署<br>`Apache-2.0` |

### 🏯 国内模型

| 模型与版本 | 核心参数 (上下文/输出) | 价格 (入/出) | 核心亮点 | 部署方式 |
|------------|------------------------|--------------|----------|----------|
| 🏯 [GLM-5.1](https://open.bigmodel.cn) | **In**: 128K<br>**Out**: 16K | 未公布 | 智谱最新旗舰<br>全模态 (文本/视觉/图像/视频/语音)<br>GLM-5 系列最新 | ☁️ 商业 API / 闭源 |
| 🏯 [Kimi K2-6](https://platform.moonshot.cn) | **In**: 128K<br>**Out**: 16K | 未公布 | 超强长上下文<br>强化的代码推理<br>Agent 自主执行 | ☁️ 商业 API / 闭源 |
| 🏯 [DeepSeek-V4-Pro<br>*(API: `deepseek-v4-pro`)*](https://deepseek.com) | **In**: 1M<br>**Out**: 384K | $0.435/$0.87 | 1.6T MoE (49B 激活)<br>1M 上下文, thinking 模式<br>384K 输出 | ✅ 开源可部署<br>`Proprietary` |
| 🏯 [DeepSeek-V4-Flash<br>*(API: `deepseek-v4-flash`)*](https://deepseek.com) | **In**: 1M<br>**Out**: 64K | $0.07/$0.28 | 284B MoE (13B 激活)<br>1M 上下文<br>极低成本 $0.004 cache hit | ✅ 开源可部署<br>`Proprietary` |
| 🏯 [MiniMax M3](https://minimaxi.com) | **In**: 1M<br>**Out**: 64K | 未公布 | MSA 架构<br>1M 上下文<br>Coding/Agentic 前沿 | ☁️ 商业 API / 闭源 |
| 🏯 [腾讯混元 HY3](https://cloud.tencent.com/product/hunyuan) | **In**: 256K<br>**Out**: 16K | 免费/低价 | 文本/图像/视频/3D 全模态<br>MoE 架构 | ☁️ 商业 API / 闭源 |
| 🏯 [Qwen3.7-Plus<br>*(API: `qwen3.7-plus`)*](https://bailian.aliyun.com/) | **In**: 128K<br>**Out**: 8K | 商业调用定价 | 专精 GUI 导航与屏幕感知<br>AndroidWorld 霸榜<br>纯 API 商业调用 | ☁️ 商业 API / 闭源 |
| 🏯 [Qwen3.7-Max<br>*(API: `qwen3.7-max`)*](https://bailian.aliyun.com/) | **In**: 128K<br>**Out**: 8K | 商业调用定价 | 极致的中文与逻辑推理<br>长程上下文强关联 | ☁️ 商业 API / 闭源 |
| 🏯 [Qwen3-Coder-480B](https://qwen.ai) | **In**: 128K<br>**Out**: 16K | 开源自部署 | 480B MoE 代码专精<br>开源代码模型标杆 | ✅ 开源可部署<br>`Apache-2.0` |
| 🏯 [ERNIE (文心一言)](https://yiyan.baidu.com) | **In**: 128K<br>**Out**: 8K | 免费/低价 | 千帆 Agent 平台<br>MCP 支持<br>百度搜索增强 | ☁️ 商业 API / 闭源 |
| 🏯 [百川 M3 Plus](https://www.baichuan-ai.com) | **In**: 128K<br>**Out**: 8K | 免费 | 免费使用<br>中文优化 | ☁️ 商业 API / 闭源 |
| 🏯 [讯飞星火 4.0](https://xinghuo.xfyun.cn) | **In**: 128K<br>**Out**: 8K | 免费/低价 | 教育场景优化<br>语音能力突出 | ☁️ 商业 API / 闭源 |
| 🏯 [Step 3](https://platform.stepfun.com) | **In**: 128K<br>**Out**: 16K | 未公布 | Step Router 智能路由<br>Pro+Flash 双引擎 | ☁️ 商业 API / 闭源 |
| 🏯 [DeepSeek-R1](https://deepseek.com) | **In**: 128K<br>**Out**: 64K | 开源自部署 | 671B MoE<br>开源推理标杆<br>MIT 许可 | ✅ 开源可部署<br>`MIT` |
| 🏯 [MiMo-V2.5-Pro<br>*(API: `mimo-v2.5-pro`)*](https://mimo.xiaomi.com) | **In**: 1M<br>**Out**: 64K | 开源自部署 / API调用 | 1.02T 参数 MoE 架构<br>1M 超长上下文支持<br>Agent/Coding 开源综合第一 | ✅ 开源可部署<br>`MIT` |
| 🏯 [MiMo-V2.5 (基础版)](https://mimo.xiaomi.com) | **In**: 128K<br>**Out**: 16K | 开源自部署 | Agent 能力前沿<br>Pro/Omni/Flash 多版本<br>开源 | ✅ 开源可部署<br>`Apache-2.0` |
| 🏯 [MiMo-7B-RL](https://mimo.xiaomi.com) | **In**: 128K<br>**Out**: 16K | 开源自部署 | 7B 参数<br>AIME 2024: 80.1 超 DeepSeek R1<br>小模型推理标杆 | ✅ 开源可部署<br>`Apache-2.0` |
| 🏯 [MiniCPM4-8B](https://github.com/OpenBMB/MiniCPM) | **In**: 128K<br>**Out**: 8K | 开源自部署 | 8B 端侧部署<br>Apache 2.0<br>Ollama 支持 | ✅ 开源可部署<br>`Apache-2.0` |

<!-- AUTOGEN_END -->
<!-- 以上内容由脚本自动生成 -->

---

## ⚡ 推理能力速查

| 能力维度 | 顶级闭源 | 顶级开源 | 端侧小模型 |
|---------|---------|---------|-----------|
| **数学推理** | o3 | DeepSeek-R1 | MiMo-7B-RL |
| **代码生成** | Claude Opus 4 | Qwen3-Coder-480B | Phi-4 |
| **Agent 执行** | GPT-5.5 | MiMo-V2.5-Pro | — |
| **长上下文** | Gemini 3.5 (2M) | Llama 4 Scout (10M) | — |
| **中文能力** | — | DeepSeek-V4 / Qwen3 | MiniCPM4-8B |
| **多模态** | GPT-5.5 Pro | GLM-5.1 | — |

---

> **更新频率**：每季度更新，重大发布即时更新。
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
