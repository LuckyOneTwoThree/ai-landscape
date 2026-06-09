# 贡献指南

感谢你对 AI Landscape 项目的关注！我们欢迎社区贡献，帮助收录更多优秀的 AI 工具。

## 如何添加新工具

1. **Fork** 本仓库到你的 GitHub 账号
2. 在 `data/` 目录下找到对应的 YAML 分类文件
3. 按照下方模板格式添加条目
4. 提交 **Pull Request**

## 条目模板

```yaml
- name: 工具名称
  description: 一句话简要描述该工具的功能
  url: 官方网站链接
  repo: GitHub 仓库地址
  type: tool / platform / library / model
  category: 对应分类（与 data/ 下文件名一致）
  language: 主要编程语言
  license: 开源许可证（如 MIT、Apache-2.0）
  stars_estimate: GitHub Star 数（大致数量）
  status: active / maintenance / stale
  tags:
    - 标签1
    - 标签2
  highlights:
    - 亮点一：简要说明核心优势
    - 亮点二：突出特色或差异化
    - 亮点三：（可选）社区或生态亮点
```

## 质量门槛

为保持列表质量，收录的工具需满足以下至少一条：

- GitHub Star 数 **> 100**，或有知名机构/团队背书
- 项目处于 **积极维护** 状态（近 3 个月内有更新）
- 文档完善，有清晰的使用说明

### 标签（Tags）规范

提交新工具时，`tags` 字段必须从 `data/taxonomy.yaml` 中选取，禁止自造标签。

标签分为 5 类：
- **capability**: 能力特征（multimodal, reasoning, coding, agent 等）
- **deployment**: 部署方式（open-source, self-hosted, cloud-only 等）
- **architecture**: 架构特征（moe, stateful, graph 等）
- **use-case**: 使用场景（rag, search, coding-assistant 等）
- **ecosystem**: 生态集成（langchain, mcp, vscode-extension 等）

每个工具建议选 3-5 个最相关的标签。

## PR 说明要求

提交 PR 时，请在描述中说明：

1. **所属分类**：该工具应归入哪个类别
2. **推荐理由**：为什么值得收录（相比同类工具有何优势）
3. **重叠检查**：是否与列表中已有条目存在重复

## 行为准则

请参阅 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)，共同维护友好、包容的社区环境。
