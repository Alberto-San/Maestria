import argparse
import logging
import sys
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
import pandas as pd
import numpy as np
import datetime as dt
from utils import *
from NestedDictBuilder import *

# ----------------- Logging Setup -----------------
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# ----------------- Sheet Converter -----------------
class SheetToJsonConverter:
    """Convert a single flattened DataFrame to a nested dictionary."""

    def convert(self, df: pd.DataFrame) -> Dict:
        """
        Convert a flattened sheet (with hierarchical row/column paths) to nested dict.

        Rules:
          - Index index (named "Index") becomes outer path.
          - Column names become inner path.
          - Non-null values are written to nested path.
          - All-null rows still create an empty branch.
        """
        # Ensure index is "Index"
        if df.index.name != "Index":
            if "Index" in df.columns:
                df = df.set_index("Index")
            else:
                df = df.copy()
                df.index = pd.Index([f"row_{i}" for i in range(len(df))], name="Index")

        # Normalize column names
        df.columns = [str(c) for c in df.columns]

        result = {}

        for row_label, row in df.iterrows():
            row_path = split_path(row_label)
            row_branch = (
                NestedDictBuilder.ensure_path(result, row_path)
                if row_path else result
            )

            for col_name, val in row.items():
                safe_val = json_safe_scalar(val)
                if safe_val is None:
                    continue  # Skip nulls

                col_path = split_path(col_name)
                if not col_path:
                    # Fallback: store under a generic key to avoid clobbering
                    NestedDictBuilder.set_value(row_branch, ["value"], safe_val)
                else:
                    NestedDictBuilder.set_value(row_branch, col_path, safe_val)

        return result
