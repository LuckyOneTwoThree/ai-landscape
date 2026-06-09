# 📊 安全评估框架

> 最后更新：2026-06-08
> 数据来源：`data/safety-and-compliance.yaml` 自动生成

---

## 🔬 安全评估：量化 AI 系统的安全性

安全评估的核心：**用标准化基准测试衡量模型的安全性和对齐程度**。

| 评估维度 | 评估内容 | 推荐工具 |
|---------|---------|---------|
| **政府级合规** | 100+ 预构建评估项，Anthropic/DeepMind 采用 | **[Inspect](https://inspect.aisi.org.uk)** |
| **学术研究** | 510 种有害行为，18 种对抗攻击方法 | **[HarmBench](https://harmbench.org)** |
| **红队测试** | 漏洞扫描与攻击模拟 | **Promptfoo** / **Garak** |
| **内容审核** | 有害内容检测 | **Llama Guard** / **OpenAI Moderation** |

> [!TIP]
> **Inspect 是政府级安全评估的首选**
> 英国 AI 安全研究所出品，100+ 预构建评估项，已被 Anthropic、DeepMind 等头部公司采用。

---

## 📋 安全评估工具总览

<!-- AUTOGEN_START -->

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [Inspect](https://inspect.aisi.org.uk) | 英国 AI 安全研究所评估框架，100+ 预构建评估项 | security, data-analysis, compliance | 英国 AISI 出品<br>100+ 预构建评估<br>Anthropic/DeepMind 采用 |
| [HarmBench](https://harmbench.org) | AI 安全中心发布的标准化红队基准，510 种有害行为 | security, data-analysis, academic | 510 种有害行为<br>18 种对抗攻击方法<br>学术界标准基准 |

<!-- AUTOGEN_END -->

---

## 💡 工具对比

| 维度 | Inspect | HarmBench |
|------|---------|-----------|
| **出品方** | 英国 AISI | AI 安全中心 |
| **Stars** | 1.2K | 900 |
| **评估项** | 100+ | 510 种有害行为 |
| **对抗攻击** | 内置 | 18 种方法 |
| **政府采用** | ✅ | ❌ |
| **学术采用** | ✅ | ✅ |
| **适用场景** | 政府级合规评估 | 学术安全研究 |

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
