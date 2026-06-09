#!/usr/bin/env python3
"""
Validate YAML data files for AI Tech Stack Landscape.
"""

import yaml
import sys
import os
from pathlib import Path

# Required fields for each entry
REQUIRED_FIELDS = ['name', 'description', 'url', 'category', 'type', 'status', 'tags', 'highlights']

# Valid categories
VALID_CATEGORIES = [
    'foundation-models',
    'infrastructure',
    'data-and-knowledge',
    'dev-frameworks',
    'lowcode-platforms',
    'tools-and-protocols',
    'skills-and-plugins',
    'observability',
    'safety-and-compliance',
    'applications',
]

# Valid types
VALID_TYPES = ['open', 'closed', 'protocol']

# Valid statuses
VALID_STATUSES = ['active', 'beta', 'archived', 'deprecated', 'maintenance']

# Valid tags (from taxonomy.yaml)
VALID_TAGS = set()

def load_taxonomy(taxonomy_path):
    """Load valid tags from taxonomy.yaml."""
    with open(taxonomy_path, 'r', encoding='utf-8') as f:
        taxonomy = yaml.safe_load(f)
    
    for category, tags in taxonomy.items():
        if isinstance(tags, list):
            VALID_TAGS.update(tags)

def validate_entry(entry, filename, index):
    """Validate a single entry."""
    errors = []
    
    # Check required fields
    for field in REQUIRED_FIELDS:
        if not entry.get(field):
            errors.append(f"  Missing required field: {field}")
    
    # Check category (allow sub-categories like "tools-and-protocols/mcp")
    if entry.get('category'):
        main_category = entry['category'].split('/')[0]
        if main_category not in VALID_CATEGORIES:
            errors.append(f"  Invalid category: {entry['category']}")
    
    # Check type
    if entry.get('type') and entry['type'] not in VALID_TYPES:
        errors.append(f"  Invalid type: {entry['type']}")
    
    # Check status
    if entry.get('status') and entry['status'] not in VALID_STATUSES:
        errors.append(f"  Invalid status: {entry['status']}")
    
    # Check tags
    if entry.get('tags'):
        for tag in entry['tags']:
            if tag not in VALID_TAGS:
                errors.append(f"  Invalid tag: {tag}")
    
    # Check URL format
    if entry.get('url'):
        if not entry['url'].startswith(('http://', 'https://')):
            errors.append(f"  Invalid URL format: {entry['url']}")
    
    # Check open source entries have stars and license
    # Models (foundation-models) are exempt from stars requirement as they may not have GitHub repos
    if entry.get('type') == 'open':
        main_category = entry.get('category', '').split('/')[0]
        if main_category != 'foundation-models' and not entry.get('stars'):
            errors.append(f"  Open source entry missing stars")
        if not entry.get('license'):
            errors.append(f"  Open source entry missing license")
    
    return errors

def validate_file(filepath):
    """Validate a YAML file."""
    errors = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        if not isinstance(data, list):
            errors.append(f"File should contain a list of entries")
            return errors
        
        for i, entry in enumerate(data):
            entry_errors = validate_entry(entry, filepath.name, i)
            if entry_errors:
                errors.append(f"Entry {i+1} ({entry.get('name', 'unnamed')}):")
                errors.extend(entry_errors)
    
    except yaml.YAMLError as e:
        errors.append(f"YAML parsing error: {e}")
    except Exception as e:
        errors.append(f"Error reading file: {e}")
    
    return errors

def main():
    """Main validation function."""
    # Get project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    data_dir = project_root / 'data'
    taxonomy_path = data_dir / 'taxonomy.yaml'
    
    # Load taxonomy
    if taxonomy_path.exists():
        load_taxonomy(taxonomy_path)
        print(f"✅ Loaded {len(VALID_TAGS)} valid tags from taxonomy.yaml")
    else:
        print("⚠️  taxonomy.yaml not found, skipping tag validation")
    
    # Validate all YAML files
    total_errors = 0
    total_entries = 0
    
    for yaml_file in sorted(data_dir.glob('*.yaml')):
        if yaml_file.name == 'taxonomy.yaml':
            continue
        
        print(f"\n📄 Validating {yaml_file.name}...")
        
        with open(yaml_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        if isinstance(data, list):
            total_entries += len(data)
        
        errors = validate_file(yaml_file)
        
        if errors:
            total_errors += len(errors)
            print(f"  ❌ Found {len(errors)} errors:")
            for error in errors:
                print(f"    {error}")
        else:
            print(f"  ✅ All entries valid")
    
    # Summary
    print(f"\n{'='*60}")
    print(f"Validation Summary:")
    print(f"  Total entries: {total_entries}")
    print(f"  Total errors: {total_errors}")
    print(f"{'='*60}")
    
    if total_errors > 0:
        print(f"\n❌ Validation failed with {total_errors} errors")
        sys.exit(1)
    else:
        print(f"\n✅ All validations passed!")
        sys.exit(0)

if __name__ == '__main__':
    main()
