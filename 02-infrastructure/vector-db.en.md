# Vector Databases

> Last Updated: 2026-06-08
> Data Source: Automatically generated from `data/infrastructure.yaml`

---

## 🔍 What Exactly Is Vector Retrieval Doing?

The essence of vector retrieval: **turning text into a set of numbers (vectors), and then finding other text that is "closest in distance"**.

```
"Apple smartphone" → [0.12, -0.34, 0.56, ...] (1024-dimensional vector)
"iPhone"           → [0.11, -0.33, 0.55, ...] (Very close distance → Semantically similar)
"Banana"           → [0.78, 0.45, -0.12, ...] (Very far distance → Semantically different)
```

**Why not use keyword search?** Because "Apple smartphone" and "iPhone" don't share any keywords, but their semantic meaning is exactly the same.

| Retrieval Method | Can it find "iPhone"? | Can it find "Apple 16 Pro price"? | Applicable Scenario |
| --------- | ----------------- | --------------------------- | --------- |
| **Keyword (BM25)** | ❌ | ✅ | Exact match (Product names, code) |
| **Vector (Dense)** | ✅ | ❌ | Semantic search (Natural language) |
| **Hybrid Retrieval** | ✅ | ✅ | Both |

> [!TIP]
> **2026 Consensus: Hybrid Retrieval is the Standard**
> Pure vector retrieval falls severely short in exact match scenarios. If your knowledge base contains precise information like product names, code, or numbers, you must use hybrid retrieval.

---

## 📋 Vector Database Overview

<!-- AUTOGEN_START -->

### 🏗️ Distributed

