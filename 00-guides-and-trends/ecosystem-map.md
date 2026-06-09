# AI 技术栈生态全景图

> 最后更新：2026-06-08

---

## 架构分层图

```mermaid
graph TD
    subgraph 00["🎯 00 选型指南与趋势"]
        T1[场景化推荐]
        T2[月度趋势]
        T3[生态大图]
    end

    subgraph 01["🧠 01 基础大模型层"]
        M1[语言模型<br>GPT-5.5 / Claude Opus 4.8 / Gemini 3.5]
        M2[多模态模型<br>图像 / 视频 / 音频]
        M3[嵌入模型<br>BGE-M3 / Cohere]
    end

    subgraph 02["🏗️ 02 基础设施层"]
        I1[推理引擎<br>vLLM / Ollama]
        I2[API 网关<br>LiteLLM / OpenRouter]
        I3[向量数据库<br>Milvus / Qdrant]
    end

    subgraph 03["📊 03 数据与知识层"]
        D1[数据解析]
        D2[知识图谱]
        D3[RAG 引擎]
    end

    subgraph 04["⚙️ 04 开发框架层"]
        F1[LLM 框架<br>LangChain / LlamaIndex]
        F2[多 Agent<br>LangGraph / CrewAI]
    end

    subgraph 05["🧩 05 低代码平台"]
        L1[AI 构建<br>Dify / Coze]
        L2[工作流<br>n8n / Make]
    end

    subgraph 06["🔌 06 工具与协议"]
        P1[MCP 生态]
        P2[Function Calling]
        P3[浏览器控制]
    end

    subgraph 07["🧱 07 技能与插件"]
        S1[开源技能库]
        S2[平台插件]
    end

    subgraph 08["📈 08 可观测性"]
        O1[追踪调试]
        O2[成本监控]
        O3[评测基准]
    end

    subgraph 09["🛡️ 09 安全合规"]
        G1[护栏]
        G2[审核]
    end

    subgraph 10["🖥️ 10 终端应用"]
        A1[编程 IDE<br>Cursor / Claude Code]
        A2[搜索研究<br>Perplexity / Kimi]
        A3[办公创作<br>Notion AI / Suno]
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

## 技术栈流向

```mermaid
flowchart LR
    User[用户/开发者] --> Choose{选型指南}
    Choose --> Model[大模型层]
    Model --> Infra[基础设施]
    Infra --> Data[数据知识]
    Data --> Dev[开发框架]
    Data --> Low[低代码平台]
    Dev --> Tools[工具协议]
    Low --> Plugins[技能插件]
    Tools --> Plugins
    Plugins --> Apps[终端应用]
    Model --> Obs[可观测性]
    Dev --> Obs
    Obs --> Apps
    Model --> Safety[安全合规]

    style User fill:#e94560,color:#fff
    style Apps fill:#e94560,color:#fff
```

---

## 核心数据流

```mermaid
flowchart TB
    Data[YAML 数据源<br>data/*.yaml] --> Script[build_docs.py<br>自动渲染]
    Script --> MD[Markdown 文件<br>各层级 .md]
    MD --> GitHub[GitHub 仓库]
    MD --> Site[VitePress 站点]
    Issue[Issue Form<br>社区提交] --> Action[GitHub Action]
    Action --> PR[自动 PR]
    PR --> Data
```

---

## 2026年6月 AI 格局概览

### 模型层

| 梯队 | 模型 | 厂商 | 定位 |
| ------ | ------ | ------ | ------ |
| **T0 旗舰** | [GPT-5.5](https://openai.com) Pro | OpenAI | 智能最强，Agent/编码/知识工作 |
| **T0 旗舰** | [Claude Opus 4](https://anthropic.com).8 | Anthropic | Agent 可靠性最强，编码一致性 |
| **T0 旗舰** | [Gemini 3.5 Flash](https://gemini.google.com) | Google | Agent 工作流，多 Agent 协调 |
| **T1 高性价比** | [DeepSeek-V4-Pro](https://deepseek.com) | DeepSeek | 开源 MoE，1M 上下文 |
| **T1 高性价比** | [Qwen3-Coder](https://qwen.ai)-480B | 阿里 | Agent 级编程，开源 |
| **T1 高性价比** | [GLM-5.1](https://open.bigmodel.cn) | 智谱 | 全模态矩阵，中文优化 |
| **T2 轻量级** | [GPT-5.5-mini](https://openai.com) | OpenAI | 高性价比，快速响应 |
| **T2 轻量级** | [Claude Haiku 4](https://anthropic.com) | Anthropic | 轻量级，低成本 |
| **T2 轻量级** | [DeepSeek-V4-Flash](https://deepseek.com) | DeepSeek | 超高性价比 |

### 工具层

| 类别 | 代表工具 | 核心能力 |
| ------ | ---------- | ---------- |
| **AI IDE** | Cursor, Windsurf | AI 原生编码，Agent 模式 |
| **编码 Agent** | [Codex](https://openai.com), Claude Code | 终端内自主编码，PR 生成 |
| **AI App Builder** | Bolt.new, Lovable, v0 | 一句话生成完整应用 |
| **AI 搜索** | Perplexity, Kimi | 实时搜索+AI 总结 |
| **Agent 框架** | [OpenAI Agents SDK](https://platform.openai.com/docs/assistants/overview), LangGraph | Agent 编排，工具调用 |
| **工具协议** | MCP, A2A | 标准化工具连接 |

### 趋势层

1. **Agent 成为核心**：所有前沿模型均以 Agent 能力为核心卖点
2. **编码 Agent 爆发**：Codex、Claude Code、Cursor 全面 Agent 化
3. **计算机使用成为标配**：GPT-5.5 OSWorld 78.7%，Claude Opus 4.8 Online-Mind2Web 84%
4. **多 Agent 协调**：Gemini 3.5 专注多 Agent 工作流
5. **Vibe Coding 主流化**：自然语言驱动的开发方式被广泛接受
6. **MCP 成为事实标准**：所有主流 IDE/框架均已支持
7. **中国模型持续追赶**：DeepSeek V4、GLM-5.1、Kimi K2-6 均达到前沿水平

---

> 数据驱动，自动化维护，社区共建。
