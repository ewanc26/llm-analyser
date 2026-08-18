"""CLI argument parsing for llm-analyser."""

import argparse
import os
import sys


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    if "--support" in sys.argv[1:]:
        print("Support llm-analyser development:")
        print("  Ko-fi: https://ko-fi.com/ewancroft")
        print("  GitHub Sponsors: https://github.com/sponsors/ewanc26")
        sys.exit(0)
    parser = argparse.ArgumentParser(
        description="Analyse .docx files and generate Markdown essays using Ollama"
    )
    parser.add_argument("directory", help="Directory to search for .docx files")
    parser.add_argument("-o", "--output", help="Output directory for essays")
    parser.add_argument(
        "-m",
        "--model",
        default="llama3.2",
        help="Ollama model to use (default: llama3.2)",
    )
    parser.add_argument(
        "--support",
        action="store_true",
        help="Print sponsor links (Ko-fi: https://ko-fi.com/ewancroft · GitHub Sponsors: https://github.com/sponsors/ewanc26)",
    )
    return parser.parse_args()


def validate_args(args: argparse.Namespace):
    """Validate parsed arguments."""
    if not os.path.exists(args.directory):
        print(f"Error: Directory '{args.directory}' does not exist")
        sys.exit(1)
