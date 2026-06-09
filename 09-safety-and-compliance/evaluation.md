# 📊 安全评估框架

> 最后更新：2026-06-08
> 数据来源：`data/safety-and-compliance.yaml` 自动生成

---

## 🔬 安全评估：量化 AI 系统的安全性

安全评估的核心：**用标准化基准测试衡量模型的安全性和对齐程度**。

| [](https://promptfoo.dev)评估维度[](https://promptfoo.dev) | [](https://promptfoo.dev)评估内容[](https://promptfoo.dev) | [](https://promptfoo.dev)推荐工具[](https://promptfoo.dev) |
| --------- | --------- | --------- |
| **[](https://promptfoo.dev)政府级合规[](https://promptfoo.dev)** | [](https://promptfoo.dev)100[](https://promptfoo.dev)+ [](https://promptfoo.dev)预构建评估项[](https://promptfoo.dev)，[](https://promptfoo.dev)Anthropic[](https://promptfoo.dev)/[](https://promptfoo.dev)DeepMind[](https://promptfoo.dev) [](https://promptfoo.dev)采用[](https://promptfoo.dev) | [**Inspect**](https://inspect.ai) |
| **[](https://promptfoo.dev)学术研究[](https://promptfoo.dev)** | [](https://promptfoo.dev)510[](https://promptfoo.dev) [](https://promptfoo.dev)种有害行为[](https://promptfoo.dev)，[](https://promptfoo.dev)18[](https://promptfoo.dev) [](https://promptfoo.dev)种对抗攻击方法[](https://promptfoo.dev) | [**HarmBench**](https://harmbench.org) |
| **[](https://promptfoo.dev)红队测试[](https://promptfoo.dev)** | [](https://promptfoo.dev)漏洞扫描与攻击模拟[](https://promptfoo.dev) | [**Promptfoo[**](https://promptfoo.dev) / [**](https://promptfoo.dev)Garak**](https://garak.ai) |
| **[](https://promptfoo.dev)内容审核[](https://promptfoo.dev)** | [](https://promptfoo.dev)有害内容检测[](https://promptfoo.dev) | [**Llama Guard**](https://ai.meta.com/llama/) / [**OpenAI Moderation**](https://platform.openai.com/docs/guides/moderation) |

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

| [](https://promptfoo.dev)维度[](https://promptfoo.dev) | [Inspect](https://inspect.aisi.org.uk) | [HarmBench](https://harmbench.org) |
| ------ | --------- | ----------- |
| **[](https://promptfoo.dev)出品方[](https://promptfoo.dev)** | [](https://promptfoo.dev)英国[](https://promptfoo.dev) [](https://promptfoo.dev)AISI[](https://promptfoo.dev) | [](https://promptfoo.dev)AI[](https://promptfoo.dev) [](https://promptfoo.dev)安全中心[](https://promptfoo.dev) |
| **[](https://promptfoo.dev)Stars[](https://promptfoo.dev)** | [](https://promptfoo.dev)1[](https://promptfoo.dev).[](https://promptfoo.dev)2K[](https://promptfoo.dev) | [](https://promptfoo.dev)900[](https://promptfoo.dev) |
| **[](https://promptfoo.dev)评估项[](https://promptfoo.dev)** | [](https://promptfoo.dev)100[](https://promptfoo.dev)+ | [](https://promptfoo.dev)510[](https://promptfoo.dev) [](https://promptfoo.dev)种有害行为[](https://promptfoo.dev) |
| **[](https://promptfoo.dev)对抗攻击[](https://promptfoo.dev)** | [](https://promptfoo.dev)内置[](https://promptfoo.dev) | [](https://promptfoo.dev)18[](https://promptfoo.dev) [](https://promptfoo.dev)种方法[](https://promptfoo.dev) |
| **[](https://promptfoo.dev)政府采用[](https://promptfoo.dev)** | ✅ | ❌ |
| **[](https://promptfoo.dev)学术采用[](https://promptfoo.dev)** | ✅ | ✅ |
| **[](https://promptfoo.dev)适用场景[](https://promptfoo.dev)** | [](https://promptfoo.dev)政府级合规评估[](https://promptfoo.dev) | [](https://promptfoo.dev)学术安全研究[](https://promptfoo.dev) |

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
