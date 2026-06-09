# Monolithic LLM Frameworks

> Last Updated: 2026-06-08
> Data Source: Automatically generated from `data/frameworks.yaml`

---

## 🔧 Framework Selection: What Do You Really Need?

The core question in choosing a framework is not "Which is the best?", but **"What does your project need?"**.

| Your Situation | **Recommended Framework** | Reason |
| --------- | **---------** | ------ |
| **Rapid Prototype / MVP** | **LangChain** | Most complete ecosystem, most integrations, largest community |
| **RAG / Knowledge Base** | **LlamaIndex** | Specialized in data processing, PageIndex, Agentic RAG |
| **Enterprise / Microsoft Ecosystem** | **Semantic Kernel** | Azure integration, MAF merged, enterprise-grade |
| **Declarative Prompt Engineering** | **DSPy** | Automatic Prompt optimization, programmable LLMs |
| **Frontend AI Integration** | **Vercel AI SDK** | React/[Next.js](https://nextjs.org) native, streaming UI |
| **Type Safety / Structured Output** | **Pydantic AI / Instructor** | Deep Pydantic integration |
| **Java/JVM Ecosystem** | **LangChain4j** | Java version of [LangChain](https://langchain.com), 12.2K Stars |
| **Go Ecosystem** | **Eino** | From ByteDance, 11.7K Stars |
| **Ruby Ecosystem** | **RubyLLM** | All-in-one Ruby AI framework |

> [!TIP]
> **90% of projects only need LangChain or LlamaIndex**
> If you are unsure what to choose, start with LangChain. It has the most complete ecosystem and comprehensive documentation, making it easiest to find solutions when you encounter problems. Once you are familiar with LLM development, choose a more specialized framework based on your specific needs.

---

## 📋 LLM Development Frameworks Overview

<!-- AUTOGEN_START -->

#### 🔥 Hot Projects (50K+ Stars)

| Name | Introduction | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [LangChain](https://langchain.com) | The most popular LLM application development framework, most complete ecosystem, v0.4 introduced GraphRAG | pipeline, rag, mcp, [langchain](https://langchain.com) | Largest community ecosystem (110K+ Stars)<br>Rich integration components<br>v0.4 introduced GraphRAG and Hub integration<br>Deep integration with LangSmith for observability |
| [LlamaIndex](https://llamaindex.ai) | Data middleware framework connecting LLMs and private data, specializing in RAG and knowledge retrieval | rag, embedding-model | Specialized in RAG, [LlamaParse](https://cloud.llamaindex.ai/parse) for document parsing<br>Seamless integration with LlamaCloud indexing<br>PageIndex requires no chunking (98.7% accuracy)<br>Agentic RAG multimodal support |

#### ⭐ Active Projects (10K-50K Stars)

| Name | Introduction | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [DSPy](https://dspy.ai) | Declarative programming prompt engineering framework from Stanford, solving the fragility of traditional Prompts | automation, graph | Declarative Prompt programming<br>Automatic optimization and compilation<br>Low cost for model migration<br>22K+ Stars |
| [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/) | Enterprise-grade Agent development framework from Microsoft, merged with AutoGen into Microsoft Agent Framework | enterprise, agent, microsoft, pipeline | Merged with AutoGen into MAF<br>MCP + Aspire multi-agent orchestration<br>Enterprise-grade production-ready<br>Strengthens native C# AI Agent capabilities |
| [Haystack](https://haystack.deepset.ai) | Enterprise-grade NLP/RAG framework from deepset, focusing on pipeline mode and production stability | rag, pipeline, enterprise, [langchain](https://langchain.com) | Clear Pipeline mode<br>Enterprise-grade stability<br>Complete pipeline from document processing to generation<br>19K+ Stars |
| [Vercel AI SDK](https://sdk.vercel.ai) | Frontend AI integration SDK, React/[Next.js](https://nextjs.org) native, streaming UI | content-creation, streaming, coding-assistant | React/[Next.js](https://nextjs.org) native<br>Streaming UI rendering<br>Multi-model support<br>Top choice for frontend AI integration |
| [Instructor](https://python.useinstructor.com) | Framework specializing in LLM → structured data, deep Pydantic integration | structured, compliance, coding-assistant | Specialized in structured output<br>Deep Pydantic integration<br>Multi-model support |
| [LangChain4j](https://github.com/langchain4j/langchain4j) | Java version of [LangChain](https://langchain.com), LLM application framework designed for the Java/JVM ecosystem | coding-assistant, [langchain](https://langchain.com) | 12.2K Stars<br>Java/JVM ecosystem<br>Official [LangChain](https://langchain.com) Java version |
| [Eino](https://github.com/cloudwego/eino) | Go language LLM application development framework from ByteDance | coding-assistant, [langchain](https://langchain.com) | 11.7K Stars<br>From ByteDance<br>Go ecosystem |

#### 🆕 Emerging Projects (<10K Stars)

| Name | Introduction | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [Spring AI Alibaba](https://github.com/alibaba/spring-ai-alibaba) | Java Agentic AI framework from Alibaba, Spring ecosystem integration | coding-assistant, china-based, agent | 9.9K Stars<br>From Alibaba<br>Spring ecosystem integration |
| [BAML](https://github.com/BoundaryML/baml) | AI framework bringing engineering to Prompt Engineering, structured output | structured, automation, coding-assistant | 8.3K Stars<br>Structured output<br>Engineered Prompt |
| [Pydantic AI](https://ai.pydantic.dev) | Type-safe GenAI development framework based on Pydantic, bringing the [FastAPI](https://fastapi.tiangolo.com) experience to AI | coding-assistant, structured, compliance | Type-safe (runtime errors become compile-time errors)<br>Multi-model support (OpenAI/Anthropic/Gemini)<br>[FastAPI](https://fastapi.tiangolo.com)-style development experience<br>Dependency injection system |
| [AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG) | Automated RAG optimization framework, automatically finds the best RAG pipeline | rag, automation, pipeline | 4.8K Stars<br>Automated RAG optimization<br>Automatically finds the best pipeline |
| [Koog](https://github.com/JetBrains/koog) | JVM (Java/Kotlin) AI Agent framework from JetBrains | coding-assistant | 4.3K Stars<br>From JetBrains<br>Java/Kotlin support |
| [AdalFlow](https://github.com/SylphAI-Inc/AdalFlow) | LLM application building and automatic optimization framework, from SylphAI | automation, [langchain](https://langchain.com) | 4.2K Stars<br>Automatic optimization<br>From SylphAI |
| [RubyLLM](https://github.com/crmne/ruby_llm) | All-in-one AI framework for Ruby, supporting all mainstream Providers | coding-assistant, [langchain](https://langchain.com), agentic | 4K Stars<br>Ruby ecosystem<br>Multi-Provider support |

<!-- AUTOGEN_END -->

---

## 🏛️ Three Major Camps

### 🔵 Full-Stack Frameworks: Can Do Anything

| Framework | Language | Stars | Core Advantage | Best For |
| ------ | ------ | ------- | --------- | -------- |
| [**LangChain**](https://langchain.com) | Python/TS | 138K | Most complete ecosystem, most integrations | Rapid prototyping, full-stack development |
| [**LlamaIndex**](https://llamaindex.ai) | Python | 50K | RAG specialized, PageIndex | Knowledge bases, data-intensive |
| [**Haystack**](https://haystack.deepset.ai) | Python | 25K | Modular Pipelines | Search, RAG, production-ready |
| [**Semantic Kernel**](https://learn.microsoft.com/en-us/semantic-kernel/) | C#/Python/Java | 18K | Microsoft ecosystem, Azure integration | Enterprise-grade, .NET ecosystem |

### 🟢 Specialized Frameworks: Pushing One Direction to the Extreme

| Framework | Direction | Stars | Core Advantage | Best For |
| ------ | ------ | ------- | --------- | -------- |
| [**DSPy**](https://dspy.ai) | Declarative Prompts | 22K | Automatic Prompt optimization | Prompt Engineers |
| [**Pydantic AI**](https://ai.pydantic.dev) | Type Safety | 18K | Deep Pydantic integration | Python Developers |
| [**Instructor**](https://python.useinstructor.com) | Structured Output | 13K | LLM → Structured data | Data processing |
| [**BAML**](https://github.com/BoundaryML/baml) | Engineered Prompts | 8.3K | Structured output | Enterprise applications |
| [**Vercel AI SDK**](https://sdk.vercel.ai) | Frontend Integration | 15K | React/[Next.js](https://nextjs.org) native | Frontend developers |

### 🟡 Language-Specific: Non-Python Ecosystems

| Framework | Language | Stars | Core Advantage | Best For |
| ------ | ------ | ------- | --------- | -------- |
| [**LangChain4j**](https://github.com/langchain4j/langchain4j) | Java | 12.2K | Java version of [LangChain](https://langchain.com) | Java/JVM developers |
| [**Eino**](https://github.com/cloudwego/eino) | Go | 11.7K | From ByteDance | Go developers |
| [**RubyLLM**](https://github.com/crmne/ruby_llm) | Ruby | 4K | All-in-one Ruby AI framework | Ruby developers |
| [**Mastra**](https://mastra.ai) | TypeScript | 25K | Full-stack Agent framework | TypeScript developers |

## 💡 Framework Comparison

| Dimension | [LangChain](https://langchain.com) | [LlamaIndex](https://llamaindex.ai) | [DSPy](https://dspy.ai) | [Pydantic AI](https://ai.pydantic.dev) |
| ------ | ----------- | ------------ | ------ | ------------- |
| **Learning Curve** | Medium | Medium | High | Low |
| **Ecosystem Completeness** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **RAG Support** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ |
| **Type Safety** | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Production Ready** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Community Activity** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

## 🚀 Quick Start

**Minimal LangChain Example**:
```python
# pip install langchain langchain-openai
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-5.4-mini")
prompt = ChatPromptTemplate.from_template("Explain in one sentence: {topic}")
chain = prompt | llm

result = chain.invoke({"topic": "Quantum Computing"})
print(result.content)
```

**Minimal LlamaIndex RAG**:
```python
# pip install llama-index
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("./data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

response = query_engine.query("What is this document about?")
print(response)
```

---

> **Update Frequency**: Quarterly updates
> **Automation**: Run `python scripts/build_docs.py` to re-render tables from YAML.
