"""Configuration and file discovery for llm-analyser."""

import os
import re
from pathlib import Path
from typing import List


def find_docx_files(directory: str) -> List[Path]:
    """Find all .docx files in a directory tree, excluding temp files."""
    directory_path = Path(directory)
    return [p for p in directory_path.rglob("*.docx") if not p.name.startswith("~$")]


def get_output_dir(directory: str, output_dir: str | None = None) -> Path:
    """Determine the output directory for analysis results."""
    if output_dir is not None:
        return Path(output_dir)

    folder_slug = re.sub(r"[^a-zA-Z0-9]+", "_", Path(directory).name.lower())
    script_root = Path(__file__).parent.parent.parent
    return script_root / f"{folder_slug}_essays"


def executor_settings() -> tuple[type, int]:
    """Determine the best executor (process vs thread) and worker count."""
    use_multiprocessing = os.cpu_count() is not None and os.cpu_count() >= 4
    Executor = (
        __import__("concurrent.futures").futures.ProcessPoolExecutor
        if use_multiprocessing
        else __import__("concurrent.futures").futures.ThreadPoolExecutor
    )
    max_workers = min(os.cpu_count() or 2, 8)
    return Executor, max_workers
