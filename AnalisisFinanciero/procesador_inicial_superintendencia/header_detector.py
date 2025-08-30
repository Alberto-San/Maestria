# flatten_excel.py

import argparse
import json
import logging
import sys
from pathlib import Path
import pandas as pd
import numpy as np
from utils import *

# ----------------- Logging Setup -----------------
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class HeaderDetector:
    """Detects hierarchical levels in Excel (row & column headers)."""

    @staticmethod
    def detect(raw_df):
        """
        Infer (row_levels, col_levels) from leading nulls.
        Returns dict with metadata.
        """
        nrows, ncols = raw_df.shape

        # Skip fully blank top rows
        blank_top_rows = 0
        i = 0
        while i < nrows and raw_df.iloc[i, :].apply(is_blank).all():
            blank_top_rows += 1
            i += 1

        # Collect header rows (must start with at least one blank)
        header_rows = []
        while i < nrows:
            lead_nulls = count_leading_nulls(raw_df.iloc[i, :].tolist())
            if lead_nulls == 0:
                break
            header_rows.append(i)
            i += 1

        col_levels = len(header_rows)

        # Row levels: min leading blanks across header rows
        if col_levels > 0:
            row_levels = min(count_leading_nulls(raw_df.iloc[r, :].tolist()) for r in header_rows)
        else:
            r_idx = first_nonempty_row_idx(raw_df)
            row_levels = count_leading_nulls(raw_df.iloc[r_idx, :].tolist()) if r_idx is not None else 0

        # Count blank left columns
        blank_left_cols = 0
        j = 0
        while j < ncols and raw_df.iloc[:, j].apply(is_blank).all():
            blank_left_cols += 1
            j += 1

        return {
            "row_levels": int(row_levels),
            "col_levels": int(col_levels),
            "blank_top_rows": int(blank_top_rows),
            "blank_left_cols": int(blank_left_cols),
        }

