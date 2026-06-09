#!/usr/bin/env python3
"""
build_docs.py — Auto-generate markdown tables from YAML data.

Reads YAML from data/, groups by category/sub_category, inserts tables
between <!-- AUTOGEN_START --> and <!-- AUTOGEN_END --> markers.

Supports per-model-type column rendering:
- LLM: model name + badges, context/output, price, highlights
- Embedding/Reranker: dimensions, max tokens, MTEB score
- Image: resolution, API, styles
- Video: duration, resolution, fps
- Audio: languages, sample rate, realtime

Usage: python scripts/build_docs.py
"""

import sys
import re
import yaml
from pathlib import Path
from collections import defaultdict, OrderedDict

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"

DIR_MAP = {
    "foundation-models": "01-foundation-models",
    "infrastructure": "02-infrastructure",
    "data-and-knowledge": "03-data-and-knowledge",
    "dev-frameworks": "04-dev-frameworks",
    "lowcode-platforms": "05-lowcode-platforms",
    "tools-and-protocols": "06-tools-and-protocols",
    "skills-and-plugins": "07-skills-and-plugins",
    "observability": "08-observability",
    "safety-and-compliance": "09-safety-and-compliance",
    "applications": "10-applications",
}

# Sub-category display names
SUB_CAT_NAMES = OrderedDict([
    ("overseas", "🌍 海外模型"),
    ("domestic", "🇨🇳 国内模型"),
    ("reasoning", "🧠 推理模型"),
    ("opensource", "📖 开源可部署"),
    ("image", "🎨 图像生成"),
    ("video", "🎬 视频生成"),
    ("audio", "🎵 音频/语音"),
    ("multimodal-understanding", "👁️ 多模态理解"),
    ("embedding", "📐 Embedding 模型"),
    ("reranker", "🔄 Reranker 模型"),
    # Infrastructure
    ("cloud", "☁️ 云端推理"),
    ("local", "💻 本地推理"),
    ("edge", "📱 端侧推理"),
    ("distributed", "🏗️ 分布式"),
    ("embedded", "📦 嵌入式"),
    ("cloud-native", "☁️ 云原生"),
    ("extension", "🔌 扩展"),
    ("library", "📚 库"),
    ("proxy", "🔀 代理"),
    ("management", "📋 管理"),
    ("aggregator", "🔗 聚合"),
    ("gateway", "🚪 网关"),
    ("serverless", "☁️ Serverless 推理"),
    ("rental", "💳 GPU 租赁"),
    # Data & Knowledge
    ("parsing", "📄 文档解析"),
    ("rag", "🔍 RAG 知识库"),
    ("knowledge-graph", "🕸️ 知识图谱"),
    ("synthetic-data", "🧪 合成数据"),
    # Skills & Plugins
    ("agent-skills", "🤖 Agent 技能库"),
    ("framework-tools", "📦 框架工具"),
    ("platform-plugins", "🏪 平台插件"),
    ("design", "🎨 设计"),
    ("frontend", "🌐 前端"),
    ("coding", "💻 编码"),
    ("research", "📚 研究"),
    ("writing", "✍️ 写作"),
    ("marketing", "📢 营销"),
    ("product", "📊 产品"),
    ("security", "🔒 安全"),
    ("documentation", "📝 文档"),
    ("comprehensive", "📦 综合"),
    # Observability
    ("tracing", "📊 追踪"),
    ("cost", "💰 成本监控"),
    ("benchmark", "📈 评测基准"),
    # Safety & Compliance
    ("guardrails", "🛡️ 护栏"),
    ("moderation", "🔍 内容审核"),
    ("red-teaming", "🔴 红队测试"),
    ("evaluation", "📊 安全评估"),
    # Tools & Protocols
    ("protocol", "📡 协议"),
    ("built-in", "🔧 内置工具"),
    ("browser", "🌐 浏览器"),
    ("computer-use", "🖥️ 计算机使用"),
    ("mcp-server", "🔌 MCP 服务器"),
    ("mcp-client", "📱 MCP 客户端"),
    ("mcp-marketplace", "🏪 MCP 市场"),
    ("integration", "🔗 工具集成"),
    # Applications
    ("agent", "🤖 Agent 工具"),
    ("productivity", "📋 办公与创作"),
    ("search", "🔍 搜索与研究"),
])


