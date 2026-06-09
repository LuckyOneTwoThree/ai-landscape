# AI Technology Stack Ecosystem Map

> Last Updated: 2026-06-08

---

## Architecture Layer Diagram

```mermaid
graph TD
    subgraph 00["🎯 00 Selection Guides and Trends"]
        T1[Scenario-based Recommendations]
        T2[Monthly Trends]
        T3[Ecosystem Map]
    end

    subgraph 01["🧠 01 Foundation Model Layer"]
        M1[Language Models<br>GPT-5.5 / Claude Opus 4.8 / Gemini 3.5]
        M2[Multimodal Models<br>Image / Video / Audio]
        M3[Embedding Models<br>BGE-M3 / Cohere]
    end

    subgraph 02["🏗️ 02 Infrastructure Layer"]
        I1[Inference Engines<br>vLLM / Ollama]
        I2[API Gateways<br>LiteLLM / OpenRouter]
        I3[Vector Databases<br>Milvus / Qdrant]
    end

    subgraph 03["📊 03 Data and Knowledge Layer"]
        D1[Data Parsing]
        D2[Knowledge Graphs]
        D3[RAG Engines]
    end

    subgraph 04["⚙️ 04 Development Framework Layer"]
        F1[LLM Frameworks<br>LangChain / LlamaIndex]
        F2[Multi-Agent<br>LangGraph / CrewAI]
    end

    subgraph 05["🧩 05 Low-Code Platforms"]
        L1[AI Builders<br>Dify / Coze]
        L2[Workflows<br>n8n / Make]
    end

    subgraph 06["🔌 06 Tools and Protocols"]
        P1[MCP Ecosystem]
        P2[Function Calling]
        P3[Browser Control]
    end

    subgraph 07["🧱 07 Skills and Plugins"]
        S1[Open Source Skill Libraries]
        S2[Platform Plugins]
    end

    subgraph 08["📈 08 Observability"]
        O1[Tracing and Debugging]
        O2[Cost Monitoring]
        O3[Evaluation Benchmarks]
    end

    subgraph 09["🛡️ 09 Security and Compliance"]
        G1[Guardrails]
        G2[Auditing]
    end

    subgraph 10["🖥️ 10 Terminal Applications"]
        A1[Programming IDEs<br>Cursor / Claude Code]
        A2[Search and Research<br>Perplexity / Kimi]
        A3[Office and Creation<br>Notion AI / Suno]
    end

    01 --> 02
    02 --> 03
    03 --> 04
    03 --> 05
    04 --> 06
    05 --> 07
    06 --> 07
    07 --> 10
    01 --> 08
    01 --> 09
    04 --> 08
    08 --> 10

    style 00 fill:#1a1a2e,stroke:#e94560,color:#fff
    style 01 fill:#16213e,stroke:#0f3460,color:#fff
    style 02 fill:#1a1a2e,stroke:#0f3460,color:#fff
    style 03 fill:#16213e,stroke:#0f3460,color:#fff
    style 04 fill:#1a1a2e,stroke:#0f3460,color:#fff
    style 05 fill:#16213e,stroke:#0f3460,color:#fff
    style 06 fill:#1a1a2e,stroke:#0f3460,color:#fff
    style 07 fill:#16213e,stroke:#0f3460,color:#fff
    style 08 fill:#1a1a2e,stroke:#0f3460,color:#fff
    style 09 fill:#16213e,stroke:#0f3460,color:#fff
    style 10 fill:#16213e,stroke:#e94560,color:#fff
```

---

## Technology Stack Flow

```mermaid
flowchart LR
    User[Users/Developers] --> Choose{Selection Guides}
    Choose --> Model[Model Layer]
    Model --> Infra[Infrastructure]
    Infra --> Data[Data & Knowledge]
    Data --> Dev[Development Frameworks]
    Data --> Low[Low-Code Platforms]
    Dev --> Tools[Tools & Protocols]
    Low --> Plugins[Skills & Plugins]
    Tools --> Plugins
    Plugins --> Apps[Terminal Applications]
    Model --> Obs[Observability]
    Dev --> Obs
    Obs --> Apps
    Model --> Safety[Security & Compliance]

    style User fill:#e94560,color:#fff
    style Apps fill:#e94560,color:#fff
```

