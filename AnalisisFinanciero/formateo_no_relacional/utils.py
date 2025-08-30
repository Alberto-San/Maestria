import argparse
import logging
import sys
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
import pandas as pd
import numpy as np
import datetime as dt

# ----------------- Logging Setup -----------------
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# ----------------- Utilities -----------------
def is_excel_file(path: Path) -> bool:
    """Check if path is a valid Excel file (not temporary)."""
    return path.suffix.lower() in {".xlsx", ".xlsm"} and not path.name.startswith("~$")


def json_safe_scalar(value: Any) -> Any:
    """
    Convert pandas/numpy scalars to JSON-safe Python types.
    - NaN, NaT, None → None
    - np.int64 → int
    - np.float64 → float
    - Timestamp → ISO string
    - Timedelta → string
    """
    if value is None:
        return None
    if isinstance(value, (float, np.floating)):
        if np.isnan(value):
            return None
        return float(value)
    if isinstance(value, (int, np.integer)):
        return int(value)
    if isinstance(value, (bool, np.bool_)):
        return bool(value)
    if isinstance(value, (pd.Timestamp, dt.datetime)):
        return value.isoformat()
    if isinstance(value, (pd.Timedelta, dt.timedelta)):
        return str(value)
    if pd.isna(value):
        return None
    return value


def split_path(label: str) -> List[str]:
    """Split 'A.B.C' → ['A','B','C'], trimming and filtering empty parts."""
    if not label or not str(label).strip():
        return []
    return [p.strip() for p in str(label).split(".") if p.strip()]