# AGENTS.md

Guidance for agents working on LLM Analyser, a Python CLI that extracts `.docx` content and asks local Ollama models to produce Markdown essays.

## Architecture

- `main.py` is the user entry point.
- `src/llm_analyser/` separates CLI/config, DOCX extraction, prompt construction, Ollama access, and orchestration.
- `Modelfile` defines the custom local model; changes require recreating it.

## Rules

- Treat documents as private and untrusted. Never upload them to a remote service, log their full contents, or execute embedded content.
- Extract paragraphs and tables in predictable document order and report unreadable/empty inputs clearly.
- Bound concurrency, request timeouts, context size, and output paths. Avoid loading an entire large corpus unnecessarily.
- Prevent output filename collisions and path traversal; do not overwrite source documents.
- Model output is untrusted Markdown. Do not claim factual accuracy beyond the supplied documents.

## Validation

Create a virtual environment, install `requirements.txt`, run `python -m compileall main.py src`, and execute focused tests with a mocked Ollama client. Cover nested discovery, empty/corrupt DOCX, tables, duplicate names, Unicode, model timeout, partial batch failure, custom output directory, and deterministic prompt construction. Do not commit input documents, generated essays, models, or virtual environments.
