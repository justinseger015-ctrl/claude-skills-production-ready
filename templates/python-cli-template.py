#!/usr/bin/env python3
"""
Module: template_script.py
Description: [Clear description of what this script does]

This template provides a standardized CLI interface following claude-skills standards.
See standards/cli-standards.md for full documentation.

Usage:
    python template_script.py input.txt
    python template_script.py input.txt --output json
    python template_script.py input.txt -o json --file results.json -v

Author: [Your Name]
Version: 1.0.0
Last Updated: 2025-11-05
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime


def process_content(content: str, **kwargs) -> Dict[str, Any]:
    """
    Main processing logic for the script.

    Args:
        content: Input content to process
        **kwargs: Additional configuration options

    Returns:
        Dictionary containing processing results

    Raises:
        ValueError: If content is invalid
    """
    # TODO: Implement your processing logic here

    # Example return structure
    results = {
        "status": "success",
        "data": {
            "summary": "Processed successfully",
            "details": []
        },
        "metadata": {
            "input_length": len(content),
            "processing_time_ms": 0
        }
    }

    return results


def format_text_output(results: Dict[str, Any], verbose: bool = False) -> str:
    """
    Format results as human-readable text.

    Args:
        results: Processing results dictionary
        verbose: Include detailed information if True

    Returns:
        Formatted text output
    """
    output = "=== Processing Results ===\n\n"

    output += f"Status: {results['status']}\n"
    output += f"Summary: {results['data']['summary']}\n"

    if verbose:
        output += "\n--- Metadata ---\n"
        for key, value in results['metadata'].items():
            output += f"{key}: {value}\n"

    return output


def format_json_output(results: Dict[str, Any]) -> str:
    """
    Format results as JSON with metadata.

    Args:
        results: Processing results dictionary

    Returns:
        JSON-formatted string
    """
    output = {
        "metadata": {
            "tool": Path(__file__).name,
            "version": "1.0.0",
            "timestamp": datetime.utcnow().isoformat() + "Z"
        },
        "results": results
    }

    return json.dumps(output, indent=2)


def format_csv_output(results: Dict[str, Any]) -> str:
    """
    Format results as CSV (if applicable).

    Args:
        results: Processing results dictionary

    Returns:
        CSV-formatted string
    """
    # TODO: Implement CSV formatting if needed
    # This is optional and depends on your data structure

    output = "column1,column2,column3\n"
    output += "value1,value2,value3\n"

    return output


def main():
    """
    Main entry point with standardized argument parsing.

    Parses command-line arguments, validates input, processes content,
    and writes output in the specified format.
    """
    parser = argparse.ArgumentParser(
        description='[Clear, concise description of tool purpose]',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s input.txt
  %(prog)s input.txt --output json
  %(prog)s input.txt -o json --file results.json
  %(prog)s input.txt -o text -v

For more information, see the skill documentation at:
documentation/skills/[your-skill]/SKILL.md
        """
    )

    # Positional arguments
    parser.add_argument(
        'input',
        help='Input file path or data source to process'
    )

    # Optional arguments with both short and long forms
    parser.add_argument(
        '--output', '-o',
        choices=['text', 'json', 'csv'],
        default='text',
        help='Output format: text (default), json, or csv'
    )

    parser.add_argument(
        '--file', '-f',
        help='Write output to file instead of stdout'
    )

    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output with detailed information'
    )

    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 1.0.0'
    )

    # Parse arguments
    args = parser.parse_args()

    try:
        # Validate input file
        input_path = Path(args.input)

        if not input_path.exists():
            print(f"Error: Input file not found: {args.input}", file=sys.stderr)
            sys.exit(1)

        if not input_path.is_file():
            print(f"Error: Path is not a file: {args.input}", file=sys.stderr)
            sys.exit(1)

        # Read input content
        if args.verbose:
            print(f"Reading input file: {args.input}", file=sys.stderr)

        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            print(f"Error: Unable to read file as text: {args.input}", file=sys.stderr)
            print("Hint: Ensure file is UTF-8 encoded text", file=sys.stderr)
            sys.exit(1)

        if args.verbose:
            print(f"Processing {len(content)} characters...", file=sys.stderr)

        # Process content
        results = process_content(content, verbose=args.verbose)

        # Format output based on requested format
        if args.output == 'json':
            output = format_json_output(results)
        elif args.output == 'csv':
            output = format_csv_output(results)
        else:  # text (default)
            output = format_text_output(results, verbose=args.verbose)

        # Write output to file or stdout
        if args.file:
            try:
                output_path = Path(args.file)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(output)

                if args.verbose:
                    print(f"Results written to: {args.file}", file=sys.stderr)
                else:
                    print(f"Output saved to: {args.file}")

            except PermissionError:
                print(f"Error: Permission denied writing to: {args.file}", file=sys.stderr)
                sys.exit(4)
            except Exception as e:
                print(f"Error writing output file: {e}", file=sys.stderr)
                sys.exit(4)
        else:
            # Print to stdout
            print(output)

        # Success
        sys.exit(0)

    except FileNotFoundError as e:
        print(f"Error: File not found: {e}", file=sys.stderr)
        sys.exit(1)

    except PermissionError as e:
        print(f"Error: Permission denied: {e}", file=sys.stderr)
        sys.exit(1)

    except ValueError as e:
        print(f"Error: Invalid input: {e}", file=sys.stderr)
        sys.exit(3)

    except KeyboardInterrupt:
        print("\nOperation cancelled by user", file=sys.stderr)
        sys.exit(130)

    except Exception as e:
        print(f"Error: Unexpected error occurred: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