def category_to_path(category: str) -> Path:
    parts = category.split("/")
    prefix = parts[0]
    rest = "/".join(parts[1:]) if len(parts) > 1 else prefix
    return PROJECT_ROOT / DIR_MAP.get(prefix, prefix) / f"{rest}.md"


def is_open_source(entry: dict) -> bool:
    t = str(entry.get("type", "")).lower()
    if t == "open":
        return True
    if t in ("closed", "protocol"):
        return False
    return bool(str(entry.get("license", "")).lower() not in ("proprietary", "closed", ""))


def fmt(val) -> str:
    if val is None:
        return ""
    if isinstance(val, list):
        return ", ".join(str(v) for v in val)
    if isinstance(val, dict):
        return ", ".join(f"{k}: {v}" for k, v in val.items())
    return str(val)


def make_badges(tags: list) -> str:
    """Convert tags to badge-style display: `tag1` `tag2`"""
    if not tags:
        return ""
    return " ".join(f"`{t}`" for t in tags[:3])


def get_model_type(category: str, sub_category: str = "") -> str:
    """Determine model type from category/sub_category for column rendering."""
    cat = category.lower()
    sub = sub_category.lower()
    # Only match foundation-models for LLM/embedding/multimodal
    if cat.startswith("foundation-models/"):
        if "llm" in cat:
            return "llm"
        elif "embedding" in cat or "reranker" in cat:
            return "embedding"
        elif sub in ("image", "video", "audio"):
            return sub
        elif "multimodal" in cat:
            return "generic"
    # Infrastructure types
    if "inference" in cat:
        return "inference"
    elif "vector-db" in cat:
        return "vector-db"
    elif "api-gateway" in cat:
        return "api-gateway"
    # Everything else is generic
    return "generic"


def make_llm_table(entries: list) -> str:
    """LLM table: 模型与版本 | 核心参数 (上下文/输出) | 价格 (入/出) | 核心亮点 | 部署方式"""
    if not entries:
        return ""
    rows = [
        "| 模型与版本 | 核心参数 (上下文/输出) | 价格 (入/出) | 核心亮点 | 部署方式 |",
        "|------------|------------------------|--------------|----------|----------|",
    ]
    for e in entries:
        name = e.get("name", "")
        api_name = e.get("api_model_name", "")
        if api_name:
            name = f"{name}<br>*(API: `{api_name}`)*"
            
        url = e.get("url", "")
        # Add region badge
        sub = e.get("sub_category", "")
        region = "🌏" if sub == "overseas" else "🏯" if sub == "domestic" else ""
        name_cell = f"{region} [{name}]({url})" if url else f"{region} {name}"
        
        ctx = e.get("context_window", "-")
        out = e.get("output_limit", "-")
        ctx_cell = f"**In**: {ctx}<br>**Out**: {out}" if out != "-" else f"**In**: {ctx}"
        
        price = str(e.get("price", "-"))
        
        hl = e.get("highlights", [])
        hl_cell = "<br>".join(str(h) for h in hl[:3]).replace("|", "\\|") if hl else "—"
        
        # 部署方式 (type/license)
        t = str(e.get("type", "")).lower()
        if t == "open" or is_open_source(e):
            lic = e.get("license", "Open")
            deploy = f"✅ 开源可部署<br>`{lic}`"
        else:
            deploy = "☁️ 商业 API / 闭源"
            
        rows.append(f"| {name_cell} | {ctx_cell} | {price} | {hl_cell} | {deploy} |")
    return "\n".join(rows)


