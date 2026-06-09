# 向量数据库

> 最后更新：2026-06-08
> 数据来源：`data/infrastructure.yaml` 自动生成

---

## 🔍 向量检索到底在干什么？

向量检索的本质：**把文本变成一组数字（向量），然后找到"距离最近"的其他文本**。

```
"苹果手机" → [0.12, -0.34, 0.56, ...] (1024 维向量)
"iPhone"   → [0.11, -0.33, 0.55, ...] (距离很近 → 语义相似)
"香蕉"     → [0.78, 0.45, -0.12, ...] (距离很远 → 语义不同)
```

**为什么不用关键词搜索？** 因为"苹果手机"和"iPhone"没有任何共同关键词，但语义完全相同。

| 检索方式 | 能搜到"iPhone"吗 | 能搜到"苹果 16 Pro 价格"吗 | 适用场景 |
| --------- | ----------------- | --------------------------- | --------- |
| **关键词 (BM25)** | ❌ | ✅ | 精确匹配（产品名、代码） |
| **向量 (Dense)** | ✅ | ❌ | 语义搜索（自然语言） |
| **混合检索** | ✅ | ✅ | 两者兼顾 |

> [!TIP]
> **2026 年的共识：混合检索是标配**
> 纯向量检索在精确匹配场景下严重不足。如果你的知识库包含产品名、代码、数字等精确信息，一定要用混合检索。

---

## 📋 向量数据库总览

<!-- AUTOGEN_START -->

### 🏗️ 分布式

