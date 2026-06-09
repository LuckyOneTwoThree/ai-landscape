# AI 护栏与安全防护

> 最后更新：2026-06-08
> 数据来源：`data/safety-and-compliance.yaml` 自动生成

---

## 🛡️ AI 护栏：让 LLM 更安全

| 你的情况 | 推荐方案 | 理由 |
|---------|---------|------|
| **可编程规则** | [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | NVIDIA 出品，6.4K Stars |
| **输出验证** | [Guardrails AI](https://github.com/guardrails-ai/guardrails) | 自动纠正，5K Stars |
| **Prompt 注入防护** | Superagent / [Rebuff AI](https://github.com/protectai/rebuff) | 防注入/数据泄露 |
| **内容安全分类** | Llama Guard | Meta 出品 |

> [!TIP]
> **NeMo Guardrails 是企业级护栏的首选**
> NVIDIA 出品，支持可编程规则，可以定义 LLM 可以说什么、不可以说什么。

---

## 📋 AI 护栏工具总览

<!-- AUTOGEN_START -->

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | NVIDIA 出品的 LLM 护栏工具包，可编程规则 | security, gpu-acceleration, automation | NVIDIA 出品<br>可编程规则<br>6.4K Stars |
| [Guardrails AI](https://github.com/guardrails-ai/guardrails) | 开源 LLM 输出验证与纠正框架 | security, compliance, open-source | 开源输出验证<br>自动纠正<br>100+ 社区验证器 |
| [Rebuff AI](https://github.com/protectai/rebuff) | Prompt 注入检测的自愈式防护框架 | security, automation | 自愈式防护<br>Prompt 注入检测<br>1.5K Stars |
| [Prompt Armor](https://promptarmor.com) | Prompt 注入检测与防护工具 | security | Prompt 注入检测<br>防护工具<br>企业级 |
| [Lakera Guard](https://www.lakera.ai/lakera-guard) | 实时 Prompt 注入防护 API，50ms 以下延迟 | security, real-time, enterprise | 实时防护 (50ms 延迟)<br>100+ 语言 98% 准确率<br>Check Point 收购 |

<!-- AUTOGEN_END -->

---

## 🏛️ 护栏分类

### 🔵 可编程规则型

| 工具 | Stars | 核心优势 | 适合谁 |
|------|-------|---------|--------|
| **NeMo Guardrails** | 6.4K | NVIDIA 出品，可编程规则 | 企业级 |
| **Guardrails AI** | 5K | 开源输出验证，自动纠正 | 开发者 |

### 🟢 Prompt 注入防护型

| 工具 | Stars | 核心优势 | 适合谁 |
|------|-------|---------|--------|
| **Superagent** | 6.6K | 防注入/数据泄露 | 企业级 |
| **Rebuff AI** | 1.5K | 自愈式防护 | 开发者 |

### 🟡 内容安全分类型

| 工具 | Stars | 核心优势 | 适合谁 |
|------|-------|---------|--------|
| **Llama Guard** | 3K | Meta 出品，内容安全分类 | 内容审核 |
| **OpenAI Moderation** | - | OpenAI 内置，免费 | OpenAI 用户 |

## 💡 护栏策略

| 策略 | 实现方式 | 适用场景 |
|------|---------|---------|
| **输入过滤** | Prompt 注入检测 | 所有场景 |
| **输出验证** | 结构化输出校验 | 数据处理 |
| **内容审核** | 安全分类模型 | 用户交互 |
| **规则引擎** | 可编程规则 | 企业级 |

> [!TIP]
> **最佳实践：多层防护**
> 1. **输入层**：Prompt 注入检测（Superagent）
> 2. **处理层**：可编程规则（NeMo Guardrails）
> 3. **输出层**：内容审核（Llama Guard）

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
