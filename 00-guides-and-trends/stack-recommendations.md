# 场景化技术栈推荐

> 最后更新：2026-06-08
> 本文件提供面向不同场景的"黄金组合"技术栈推荐。

---

## 一、个人开发者 AI 全栈方案

| 环节 | 推荐方案 | 备选方案 |
|------|---------|---------|
| 推理模型 | DeepSeek-V4-Pro (云端) | Qwen3-235B (本地) |
| 通用模型 | GPT-5.5 (云端) | Claude Opus 4.8 |
| 本地部署 | Ollama + Qwen3-8B | LM Studio |
| Agent 框架 | LangChain + LangGraph | OpenAI Agents SDK |
| 工具协议 | MCP | Function Calling |
| 知识库 | Chroma + LlamaIndex | Qdrant |
| 部署 | Vercel / Fly.io | Railway |

**月成本估算**：$20-50 (API 调用) + 免费本地推理

---

## 二、企业 RAG 方案

| 环节 | 推荐方案 | 备选方案 |
|------|---------|---------|
| 推理引擎 | vLLM 自部署 / Azure OpenAI | Claude Opus 4.8 API |
| 应用平台 | Dify (自部署) | Coze |
| 数据解析 | Unstructured + LlamaParse | Docling |
| 向量数据库 | Milvus (分布式) | Qdrant |
| 可观测性 | Langfuse (自部署) | LangSmith |
| 安全护栏 | NeMo Guardrails | Guardrails AI |

**月成本估算**：$500-2000 (GPU + API)

---

## 三、多 Agent 自动化方案

| 环节 | 推荐方案 | 备选方案 |
|------|---------|---------|
| 编排框架 | LangGraph | CrewAI |
| 工具集成 | Composio (250+ 连接器) | MCP Servers |
| 工作流 | n8n | Make |
| 追踪调试 | LangSmith | AgentOps |
| 模型 | GPT-5.5 / Claude Opus 4.8 | DeepSeek-V4-Pro |

**月成本估算**：$50-200

---

## 四、低代码快速原型方案

| 环节 | 推荐方案 | 备选方案 |
|------|---------|---------|
| 构建平台 | Dify | Coze |
| RAG | 平台内置 | FastGPT |
| 插件 | 平台插件市场 | MCP Servers |
| 模型 | GPT-5.5-mini / Claude Haiku 4 | DeepSeek-V4-Flash |

**月成本估算**：$10-50

---

## 五、AI 编程提效方案

| 环节 | 推荐方案 | 备选方案 |
|------|---------|---------|
| IDE | Cursor | Windsurf |
| CLI 助手 | Claude Code | Codex CLI |
| 模型 | GPT-5.5 / Claude Opus 4.8 | DeepSeek-V4-Pro |
| 代码搜索 | GitHub Copilot | Augment Code |

**月成本估算**：$20-50 (IDE 订阅 + API)

---

## 六、Agent 开发方案

| 环节 | 推荐方案 | 备选方案 |
|------|---------|---------|
| 框架 | OpenAI Agents SDK | LangGraph |
| 工具协议 | MCP (Model Context Protocol) | A2A (Agent-to-Agent) |
| 计算机使用 | GPT-5.5 (OSWorld 78.7%) | Claude Opus 4.8 (Online-Mind2Web 84%) |
| 编码 Agent | Codex | Claude Code |
| 追踪调试 | LangSmith | AgentOps |
| 安全护栏 | NeMo Guardrails | Guardrails AI |

**月成本估算**：$100-500

---

## 七、多模态内容创作方案

| 环节 | 推荐方案 | 备选方案 |
|------|---------|---------|
| 文本生成 | GPT-5.5 / Claude Opus 4.8 | Gemini 3.5 Flash |
| 图像生成 | Midjourney / DALL-E 3 | Stable Diffusion |
| 视频生成 | Sora / Runway Gen-3 | Pika |
| 音频生成 | ElevenLabs / Suno | Bark |
| 代码生成 | Cursor / Claude Code | GitHub Copilot |

**月成本估算**：$50-200

---

## 八、数据分析方案

| 环节 | 推荐方案 | 备选方案 |
|------|---------|---------|
| 数据处理 | Pandas / Polars | Dask |
| 可视化 | Plotly / Streamlit | Matplotlib |
| 机器学习 | Scikit-learn / XGBoost | LightGBM |
| 深度学习 | PyTorch / TensorFlow | JAX |
| 大模型分析 | GPT-5.5 / Claude Opus 4.8 | Gemini 3.1 Pro |

**月成本估算**：$20-100

---

## 成本对比表

| 方案 | 月成本范围 | 适合场景 |
|------|-----------|----------|
| 个人开发者全栈 | $20-50 | 独立开发、学习、实验 |
| 企业 RAG | $500-2000 | 企业知识库、客服系统 |
| 多 Agent 自动化 | $50-200 | 工作流自动化、任务编排 |
| 低代码快速原型 | $10-50 | 快速验证想法、MVP |
| AI 编程提效 | $20-50 | 日常开发、代码审查 |
| Agent 开发 | $100-500 | Agent 产品、自动化系统 |
| 多模态创作 | $50-200 | 内容创作、设计 |
| 数据分析 | $20-100 | 数据科学、机器学习 |

---

## 技术栈选择指南

### 按预算选择

| 预算 | 推荐方案 |
|------|----------|
| **$0-20/月** | 本地模型 (Ollama + Qwen3) + 开源工具 |
| **$20-50/月** | 云端 API (DeepSeek/GPT-5.5-mini) + Cursor |
| **$50-200/月** | 多模型组合 + 专业工具 |
| **$200+/月** | 全栈方案 + 企业级工具 |

### 按技术栈选择

| 技术栈 | 推荐方案 |
|--------|----------|
| **Python 全栈** | LangChain + FastAPI + Streamlit |
| **TypeScript 全栈** | Mastra + Next.js + Vercel |
| **低代码** | Dify + Coze + n8n |
| **企业级** | Azure OpenAI + LangChain + Milvus |

### 按场景选择

| 场景 | 推荐方案 |
|------|----------|
| **快速原型** | Bolt.new / Lovable / v0 |
| **专业开发** | Cursor / Claude Code / Codex |
| **企业应用** | Dify + Milvus + Langfuse |
| **Agent 产品** | OpenAI Agents SDK + MCP |

---

> **更新频率**：每季度更新一次。
