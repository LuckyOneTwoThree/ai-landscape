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
    matches = re.findall(r'\[([^\]]+)\]\((https?://[^\)]+)\)', content)
    for text, url in matches:
        clean_text = re.sub(r'<[^>]+>', '', text).replace('*', '').strip()
        
        # Strip parentheses content like "(海螺视频)" or "(Max/Pro)"
        no_paren = re.sub(r'\s*\([^)]*\)', '', clean_text).strip()
        if no_paren:
            local_mapping[no_paren.lower()] = url
            
        parts = [p.strip() for p in clean_text.split('/')]
        for p in parts:
            if p:
                local_mapping[p.lower()] = url
        
        local_mapping[clean_text.lower()] = url
        
        if "jina-embeddings-v5-omni" in clean_text.lower():
            local_mapping["jina v5 omni"] = url
            local_mapping["jina reranker"] = url
        if "cohere-embed-v4" in clean_text.lower():
            local_mapping["cohere embed v4"] = url
            local_mapping["cohere rerank v3"] = url
            local_mapping["cohere rerank"] = url
        if "gte-qwen2" in clean_text.lower():
            local_mapping["gte-qwen2"] = url
        if "bge-m3" in clean_text.lower():
            local_mapping["bge-m3"] = url
        if "bge-reranker" in clean_text.lower():
            local_mapping["bge-reranker-v2"] = url
        if "codestral embed" in clean_text.lower():
            local_mapping["codestral embed"] = url
    return local_mapping

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    local_map = extract_local_links(content)
    for k, v in URL_MAPPING.items():
        local_map[k.lower()] = v

    lines = content.split('\n')
    modified = False
    new_lines = []
    
    in_table = False

    for line in lines:
        if line.strip().startswith('|'):
            if not in_table:
                in_table = True
            
            original_line = line
            
            # 1. Process bolded items **Text**
            bolds = re.findall(r'(?<!\[)\*\*(.*?)\*\*(?!\])', line)
            for b in set(bolds):
                term = b.strip()
                term_lower = term.lower()
                url = None
                
                if term_lower in local_map:
                    url = local_map[term_lower]
                else:
                    for k, v in local_map.items():
                        if k in term_lower and len(k) > 4:
                            url = v
                            break
                            
                if url:
                    line = line.replace(f"**{b}**", f"[**{term}**]({url})")

            # 2. Process non-bolded items. Instead of skipping the whole col if it has `[`, 
            # we just replace words if they are NOT inside `[` and `]`.
            cols = [c.strip() for c in line.split('|')]
            for i, col in enumerate(cols):
                if not col or '--' in col: continue
                
                existing_links = []
                def stash_link(match):
                    existing_links.append(match.group(0))
                    return f"__LINK_PLACEHOLDER_{len(existing_links)-1}__"
                    
                stashed_col = re.sub(r'\[.*?\]\(.*?\)', stash_link, col)
                
                col_changed = False
                for k, v in local_map.items():
                    if len(k) <= 2: continue
                    pattern = re.compile(r'(?<![A-Za-z0-9_])(' + re.escape(k) + r')(?![A-Za-z0-9_])', re.IGNORECASE)
                    if pattern.search(stashed_col):
                        stashed_col = pattern.sub(lambda m: f"[{m.group(1)}]({v})", stashed_col)
                        col_changed = True
                        
                if col_changed:
                    for idx, link in enumerate(existing_links):
                        stashed_col = stashed_col.replace(f"__LINK_PLACEHOLDER_{idx}__", link)
                    cols[i] = stashed_col

            new_joined_line = ' | '.join(cols).strip()
            if new_joined_line.startswith('|'):
                line = new_joined_line
            else:
                line = f"| {' | '.join(c for c in cols if c)} |"
                if original_line.startswith('|'):
                    line = '|' + line[1:]
                if original_line.endswith('|'):
                    line = line[:-1] + '|'

            if line != original_line:
                modified = True

        else:
            in_table = False
            
        new_lines.append(line)

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(new_lines))
        return True
    return False

def main():
    root_dir = Path("D:/HelloWorld/Git_Project/ai-landscape")
    md_files = list(root_dir.rglob("*.md"))
    
    modified_count = 0
    for f in md_files:
        if "website" in str(f) or "scripts" in str(f): continue
        if process_file(f):
            modified_count += 1
            print(f"Modified: {f.relative_to(root_dir)}")

    print(f"\nTotal files modified: {modified_count}")

if __name__ == "__main__":
    main()
