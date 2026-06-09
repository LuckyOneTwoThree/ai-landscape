# 🔴 红队测试工具

> 最后更新：2026-06-08
> 数据来源：`data/safety-and-compliance.yaml` 自动生成

---

## 🎯 红队测试：模拟攻击发现漏洞

红队测试的核心：**在部署前用自动化手段模拟攻击，发现 AI 系统的安全漏洞**。

| [](https://github.com/Azure/PyRIT)测试目标[](https://github.com/Azure/PyRIT) | [](https://github.com/Azure/PyRIT)测试方法[](https://github.com/Azure/PyRIT) | [](https://github.com/Azure/PyRIT)推荐工具[](https://github.com/Azure/PyRIT) |
| --------- | --------- | --------- |
| [**[](https://github.com/Azure/PyRIT)Prompt[](https://github.com/Azure/PyRIT) [](https://github.com/Azure/PyRIT)注入攻击[](https://github.com/Azure/PyRIT)**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | [](https://github.com/Azure/PyRIT)构造恶意[](https://github.com/Azure/PyRIT) [](https://github.com/Azure/PyRIT)Prompt[](https://github.com/Azure/PyRIT) [](https://github.com/Azure/PyRIT)绕过系统指令[](https://github.com/Azure/PyRIT) | [**Promptfoo[**](https://promptfoo.dev) / [**](https://promptfoo.dev)Garak**](https://[garak](https://garak.ai).ai) |
| [**[](https://github.com/Azure/PyRIT)越狱攻击[](https://github.com/Azure/PyRIT)**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | [](https://github.com/Azure/PyRIT)让模型生成有害内容[](https://github.com/Azure/PyRIT) | [**PyRIT[**](https://github.com/Azure/PyRIT) / [**](https://github.com/Azure/PyRIT)HarmBench**](https://harmbench.org) |
| [**[](https://github.com/Azure/PyRIT)幻觉检测[](https://github.com/Azure/PyRIT)**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | [](https://github.com/Azure/PyRIT)测试模型是否编造事实[](https://github.com/Azure/PyRIT) | [**Garak**](https://garak.ai) |
| [**[](https://github.com/Azure/PyRIT)数据泄露[](https://github.com/Azure/PyRIT)**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | [](https://github.com/Azure/PyRIT)测试模型是否泄露训练数据[](https://github.com/Azure/PyRIT) | [**PyRIT**](https://github.com/Azure/PyRIT) |
| [**[](https://github.com/Azure/PyRIT)多轮攻击[](https://github.com/Azure/PyRIT)**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | [](https://github.com/Azure/PyRIT)多步骤渐进式攻击[](https://github.com/Azure/PyRIT) | [**PyRIT**](https://github.com/Azure/PyRIT) |
| [**[](https://github.com/Azure/PyRIT)CI[](https://github.com/Azure/PyRIT)/[](https://github.com/Azure/PyRIT)CD[](https://github.com/Azure/PyRIT) [](https://github.com/Azure/PyRIT)集成[](https://github.com/Azure/PyRIT)**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | [](https://github.com/Azure/PyRIT)每次发布前自动扫描[](https://github.com/Azure/PyRIT) | [**Promptfoo**](https://promptfoo.dev) |

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

| [](https://github.com/Azure/PyRIT)维度[](https://github.com/Azure/PyRIT) | [](https://github.com/Azure/PyRIT)Promptfoo[](https://github.com/Azure/PyRIT) | [](https://github.com/Azure/PyRIT)Garak[](https://github.com/Azure/PyRIT) | [](https://github.com/Azure/PyRIT)PyRIT[](https://github.com/Azure/PyRIT) |
| ------ | ----------- | ------- | ------- |
| [**[](https://github.com/Azure/PyRIT)出品方[](https://github.com/Azure/PyRIT)**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | [](https://github.com/Azure/PyRIT)OpenAI[](https://github.com/Azure/PyRIT) [](https://github.com/Azure/PyRIT)收购[](https://github.com/Azure/PyRIT) | [](https://github.com/Azure/PyRIT)NVIDIA[](https://github.com/Azure/PyRIT) | [](https://github.com/Azure/PyRIT)Microsoft[](https://github.com/Azure/PyRIT) |
| [**[](https://github.com/Azure/PyRIT)Stars[](https://github.com/Azure/PyRIT)**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | [](https://github.com/Azure/PyRIT)8K[](https://github.com/Azure/PyRIT) | [](https://github.com/Azure/PyRIT)4[](https://github.com/Azure/PyRIT).[](https://github.com/Azure/PyRIT)5K[](https://github.com/Azure/PyRIT) | [](https://github.com/Azure/PyRIT)2[](https://github.com/Azure/PyRIT).[](https://github.com/Azure/PyRIT)8K[](https://github.com/Azure/PyRIT) |
| [**[](https://github.com/Azure/PyRIT)漏洞类型[](https://github.com/Azure/PyRIT)**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | [](https://github.com/Azure/PyRIT)50[](https://github.com/Azure/PyRIT)+ | [](https://github.com/Azure/PyRIT)37[](https://github.com/Azure/PyRIT)+ | [](https://github.com/Azure/PyRIT)多模态[](https://github.com/Azure/PyRIT) |
| [**[](https://github.com/Azure/PyRIT)多轮攻击[](https://github.com/Azure/PyRIT)**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | ❌ | ❌ | ✅ |
| [**[](https://github.com/Azure/PyRIT)CI[](https://github.com/Azure/PyRIT)/[](https://github.com/Azure/PyRIT)CD[](https://github.com/Azure/PyRIT) [](https://github.com/Azure/PyRIT)集成[](https://github.com/Azure/PyRIT)**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| [**[](https://github.com/Azure/PyRIT)报告输出[](https://github.com/Azure/PyRIT)**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | [](https://github.com/Azure/PyRIT)YAML[](https://github.com/Azure/PyRIT)/[](https://github.com/Azure/PyRIT)JSON[](https://github.com/Azure/PyRIT) | [](https://github.com/Azure/PyRIT)结构化报告[](https://github.com/Azure/PyRIT) | [](https://github.com/Azure/PyRIT)结构化报告[](https://github.com/Azure/PyRIT) |
| [**[](https://github.com/Azure/PyRIT)适用场景[](https://github.com/Azure/PyRIT)**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | [](https://github.com/Azure/PyRIT)CI[](https://github.com/Azure/PyRIT)/[](https://github.com/Azure/PyRIT)CD[](https://github.com/Azure/PyRIT) [](https://github.com/Azure/PyRIT)自动扫描[](https://github.com/Azure/PyRIT) | [](https://github.com/Azure/PyRIT)快速漏洞扫描[](https://github.com/Azure/PyRIT) | [](https://github.com/Azure/PyRIT)多轮攻击编排[](https://github.com/Azure/PyRIT) |

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
