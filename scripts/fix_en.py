import re
from pathlib import Path

def clean_bolds(match):
    row = match.group(0)
    cols = row.split('|')
    if len(cols) > 2:
        col2 = cols[2]
        # remove broken link wrappers
        col2 = re.sub(r'\[\*\*([^[\]]*?)\[\*\*\]\([^)]+\)', r'**\1**', col2)
        col2 = re.sub(r'\[\*\*\]\([^)]+\)', '', col2)
        col2 = re.sub(r'\[(.*?)\]\(https?://\[.*?\]\([^)]+\)[^)]*\)', r'\1', col2)
        col2 = re.sub(r'\[(.*?)\]\(https?://[^)]+?\)', r'\1', col2)
        col2 = re.sub(r'\[\*\*(.*?)(?:\[\*\*|\*\*\]).*?\)', r'**\1**', col2)
        
        # Super aggressive cleanup
        col2 = re.sub(r'https?://[^\s\])]+', '', col2)
        col2 = col2.replace('[', '').replace(']', '').replace('(', '').replace(')', '')
        col2 = col2.replace('**', '')
        cols[2] = ' **' + col2.strip() + '** '
        
    return '|'.join(cols)

def fix_text(text):
    text = re.sub(r'\[\]\(https?://[^)]+\)', '', text)
    
    parts = text.split('<!-- AUTOGEN_START -->')
    
    # Clean the first part (manual table)
    parts[0] = re.sub(r'\|.*\|.*\|.*\|', clean_bolds, parts[0])
    
    return '<!-- AUTOGEN_START -->'.join(parts)

def main():
    root = Path('D:/HelloWorld/Git_Project/ai-landscape')
    count = 0
    for path in root.rglob('*.en.md'):
        if 'website' in str(path): continue
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()
            
        new_text = fix_text(text)
        
        if new_text != text:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_text)
            count += 1
            print(f"Fixed {path.relative_to(root)}")
            
    print(f"Fixed {count} files")

if __name__ == '__main__':
    main()