def make_embedding_table(entries: list) -> str:
    """Embedding/Reranker table: 模型与版本 | 维度 | 最大Token | MTEB 评分 | 核心亮点"""
    if not entries:
        return ""
    rows = [
        "| 模型与版本 | 维度 | 最大Token | MTEB 评分 | 核心亮点 |",
        "|------------|------|----------|-----------|----------|",
    ]
    for e in entries:
        name = e.get("name", "")
        api_name = e.get("api_model_name", "")
        if api_name:
            name = f"{name}<br>*(API: `{api_name}`)*"
            
        url = e.get("url", "")
        name_cell = f"[{name}]({url})" if url else f"{name}"
        
        props = e.get("properties", {})
        dim = props.get("dimensions", "-")
        max_tok = props.get("max_tokens", "-")
        mteb = props.get("mteb_score", "-")
        
        hl = e.get("highlights", [])
        hl_cell = "<br>".join(str(h) for h in hl[:3]).replace("|", "\\|") if hl else "—"
        
        rows.append(f"| {name_cell} | {dim} | {max_tok} | {mteb} | {hl_cell} |")
    return "\n".join(rows)


def make_image_table(entries: list) -> str:
    """Image table: 模型名称 | 简介 | 分辨率 | API | 风格 | 核心亮点"""
    if not entries:
        return ""
    rows = [
        "| 模型名称 | 简介 | 分辨率 | API | 风格 | 核心亮点 |",
        "|----------|------|--------|-----|------|----------|",
    ]
    for e in entries:
        name = e.get("name", "")
        url = e.get("url", "")
        icon = "✅" if is_open_source(e) else ""
        name_cell = f"{icon} [{name}]({url})" if url else f"{icon} {name}"
        desc = e.get("description", "").replace("|", "\\|")
        badges = make_badges(e.get("tags", []))
        if badges:
            desc = f"{desc}<br>{badges}"
        props = e.get("properties", {})
        res = props.get("max_resolution", "-")
        api = "✅" if props.get("api_available") else "❌"
        styles = ", ".join(props.get("styles", [])) or "-"
        hl = e.get("highlights", [])
        hl_cell = "<br>".join(str(h) for h in hl[:3]).replace("|", "\\|") if hl else "—"
        rows.append(f"| {name_cell} | {desc} | {res} | {api} | {styles} | {hl_cell} |")
    return "\n".join(rows)


def make_video_table(entries: list) -> str:
    """Video table: 模型名称 | 简介 | 最大时长 | 分辨率 | 帧率 | 核心亮点"""
    if not entries:
        return ""
    rows = [
        "| 模型名称 | 简介 | 最大时长 | 分辨率 | 帧率 | 核心亮点 |",
        "|----------|------|----------|--------|------|----------|",
    ]
    for e in entries:
        name = e.get("name", "")
        url = e.get("url", "")
        icon = "✅" if is_open_source(e) else ""
        name_cell = f"{icon} [{name}]({url})" if url else f"{icon} {name}"
        desc = e.get("description", "").replace("|", "\\|")
        badges = make_badges(e.get("tags", []))
        if badges:
            desc = f"{desc}<br>{badges}"
        props = e.get("properties", {})
        dur = props.get("max_duration", "-")
        res = props.get("max_resolution", "-")
        fps = props.get("fps", "-")
        hl = e.get("highlights", [])
        hl_cell = "<br>".join(str(h) for h in hl[:3]).replace("|", "\\|") if hl else "—"
        rows.append(f"| {name_cell} | {desc} | {dur} | {res} | {fps} | {hl_cell} |")
    return "\n".join(rows)


def make_audio_table(entries: list) -> str:
    """Audio table: 模型名称 | 简介 | 语言 | 采样率 | 实时 | 核心亮点"""
    if not entries:
        return ""
    rows = [
        "| 模型名称 | 简介 | 语言 | 采样率 | 实时 | 核心亮点 |",
        "|----------|------|------|--------|------|----------|",
    ]
    for e in entries:
        name = e.get("name", "")
        url = e.get("url", "")
        icon = "✅" if is_open_source(e) else ""
        name_cell = f"{icon} [{name}]({url})" if url else f"{icon} {name}"
        desc = e.get("description", "").replace("|", "\\|")
        badges = make_badges(e.get("tags", []))
        if badges:
            desc = f"{desc}<br>{badges}"
        props = e.get("properties", {})
        langs = ", ".join(props.get("languages", [])) or "-"
        sr = props.get("sample_rate", "-")
        rt = "✅" if props.get("realtime") else "❌"
        hl = e.get("highlights", [])
        hl_cell = "<br>".join(str(h) for h in hl[:3]).replace("|", "\\|") if hl else "—"
        rows.append(f"| {name_cell} | {desc} | {langs} | {sr} | {rt} | {hl_cell} |")
    return "\n".join(rows)


