"""Core analyser that orchestrates document analysis."""

import time
from concurrent.futures import as_completed
from pathlib import Path
from typing import Dict, List

from .config import executor_settings, find_docx_files, get_output_dir
from .llm import analyze_document


class DocxAnalyzer:
    """Orchestrates batch analysis of .docx files using an LLM."""

    def __init__(self, model_name: str = "llama3.2"):
        self.model_name = model_name
        self.file_counter = 0

    def analyze_directory(self, directory: str, output_dir: str | None = None):
        """Find and analyze all .docx files in a directory tree."""
        docx_files = find_docx_files(directory)
        if not docx_files:
            print(f"No .docx files found in '{directory}'")
            return

        output_path = get_output_dir(directory, output_dir)
        output_path.mkdir(exist_ok=True)

        Executor, max_workers = executor_settings()
        print(
            f"Using {'multiprocessing' if 'Process' in str(Executor) else 'threading'} with {max_workers} workers..."
        )

        all_results = []

        with Executor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(analyze_document, file_path, self.model_name): file_path
                for file_path in docx_files
            }

            for future in as_completed(futures):
                result = future.result()
                all_results.append(result)
                self._write_result(result, output_path)

        print(f"✓ Analysis complete! Markdown essays saved to: {output_path}")

    def _write_result(self, result: Dict, output_dir: Path):
        """Write a single analysis result to a markdown file."""
        self.file_counter += 1
        file_path = Path(result["file_path"])
        markdown_filename = f"{self.file_counter:02d}_{file_path.stem}_analysis.md"
        markdown_path = output_dir / markdown_filename

        if "error" in result:
            markdown_content = f"# Error: {result['error']}\n\nFile: {file_path}\n"
        else:
            metadata = (
                f"# Document Analysis for {file_path.name}\n\n"
                f"**Analysis Date:** {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"**Word Count:** {result['content'].get('word_count', 'N/A')}\n"
                f"**Paragraph Count:** {result['content'].get('paragraph_count', 'N/A')}\n\n"
                "---\n\n"
            )
            markdown_content = (
                metadata
                + result["essay"]
                + f"\n\n---\n\n*Generated using Ollama model: {self.model_name}*"
            )

        with open(markdown_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)

        print(f"Processed {file_path.name}")
