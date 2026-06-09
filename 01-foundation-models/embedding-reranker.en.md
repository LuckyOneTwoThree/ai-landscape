# Embedding and Retrieval Models

> Last Updated: 2026-06-08
> Data Source: Auto-generated from `data/models.yaml`

---

## 🧠 Best Combinations for RAG Retrieval Architectures

In 2026, simply comparing "maximum dimensions" is obsolete. Modern enterprise-grade RAG architectures focus more on **multimodal hybrid retrieval** and balancing cost and precision through **Matryoshka (nested) elastic dimensions**.

| Architecture Need | **Recommended Embedding** | Recommended Reranker | Combination Advantage |
| ------------------- | ----------------------- | ---------------------- | ----------------------- |
| **All-Round Commercial Flagship** | **[Cohere Embed v4](https://cohere.com)** | [Cohere Rerank v3](https://cohere.com) | Supports text + chart interleaving, Matryoshka elastic dimensions |
| **Top Open Source** | **[BGE-M3](https://github.com/FlagOpen/FlagEmbedding)** | **[BGE-Reranker-V2](https://github.com/FlagOpen/FlagEmbedding)** | Sparse + dense dual retrieval, extremely high recall for local deployment |
| **Chinese Deep Semantics** | **[GTE-Qwen2](https://huggingface.co/Alibaba-NLP/gte-Qwen2)** | [BGE-Reranker-V2](https://github.com/FlagOpen/FlagEmbedding) | Optimized for Chinese polysemy, rare characters, and specialized domains |
| **Ultra-Long Context (32K+)** | **[Jina v5 Omni](https://jina.ai)** | [Jina Reranker](https://jina.ai) | 32K context embedding, no need to chunk PDFs |
| **Code Snippet Retrieval** | **Codestral Embed** | — | Specialized in AST structures and function-level recall |

> [!TIP]
> **Two-Stage Retrieval (Embedding + Reranker) is the Standard**
> Pure vector retrieval has limited recall. First using Embedding to recall the Top-50, then using a Reranker to precision-rank to the Top-5, can improve retrieval accuracy by 20-40%.

---

## 📋 Embedding and Retrieval Models Overview

<!-- 以下内容由脚本自动生成，请勿手动修改 -->
<!-- AUTOGEN_START -->

### 📐 Embedding Models

| Model and Version | Dimensions | Max Tokens | MTEB Score | Core Highlights |
| ------------------- | ------------ | ------------ | ------------ | ----------------- |
| [BGE-M3](https://github.com/FlagOpen/FlagEmbedding) | 1024 | 8192 | 66.1 | Supports 100+ languages<br>Sparse and dense dual retrieval<br>MIT open source |
| [text-embedding-3-large/small](https://openai.com) | 3072 | 8191 | 64.6 | Large/[small](https://openai.com) tiers<br>Adjustable dimensions<br>Leading performance |
| [voyage-4-large](https://voyageai.com) | 1024 | 32000 | Leading | Highest retrieval precision at same size<br>Native support for 32K context<br>Lower commercial API costs |
| [GTE-Qwen2](https://huggingface.co/Alibaba-NLP/gte-Qwen2) | 1536 | 8192 | 63.5 | Chinese optimization<br>Apache 2.0 open source<br>Qwen2 architecture |
| [jina-embeddings-v5-omni](https://jina.ai) | 1024 | 8192 | 65.5 | Omnimodal unified latent space<br>Open source, supports private deployment<br>32K ultra-long context |
| [cohere-embed-v4<br>*(API: `cohere-embed-v4`)*](https://cohere.com) | 256/1024/3072 | 128000 | - | Truly interleaves text, images, and charts<br>Matryoshka elastic dimension configuration<br>Supports 100+ languages |

### 🔄 Reranker Models

| Model and Version | Dimensions | Max Tokens | MTEB Score | Core Highlights |
| ------------------- | ------------ | ------------ | ------------ | ----------------- |
| [BGE-Reranker-V2](https://github.com/FlagOpen/FlagEmbedding) | - | 512 | 67.3 | Open source Reranker benchmark<br>Best paired with [BGE-M3](https://github.com/FlagOpen/FlagEmbedding)<br>MIT open source |

<!-- AUTOGEN_END -->
<!-- 以上内容由脚本自动生成 -->

---

## 🔧 Dimension Selection Guide

| Dimensions | Precision | Storage Cost | Retrieval Speed | Suitable Scenarios |
| ------------ | ----------- | -------------- | ----------------- | -------------------- |
| **256** | Low | Lowest | Fastest | Prototype validation, resource-constrained |
| **1024** | Medium | Medium | Fast | General RAG, best cost-performance |
| **1536** | High | Higher | Medium | Chinese semantics, specialized domains |
| **3072** | Highest | Highest | Slow | Precision-first, large-scale knowledge bases |

> [!TIP]
> **The Magic of Matryoshka Dimensions**
> Cohere Embed v4 and text-embedding-3 support Matryoshka dimensions. You can use 256 dimensions for coarse filtering, then 1024 dimensions for precise ranking. This hierarchical retrieval can reduce storage costs by 4 times while maintaining precision.

## 💡 RAG Best Practices

| Component | Recommended Solution | Description |
| ----------- | ---------------------- | ------------- |
| **Document Chunking** | Semantic chunking (512 Tokens) | Avoid fixed-character chunking to preserve semantics |
| **Embedding** | [BGE-M3](https://github.com/FlagOpen/FlagEmbedding) (Open Source) / Cohere (Commercial) | Best results with sparse + dense dual retrieval |
| **Vector Storage** | Milvus / Qdrant / pgvector | See `02-infrastructure/vector-db.md` |
| **Reranking** | [BGE-Reranker-V2](https://github.com/FlagOpen/FlagEmbedding) / [Cohere Rerank](https://cohere.com) | Two-stage retrieval improves accuracy by 20-40% |
| **Hybrid Search** | Elasticsearch / Vespa | Full-text + vector hybrid, exact match + semantic |

---

> **Update Frequency**: Updated quarterly
> **Automation**: Run `python scripts/build_docs.py` to re-render tables from YAML.
