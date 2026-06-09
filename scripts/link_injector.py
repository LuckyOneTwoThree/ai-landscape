import os
import re
from pathlib import Path

# Base global mappings just in case
URL_MAPPING = {
    "Claude Opus 4": "https://anthropic.com",
    "Claude Opus 4.8": "https://anthropic.com",
    "DeepSeek-V4-Pro": "https://deepseek.com",
    "MiMo-V2.5-Pro": "https://mimo.xiaomi.com",
    "Claude Sonnet 4": "https://anthropic.com",
    "Claude Sonnet 4.6": "https://anthropic.com",
    "Qwen3-Coder": "https://qwen.ai",
    "Mistral Large 3": "https://mistral.ai",
    "GPT-5.5 Instant": "https://openai.com",
    "GPT-5.5-mini": "https://openai.com",
    "GPT-5.5": "https://openai.com",
    "MiMo-V2.5": "https://mimo.xiaomi.com",
    "Qwen3-235B": "https://qwen.ai",
    "Qwen3-8B": "https://qwen.ai",
    "DeepSeek-V4-Flash": "https://deepseek.com",
    "Gemini 3.5 Flash": "https://gemini.google.com",
    "o3": "https://openai.com",
    "Phi-4": "https://azure.microsoft.com/en-us/products/phi",
    "DeepSeek-R1": "https://deepseek.com",
    "MiMo-7B-RL": "https://mimo.xiaomi.com",
    "Gemini 3.5 Pro": "https://gemini.google.com",
    "Gemini 3.1 Pro": "https://gemini.google.com",
    "Llama 4 Scout (10M)": "https://ai.meta.com/llama/",
    "Kimi K2-6": "https://platform.moonshot.cn",
    "GPT-5.5 Pro": "https://openai.com",
    "GLM-5.1": "https://open.bigmodel.cn",
    "混元 HY3": "https://cloud.tencent.com/product/hunyuan",
    "MiniMax M3": "https://minimaxi.com",
    "Ollama": "https://ollama.com",
    "LM Studio": "https://lmstudio.ai",
    "vLLM": "https://github.com/vllm-project/vllm",
    "Azure OpenAI": "https://azure.microsoft.com/en-us/products/ai-services/openai-service",
    "Unstructured": "https://unstructured.io/",
    "LlamaParse": "https://cloud.llamaindex.ai/parse",
    "Docling": "https://github.com/DS4SD/docling",
    "Composio": "https://composio.dev",
    "n8n": "https://n8n.io",
    "Make": "https://make.com",
    "AgentOps": "https://agentops.ai",
    "Claude Haiku 4": "https://anthropic.com",
    "Codex CLI": "https://openai.com",
    "Codex": "https://openai.com",
    "Midjourney": "https://midjourney.com",
    "DALL-E 3": "https://openai.com",
    "Stable Diffusion": "https://stability.ai",
    "Sora": "https://openai.com",
    "Runway Gen-3": "https://runwayml.com",
    "Pika": "https://pika.art",
    "ElevenLabs": "https://elevenlabs.io",
    "Bark": "https://github.com/suno-ai/bark",
    "Pandas": "https://pandas.pydata.org",
    "Polars": "https://pola.rs",
    "Dask": "https://dask.org",
    "Plotly": "https://plotly.com",
    "Streamlit": "https://streamlit.io",
    "Matplotlib": "https://matplotlib.org",
    "Scikit-learn": "https://scikit-learn.org",
    "XGBoost": "https://xgboost.ai",
    "LightGBM": "https://lightgbm.readthedocs.io",
    "PyTorch": "https://pytorch.org",
    "TensorFlow": "https://tensorflow.org",
    "JAX": "https://github.com/google/jax",
    "Mastra": "https://mastra.ai",
    "Next.js": "https://nextjs.org",
    "Vercel": "https://vercel.com",
    "FastAPI": "https://fastapi.tiangolo.com",
    "OpenAI Agents SDK": "https://platform.openai.com/docs/assistants/overview"
}

