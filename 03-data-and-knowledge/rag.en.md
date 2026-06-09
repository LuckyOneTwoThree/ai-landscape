# RAG Knowledge Base

> Last Updated: 2026-06-08
> Data Source: Automatically generated from `data/data-and-knowledge.yaml`

---

## 🔗 Data Pipeline Landscape

RAG is not isolated; it is the core segment of the data pipeline. Here is the sequential relationship of the four files in module 03:

```
Raw Data (PDF/HTML/Database)
  ↓
📄 Document Parsing (data-parsing.md) → MinerU / Docling / LlamaParse
  ↓ Structured Text + Tables
🕸️ Knowledge Graph (knowledge-graph.md) → Neo4j / LightRAG / GraphRAG  (Optional, when entity relationships are dense)
  ↓
🔍 RAG Knowledge Base (This File) → Embedding + Vector Retrieval + Reranking + LLM Generation
  ↓
🧪 Synthetic Data (synthetic-data.md) → Distilabel / Argilla  (Optional, for evaluation/QA pair generation)
```

> [!TIP]
> **90% of scenarios only need the main line: "Document Parsing → RAG"**. Knowledge graphs and synthetic data are icing on the cake, not absolute necessities.

---

## 🔄 Complete RAG Workflow

The essence of RAG (Retrieval-Augmented Generation): **First find relevant content from your documents, then have the LLM answer based on that content**.

```
User Query
  ↓
Embedding (Convert query to vector)
  ↓
Vector Retrieval (Find the most relevant document chunks)
  ↓
Reranking (Fine sorting, filter out false recalls)
  ↓
LLM Generation (Answer based on retrieved results)
  ↓
Answer + Source Citations
```

**Common Pitfalls in Each Step**:

| Step | Common Pitfall | Solution |
| ------ | -------- | --------- |
| **Document Splitting** | Splitting by fixed characters, destroying semantics | Split by semantics (paragraph, sentence boundaries) |
| **Embedding** | Using general models, inaccurate for professional terms | Fine-tune or use domain-specific models |
| **Vector Retrieval** | Only using Dense, weak exact match | Hybrid retrieval (Dense + BM25) |
| **Reranking** | Skipping this step, many noisy recalls | Two-stage retrieval, improves 20-40% |
| **LLM Generation** | No citations provided, severe hallucinations | Require LLM to annotate source citations |

---

## 📋 Knowledge Base Ecosystem Overview

<!-- AUTOGEN_START -->

| Name | Introduction | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [PrivateGPT](https://github.com/zylon-ai/private-gpt) | 100% private RAG system, no internet needed, supports local LLMs + local vector databases | rag, self-hosted | 55K Stars<br>100% private<br>No internet required |
| [RAGFlow](https://github.com/infiniflow/ragflow) | Open-source RAG engine, deep document understanding + retrieval augmentation | rag, pipeline, document | Open-source RAG engine<br>Deep document understanding<br>40K Stars |
| [Quivr](https://github.com/QuivrHQ/quivr) | Personal AI assistant, supports RAG knowledge bases in various file formats | rag, self-hosted, pipeline | 36K Stars<br>Personal assistant<br>Multi-format support |
| [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) | Out-of-the-box RAG desktop app, supports various LLMs | rag, desktop, low-code | Out-of-the-box RAG<br>Desktop application<br>35K Stars |
| [Khoj](https://github.com/khoj-ai/khoj) | Open-source AI personal assistant, supports RAG for Obsidian/Notion/local files | rag, document, self-hosted | 25K Stars<br>Obsidian integration<br>Personal assistant |
| [Verba](https://github.com/weaviate/Verba) | Out-of-the-box RAG app from Weaviate, GoldRAG retrieval strategy | rag, easy-to-use | 7K Stars<br>From Weaviate<br>Out-of-the-box |

<!-- AUTOGEN_END -->

---

## 📊 Splitting Strategies Comparison

Splitting is the **most underestimated step** in RAG. If splitting is done poorly, everything afterwards is in vain.

| Strategy | Method | Pros | Cons | Applicable Scenarios |
| ------ | ------ | ------ | ------ | --------- |
| **Fixed Characters** | Split a chunk every 500 characters | Simplest | Destroys semantics | ❌ Not recommended |
| **By Paragraph** | Separate by empty lines | Preserves paragraph semantics | Uneven paragraph lengths | General documents |
| **By Semantics** | Determine boundaries using Embedding similarity | Complete semantics | High computation cost | High-quality RAG |
| **Recursive Splitting** | Big chunks first, then small chunks | Flexible | Complex to implement | LangChain default |

> [!TIP]
> **Recommended: LangChain's RecursiveCharacterTextSplitter**
> ```python
> from langchain.text_splitter import RecursiveCharacterTextSplitter
> splitter = RecursiveCharacterTextSplitter(
>     chunk_size=512,
>     chunk_overlap=50,
>     separators=["\n\n", "\n", "。", "！", "？", " "]
> )
> chunks = splitter.split_text(text)
> ```
> `chunk_size=512` + `chunk_overlap=50` is the best starting point for most scenarios.

## 💡 Minimal RAG Solution

Tech stack recommendation for individuals/small teams:

| Step | Recommended Solution | Description |
| ------ | --------- | ------ |
| **Document Parsing** | MinerU / Marker | See `data-parsing.md` |
| **Document Splitting** | RecursiveCharacterTextSplitter | chunk_size=512 |
| **Embedding** | BGE-M3 (Open-source) | See `01-foundation-models/embedding-reranker.md` |
| **Vector Storage** | Chroma (Prototype) / Qdrant (Production) | See `02-infrastructure/vector-db.md` |
| **Reranking** | BGE-Reranker-V2 (Open-source) | Two-stage retrieval improves accuracy |
| **LLM** | [DeepSeek-V4-Flash](https://deepseek.com) / [Claude Sonnet 4](https://anthropic.com) | See `01-foundation-models/llm.md` |

**Minimal RAG Code** (LangChain + Chroma):
```python
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# 1. Load document
loader = PyMuPDFLoader("document.pdf")
docs = loader.load()

# 2. Split
splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# 3. Vectorize + Store
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-m3")
vectorstore = Chroma.from_documents(chunks, embeddings)

# 4. Retrieve
results = vectorstore.similarity_search("User query", k=5)
```

## 📈 RAG Evaluation Metrics

How do you know if your RAG is performing well?

| Metric | Meaning | How to Measure |
| ------ | ------ | -------- |
| **Recall Rate** | Are relevant documents retrieved? | Manual annotation + automatic calculation |
| **Precision** | Are the retrieved documents relevant? | Manual annotation + automatic calculation |
| **Faithfulness** | Is the LLM answer based on retrieved results? | LLM-as-Judge |
| **Relevance** | Does the LLM answer address the question? | LLM-as-Judge |

> [!TIP]
> **Fast Evaluation Method**
> Prepare 10-20 typical questions + expected answers, run them through RAG, and manually check:
> 1. Do the retrieved documents contain the answer? (Recall Rate)
> 2. Is the LLM's answer correct? (Faithfulness + Relevance)
>
> If the recall rate is low → Optimize Embedding or splitting strategy
> If faithfulness is low → Optimize Prompt or switch to a stronger LLM

---

> **Update Frequency**: Quarterly updates
> **Automation**: Run `python scripts/build_docs.py` to re-render tables from YAML.
