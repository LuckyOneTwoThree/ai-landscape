# Scenario-based Tech Stack Recommendations

> Last Updated: 2026-06-08
> This document provides "golden combination" tech stack recommendations tailored for various scenarios.

---

## 1. Personal Developer AI Full-Stack Solution

| Component | Recommended Solution | Alternative Solution |
| ----------- | ---------------------- | ---------------------- |
| Reasoning Model | [DeepSeek-V4-Pro](https://deepseek.com) (Cloud) | [Qwen3-235B](https://qwen.ai) (Local) |
| General Model | [GPT-5.5](https://openai.com) (Cloud) | [Claude Opus 4](https://anthropic.com).8 |
| Local Deployment | [Ollama](https://ollama.com) + [Qwen3-8B](https://qwen.ai) | [LM Studio](https://lmstudio.ai) |
| Agent Framework | LangChain + LangGraph | [OpenAI Agents SDK](https://platform.openai.com/docs/assistants/overview) |
| Tool Protocol | MCP | Function Calling |
| Knowledge Base | Chroma + LlamaIndex | Qdrant |
| Deployment | [Vercel](https://vercel.com) / Fly.io | Railway |

**Estimated Monthly Cost**: $20-50 (API usage) + Free local inference

---

## 2. Enterprise RAG Solution

| Component | Recommended Solution | Alternative Solution |
| ----------- | ---------------------- | ---------------------- |
| Inference Engine | [vLLM](https://github.com/vllm-project/vllm) Self-hosted / [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service) | [Claude Opus 4](https://anthropic.com).8 API |
| Application Platform | Dify (Self-hosted) | Coze |
| Data Parsing | [Unstructured](https://unstructured.io/) + [LlamaParse](https://cloud.llamaindex.ai/parse) | [Docling](https://github.com/DS4SD/docling) |
| Vector Database | Milvus (Distributed) | Qdrant |
| Observability | Langfuse (Self-hosted) | LangSmith |
| Security Guardrails | NeMo Guardrails | Guardrails AI |

**Estimated Monthly Cost**: $500-2000 (GPU + API)

---

## 3. Multi-Agent Automation Solution

| Component | Recommended Solution | Alternative Solution |
| ----------- | ---------------------- | ---------------------- |
| Orchestration Framework | LangGraph | CrewAI |
| Tool Integration | [Composio](https://composio.dev) (250+ Connectors) | MCP Servers |
| Workflow | [n8n](https://n8n.io) | [Make](https://make.com) |
| Tracing & Debugging | LangSmith | [AgentOps](https://agentops.ai) |
| Model | [GPT-5.5](https://openai.com) / [Claude Opus 4](https://anthropic.com).8 | [DeepSeek-V4-Pro](https://deepseek.com) |

**Estimated Monthly Cost**: $50-200

---

## 4. Low-Code Rapid Prototyping Solution

| Component | Recommended Solution | Alternative Solution |
| ----------- | ---------------------- | ---------------------- |
| Builder Platform | Dify | Coze |
| RAG | Built-in to Platform | FastGPT |
| Plugins | Platform Plugin Market | MCP Servers |
| Model | [GPT-5.5-mini](https://openai.com) / [Claude Haiku 4](https://anthropic.com) | [DeepSeek-V4-Flash](https://deepseek.com) |

**Estimated Monthly Cost**: $10-50

---

## 5. AI Programming Efficiency Solution

| Component | Recommended Solution | Alternative Solution |
| ----------- | ---------------------- | ---------------------- |
| IDE | Cursor | Windsurf |
| CLI Assistant | Claude Code | [Codex CLI](https://openai.com) |
| Model | [GPT-5.5](https://openai.com) / [Claude Opus 4](https://anthropic.com).8 | [DeepSeek-V4-Pro](https://deepseek.com) |
| Code Search | GitHub Copilot | Augment Code |

**Estimated Monthly Cost**: $20-50 (IDE Subscription + API)

---

## 6. Agent Development Solution

| Component | Recommended Solution | Alternative Solution |
| ----------- | ---------------------- | ---------------------- |
| Framework | [OpenAI Agents SDK](https://platform.openai.com/docs/assistants/overview) | LangGraph |
| Tool Protocol | MCP (Model Context Protocol) | A2A (Agent-to-Agent) |
| Computer Use | [GPT-5.5](https://openai.com) (OSWorld 78.7%) | [Claude Opus 4](https://anthropic.com).8 (Online-Mind2Web 84%) |
| Coding Agent | [Codex](https://openai.com) | Claude Code |
| Tracing & Debugging | LangSmith | [AgentOps](https://agentops.ai) |
| Security Guardrails | NeMo Guardrails | Guardrails AI |

**Estimated Monthly Cost**: $100-500

---

## 7. Multimodal Content Creation Solution

| Component | Recommended Solution | Alternative Solution |
| ----------- | ---------------------- | ---------------------- |
| Text Generation | [GPT-5.5](https://openai.com) / [Claude Opus 4](https://anthropic.com).8 | [Gemini 3.5 Flash](https://gemini.google.com) |
| Image Generation | [Midjourney](https://midjourney.com) / [DALL-E 3](https://openai.com) | [Stable Diffusion](https://stability.ai) |
| Video Generation | [Sora](https://openai.com) / [Runway Gen-3](https://runwayml.com) | [Pika](https://pika.art) |
| Audio Generation | [ElevenLabs](https://elevenlabs.io) / Suno | [Bark](https://github.com/suno-ai/bark) |
| Code Generation | Cursor / Claude Code | GitHub Copilot |

**Estimated Monthly Cost**: $50-200

---

## 8. Data Analysis Solution

| Component | Recommended Solution | Alternative Solution |
| ----------- | ---------------------- | ---------------------- |
| Data Processing | [Pandas](https://pandas.pydata.org) / [Polars](https://pola.rs) | [Dask](https://dask.org) |
| Visualization | [Plotly](https://plotly.com) / [Streamlit](https://streamlit.io) | [Matplotlib](https://matplotlib.org) |
| Machine Learning | [Scikit-learn](https://scikit-learn.org) / [XGBoost](https://xgboost.ai) | [LightGBM](https://lightgbm.readthedocs.io) |
| Deep Learning | [PyTorch](https://pytorch.org) / [TensorFlow](https://tensorflow.org) | [JAX](https://github.com/google/jax) |
| LLM Analysis | [GPT-5.5](https://openai.com) / [Claude Opus 4](https://anthropic.com).8 | [Gemini 3.1 Pro](https://gemini.google.com) |

**Estimated Monthly Cost**: $20-100

---

## Cost Comparison Table

| Solution | Monthly Cost Range | Suitable Scenarios |
| ---------- | -------------------- | -------------------- |
| Personal Developer Full-Stack | $20-50 | Indie hacking, learning, experimentation |
| Enterprise RAG | $500-2000 | Enterprise knowledge bases, customer service systems |
| Multi-Agent Automation | $50-200 | Workflow automation, task orchestration |
| Low-Code Rapid Prototyping | $10-50 | Idea validation, MVPs |
| AI Programming Efficiency | $20-50 | Daily development, code reviews |
| Agent Development | $100-500 | Agent products, automated systems |
| Multimodal Content Creation | $50-200 | Content creation, design |
| Data Analysis | $20-100 | Data science, machine learning |

---

## Tech Stack Selection Guide

### Selection by Budget

| Budget | Recommended Solution |
| -------- | ---------------------- |
| **$0-20/month** | Local Models ([Ollama](https://ollama.com) + Qwen3) + Open-Source Tools |
| **$20-50/month** | Cloud APIs (DeepSeek/[GPT-5.5-mini](https://openai.com)) + Cursor |
| **$50-200/month** | Multi-Model Combination + Professional Tools |
| **$200+/month** | Full-Stack Solutions + Enterprise Tools |

### Selection by Tech Stack

| Tech Stack | Recommended Solution |
| ------------ | ---------------------- |
| **Python Full-Stack** | LangChain + [FastAPI](https://fastapi.tiangolo.com) + [Streamlit](https://streamlit.io) |
| **TypeScript Full-Stack** | [Mastra](https://mastra.ai) + [Next.js](https://nextjs.org) + [Vercel](https://vercel.com) |
| **Low-Code** | Dify + Coze + [n8n](https://n8n.io) |
| **Enterprise** | [Azure OpenAI](https://azure.microsoft.com/en-us/products/ai-services/openai-service) + LangChain + Milvus |

### Selection by Scenario

| Scenario | Recommended Solution |
| ---------- | ---------------------- |
| **Rapid Prototyping** | Bolt.new / Lovable / v0 |
| **Professional Dev** | Cursor / Claude Code / [Codex](https://openai.com) |
| **Enterprise Apps** | Dify + Milvus + Langfuse |
| **Agent Products** | [OpenAI Agents SDK](https://platform.openai.com/docs/assistants/overview) + MCP |

---

> **Update Frequency**: Updated quarterly.