def extract_local_links(content):
    local_mapping = {}
    # Extract links from the AUTOGEN section
    matches = re.findall(r'\[([^\]]+)\]\((https?://[^\)]+)\)', content)
    for text, url in matches:
        clean_text = re.sub(r'<[^>]+>', '', text).replace('*', '').strip()
        
        # Strip parentheses content like "(海螺视频)" or "(Max/Pro)"
        no_paren = re.sub(r'\s*\([^)]*\)', '', clean_text).strip()
        if no_paren:
            local_mapping[no_paren] = url
            
        parts = [p.strip() for p in clean_text.split('/')]
        for p in parts:
            if p:
                local_mapping[p] = url
                
        local_mapping[clean_text] = url
        
    # Inject specific overrides
    overrides = {
        "jina-embeddings-v5-omni": ["jina v5 omni", "jina reranker"],
        "cohere-embed-v4": ["cohere embed v4", "cohere rerank v3", "cohere rerank"],
        "gte-qwen2": ["gte-qwen2"],
        "bge-m3": ["bge-m3"],
        "bge-reranker": ["bge-reranker-v2"],
        "codestral embed": ["codestral embed"]
    }
    
    for key, overrides_list in overrides.items():
        found_url = None
        for text, url in matches:
            if key.lower() in text.lower():
                found_url = url
                break
        if found_url:
            for override in overrides_list:
                local_mapping[override] = found_url
                
    return local_mapping

def replace_with_links(text, mapping):
    # We want to replace matching tool names in the text with links.
    # We should sort the mapping keys by length descending to match longest phrases first.
    sorted_keys = sorted(mapping.keys(), key=len, reverse=True)
    
    # We stash existing markdown links to avoid replacing inside them.
    stashed_links = []
    def stash(match):
        stashed_links.append(match.group(0))
        return f"__LINK_{len(stashed_links)-1}__"
    
    text = re.sub(r'\[.*?\]\(.*?\)', stash, text)
    
    for key in sorted_keys:
        if len(key) <= 2: continue
        url = mapping[key]
        
        # We replace the exact key (case insensitive), ensuring it's not part of another word.
        # Use regex boundary. Since names can have non-word chars, we use negative lookahead/lookbehind.
        escaped_key = re.escape(key)
        pattern = re.compile(r'(?<![A-Za-z0-9_])(' + escaped_key + r')(?![A-Za-z0-9_])', re.IGNORECASE)
        
        text = pattern.sub(lambda m: f"[{m.group(1)}]({url})", text)
        
    # Unstash links
    for i, link in enumerate(stashed_links):
        text = text.replace(f"__LINK_{i}__", link)
        
    return text

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into manual and autogen parts
    if '<!-- AUTOGEN_START -->' not in content:
        return False
        
    manual_part, autogen_part = content.split('<!-- AUTOGEN_START -->', 1)
    
    local_map = extract_local_links(autogen_part)
    for k, v in URL_MAPPING.items():
        local_map[k] = v
        
    # We only apply replacements to table rows in the manual part
    lines = manual_part.split('\n')
    new_lines = []
    modified = False
    
    in_table = False
    for line in lines:
        if line.strip().startswith('|'):
            if '---' in line:
                new_lines.append(line)
                continue
                
            original_line = line
            
            # Split columns and process them
            cols = line.split('|')
            for i in range(1, len(cols)-1): # Skip first and last empty elements due to |...| format
                col = cols[i]
                # Process the column text
                new_col = replace_with_links(col, local_map)
                cols[i] = new_col
                
            new_line = '|'.join(cols)
            if new_line != original_line:
                modified = True
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    if modified:
        new_content = '\n'.join(new_lines) + '<!-- AUTOGEN_START -->' + autogen_part
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    root_dir = Path("D:/HelloWorld/Git_Project/ai-landscape")
    # Process both .md and .en.md
    md_files = list(root_dir.rglob("*.md"))
    
    modified_count = 0
    for f in md_files:
        if "website" in str(f) or "scripts" in str(f) or "pm" in str(f): continue
        if process_file(f):
            modified_count += 1
            print(f"Modified: {f.relative_to(root_dir)}")

    print(f"\nTotal files modified: {modified_count}")

if __name__ == "__main__":
    main()
