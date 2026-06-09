import os
import re
from pathlib import Path

def extract_links(content):
    # Find all [Text](URL) in the content
    return re.findall(r'\[([^\]]+)\]\((https?://[^)]+)\)', content)

def extract_bold_terms(content):
    # Find all **Term** in the tables (lines starting with |)
    terms = set()
    lines = content.split('\n')
    in_table = False
    for line in lines:
        if line.strip().startswith('|'):
            in_table = True
            # Extract bold terms like **Claude Opus 4**
            founds = re.findall(r'\*\*([^*]+)\*\*', line)
            for f in founds:
                terms.add(f.strip())
        else:
            in_table = False
    return terms

def main():
    root_dir = Path("D:/HelloWorld/Git_Project/ai-landscape")
    md_files = list(root_dir.rglob("*.md"))
    
    global_links = {}
    for f in md_files:
        if "website" in str(f): continue
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            links = extract_links(content)
            for text, url in links:
                # Clean up text if it contains bold or br
                clean_text = re.sub(r'<[^>]+>', '', text).replace('*', '').strip()
                # If there's a split like GPT-5.5 Pro / Thinking, just take the first part or both
                parts = [p.strip() for p in clean_text.split('/')]
                for p in parts:
                    if p: global_links[p] = url
                global_links[clean_text] = url

    all_terms = set()
    for f in md_files:
        if "website" in str(f) or "en.md" in str(f): continue
        with open(f, 'r', encoding='utf-8') as file:
            all_terms.update(extract_bold_terms(file.read()))

    print(f"Total global links found: {len(global_links)}")
    print(f"Total bold terms in tables: {len(all_terms)}")
    
    missing = []
    for term in all_terms:
        # try to find match
        found = False
        for k in global_links.keys():
            if term.lower() in k.lower() or k.lower() in term.lower():
                found = True
                break
        if not found:
            missing.append(term)
            
    print(f"Terms potentially missing URLs: {len(missing)}")
    print(missing[:10])

if __name__ == "__main__":
    main()
