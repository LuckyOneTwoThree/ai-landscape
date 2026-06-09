# Multi-Agent Frameworks

> Last Updated: 2026-06-08
> Data Source: Automatically generated from `data/frameworks.yaml`

---

## 🤖 Core Issues in Multi-Agent Systems

A Multi-Agent system is not just "putting multiple LLMs together," but rather **making multiple Agents collaborate to complete complex tasks**.

| Your Situation | Recommended Framework | Reason |
| --------- | --------- | ------ |
| **Rapid Prototype / Role-Playing** | [CrewAI](https://crewai.com) | Simplest, intuitive role definition |
| **Complex Workflows / State Machines** | [LangGraph](https://langchain-ai.github.io/langgraph/) | State graph orchestration, flexible and powerful |
| **OpenAI Ecosystem** | [OpenAI Agents SDK](https://platform.openai.com/docs/assistants/overview) | Official support, lightweight |
| **Microsoft Ecosystem** | [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | Enterprise-grade, Azure integration |
| **HuggingFace Ecosystem** | [Smolagents](https://github.com/huggingface/smolagents) | Lightweight, 12K Stars |
| **TypeScript Full-Stack** | [Mastra](https://mastra.ai) / [VoltAgent](https://github.com/VoltAgent/voltagent) | TS native, full-stack development |

> [!TIP]
> **Three Architecture Patterns for Multi-Agent Systems**
> 1. **Sequential Execution**: Agent A → Agent B → Agent C (Pipeline)
> 2. **Parallel Execution**: Agent A + Agent B + Agent C → Merge results (MapReduce)
> 3. **Dynamic Routing**: Dynamically select Agents based on the task (State Machine)
>
> For most projects, sequential execution is enough. Use dynamic routing only when you truly need parallel processing or complex decision-making.

---

## 📋 Multi-Agent Frameworks Overview

<!-- AUTOGEN_START -->

#### 🔥 Hot Projects (50K+ Stars)

| Name | Introduction | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [MetaGPT](https://github.com/FoundationAgents/MetaGPT) | Multi-Agent framework, AI software company, 68.6K Stars | agent, automation, open-source | 68.6K Stars<br>AI software company<br>Multi-Agent framework |
| [CrewAI](https://crewai.com) | Fastest-growing multi-agent role-playing framework, focusing on ease of use and production readiness | agent, content-creation, enterprise | Intuitive role definition<br>Flows workflow orchestration<br>30K+ Stars<br>Reliable design principles |

#### ⭐ Active Projects (10K-50K Stars)

| Name | Introduction | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [AutoGen (→ MAF)](https://microsoft.github.com/autogen/) | Microsoft's multi-agent conversational framework, merged with Semantic Kernel into [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | agent, chat, microsoft | Multi-agent dialogue orchestration<br>Merged into MAF<br>43K+ Stars (Original repository)<br>[AutoGen](https://microsoft.github.com/autogen/) concepts deeply integrated into the industry |
| [Agno](https://agno.com) | High-performance full-stack multi-agent framework (formerly Phidata), focusing on speed and scalability | agent, high-performance, all-in-one | Multi-Agent Framework + Runtime + Control Plane<br>Built-in memory/knowledge base/session management<br>Dynamic tool integration<br>35K+ Stars |
| [LangGraph](https://langchain-ai.github.io/langgraph/) | The next-generation core of LangChain, orchestrating complex multi-agents based on state graphs | graph, stateful, agent, pipeline | Directed graph state machine<br>Loops/conditional branches<br>Built-in persistent checkpoints<br>Human-in-the-loop nodes and time travel<br>29K+ Stars |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) | OpenAI's official multi-agent orchestration SDK, evolved from Swarm, aimed at production environments | agent, openai-compatible, enterprise | Evolved from Swarm<br>Agent Handoffs<br>Guardrails for safety<br>Debugging and tracing<br>25K+ Stars |
| [Mastra](https://mastra.ai) | TypeScript native Agent framework, suitable for full-stack development | agent, coding-assistant, workflow, all-in-one | TS native Agent framework<br>Agent network orchestration<br>Suitable for full-stack development |
| [Smolagents](https://github.com/huggingface/smolagents) | Lightweight Agent framework from HuggingFace | agent, open-source, easy-to-use | From HuggingFace<br>Lightweight Agents<br>12K Stars |
| [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | AI Agent building, orchestration, and deployment framework from Microsoft | microsoft, agent, pipeline | 11.1K Stars<br>From Microsoft<br>Orchestration + Deployment |

#### 🆕 Emerging Projects (<10K Stars)

| Name | Introduction | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [VoltAgent](https://github.com/VoltAgent/voltagent) | TypeScript AI Agent engineering platform, open-source | coding-assistant, agent, automation | 9.5K Stars<br>TypeScript<br>Agent engineering platform |
| [Agent Squad](https://github.com/2FastLabs/agent-squad) | Flexible multi-agent management framework, supporting various Agent types | agent, easy-to-use, coding-assistant | 7.6K Stars<br>Flexible management<br>Multiple Agent types |
| [Swarms](https://github.com/kyegomez/swarms) | Enterprise-grade, production-ready multi-agent orchestration framework | enterprise, agent | 6.8K Stars<br>Enterprise-grade<br>Production-ready |
| [OpenAgentsControl](https://github.com/darrenhinde/OpenAgentsControl) | Rust AI Agent framework, plan-first development workflow | coding-assistant, agent, automation | 4.3K Stars<br>Rust ecosystem<br>Plan-first workflow |

<!-- AUTOGEN_END -->

---

## 🏛️ Two Major Camps

### 🔵 Role-Playing: Define Roles, Automate Collaboration

| Framework | Stars | Core Advantage | Best For |
| ------ | ------- | --------- | -------- |
| [**CrewAI**](https://crewai.com) | 53K | Simplest, intuitive role definition | Rapid prototyping, role-playing |
| [**Agent Squad**](https://github.com/2FastLabs/agent-squad) | 7.6K | Flexible multi-agent management | Multi-type Agent collaboration |
| [**Swarms**](https://github.com/kyegomez/swarms) | 6.8K | Enterprise-grade production readiness | Enterprise applications |

### 🟢 State Graph: Define Processes, Precise Control

| Framework | Stars | Core Advantage | Best For |
| ------ | ------- | --------- | -------- |
| [**LangGraph**](https://langchain-ai.github.io/langgraph/) | 34K | State graph orchestration, flexible and powerful | Complex workflows |
| [**OpenAI Agents SDK**](https://platform.openai.com/docs/assistants/overview) | 27K | Official support, lightweight | OpenAI ecosystem |
| [**Microsoft Agent Framework**](https://github.com/microsoft/agent-framework) | 11.1K | From Microsoft, enterprise-grade | Microsoft ecosystem |
| [**Smolagents**](https://github.com/huggingface/smolagents) | 12K | From HuggingFace, lightweight | HuggingFace ecosystem |

### 🟡 TypeScript Full-Stack

| Framework | Stars | Core Advantage | Best For |
| ------ | ------- | --------- | -------- |
| [**Mastra**](https://mastra.ai) | 25K | From Gatsby team, full-stack Agents | TS full-stack developers |
| [**VoltAgent**](https://github.com/VoltAgent/voltagent) | 9.5K | Agent engineering platform | TS developers |

## 💡 Framework Comparison

| Dimension | [CrewAI](https://crewai.com) | [LangGraph](https://langchain-ai.github.io/langgraph/) | [OpenAI Agents SDK](https://platform.openai.com/docs/assistants/overview) | [Smolagents](https://github.com/huggingface/smolagents) |
| ------ | -------- | ----------- | ------------------- | ------------ |
| **Learning Curve** | Low | High | Low | Low |
| **Flexibility** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| **Production Ready** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Memory Management** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ |
| **Community Activity** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |

## 🚀 Quick Start

**Minimal CrewAI Example**:
```python
# pip install crewai
from crewai import Agent, Task, Crew

# Define Agents
researcher = Agent(role="Researcher", goal="Collect information", backstory="You are a research expert")
writer = Agent(role="Writer", goal="Write articles", backstory="You are a writing expert")

# Define Tasks
research_task = Task(description="Research AI development trends", agent=researcher)
write_task = Task(description="Write a research report", agent=writer)

# Run Crew
crew = Crew(agents=[researcher, writer], tasks=[research_task, write_task])
result = crew.kickoff()
print(result)
```

**Minimal LangGraph Example**:
```python
# pip install langgraph
from langgraph.graph import StateGraph, END

# Define State
class State(dict):
    messages: list

# Define Nodes
def researcher(state: State):
    # Research logic
    return {"messages": state.get("messages", []) + ["Research completed"]}

def writer(state: State):
    # Writing logic
    return {"messages": state.get("messages", []) + ["Writing completed"]}

# Build Graph
graph = StateGraph(State)
graph.add_node("researcher", researcher)
graph.add_node("writer", writer)
graph.add_edge("researcher", "writer")
graph.add_edge("writer", END)
graph.set_entry_point("researcher")

# Run
app = graph.compile()
result = app.invoke({"messages": []})
print(result)
```

## 🧠 Agent Memory Management

One of the core challenges in Multi-Agent systems is **memory management**:

| Framework | Memory Type | Description |
| ------ | --------- | ------ |
| [**CrewAI**](https://crewai.com) | Short-term Memory | Intra-session memory, not cross-session |
| [**LangGraph**](https://langchain-ai.github.io/langgraph/) | State Persistence | Persists state via Checkpoints |
| **Cognee** | Long-term Memory | Knowledge Graph + Vector Retrieval (See `02-infrastructure/vector-db.md`) |
| **OpenViking** | Context Database | Context management designed specifically for Agents (See `02-infrastructure/vector-db.md`) |

> [!TIP]
> **Best Practices for Memory Management**
> - **Short-term Tasks**: Use built-in framework memory (CrewAI/LangGraph)
> - **Long-term Tasks**: Use Cognee or OpenViking for persistent memory (See Infrastructure layer)
> - **Knowledge-intensive**: Use Knowledge Graphs (GraphRAG) for structured memory

---

> **Update Frequency**: Quarterly updates
> **Automation**: Run `python scripts/build_docs.py` to re-render tables from YAML.
