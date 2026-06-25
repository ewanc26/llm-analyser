#!/usr/bin/env python3
"""Entry point for llm-analyser — analyse .docx files with LLMs."""

import sys

from src.llm_analyser.analyser import DocxAnalyzer
from src.llm_analyser.cli import parse_args, validate_args


def main():
    """Parse args and run document analysis across the given directory."""
    args = parse_args()
    validate_args(args)

    analyzer = DocxAnalyzer(model_name=args.model)

    try:
        analyzer.analyze_directory(args.directory, args.output)
    except KeyboardInterrupt:
        print("\nAnalysis interrupted by user")
    except Exception as e:
        print(f"Error during analysis: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
