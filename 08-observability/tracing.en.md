# LLM Tracing and Observability

> Last Updated: 2026-06-08
> Data Source: Automatically generated from `data/observability.yaml`

---

## 📊 LLM Tracing: Making AI Applications Observable

| Your Situation | Recommended Platform | Reason |
| --------- | --------- | ------ |
| **LangChain Ecosystem** | [LangSmith](https://smith.langchain.com) | Official tracing + evaluation |
| **Open Source / Private Deployment** | [Langfuse](https://langfuse.com) | MIT open-source, 8K Stars |
| **AI Gateway + Tracing** | [Portkey](https://portkey.ai) | Full-link tracing |
| **OpenTelemetry Native** | [OpenLIT](https://openlit.io) / [Langtrace](https://langtrace.ai) | Standardized tracing |
| **Agent Observability** | [RagaAI Catalyst](https://raga.ai) | 16K Stars |

> [!TIP]
> **Langfuse is the best choice for open-source scenarios**
> With 8K Stars and an MIT license, it supports tracing, evaluation, and prompt management. It can be self-hosted to ensure data privacy.

---

## 📋 LLM Tracing Tools Overview

<!-- AUTOGEN_START -->

| Name | Introduction | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [RagaAI Catalyst](https://github.com/raga-ai-hub/RagaAI-Catalyst) | AI Agent observability, monitoring, and evaluation framework | observability, data-analysis, agent | AI Agent observability<br>Monitoring + Evaluation<br>16K Stars |
| [Langfuse](https://github.com/langfuse/langfuse) | Open-source LLM engineering platform: tracing, evaluation, prompt management | observability, data-analysis, open-source | Open-source LLM platform<br>Tracing+Evaluation+Prompt Mgmt<br>8K Stars |
| [Helicone](https://github.com/Helicone/helicone) | Open-source LLM observability platform, supports OpenAI/Claude | observability, open-source | Open-source LLM observability<br>6K Stars<br>OpenAI/Claude support |
| [Pezzo](https://github.com/pezzolabs/pezzo) | Open-source developer-first LLMOps platform, prompt management + tracing | observability, automation | 3.2K Stars<br>Developer-first<br>Prompt Mgmt + Tracing |
| [OpenLIT](https://github.com/openlit/openlit) | OpenTelemetry-native LLM observability platform | observability, open-source | OpenTelemetry-native<br>LLM observability<br>2.5K Stars |
| [Langtrace](https://github.com/Scale3-Labs/langtrace) | LLM tracing tool based on OpenTelemetry | observability, open-source | OpenTelemetry tracing<br>1.2K Stars<br>Lightweight |
| [LangSmith](https://smith.langchain.com) | LangChain's official LLM application tracing and evaluation platform | observability, data-analysis, langchain | Official LangChain<br>Tracing + Evaluation<br>LLM app platform |

<!-- AUTOGEN_END -->

---

## 🏛️ Two Major Camps

### 🔵 Commercial SaaS: Out-of-the-Box

| Platform | Core Advantage | Best For |
| ------ | --------- | -------- |
| [**LangSmith**](https://smith.langchain.com) | Official LangChain, tracing + evaluation | LangChain ecosystem |
| [**Portkey**](https://portkey.ai) | AI Gateway + full-link tracing | Enterprise-grade |
| [**Helicone**](https://github.com/Helicone/helicone) | Open-source, request logs/cost tracing | Developers |

### 🟢 Open-Source Self-Hosted: Keep Data in Your Hands

| Platform | Stars | Core Advantage | Best For |
| ------ | ------- | --------- | -------- |
| [**Langfuse**](https://langfuse.com) | 8K | MIT open-source, tracing+eval+prompt mgmt | Private deployment |
| [**RagaAI Catalyst**](https://raga.ai) | 16K | Agent observability, monitoring+eval | Agent development |
| [**OpenLIT**](https://openlit.io) | 2.5K | OpenTelemetry native | Standardized tracing |
| [**Langtrace**](https://langtrace.ai) | 1.2K | OpenTelemetry tracing | Lightweight |

## 💡 Tool Comparison

| Dimension | [LangSmith](https://smith.langchain.com) | [Langfuse](https://langfuse.com) | [Portkey](https://portkey.ai) | [OpenLIT](https://openlit.io) |
| ------ | ----------- | ---------- | --------- | --------- |
| **Open Source** | ❌ | ✅ | ✅ | ✅ |
| **LangChain Integration** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Evaluation Features** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Prompt Management** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Cost Tracing** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |

---

> **Update Frequency**: Updated quarterly
> **Automation**: Run `python scripts/build_docs.py` to re-render tables from YAML.
