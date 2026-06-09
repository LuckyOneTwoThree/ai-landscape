# Document Parsing

> Last Updated: 2026-06-08
> Data Source: Automatically generated from `data/data-and-knowledge.yaml`

---

## 📄 Pitfalls in Document Parsing

Converting PDF to text sounds simple, but it is actually the **most error-prone step** in the RAG pipeline.

| Document Type | Difficulty | Common Pitfalls | Recommended Solutions |
| --------- | ------ | -------- | --------- |
| **Text-only PDF** | ⭐ | Almost none | [PyMuPDF](https://github.com/pymupdf/PyMuPDF) direct extraction |
| **Scanned PDF** | ⭐⭐⭐ | OCR recognition errors, layout formatting mess | [Marker](https://github.com/datalab-to/marker) / [Docling](https://github.com/DS4SD/docling) |
| **PDF with Tables** | ⭐⭐⭐⭐ | Table structure loss, column misalignment | [MinerU](https://github.com/opendatalab/MinerU) / [Docling](https://github.com/DS4SD/docling) |
| **Multi-column Layout PDF** | ⭐⭐⭐ | Reading order disruption | [Nougat](https://github.com/facebookresearch/nougat) / [Marker](https://github.com/datalab-to/marker) |
| **PDF with Images** | ⭐⭐⭐⭐ | Missing image captions/descriptions | Direct understanding via multimodal models |
| **Webpage / HTML** | ⭐⭐ | High noise (ads, navigation) | [Crawl4AI](https://github.com/unclecode/crawl4ai) / [Jina Reader](https://jina.ai/reader) |

> [!TIP]
> **90% of PDF parsing issues can be solved with MinerU**
> MinerU is currently the most active open-source document parsing tool in the Chinese community, offering excellent support for Chinese PDFs, and can handle tables, formulas, and multi-column layouts. You can use it simply via `pip install magic-pdf`.

---

## 📋 Document Parsing Engines Overview

<!-- AUTOGEN_START -->

#### ⭐ Active Projects (10K-50K Stars)

| Name | Introduction | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [MinerU](https://github.com/opendatalab/MinerU) | The most active open-source document parsing tool in China, with excellent support for Chinese PDFs | document, data-analysis, chinese | Top choice for Chinese PDF parsing<br>Supports tables/formulas/multi-column<br>32K Stars |
| [Unstructured](https://github.com/Unstructured-IO/unstructured) | The most popular document parsing library, supporting 20+ formats like PDF/Word/HTML, a standard for RAG | document, data-analysis, rag | 28K Stars<br>20+ formats supported<br>RAG standard |
| [Firecrawl](https://github.com/mendableai/firecrawl) | Web scraping API designed for LLMs, outputting clean Markdown/structured data | search, document, api-gateway | 28K Stars<br>Outputs clean Markdown<br>API-first |
| [Crawl4AI](https://github.com/unclecode/crawl4ai) | Web scraping tool designed for LLMs, outputting Markdown | search, document | Designed for LLMs<br>Webpage to Markdown<br>25K Stars |
| [Docling](https://github.com/DS4SD/docling) | Document parsing tool from IBM, supporting multiple formats | document, data-analysis, enterprise | Structured high-fidelity parser from IBM<br>Perfectly restores complex semantic hierarchies and tables<br>Built-in MCP Server, excellent ecosystem |
| [Marker](https://github.com/datalab-to/marker) | AI-driven PDF parsing tool, supporting scanned documents, tables, and formulas | document, data-analysis | Extremely fast deep learning model pipeline<br>Perfectly adapts to scientific literature and complex formula conversion<br>Supports optional LLM-boost |
| [GOT-OCR](https://github.com/Ucas-HaoranWei/GOT-OCR2.0) | General OCR model from StepFun, supporting complex documents/sheet music/mathematical formulas | data-analysis, chinese | 12K Stars<br>General OCR<br>Formulas + Sheet music |

#### 🆕 Emerging Projects (<10K Stars)

| Name | Introduction | Tags | Highlights |
| ------ | ------ | ------ | ------ |
| [Nougat](https://github.com/facebookresearch/nougat) | Academic document parsing model from Meta, excelling in formula recognition | document, data-analysis, academic | From Meta<br>Academic paper parsing<br>Formula recognition |
| [PyMuPDF](https://github.com/pymupdf/PyMuPDF) | High-performance PDF processing library, the top choice for pure text extraction | document, open-source, fast-inference | High-performance PDF library<br>Pure text extraction<br>Lightweight |
| [LlamaParse](https://github.com/run-llama/llama_parse) | Document parsing API from LlamaIndex, optimized specifically for RAG | document, api-gateway, rag | Efficient closed-source API parsing service designed for LLMs<br>No local environment configuration needed, out-of-the-box<br>Native seamless integration with the LlamaIndex ecosystem |
| [Jina Reader](https://jina.ai/reader) | Webpage to Markdown API, the simplest webpage parsing solution | search, api-gateway, document | Webpage to Markdown API<br>Simplest solution<br>No deployment required |

<!-- AUTOGEN_END -->

---

## 🔧 Parsing Solutions Comparison

| Solution | Type | Tables | Formulas | OCR | Chinese | Best For |
| ------ | ------ | ------ | ------ | ----- | ------ | -------- |
| [**PyMuPDF**](https://github.com/pymupdf/PyMuPDF) | Library | ❌ | ❌ | ❌ | ✅ | Text-only PDFs, most lightweight |
| [**Marker**](https://github.com/datalab-to/marker) | Tool | ✅ | ✅ | ✅ | ✅ | Scanned documents, multi-language |
| [**MinerU**](https://github.com/opendatalab/MinerU) | Tool | ✅ | ✅ | ✅ | ✅ | Top choice for Chinese PDFs |
| [**Docling**](https://github.com/DS4SD/docling) | Tool | ✅ | ✅ | ✅ | ✅ | From IBM, enterprise-grade |
| [**Nougat**](https://github.com/facebookresearch/nougat) | Model | ✅ | ✅ | ✅ | ❌ | Academic papers, formula-dense |
| [**Crawl4AI**](https://github.com/unclecode/crawl4ai) | Tool | — | — | — | ✅ | Web scraping, LLM-friendly |
| [**Jina Reader**](https://jina.ai/reader) | API | — | — | — | ✅ | Webpage to Markdown, simplest |

## 💡 Minimal Document Parsing Workflow

```python
# Approach 1: Text-only PDF (Simplest)
import pymupdf
doc = pymupdf.open("document.pdf")
text = "\n".join(page.get_text() for page in doc)

# Approach 2: Complex PDF (Tables, Scanned documents)
# pip install magic-pdf
from magic_pdf.data.data_reader_writer import FileBasedDataWriter
# Refer to the official MinerU documentation

# Approach 3: Web Scraping
# pip install crawl4ai
from crawl4ai import AsyncWebCrawler
async with AsyncWebCrawler() as crawler:
    result = await crawler.arun("https://example.com")
    print(result.markdown)  # Directly obtain Markdown
```

> [!TIP]
> **The quality of parsed text directly determines RAG performance**
> If the parsed text has misaligned tables, missing formulas, or disordered reading sequences, no amount of subsequent optimization in Embedding and retrieval will help. It is recommended to manually inspect the parsing results of 10 documents before processing in bulk.

---

> **Update Frequency**: Quarterly updates
> **Automation**: Run `python scripts/build_docs.py` to re-render tables from YAML.
