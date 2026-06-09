# 推理引擎与部署框架

> 最后更新：2026-06-08
> 数据来源：`data/infrastructure.yaml` 自动生成

---

## 🏗️ 本地部署实战

对个人开发者来说，最核心的问题是：**我的显卡能跑什么模型？**

| 显卡 | 显存 | 能跑的模型 (4-bit 量化) | 推荐引擎 |
|------|------|------------------------|---------|
| **RTX 4090** | 24GB | Qwen3-32B, Llama-3-70B (勉强) | [vLLM](https://github.com/vllm-project/vllm) / [Ollama](https://ollama.com) |
| **RTX 3090** | 24GB | Qwen3-14B, DeepSeek-V4-16B | [Ollama](https://ollama.com) / [llama.cpp](https://github.com/ggerganov/llama.cpp) |
| **RTX 4070** | 12GB | [Qwen3-8B](https://qwen.ai), [Phi-4](https://azure.microsoft.com/en-us/products/phi)-14B | [Ollama](https://ollama.com) |
| **Mac M4 Pro** | 24GB 统一 | Qwen3-32B, Llama-3-70B (量化) | [Ollama](https://ollama.com) / MLX |
| **Mac M4** | 16GB 统一 | Qwen3-14B, [Phi-4](https://azure.microsoft.com/en-us/products/phi)-14B | [Ollama](https://ollama.com) / MLX |
| **CPU only** | — | [Qwen3-8B](https://qwen.ai) (慢), [Phi-4](https://azure.microsoft.com/en-us/products/phi)-mini | [llama.cpp](https://github.com/ggerganov/llama.cpp) |

> [!TIP]
> **Mac 的统一内存是隐藏优势**
> Mac M4 Pro 的 24GB 统一内存可以全用于模型推理，实际可用显存比 RTX 4090 还多。跑 70B 模型用 Q4_K_M 量化，Mac 反而比 4090 更稳。

**最简本地部署（Ollama）**：
```bash
# 安装 Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# 一键运行
ollama run qwen3:14b          # 14B 模型，RTX 3090 可跑
ollama run deepseek-v4:16b    # DeepSeek 16B，中文优秀
ollama run phi4:14b            # Phi-4 14B，推理能力强
```

---

## 📋 推理引擎总览

<!-- AUTOGEN_START -->

### ☁️ 云端推理

| 引擎 | 语言 | 量化 | 最大模型 | 部署方式 | 核心亮点 |
|------|------|------|----------|----------|----------|
| ✅ [vLLM](https://github.com/vllm-project/vllm) | Python | AWQ, GPTQ, FP8, INT4 | 405B | Docker, pip | PagedAttention 连续批处理<br>多 LoRA 支持<br>OpenAI 兼容 API |
| ✅ [SGLang](https://github.com/sgl-project/sglang) | Python | AWQ, GPTQ, FP8 | 405B | Docker, pip | RadixAttention 高吞吐<br>结构化生成 (JSON/正则)<br>多模态支持 |
| ✅ [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | C++/Python | FP8, INT4, INT8 | 405B | Docker, Triton | NVIDIA GPU 深度优化<br>FP8/INT4 量化<br>推测解码 |
| ✅ [TGI (Text Generation Inference)](https://github.com/huggingface/text-generation-inference) | Rust | GPTQ, AWQ, bitsandbytes | 70B | Docker | HuggingFace 生态集成<br>简单部署<br>Token 流式输出 |
| ✅ [LMDeploy](https://github.com/InternLM/lmdeploy) | Python/C++ | W4A16, W8A16, KV-INT4 | 70B | Docker, pip | TurboMind 高吞吐<br>W4A16/KV Cache 量化<br>InternLM/Qwen/Llama 支持 |
| ✅ [xinference](https://github.com/xorbitsai/inference) | Python | 取决于后端 | 405B | Docker, pip | 多后端 (vLLM/llama.cpp/TensorRT)<br>模型管理/分布式推理<br>OpenAI 兼容 API |

### 💻 本地推理

| 引擎 | 语言 | 量化 | 最大模型 | 部署方式 | 核心亮点 |
|------|------|------|----------|----------|----------|
| ✅ [Ollama](https://ollama.com) | Go | GGUF | 70B | macOS, Linux, Windows | 一键安装运行<br>REST API<br>模型库丰富 |
| ✅ [MLX LM](https://github.com/ml-explore/mlx-lm) | - | - | - | - | Apple Silicon 优化<br>统一内存<br>5K Stars |
|  [LM Studio](https://lmstudio.ai) | — | GGUF | 70B | macOS, Linux, Windows | 图形界面<br>本地模型运行<br>内置模型搜索 |
| ✅ [GPT4All](https://gpt4all.io) | C++ | GGUF | 13B | macOS, Linux, Windows | 离线运行<br>简单易用<br>本地知识库 |
| ✅ [Jan](https://jan.ai) | TypeScript | GGUF | 70B | macOS, Linux, Windows | 开源桌面应用<br>本地模型运行<br>插件扩展 |
| ✅ [ExLlamaV2](https://github.com/turboderp/exllamav2) | Python/C++ | EXL2, GPTQ, 2-8bit | 70B | Linux, Windows | EXL2 混合精度量化 (2-8 bit)<br>24GB 显存跑 70B<br>速度极快 |
| ✅ [LocalAI](https://github.com/mudler/LocalAI) | Go | GGUF, GPTQ | 70B | Docker, Linux, macOS | 支持 LLM/语音/图像/视频<br>OpenAI 兼容 API<br>CPU/GPU 运行 |

### 📱 端侧推理

| 引擎 | 语言 | 量化 | 最大模型 | 部署方式 | 核心亮点 |
|------|------|------|----------|----------|----------|
| ✅ [MLC-LLM](https://github.com/mlc-ai/mlc-llm) | Python/C++ | Q4, Q8 | 70B | 全平台, 移动端 | 通用 GPU 编译<br>全平台部署<br>高性能 |
|  [Core ML](https://developer.apple.com/core-ml/) | Swift | INT4, INT8 | 7B | iOS, macOS | Apple 设备原生优化<br>Neural Engine 加速<br>Swift 集成 |
| ✅ [ONNX Runtime](https://onnxruntime.ai) | C++/Python | INT4, INT8, FP16 | 70B | 全平台 | 跨平台推理<br>多硬件后端<br>生产级 |
| ✅ [WebLLM](https://github.com/mlc-ai/web-llm) | TypeScript | Q4, Q8 | 7B | 浏览器 | 浏览器端推理<br>WebGPU 加速<br>无需服务器 |
| ✅ [MNN](https://github.com/alibaba/MNN) | C++ | INT4, INT8, FP16 | 7B | Android, iOS, 嵌入式 | 阿里出品<br>移动端优化<br>极致轻量 |

### 🚪 网关

| 引擎 | 语言 | 量化 | 最大模型 | 部署方式 | 核心亮点 |
|------|------|------|----------|----------|----------|
| ✅ [llama.cpp](https://github.com/ggerganov/llama.cpp) | C++ | GGUF, Q4_K_M, Q5_K_M | 70B | 全平台 | C++ 实现，无依赖<br>GGUF 量化格式<br>CPU/GPU 混合推理 |

<!-- AUTOGEN_END -->

---

## ⚡ 量化：花 5 分钟省 50% 显存

量化的核心取舍：**用一点质量损失换巨大的显存节省**。

| 格式 | 精度 | 大小缩减 | 速度 | 质量损失 | 怎么用 |
|------|------|---------|------|---------|--------|
| **FP8** | 8-bit | 2× | ⭐⭐⭐⭐⭐ | 极低 | vLLM 直接支持 |
| **AWQ** | 4-bit | 4× | ⭐⭐⭐⭐⭐ | 低 | vLLM / AutoGPTQ |
| **GPTQ** | 4-bit | 4× | ⭐⭐⭐⭐ | 低 | 兼容性最好 |
| **GGUF** | 2-8 bit | 2-8× | ⭐⭐⭐⭐ | 可变 | Ollama / llama.cpp 直接用 |
| **EXL2** | 2-6 bit | 2-6× | ⭐⭐⭐⭐⭐ | 同大小最高 | ExLlamaV2，极客玩家 |

> [!TIP]
> **不知道选什么量化？**
> - 用 Ollama → GGUF（`ollama run` 自动下载 GGUF）
> - 用 vLLM → AWQ 或 FP8（吞吐最高）
> - 用 ExLlamaV2 → EXL2（同显存塞更大模型）

**量化对质量的影响有多大？** 以 Qwen3-32B 为例：

| 量化 | 模型大小 | MMLU | 代码生成 | 数学推理 |
|------|---------|------|---------|---------|
| FP16 (原始) | 64GB | 78.5 | 82.3 | 71.2 |
| AWQ-4bit | 16GB | 77.8 (-0.7) | 81.5 (-0.8) | 69.8 (-1.4) |
| GGUF-Q4 | 18GB | 77.2 (-1.3) | 80.9 (-1.4) | 68.5 (-2.7) |

> [!TIP]
> **4-bit 量化的质量损失通常 < 2%**，但显存节省 4 倍。除非你是做精度敏感的生产系统，否则 4-bit 完全够用。

## 🔥 2026 前沿：KV-Cache 与 MoE 部署

**KV-Cache 优化**：跑长上下文（32K+）时，KV-Cache 占用的显存比模型本身还多。

| 引擎 | KV-Cache 策略 | 效果 |
|------|--------------|------|
| **vLLM** | PagedAttention | 显存占用降低 40-60% |
| **SGLang** | RadixAttention | 多轮对话复用前缀 Cache，效果最佳 |
| **llama.cpp** | 量化 KV-Cache | KV 也量化，进一步省显存 |

**MoE 模型部署**：MoE 模型（如 DeepSeek-V4-685B）总参数量巨大，但每次推理只激活部分 Expert。

| 显卡配置 | 能跑的 MoE 模型 | 策略 |
|---------|----------------|------|
| 4×A100 (80GB) | DeepSeek-V4-685B | Expert 并行 |
| 2×A100 | Mixtral-8x22B | Expert 缓存 + 预加载 |
| 单卡 RTX 4090 | Phi-4-MoE (激活 7B) | 直接跑 |

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
