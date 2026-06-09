# 🌐 AI Tech Stack Landscape — AI 技术栈生态全景图

![Stars](https://img.shields.io/github/stars/ai-landscape/ai-landscape?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)
![Tools](https://img.shields.io/badge/tools-463-blue?style=flat-square)
![Last Update](https://img.shields.io/badge/last--update-2026--06--08-brightgreen?style=flat-square)

## 架构全景

```mermaid
graph TD
    subgraph L0["00 选型指南"]
        T[场景推荐 · 趋势追踪]
    end
    subgraph L1["01-03 模型·基建·数据"]
        M[大模型] --> I[基础设施]
        I --> D[数据知识]
    end
    subgraph L45["04-05 开发框架"]
        F[代码框架] & L[低代码平台]
    end
    subgraph L67["06-07 工具·插件"]
        P[协议工具] & S[技能插件]
    end
    subgraph L89["08-09 运维·安全"]
        O[可观测性] & G[安全合规]
    end
    subgraph LA["10 终端应用"]
        A[编程 · 搜索 · 创作]
    end
    D --> F & L
    F --> P
    L --> S
    P & S --> A
    M --> O & G
    style L0 fill:#e94560,color:#fff
    style LA fill:#e94560,color:#fff
```

> 一份全面、结构化的 AI 技术栈目录，涵盖从基础大模型到终端应用的完整生态。帮助开发者、产品经理和决策者快速了解 AI 领域的技术选型与全景格局。欢迎 Star ⭐ 和 PR 贡献！

---

## 📊 数据统计

| 指标 | 数量 |
|------|------|
| 总条目数 | 463 |
| 开源项目 | 322 (69.6%) |
| Markdown 文件 | 34 |
| YAML 数据源 | 11 |
| 覆盖分类 | 10 个模块 |

---

## 📑 快速导航

| 层级 | 目录 | 说明 |
|------|------|------|
| `00` | [选型指南与趋势](./00-guides-and-trends/) | 行业趋势分析、技术选型建议与横向对比 |
| `01` | [基础大模型层](./01-foundation-models/) | LLM、多模态模型、开源与闭源模型汇总 |
| `02` | [基础设施层](./02-infrastructure/) | GPU 云、推理引擎、训练平台、MLOps |
| `03` | [数据与知识层](./03-data-and-knowledge/) | 数据管线、向量数据库、知识图谱、RAG |
| `04` | [代码开发框架层](./04-dev-frameworks/) | LangChain、LlamaIndex、Semantic Kernel 等开发框架 |
| `05` | [低代码平台](./05-lowcode-platforms/) | Dify、Coze、Flowise 等低代码/无代码 AI 构建平台 |
| `06` | [底层工具与协议](./06-tools-and-protocols/) | MCP、A2A、Function Calling、Tool Use 等协议与工具 |
| `07` | [技能与插件](./07-skills-and-plugins/) | Agent 技能、插件市场、能力扩展模块 |
| `08` | [可观测性与运维](./08-observability/) | LLM 监控、Tracing、评估、日志与告警 |
| `09` | [安全与合规](./09-safety-and-compliance/) | 内容审核、数据隐私、AI 安全防护、合规框架 |
| `10` | [终端成品应用](./10-applications/) | AI 助手、编程工具、搜索、创意等终端产品 |

---

## 🧭 我应该从哪里开始？

| 角色 | 推荐入口 | 原因 |
|------|----------|------|
| 👨‍💻 **开发者** | [`04-dev-frameworks`](./04-dev-frameworks/) → [`06-tools-and-protocols`](./06-tools-and-protocols/) | 快速找到构建 AI 应用所需的框架和协议 |
| 📋 **产品经理** | [`05-lowcode-platforms`](./05-lowcode-platforms/) → [`07-skills-and-plugins`](./07-skills-and-plugins/) | 了解可落地的低代码方案和已有插件能力 |
| 🙋 **终端用户** | [`10-applications`](./10-applications/) | 直接浏览已上线的 AI 产品和工具 |
| 🧑‍💼 **决策者** | [`00-guides-and-trends`](./00-guides-and-trends/) | 行业全景、趋势判断和选型参考 |

---

## 🚀 快速开始

### 本地运行

```bash
# 克隆仓库
git clone https://github.com/ai-landscape/ai-landscape.git
cd ai-landscape

# 安装依赖
pip install pyyaml

# 构建文档
python scripts/build_docs.py

# 查看生成的文档
open docs/index.html
```

### 贡献新工具

1. Fork 本仓库
2. 编辑 `data/` 目录下的 YAML 文件
3. 提交 PR，我们会尽快审核

或者直接 [提交 Issue](https://github.com/ai-landscape/ai-landscape/issues/new?template=tool-submission.yml) 告诉我们你发现的工具！

---

## 🤝 贡献指南

我们欢迎任何形式的贡献！请先阅读 [CONTRIBUTING.md](./CONTRIBUTING.md) 了解：

- 如何提交新的工具/产品条目
- 内容格式与分类规范
- PR 流程与 Review 标准

> 💡 发现遗漏的工具或错误信息？提个 Issue 或直接开 PR，都是对我们最好的支持！

---

## 📄 License

本项目采用 [MIT License](./LICENSE) 开源。

---

## 🙏 致谢

感谢所有贡献者和以下开源项目：

- [awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted)
- [awesome-chatgpt-plugins](https://github.com/acheong08/awesome-chatgpt-plugins)
- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)
