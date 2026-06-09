#!/usr/bin/env python3
"""
Parse a GitHub Issue (created via the Issue Form) and add the tool
to the appropriate YAML data file.

Usage:
    python scripts/issue_to_pr.py <issue_number>

Requires:
    - GITHUB_TOKEN environment variable
    - PyYAML (pip install pyyaml)
"""

import os
import re
import sys
import json
import urllib.request
import urllib.error

import yaml


# ---------------------------------------------------------------------------
# Category mapping: issue form dropdown value -> (yaml_file, default_category_path)
# ---------------------------------------------------------------------------
CATEGORY_MAP = {
    "01 - Foundation Models (LLM/Multimodal/Embedding)": "data/models.yaml",
    "02 - Infrastructure (Inference/API Gateway/Vector DB)": "data/infrastructure.yaml",
    "03 - Data & Knowledge (Parsing/Synthetic/Graph/RAG)": "data/data-and-knowledge.yaml",
    "04 - Dev Frameworks (LLM Framework/Multi-Agent)": "data/frameworks.yaml",
    "05 - Low-code Platforms (AI Builder/Workflow)": "data/lowcode.yaml",
    "06 - Tools & Protocols (MCP/Function Calling/Browser)": "data/tools.yaml",
    "07 - Skills & Plugins": "data/skills-and-plugins.yaml",
    "08 - Observability (Tracing/Cost/Benchmarks)": "data/observability.yaml",
    "09 - Safety & Compliance": "data/safety-and-compliance.yaml",
    "10 - Applications (Coding IDE/Search/Productivity)": "data/applications.yaml",
}

# Map category prefix to a YAML category path used inside entries
CATEGORY_PATH_MAP = {
    "01 - Foundation Models": "foundation-models/llm",
    "02 - Infrastructure": "infrastructure/inference",
    "03 - Data & Knowledge": "data-and-knowledge/rag",
    "04 - Dev Frameworks": "dev-frameworks/llm-framework",
    "05 - Low-code Platforms": "lowcode-platforms/ai-builder",
    "06 - Tools & Protocols": "tools-and-protocols/mcp",
    "07 - Skills & Plugins": "skills-and-plugins/agent-skills",
    "08 - Observability": "observability/tracing",
    "09 - Safety & Compliance": "safety-and-compliance/content-safety",
    "10 - Applications": "applications/coding-ide",
}

# Map the "Open Source?" dropdown value to a type string
TYPE_MAP = {
    "Yes (open source)": "open",
    "No (closed source)": "closed",
    "Partial (freemium/open core)": "partial",
}

GITHUB_API = "https://api.github.com"


def fetch_issue(owner: str, repo: str, issue_number: int, token: str) -> dict:
    """Fetch an issue from the GitHub API."""
    url = f"{GITHUB_API}/repos/{owner}/{repo}/issues/{issue_number}"
    req = urllib.request.Request(url, headers={
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "ai-landscape-bot",
    })
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())


def parse_issue_form(body: str) -> dict:
    """
    Parse a GitHub Issue Form body rendered as markdown.

    Issue Forms render as:
        ### Field Label
        Value
    """
    fields = {}

    # Split on '### ' headings
    sections = re.split(r"^### ", body, flags=re.MULTILINE)

    for section in sections:
        if not section.strip():
            continue
        lines = section.strip().split("\n", 1)
        heading = lines[0].strip()
        value = lines[1].strip() if len(lines) > 1 else ""

        # Map known headings to field ids
        heading_lower = heading.lower()
        if "tool name" in heading_lower:
            fields["name"] = value
        elif "official url" in heading_lower:
            fields["url"] = value
        elif "github repository" in heading_lower:
            fields["repo"] = value if value and value != "_No response_" else ""
        elif "one-line description" in heading_lower or "description" in heading_lower:
            fields["description"] = value
        elif "category" in heading_lower:
            fields["category"] = value
        elif "open source" in heading_lower:
            fields["type"] = value
        elif "license" in heading_lower:
            fields["license"] = value if value and value != "_No response_" else ""
        elif "key highlights" in heading_lower or "highlights" in heading_lower:
            # Parse bullet points
            highlights = []
            for line in value.split("\n"):
                line = line.strip()
                if line.startswith("- "):
                    highlights.append(line[2:].strip())
                elif line.startswith("* "):
                    highlights.append(line[2:].strip())
            fields["highlights"] = highlights
        elif "additional" in heading_lower:
            fields["additional"] = value if value and value != "_No response_" else ""

    return fields


