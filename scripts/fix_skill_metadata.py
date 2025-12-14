#!/usr/bin/env python3
"""
Fix SKILL.md metadata by standardizing YAML frontmatter to required format.

This script:
1. Finds all skills/*/SKILL.md files
2. Extracts existing frontmatter
3. Standardizes to required format with metadata section
4. Preserves existing content
"""

import os
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple, Any


def find_skill_files(base_dir: Path) -> List[Path]:
    """Find all SKILL.md files in the skills directory."""
    skills_dir = Path(base_dir) / "skills"
    return list(skills_dir.glob("*/*/SKILL.md"))

def extract_frontmatter(content: str) -> Tuple[Optional[str], str]:
    """Extract YAML frontmatter from markdown content."""
    pattern: str = r'^---\n(.*?)\n---\n(.*)$'
    match: Optional[re.Match[str]] = re.match(pattern, content, re.DOTALL)
    if match:
        return match.group(1), match.group(2)
    return None, content

def parse_yaml_flexible(yaml_text: str) -> Dict[str, Any]:
    """
    Parse YAML flexibly, handling both flat and nested structures.
    Returns a normalized dictionary.
    """
    data: Dict[str, Any] = {
        'name': None,
        'description': None,
        'license': 'MIT',
        'metadata': {}
    }

    lines: List[str] = yaml_text.split('\n')
    current_key: Optional[str] = None
    in_list: bool = False
    current_list: List[str] = []

    for line in lines:
        stripped = line.strip()

        # Skip empty lines
        if not stripped:
            continue

        # Handle list items
        if stripped.startswith('- '):
            if current_key:
                current_list.append(stripped[2:])
            continue

        # Handle key-value pairs
        if ':' in line and not line.strip().startswith('#'):
            # Save previous list if any
            if current_key and current_list:
                if current_key.startswith('metadata.'):
                    data['metadata'][current_key.split('.', 1)[1]] = current_list
                else:
                    data['metadata'][current_key] = current_list
                current_list = []

            # Parse new key-value
            indent = len(line) - len(line.lstrip())
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()

            # Top-level keys
            if indent < 2:
                if key in ['name', 'description', 'license']:
                    data[key] = value
                elif key == 'metadata':
                    current_key = 'metadata'
                else:
                    # Other top-level keys go into metadata
                    if value:
                        data['metadata'][key] = value
                    else:
                        current_key = f'metadata.{key}'
            # Metadata sub-keys
            elif indent >= 2:
                if value:
                    data['metadata'][key] = value
                else:
                    current_key = key

    # Save final list if any
    if current_key and current_list:
        if current_key.startswith('metadata.'):
            data['metadata'][current_key.split('.', 1)[1]] = current_list
        else:
            data['metadata'][current_key] = current_list

    return data

def get_python_tools(skill_dir: Path) -> List[str]:
    """Get list of Python tools in scripts/ directory."""
    scripts_dir: Path = skill_dir / "scripts"
    if not scripts_dir.exists():
        return []

    py_files: List[str] = sorted([f.name for f in scripts_dir.glob("*.py")])
    return py_files


def get_domain_from_path(skill_path: Path) -> str:
    """Extract domain from skill path."""
    # Path format: skills/domain-team/skill-name/SKILL.md
    parts: Tuple[str, ...] = skill_path.parts
    domain_team: str = parts[-3]  # e.g., 'marketing-team'
    domain: str = domain_team.replace('-team', '')
    return domain


def get_category_from_domain(domain: str) -> str:
    """Map domain to category."""
    category_map: Dict[str, str] = {
        'marketing': 'Marketing',
        'product': 'Product Management',
        'engineering': 'Engineering',
        'delivery': 'Project Delivery'
    }
    return category_map.get(domain, domain.title())


def get_default_keywords(skill_name: str, domain: str, existing_keywords: Optional[List[str]] = None) -> List[str]:
    """Generate default keywords based on skill name and domain."""
    if existing_keywords:
        # Keep existing if they look reasonable
        if len(existing_keywords) >= 3:
            return existing_keywords[:10]  # Limit to 10

    keywords: List[str] = [domain]

    # Add skill-specific keywords based on name
    name_parts: List[str] = skill_name.replace('-', ' ').split()
    keywords.extend([part for part in name_parts if len(part) > 3])

    return keywords[:5]  # Limit to 5 keywords

