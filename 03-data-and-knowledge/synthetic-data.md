# 合成数据

> 最后更新：2026-06-08
> 数据来源：`data/data-and-knowledge.yaml` 自动生成

---

## 🧪 什么时候需要合成数据？

| 场景 | 需要合成数据吗 | 理由 |
| ------ | -------------- | ------ |
| **微调模型，但只有 100 条数据** | ✅ 需要 | 数据量太少，模型学不到东西 |
| **训练分类器，但某些类别样本极少** | ✅ 需要 | 类别不平衡，模型偏向多数类 |
| **测试 RAG 系统，但没有标注数据** | ✅ 需要 | 用 LLM 生成 Q&A 对做评估 |
| **已经有 10 万条高质量数据** | ❌ 不需要 | 数据量足够，合成数据反而引入噪声 |

> [!TIP]
> **合成数据的核心价值：冷启动**
> 当你没有足够的真实数据时，用 LLM 生成合成数据是最快的冷启动方案。但合成数据永远不能完全替代真实数据——一旦有了真实数据，应该逐步替换。

---

## 📋 合成数据平台总览

<!-- AUTOGEN_START -->

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [Cleanlab](https://github.com/cleanlab/cleanlab) | 数据质量工具，自动检测标注错误/异常值，提升训练数据质量 | data-analysis | 11.5K Stars<br>数据质量<br>自动检测标注错误 |
| [Distilabel](https://github.com/argilla-io/distilabel) | Argilla 出品的合成数据生成框架 | data-analysis, openai-compatible, pipeline | 为 LLM 设计的高效可编程造数据流水线<br>内置 LLM-as-a-judge 智能过滤与打分<br>直接导出兼容 SFT/DPO 的极简格式 |
| [Argilla](https://github.com/argilla-io/argilla) | 数据标注与合成数据平台，支持人机协作 | data-analysis, collaboration | 为人类反馈 (RLHF) 打造的顶级标注协同 UI<br>与 Distilabel 无缝串联，构成闭环<br>小团队精细化数据清洗的必备案头工具 |
| [SDG (Synthetic Data Generator)](https://github.com/hitsz-ids/synthetic-data-generator) | 国内最活跃的合成数据生成框架，支持多种生成策略 | data-analysis, chinese, langchain | 2.4K Stars<br>国内最活跃<br>多种生成策略 |
| [Bespoke Curator](https://github.com/bespokelabsai/curator) | 合成数据策展框架，支持后训练与结构化数据生成 | data-analysis, academic | 1.7K Stars<br>后训练数据<br>结构化生成 |
| [Synthetic Data Kit](https://github.com/meta-llama/synthetic-data-kit) | Meta 出品的合成数据生成工具，支持 PDF/HTML/URL 转 QA 对 | data-analysis, open-source | 1.6K Stars<br>Meta 出品<br>PDF→QA 对 |
| [DataDreamer](https://github.com/datadreamer-dev/datadreamer) | 合成数据生成流水线框架 | data-analysis, pipeline, openai-compatible | 合成数据流水线<br>LLM 驱动<br>批量生成 |
| [Magpie](https://github.com/magpie-align/magpie) | ICLR 2025 论文，从零开始用 LLM 生成对齐数据，无需种子数据 | data-analysis, compliance, academic | 900 Stars<br>ICLR 2025<br>无需种子数据 |
| [GPT-5.4-mini](https://openai.com) | 最便宜的高质量合成数据生成 API | data-analysis, api-gateway, cost-effective | 最便宜的合成数据 API<br>高质量<br>低延迟 |

<!-- AUTOGEN_END -->

---

## 🔧 合成数据的三种模式

### 模式一：从文档生成 Q&A 对

最常见场景：**用你的文档生成训练数据，微调模型**。

```python
import openai

def generate_qa_from_doc(doc: str, n: int = 5) -> list[dict]:
    """从文档生成 Q&A 对"""
    response = openai.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[{
            "role": "user",
            "content": f"""基于以下文档，生成 {n} 个问答对。
            要求：问题多样化（事实性、推理性、总结性），答案准确。
            
            文档：{doc}
            
            返回 JSON 格式：
            [{{"question": "...", "answer": "..."}}]"""
        }]
    )
    return response.choices[0].message.content
```

### 模式二：从种子数据扩展

给 LLM 几个示例，让它生成更多类似数据。

```python
def expand_from_seeds(seeds: list[dict], n: int = 20) -> list[dict]:
    """从种子数据扩展"""
    response = openai.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[{
            "role": "user",
            "content": f"""基于以下 {len(seeds)} 个示例，生成 {n} 个类似但不同的数据。
            保持格式一致，内容多样化。
            
            示例：{seeds}
            
            返回 JSON 格式：[...]"""
        }]
    )
    return response.choices[0].message.content
```

### 模式三：用 LLM 做数据标注

让 LLM 给数据打标签，再人工校验。

```python
def label_data(texts: list[str]) -> list[dict]:
    """用 LLM 标注数据"""
    response = openai.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[{
            "role": "user",
            "content": f"""对以下文本进行情感分类（正面/负面/中性）。
            
            文本：{texts}
            
            返回 JSON 格式：[{{"text": "...", "label": "..."}}]"""
        }]
    )
    return response.choices[0].message.content
```

## 💡 工具对比

| 工具 | 类型 | 适合谁 | 特点 |
| ------ | ------ | -------- | ------ |
| [**GPT-5.4-mini**](https://openai.com) | API | 最灵活 | 便宜，质量好 |
| **DeepSeek-V4** | API | 成本敏感 | 国内最便宜 |
| [**DataDreamer**](https://github.com/datadreamer-dev/datadreamer) | 框架 | 批量生成 | 流水线化 |
| [**Argilla**](https://github.com/argilla-io/argilla) | 平台 | 人工校验 | 合成 + 人工标注 |

> [!TIP]
> **合成数据的质量控制**
> 1. **多样性**：用不同 Prompt 生成，避免模板化
> 2. **准确性**：人工抽查 10%，确认质量
> 3. **去重**：合成数据容易重复，用 Jaccard 相似度去重
> 4. **比例**：合成数据不超过总数据的 50%，否则模型学到的是 LLM 的偏见

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
