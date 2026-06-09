# 📊 Safety Evaluation Frameworks

> Last Updated: 2026-06-08
> Data Source: Generated automatically from `data/safety-and-compliance.yaml`

---

## 🔬 Safety Evaluation: Quantifying AI System Security

The core of safety evaluation: **Using standardized benchmarks to measure the safety and alignment of models**.

| Evaluation Dimension | **Evaluation Content** | Recommended Tools |
| --------- | --------- | --------- |
| **Government-Grade Compliance** | **100+ pre-built evaluations, adopted by Anthropic/DeepMind** | **[Inspect](https://inspect.aisi.org.uk)** |
| **Academic Research** | **510 harmful behaviors, 18 adversarial attack methods** | **[HarmBench](https://harmbench.org)** |
| **Red Teaming** | **Vulnerability scanning and attack simulation** | **Promptfoo** / **Garak** |
| **Content Moderation** | **Harmful content detection** | **Llama Guard** / **OpenAI Moderation** |

> [!TIP]
> **Inspect is the premier choice for government-grade safety evaluation**
> Developed by the UK AI Safety Institute, it features 100+ pre-built evaluations and is adopted by top-tier companies like Anthropic and DeepMind.

---

## 📋 Safety Evaluation Tools Overview

<!-- AUTOGEN_START -->

| Name | Description | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [Inspect](https://inspect.aisi.org.uk) | UK AI Safety Institute evaluation framework, 100+ pre-built evaluations | security, data-analysis, compliance | By UK AISI<br>100+ pre-built evaluations<br>Adopted by Anthropic/DeepMind |
| [HarmBench](https://harmbench.org) | Standardized red teaming benchmark by Center for AI Safety, 510 harmful behaviors | security, data-analysis, academic | 510 harmful behaviors<br>18 adversarial attack methods<br>Academic standard benchmark |

<!-- AUTOGEN_END -->

---

## 💡 Tool Comparison

| Dimension | [Inspect](https://inspect.aisi.org.uk) | [HarmBench](https://harmbench.org) |
| ------ | --------- | ----------- |
| **Creator** | UK AISI | Center for AI Safety |
| **Stars** | 1.2K | 900 |
| **Evaluations** | 100+ | 510 harmful behaviors |
| **Adversarial Attacks** | Built-in | 18 methods |
| **Government Adoption** | ✅ | ❌ |
| **Academic Adoption** | ✅ | ✅ |
| **Best For** | Government-grade compliance evaluation | Academic safety research |

---

> **Update Frequency**: Quarterly
> **Automation**: Run `python scripts/build_docs.py` to re-render tables from YAML.
