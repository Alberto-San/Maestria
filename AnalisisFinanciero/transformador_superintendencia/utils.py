import argparse
import logging
import sys
from pathlib import Path
import pandas as pd
import numpy as np
import re
import json
from typing import List, Tuple, Dict, Optional

# ----------------- Logging Setup -----------------
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# ----------------- Utilities -----------------
def is_excel_file(path: Path) -> bool:
    """Check if path is a valid Excel file (not temporary)."""
    return path.suffix.lower() in {".xlsx", ".xlsm"} and not path.name.startswith("~$")


def normalize_label(label: object, empty_fallback: str = "unnamed") -> str:
    """
    Normalize a hierarchical column label by:
      - Collapsing whitespace and multiple dots
      - Removing adjacent duplicate segments
      - Trimming
    """
    if label is None or (isinstance(label, float) and np.isnan(label)):
        return empty_fallback
    s = str(label).strip()

    # Collapse spaces around dots and multiple dots
    s = re.sub(r"\s*\.\s*", ".", s)       # " A . B " → "A.B"
    s = re.sub(r"\.+", ".", s)            # "A..B" → "A.B"
    s = s.strip(". ")                      # ". A . B ." → "A.B"

    if not s:
        return empty_fallback

    # Split and clean parts
    parts = [p.strip() for p in s.split(".") if p.strip()]
    if not parts:
        return empty_fallback

    # Remove adjacent duplicates: ["A", "A", "B"] → ["A", "B"]
    dedup = [parts[0]]
    for p in parts[1:]:
        if p != dedup[-1]:
            dedup.append(p)

    result = ".".join(dedup)
    return result if result else empty_fallback


def uniquify(names: List[str], empty_fallback: str = "unnamed") -> List[str]:
    """
    Ensure uniqueness of names by appending __2, __3, etc. to duplicates.
    """
    seen: Dict[str, int] = {}
    output = []
    for name in names:
        base = name.strip() if name and str(name).strip() else empty_fallback
        if base not in seen:
            seen[base] = 1
            output.append(base)
        else:
            seen[base] += 1
            output.append(f"{base}__{seen[base]}")
    return output