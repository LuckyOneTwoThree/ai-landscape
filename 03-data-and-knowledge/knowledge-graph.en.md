# Knowledge Graph

> Last Updated: 2026-06-08
> Data Source: Automatically generated from `data/data-and-knowledge.yaml`

---

## 🕸️ When Do You Need a Knowledge Graph?

A knowledge graph is not a silver bullet. For most RAG scenarios, vector retrieval is sufficient. **You only need a graph in these situations**:

| Scenario | **Need a Graph?** | Reason |
| ------ | **-----------** | ------ |
| **"Who is Zhang San's boss?"** | **✅ Yes** | Multi-hop relationship reasoning, vector retrieval cannot handle this |
| **"The leaders of all company projects"** | **✅ Yes** | Structured querying, naturally suited for graph databases |
| **"The user manual for this product"** | **❌ No** | Pure text retrieval, vectors are sufficient |
| **"Help me write a weekly report"** | **❌ No** | Generative task, no graph needed |
| **"What is the relationship between A and B?"** | **✅ Yes** | Relationship discovery, core advantage of graphs |

> [!TIP]
> **90% of RAG scenarios do not require a knowledge graph**
> If your requirement is to "answer questions based on documents", pure vector retrieval + Reranking is enough. Knowledge graphs are suitable for scenarios **dense with entity relationships** (organizational structures, supply chains, legal provision correlations, etc.).

---

## 📋 Knowledge Graph Ecosystem Overview

<!-- AUTOGEN_START -->

| Name | Introduction | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [GraphRAG](https://github.com/microsoft/graphrag) | Graph-enhanced RAG framework from Microsoft | rag, microsoft | From Microsoft<br>Graph-enhanced RAG<br>25K Stars |
| [Neo4j](https://neo4j.com/) | The most popular graph database with a mature ecosystem | rag, enterprise | Industry-standard native graph database engine<br>Cypher query language perfectly synergizes with LLMs<br>Seamlessly integrates with mainstream RAG frameworks |
| [NebulaGraph](https://github.com/vesoft-inc/nebula) | Distributed graph database, supporting large-scale graph data | rag, distributed | Distributed graph database<br>Large-scale graph data<br>11K Stars |
| [LightRAG](https://github.com/HKUDS/LightRAG) | LLM-driven lightweight knowledge graph RAG framework | rag, openai-compatible | Open-sourced by HKU, dual-level ultra-fast graph retrieval architecture<br>Costs less than one-tenth of Microsoft's solution<br>Natively supports seamless incremental graph updates |
| [FalkorDB](https://github.com/FalkorDB/FalkorDB) | Ultra-fast graph database powered by GraphBLAS, suitable for knowledge graph RAG | rag, fast-inference | 4.5K Stars<br>GraphBLAS acceleration<br>Ultra-fast graph queries |
| [HippoRAG](https://github.com/OSU-NLP-Group/HippoRAG) | Hippocampus-inspired RAG framework, NeurIPS 2024 paper, integrating knowledge graph + retrieval | rag, academic | 3.5K Stars<br>NeurIPS 2024<br>Hippocampus-inspired |

<!-- AUTOGEN_END -->

---

## 🏗️ Graph Construction Pipeline

```
Raw Documents
  ↓
Entity Extraction (LLM / NER Model)
  ↓
Relationship Extraction (LLM / Relation Classification)
  ↓
Entity Disambiguation (Synonym Merging)
  ↓
Graph Database Storage (Neo4j / NebulaGraph)
  ↓
Query and Reasoning (Cypher / SPARQL)
```

**Building a graph with LLM** (Simplest approach):
```python
import openai

def extract_entities(text: str) -> list[dict]:
    """Extract entities and relationships using LLM"""
    response = openai.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[{
            "role": "user",
            "content": f"""Extract entities and relationships from the following text and return in JSON format:
            Entity types: Person, Organization, Product, Location
            Relationship types: Works_at, Created, Located_in, Cooperates_with
            
            Text: {text}
            
            Return format:
            {{"entities": [...], "relations": [...]}}"""
        }]
    )
    return response.choices[0].message.content
```

## 🔧 Tool Comparison

| Tool | Type | Best For | Learning Curve |
| ------ | ------ | -------- | --------- |
| [**Neo4j**](https://neo4j.com/) | Graph Database | Top choice for beginners, best ecosystem | Medium |
| [**NebulaGraph**](https://github.com/vesoft-inc/nebula) | Graph Database | Large-scale, domestic | High |
| [**LightRAG**](https://github.com/HKUDS/LightRAG) | LLM + Graph | Fast building, LLM-driven | Low |
| [**GraphRAG**](https://github.com/microsoft/graphrag) | Microsoft Solution | Enterprise-grade, Azure integration | Medium |
| [**HippoRAG**](https://github.com/OSU-NLP-Group/HippoRAG) | Hippocampus-inspired | Academic research, NeurIPS paper | Medium |
| [**FalkorDB**](https://github.com/FalkorDB/FalkorDB) | Graph Database | Ultra-fast queries, GraphBLAS | Medium |

> [!TIP]
> **LightRAG is the best starting point for individuals/small teams**
> It automatically extracts entities and relationships from documents using LLMs to build a graph, and then uses the graph to enhance RAG retrieval. No manual Schema design is needed, ready out-of-the-box.

---

> **Update Frequency**: Quarterly updates
> **Automation**: Run `python scripts/build_docs.py` to re-render tables from YAML.
