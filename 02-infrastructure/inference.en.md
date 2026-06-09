# Inference Engines & Deployment Frameworks

> Last Updated: 2026-06-08
> Data Source: Automatically generated from `data/infrastructure.yaml`

---

## 🏗️ Local Deployment in Practice

For individual developers, the core question is: **What models can my GPU run?**

| GPU | **VRAM** | Capable Models (4-bit Quantization) | Recommended Engine |
| ------ | **------** | ------------------------ | --------- |
| **RTX 4090** | **24GB** | Qwen3-32B, Llama-3-70B (barely) | [vLLM](https://github.com/vllm-project/vllm) / [Ollama](https://ollama.com) |
| **RTX 3090** | **24GB** | Qwen3-14B, DeepSeek-V4-16B | [Ollama](https://ollama.com) / [llama.cpp](https://github.com/ggerganov/llama.cpp) |
| **RTX 4070** | **12GB** | [Qwen3-8B](https://qwen.ai), [Phi-4](https://azure.microsoft.com/en-us/products/phi)-14B | [Ollama](https://ollama.com) |
| **Mac M4 Pro** | **24GB Unified** | Qwen3-32B, Llama-3-70B (Quantized) | [Ollama](https://ollama.com) / MLX |
| **Mac M4** | **16GB Unified** | Qwen3-14B, [Phi-4](https://azure.microsoft.com/en-us/products/phi)-14B | [Ollama](https://ollama.com) / MLX |
| **CPU only** | **—** | [Qwen3-8B](https://qwen.ai) (Slow), [Phi-4](https://azure.microsoft.com/en-us/products/phi)-mini | [llama.cpp](https://github.com/ggerganov/llama.cpp) |

> [!TIP]
> **Mac's Unified Memory is a hidden advantage**
> The Mac M4 Pro's 24GB unified memory can be entirely allocated to model inference, meaning it has more effective VRAM than an RTX 4090. Running a 70B model with Q4_K_M quantization is often more stable on a Mac than on a 4090.

**Simplest Local Deployment (Ollama)**:
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Run with one click
ollama run qwen3:14b          # 14B model, playable on RTX 3090
ollama run deepseek-v4:16b    # DeepSeek 16B, excellent Chinese support
ollama run phi4:14b            # Phi-4 14B, strong reasoning capabilities
```

---

## 📋 Inference Engines Overview

<!-- AUTOGEN_START -->

### ☁️ Cloud Inference

| Engine | Language | Quantization | Max Model | Deployment | Core Highlights |
| ------ | ------ | ------ | ---------- | ---------- | ---------- |
| ✅ [vLLM](https://github.com/vllm-project/vllm) | Python | AWQ, GPTQ, FP8, INT4 | 405B | Docker, pip | PagedAttention continuous batching<br>Multi-LoRA support<br>OpenAI-compatible API |
| ✅ [SGLang](https://github.com/sgl-project/sglang) | Python | AWQ, GPTQ, FP8 | 405B | Docker, pip | RadixAttention high throughput<br>Structured generation (JSON/Regex)<br>Multimodal support |
| ✅ [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | C++/Python | FP8, INT4, INT8 | 405B | Docker, Triton | NVIDIA GPU deep optimization<br>FP8/INT4 quantization<br>Speculative decoding |
| ✅ [TGI (Text Generation Inference)](https://github.com/huggingface/text-generation-inference) | Rust | GPTQ, AWQ, bitsandbytes | 70B | Docker | HuggingFace ecosystem integration<br>Simple deployment<br>Token streaming output |
| ✅ [LMDeploy](https://github.com/InternLM/lmdeploy) | Python/C++ | W4A16, W8A16, KV-INT4 | 70B | Docker, pip | TurboMind high throughput<br>W4A16/KV Cache quantization<br>InternLM/Qwen/Llama support |
| ✅ [xinference](https://github.com/xorbitsai/inference) | Python | Depends on backend | 405B | Docker, pip | Multi-backend ([vLLM](https://github.com/vllm-project/vllm)/[llama.cpp](https://github.com/ggerganov/llama.cpp)/TensorRT)<br>Model management/distributed inference<br>OpenAI-compatible API |

### 💻 Local Inference

| Engine | Language | Quantization | Max Model | Deployment | Core Highlights |
| ------ | ------ | ------ | ---------- | ---------- | ---------- |
| ✅ [Ollama](https://ollama.com) | Go | GGUF | 70B | macOS, Linux, Windows | 1-click install and run<br>REST API<br>Rich model library |
| ✅ [MLX LM](https://github.com/ml-explore/mlx-lm) | - | - | - | - | Apple Silicon optimization<br>Unified memory<br>5K Stars |
| [LM Studio](https://lmstudio.ai) | — | GGUF | 70B | macOS, Linux, Windows | GUI application<br>Local model execution<br>Built-in model search |
| ✅ [GPT4All](https://gpt4all.io) | C++ | GGUF | 13B | macOS, Linux, Windows | Offline execution<br>Simple and easy to use<br>Local knowledge base |
| ✅ [Jan](https://jan.ai) | TypeScript | GGUF | 70B | macOS, Linux, Windows | Open-source desktop app<br>Local model execution<br>Plugin extensions |
| ✅ [ExLlamaV2](https://github.com/turboderp/exllamav2) | Python/C++ | EXL2, GPTQ, 2-8bit | 70B | Linux, Windows | EXL2 mixed-precision quantization (2-8 bit)<br>Run 70B on 24GB VRAM<br>Extremely fast |
| ✅ [LocalAI](https://github.com/mudler/LocalAI) | Go | GGUF, GPTQ | 70B | Docker, Linux, macOS | Supports LLM/Voice/Image/Video<br>OpenAI-compatible API<br>CPU/GPU execution |

### 📱 Edge Inference

| Engine | Language | Quantization | Max Model | Deployment | Core Highlights |
| ------ | ------ | ------ | ---------- | ---------- | ---------- |
| ✅ [MLC-LLM](https://github.com/mlc-ai/mlc-llm) | Python/C++ | Q4, Q8 | 70B | Cross-platform, Mobile | Universal GPU compilation<br>Cross-platform deployment<br>High performance |
| [Core ML](https://developer.apple.com/core-ml/) | Swift | INT4, INT8 | 7B | iOS, macOS | Apple device native optimization<br>Neural Engine acceleration<br>Swift integration |
| ✅ [ONNX Runtime](https://onnxruntime.ai) | C++/Python | INT4, INT8, FP16 | 70B | Cross-platform | Cross-platform inference<br>Multi-hardware backend<br>Production-grade |
| ✅ [WebLLM](https://github.com/mlc-ai/web-llm) | TypeScript | Q4, Q8 | 7B | Browser | In-browser inference<br>WebGPU acceleration<br>Serverless |
| ✅ [MNN](https://github.com/alibaba/MNN) | C++ | INT4, INT8, FP16 | 7B | Android, iOS, Embedded | Developed by Alibaba<br>Mobile optimization<br>Extremely lightweight |

### 🚪 Gateway

| Engine | Language | Quantization | Max Model | Deployment | Core Highlights |
| ------ | ------ | ------ | ---------- | ---------- | ---------- |
| ✅ [llama.cpp](https://github.com/ggerganov/llama.cpp) | C++ | GGUF, Q4_K_M, Q5_K_M | 70B | Cross-platform | C++ implementation, zero dependencies<br>GGUF quantization format<br>CPU/GPU hybrid inference |

<!-- AUTOGEN_END -->

---

## ⚡ Quantization: Spend 5 Minutes to Save 50% VRAM

The core trade-off of quantization: **sacrifice a little bit of quality for massive VRAM savings**.

| Format | Precision | Size Reduction | Speed | Quality Loss | How to Use |
| ------ | ------ | --------- | ------ | --------- | -------- |
| **FP8** | 8-bit | 2× | ⭐⭐⭐⭐⭐ | Very Low | Supported natively by [vLLM](https://github.com/vllm-project/vllm) |
| **AWQ** | 4-bit | 4× | ⭐⭐⭐⭐⭐ | Low | [vLLM](https://github.com/vllm-project/vllm) / AutoGPTQ |
| **GPTQ** | 4-bit | 4× | ⭐⭐⭐⭐ | Low | Best compatibility |
| **GGUF** | 2-8 bit | 2-8× | ⭐⭐⭐⭐ | Variable | Use directly with [Ollama](https://ollama.com) / [llama.cpp](https://github.com/ggerganov/llama.cpp) |
| **EXL2** | 2-6 bit | 2-6× | ⭐⭐⭐⭐⭐ | Highest at same size | [ExLlamaV2](https://github.com/turboderp/exllamav2), for advanced users |

> [!TIP]
> **Don't know which quantization to choose?**
> - Using Ollama → GGUF (`ollama run` auto-downloads GGUF)
> - Using vLLM → AWQ or FP8 (Highest throughput)
> - Using ExLlamaV2 → EXL2 (Fit larger models into the same VRAM)

**How much does quantization impact quality?** Take Qwen3-32B as an example:

| Quantization | Model Size | MMLU | Code Generation | Math Reasoning |
| ------ | --------- | ------ | --------- | --------- |
| FP16 (Original) | 64GB | 78.5 | 82.3 | 71.2 |
| AWQ-4bit | 16GB | 77.8 (-0.7) | 81.5 (-0.8) | 69.8 (-1.4) |
| GGUF-Q4 | 18GB | 77.2 (-1.3) | 80.9 (-1.4) | 68.5 (-2.7) |

> [!TIP]
> **Quality loss from 4-bit quantization is usually < 2%**, but it saves 4x the VRAM. Unless you are building a precision-sensitive production system, 4-bit is completely sufficient.

## 🔥 2026 Frontier: KV-Cache and MoE Deployment

**KV-Cache Optimization**: When running long contexts (32K+), KV-Cache consumes more VRAM than the model itself.

| Engine | KV-Cache Strategy | Effect |
| ------ | -------------- | ------ |
| [**vLLM**](https://github.com/vllm-project/vllm) | PagedAttention | Reduces VRAM usage by 40-60% |
| [**SGLang**](https://github.com/sgl-project/sglang) | RadixAttention | Reuses prefix cache for multi-turn dialogues, best effect |
| [**llama.cpp**](https://github.com/ggerganov/llama.cpp) | Quantized KV-Cache | Quantizes KV as well, further saving VRAM |

**MoE Model Deployment**: Mixture-of-Experts (MoE) models (like DeepSeek-V4-685B) have a massive total parameter count, but only activate a subset of Experts per inference step.

| GPU Setup | Capable MoE Models | Strategy |
| --------- | ---------------- | ------ |
| 4×A100 (80GB) | DeepSeek-V4-685B | Expert Parallelism |
| 2×A100 | Mixtral-8x22B | Expert Caching + Preloading |
| Single RTX 4090 | [Phi-4](https://azure.microsoft.com/en-us/products/phi)-MoE (7B active) | Direct execution |

---

> **Update Frequency**: Updated quarterly
> **Automation**: Run `python scripts/build_docs.py` to re-render tables from YAML.
