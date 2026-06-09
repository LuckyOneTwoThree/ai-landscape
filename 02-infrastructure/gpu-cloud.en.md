# GPU Cloud Services

> Last Updated: 2026-06-08
> Data Source: Automatically generated from `data/infrastructure.yaml`

---

## 🤔 When Do You Need GPU Cloud Services?

| Scenario | **Need GPU Cloud?** | Reason |
| ------ | **-------------** | ------ |
| **No GPU, want to run open-source models** | **✅ Yes** | Fastest way to get started |
| **Have GPU but insufficient VRAM** | **✅ Yes** | Rent larger GPUs on demand |
| **Production needs high availability** | **✅ Yes** | Serverless auto-scaling |
| **Already have sufficient GPU clusters** | **❌ No** | Self-hosting offers better control |
| **Only calling APIs, not running models** | **❌ No** | Just use model provider APIs |

> [!TIP]
> **Serverless vs GPU Rentals**
> - **Serverless** (Together AI/Fireworks/Replicate): Pay per request, zero maintenance, ideal for inference.
> - **GPU Rentals** (RunPod/Lambda Labs): Pay per hour, full control, ideal for training + custom inference.

---

## 📋 GPU Cloud Services Overview

<!-- AUTOGEN_START -->

### ☁️ Serverless Inference

| Name | Description | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [Together AI](https://together.ai) | The most popular open-source model hosting platform, Serverless inference + Fine-tuning | gpu-acceleration, serverless, open-source | 1-click deployment for 200+ open-source models<br>Serverless pay-per-use inference<br>Fine-tuning service<br>Ultra-low cold start latency |
| [Fireworks AI](https://fireworks.ai) | High-speed inference platform, focused on extreme latency optimization for open-source models | gpu-acceleration, fast-inference, open-source | Industry-leading inference speed<br>Deep optimization for open-source models<br>Function Calling support<br>Batch inference |
| [Replicate](https://replicate.com) | The simplest model deployment platform, run models with one line of code | gpu-acceleration, easy-to-use, multimodal | 1-line code model deployment<br>Rich multimodal models<br>API + Web interface<br>Per-second billing |
| [Modal](https://modal.com) | Developer-oriented Serverless GPU platform, Python-native | gpu-acceleration, serverless, coding-assistant | Python-native development experience<br>Auto-scaling<br>Ultra-low cold start<br>Ideal for custom inference logic |
| [Silicon Flow (硅基流动)](https://siliconflow.cn) | The most popular open-source model inference platform in China, extreme cost-effectiveness | gpu-acceleration, china-based, cost-effective, open-source | Most popular open-source model platform in China<br>DeepSeek/Qwen/FLUX 1-click deployment<br>Extreme cost-effectiveness<br>Free quota |

### 💳 GPU Rentals

| Name | Description | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [RunPod](https://runpod.io) | GPU rental marketplace, rent A100/H100 by the hour | gpu-acceleration, cost-effective | Hourly GPU rentals<br>A100/H100 availability<br>Serverless + Pod modes<br>Rich community templates |
| [Lambda Labs](https://lambdalabs.com) | GPU cloud provider, highly cost-effective H100 clusters | gpu-acceleration, distributed | Cost-effective H100 clusters<br>1-4 GPUs to multi-node setups<br>Ideal for large-scale training |

<!-- AUTOGEN_END -->

---

## 🔧 Selection Recommendations

| Scenario | Recommendation | Reason |
| ------ | ------ | ------ |
| **Quickly run open-source models** | [Together AI](https://together.ai) / [Silicon Flow](https://siliconflow.cn) | 1-click deployment for 200+ models |
| **Extreme inference speed** | [Fireworks AI](https://fireworks.ai) | Industry-leading latency optimization |
| **1-line code deployment** | [Replicate](https://replicate.com) | Simplest deployment experience |
| **Custom inference logic** | [Modal](https://modal.com) | Python-native, highest flexibility |
| **Large-scale training** | [Lambda Labs](https://lambdalabs.com) / [RunPod](https://runpod.io) | Cost-effective H100 clusters |
| **Users in China** | [Silicon Flow](https://siliconflow.cn) (硅基流动) | Most popular in China, free quota |

---

> **Update Frequency**: Updated quarterly
> **Automation**: Run `python scripts/build_docs.py` to re-render tables from YAML.
