# AGENTS.md

Guidance for agents working on LLM Analyser, a Python CLI that extracts `.docx` content and asks local Ollama models to produce Markdown essays.

## Architecture

- `main.py` parses and validates the input directory, constructs `DocxAnalyzer`, and converts uncaught batch errors into exit status 1.
- `src/llm_analyser/config.py` recursively discovers non-Word-temporary `.docx` files and selects a process pool on hosts with at least four CPUs, otherwise a thread pool, capped at eight workers.
- `docx_reader.py` extracts non-empty paragraphs and tables; `prompt.py` sends only the first 500 paragraph characters plus all extracted table text; `llm.py` wraps per-file failures into result dictionaries.
- `analyser.py` consumes futures in completion order and prefixes output names with an incrementing completion counter, so output numbering is intentionally nondeterministic today.
- `Modelfile` defines the custom local model; changes require recreating it.

## Rules

- Treat documents as private and untrusted. Never upload them to a remote service, log their full contents, or execute embedded content.
- Preserve paragraph/table extraction order within each document and report unreadable/empty inputs clearly. Do not describe the current 500-character preview as full-document analysis.
- Bound concurrency, request timeouts, context size, and output paths. Avoid loading an entire large corpus unnecessarily.
- Prevent output filename collisions and path traversal; note that `Path.mkdir(exist_ok=True)` does not create missing parent directories and existing numbered output files are currently overwritten.
- Model output is untrusted Markdown. Do not claim factual accuracy beyond the supplied documents.

## Validation

Create a virtual environment, install `requirements.txt`, run `python -m compileall main.py src`, and execute focused tests with mocked `ollama.Client` and executors. Cover temporary-file exclusion, nested discovery, empty/corrupt DOCX, tables, the 500-character truncation boundary, duplicate stems, nondeterministic completion order, worker selection, per-file errors, missing parent output directories, and custom output paths. Do not commit input documents, generated essays, models, or virtual environments.
