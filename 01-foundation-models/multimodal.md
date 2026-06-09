# 多模态模型

> 最后更新：2026-06-08
> 数据来源：`data/models.yaml` 自动生成

---

## 🎯 多模态生成引擎定位指南

多模态生成早已跨过"抽卡盲盒"阶段，2026 年的核心在于**可控性与生产管线集成**。

### 🎨 图像生成选型

| 核心需求 | 首选引擎 | 开源替代 | 关键差异 |
|---------|---------|---------|---------|
| **艺术美学与高保真摄影** | **Midjourney V8.1** | DALL-E 4 | 统治级的材质质感与构图美学，2K HD |
| **极致排版与文字渲染** | **DALL-E 4** | FLUX.2 | 文字渲染准确，Prompt 遵循度高 |
| **中文风格与国风** | **即梦 (Jimeng)** | — | 字节出品，抖音生态集成 |

### 🎬 视频生成选型

| 核心需求 | 首选引擎 | 开源替代 | 关键差异 |
|---------|---------|---------|---------|
| **长视频与一致性** | **Sora 2.0** | CogVideoX-3 | 60s 超长视频，物理规律模拟 |
| **运镜控制与电影感** | **可灵 (Kling) 3.5** | — | 无提示词物理轨迹，4K 60fps |
| **快速迭代与短视频** | **Hailuo 2** | — | MiniMax 出品，与 M3 生态集成 |

### 🎵 音频生成选型

| 核心需求 | 首选引擎 | 开源替代 | 关键差异 |
|---------|---------|---------|---------|
| **全曲目音乐生成** | **Suno v5.5** | — | 自定义 Voices 音色克隆，原生无损全曲 |
| **语音合成 (TTS)** | **GLM-TTS** | CosyVoice 2 | 自然度极高，中文优化 |
| **语音识别 (ASR)** | — | **Whisper V3** | 多语言，MIT 开源 |

> [!TIP]
> **多模态模型的 API 可用性**
> 不是所有模型都提供 API。Midjourney 仅通过 Discord/Web 使用，部分开源模型需要自部署。选型时务必确认你的使用方式是否匹配。

---

## 📋 多模态模型总览

<!-- 以下内容由脚本自动生成，请勿手动修改 -->
<!-- AUTOGEN_START -->

### 🎨 图像生成

