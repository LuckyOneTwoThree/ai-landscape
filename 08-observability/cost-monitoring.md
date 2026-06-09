# 成本监控与预算管理

> 最后更新：2026-06-08
> 数据来源：`data/observability.yaml` 自动生成

---

## 💰 成本监控：控制 AI 开支

| 你的情况 | 推荐方案 | 理由 |
|---------|---------|------|
| **多模型路由** | [LiteLLM Budget Manager](https://github.com/BerriAI/litellm) | 内置预算管理 |
| **OpenRouter 用户** | [OpenRouter Usage](https://openrouter.ai) | 内置 Token 消耗监控 |
| **企业级** | Portkey | 全链路成本追踪 |

> [!TIP]
> **LiteLLM Budget Manager 是最简单的成本控制方案**
> 设置预算上限，超过自动降级到便宜模型。支持 100+ LLM Provider。

---

## 📋 成本监控工具总览

<!-- AUTOGEN_START -->

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [LiteLLM Budget Manager](https://github.com/BerriAI/litellm) | LiteLLM 内置的预算与 Token 限额管理 | cost-effective, openai-compatible | 预算管理<br>Token 限额<br>内置功能 |
| [OpenRouter Usage](https://openrouter.ai) | OpenRouter 内置的 Token 消耗与成本监控 | cost-effective, observability, openai-compatible | Token 消耗监控<br>成本分析<br>内置功能 |

<!-- AUTOGEN_END -->

---

## 💡 成本优化策略

| 策略 | 实现方式 | 节省比例 |
|------|---------|---------|
| **模型路由** | 简单任务用便宜模型 | 30-50% |
| **Prompt 缓存** | 相同 Prompt 自动缓存 | 20-40% |
| **Token 限流** | 按用户/团队设置预算 | 防止超支 |
| **批量处理** | 非实时任务用 Batch API | 50% |

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
