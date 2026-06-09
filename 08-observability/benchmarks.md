# LLM 评测基准

> 最后更新：2026-06-08
> 数据来源：`data/observability.yaml` 自动生成

---

## 📈 LLM 评测：怎么知道模型好不好？

| 你的情况 | 推荐平台 | 理由 |
| --------- | --------- | ------ |
| **众包评测 / ELO 排名** | [LMSYS Chatbot Arena](https://lmarena.ai) | 最权威，社区驱动 |
| **开源 LLM 排行榜** | [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) | HuggingFace 官方 |
| **多维度评测** | [HELM](https://github.com/stanford-crfm/helm) | 斯坦福学术权威 |
| **LLM 评估框架** | [OpenAI Evals](https://github.com/openai/evals) / [DeepEval](https://github.com/confident-ai/deepeval) | 自定义评估任务 |
| **国内评测** | [OpenCompass](https://github.com/open-compass/opencompass) | 国内最权威 |

> [!TIP]
> **LMSYS Chatbot Arena 是最权威的 LLM 评测**
> 通过众包方式让用户盲测两个模型，生成 ELO 排名。目前已有 100+ 模型参与评测。

---

## 📋 LLM 评测工具总览

<!-- AUTOGEN_START -->

| 名称 | 简介 | 标签 | 亮点 |
| ------ | ------ | ------ | ------ |
| [OpenAI Evals](https://github.com/openai/evals) | OpenAI 官方 LLM 评估框架，支持自定义评估任务 | data-analysis, openai-compatible | 18.6K Stars<br>OpenAI 官方<br>自定义评估 |
| [DeepEval](https://github.com/confident-ai/deepeval) | LLM 评估框架，支持 14+ 评估指标，单元测试风格 | data-analysis, automation, observability | 16K Stars<br>14+ 评估指标<br>单元测试风格 |
| [OpenCompass](https://github.com/open-compass/opencompass) | LLM 评估平台，支持 100+ 数据集，国内最权威 | data-analysis, chinese | 7K Stars<br>100+ 数据集<br>国内最权威 |
| [AgentBench](https://github.com/THUDM/AgentBench) | ICLR 2024 论文，评估 LLM 作为 Agent 的能力 | data-analysis, agent, academic | 3.5K Stars<br>ICLR 2024<br>Agent 评估 |
| [EvalScope](https://github.com/modelscope/evalscope) | ModelScope 出品的 LLM 评估框架，支持自定义评估 | data-analysis, open-source | 2.9K Stars<br>ModelScope 出品<br>自定义评估 |
| [LMSYS Chatbot Arena](https://lmarena.ai) | LLM 众包评测平台，ELO 排名 | data-analysis | LLM 众包评测<br>ELO 排名<br>最权威 |
| [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) | HuggingFace 的开源 LLM 排行榜 | data-analysis, open-source | HuggingFace 排行榜<br>开源 LLM 评测<br>社区驱动 |
| [HELM](https://github.com/stanford-crfm/helm) | 斯坦福的 LLM 评估框架，多维度评测 | data-analysis, academic | 斯坦福评估框架<br>多维度评测<br>学术权威 |

<!-- AUTOGEN_END -->

---

## 🏛️ 评测分类

### 🔵 众包评测平台

| 平台 | 核心优势 | 适合谁 |
| ------ | --------- | -------- |
| [**LMSYS Chatbot Arena**](https://lmarena.ai) | ELO 排名，最权威 | 模型选型 |
| [**Open LLM Leaderboard**](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) | HuggingFace 官方 | 开源模型对比 |

### 🟢 学术评测框架

| 平台 | Stars | 核心优势 | 适合谁 |
| ------ | ------- | --------- | -------- |
| [**HELM**](https://github.com/stanford-crfm/helm) | - | 斯坦福多维度评测 | 学术研究 |
| [**OpenCompass**](https://github.com/open-compass/opencompass) | 7K | 国内最权威，100+ 数据集 | 国内评测 |
| [**AgentBench**](https://github.com/THUDM/AgentBench) | 3.5K | ICLR 2024 Agent 评估 | Agent 评测 |

### 🟡 自定义评估框架

| 平台 | Stars | 核心优势 | 适合谁 |
| ------ | ------- | --------- | -------- |
| [**OpenAI Evals**](https://github.com/openai/evals) | 18.6K | OpenAI 官方，自定义评估 | 开发者 |
| [**DeepEval**](https://github.com/confident-ai/deepeval) | 16K | 14+ 评估指标，单元测试风格 | 开发者 |

## 💡 评测指标说明

| 指标 | 含义 | 常用基准 |
| ------ | ------ | --------- |
| **MMLU** | 多任务语言理解 | 知识广度 |
| **HumanEval** | 代码生成 | 编程能力 |
| **MATH** | 数学推理 | 数学能力 |
| **ARC** | 科学推理 | 推理能力 |
| **ELO** | 众包排名 | 综合体验 |

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