def make_generic_table(entries: list) -> str:
    """Generic table for non-model categories (frameworks, tools, apps)."""
    if not entries:
        return ""
    rows = ["| 名称 | 简介 | 标签 | 亮点 |", "|------|------|------|------|"]
    for e in entries:
        name = e.get("name", "")
        url = e.get("url", "")
        name_cell = f"[{name}]({url})" if url else name
        desc = fmt(e.get("description", "")).replace("|", "\\|")
        tags = fmt(e.get("tags", [])).replace("|", "\\|")
        hl = fmt(e.get("highlights", [])).replace("|", "\\|")
        if isinstance(e.get("highlights"), list):
            hl = "<br>".join(str(h) for h in e["highlights"]).replace("|", "\\|")
        rows.append(f"| {name_cell} | {desc} | {tags} | {hl} |")
    return "\n".join(rows)




def make_inference_table(entries: list) -> str:
    """Inference engine table: 引擎 | 语言 | 量化 | 最大模型 | 部署方式 | 核心亮点"""
    if not entries:
        return ""
    rows = [
        "| 引擎 | 语言 | 量化 | 最大模型 | 部署方式 | 核心亮点 |",
        "|------|------|------|----------|----------|----------|",
    ]
    for e in entries:
        name = e.get("name", "")
        url = e.get("url", "")
        icon = "✅" if is_open_source(e) else ""
        name_cell = f"{icon} [{name}]({url})" if url else f"{icon} {name}"
        props = e.get("properties", {})
        lang = props.get("language", "-")
        quant = ", ".join(props.get("quantization", [])) or "-"
        max_model = props.get("max_model", "-")
        deploy = ", ".join(props.get("deploy", [])) or "-"
        hl = e.get("highlights", [])
        hl_cell = "<br>".join(str(h) for h in hl[:3]).replace("|", "\\|") if hl else "—"
        rows.append(f"| {name_cell} | {lang} | {quant} | {max_model} | {deploy} | {hl_cell} |")
    return "\n".join(rows)


def make_vector_db_table(entries: list) -> str:
    """Vector DB table: 数据库 | 规模 | 索引类型 | 云服务 | 延迟 | 核心亮点"""
    if not entries:
        return ""
    rows = [
        "| 数据库 | 规模 | 索引类型 | 云服务 | 延迟 | 核心亮点 |",
        "|--------|------|----------|--------|------|----------|",
    ]
    for e in entries:
        name = e.get("name", "")
        url = e.get("url", "")
        icon = "✅" if is_open_source(e) else ""
        name_cell = f"{icon} [{name}]({url})" if url else f"{icon} {name}"
        props = e.get("properties", {})
        scale = props.get("scale", "-")
        index = ", ".join(props.get("index_types", [])) or "-"
        cloud = props.get("cloud", "-")
        latency = props.get("latency", "-")
        hl = e.get("highlights", [])
        hl_cell = "<br>".join(str(h) for h in hl[:3]).replace("|", "\\|") if hl else "—"
        rows.append(f"| {name_cell} | {scale} | {index} | {cloud} | {latency} | {hl_cell} |")
    return "\n".join(rows)


def make_api_gateway_table(entries: list) -> str:
    """API Gateway table: 工具 | Provider数 | 功能 | 核心亮点"""
    if not entries:
        return ""
    rows = [
        "| 工具 | Provider数 | 功能 | 核心亮点 |",
        "|------|-----------|------|----------|",
    ]
    for e in entries:
        name = e.get("name", "")
        url = e.get("url", "")
        icon = "✅" if is_open_source(e) else ""
        name_cell = f"{icon} [{name}]({url})" if url else f"{icon} {name}"
        props = e.get("properties", {})
        providers = props.get("providers", "-")
        features = ", ".join(props.get("features", [])) or "-"
        hl = e.get("highlights", [])
        hl_cell = "<br>".join(str(h) for h in hl[:3]).replace("|", "\\|") if hl else "—"
        rows.append(f"| {name_cell} | {providers} | {features} | {hl_cell} |")
    return "\n".join(rows)

