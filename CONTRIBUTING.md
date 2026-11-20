# Contributing to LLM Analyser

A tool that analyses one or more `.docx` files and uses a local Ollama model to generate Markdown essays about them, processing files concurrently. Thanks for wanting to help!

## Getting started

```bash
pip install -r requirements.txt
ollama create document-analyser -f ./Modelfile
python main.py <directory_to_analyse> --dry-run-safe  # see README for flags
```

Options: `-m` selects the Ollama model, `-o` sets the output directory (default: `<directory-slug>_essays` beside `main.py`).

## Notes for this project

- `Modelfile` **is** the model: prompt, parameters and base model all live there. If you change it, recreate with `ollama create document-analyser -f ./Modelfile` and re-run before opening the PR.
- `python-docx` reads both paragraphs and tables — keep table extraction working; documents are often more table than prose.
- Empty or unreadable documents must still be reported gracefully, with output noting that no readable content was found; keep that failure path covered.
- Concurrency is a feature (batch runs on many files); don't serialise it in a fix without saying so in the PR.

## Before opening a PR

- The documented build and tests pass, and you ran them yourself.
- Conventional commits; one focused PR per change.
- AI-assisted PRs are welcome; stand behind every line.

## Licence

GPL-3.0 (see [LICENSE](LICENSE)). Contributions are accepted under the same terms. Contributions are accepted under the same terms.