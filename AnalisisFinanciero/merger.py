from __future__ import annotations
import json
from pathlib import Path
from typing import Iterable, Union, Dict, Any

PathLike = Union[str, Path]

def bundle_json_files(
    files: Iterable[PathLike],
    output_path: PathLike | None = None,
    key: str | callable = "stem",
    encoding: str = "utf-8",
) -> Dict[str, Any]:
    """
    Combine multiple JSON files into a single dict: {<file-key>: <file-content>}.

    Args:
        files: Iterable of file paths (e.g., list[PathLike] or Path.glob()).
        output_path: If provided, write the bundled JSON to this path.
        key: How to derive the dict key from each file path:
             - "stem" -> filename without extension (default)
             - "name" -> filename with extension
             - "path" -> full path string
             - callable(Path) -> custom key function
        encoding: File encoding for reading/writing.

    Returns:
        Dict mapping computed keys to parsed JSON contents.

    Notes:
        - If two files resolve to the same key, a suffix like "#2", "#3" is appended.
        - Raises ValueError if any file is not valid JSON.
    """
    result: Dict[str, Any] = {}

    for f in files:
        p = Path(f)
        if not p.is_file():
            raise FileNotFoundError(f"Not a file: {p}")

        with p.open("r", encoding=encoding) as fh:
            try:
                data = json.load(fh)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON in {p}: {e}") from e

        # Compute the key
        if callable(key):
            k = key(p)
        elif key == "stem":
            k = p.stem
        elif key == "name":
            k = p.name
        elif key == "path":
            k = str(p)
        else:
            raise ValueError("key must be 'stem', 'name', 'path', or a callable(Path)->str")

        # Ensure unique keys
        if k in result:
            i = 2
            new_k = f"{k}#{i}"
            while new_k in result:
                i += 1
                new_k = f"{k}#{i}"
            k = new_k

        result[k] = data

    if output_path:
        out = Path(output_path)
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", encoding=encoding) as fo:
            json.dump(result, fo, indent=2, ensure_ascii=False)

    return result


from pathlib import Path

# 1) Bundle all JSON files in a folder, keys are filenames (without .json)
files = Path(r"C:\Users\Usuario\Documents\Repositorios\Maestria\AnalisisFinanciero\data\json").glob("*.json")
bundle = bundle_json_files(files, output_path="bundle.json")

# 2) Use filenames WITH extension as keys
files = ["a.json", "b.json", "c.json"]
bundle = bundle_json_files(files, key="name")

# 3) Custom key (e.g., include parent folder name)
bundle = bundle_json_files(
    Path("data").glob("*.json"),
    key=lambda p: f"{p.parent.name}/{p.stem}"
)
