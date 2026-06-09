# LLM Benchmarks

> Last Updated: 2026-06-08
> Data Source: Automatically generated from `data/observability.yaml`

---

## 📈 LLM Benchmarking: How to Know if a Model is Good?

| Your Situation | **Recommended Platform** | Reason |
| --------- | **---------** | ------ |
| **Crowdsourced Benchmarking / ELO Ranking** | **LMSYS Chatbot Arena** | Most authoritative, community-driven |
| **Open Source LLM Leaderboard** | **Open LLM Leaderboard** | Official HuggingFace |
| **Multi-dimensional Benchmarking** | **HELM** | Stanford academic authority |
| **LLM Evaluation Framework** | **OpenAI Evals / DeepEval** | Custom evaluation tasks |
| **Domestic Benchmarking (China)** | **OpenCompass** | Most authoritative in China |

> [!TIP]
> **LMSYS Chatbot Arena is the most authoritative LLM benchmark**
> It generates ELO rankings through crowdsourced blind tests where users compare two models. Currently, 100+ models participate in the benchmark.

---

## 📋 LLM Benchmarking Tools Overview

<!-- AUTOGEN_START -->

| Name | Introduction | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [OpenAI Evals](https://github.com/openai/evals) | Official OpenAI LLM evaluation framework, supports custom evaluation tasks | data-analysis, openai-compatible | 18.6K Stars<br>Official OpenAI<br>Custom evaluation |
| [DeepEval](https://github.com/confident-ai/deepeval) | LLM evaluation framework, supports 14+ evaluation metrics, unit testing style | data-analysis, automation, observability | 16K Stars<br>14+ metrics<br>Unit testing style |
| [OpenCompass](https://github.com/open-compass/opencompass) | LLM evaluation platform, supports 100+ datasets, most authoritative in China | data-analysis, chinese | 7K Stars<br>100+ datasets<br>Most authoritative in China |
| [AgentBench](https://github.com/THUDM/AgentBench) | ICLR 2024 paper, evaluates LLM capabilities as Agents | data-analysis, agent, academic | 3.5K Stars<br>ICLR 2024<br>Agent evaluation |
| [EvalScope](https://github.com/modelscope/evalscope) | LLM evaluation framework by ModelScope, supports custom evaluation | data-analysis, open-source | 2.9K Stars<br>By ModelScope<br>Custom evaluation |
| [LMSYS Chatbot Arena](https://lmarena.ai) | LLM crowdsourced benchmarking platform, ELO ranking | data-analysis | LLM crowdsourcing<br>ELO ranking<br>Most authoritative |
| [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) | HuggingFace's open-source LLM leaderboard | data-analysis, open-source | HuggingFace leaderboard<br>Open-source LLM benchmark<br>Community-driven |
| [HELM](https://github.com/stanford-crfm/helm) | Stanford's LLM evaluation framework, multi-dimensional benchmarking | data-analysis, academic | Stanford framework<br>Multi-dimensional<br>Academic authority |

<!-- AUTOGEN_END -->

---

## 🏛️ Benchmarking Categories

### 🔵 Crowdsourced Benchmarking Platforms

| Platform | Core Advantage | Best For |
| ------ | --------- | -------- |
| [**LMSYS Chatbot Arena**](https://chat.lmsys.org) | ELO ranking, most authoritative | Model selection |
| [**Open LLM Leaderboard**](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) | HuggingFace official | Open-source model comparison |

### 🟢 Academic Benchmarking Frameworks

| Platform | Stars | Core Advantage | Best For |
| ------ | ------- | --------- | -------- |
| [**HELM**](https://crfm.stanford.edu/helm/) | - | Stanford multi-dimensional benchmark | Academic research |
| [**OpenCompass**](https://opencompass.org.cn) | 7K | Most authoritative in China, 100+ datasets | Domestic benchmarking |
| [**AgentBench**](https://github.com/THUDM/AgentBench) | 3.5K | ICLR 2024 Agent evaluation | Agent evaluation |

### 🟡 Custom Evaluation Frameworks

| Platform | Stars | Core Advantage | Best For |
| ------ | ------- | --------- | -------- |
| [**OpenAI Evals**](https://github.com/openai/evals) | 18.6K | Official OpenAI, custom evaluation | Developers |
| [**DeepEval**](https://confident-ai.com) | 16K | 14+ metrics, unit testing style | Developers |

## 💡 Benchmark Metrics Explanation

| Metric | Meaning | Common Benchmark For |
| ------ | ------ | --------- |
| **MMLU** | Massive Multitask Language Understanding | Knowledge breadth |
| **HumanEval** | Code generation | Programming ability |
| **MATH** | Mathematical reasoning | Mathematical ability |
| **ARC** | Scientific reasoning | Reasoning ability |
| **ELO** | Crowdsourced ranking | Comprehensive experience |

---

> **Update Frequency**: Updated quarterly
> **Automation**: Run `python scripts/build_docs.py` to re-render tables from YAML.
