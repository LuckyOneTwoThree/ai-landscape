# API 网关与路由

> 最后更新：2026-06-08
> 数据来源：`data/infrastructure.yaml` 自动生成

---

## 💰 为什么要用 API 网关？

对个人/小团队来说，API 网关解决的核心问题是**省钱**。

**场景**：你的 Agent 一天调用 1000 次 LLM，其中 800 次是简单问答，200 次是复杂推理。

| 方案 | 简单任务 (800次) | 复杂任务 (200次) | 日成本 |
| ------ | ----------------- | ----------------- | -------- |
| [**全用 GPT-5.5**](https://openai.com) | 800 × $0.015 = $12 | 200 × $0.075 = $15 | **$27** |
| **路由：简单用 nano，复杂用 5.5** | 800 × $0.001 = $0.8 | 200 × $0.075 = $15 | **$15.8** |

**省了 41%**，而且简单任务的质量几乎没有下降。

> [!TIP]
> **什么时候不需要网关？**
> - 只用一个模型供应商 → 直接调 API
> - 一天调用量 < 100 次 → 不值得折腾
> - 所有任务复杂度差不多 → 没有路由空间

---

## 📋 API 网关总览

<!-- AUTOGEN_START -->

### 📱 端侧推理

| 工具 | Provider数 | 功能 | 核心亮点 |
| ------ | ----------- | ------ | ---------- |
| [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/) | 10+ | 边缘路由, 限流, 缓存 | 边缘节点低延迟<br>多 Provider 支持<br>限流/日志 |

### 🔀 代理

| 工具 | Provider数 | 功能 | 核心亮点 |
| ------ | ----------- | ------ | ---------- |
| ✅ [LiteLLM](https://github.com/BerriAI/litellm) | 100+ | 负载均衡, 故障转移, 限流, 缓存 | 统一 OpenAI 格式<br>100+ Provider 支持<br>负载均衡/故障转移 |

### 📋 管理

| 工具 | Provider数 | 功能 | 核心亮点 |
| ------ | ----------- | ------ | ---------- |
| ✅ [OneAPI](https://github.com/songquanpeng/one-api) | 50+ | 限流, 计费, 密钥分发 | 多渠道 Token 管理<br>Azure/OpenAI/国产模型<br>限流/计费/密钥分发 |
| ✅ [CC Switch](https://github.com/farion1231/cc-switch) | ['Claude Code', '[Codex](https://openai.com)', 'Gemini CLI', 'OpenCode', 'Hermes Agent'] | 配置切换, 多工具管理, 跨平台 | Claude Code/[Codex](https://openai.com)/Gemini 统一管理<br>跨平台桌面应用<br>Tauri 2 构建 |

### 🔗 聚合

| 工具 | Provider数 | 功能 | 核心亮点 |
| ------ | ----------- | ------ | ---------- |
| ✅ [one-api](https://github.com/songquanpeng/one-api) | - | - | 国产多模型代理<br>计费系统<br>37K Stars |
| [OpenRouter](https://openrouter.ai) | 200+ | 自动路由, 按量付费 | 200+ 模型<br>按用量付费<br>自动路由最优 Provider |
| ✅ [new-api](https://github.com/QuantumNous/new-api) | 50+ | 聚合分发, 计费, 限流 | 统一 OpenAI 兼容 API<br>多模型聚合分发<br>国内生态首选 |

### 🚪 网关

| 工具 | Provider数 | 功能 | 核心亮点 |
| ------ | ----------- | ------ | ---------- |
| ✅ [Portkey](https://portkey.ai) | 100+ | 可观测, 重试, Guardrails, A/B | 可观测性<br>自动重试/回退<br>Guardrails/缓存 |
| ✅ [Kong](https://github.com/Kong/kong) | ['通用 API + AI 插件'] | 限流, 负载均衡, 插件, 可观测 | 企业级 API 网关标准<br>AI 插件生态<br>高性能/高可用 |
| ✅ [Higress](https://github.com/higress-group/higress) | ['国内模型 + 国际模型'] | AI路由, 限流, 缓存, Wasm插件 | 阿里云出品<br>AI 原生设计<br>Envoy 底座 |

<!-- AUTOGEN_END -->

---

## 🔄 多模型路由实战

**核心思路**：根据任务复杂度自动选择模型。

| 任务类型 | 推荐模型 | 价格 (输入/输出) |
| --------- | --------- | ----------------- |
| **日常对话 / 简单问答** | GPT-5.4-nano / [DeepSeek-V4-Flash](https://deepseek.com) | $0.10 / $0.40 |
| **代码生成 / 文档撰写** | GPT-5.4-mini / [Claude Haiku 4](https://anthropic.com) | $0.40 / $1.60 |
| **复杂推理 / 系统设计** | [GPT-5.5](https://openai.com) / [Claude Opus 4](https://anthropic.com) | $5.00 / $25.00 |

**用 LiteLLM 实现路由**：
```python
# pip install litellm
from litellm import completion

def smart_route(prompt: str, complexity: str = "simple"):
    """根据任务复杂度选择模型"""
    models = {
        "simple": "deepseek/deepseek-chat",   # $0.07/MTok
        "medium": "gpt-5.4-mini",             # $0.40/MTok
        "complex": "gpt-5.5",                 # $5.00/MTok
    }
    return completion(
        model=models[complexity],
        messages=[{"role": "user", "content": prompt}]
    )

# 简单任务 → 便宜模型
smart_route("今天天气怎么样？", "simple")

# 复杂任务 → 旗舰模型
smart_route("设计一个分布式任务调度系统", "complex")
```

> [!TIP]
> **缓存是最大的省钱利器**
> 如果你的 Agent 有大量重复 Context（如系统提示），开启 Prompt 缓存可以将月账单砍掉 50-80%。DeepSeek 的缓存命中价格仅 $0.004/MTok，比直接调用便宜 17 倍。

## 🌏 工具速查

| 工具 | Stars | 定位 | 适合谁 |
| ------ | ------- | ------ | -------- |
| [**CC Switch**](https://github.com/farion1231/cc-switch) | 94K | 桌面 AI 模型管理 | 本地实验，模型对比 |
| [**one-api**](https://github.com/songquanpeng/one-api) | 37K | 多模型统一代理 | 国内团队，多供应商 |
| [**new-api**](https://github.com/QuantumNous/new-api) | 37K | [one-api](https://github.com/songquanpeng/one-api) 增强版 | 需要更多功能 |
| [**LiteLLM**](https://github.com/BerriAI/litellm) | 15K | AI 多模型代理 | 开发者，自建路由 |
| [**OpenRouter**](https://openrouter.ai) | — | 云端多模型路由 | 不想自建，按量付费 |
| [**Higress**](https://github.com/higress-group/higress) | 8.5K | 阿里云原生网关 | 阿里云用户 |
| [**Kong**](https://github.com/Kong/kong) | 43K | 企业级 API 网关 | 传统 API + AI 混合 |

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
