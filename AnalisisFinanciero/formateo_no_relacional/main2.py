from pathlib import Path
import pandas as pd
import numpy as np
import json
import math
import datetime as dt

INPUT_DIR  = Path(r"C:\Users\Usuario\Documents\Repositorios\Maestria\AnalisisFinanciero\data\transform")
OUTPUT_DIR = INPUT_DIR / "excel_to_json"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ---------------- helpers ----------------

def _json_safe_scalar(v):
    """Convert pandas/numpy scalars to JSON-safe Python values; NaN/NaT -> None."""
    if v is None:
        return None
    if isinstance(v, (np.floating, float)):
        if pd.isna(v) or math.isnan(float(v)):
            return None
        return float(v)
    if pd.isna(v):
        return None
    if isinstance(v, (np.integer,)):
        return int(v)
    if isinstance(v, (np.bool_, bool)):
        return bool(v)
    if isinstance(v, (pd.Timestamp, dt.datetime, dt.date)):
        return v.isoformat()
    if isinstance(v, (pd.Timedelta, dt.timedelta)):
        return str(v)
    return v

def _split_path(label: str):
    """Split 'A.B.C' -> ['A','B','C'], ignoring empties and trimming whitespace."""
    if label is None:
        return []
    parts = [p.strip() for p in str(label).split(".")]
    return [p for p in parts if p != ""]

def _ensure_path(d: dict, keys):
    """Ensure d[keys[0]]...[keys[-1]] exists as dict; return the leaf dict."""
    cur = d
    for k in keys:
        if k not in cur or not isinstance(cur[k], dict):
            cur[k] = {} if k not in cur else (cur[k] if isinstance(cur[k], dict) else {})
        cur = cur[k]
    return cur

def _nested_set(d: dict, keys, value):
    """Set d[k1][k2]...[kn] = value, creating intermediate dicts."""
    cur = d
    for k in keys[:-1]:
        cur = cur.setdefault(k, {})
    cur[keys[-1]] = value

def _deep_merge(a: dict, b: dict):
    """Merge dict b into a (recursively)."""
    for k, v in b.items():
        if k in a and isinstance(a[k], dict) and isinstance(v, dict):
            _deep_merge(a[k], v)
        else:
            a[k] = v
    return a

def _is_excel_file(p: Path):
    return p.suffix.lower() in {".xlsx", ".xlsm"} and not p.name.startswith("~$")

# --------------- core conversion ----------------

def sheet_to_nested(df: pd.DataFrame) -> dict:
    """
    Convert a single flattened sheet to nested dict:
      for each row r and column c with value v -> tree[row_path + col_path] = v
    - Creates the row path branch even when all values in the row are null.
    """
    # Ensure index is the "Row" labels; if not, try to set it.
    if df.index.name is None or df.index.name != "Row":
        if "Row" in df.columns:
            df = df.set_index("Row")
        else:
            # last resort: keep as-is but create synthetic labels
            df = df.copy()
            df.index.name = "Row"
            if not isinstance(df.index, pd.Index):
                df.index = pd.Index([f"row_{i}" for i in range(len(df))], name="Row")

    # Use strings for column names
    df.columns = [str(c) for c in df.columns]

    out = {}

    # Iterate rows
    for row_label, row in df.iterrows():
        row_path = _split_path(row_label)

        # Always create the row branch to preserve presence (even if all values are null)
        row_branch = _ensure_path(out, row_path) if row_path else out

        # Write non-null cells into nested column paths
        for col_name, val in row.items():
            val_safe = _json_safe_scalar(val)
            if val_safe is None:
                continue  # skip nulls in the JSON payload
            col_path = _split_path(col_name)
            if not col_path:
                # put scalar directly under the row node if column path is empty
                # (rare; normally columns have names)
                # To avoid clobbering dict, store under a default key
                _nested_set(row_branch, ["value"], val_safe)
            else:
                _nested_set(row_branch, col_path, val_safe)

    return out

def workbook_to_nested_json(xlsx_path: Path) -> dict:
    """
    Read all sheets of a flattened workbook and merge them into one nested dict.
    """
    xl = pd.ExcelFile(xlsx_path, engine="openpyxl")
    merged = {}
    for sheet in xl.sheet_names:
        # Read with first column as index (the flattened exporter wrote "Row" there)
        try:
            df = pd.read_excel(xlsx_path, sheet_name=sheet, engine="openpyxl", dtype=object, header=0, index_col=0)
        except Exception:
            df = pd.read_excel(xlsx_path, sheet_name=sheet, engine="openpyxl", dtype=object, header=0)
        tree = sheet_to_nested(df)
        _deep_merge(merged, tree)
    return merged

def folder_excels_to_json(
    input_dir: Path = INPUT_DIR,
    output_dir: Path = OUTPUT_DIR
):
    files = sorted([p for p in input_dir.iterdir() if _is_excel_file(p)])
    if not files:
        print(f"No Excel workbooks found in: {input_dir}")
        return []

    outputs = []
    for xlsx in files:
        try:
            payload = workbook_to_nested_json(xlsx)
            out_path = output_dir / f"{xlsx.stem}.json"
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(payload, f, ensure_ascii=False, indent=2)
            print(f"✔ JSON saved: {out_path}")
            outputs.append(str(out_path))
        except Exception as e:
            print(f"✖ Failed on {xlsx.name}: {e}")
    return outputs

# -------- run on your folder --------
outputs = folder_excels_to_json(INPUT_DIR, OUTPUT_DIR)
print("\nSummary:")
for o in outputs:
    print(" -", o)