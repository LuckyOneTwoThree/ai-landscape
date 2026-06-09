# 嵌入与检索模型

> 最后更新：2026-06-08
> 数据来源：`data/models.yaml` 自动生成

---

## 🧠 RAG 检索架构最佳组合

在 2026 年，单纯比较"最大维度"已经过时。现代企业级 RAG 架构更加关注**多模态融合检索**以及通过 **Matryoshka (套娃) 弹性维度**来平衡成本与精度。

| 架构需求 | 推荐 Embedding | 推荐 Reranker | 组合优势 |
| --------- | --------------- | -------------- | --------- |
| **全能商业旗舰** | [**Cohere Embed v4**](https://cohere.com) | [Cohere Rerank v3](https://cohere.com) | 支持文本+图表混排，Matryoshka 弹性维度 |
| **开源首选** | [**BGE-M3**](https://github.com/FlagOpen/FlagEmbedding) | **[BGE-Reranker-V2](https://github.com/FlagOpen/FlagEmbedding)** | 稀疏+密集双检索，本地部署极高召回 |
| **中文深层语义** | [**GTE-Qwen2**](https://huggingface.co/Alibaba-NLP/gte-Qwen2) | [BGE-Reranker-V2](https://github.com/FlagOpen/FlagEmbedding) | 中文多义词、生僻字、专业领域优化 |
| **超长上下文 (32K+)** | [**Jina v5 Omni**](https://jina.ai) | [Jina Reranker](https://jina.ai) | 32K 上下文嵌入，无需切割 PDF |
| **代码片段检索** | **Codestral Embed** | — | 专精 AST 结构与函数级召回 |

> [!TIP]
> **Embedding + Reranker 两阶段检索是标配**
> 单纯的向量检索召回率有限。先用 Embedding 召回 Top-50，再用 Reranker 精排到 Top-5，可以将检索准确率提升 20-40%。

---

## 📋 嵌入与检索模型总览

<!-- 以下内容由脚本自动生成，请勿手动修改 -->
<!-- AUTOGEN_START -->

### 📐 Embedding 模型

| 模型与版本 | 维度 | 最大Token | MTEB 评分 | 核心亮点 |
|------------|------|----------|-----------|----------|
| [BGE-M3](https://github.com/FlagOpen/FlagEmbedding) | 1024 | 8192 | 66.1 | 支持 100+ 语言<br>稀疏与密集双检索<br>MIT 开源 |
| [text-embedding-3-large/small](https://openai.com) | 3072 | 8191 | 64.6 | large/small 分层<br>维度可调<br>性能领先 |
| [voyage-4-large](https://voyageai.com) | 1024 | 32000 | 领先 | 同尺寸最高检索精度<br>原生支持 32K 上下文<br>更低的商业调用成本 |
| [GTE-Qwen2](https://huggingface.co/Alibaba-NLP/gte-Qwen2) | 1536 | 8192 | 63.5 | 中文优化<br>Apache 2.0 开源<br>Qwen2 架构 |
| [jina-embeddings-v5-omni](https://jina.ai) | 1024 | 8192 | 65.5 | 全模态统一潜空间<br>开源可私有化部署<br>32K 超长上下文 |
| [cohere-embed-v4<br>*(API: `cohere-embed-v4`)*](https://cohere.com) | 256/1024/3072 | 128000 | - | 真正交织文本、图像与图表<br>Matryoshka 弹性维度配置<br>支持 100+ 语种 |

### 🔄 Reranker 模型

| 模型与版本 | 维度 | 最大Token | MTEB 评分 | 核心亮点 |
|------------|------|----------|-----------|----------|
| [BGE-Reranker-V2](https://github.com/FlagOpen/FlagEmbedding) | - | 512 | 67.3 | 开源 Reranker 标杆<br>配合 BGE-M3 最佳<br>MIT 开源 |

<!-- AUTOGEN_END -->
<!-- 以上内容由脚本自动生成 -->

---

## 🔧 维度选择指南

| 维度 | 精度 | 存储成本 | 检索速度 | 适用场景 |
| ------ | ------ | --------- | --------- | --------- |
| **256** | 低 | 最低 | 最快 | 原型验证，资源受限 |
| **1024** | 中 | 中 | 快 | 通用 RAG，性价比最优 |
| **1536** | 高 | 较高 | 中 | 中文语义，专业领域 |
| **3072** | 最高 | 最高 | 慢 | 精度优先，大规模知识库 |

> [!TIP]
> **Matryoshka 维度的妙用**
> Cohere Embed v4 和 text-embedding-3 支持 Matryoshka 维度，可以用 256 维做粗筛，再用 1024 维精排。这种分层检索可以在保持精度的同时将存储成本降低 4 倍。

## 💡 RAG 最佳实践

| 环节 | 推荐方案 | 说明 |
| ------ | --------- | ------ |
| **文档切分** | 按语义切分 (512 Token) | 避免按固定字符切分破坏语义 |
| **Embedding** | [BGE-M3](https://github.com/FlagOpen/FlagEmbedding) (开源) / Cohere (商业) | 稀疏+密集双检索效果最佳 |
| **向量存储** | Milvus / Qdrant / pgvector | 参见 `02-infrastructure/vector-db.md` |
| **Reranking** | [BGE-Reranker-V2](https://github.com/FlagOpen/FlagEmbedding) / [Cohere Rerank](https://cohere.com) | 两阶段检索提升 20-40% 准确率 |
| **混合搜索** | Elasticsearch / Vespa | 全文+向量混合，精确+语义 |

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