| 模型名称 | 简介 | 分辨率 | API | 风格 | 核心亮点 |
|----------|------|--------|-----|------|----------|
|  [Midjourney V8.1](https://midjourney.com) | 2026年4月发布的最新旗舰，极速生成与原生 2K HD 支持<br>`image-generation` `content-creation` | 2048x2048 (HD Mode) | ✅ | 写实, 艺术, 动漫 | 原生支持 2K HD 生成<br>生成速度提升 4-5 倍<br>指令集与细节遵循大幅增强 |
|  [DALL-E 4](https://openai.com/dall-e) | OpenAI 图像生成模型，与 GPT-5.5 深度集成<br>`image-generation` `openai-compatible` | 1024x1024 | ✅ | 写实, 艺术 | GPT-5.5 原生集成<br>文本渲染准确<br>API 可用 |
|  [即梦 (Jimeng)](https://jimeng.jianying.com) | 字节跳动 AI 图像/视频创作平台<br>`image-generation` `video-generation` `chinese` | 1024x1024 | ✅ | 写实, 动漫, 国风 | 字节跳动出品<br>图像+视频创作<br>抖音生态集成 |
| ✅ [FLUX.2 (Max/Pro)](https://bfl.ai) | BFL 2026 最强开源图像底座，彻底颠覆照片级生成<br>`image-generation` `flagship` | 2048x2048 | ✅ | - | 最高 4 MP 原生输出<br>极强排版与多视角一致性<br>Max/Flex/Pro 多版本矩阵 |

### 🎬 视频生成

| 模型名称 | 简介 | 最大时长 | 分辨率 | 帧率 | 核心亮点 |
|----------|------|----------|--------|------|----------|
|  [Sora 2.0](https://openai.com/sora) | OpenAI 物理世界模拟器，已与 GPT-5.5 深度联动<br>`video-generation` `openai-compatible` | 60s | 1080p | 24 | 超长一致性视频<br>物理规律模拟<br>4K 输出 |
|  [可灵 (Kling) 3.5](https://kling.kuaishou.com) | 快手 2026 最新视频大模型，支持无提示词物理轨迹与 4K 60fps<br>`video-generation` `chinese` | 30s | 1080p | 24 | 无提示词物理轨迹推演<br>原生多语言音频融合<br>4K 60fps 电影级呈现 |
|  [Hailuo 2 (海螺视频)](https://hailuoai.video) | MiniMax 视频生成模型，高质量 AI 视频<br>`video-generation` `chinese` | 30s | 1080p | 24 | MiniMax 出品<br>高质量视频生成<br>与 M3 生态集成 |
| ✅ [CogVideoX-3](https://github.com/THUDM/CogVideo) | 智谱 AI 开源视频生成模型<br>`video-generation` `open-source` `chinese` | 15s | 720p | 24 | 开源视频生成<br>智谱 AI 出品<br>Apache 2.0 |
|  [Runway Gen-4](https://runwayml.com) | 好莱坞级别视频生成与工业管线标配<br>`video-generation` `enterprise` | 10s | 4K | - | Motion Brush 3.0<br>Aleph 高级视频编排<br>Director Mode 导演视角 |
|  [Luma Ray3](https://lumalabs.ai) | 物理真实感与 3D 空间理解最强视频模型<br>`video-generation` `content-creation` | 5s | 1080p | - | 物理引擎级连贯性<br>替代旧版 Dream Machine<br>极致光影折射与动态模糊 |
|  [Pika 2.0](https://pika.art) | 极速迭代与炫酷风格化的短视频利器<br>`video-generation` `content-creation` | 3s | - | - | 首创 Pikaffects 特效<br>支持背景与人物局部重绘<br>速度与社交媒体首选 |

### 🎵 音频/语音

| 模型名称 | 简介 | 语言 | 采样率 | 实时 | 核心亮点 |
|----------|------|------|--------|------|----------|
|  [Suno v5.5](https://suno.com) | 2026年行业霸主，支持 Voices 自定义音色训练<br>`voice-synthesis` `music-generation` | 英语, 中文, 日语 | 44.1kHz | ❌ | 自定义 Voices 音色克隆<br>音质大幅跃升<br>原生无损全曲生成 |
|  [Udio 2.0](https://udio.com) | 高质量 AI 音乐生成，与 Suno v5.5 并驾齐驱<br>`voice-synthesis` `music-generation` | 英语, 中文, 日语 | 44.1kHz | ❌ | 高质量音乐生成<br>2.0 音质飞跃<br>多风格支持 |
|  [MiniMax Music 2](https://minimaxi.com) | MiniMax AI 音乐生成模型<br>`voice-synthesis` `music-generation` `chinese` | 中文, 英语 | 44.1kHz | ❌ | MiniMax 出品<br>中文音乐优化 |
|  [GLM-TTS / CosyVoice 2](https://open.bigmodel.cn) | 前沿语音合成模型，自然度极高<br>`voice-synthesis` `chinese` | 中文, 英语, 日语 | 24kHz | ✅ | GLM-TTS 智谱出品<br>CosyVoice 2 阿里出品<br>自然度极高 |
| ✅ [Whisper V3](https://github.com/openai/whisper) | OpenAI 开源语音识别模型，多语言支持<br>`voice-synthesis` `voice-recognition` `open-source` | 多语言 | 16kHz | ❌ | 多语言语音识别<br>MIT 开源<br>准确率极高 |

<!-- AUTOGEN_END -->
<!-- 以上内容由脚本自动生成 -->

---

## 💡 工作流集成指南

| 工作流 | 推荐组合 | 说明 |
|--------|---------|------|
| **图文创作** | Midjourney V8.1 + GPT-5.5 | 图像生成 + 文案优化 |
| **短视频制作** | 可灵 3.5 + Suno v5.5 | 视频 + 配乐 |
| **播客/有声书** | GLM-TTS + Whisper V3 | 合成 + 校验 |
| **产品展示** | DALL-E 4 + Sora 2.0 | 产品图 + 展示视频 |
| **教育内容** | 即梦 + CosyVoice 2 | 中文图文 + 中文语音 |

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
