# RAG 知识库

> 最后更新：2026-06-08
> 数据来源：`data/data-and-knowledge.yaml` 自动生成

---

## 🔗 数据管线全景图

RAG 不是孤立的，它是数据管线的核心环节。以下是 03 模块四个文件的串联关系：

```
原始数据 (PDF/HTML/数据库)
  ↓
📄 文档解析 (data-parsing.md) → MinerU / Docling / LlamaParse
  ↓ 结构化文本 + 表格
🕸️ 知识图谱 (knowledge-graph.md) → Neo4j / LightRAG / GraphRAG  (可选，实体关系密集时)
  ↓
🔍 RAG 知识库 (本文件) → Embedding + 向量检索 + Reranking + LLM 生成
  ↓
🧪 合成数据 (synthetic-data.md) → Distilabel / Argilla  (可选，评估/QA对生成)
```

> [!TIP]
> **90% 的场景只需要"文档解析 → RAG"这条主线**。知识图谱和合成数据是锦上添花，不是必需品。

---

## 🔄 RAG 的完整流程

RAG (Retrieval-Augmented Generation) 的本质：**先从你的文档里找到相关内容，再让 LLM 基于这些内容回答**。

```
用户问题
  ↓
Embedding (把问题变成向量)
  ↓
向量检索 (找到最相关的文档片段)
  ↓
Reranking (精排，去掉误召回)
  ↓
LLM 生成 (基于检索结果回答)
  ↓
回答 + 引用来源
```

**每个环节的常见坑**：

| 环节 | 常见坑 | 解决方案 |
| ------ | -------- | --------- |
| **文档切分** | 按固定字符切分，破坏语义 | 按语义切分（段落、句子边界） |
| **Embedding** | 用通用模型，专业术语不准 | 微调或用专业领域模型 |
| **向量检索** | 只用 Dense，精确匹配弱 | 混合检索（Dense + BM25） |
| **Reranking** | 跳过这一步，召回噪声多 | 两阶段检索，提升 20-40% |
| **LLM 生成** | 没给引用，幻觉严重 | 要求 LLM 标注引用来源 |

---

## 📋 知识库生态总览

<!-- AUTOGEN_START -->

| 名称 | 简介 | 标签 | 亮点 |
| ------ | ------ | ------ | ------ |
| [PrivateGPT](https://github.com/zylon-ai/private-gpt) | 100% 私有 RAG 系统，无需联网，支持本地 LLM + 本地向量库 | rag, self-hosted | 55K Stars<br>100% 私有<br>无需联网 |
| [RAGFlow](https://github.com/infiniflow/ragflow) | 开源 RAG 引擎，深度文档理解 + 检索增强 | rag, pipeline, document | 开源 RAG 引擎<br>深度文档理解<br>40K Stars |
| [Quivr](https://github.com/QuivrHQ/quivr) | 个人 AI 助手，支持多种文件格式的 RAG 知识库 | rag, self-hosted, pipeline | 36K Stars<br>个人助手<br>多格式支持 |
| [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm) | 开箱即用的 RAG 桌面应用，支持多种 LLM | rag, desktop, low-code | 开箱即用 RAG<br>桌面应用<br>35K Stars |
| [Khoj](https://github.com/khoj-ai/khoj) | 开源 AI 个人助理，支持 Obsidian/Notion/本地文件的 RAG | rag, document, self-hosted | 25K Stars<br>Obsidian 集成<br>个人助理 |
| [Verba](https://github.com/weaviate/Verba) | Weaviate 出品的开箱即用 RAG 应用，GoldRAG 检索策略 | rag, easy-to-use | 7K Stars<br>Weaviate 出品<br>开箱即用 |

<!-- AUTOGEN_END -->

---

## 📊 切分策略对比

切分是 RAG 中**最被低估的环节**。切分不好，后面全白费。

| 策略 | 方法 | 优点 | 缺点 | 适用场景 |
| ------ | ------ | ------ | ------ | --------- |
| **固定字符** | 每 500 字符切一段 | 最简单 | 破坏语义 | ❌ 不推荐 |
| **按段落** | 以空行分隔 | 保留段落语义 | 段落长度不均 | 通用文档 |
| **按语义** | 用 Embedding 相似度判断边界 | 语义完整 | 计算量大 | 高质量 RAG |
| **递归切分** | 先按大块，再按小块 | 灵活 | 实现复杂 | LangChain 默认 |

> [!TIP]
> **推荐：LangChain 的 RecursiveCharacterTextSplitter**
> ```python
> from langchain.text_splitter import RecursiveCharacterTextSplitter
> splitter = RecursiveCharacterTextSplitter(
>     chunk_size=512,
>     chunk_overlap=50,
>     separators=["\n\n", "\n", "。", "！", "？", " "]
> )
> chunks = splitter.split_text(text)
> ```
> `chunk_size=512` + `chunk_overlap=50` 是大多数场景的最佳起点。

## 💡 最简 RAG 方案

个人/小团队的技术栈推荐：

| 环节 | 推荐方案 | 说明 |
| ------ | --------- | ------ |
| **文档解析** | MinerU / Marker | 参见 `data-parsing.md` |
| **文档切分** | RecursiveCharacterTextSplitter | chunk_size=512 |
| **Embedding** | BGE-M3 (开源) | 参见 `01-foundation-models/embedding-reranker.md` |
| **向量存储** | Chroma (原型) / Qdrant (生产) | 参见 `02-infrastructure/vector-db.md` |
| **Reranking** | BGE-Reranker-V2 (开源) | 两阶段检索提升准确率 |
| **LLM** | [DeepSeek-V4-Flash](https://deepseek.com) / [Claude Sonnet 4](https://anthropic.com) | 参见 `01-foundation-models/llm.md` |

**最简 RAG 代码**（LangChain + Chroma）：
```python
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# 1. 加载文档
loader = PyMuPDFLoader("document.pdf")
docs = loader.load()

# 2. 切分
splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=50)
chunks = splitter.split_documents(docs)

# 3. 向量化 + 存储
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-m3")
vectorstore = Chroma.from_documents(chunks, embeddings)

# 4. 检索
results = vectorstore.similarity_search("用户问题", k=5)
```

## 📈 RAG 评估指标

怎么知道你的 RAG 效果好不好？

| 指标 | 含义 | 怎么测 |
| ------ | ------ | -------- |
| **召回率** | 相关文档是否被检索到 | 人工标注 + 自动计算 |
| **准确率** | 检索到的文档是否相关 | 人工标注 + 自动计算 |
| **忠实度** | LLM 回答是否基于检索结果 | LLM-as-Judge |
| **相关性** | LLM 回答是否回答了问题 | LLM-as-Judge |

> [!TIP]
> **快速评估方法**
> 准备 10-20 个典型问题 + 期望答案，跑一遍 RAG，人工检查：
> 1. 检索到的文档是否包含答案？（召回率）
> 2. LLM 的回答是否正确？（忠实度 + 相关性）
>
> 如果召回率低 → 优化 Embedding 或切分策略
> 如果忠实度低 → 优化 Prompt 或换更强的 LLM

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
