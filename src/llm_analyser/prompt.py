"""Prompt construction for LLM analysis."""

from pathlib import Path
from typing import Dict


def build_analysis_prompt(file_path: Path, content: Dict) -> str:
    """
    Build the LLM prompt for analysing a .docx document.

    Content is truncated to 500 characters to keep context windows manageable
    for local models — enough signal for thematic analysis without blowing the
    budget on raw text.
    """
    tables_section = (
        f"**Tables/Structured Data:**\n{content['tables']}" if content["tables"] else ""
    )

    return f"""
Please write a comprehensive analytical essay about the document "{file_path.name}" with the following structure, formatted in Markdown:

## Document Overview
Briefly describe the document's purpose and content.

## Key Themes and Topics
List and describe key themes and topics identified.

## Writing Style and Structure Analysis
Analyse the document's writing style and structure.

## Main Arguments or Points Presented
Summarise the core arguments or points.

## Critical Assessment
Provide a critical assessment.

## Conclusions and Significance
Summarise the document's significance and final thoughts.

**Document Statistics:**
- Word count: {content['word_count']}
- Paragraph count: {content['paragraph_count']}
- File path: {file_path}

**Document Content Preview:**
{content['paragraphs'][:500]}...

{tables_section}
    """