# Map model type to table renderer
TABLE_RENDERERS = {
    "llm": make_llm_table,
    "embedding": make_embedding_table,
    "image": make_image_table,
    "video": make_video_table,
    "audio": make_audio_table,
    "inference": make_inference_table,
    "vector-db": make_vector_db_table,
    "api-gateway": make_api_gateway_table,
    "generic": make_generic_table,
}


def generate_content(entries: list, category: str = "") -> str:
    """Generate table content, grouping by sub_category if present.
    
    For LLM models, re-group by license type (closed API vs open source)
    instead of sub_category (overseas/domestic/opensource).
    
    For categories with many entries in a single sub_category (>10),
    add secondary grouping by stars level for better readability.
    
    When there's only one sub_category, skip the ### header to avoid
    redundancy with the manually written ## header in the md file.
    """
    model_type = get_model_type(category)
    renderer = TABLE_RENDERERS.get(model_type, make_generic_table)
    has_sub = any(e.get("sub_category") for e in entries)
    
    # For LLM: re-group by license type
    if model_type == "llm" and has_sub:
        return _generate_llm_grouped(entries, renderer)
    
    if not has_sub:
        return renderer(entries)
    
    groups = defaultdict(list)
    for e in entries:
        groups[e.get("sub_category", "other")].append(e)
    
    order = list(SUB_CAT_NAMES.keys())
    sorted_keys = sorted(groups.keys(), key=lambda k: order.index(k) if k in order else 99)
    
    # If only one sub_category, skip the ### header to avoid redundancy
    if len(sorted_keys) == 1:
        key = sorted_keys[0]
        sub_type = get_model_type(category, sub_category=key)
        sub_renderer = TABLE_RENDERERS.get(sub_type, make_generic_table)
        
        # Secondary grouping for large categories
        if len(groups[key]) > 10:
            return _generate_secondary_grouped(groups[key], sub_renderer, key)
        else:
            return sub_renderer(groups[key])
    
    sections = []
    for key in sorted_keys:
        header = SUB_CAT_NAMES.get(key, key.replace("-", " ").title())
        # Use sub_category to determine renderer
        sub_type = get_model_type(category, sub_category=key)
        sub_renderer = TABLE_RENDERERS.get(sub_type, make_generic_table)
        
        # Secondary grouping for large categories
        if len(groups[key]) > 10:
            sub_sections = _generate_secondary_grouped(groups[key], sub_renderer, key)
            sections.append(f"### {header}\n\n{sub_sections}")
        else:
            table = sub_renderer(groups[key])
            sections.append(f"### {header}\n\n{table}")
    
    return "\n\n".join(sections)


def _generate_secondary_grouped(entries: list, renderer, sub_category: str) -> str:
    """Add secondary grouping for categories with many entries.
    
    Grouping strategy based on sub_category:
    - agent: by type (🆓 开源 / ☁️ 商业) - many commercial products don't have GitHub stars
    - coding: by type (🆓 开源 / ☁️ 商业)
    - productivity: by region (🌏 海外 / 🇨🇳 国内)
    - search: by type (🔍 通用搜索 / 📚 学术搜索 / 🔌 API 服务)
    - platform-plugins: by stars level
    - comprehensive: by stars level
    - default: by stars level
    """
    # Determine grouping strategy
    if sub_category in ["agent", "coding"]:
        return _group_by_type(entries, renderer)
    elif sub_category == "productivity":
        return _group_by_region(entries, renderer)
    elif sub_category == "search":
        return _group_by_search_type(entries, renderer)
    elif sub_category in ["platform-plugins", "comprehensive"]:
        return _group_by_stars(entries, renderer)
    else:
        return _group_by_stars(entries, renderer)


