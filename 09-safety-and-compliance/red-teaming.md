# 🔴 红队测试工具

> 最后更新：2026-06-08
> 数据来源：`data/safety-and-compliance.yaml` 自动生成

---

## 🎯 红队测试：模拟攻击发现漏洞

红队测试的核心：**在部署前用自动化手段模拟攻击，发现 AI 系统的安全漏洞**。

| 测试目标 | 测试方法 | 推荐工具 |
|---------|---------|---------|
| **Prompt 注入攻击** | 构造恶意 Prompt 绕过系统指令 | **[Promptfoo](https://promptfoo.dev)** / **[Garak](https://garak.ai)** |
| **越狱攻击** | 让模型生成有害内容 | **[PyRIT](https://github.com/Azure/PyRIT)** / **HarmBench** |
| **幻觉检测** | 测试模型是否编造事实 | **[Garak](https://garak.ai)** |
| **数据泄露** | 测试模型是否泄露训练数据 | **[PyRIT](https://github.com/Azure/PyRIT)** |
| **多轮攻击** | 多步骤渐进式攻击 | **[PyRIT](https://github.com/Azure/PyRIT)** |
| **CI/CD 集成** | 每次发布前自动扫描 | **[Promptfoo](https://promptfoo.dev)** |

> [!TIP]
> **快速扫描用 Garak，多轮攻击用 PyRIT，CI/CD 集成用 Promptfoo**
> Promptfoo 已被 OpenAI 收购，成为官方推荐的红队测试方案。

---

## 📋 红队测试工具总览

<!-- AUTOGEN_START -->

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [Promptfoo](https://promptfoo.dev) | 最流行的 LLM 红队测试框架，支持 50+ 漏洞类型扫描 | security, open-source, cli-tool | 50+ 漏洞类型扫描<br>YAML 定义测试用例<br>CI/CD 集成<br>OpenAI 收购 |
| [Garak](https://garak.ai) | NVIDIA 出品的 LLM 漏洞扫描器，内置 37+ 探测模块 | security, gpu-acceleration, data-analysis | NVIDIA 出品<br>37+ 探测模块 (注入/越狱/幻觉/毒性)<br>结构化报告输出 |
| [PyRIT](https://github.com/Azure/PyRIT) | 微软推出的生成式 AI 风险识别框架，多轮次攻击编排 | security, microsoft, agent | Microsoft 出品<br>多轮次攻击编排<br>多模态攻击支持 |

<!-- AUTOGEN_END -->

---

## 💡 工具对比

| 维度 | Promptfoo | Garak | PyRIT |
|------|-----------|-------|-------|
| **出品方** | OpenAI 收购 | NVIDIA | Microsoft |
| **Stars** | 8K | 4.5K | 2.8K |
| **漏洞类型** | 50+ | 37+ | 多模态 |
| **多轮攻击** | ❌ | ❌ | ✅ |
| **CI/CD 集成** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **报告输出** | YAML/JSON | 结构化报告 | 结构化报告 |
| **适用场景** | CI/CD 自动扫描 | 快速漏洞扫描 | 多轮攻击编排 |

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
