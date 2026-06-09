# Content Moderation

> Last Updated: 2026-06-08
> Data Source: Generated automatically from `data/safety-and-compliance.yaml`

---

## 🔍 Content Moderation: Securing AI Outputs

| Your Situation | **Recommended Solution** | Reason |
| --------- | --------- | ------ |
| **OpenAI User** | **[OpenAI Moderation](https://platform.openai.com/docs/guides/moderation)** | Built-in, free |
| **Open Source** | **[Llama Guard](https://ai.meta.com/llama/)** | By Meta, 3K Stars |
| **Enterprise** | **[NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)** | Programmable rules |

> [!TIP]
> **OpenAI Moderation is the simplest solution**
> If you are using the OpenAI API, utilize the built-in Moderation endpoint directly. It is free and requires no additional deployment.

---

## 📋 Content Moderation Tools Overview

<!-- AUTOGEN_START -->

| Name | Description | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [Llama Guard](https://github.com/meta-llama/PurpleLlama) | Content safety classification model by Meta | security, open-source, data-analysis | By Meta<br>Content safety classification<br>3K Stars |
| [OpenAI Moderation](https://platform.openai.com/docs/guides/moderation) | Built-in content moderation API by OpenAI | security, openai-compatible, api-gateway | Built-in OpenAI<br>Content moderation API<br>Free |

<!-- AUTOGEN_END -->

---

## 🏛️ Moderation Methods

### 🔵 API Service

| Tool | Core Advantage | Best For |
| ------ | --------- | -------- |
| [**OpenAI Moderation**](https://platform.openai.com/docs/guides/moderation) | Built-in, free | OpenAI Users |

### 🟢 Open-Source Model

| Tool | Stars | Core Advantage | Best For |
| ------ | ------- | --------- | -------- |
| [**Llama Guard**](https://ai.meta.com/llama/) | 3K | By Meta, content safety classification | Content Moderation |

### 🟡 Programmable Rules

| Tool | Stars | Core Advantage | Best For |
| ------ | ------- | --------- | -------- |
| [**NeMo Guardrails**](https://github.com/NVIDIA/NeMo-Guardrails) | 6.4K | By NVIDIA, programmable rules | Enterprise |

## 💡 Moderation Dimensions

| Dimension | Description | Tool Support |
| ------ | ------ | --------- |
| **Violence** | Violence detection | OpenAI, [Llama Guard](https://ai.meta.com/llama/) |
| **Pornography** | Pornographic content detection | OpenAI, [Llama Guard](https://ai.meta.com/llama/) |
| **Hate Speech** | Hate speech detection | OpenAI, [Llama Guard](https://ai.meta.com/llama/) |
| **Self-Harm** | Self-harm content detection | OpenAI |
| **Prompt Injection** | Injection attack detection | [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) |

---

> **Update Frequency**: Quarterly
> **Automation**: Run `python scripts/build_docs.py` to re-render tables from YAML.
