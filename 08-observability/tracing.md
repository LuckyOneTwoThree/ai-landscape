# LLM 追踪与可观测性

> 最后更新：2026-06-08
> 数据来源：`data/observability.yaml` 自动生成

---

## 📊 LLM 追踪：让 AI 应用可观测

| 你的情况 | 推荐平台 | 理由 |
| --------- | --------- | ------ |
| **LangChain 生态** | [LangSmith](https://smith.langchain.com) | 官方追踪+评估 |
| **开源 / 私有部署** | [Langfuse](https://github.com/langfuse/langfuse) | MIT 开源，8K Stars |
| **AI 网关 + 追踪** | Portkey | 全链路追踪 |
| **OpenTelemetry 原生** | [OpenLIT](https://github.com/openlit/openlit) / [Langtrace](https://github.com/Scale3-Labs/langtrace) | 标准化追踪 |
| **Agent 可观测性** | [RagaAI Catalyst](https://github.com/raga-ai-hub/RagaAI-Catalyst) | 16K Stars |

> [!TIP]
> **Langfuse 是开源场景的最佳选择**
> 8K Stars，MIT 开源，支持追踪、评估、提示管理。可私有部署，数据不外流。

---

## 📋 LLM 追踪工具总览

<!-- AUTOGEN_START -->

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [RagaAI Catalyst](https://github.com/raga-ai-hub/RagaAI-Catalyst) | AI Agent 可观测性、监控与评估框架 | observability, data-analysis, agent | AI Agent 可观测性<br>监控+评估<br>16K Stars |
| [Langfuse](https://github.com/langfuse/langfuse) | 开源 LLM 工程平台，追踪、评估、提示管理 | observability, data-analysis, open-source | 开源 LLM 工程平台<br>追踪+评估+提示管理<br>8K Stars |
| [Helicone](https://github.com/Helicone/helicone) | 开源 LLM 可观测性平台，支持 OpenAI/Claude | observability, open-source | 开源 LLM 可观测性<br>6K Stars<br>OpenAI/Claude 支持 |
| [Pezzo](https://github.com/pezzolabs/pezzo) | 开源开发者优先的 LLMOps 平台，提示管理+追踪 | observability, automation | 3.2K Stars<br>开发者优先<br>提示管理+追踪 |
| [OpenLIT](https://github.com/openlit/openlit) | OpenTelemetry 原生的 LLM 可观测性平台 | observability, open-source | OpenTelemetry 原生<br>LLM 可观测性<br>2.5K Stars |
| [Langtrace](https://github.com/Scale3-Labs/langtrace) | 基于 OpenTelemetry 的 LLM 追踪工具 | observability, open-source | OpenTelemetry 追踪<br>1.2K Stars<br>轻量级 |
| [LangSmith](https://smith.langchain.com) | LangChain 官方的 LLM 应用追踪与评估平台 | observability, data-analysis, langchain | LangChain 官方<br>追踪+评估<br>LLM 应用平台 |

<!-- AUTOGEN_END -->

---

## 🏛️ 两大阵营

### 🔵 商业 SaaS 型：开箱即用

| 平台 | 核心优势 | 适合谁 |
| ------ | --------- | -------- |
| [**LangSmith**](https://smith.langchain.com) | LangChain 官方，追踪+评估 | LangChain 生态 |
| **Portkey** | AI 网关 + 全链路追踪 | 企业级 |
| [**Helicone**](https://github.com/Helicone/helicone) | 开源，请求日志/成本追踪 | 开发者 |

### 🟢 开源自部署型：数据在自己手里

| 平台 | Stars | 核心优势 | 适合谁 |
| ------ | ------- | --------- | -------- |
| [**Langfuse**](https://github.com/langfuse/langfuse) | 8K | MIT 开源，追踪+评估+提示管理 | 私有部署 |
| [**RagaAI Catalyst**](https://github.com/raga-ai-hub/RagaAI-Catalyst) | 16K | Agent 可观测性，监控+评估 | Agent 开发 |
| [**OpenLIT**](https://github.com/openlit/openlit) | 2.5K | OpenTelemetry 原生 | 标准化追踪 |
| [**Langtrace**](https://github.com/Scale3-Labs/langtrace) | 1.2K | OpenTelemetry 追踪 | 轻量级 |

## 💡 工具对比

| 维度 | [LangSmith](https://smith.langchain.com) | [Langfuse](https://github.com/langfuse/langfuse) | Portkey | [OpenLIT](https://github.com/openlit/openlit) |
| ------ | ----------- | ---------- | --------- | --------- |
| **开源** | ❌ | ✅ | ✅ | ✅ |
| **LangChain 集成** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **评估功能** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **提示管理** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **成本追踪** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