def _group_by_stars(entries: list, renderer) -> str:
    """Group entries by stars level."""
    hot = []      # 50K+
    active = []   # 10K-50K
    emerging = [] # <10K
    
    for e in entries:
        stars = e.get("stars", 0) or 0
        if stars >= 50000:
            hot.append(e)
        elif stars >= 10000:
            active.append(e)
        else:
            emerging.append(e)
    
    sections = []
    if hot:
        sections.append(f"#### 🔥 热门项目 (50K+ Stars)\n\n{renderer(hot)}")
    if active:
        sections.append(f"#### ⭐ 活跃项目 (10K-50K Stars)\n\n{renderer(active)}")
    if emerging:
        sections.append(f"#### 🆕 新兴项目 (<10K Stars)\n\n{renderer(emerging)}")
    
    return "\n\n".join(sections)


def _group_by_type(entries: list, renderer) -> str:
    """Group entries by type (open vs closed)."""
    open_source = []
    commercial = []
    
    for e in entries:
        if is_open_source(e):
            open_source.append(e)
        else:
            commercial.append(e)
    
    sections = []
    if open_source:
        sections.append(f"#### 🆓 开源项目\n\n{renderer(open_source)}")
    if commercial:
        sections.append(f"#### ☁️ 商业产品\n\n{renderer(commercial)}")
    
    return "\n\n".join(sections)


def _group_by_region(entries: list, renderer) -> str:
    """Group entries by region (overseas vs domestic)."""
    overseas = []
    domestic = []
    
    for e in entries:
        url = e.get("url", "").lower()
        name = e.get("name", "").lower()
        # Heuristic: check for Chinese company names or domains
        is_domestic = any(k in url or k in name for k in [
            "baidu", "alibaba", "tencent", "bytedance", "xiaomi", "huawei",
            "zhipu", "moonshot", "deepseek", "minimax", "stepfun", "iflytek",
            "baichuan", "sensetime", "01.ai", "yiyan", "doubao", "feishu",
            "dingtalk", "wps", "chatglm", "kimi", "hailuo", "tongyi",
            "qwen", "wenxin", "xinghuo", "metaso", "nami", "tiangong"
        ])
        
        if is_domestic:
            domestic.append(e)
        else:
            overseas.append(e)
    
    sections = []
    if overseas:
        sections.append(f"#### 🌏 海外产品\n\n{renderer(overseas)}")
    if domestic:
        sections.append(f"#### 🇨🇳 国内产品\n\n{renderer(domestic)}")
    
    return "\n\n".join(sections)


def _group_by_search_type(entries: list, renderer) -> str:
    """Group search entries by type."""
    general = []      # 通用搜索
    academic = []     # 学术搜索
    api_service = []  # API 服务
    
    for e in entries:
        tags = e.get("tags", [])
        name = e.get("name", "").lower()
        
        if "api" in tags or "api" in name:
            api_service.append(e)
        elif "academic" in tags or "deep-research" in tags:
            academic.append(e)
        else:
            general.append(e)
    
    sections = []
    if general:
        sections.append(f"#### 🔍 通用搜索\n\n{renderer(general)}")
    if academic:
        sections.append(f"#### 📚 学术搜索\n\n{renderer(academic)}")
    if api_service:
        sections.append(f"#### 🔌 API 服务\n\n{renderer(api_service)}")
    
    return "\n\n".join(sections)


def _generate_llm_grouped(entries: list, renderer) -> str:
    """Re-group LLM models by region: overseas vs domestic.
    
    Within each group, open source models are marked with ✅.
    """
    overseas = [e for e in entries if e.get("sub_category") == "overseas"]
    domestic = [e for e in entries if e.get("sub_category") == "domestic"]
    opensrc = [e for e in entries if e.get("sub_category") == "opensource"]
    
    # Merge opensrc into overseas/domestic based on description/url
    for e in opensrc:
        url = e.get("url", "").lower()
        # Heuristic: Meta/Microsoft/Google/Mistral = overseas, others = domestic
        if any(k in url for k in ["meta.com", "microsoft", "google", "mistral", "huggingface"]):
            e["sub_category"] = "overseas"
            overseas.append(e)
        else:
            e["sub_category"] = "domestic"
            domestic.append(e)
    
    sections = []
    
    if overseas:
        table = renderer(overseas)
        sections.append(f"### 🌏 海外模型\n\n{table}")
    
    if domestic:
        table = renderer(domestic)
        sections.append(f"### 🏯 国内模型\n\n{table}")
    
    return "\n\n".join(sections)


