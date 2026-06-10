import os
import yaml
import time
import requests
import re

DATA_DIR = os.path.join(os.path.dirname(__file__), '../data')
GITHUB_API_URL = "https://api.github.com/repos/{owner}/{repo}"

# Add your GitHub token here via environment variable to avoid rate limits
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def get_github_stars(repo_url):
    # Extract owner and repo from url (e.g., https://github.com/langchain-ai/langchain)
    match = re.search(r"github\.com/([^/]+)/([^/]+)", repo_url)
    if not match:
        return None
    
    owner, repo = match.groups()
    repo = repo.replace(".git", "") # Cleanup
    
    headers = {"Accept": "application/vnd.github.v3+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
        
    url = GITHUB_API_URL.format(owner=owner, repo=repo)
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get('stargazers_count')
        elif response.status_code == 403 or response.status_code == 429:
            print(f"Rate limited on {repo_url}. Sleeping for 60s...")
            time.sleep(60)
            # Simple retry once
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                return response.json().get('stargazers_count')
        else:
            print(f"Failed to fetch {repo_url}: Status {response.status_code}")
    except Exception as e:
        print(f"Error fetching {repo_url}: {e}")
    
    return None

def process_yaml_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        
    if not isinstance(data, list):
        return False
        
    updated = False
    for item in data:
        if 'repo' in item and isinstance(item['repo'], str) and 'github.com' in item['repo']:
            repo_url = item['repo']
            new_stars = get_github_stars(repo_url)
            
            if new_stars is not None:
                old_stars = item.get('stars', 0)
                if new_stars != old_stars:
                    print(f"  [{item['name']}] Stars updated: {old_stars} -> {new_stars}")
                    item['stars'] = new_stars
                    updated = True
            
            # Sleep a bit to avoid triggering abuse mechanisms even with token
            time.sleep(0.5)
            
    if updated:
        # Write back
        # Using sort_keys=False to preserve order, and allow_unicode=True for Chinese chars
        with open(filepath, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
        return True
        
    return False

def main():
    if not os.path.exists(DATA_DIR):
        print(f"Data directory not found at {DATA_DIR}")
        return
        
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".yaml") and filename != "taxonomy.yaml":
            filepath = os.path.join(DATA_DIR, filename)
            process_yaml_file(filepath)
            
    print("Star update completed.")

if __name__ == "__main__":
    # Ensure pyyaml and requests are installed
    try:
        import yaml
        import requests
    except ImportError:
        print("Please install required packages: pip install pyyaml requests")
        exit(1)
        
    main()