def build_metadata_section(skill_path: Path, existing_data: Dict[str, Any]) -> Dict[str, Any]:
    """Build the standardized metadata section."""
    skill_dir: Path = skill_path.parent
    domain: str = get_domain_from_path(skill_path)
    category: str = get_category_from_domain(domain)
    skill_name: str = skill_dir.name
    python_tools: List[str] = get_python_tools(skill_dir)

    # Use existing metadata or defaults
    existing_meta: Dict[str, Any] = existing_data.get('metadata', {})

    # Handle keywords - could be list or string
    existing_keywords: Any = existing_meta.get('keywords', [])
    if isinstance(existing_keywords, str):
        existing_keywords = [k.strip() for k in existing_keywords.strip('[]').split(',')]

    keywords: List[str] = get_default_keywords(skill_name, domain, existing_keywords)

    # Handle tech-stack
    tech_stack: Any = existing_meta.get('tech-stack', ['Python 3.8+', 'Markdown'])
    if isinstance(tech_stack, str):
        tech_stack = [tech_stack]

    metadata: Dict[str, Any] = {
        'version': existing_meta.get('version', '1.0.0'),
        'author': existing_meta.get('author', 'Claude Skills Team'),
        'category': existing_meta.get('category', category),
        'domain': existing_meta.get('domain', domain),
        'updated': datetime.now().strftime('%Y-%m-%d'),
        'keywords': keywords,
        'tech-stack': tech_stack,
        'python-tools': python_tools
    }

    return metadata

def format_yaml_list(items: List[str], indent: int = 2) -> str:
    """Format a list for YAML output."""
    if not items:
        return ' []'

    spaces: str = ' ' * indent
    return '\n' + '\n'.join(f'{spaces}- {item}' for item in items)


def build_updated_frontmatter(existing_data: Dict[str, Any], metadata: Dict[str, Any]) -> str:
    """Build updated YAML frontmatter with standardized metadata section."""
    lines: List[str] = []
    lines.append('---')
    lines.append(f'name: {existing_data.get("name", "unknown")}')
    lines.append(f'description: {existing_data.get("description", "")}')
    lines.append(f'license: {existing_data.get("license", "MIT")}')
    lines.append('metadata:')
    lines.append(f'  version: {metadata["version"]}')
    lines.append(f'  author: {metadata["author"]}')
    lines.append(f'  category: {metadata["category"]}')
    lines.append(f'  domain: {metadata["domain"]}')
    lines.append(f'  updated: {metadata["updated"]}')
    lines.append(f'  keywords:{format_yaml_list(metadata["keywords"])}')
    lines.append(f'  tech-stack:{format_yaml_list(metadata["tech-stack"])}')
    lines.append(f'  python-tools:{format_yaml_list(metadata["python-tools"])}')
    lines.append('---')

    return '\n'.join(lines)

def update_skill_file(skill_path: Path, force: bool = False) -> bool:
    """Update a single SKILL.md file with metadata section."""
    print(f"\nProcessing: {skill_path.relative_to(skill_path.parents[3])}")

    # Read current content
    with open(skill_path, 'r', encoding='utf-8') as f:
        content: str = f.read()

    # Extract frontmatter
    frontmatter: Optional[str]
    body: str
    frontmatter, body = extract_frontmatter(content)

    if not frontmatter:
        print(f"  ⚠️  No frontmatter found, skipping")
        return False

    # Parse existing frontmatter
    existing_data: Dict[str, Any] = parse_yaml_flexible(frontmatter)

    # Check if already has python-tools field (standardized format)
    if not force and 'python-tools' in existing_data.get('metadata', {}):
        print(f"  ℹ️  Already standardized, skipping")
        return False

    # Build metadata section
    metadata: Dict[str, Any] = build_metadata_section(skill_path, existing_data)

    # Build updated frontmatter
    new_frontmatter: str = build_updated_frontmatter(existing_data, metadata)

    # Combine with body
    new_content: str = new_frontmatter + '\n\n' + body

    # Write updated content
    with open(skill_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    tools_count: int = len(metadata['python-tools'])
    print(f"  ✅ Updated ({tools_count} Python tools)")
    return True

def main() -> None:
    """Main execution."""
    # Get base directory (script is in scripts/, need parent)
    script_dir: Path = Path(__file__).parent
    base_dir: Path = script_dir.parent

    print("=" * 60)
    print("SKILL.md Metadata Fixer")
    print("=" * 60)
    print(f"\nBase directory: {base_dir}")
    print(f"Today's date: {datetime.now().strftime('%Y-%m-%d')}")

    # Find all SKILL.md files
    skill_files: List[Path] = find_skill_files(base_dir)
    print(f"\nFound {len(skill_files)} SKILL.md files")

    # Update each file
    updated_count: int = 0
    skipped_count: int = 0

    for skill_path in sorted(skill_files):
        if update_skill_file(skill_path):
            updated_count += 1
        else:
            skipped_count += 1

    # Summary
    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"Total files found: {len(skill_files)}")
    print(f"Files updated: {updated_count}")
    print(f"Files skipped: {skipped_count}")
    print("\n✅ Done!")

if __name__ == '__main__':
    main()