def update_md(filepath: Path, new_content: str) -> bool:
    """Replace content between AUTOGEN markers. Returns True if changed."""
    if not filepath.exists():
        return False
    
    original = filepath.read_text(encoding="utf-8")
    start = "<!-- AUTOGEN_START -->"
    end = "<!-- AUTOGEN_END -->"
    
    block = f"{start}\n\n{new_content}\n\n{end}"
    
    if start in original and end in original:
        pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
        updated = pattern.sub(block, original)
    else:
        last_sep = original.rfind("\n---\n")
        if last_sep != -1:
            updated = original[:last_sep] + f"\n\n{block}\n\n---" + original[last_sep + 4:]
        else:
            updated = original + f"\n\n{block}\n"
    
    if updated != original:
        filepath.write_text(updated, encoding="utf-8")
        return True
    return False


def validate_entries(entries: list, yaml_file: str) -> list:
    """Validate YAML entries and return list of warning strings."""
    warnings = []

    # Load taxonomy for tag validation
    tax_path = DATA_DIR / "taxonomy.yaml"
    valid_tags = set()
    if tax_path.exists():
        tax_data = yaml.safe_load(tax_path.read_text(encoding="utf-8"))
        if isinstance(tax_data, dict):
            for cat, tags in tax_data.items():
                if isinstance(tags, list):
                    valid_tags.update(tags)

    required_fields = ["name", "description", "url", "category"]
    for i, entry in enumerate(entries):
        if not isinstance(entry, dict):
            warnings.append(f"  [{yaml_file}#{i}] Not a dict: {type(entry)}")
            continue

        # Check required fields
        for field in required_fields:
            if not entry.get(field):
                warnings.append(f"  [{yaml_file}#{i}] Missing required field: {field} (name={entry.get('name', '?')})")

        # Validate tags against taxonomy
        tags = entry.get("tags", [])
        for tag in tags:
            if valid_tags and tag not in valid_tags:
                warnings.append(f"  [{yaml_file}#{i}] Invalid tag '{tag}' not in taxonomy.yaml (name={entry.get('name', '?')})")

    return warnings


def main():
    print("=" * 60)
    print("  AI Landscape — build_docs.py")
    print("=" * 60)
    print()

    all_entries = []
    all_warnings = []
    for yf in sorted(DATA_DIR.glob("*.yaml")):
        if yf.name == "taxonomy.yaml":
            continue
        try:
            data = yaml.safe_load(yf.read_text(encoding="utf-8"))
            if isinstance(data, list):
                all_entries.extend(data)
                print(f"  [LOAD] {yf.name} — {len(data)} entries")
                # Validate
                warns = validate_entries(data, yf.name)
                all_warnings.extend(warns)
        except Exception as e:
            print(f"  [ERR]  {yf.name} — {e}")

    if all_warnings:
        print(f"\n  ⚠️  Validation warnings ({len(all_warnings)}):")
        for w in all_warnings:
            print(w)

    print(f"\n  Total: {len(all_entries)} entries\n")

    by_cat = defaultdict(list)
    for entry in all_entries:
        cat = entry.get("category", "unknown")
        by_cat[cat].append(entry)

    updated_count = 0
    for cat, entries in sorted(by_cat.items()):
        md_path = category_to_path(cat)
        content = generate_content(entries, category=cat)
        
        if update_md(md_path, content):
            rel = md_path.relative_to(PROJECT_ROOT)
            print(f"  [UPDATE] {rel} — {len(entries)} entries")
            updated_count += 1
        else:
            rel = md_path.relative_to(PROJECT_ROOT)
            if md_path.exists():
                print(f"  [OK]    {rel}")
            else:
                print(f"  [SKIP]  {rel} — not found")

    print(f"\n{'=' * 60}")
    print(f"  Done! Updated {updated_count} file(s).")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