---

## Core Data Flow

```mermaid
flowchart TB
    Data[YAML Data Sources<br>data/*.yaml] --> Script[build_docs.py<br>Auto Rendering]
    Script --> MD[Markdown Files<br>Various Level .md]
    MD --> GitHub[GitHub Repository]
    MD --> Site[VitePress Site]
    Issue[Issue Form<br>Community Submission] --> Action[GitHub Action]
    Action --> PR[Auto PR]
    PR --> Data
```

---

## June 2026 AI Landscape Overview

### Model Layer

| Tier | Model | Vendor | Positioning |
| ------ | ------- | -------- | ------------- |
| **T0 Flagship** | [GPT-5.5](https://openai.com) Pro | OpenAI | Strongest Intelligence, Agent/Coding/Knowledge Work |
| **T0 Flagship** | [Claude Opus 4](https://anthropic.com).8 | Anthropic | Strongest Agent Reliability, Coding Consistency |
| **T0 Flagship** | [Gemini 3.5 Flash](https://gemini.google.com) | Google | Agent Workflows, Multi-Agent Coordination |
| **T1 High Cost-Performance** | [DeepSeek-V4-Pro](https://deepseek.com) | DeepSeek | Open-Source MoE, 1M Context |
| **T1 High Cost-Performance** | [Qwen3-Coder](https://qwen.ai)-480B | Alibaba | Agent-level Programming, Open-Source |
| **T1 High Cost-Performance** | [GLM-5.1](https://open.bigmodel.cn) | Zhipu AI | Omnimodal Matrix, Chinese Optimization |
| **T2 Lightweight** | [GPT-5.5-mini](https://openai.com) | OpenAI | High Cost-Performance, Rapid Response |
| **T2 Lightweight** | [Claude Haiku 4](https://anthropic.com) | Anthropic | Lightweight, Low Cost |
| **T2 Lightweight** | [DeepSeek-V4-Flash](https://deepseek.com) | DeepSeek | Ultra-High Cost-Performance |

### Tool Layer

| Category | Representative Tools | Core Capabilities |
| ---------- | ---------------------- | ------------------- |
| **AI IDE** | Cursor, Windsurf | AI-Native Coding, Agent Mode |
| **Coding Agents** | [Codex](https://openai.com), Claude Code | Autonomous Coding in Terminal, PR Generation |
| **AI App Builders** | Bolt.new, Lovable, v0 | Generating Complete Apps with One Prompt |
| **AI Search** | Perplexity, Kimi | Real-Time Search + AI Summarization |
| **Agent Frameworks** | [OpenAI Agents SDK](https://platform.openai.com/docs/assistants/overview), LangGraph | Agent Orchestration, Tool Calling |
| **Tool Protocols** | MCP, A2A | Standardized Tool Connections |

### Trend Layer

1. **Agents as the Core**: All frontier models feature Agent capabilities as their core selling point.
2. **Explosion of Coding Agents**: Codex, Claude Code, and Cursor have comprehensively transitioned to Agentic paradigms.
3. **Computer Use as Standard**: GPT-5.5 OSWorld 78.7%, Claude Opus 4.8 Online-Mind2Web 84%.
4. **Multi-Agent Coordination**: Gemini 3.5 focuses on multi-Agent workflows.
5. **Mainstreaming of Vibe Coding**: Natural language-driven development approaches are widely accepted.
6. **MCP as the De Facto Standard**: Supported by all mainstream IDEs/frameworks.
7. **Continuous Catch-Up by Chinese Models**: DeepSeek V4, GLM-5.1, and Kimi K2-6 have all reached frontier levels.

---

> Data-driven, automated maintenance, community co-creation.