| 数据库 | 规模 | 索引类型 | 云服务 | 延迟 | 核心亮点 |
| -------- | ------ | ---------- | -------- | ------ | ---------- |
| ✅ [Redis](https://github.com/redis/redis) | - | - | - | - | 74.8K Stars<br>实时数据<br>高性能向量 |
| ✅ [TiDB](https://github.com/pingcap/tidb) | - | - | - | - | 40.1K Stars<br>Agent 工作负载<br>分布式 |
| ✅ [OpenViking](https://github.com/volcengine/OpenViking) | - | - | - | - | 25.3K Stars<br>火山引擎出品<br>Agent 上下文数据库 |
| ✅ [Qdrant](https://qdrant.tech) | 十亿级 | HNSW | [Qdrant](https://qdrant.tech) Cloud | <5ms | Rust 编写高性能<br>Payload 过滤<br>多向量支持 |
| ✅ [Typesense](https://github.com/typesense/typesense) | 十亿级 | HNSW | [Typesense](https://github.com/typesense/typesense) Cloud | <5ms | 全文+向量混合搜索<br>容错搜索 (typo-tolerant)<br>极速响应 |
| ✅ [Cognee](https://github.com/topoteretes/cognee) | - | - | - | - | 17.7K Stars<br>AI 记忆平台<br>持久化记忆 |
| ✅ [Milvus](https://milvus.io) | 百亿级 | IVF, HNSW, DiskANN | Zilliz Cloud | <10ms | 分布式架构<br>GPU 加速索引<br>IVF/HNSW/DiskANN |
| ✅ [Weaviate](https://weaviate.io) | 十亿级 | HNSW | [Weaviate](https://weaviate.io) Cloud | <10ms | 内置向量化模块<br>多模态搜索<br>GraphQL API |
| ✅ [Vespa](https://vespa.ai) | 百亿级 | HNSW, 自定义 | [Vespa](https://vespa.ai) Cloud | 1-10ms | 全文+向量混合搜索<br>实时索引<br>ML 模型内嵌 |
| ✅ [Elasticsearch 8.x](https://www.elastic.co/elasticsearch) | 百亿级 | HNSW | Elastic Cloud | 5-50ms | HNSW 原生支持<br>全文+向量混合<br>生态极其广泛 |

### 📦 嵌入式

| 数据库 | 规模 | 索引类型 | 云服务 | 延迟 | 核心亮点 |
| -------- | ------ | ---------- | -------- | ------ | ---------- |
| ✅ [Chroma](https://www.trychroma.com) | 百万级 | HNSW | [Chroma](https://www.trychroma.com) Cloud | <10ms | 极简 API<br>嵌入式部署<br>自动向量化 |
| ✅ [LanceDB](https://lancedb.com) | 千万级 | IVF, HNSW | [LanceDB](https://lancedb.com) Cloud | <10ms | 零配置嵌入式<br>多模态支持<br>Apache Arrow 格式 |

### ☁️ 云原生

| 数据库 | 规模 | 索引类型 | 云服务 | 延迟 | 核心亮点 |
| -------- | ------ | ---------- | -------- | ------ | ---------- |
| [Pinecone](https://www.pinecone.io) | 十亿级 | 专有 | [Pinecone](https://www.pinecone.io) | <10ms | 全托管 Serverless<br>低运维<br>混合搜索 |

### 🔌 扩展

| 数据库 | 规模 | 索引类型 | 云服务 | 延迟 | 核心亮点 |
| -------- | ------ | ---------- | -------- | ------ | ---------- |
| ✅ [pgvector](https://github.com/pgvector/pgvector) | 千万级 | IVFFlat, HNSW | 各云厂商 PG | <50ms | 基于 PostgreSQL<br>无需额外基础设施<br>IVFFlat/HNSW 索引 |

### 📚 库

| 数据库 | 规模 | 索引类型 | 云服务 | 延迟 | 核心亮点 |
| -------- | ------ | ---------- | -------- | ------ | ---------- |
| ✅ [FAISS](https://github.com/facebookresearch/faiss) | 十亿级 | IVF, HNSW, PQ | — | <1ms | Meta 开源<br>GPU 加速<br>极致性能 |
| ✅ [txtai](https://github.com/neuml/txtai) | 百万级 | HNSW | — | <10ms | 语义搜索<br>RAG 工作流<br>Python 原生 |

<!-- AUTOGEN_END -->

---

## 🏛️ 两大阵营

### 专精向量派：只做向量检索，做到极致

| 数据库 | 特点 | 最大规模 | 部署方式 | 适合谁 |
| -------- | ------ | --------- | --------- | -------- |
| [**Qdrant**](https://qdrant.tech) | Rust 写的，性能极好 | 10 亿+ | Docker / Cloud | 小团队首选 |
| [**Milvus**](https://milvus.io) | 企业级，GPU 加速 | 100 亿+ | K8s / Cloud | 大规模场景 |
| [**Chroma**](https://www.trychroma.com) | 嵌入式，5 分钟上手 | 千万级 | pip install | 原型验证 |

### 混合检索派：全文 + 向量，一步到位

| 数据库 | 特点 | 全文检索 | 向量检索 | 适合谁 |
| -------- | ------ | --------- | --------- | -------- |
| **Elasticsearch** | 生态最成熟 | ✅ 原生 | ✅ 原生 | 已有 ES 基建 |
| [**pgvector**](https://github.com/pgvector/pgvector) | PG 扩展，零迁移 | ✅ PG 全文 | ✅ 扩展 | 已有 PostgreSQL |
| [**Typesense**](https://github.com/typesense/typesense) | 轻量易用 | ✅ 原生 | ✅ 扩展 | 小团队快速上手 |

> [!TIP]
> **不知道选什么？**
> - 快速原型 → Chroma（`pip install chromadb`）
> - 小规模生产 → Qdrant（单机 Docker）
> - 已有 PG → pgvector（一个扩展搞定）
> - 需要混合检索 → Elasticsearch / Typesense

## 💡 RAG 最简方案

个人/小团队的 RAG 技术栈：

| 环节 | 推荐方案 | 说明 |
| ------ | --------- | ------ |
| **文档切分** | 按语义切分，512 Token | 避免按固定字符切分破坏语义 |
| **Embedding** | BGE-M3 (开源) | 参见 `01-foundation-models/embedding-reranker.md` |
| **向量存储** | [Chroma](https://www.trychroma.com) (原型) / [Qdrant](https://qdrant.tech) (生产) | 千万级以下单机足够 |
| **Reranking** | BGE-Reranker-V2 (开源) | 两阶段检索提升 20-40% 准确率 |

**最简 RAG 代码**（Chroma + BGE-M3）：
```python
# pip install chromadb FlagEmbedding
import chromadb
from FlagEmbedding import BGEM3FlagModel

model = BGEM3FlagModel('BAAI/bge-m3')
client = chromadb.Client()
collection = client.create_collection("docs")

# 索引
docs = ["你的文档片段..."]
embeddings = model.encode(docs)['dense_vecs']
collection.add(documents=docs, embeddings=embeddings, ids=["1"])

# 检索
query = "用户问题"
query_emb = model.encode([query])['dense_vecs']
results = collection.query(query_embeddings=query_emb, n_results=5)
```

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
