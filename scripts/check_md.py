import glob
import re

for f in glob.glob('**/*.md', recursive=True):
    if 'website' in f or 'scripts' in f or 'pm' in f: continue
    content = open(f, encoding='utf-8').read()
    
    lines = content.split('\n')
    in_table = False
    expected_cols = 0
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Check for weird link structures
        if re.search(r'\]\([^)]+\)\]\(', line):
            print(f'{f}:{i+1} Double linked: {line}')
        if '[[' in line:
            print(f'{f}:{i+1} Nested bracket: {line}')
            
        # Check table columns
        if line.startswith('|'):
            cols = len(re.findall(r'(?<!\\)\|', line))
            if not in_table:
                in_table = True
                expected_cols = cols
            else:
                if cols != expected_cols:
                    print(f'{f}:{i+1} Column mismatch (expected {expected_cols}, got {cols}): {line}')
        else:
            in_table = False
