#!/usr/bin/env python3
"""
Comprehensive Migration Script for 42 Engineering Scripts
Migrates all scripts to standardized argparse CLI patterns
"""

import os
import re
from pathlib import Path
from typing import Tuple, Dict, List

BASE_PATH = Path("/Users/ricky/Library/CloudStorage/GoogleDrive-rickydwilson@gmail.com/My Drive/Websites/GitHub/claude-skills/engineering-team")

SKILLS = [
    "code-reviewer",
    "senior-architect",
    "senior-backend",
    "senior-computer-vision",
    "senior-data-engineer",
    "senior-data-scientist",
    "senior-devops",
    "senior-frontend",
    "senior-fullstack",
    "senior-ml-engineer",
    "senior-prompt-engineer",
    "senior-qa",
    "senior-secops",
    "senior-security"
]

def extract_class_name(content: str) -> str:
    """Extract main class name from script"""
    match = re.search(r'class (\w+):', content)
    return match.group(1) if match else "Tool"

def migrate_script(script_path: Path) -> Tuple[bool, str]:
    """Migrate a single script to standardized pattern"""
    try:
        with open(script_path, 'r') as f:
            content = f.read()

        original_content = content

        # Get class name
        class_name = extract_class_name(content)

        # Create description
        description = f"{class_name} - Tool for automated processing"

        # Step 1: Update the main() function signature and parser creation
        # Replace the current main function structure with standardized one

        # Pattern to match the main() function completely
        main_pattern = r'def main\(\):.*?(?=\n\nif __name__)'
        main_match = re.search(main_pattern, content, re.DOTALL)

        if main_match:
            new_main = f'''def main():
    """Main entry point with standardized CLI interface"""
    parser = argparse.ArgumentParser(
        description="{description}",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s input_path
  %(prog)s input_path --output json
  %(prog)s input_path -o json --file results.json
  %(prog)s input_path -v

For more information, see the skill documentation.
        """
    )

    parser.add_argument(
        '--input', '-i',
        required=True,
        dest='target',
        help='Input file or target path to process'
    )

    parser.add_argument(
        '--output', '-o',
        choices=['text', 'json', 'csv'],
        default='text',
        help='Output format (default: text)'
    )

    parser.add_argument(
        '--config', '-c',
        help='Configuration file path'
    )

    parser.add_argument(
        '--file', '-f',
        help='Write output to file instead of stdout'
    )

    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )

    args = parser.parse_args()

    tool = {class_name}(
        args.target,
        verbose=args.verbose
    )

    results = tool.run()

    # Format output based on requested format
    if args.output == 'json':
        output = json.dumps(results, indent=2)
    else:
        # Default text output - use JSON for now
        output = json.dumps(results, indent=2)

    # Write output
    if args.file:
        with open(args.file, 'w') as f:
            f.write(output)
        print(f"Results written to {{args.file}}")
    else:
        print(output)'''

            content = re.sub(main_pattern, new_main, content, flags=re.DOTALL)

        # Write updated content
        if content != original_content:
            with open(script_path, 'w') as f:
                f.write(content)
            return True, f"Migrated: {script_path.name}"
        else:
            return False, f"No changes needed: {script_path.name}"

    except Exception as e:
        return False, f"Error migrating {script_path.name}: {str(e)}"

def main():
    """Migrate all 42 scripts"""
    results = {
        'total': 0,
        'migrated': 0,
        'skipped': 0,
        'errors': [],
        'files': []
    }

    for skill in SKILLS:
        skill_path = BASE_PATH / skill / "scripts"
        if skill_path.exists():
            scripts = sorted(skill_path.glob("*.py"))
            for script in scripts:
                results['total'] += 1
                success, message = migrate_script(script)

                if success and "Migrated" in message:
                    results['migrated'] += 1
                    results['files'].append(str(script))
                    print(f"✓ {message}")
                elif success:
                    results['skipped'] += 1
                    print(f"⊘ {message}")
                else:
                    results['errors'].append(message)
                    print(f"✗ {message}")

    print(f"\n{'='*70}")
    print(f"Migration Summary")
    print(f"{'='*70}")
    print(f"Total scripts processed: {results['total']}")
    print(f"Successfully migrated: {results['migrated']}")
    print(f"Skipped: {results['skipped']}")
    print(f"Errors: {len(results['errors'])}")

    if results['errors']:
        print(f"\nErrors encountered:")
        for error in results['errors']:
            print(f"  {error}")

    print(f"\nMigrated files:")
    for file_path in results['files']:
        print(f"  {file_path}")

if __name__ == '__main__':
    main()
