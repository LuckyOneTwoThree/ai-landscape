# 知识图谱

> 最后更新：2026-06-08
> 数据来源：`data/data-and-knowledge.yaml` 自动生成

---

## 🕸️ 什么时候需要知识图谱？

知识图谱不是万能的。大多数 RAG 场景用向量检索就够了，**只有在这些情况下才需要图谱**：

| 场景 | 需要图谱吗 | 理由 |
|------|-----------|------|
| **"张三的老板是谁"** | ✅ 需要 | 多跳关系推理，向量检索搞不定 |
| **"公司所有项目的负责人"** | ✅ 需要 | 结构化查询，图数据库天然擅长 |
| **"这个产品的说明书"** | ❌ 不需要 | 纯文本检索，向量够用 |
| **"帮我写个周报"** | ❌ 不需要 | 生成任务，不需要图谱 |
| **"A 和 B 之间有什么关系"** | ✅ 需要 | 关系发现，图谱核心优势 |

> [!TIP]
> **90% 的 RAG 场景不需要知识图谱**
> 如果你的需求是"基于文档回答问题"，纯向量检索 + Reranking 就够了。知识图谱适合的是**实体关系密集**的场景（组织架构、供应链、法律条文关联等）。

---

## 📋 知识图谱生态总览

<!-- AUTOGEN_START -->

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [GraphRAG](https://github.com/microsoft/graphrag) | 微软出品的图增强 RAG 框架 | rag, microsoft | 微软出品<br>图增强 RAG<br>25K Stars |
| [Neo4j](https://neo4j.com/) | 最流行的图数据库，生态成熟 | rag, enterprise | 行业标杆的原生图数据库引擎<br>Cypher 查询语言完美协同大模型<br>无缝集成主流 RAG 框架 |
| [NebulaGraph](https://github.com/vesoft-inc/nebula) | 分布式图数据库，支持大规模图数据 | rag, distributed | 分布式图数据库<br>大规模图数据<br>11K Stars |
| [LightRAG](https://github.com/HKUDS/LightRAG) | LLM 驱动的轻量级知识图谱 RAG 框架 | rag, openai-compatible | 香港大学开源，双层极速图谱检索架构<br>成本不到微软方案的十分之一<br>原生支持图谱的无缝增量更新 |
| [FalkorDB](https://github.com/FalkorDB/FalkorDB) | 超快图数据库，GraphBLAS 底层，适合知识图谱 RAG | rag, fast-inference | 4.5K Stars<br>GraphBLAS 加速<br>超快图查询 |
| [HippoRAG](https://github.com/OSU-NLP-Group/HippoRAG) | 受海马体启发的 RAG 框架，NeurIPS 2024 论文，知识图谱+检索融合 | rag, academic | 3.5K Stars<br>NeurIPS 2024<br>海马体启发 |

<!-- AUTOGEN_END -->

---

## 🏗️ 图谱构建流程

```
原始文档
  ↓
实体抽取 (LLM / NER 模型)
  ↓
关系抽取 (LLM / 关系分类)
  ↓
实体消歧 (同义词合并)
  ↓
图数据库存储 (Neo4j / NebulaGraph)
  ↓
查询与推理 (Cypher / SPARQL)
```

**用 LLM 构建图谱**（最简方案）：
```python
import openai

def extract_entities(text: str) -> list[dict]:
    """用 LLM 抽取实体和关系"""
    response = openai.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[{
            "role": "user",
            "content": f"""从以下文本中抽取实体和关系，返回 JSON 格式：
            实体类型：人物、组织、产品、地点
            关系类型：任职于、创建了、位于、合作
            
            文本：{text}
            
            返回格式：
            {{"entities": [...], "relations": [...]}}"""
        }]
    )
    return response.choices[0].message.content
```

## 🔧 工具对比

| 工具 | 类型 | 适合谁 | 学习成本 |
|------|------|--------|---------|
| **Neo4j** | 图数据库 | 入门首选，生态最好 | 中 |
| **NebulaGraph** | 图数据库 | 大规模，国产 | 高 |
| **LightRAG** | LLM + 图谱 | 快速构建，LLM 驱动 | 低 |
| **GraphRAG** | 微软方案 | 企业级，与 Azure 集成 | 中 |
| **HippoRAG** | 海马体启发 | 学术研究，NeurIPS 论文 | 中 |
| **FalkorDB** | 图数据库 | 超快查询，GraphBLAS | 中 |

> [!TIP]
> **LightRAG 是个人/小团队的最佳起点**
> 它用 LLM 自动从文档中抽取实体和关系，构建图谱，然后用图谱增强 RAG 检索。不需要手动设计 Schema，开箱即用。

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
