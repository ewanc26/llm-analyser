"""LLM interaction layer for llm-analyser."""

from pathlib import Path
from typing import Dict

import ollama


def analyze_document(file_path: Path, model_name: str) -> Dict:
    """Process a single .docx file and return its content and generated essay."""
    from .docx_reader import read_docx
    from .prompt import build_analysis_prompt

    try:
        client = ollama.Client()
        content = read_docx(file_path)

        if not content["paragraphs"]:
            essay_text = f"No readable content found in {file_path.name}"
        else:
            prompt = build_analysis_prompt(file_path, content)
            response = client.generate(model=model_name, prompt=prompt)
            essay_text = response["response"]

        return {"file_path": str(file_path), "content": content, "essay": essay_text}

    except Exception as e:
        return {
            "file_path": str(file_path),
            "error": str(e),
            "content": {},
            "essay": "",
        }
