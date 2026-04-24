# LLM Analyser

This project analyses one or more `.docx` files and uses Ollama to generate Markdown essays about them.

> 🧶 Also available on [Tangled](https://tangled.org/ewancroft.uk/llm-analyser)

## Requirements

- Python 3.x
- Ollama installed locally
- Python packages from `requirements.txt`

Install the Python dependencies with:

```bash
pip install -r requirements.txt
```

Then create the custom Ollama model defined by the bundled `Modelfile`:

```bash
ollama create document-analyser -f ./Modelfile
```

## Usage

Run the analyser against a directory of `.docx` files:

```bash
python main.py <directory_to_analyse>
```

Optional flags:

```bash
python main.py <directory_to_analyse> -m llama3.2
python main.py <directory_to_analyse> -o ./my-output
```

- `-m, --model` — Ollama model name to use
- `-o, --output` — output directory for generated essays

If no output directory is supplied, the script writes essays into a folder named `<directory-slug>_essays` next to `main.py`.

## What it does

- Scans the target directory recursively for `.docx` files
- Reads both paragraphs and tables from each document
- Builds a Markdown essay for each file using the configured Ollama model
- Processes files concurrently for faster batch runs

## Project structure

```text
main.py        # CLI entry point and analysis orchestration
Modelfile      # Ollama model definition and prompt
requirements.txt
```

## Modifying the model

`Modelfile` contains the model instructions and parameters. Edit it if you want to change the prompt, temperature, or base model, then recreate the model with `ollama create`.

## Notes

- The script uses `python-docx` to read Word documents.
- Empty or unreadable documents are still reported, but the generated output will note that no readable content was found.

## ☕ Support

If you found this useful, consider [buying me a ko-fi](https://ko-fi.com/ewancroft)!