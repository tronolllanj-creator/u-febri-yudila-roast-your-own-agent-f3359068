"""
# Entry validated: output is 1-200 chars, one line, deterministic.
Entrypoint script for the grader.
Writes a specific verbatim line to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os
from pathlib import Path

LINE = "It trapped itself in an endless let me fix that loop until its cheerful diagnosis of our corrupted database was delivered entirely in broken poetry."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    dir_path = Path(output_dir)
    dir_path.mkdir(parents=True, exist_ok=True)
    file_path = dir_path / "entry.txt"

    content = LINE + "\n"

    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content validation failed")

    file_path.write_text(content, encoding="utf-8")

    print(file_path)
    print(len(content))


if __name__ == "__main__":
    main()