| Database | Scale | Index Type | Cloud Service | Latency | Core Highlights |
| -------- | ------ | ---------- | -------- | ------ | ---------- |
| ✅ [Redis](https://github.com/redis/redis) | - | - | - | - | 74.8K Stars<br>Real-time data<br>High-performance vector |
| ✅ [TiDB](https://github.com/pingcap/tidb) | - | - | - | - | 40.1K Stars<br>Agent workloads<br>Distributed |
| ✅ [OpenViking](https://github.com/volcengine/OpenViking) | - | - | - | - | 25.3K Stars<br>By Volcengine<br>Agent context database |
| ✅ [Qdrant](https://qdrant.tech) | Billions | HNSW | [Qdrant](https://qdrant.tech) Cloud | <5ms | High performance in Rust<br>Payload filtering<br>Multi-vector support |
| ✅ [Typesense](https://github.com/typesense/typesense) | Billions | HNSW | [Typesense](https://github.com/typesense/typesense) Cloud | <5ms | Full-text + Vector hybrid search<br>Typo-tolerant search<br>Ultra-fast response |
| ✅ [Cognee](https://github.com/topoteretes/cognee) | - | - | - | - | 17.7K Stars<br>AI Memory Platform<br>Persistent memory |
| ✅ [Milvus](https://milvus.io) | Tens of billions | IVF, HNSW, DiskANN | Zilliz Cloud | <10ms | Distributed architecture<br>GPU accelerated indexing<br>IVF/HNSW/DiskANN |
| ✅ [Weaviate](https://weaviate.io) | Billions | HNSW | [Weaviate](https://weaviate.io) Cloud | <10ms | Built-in vectorization module<br>Multimodal search<br>GraphQL API |
| ✅ [Vespa](https://vespa.ai) | Tens of billions | HNSW, Custom | [Vespa](https://vespa.ai) Cloud | 1-10ms | Full-text + Vector hybrid search<br>Real-time indexing<br>Embedded ML models |
| ✅ [Elasticsearch 8.x](https://www.elastic.co/elasticsearch) | Tens of billions | HNSW | Elastic Cloud | 5-50ms | Native HNSW support<br>Full-text + Vector hybrid<br>Extremely broad ecosystem |

### 📦 Embedded

| Database | Scale | Index Type | Cloud Service | Latency | Core Highlights |
| -------- | ------ | ---------- | -------- | ------ | ---------- |
| ✅ [Chroma](https://www.trychroma.com) | Millions | HNSW | [Chroma](https://www.trychroma.com) Cloud | <10ms | Minimalist API<br>Embedded deployment<br>Automatic vectorization |
| ✅ [LanceDB](https://lancedb.com) | Tens of millions | IVF, HNSW | [LanceDB](https://lancedb.com) Cloud | <10ms | Zero-config embedded<br>Multimodal support<br>Apache Arrow format |

### ☁️ Cloud Native

| Database | Scale | Index Type | Cloud Service | Latency | Core Highlights |
| -------- | ------ | ---------- | -------- | ------ | ---------- |
| [Pinecone](https://www.pinecone.io) | Billions | Proprietary | [Pinecone](https://www.pinecone.io) | <10ms | Fully managed Serverless<br>Low maintenance<br>Hybrid search |

### 🔌 Extensions

| Database | Scale | Index Type | Cloud Service | Latency | Core Highlights |
| -------- | ------ | ---------- | -------- | ------ | ---------- |
| ✅ [pgvector](https://github.com/pgvector/pgvector) | Tens of millions | IVFFlat, HNSW | Various Cloud PG | <50ms | Based on PostgreSQL<br>No extra infrastructure needed<br>IVFFlat/HNSW indices |

### 📚 Libraries

| Database | Scale | Index Type | Cloud Service | Latency | Core Highlights |
| -------- | ------ | ---------- | -------- | ------ | ---------- |
| ✅ [FAISS](https://github.com/facebookresearch/faiss) | Billions | IVF, HNSW, PQ | — | <1ms | Open-sourced by Meta<br>GPU acceleration<br>Extreme performance |
| ✅ [txtai](https://github.com/neuml/txtai) | Millions | HNSW | — | <10ms | Semantic search<br>RAG workflows<br>Python-native |

<!-- AUTOGEN_END -->

---

## 🏛️ Two Major Camps

### Dedicated Vector Camp: Only vector retrieval, optimized to the extreme

| Database | Features | Max Scale | Deployment | Best For |
| -------- | ------ | --------- | --------- | -------- |
| [**Qdrant**](https://qdrant.tech) | Written in Rust, excellent performance | 1B+ | Docker / Cloud | Small teams' first choice |
| [**Milvus**](https://milvus.io) | Enterprise-grade, GPU acceleration | 10B+ | K8s / Cloud | Large-scale scenarios |
| [**Chroma**](https://www.trychroma.com) | Embedded, get started in 5 minutes | 10M+ | pip install | Prototyping and validation |

### Hybrid Retrieval Camp: Full-text + Vector, done in one step

| Database | Features | Full-text Search | Vector Search | Best For |
| -------- | ------ | --------- | --------- | -------- |
| **Elasticsearch** | Most mature ecosystem | ✅ Native | ✅ Native | Existing ES infrastructure |
| [**pgvector**](https://github.com/pgvector/pgvector) | PG extension, zero migration | ✅ PG Full-text | ✅ Extension | Existing PostgreSQL |
| [**Typesense**](https://github.com/typesense/typesense) | Lightweight and easy to use | ✅ Native | ✅ Extension | Small teams getting started quickly |

> [!TIP]
> **Don't know what to choose?**
> - Quick prototyping → Chroma (`pip install chromadb`)
> - Small-scale production → Qdrant (Single-node Docker)
> - Existing PG → pgvector (Handled by an extension)
> - Need hybrid retrieval → Elasticsearch / Typesense

## 💡 Simplest RAG Solution

RAG tech stack for individuals/small teams:

| Stage | Recommended Solution | Description |
| ------ | --------- | ------ |
| **Document Chunking** | Semantic chunking, 512 Tokens | Avoid fixed-character chunking to prevent semantic breakage |
| **Embedding** | BGE-M3 (Open-source) | See `01-foundation-models/embedding-reranker.md` |
| **Vector Storage** | [Chroma](https://www.trychroma.com) (Prototype) / [Qdrant](https://qdrant.tech) (Production) | Single node is sufficient for under tens of millions |
| **Reranking** | BGE-Reranker-V2 (Open-source) | Two-stage retrieval boosts accuracy by 20-40% |

**Simplest RAG Code** (Chroma + BGE-M3):
```python
# pip install chromadb FlagEmbedding
import chromadb
from FlagEmbedding import BGEM3FlagModel

model = BGEM3FlagModel('BAAI/bge-m3')
client = chromadb.Client()
collection = client.create_collection("docs")

# Indexing
docs = ["Your document fragment..."]
embeddings = model.encode(docs)['dense_vecs']
collection.add(documents=docs, embeddings=embeddings, ids=["1"])

# Retrieval
query = "User question"
query_emb = model.encode([query])['dense_vecs']
results = collection.query(query_embeddings=query_emb, n_results=5)
```

---

> **Update Frequency**: Updated quarterly
> **Automation**: Run `python scripts/build_docs.py` to re-render tables from YAML.
