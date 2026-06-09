# 多 Agent 框架

> 最后更新：2026-06-08
> 数据来源：`data/frameworks.yaml` 自动生成

---

## 🤖 多 Agent 的核心问题

多 Agent 系统不是"把多个 LLM 放在一起"，而是**让多个 Agent 协作完成复杂任务**。

| 你的情况 | 推荐框架 | 理由 |
|---------|---------|------|
| **快速原型 / 角色扮演** | [CrewAI](https://crewai.com) | 最简单，角色定义直观 |
| **复杂工作流 / 状态机** | [LangGraph](https://langchain-ai.github.io/langgraph/) | 状态图编排，灵活强大 |
| **OpenAI 生态** | [OpenAI Agents SDK](https://platform.openai.com/docs/assistants/overview) | 官方支持，轻量级 |
| **微软生态** | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | 企业级，Azure 集成 |
| **HuggingFace 生态** | [Smolagents](https://github.com/huggingface/smolagents) | 轻量级，12K Stars |
| **TypeScript 全栈** | [Mastra](https://mastra.ai) / [VoltAgent](https://github.com/VoltAgent/voltagent) | TS 原生，全栈开发 |

> [!TIP]
> **多 Agent 的三种架构模式**
> 1. **顺序执行**：Agent A → Agent B → Agent C（流水线）
> 2. **并行执行**：Agent A + Agent B + Agent C → 合并结果（MapReduce）
> 3. **动态路由**：根据任务动态选择 Agent（状态机）
>
> 大多数项目用顺序执行就够了。只有真正需要并行处理或复杂决策时才用动态路由。

---

## 📋 多 Agent 框架总览

<!-- AUTOGEN_START -->

#### 🔥 热门项目 (50K+ Stars)

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | 多 Agent 框架，AI 软件公司，68.6K Stars | agent, automation, open-source | 68.6K Stars<br>AI 软件公司<br>多 Agent 框架 |
| [CrewAI](https://crewai.com) | 增长最快的多 Agent 角色扮演框架，主打简单易用与生产就绪 | agent, content-creation, enterprise | 角色定义直观<br>Flows 工作流编排<br>30K+ Stars<br>可依赖设计原则 |

#### ⭐ 活跃项目 (10K-50K Stars)

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [AutoGen (→ MAF)](https://microsoft.github.io/autogen/) | 微软多智能体对话框架，已与 Semantic Kernel 合并为 Microsoft Agent Framework | agent, chat, microsoft | 多智能体对话编排<br>已合并入 MAF<br>43K+ Stars (原仓库)<br>AutoGen 概念深度融入行业 |
| [Agno](https://agno.com) | 高性能全栈多智能体框架 (前 Phidata)，专注速度与可扩展 | agent, high-performance, all-in-one | Multi-Agent Framework + Runtime + Control Plane<br>内置记忆/知识库/会话管理<br>动态工具集成<br>35K+ Stars |
| [LangGraph](https://langchain-ai.github.io/langgraph/) | LangChain 下一代核心，基于状态图实现复杂多 Agent 编排 | graph, stateful, agent, pipeline | 有向图状态机<br>循环/条件分支<br>内置持久化检查点<br>人机协作节点与时空回溯<br>29K+ Stars |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | OpenAI 官方多 Agent 编排 SDK，由 Swarm 演进而来，面向生产环境 | agent, openai-compatible, enterprise | 基于 Swarm 演进<br>Agent 交接 (Handoffs)<br>Guardrails 安全护栏<br>调试追踪<br>25K+ Stars |
| [Mastra](https://mastra.ai) | TypeScript 原生 Agent 框架，适合全栈开发 | agent, coding-assistant, workflow, all-in-one | TS 原生 Agent 框架<br>Agent 网络编排<br>适合全栈开发 |
| [Smolagents](https://github.com/huggingface/smolagents) | HuggingFace 出品的轻量级 Agent 框架 | agent, open-source, easy-to-use | HuggingFace 出品<br>轻量级 Agent<br>12K Stars |
| [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | 微软出品的 AI Agent 构建、编排与部署框架 | microsoft, agent, pipeline | 11.1K Stars<br>微软出品<br>编排+部署 |

#### 🆕 新兴项目 (<10K Stars)

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [VoltAgent](https://github.com/VoltAgent/voltagent) | TypeScript AI Agent 工程平台，开源 | coding-assistant, agent, automation | 9.5K Stars<br>TypeScript<br>Agent 工程平台 |
| [Agent Squad](https://github.com/2FastLabs/agent-squad) | 灵活的多 Agent 管理框架，支持多种 Agent 类型 | agent, easy-to-use, coding-assistant | 7.6K Stars<br>灵活管理<br>多 Agent 类型 |
| [Swarms](https://github.com/kyegomez/swarms) | 企业级生产就绪的多 Agent 编排框架 | enterprise, agent | 6.8K Stars<br>企业级<br>生产就绪 |
| [OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl) | Rust AI Agent 框架，计划优先的开发工作流 | coding-assistant, agent, automation | 4.3K Stars<br>Rust 生态<br>计划优先工作流 |

<!-- AUTOGEN_END -->

---

## 🏛️ 两大阵营

### 🔵 角色扮演型：定义角色，自动协作

| 框架 | Stars | 核心优势 | 适合谁 |
|------|-------|---------|--------|
| **CrewAI** | 53K | 最简单，角色定义直观 | 快速原型，角色扮演 |
| **Agent Squad** | 7.6K | 灵活的多 Agent 管理 | 多类型 Agent 协作 |
| **Swarms** | 6.8K | 企业级生产就绪 | 企业级应用 |

### 🟢 状态图型：定义流程，精确控制

| 框架 | Stars | 核心优势 | 适合谁 |
|------|-------|---------|--------|
| **LangGraph** | 34K | 状态图编排，灵活强大 | 复杂工作流 |
| **OpenAI Agents SDK** | 27K | 官方支持，轻量级 | OpenAI 生态 |
| **Microsoft Agent Framework** | 11.1K | 微软出品，企业级 | 微软生态 |
| **Smolagents** | 12K | HuggingFace 出品，轻量级 | HuggingFace 生态 |

### 🟡 TypeScript 全栈型

| 框架 | Stars | 核心优势 | 适合谁 |
|------|-------|---------|--------|
| **Mastra** | 25K | Gatsby 团队出品，全栈 Agent | TS 全栈开发者 |
| **VoltAgent** | 9.5K | Agent 工程平台 | TS 开发者 |

## 💡 框架对比

| 维度 | CrewAI | LangGraph | OpenAI Agents SDK | Smolagents |
|------|--------|-----------|-------------------|------------|
| **学习曲线** | 低 | 高 | 低 | 低 |
| **灵活性** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **生产就绪** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **记忆管理** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ |
| **社区活跃度** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |

## 🚀 快速上手

**CrewAI 最简示例**：
```python
# pip install crewai
from crewai import Agent, Task, Crew

# 定义 Agent
researcher = Agent(role="研究员", goal="收集信息", backstory="你是研究专家")
writer = Agent(role="作家", goal="撰写文章", backstory="你是写作专家")

# 定义 Task
research_task = Task(description="研究 AI 发展趋势", agent=researcher)
write_task = Task(description="撰写研究报告", agent=writer)

# 运行 Crew
crew = Crew(agents=[researcher, writer], tasks=[research_task, write_task])
result = crew.kickoff()
print(result)
```

**LangGraph 最简示例**：
```python
# pip install langgraph
from langgraph.graph import StateGraph, END

# 定义状态
class State(Topic):
    messages: list

# 定义节点
def researcher(state: State):
    # 研究逻辑
    return {"messages": state["messages"] + ["研究完成"]}

def writer(state: State):
    # 写作逻辑
    return {"messages": state["messages"] + ["写作完成"]}

# 构建图
graph = StateGraph(State)
graph.add_node("researcher", researcher)
graph.add_node("writer", writer)
graph.add_edge("researcher", "writer")
graph.add_edge("writer", END)

# 运行
app = graph.compile()
result = app.invoke({"messages": []})
print(result)
```

## 🧠 Agent 记忆管理

多 Agent 系统的核心挑战之一是**记忆管理**：

| 框架 | 记忆类型 | 说明 |
|------|---------|------|
| **CrewAI** | 短期记忆 | 对话内记忆，不跨会话 |
| **LangGraph** | 状态持久化 | 通过 Checkpoint 持久化状态 |
| **Cognee** | 长期记忆 | 知识图谱 + 向量检索（见 `02-infrastructure/vector-db.md`） |
| **OpenViking** | 上下文数据库 | 专为 Agent 设计的上下文管理（见 `02-infrastructure/vector-db.md`） |

> [!TIP]
> **记忆管理的最佳实践**
> - **短期任务**：用框架内置的记忆（CrewAI/LangGraph）
> - **长期任务**：用 Cognee 或 OpenViking 做持久化记忆（见基础设施层）
> - **知识密集**：用知识图谱（GraphRAG）做结构化记忆

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
