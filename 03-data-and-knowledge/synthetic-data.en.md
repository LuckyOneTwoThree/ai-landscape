# Synthetic Data

> Last Updated: 2026-06-08
> Data Source: Automatically generated from `data/data-and-knowledge.yaml`

---

## 🧪 When Do You Need Synthetic Data?

| Scenario | **Need Synthetic Data?** | Reason |
| ------ | **--------------** | ------ |
| **Fine-tuning a model, but only have 100 data points** | **✅ Yes** | Data volume is too small; the model won't learn anything |
| **Training a classifier, but some classes have very few samples** | **✅ Yes** | Class imbalance; the model will be biased towards the majority class |
| **Testing a RAG system, but have no annotated data** | **✅ Yes** | Use LLMs to generate Q&A pairs for evaluation |
| **Already have 100,000 high-quality data points** | **❌ No** | Sufficient data volume; synthetic data might introduce noise |

> [!TIP]
> **The Core Value of Synthetic Data: Cold Start**
> When you don't have enough real data, generating synthetic data with LLMs is the fastest cold start solution. However, synthetic data can never completely replace real data — once real data is available, it should be progressively replaced.

---

## 📋 Synthetic Data Platforms Overview

<!-- AUTOGEN_START -->

| Name | Introduction | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [Cleanlab](https://github.com/cleanlab/cleanlab) | Data quality tool, automatically detects labeling errors/outliers, improves training data quality | data-analysis | 11.5K Stars<br>Data quality<br>Automatically detects labeling errors |
| [Distilabel](https://github.com/argilla-io/distilabel) | Synthetic data generation framework from [Argilla](https://github.com/argilla-io/argilla) | data-analysis, openai-compatible, pipeline | Efficient programmable data generation pipeline designed for LLMs<br>Built-in LLM-as-a-judge intelligent filtering and scoring<br>Direct export in minimal format compatible with SFT/DPO |
| [Argilla](https://github.com/argilla-io/argilla) | Data annotation and synthetic data platform, supporting human-in-the-loop collaboration | data-analysis, collaboration | Top-tier annotation collaboration UI built for RLHF<br>Seamlessly integrates with [Distilabel](https://github.com/argilla-io/distilabel) to form a closed loop<br>Must-have desktop tool for fine-grained data cleaning in small teams |
| [SDG (Synthetic Data Generator)](https://github.com/hitsz-ids/synthetic-data-generator) | The most active synthetic data generation framework in China, supporting multiple generation strategies | data-analysis, chinese, langchain | 2.4K Stars<br>Most active in China<br>Multiple generation strategies |
| [Bespoke Curator](https://github.com/bespokelabsai/curator) | Synthetic data curation framework, supporting post-training and structured data generation | data-analysis, academic | 1.7K Stars<br>Post-training data<br>Structured generation |
| [Synthetic Data Kit](https://github.com/meta-llama/synthetic-data-kit) | Synthetic data generation tool from Meta, supporting PDF/HTML/URL to QA pairs | data-analysis, open-source | 1.6K Stars<br>From Meta<br>PDF→QA pairs |
| [DataDreamer](https://github.com/datadreamer-dev/datadreamer) | Synthetic data generation pipeline framework | data-analysis, pipeline, openai-compatible | Synthetic data pipeline<br>LLM-driven<br>Batch generation |
| [Magpie](https://github.com/magpie-align/magpie) | ICLR 2025 paper, generating alignment data from scratch using LLMs without seed data | data-analysis, compliance, academic | 900 Stars<br>ICLR 2025<br>No seed data required |
| [GPT-5.4-mini](https://openai.com) | The cheapest high-quality synthetic data generation API | data-analysis, api-gateway, cost-effective | Cheapest synthetic data API<br>High quality<br>Low latency |

<!-- AUTOGEN_END -->

---

## 🔧 Three Modes of Synthetic Data

### Mode 1: Generate Q&A Pairs from Documents

Most common scenario: **Generate training data from your documents to fine-tune models**.

```python
import openai

def generate_qa_from_doc(doc: str, n: int = 5) -> list[dict]:
    """Generate Q&A pairs from a document"""
    response = openai.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[{
            "role": "user",
            "content": f"""Based on the following document, generate {n} Q&A pairs.
            Requirements: Diversified questions (factual, inferential, summarization), accurate answers.
            
            Document: {doc}
            
            Return JSON format:
            [{{"question": "...", "answer": "..."}}]"""
        }]
    )
    return response.choices[0].message.content
```

### Mode 2: Expand from Seed Data

Provide the LLM with a few examples and ask it to generate more similar data.

```python
def expand_from_seeds(seeds: list[dict], n: int = 20) -> list[dict]:
    """Expand from seed data"""
    response = openai.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[{
            "role": "user",
            "content": f"""Based on the following {len(seeds)} examples, generate {n} similar but different data points.
            Maintain consistent formatting and diverse content.
            
            Examples: {seeds}
            
            Return JSON format: [...]"""
        }]
    )
    return response.choices[0].message.content
```

### Mode 3: Use LLM for Data Annotation

Have the LLM label data, followed by manual verification.

```python
def label_data(texts: list[str]) -> list[dict]:
    """Annotate data using LLM"""
    response = openai.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[{
            "role": "user",
            "content": f"""Perform sentiment classification on the following texts (Positive/Negative/Neutral).
            
            Texts: {texts}
            
            Return JSON format: [{{"text": "...", "label": "..."}}]"""
        }]
    )
    return response.choices[0].message.content
```

## 💡 Tool Comparison

| Tool | Type | Best For | Features |
| ------ | ------ | -------- | ------ |
| [**GPT-5.4-mini**](https://openai.com) | API | Most flexible | Cheap, high quality |
| **DeepSeek-V4** | API | Cost-sensitive | Cheapest in China |
| [**DataDreamer**](https://github.com/datadreamer-dev/datadreamer) | Framework | Batch generation | Pipelined |
| [**Argilla**](https://github.com/argilla-io/argilla) | Platform | Manual verification | Synthetic + Human annotation |

> [!TIP]
> **Quality Control for Synthetic Data**
> 1. **Diversity**: Generate with different Prompts to avoid templating.
> 2. **Accuracy**: Manually spot-check 10% to verify quality.
> 3. **Deduplication**: Synthetic data is prone to repetition; use Jaccard similarity for deduplication.
> 4. **Proportion**: Synthetic data should not exceed 50% of total data, otherwise the model will learn the LLM's biases.

---

> **Update Frequency**: Quarterly updates
> **Automation**: Run `python scripts/build_docs.py` to re-render tables from YAML.
