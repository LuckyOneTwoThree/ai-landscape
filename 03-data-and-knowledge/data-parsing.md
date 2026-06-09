# 文档解析

> 最后更新：2026-06-08
> 数据来源：`data/data-and-knowledge.yaml` 自动生成

---

## 📄 文档解析的坑

把 PDF 变成文本，听起来简单，实际上是 RAG 流程中**最容易翻车的环节**。

| 文档类型 | 难度 | 常见坑 | 推荐方案 |
|---------|------|--------|---------|
| **纯文本 PDF** | ⭐ | 几乎没有 | [PyMuPDF](https://github.com/pymupdf/PyMuPDF) 直接提取 |
| **扫描件 PDF** | ⭐⭐⭐ | OCR 识别错误、排版混乱 | [Marker](https://github.com/datalab-to/marker) / [Docling](https://github.com/DS4SD/docling) |
| **含表格的 PDF** | ⭐⭐⭐⭐ | 表格结构丢失、列错位 | [MinerU](https://github.com/opendatalab/MinerU) / [Docling](https://github.com/DS4SD/docling) |
| **多栏排版 PDF** | ⭐⭐⭐ | 阅读顺序错乱 | [Nougat](https://github.com/facebookresearch/nougat) / [Marker](https://github.com/datalab-to/marker) |
| **含图片的 PDF** | ⭐⭐⭐⭐ | 图片说明文字丢失 | 多模态模型直接理解 |
| **网页 / HTML** | ⭐⭐ | 噪声多（广告、导航） | [Crawl4AI](https://github.com/unclecode/crawl4ai) / [Jina Reader](https://jina.ai/reader) |

> [!TIP]
> **90% 的 PDF 解析问题可以用 MinerU 解决**
> MinerU 是目前国内开源社区最活跃的文档解析工具，对中文 PDF 支持极好，表格、公式、多栏都能处理。`pip install magic-pdf` 即可使用。

---

## 📋 文档解析引擎总览

<!-- AUTOGEN_START -->

#### ⭐ 活跃项目 (10K-50K Stars)

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [MinerU](https://github.com/opendatalab/MinerU) | 国内最活跃的开源文档解析工具，中文 PDF 支持极好 | document, data-analysis, chinese | 中文 PDF 解析首选<br>表格/公式/多栏支持<br>32K Stars |
| [Unstructured](https://github.com/Unstructured-IO/unstructured) | 最流行的文档解析库，支持 PDF/Word/HTML 等 20+ 格式，RAG 标配 | document, data-analysis, rag | 28K Stars<br>20+ 格式支持<br>RAG 标配 |
| [Firecrawl](https://github.com/mendableai/firecrawl) | 为 LLM 设计的网页爬取 API，输出干净 Markdown/结构化数据 | search, document, api-gateway | 28K Stars<br>输出干净 Markdown<br>API 优先 |
| [Crawl4AI](https://github.com/unclecode/crawl4ai) | 为 LLM 设计的网页抓取工具，输出 Markdown | search, document | 为 LLM 设计<br>网页转 Markdown<br>25K Stars |
| [Docling](https://github.com/DS4SD/docling) | IBM 出品的文档解析工具，支持多种格式 | document, data-analysis, enterprise | IBM 出品的结构化高保真解析器<br>完美还原复杂的语义层级与表格<br>内置 MCP Server，生态绝佳 |
| [Marker](https://github.com/datalab-to/marker) | AI 驱动的 PDF 解析工具，支持扫描件、表格、公式 | document, data-analysis | 极速深度学习模型流水线<br>完美适配科研文献与复杂公式转换<br>支持可选的大模型增强 (LLM-boost) |
| [GOT-OCR](https://github.com/Ucas-HaoranWei/GOT-OCR2.0) | 阶跃星辰出品的通用 OCR 模型，支持复杂文档/乐谱/数学公式 | data-analysis, chinese | 12K Stars<br>通用 OCR<br>公式+乐谱 |

#### 🆕 新兴项目 (<10K Stars)

| 名称 | 简介 | 标签 | 亮点 |
|------|------|------|------|
| [Nougat](https://github.com/facebookresearch/nougat) | Meta 出品的学术文档解析模型，擅长公式识别 | document, data-analysis, academic | Meta 出品<br>学术论文解析<br>公式识别 |
| [PyMuPDF](https://github.com/pymupdf/PyMuPDF) | 高性能 PDF 处理库，纯文本提取首选 | document, open-source, fast-inference | 高性能 PDF 库<br>纯文本提取<br>轻量级 |
| [LlamaParse](https://github.com/run-llama/llama_parse) | LlamaIndex 出品的文档解析 API，专为 RAG 优化 | document, api-gateway, rag | 专为 LLM 设计的高效闭源 API 解析服务<br>无需配置本地环境，开箱即用<br>原生无缝集成 LlamaIndex 生态 |
| [Jina Reader](https://jina.ai/reader) | 网页转 Markdown API，最简单的网页解析方案 | search, api-gateway, document | 网页转 Markdown API<br>最简单方案<br>无需部署 |

<!-- AUTOGEN_END -->

---

## 🔧 解析方案对比

| 方案 | 类型 | 表格 | 公式 | OCR | 中文 | 适合谁 |
|------|------|------|------|-----|------|--------|
| **PyMuPDF** | 库 | ❌ | ❌ | ❌ | ✅ | 纯文本 PDF，最轻量 |
| **Marker** | 工具 | ✅ | ✅ | ✅ | ✅ | 扫描件、多语言 |
| **MinerU** | 工具 | ✅ | ✅ | ✅ | ✅ | 中文 PDF 首选 |
| **Docling** | 工具 | ✅ | ✅ | ✅ | ✅ | IBM 出品，企业级 |
| **Nougat** | 模型 | ✅ | ✅ | ✅ | ❌ | 学术论文，公式密集 |
| **Crawl4AI** | 工具 | — | — | — | ✅ | 网页抓取，LLM 友好 |
| **Jina Reader** | API | — | — | — | ✅ | 网页转 Markdown，最简单 |

## 💡 最简文档解析流程

```python
# 方案 1：纯文本 PDF（最简单）
import pymupdf
doc = pymupdf.open("document.pdf")
text = "\n".join(page.get_text() for page in doc)

# 方案 2：复杂 PDF（表格、扫描件）
# pip install magic-pdf
from magic_pdf.data.data_reader_writer import FileBasedDataWriter
# 参考 MinerU 官方文档

# 方案 3：网页抓取
# pip install crawl4ai
from crawl4ai import AsyncWebCrawler
async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://example.com")
    print(result.markdown)  # 直接得到 Markdown
```

> [!TIP]
> **解析后的文本质量直接决定 RAG 效果**
> 如果解析出来的文本表格错位、公式丢失、阅读顺序混乱，后面再怎么优化 Embedding 和检索都没用。建议先人工检查 10 个文档的解析结果，确认质量后再批量处理。

---

> **更新频率**：每季度更新
> **自动化**：运行 `python scripts/build_docs.py` 从 YAML 重新渲染表格。
