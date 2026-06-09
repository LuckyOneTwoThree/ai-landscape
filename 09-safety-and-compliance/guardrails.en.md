# AI Guardrails and Security Protection

> Last Updated: 2026-06-08
> Data Source: Generated automatically from `data/safety-and-compliance.yaml`

---

## 🛡️ AI Guardrails: Securing LLMs

| Your Situation | **Recommended Solution** | Reason |
| --------- | **---------** | ------ |
| **Programmable Rules** | **NeMo Guardrails** | By NVIDIA, 6.4K Stars |
| **Output Validation** | **Guardrails AI** | Auto-correction, 5K Stars |
| **Prompt Injection Protection** | **Superagent / Rebuff AI** | Injection/Data leak prevention |
| **Content Safety Classification** | **Llama Guard** | By Meta |

> [!TIP]
> **NeMo Guardrails is the premier choice for enterprise-grade guardrails**
> Developed by NVIDIA, it supports programmable rules, allowing you to define what the LLM can and cannot say.

---

## 📋 AI Guardrails Tools Overview

<!-- AUTOGEN_START -->

| Name | Description | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | LLM guardrails toolkit by NVIDIA, programmable rules | security, gpu-acceleration, automation | By NVIDIA<br>Programmable rules<br>6.4K Stars |
| [Guardrails AI](https://github.com/guardrails-ai/guardrails) | Open-source LLM output validation and correction framework | security, compliance, open-source | Open-source output validation<br>Auto-correction<br>100+ community validators |
| [Rebuff AI](https://github.com/protectai/rebuff) | Self-healing protection framework for prompt injection detection | security, automation | Self-healing protection<br>Prompt injection detection<br>1.5K Stars |
| [Prompt Armor](https://promptarmor.com) | Prompt injection detection and protection tool | security | Prompt injection detection<br>Protection tool<br>Enterprise-grade |
| [Lakera Guard](https://www.lakera.ai/lakera-guard) | Real-time prompt injection protection API, sub-50ms latency | security, real-time, enterprise | Real-time protection (50ms latency)<br>100+ languages 98% accuracy<br>Acquired by Check Point |

<!-- AUTOGEN_END -->

---

## 🏛️ Guardrail Classification

### 🔵 Programmable Rules

| Tool | Stars | Core Advantage | Best For |
| ------ | ------- | --------- | -------- |
| [**NeMo Guardrails**](https://github.com/NVIDIA/NeMo-Guardrails) | 6.4K | By NVIDIA, programmable rules | Enterprise |
| [**Guardrails AI**](https://guardrailsai.com) | 5K | Open-source output validation, auto-correction | Developers |

### 🟢 Prompt Injection Protection

| Tool | Stars | Core Advantage | Best For |
| ------ | ------- | --------- | -------- |
| [**Superagent**](https://superagent.sh) | 6.6K | Injection/Data leak prevention | Enterprise |
| [**Rebuff AI**](https://rebuff.ai) | 1.5K | Self-healing protection | Developers |

### 🟡 Content Safety Classification

| Tool | Stars | Core Advantage | Best For |
| ------ | ------- | --------- | -------- |
| [**Llama Guard**](https://ai.meta.com/llama/) | 3K | By Meta, content safety classification | Content Moderation |
| [**OpenAI Moderation**](https://platform.openai.com/docs/guides/moderation) | - | Built-in OpenAI, free | OpenAI Users |

## 💡 Guardrail Strategies

| Strategy | Implementation | Best For |
| ------ | --------- | --------- |
| **Input Filtering** | Prompt injection detection | All scenarios |
| **Output Validation** | Structured output validation | Data processing |
| **Content Moderation** | Safety classification model | User interactions |
| **Rule Engine** | Programmable rules | Enterprise |

> [!TIP]
> **Best Practice: Multi-Layer Protection**
> 1. **Input Layer**: Prompt injection detection (Superagent)
> 2. **Processing Layer**: Programmable rules (NeMo Guardrails)
> 3. **Output Layer**: Content moderation (Llama Guard)

---

> **Update Frequency**: Quarterly
> **Automation**: Run `python scripts/build_docs.py` to re-render tables from YAML.
