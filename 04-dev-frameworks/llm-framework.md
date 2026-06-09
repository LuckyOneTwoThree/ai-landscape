# 单体 LLM 开发框架

> 最后更新：2026-06-08
> 数据来源：`data/frameworks.yaml` 自动生成

---

## 🔧 框架选型：你到底需要什么？

选框架的核心问题不是"哪个最好"，而是**"你的项目需要什么"**。

| 你的情况 | 推荐框架 | 理由 |
|---------|---------|------|
| **快速原型 / MVP** | [LangChain](https://langchain.com) | 生态最完整，集成最多，社区最大 |
| **RAG / 知识库** | [LlamaIndex](https://llamaindex.ai) | 数据处理专精，PageIndex，Agentic RAG |
| **企业级 / 微软生态** | [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/) | Azure 集成，MAF 合并，企业级 |
| **声明式 Prompt 工程** | [DSPy](https://dspy.ai) | 自动优化 Prompt，程序化 LLM |
| **前端 AI 集成** | [[Vercel](https://vercel.com) AI SDK](https://sdk.[vercel](https://vercel.com).ai) | React/[Next.js](https://nextjs.org) 原生，流式 UI |
| **类型安全 / 结构化输出** | [Pydantic AI](https://ai.pydantic.dev) / [Instructor](https://python.useinstructor.com) | Pydantic 深度集成 |
| **Java/JVM 生态** | [LangChain4j](https://github.com/langchain4j/langchain4j) | Java 版 [LangChain](https://langchain.com)，12.2K Stars |
| **Go 语言生态** | [Eino](https://github.com/cloudwego/eino) | 字节跳动出品，11.7K Stars |
| **Ruby 生态** | [RubyLLM](https://github.com/crmne/ruby_llm) | 全能 Ruby AI 框架 |

> [!TIP]
> **90% 的项目用 LangChain 或 LlamaIndex 就够了**
> 如果你不确定选什么，先用 LangChain。它的生态最完整，文档最全，遇到问题最容易找到解决方案。等你熟悉了 LLM 开发，再根据具体需求选择更专业的框架。

---

## 📋 LLM 开发框架总览

<!-- AUTOGEN_START -->

#### 🔥 热门项目 (50K+ Stars)

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [LangChain](https://langchain.com) | 最流行的 LLM 应用开发框架，生态最完整，v0.4 引入 GraphRAG | pipeline, rag, mcp, langchain | 最大的社区生态 (110K+ Stars)<br>丰富的集成组件<br>v0.4 引入 GraphRAG 与 Hub 集成<br>LangSmith 深度整合可观测性 |
| [LlamaIndex](https://llamaindex.ai) | 连接 LLM 与私有数据的数据中间层框架，专注 RAG 与知识检索 | rag, embedding-model | RAG 专精，LlamaParse 文档解析<br>LlamaCloud 索引无缝衔接<br>PageIndex 无需分块 (98.7% 准确率)<br>Agentic RAG 多模态支持 |

#### ⭐ 活跃项目 (10K-50K Stars)

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [DSPy](https://dspy.ai) | 斯坦福推出的声明式编程提示工程框架，解决传统 Prompt 脆弱性问题 | automation, graph | 声明式 Prompt 编程<br>自动优化与编译<br>模型迁移低成本<br>22K+ Stars |
| [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/) | 微软企业级 Agent 开发框架，已与 AutoGen 合并为 Microsoft Agent Framework | enterprise, agent, microsoft, pipeline | 与 AutoGen 合并为 MAF<br>MCP + Aspire 多 Agent 编排<br>企业级生产就绪<br>强化 C# 原生 AI Agent 能力 |
| [Haystack](https://haystack.deepset.ai) | deepset 开发的企业级 NLP/RAG 框架，主打管道模式与生产稳定性 | rag, pipeline, enterprise, langchain | Pipeline 管道模式清晰<br>企业级稳定<br>从文档处理到生成的完整管道<br>19K+ Stars |
| [Vercel AI SDK](https://sdk.vercel.ai) | 前端 AI 集成 SDK，React/Next.js 原生，流式 UI | content-creation, streaming, coding-assistant | React/Next.js 原生<br>流式 UI 渲染<br>多模型支持<br>前端 AI 集成首选 |
| [Instructor](https://python.useinstructor.com) | 专注 LLM → 结构化数据的框架，Pydantic 深度集成 | structured, compliance, coding-assistant | 专注结构化输出<br>Pydantic 深度集成<br>多模型支持 |
| [LangChain4j](https://github.com/langchain4j/langchain4j) | Java 版 LangChain，为 Java/JVM 生态设计的 LLM 应用框架 | coding-assistant, langchain | 12.2K Stars<br>Java/JVM 生态<br>LangChain 官方 Java 版 |
| [Eino](https://github.com/cloudwego/eino) | 字节跳动出品的 Go 语言 LLM 应用开发框架 | coding-assistant, langchain | 11.7K Stars<br>字节跳动出品<br>Go 语言生态 |

#### 🆕 新兴项目 (<10K Stars)

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [Spring AI Alibaba](https://github.com/alibaba/spring-ai-alibaba) | 阿里巴巴出品的 Java Agentic AI 框架，Spring 生态集成 | coding-assistant, china-based, agent | 9.9K Stars<br>阿里巴巴出品<br>Spring 生态集成 |
| [BAML](https://github.com/BoundaryML/baml) | AI 框架，将工程化引入 Prompt Engineering，结构化输出 | structured, automation, coding-assistant | 8.3K Stars<br>结构化输出<br>工程化 Prompt |
| [Pydantic AI](https://ai.pydantic.dev) | 基于 Pydantic 的类型安全 GenAI 开发框架，FastAPI 体验搬入 AI | coding-assistant, structured, compliance | 类型安全 (运行时错误变编写时错误)<br>多模型支持 (OpenAI/Anthropic/Gemini)<br>FastAPI 式开发体验<br>依赖注入系统 |
| [AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG) | RAG 自动优化框架，自动找到最佳 RAG 管道 | rag, automation, pipeline | 4.8K Stars<br>RAG 自动优化<br>自动找最佳管道 |
| [Koog](https://github.com/JetBrains/koog) | JetBrains 出品的 JVM (Java/Kotlin) AI Agent 框架 | coding-assistant | 4.3K Stars<br>JetBrains 出品<br>Java/Kotlin 支持 |
| [AdalFlow](https://github.com/SylphAI-Inc/AdalFlow) | LLM 应用构建与自动优化框架，SylphAI 出品 | automation, langchain | 4.2K Stars<br>自动优化<br>SylphAI 出品 |
| [RubyLLM](https://github.com/crmne/ruby_llm) | Ruby 语言的全能 AI 框架，支持所有主流 Provider | coding-assistant, langchain, agentic | 4K Stars<br>Ruby 生态<br>多 Provider 支持 |

<!-- AUTOGEN_END -->

---

## 🏛️ 三大阵营

### 🔵 全栈框架：什么都能做

| 框架 | 语言 | Stars | 核心优势 | 适合谁 |
|------|------|-------|---------|--------|
| **LangChain** | Python/TS | 138K | 生态最完整，集成最多 | 快速原型，全栈开发 |
| **LlamaIndex** | Python | 50K | RAG 专精，PageIndex | 知识库，数据密集 |
| **Haystack** | Python | 25K | 模块化 Pipeline | 搜索，RAG，生产就绪 |
| **Semantic Kernel** | C#/Python/Java | 18K | 微软生态，Azure 集成 | 企业级，.NET 生态 |

### 🟢 专精框架：一个方向做到极致

| 框架 | 方向 | Stars | 核心优势 | 适合谁 |
|------|------|-------|---------|--------|
| **DSPy** | 声明式 Prompt | 22K | 自动优化 Prompt | Prompt 工程师 |
| **Pydantic AI** | 类型安全 | 18K | Pydantic 深度集成 | Python 开发者 |
| **Instructor** | 结构化输出 | 13K | LLM → 结构化数据 | 数据处理 |
| **BAML** | 工程化 Prompt | 8.3K | 结构化输出 | 企业级应用 |
| **Vercel AI SDK** | 前端集成 | 15K | React/Next.js 原生 | 前端开发者 |

### 🟡 语言特定：非 Python 生态

| 框架 | 语言 | Stars | 核心优势 | 适合谁 |
|------|------|-------|---------|--------|
| **LangChain4j** | Java | 12.2K | Java 版 LangChain | Java/JVM 开发者 |
| **Eino** | Go | 11.7K | 字节跳动出品 | Go 开发者 |
| **RubyLLM** | Ruby | 4K | 全能 Ruby AI 框架 | Ruby 开发者 |
| **Mastra** | TypeScript | 25K | 全栈 Agent 框架 | TypeScript 开发者 |

## 💡 框架对比

| 维度 | LangChain | LlamaIndex | DSPy | Pydantic AI |
|------|-----------|------------|------|-------------|
| **学习曲线** | 中 | 中 | 高 | 低 |
| **生态完整度** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **RAG 支持** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐ |
| **类型安全** | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **生产就绪** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **社区活跃度** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |

## 🚀 快速上手

**LangChain 最简示例**：
```python
# pip install langchain langchain-openai
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-5.4-mini")
prompt = ChatPromptTemplate.from_template("用一句话解释：{topic}")
chain = prompt | llm

result = chain.invoke({"topic": "量子计算"})
print(result.content)
```

**LlamaIndex 最简 RAG**：
```python
# pip install llama-index
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("./data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

response = query_engine.query("这个文档讲了什么？")
print(response)
```

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
