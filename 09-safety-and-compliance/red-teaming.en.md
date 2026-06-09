# 🔴 Red Teaming Tools

> Last Updated: 2026-06-08
> Data Source: Generated automatically from `data/safety-and-compliance.yaml`

---

## 🎯 Red Teaming: Simulating Attacks to Discover Vulnerabilities

The core of red teaming: **Using automated methods to simulate attacks before deployment to discover security vulnerabilities in AI systems**.

| Testing Goal | **Testing Method** | Recommended Tools |
| --------- | **---------** | --------- |
| [**Prompt Injection Attacks**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | **Crafting malicious prompts to bypass system instructions** | [**Promptfoo[**](https://promptfoo.dev) / [**](https://promptfoo.dev)Garak**](https://[garak](https://garak.ai).ai) |
| [**Jailbreak Attacks**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | **Forcing the model to generate harmful content** | [**PyRIT[**](https://github.com/Azure/PyRIT) / [**](https://github.com/Azure/PyRIT)HarmBench**](https://harmbench.org) |
| [**Hallucination Detection**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | **Testing whether the model fabricates facts** | [**Garak**](https://garak.ai) |
| [**Data Leakage**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | **Testing whether the model leaks training data** | [**PyRIT**](https://github.com/Azure/PyRIT) |
| [**Multi-Turn Attacks**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | **Multi-step progressive attacks** | [**PyRIT**](https://github.com/Azure/PyRIT) |
| [**CI/CD Integration**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | **Automated scanning before every release** | [**Promptfoo**](https://promptfoo.dev) |

> [!TIP]
> **Use Garak for rapid scanning, PyRIT for multi-turn attacks, and Promptfoo for CI/CD integration**
> Promptfoo was acquired by OpenAI, becoming their officially recommended red teaming solution.

---

## 📋 Red Teaming Tools Overview

<!-- AUTOGEN_START -->

| Name | Description | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [Promptfoo](https://promptfoo.dev) | Most popular LLM red teaming framework, supporting 50+ vulnerability scans | security, open-source, cli-tool | 50+ vulnerability scans<br>YAML-defined test cases<br>CI/CD integration<br>Acquired by OpenAI |
| [Garak](https://garak.ai) | LLM vulnerability scanner by NVIDIA, 37+ built-in probe modules | security, gpu-acceleration, data-analysis | By NVIDIA<br>37+ probe modules (injection/jailbreak/hallucination/toxicity)<br>Structured report output |
| [PyRIT](https://github.com/Azure/PyRIT) | Generative AI risk identification framework by Microsoft, multi-turn attack orchestration | security, microsoft, agent | By Microsoft<br>Multi-turn attack orchestration<br>Multi-modal attack support |

<!-- AUTOGEN_END -->

---

## 💡 Tool Comparison

| Dimension | Promptfoo | Garak | PyRIT |
| ------ | ----------- | ------- | ------- |
| [**Creator**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | Acquired by OpenAI | NVIDIA | Microsoft |
| [**Stars**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | 8K | 4.5K | 2.8K |
| [**Vulnerability Types**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | 50+ | 37+ | Multi-modal |
| [**Multi-Turn Attacks**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | ❌ | ❌ | ✅ |
| [**CI/CD Integration**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| [**Report Output**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | YAML/JSON | Structured reports | Structured reports |
| [**Best For**](https://github.com/Azure/[PyRIT](https://github.com/Azure/PyRIT)) | CI/CD automated scanning | Rapid vulnerability scanning | Multi-turn attack orchestration |

---

> **Update Frequency**: Quarterly
> **Automation**: Run `python scripts/build_docs.py` to re-render tables from YAML.
