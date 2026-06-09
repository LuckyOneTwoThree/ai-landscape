# API Gateway & Routing

> Last Updated: 2026-06-08
> Data Source: Automatically generated from `data/infrastructure.yaml`

---

## 💰 Why Use an API Gateway?

For individuals or small teams, the core problem an API gateway solves is **saving money**.

**Scenario**: Your Agent makes 1,000 LLM calls a day, of which 800 are simple Q&A and 200 are complex reasoning.

| Solution | **Simple Tasks 800 calls** | Complex Tasks (200 calls) | Daily Cost |
| ------ | **-----------------** | ----------------- | -------- |
| [**All GPT-5.5**](https://openai.com) | **800 × $0.015 = $12** | 200 × $0.075 = $15 | **$27** |
| **Routing: Simple via nano, complex via 5.5** | **800 × $0.001 = $0.8** | 200 × $0.075 = $15 | **$15.8** |

**Saves 41%**, and the quality of simple tasks experiences almost no degradation.

> [!TIP]
> **When is a gateway unnecessary?**
> - Using a single model provider → Call the API directly.
> - Call volume < 100 times/day → Not worth the setup overhead.
> - All tasks have similar complexity → No room for routing.

---

## 📋 API Gateway Overview

<!-- AUTOGEN_START -->

### 📱 Edge Inference

| Tool | Providers | Features | Core Highlights |
| ------ | ----------- | ------ | ---------- |
| [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/) | 10+ | Edge Routing, Rate Limiting, Caching | Low Latency on Edge Nodes<br>Multi-Provider Support<br>Rate Limiting / Logging |

### 🔀 Proxy

| Tool | Providers | Features | Core Highlights |
| ------ | ----------- | ------ | ---------- |
| ✅ [LiteLLM](https://github.com/BerriAI/litellm) | 100+ | Load Balancing, Fallbacks, Rate Limiting, Caching | Unified OpenAI Format<br>100+ Providers Supported<br>Load Balancing / Fallback |

### 📋 Management

| Tool | Providers | Features | Core Highlights |
| ------ | ----------- | ------ | ---------- |
| ✅ [OneAPI](https://github.com/songquanpeng/one-api) | 50+ | Rate Limiting, Billing, Key Distribution | Multi-channel Token Management<br>Azure/OpenAI/Domestic Models<br>Rate Limiting / Billing / Key Distribution |
| ✅ [CC Switch](https://github.com/farion1231/cc-switch) | ['Claude Code', '[Codex](https://openai.com)', 'Gemini CLI', 'OpenCode', 'Hermes Agent'] | Configuration Switching, Multi-tool Management, Cross-platform | Unified Claude Code/[Codex](https://openai.com)/Gemini Management<br>Cross-platform Desktop App<br>Built with Tauri 2 |

### 🔗 Aggregation

| Tool | Providers | Features | Core Highlights |
| ------ | ----------- | ------ | ---------- |
| ✅ [one-api](https://github.com/songquanpeng/one-api) | - | - | Multi-model Proxy for Domestic Providers<br>Billing System<br>37K Stars |
| [OpenRouter](https://openrouter.ai) | 200+ | Auto-routing, Pay-as-you-go | 200+ Models<br>Pay per Usage<br>Auto-routes to Optimal Provider |
| ✅ [new-api](https://github.com/QuantumNous/new-api) | 50+ | Aggregation & Distribution, Billing, Rate Limiting | Unified OpenAI-compatible API<br>Multi-model Aggregation<br>Preferred for Domestic Ecosystem |

### 🚪 Gateway

| Tool | Providers | Features | Core Highlights |
| ------ | ----------- | ------ | ---------- |
| ✅ [Portkey](https://portkey.ai) | 100+ | Observability, Retries, Guardrails, A/B | Observability<br>Auto-retries / Fallback<br>Guardrails / Caching |
| ✅ [Kong](https://github.com/Kong/kong) | ['General API + AI Plugins'] | Rate Limiting, Load Balancing, Plugins, Observability | Enterprise API Gateway Standard<br>AI Plugin Ecosystem<br>High Performance / High Availability |
| ✅ [Higress](https://github.com/higress-group/higress) | ['Domestic Models + International Models'] | AI Routing, Rate Limiting, Caching, Wasm Plugins | Developed by Alibaba Cloud<br>AI-native Design<br>Envoy Foundation |

<!-- AUTOGEN_END -->

---

## 🔄 Multi-Model Routing in Practice

**Core Idea**: Automatically select a model based on task complexity.

| Task Type | Recommended Model | Pricing (Input/Output) |
| --------- | --------- | ----------------- |
| **Daily Conversations / Simple Q&A** | GPT-5.4-nano / [DeepSeek-V4-Flash](https://deepseek.com) | $0.10 / $0.40 |
| **Code Generation / Documentation Drafting** | GPT-5.4-mini / [Claude Haiku 4](https://anthropic.com) | $0.40 / $1.60 |
| **Complex Reasoning / System Design** | [GPT-5.5](https://openai.com) / [Claude Opus 4](https://anthropic.com) | $5.00 / $25.00 |

**Implementing Routing with LiteLLM**:
```python
# pip install litellm
from litellm import completion

def smart_route(prompt: str, complexity: str = "simple"):
    """Select model based on task complexity."""
    models = {
        "simple": "deepseek/deepseek-chat",   # $0.07/MTok
        "medium": "gpt-5.4-mini",             # $0.40/MTok
        "complex": "gpt-5.5",                 # $5.00/MTok
    }
    return completion(
        model=models[complexity],
        messages=[{"role": "user", "content": prompt}]
    )

# Simple task → Cheaper model
smart_route("What's the weather like today?", "simple")

# Complex task → Flagship model
smart_route("Design a distributed task scheduling system", "complex")
```

> [!TIP]
> **Caching is the ultimate cost-saver**
> If your Agent has a large amount of repetitive Context (like system prompts), enabling Prompt Caching can cut your monthly bill by 50-80%. DeepSeek's cache hit price is just $0.004/MTok, which is 17 times cheaper than direct calls.

## 🌏 Tool Quick Reference

| Tool | Stars | Positioning | Best For |
| ------ | ------- | ------ | -------- |
| [**CC Switch**](https://github.com/farion1231/cc-switch) | 94K | Desktop AI Model Management | Local experiments, model comparison |
| [**one-api**](https://github.com/songquanpeng/one-api) | 37K | Multi-model Unified Proxy | Domestic teams, multi-provider setups |
| [**new-api**](https://github.com/QuantumNous/new-api) | 37K | Enhanced version of [one-api](https://github.com/songquanpeng/one-api) | Users needing advanced features |
| [**LiteLLM**](https://github.com/BerriAI/litellm) | 15K | AI Multi-model Proxy | Developers, custom routing builds |
| [**OpenRouter**](https://openrouter.ai) | — | Cloud-based Multi-model Routing | Those avoiding self-hosting, pay-as-you-go |
| [**Higress**](https://github.com/higress-group/higress) | 8.5K | Alibaba Cloud-native Gateway | Alibaba Cloud users |
| [**Kong**](https://github.com/Kong/kong) | 43K | Enterprise API Gateway | Hybrid traditional API + AI setups |

---

> **Update Frequency**: Updated quarterly
> **Automation**: Run `python scripts/build_docs.py` to re-render tables from YAML.
