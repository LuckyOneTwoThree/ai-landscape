# 内容审核

> 最后更新：2026-06-08
> 数据来源：`data/safety-and-compliance.yaml` 自动生成

---

## 🔍 内容审核：让 AI 输出更安全

| 你的情况 | 推荐方案 | 理由 |
|---------|---------|------|
| **OpenAI 用户** | [OpenAI Moderation](https://platform.openai.com/docs/guides/moderation) | 内置，免费 |
| **开源方案** | [Llama Guard](https://github.com/meta-llama/PurpleLlama) | Meta 出品，3K Stars |
| **企业级** | NeMo Guardrails | 可编程规则 |

> [!TIP]
> **OpenAI Moderation 是最简单的方案**
> 如果你使用 OpenAI API，直接使用内置的 Moderation 端点，免费且无需额外部署。

---

## 📋 内容审核工具总览

<!-- AUTOGEN_START -->

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [Llama Guard](https://github.com/meta-llama/PurpleLlama) | Meta 出品的内容安全分类模型 | security, open-source, data-analysis | Meta 出品<br>内容安全分类<br>3K Stars |
| [OpenAI Moderation](https://platform.openai.com/docs/guides/moderation) | OpenAI 内置的内容审核 API | security, openai-compatible, api-gateway | OpenAI 内置<br>内容审核 API<br>免费 |

<!-- AUTOGEN_END -->

---

## 🏛️ 审核方式

### 🔵 API 服务型

| 工具 | 核心优势 | 适合谁 |
|------|---------|--------|
| **OpenAI Moderation** | 内置，免费 | OpenAI 用户 |

### 🟢 开源模型型

| 工具 | Stars | 核心优势 | 适合谁 |
|------|-------|---------|--------|
| **Llama Guard** | 3K | Meta 出品，内容安全分类 | 内容审核 |

### 🟡 可编程规则型

| 工具 | Stars | 核心优势 | 适合谁 |
|------|-------|---------|--------|
| **NeMo Guardrails** | 6.4K | NVIDIA 出品，可编程规则 | 企业级 |

## 💡 审核维度

| 维度 | 说明 | 工具支持 |
|------|------|---------|
| **暴力** | 暴力内容检测 | OpenAI, Llama Guard |
| **色情** | 色情内容检测 | OpenAI, Llama Guard |
| **仇恨** | 仇恨言论检测 | OpenAI, Llama Guard |
| **自残** | 自残内容检测 | OpenAI |
| **Prompt 注入** | 注入攻击检测 | NeMo Guardrails |

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