def build_entry(fields: dict) -> dict:
    """Build a YAML entry dict from parsed form fields."""
    # Determine type from dropdown
    type_raw = fields.get("type", "No (closed source)")
    entry_type = TYPE_MAP.get(type_raw, "closed")

    # Determine category path
    category_raw = fields.get("category", "")
    category_path = "foundation-models/llm"  # default
    for prefix, path in CATEGORY_PATH_MAP.items():
        if category_raw.startswith(prefix):
            category_path = path
            break

    entry = {
        "name": fields.get("name", ""),
        "description": fields.get("description", ""),
        "url": fields.get("url", ""),
        "category": category_path,
        "type": entry_type,
        "status": "active",
        "tags": [],
    }

    # Optional fields
    repo = fields.get("repo", "")
    if repo:
        entry["repo"] = repo

    license_val = fields.get("license", "")
    if license_val:
        entry["license"] = license_val

    highlights = fields.get("highlights", [])
    if highlights:
        entry["highlights"] = highlights

    return entry


def get_target_file(category_raw: str) -> str:
    """Resolve the target YAML file from the issue form category dropdown."""
    for prefix, filepath in CATEGORY_MAP.items():
        if category_raw.startswith(prefix.split(" (")[0]):
            return filepath
    return "data/models.yaml"


def load_yaml(filepath: str) -> list:
    """Load existing entries from a YAML file."""
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data if isinstance(data, list) else []


def save_yaml(filepath: str, entries: list):
    """Write entries back to the YAML file."""
    with open(filepath, "w", encoding="utf-8") as f:
        yaml.dump(entries, f, allow_unicode=True, default_flow_style=False, sort_keys=False)


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/issue_to_pr.py <issue_number>", file=sys.stderr)
        sys.exit(1)

    issue_number = int(sys.argv[1])
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN environment variable is required", file=sys.stderr)
        sys.exit(1)

    # Infer owner/repo from environment or git remote
    github_repo = os.environ.get("GITHUB_REPOSITORY", "")
    if not github_repo:
        # Try to detect from git remote
        import subprocess
        try:
            remote = subprocess.check_output(
                ["git", "remote", "get-url", "origin"], text=True
            ).strip()
            # Handle SSH and HTTPS URLs
            m = re.search(r"github\.com[:/](.+?)(?:\.git)?$", remote)
            if m:
                github_repo = m.group(1)
        except Exception:
            pass

    if not github_repo:
        print("Error: Cannot determine repository. Set GITHUB_REPOSITORY env var.", file=sys.stderr)
        sys.exit(1)

    owner, repo = github_repo.split("/", 1)

    # Fetch the issue
    print(f"Fetching issue #{issue_number} from {owner}/{repo}...")
    issue_data = fetch_issue(owner, repo, issue_number, token)

    body = issue_data.get("body", "")
    if not body:
        print("Error: Issue body is empty", file=sys.stderr)
        sys.exit(1)

    # Parse form fields
    fields = parse_issue_form(body)
    print(f"Parsed fields: name={fields.get('name')!r}, category={fields.get('category')!r}")

    if not fields.get("name"):
        print("Error: Could not parse tool name from issue body", file=sys.stderr)
        sys.exit(1)

    # Determine target file
    category_raw = fields.get("category", "")
    target_file = get_target_file(category_raw)
    print(f"Target file: {target_file}")

    # Build new entry
    entry = build_entry(fields)

    # Load existing data, append, and save
    entries = load_yaml(target_file)

    # Check for duplicates
    for existing in entries:
        if existing.get("name", "").lower() == entry["name"].lower():
            print(f"Warning: '{entry['name']}' already exists in {target_file}, skipping.")
            sys.exit(0)

    entries.append(entry)
    save_yaml(target_file, entries)

    print(f"\n✅ Added '{entry['name']}' to {target_file}")
    print(f"   Category: {entry['category']}")
    print(f"   Type: {entry['type']}")
    print(f"   URL: {entry['url']}")
    if entry.get("highlights"):
        print(f"   Highlights: {entry['highlights']}")


if __name__ == "__main__":
    main()
