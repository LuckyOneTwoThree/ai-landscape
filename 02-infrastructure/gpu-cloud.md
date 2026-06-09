# GPU 云服务

> 最后更新：2026-06-08
> 数据来源：`data/infrastructure.yaml` 自动生成

---

## 🤔 什么时候需要 GPU 云服务？

| 场景 | 需要 GPU 云吗 | 理由 |
| ------ | ------------- | ------ |
| **没有 GPU，想跑开源模型** | ✅ 需要 | 最快的起步方式 |
| **有 GPU 但显存不够** | ✅ 需要 | 按需租用更大显卡 |
| **生产环境需要高可用** | ✅ 需要 | Serverless 自动扩缩容 |
| **已有足够 GPU 集群** | ❌ 不需要 | 自建更可控 |
| **只是调 API，不跑模型** | ❌ 不需要 | 直接用模型厂商 API |

> [!TIP]
> **Serverless vs GPU 租赁**
> - **Serverless**（Together AI/Fireworks/Replicate）：按请求计费，零运维，适合推理
> - **GPU 租赁**（RunPod/Lambda Labs）：按小时计费，完全控制，适合训练 + 自定义推理

---

## 📋 GPU 云服务总览

<!-- AUTOGEN_START -->

### ☁️ Serverless 推理

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [Together AI](https://together.ai) | 最流行的开源模型托管平台，Serverless 推理 + Fine-tuning | gpu-acceleration, serverless, open-source | 200+ 开源模型一键部署<br>Serverless 推理按量付费<br>Fine-tuning 微调服务<br>极低冷启动延迟 |
| [Fireworks AI](https://fireworks.ai) | 高速推理平台，专注开源模型极致延迟优化 | gpu-acceleration, fast-inference, open-source | 推理速度行业领先<br>开源模型深度优化<br>Function Calling 支持<br>批量推理 |
| [Replicate](https://replicate.com) | 最简单的模型部署平台，一行代码跑模型 | gpu-acceleration, easy-to-use, multimodal | 一行代码部署模型<br>多模态模型丰富<br>API + Web 界面<br>按秒计费 |
| [Modal](https://modal.com) | 开发者导向的 Serverless GPU 平台，Python 原生 | gpu-acceleration, serverless, coding-assistant | Python 原生开发体验<br>自动扩缩容<br>极低冷启动<br>适合自定义推理逻辑 |
| [Silicon Flow (硅基流动)](https://siliconflow.cn) | 国内最流行的开源模型推理平台，极致性价比 | gpu-acceleration, china-based, cost-effective, open-source | 国内最流行的开源模型平台<br>DeepSeek/Qwen/FLUX 一键部署<br>极致性价比<br>免费额度 |

### 💳 GPU 租赁

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [RunPod](https://runpod.io) | GPU 租赁市场，按小时租用 A100/H100 | gpu-acceleration, cost-effective | 按小时租用 GPU<br>A100/H100 可用<br>Serverless + Pod 两种模式<br>社区模板丰富 |
| [Lambda Labs](https://lambdalabs.com) | GPU 云服务商，H100 集群性价比高 | gpu-acceleration, distributed | H100 集群性价比高<br>1-4 卡到多节点<br>适合大规模训练 |

<!-- AUTOGEN_END -->

---

## 🔧 选型建议

| 场景 | 推荐 | 理由 |
| ------ | ------ | ------ |
| **快速跑开源模型** | [Together AI](https://together.ai) / [Silicon Flow](https://siliconflow.cn) | 200+ 模型一键部署 |
| **极致推理速度** | [Fireworks AI](https://fireworks.ai) | 延迟优化行业领先 |
| **一行代码部署** | [Replicate](https://replicate.com) | 最简单的部署体验 |
| **自定义推理逻辑** | [Modal](https://modal.com) | Python 原生，灵活度最高 |
| **大规模训练** | [Lambda Labs](https://lambdalabs.com) / [RunPod](https://runpod.io) | H100 集群性价比高 |
| **国内用户** | [Silicon Flow](https://siliconflow.cn) (硅基流动) | 国内最流行，免费额度 |

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
