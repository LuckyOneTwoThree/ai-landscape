import re
from pathlib import Path

def strip_links(text):
    # Regex to find `[something](url)` and replace it with `something`
    # We must handle nested brackets carefully if they exist, but normally they don't if we just do inner-most first.
    # Actually, a simple iterative replacement works best for nested links.
    prev = None
    while text != prev:
        prev = text
        text = re.sub(r'\[([^\[\]]+?)\]\(https?://[^)]+\)', r'\1', text)
    return text

def main():
    root = Path("D:/HelloWorld/Git_Project/ai-landscape")
    count = 0
    for path in root.rglob("*.md"):
        if "website" in str(path) or "scripts" in str(path) or "pm" in str(path):
            continue
            
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if "<!-- AUTOGEN_START -->" not in content:
            continue
            
        manual_part, autogen_part = content.split("<!-- AUTOGEN_START -->", 1)
        
        # We only strip links from table rows in the manual part, to be extra safe
        # (in case there are valid links in paragraph text, though there aren't many)
        lines = manual_part.split('\n')
        new_lines = []
        modified = False
        
        for line in lines:
            if line.strip().startswith('|'):
                new_line = strip_links(line)
                if new_line != line:
                    modified = True
                new_lines.append(new_line)
            else:
                new_lines.append(line)
                
        if modified:
            new_content = '\n'.join(new_lines) + "<!-- AUTOGEN_START -->" + autogen_part
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f"Stripped links in: {path.relative_to(root)}")
            
    print(f"Total stripped: {count}")

if __name__ == '__main__':
    main()
