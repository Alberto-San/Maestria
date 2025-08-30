# flatten_excel.py

import logging
from pathlib import Path
import pandas as pd
import numpy as np
from utils import *
from header_detector import HeaderDetector

# ----------------- Logging Setup -----------------
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# ----------------- Excel Flattener -----------------
class ExcelFlattener:
    """Flattens a single sheet of an Excel file with hierarchical headers."""

    def __init__(self, keep_all_columns=False, row_label_empty_fallback="unnamed"):
        self.keep_all_columns = keep_all_columns
        self.row_label_empty_fallback = row_label_empty_fallback

    def flatten(self, file_path, sheet_name=0):
        """
        Flatten one sheet.

        Args:
            file_path: Path to Excel file.
            sheet_name: Sheet name or index.

        Returns:
            (flattened_df, metadata_dict)
        """
        try:
            raw = pd.read_excel(file_path, sheet_name=sheet_name, header=None, dtype=object, engine="openpyxl")
        except Exception as e:
            logger.error(f"Failed to read {file_path}, sheet '{sheet_name}': {e}")
            raise

        # Normalize blanks
        raw = raw.applymap(lambda x: np.nan if is_blank(x) else x)

        meta = HeaderDetector.detect(raw)
        row_levels = meta["row_levels"]
        col_levels = meta["col_levels"]

        # --- Column names ---
        if col_levels > 0:
            header_block = raw.iloc[:col_levels, row_levels:].copy()
            header_block = header_block.ffill(axis=1).ffill(axis=0)
            col_names = []
            for j in range(header_block.shape[1]):
                parts = [str(v).strip() for v in header_block.iloc[:, j] if not pd.isna(v) and str(v).strip()]
                col_names.append(".".join(parts))
        else:
            r_idx = first_nonempty_row_idx(raw)
            if r_idx is None:
                logger.warning(f"Worksheet '{sheet_name}' in {file_path} is empty.")
                df_empty = pd.DataFrame()
                meta["explanation"] = "Worksheet appears empty."
                return df_empty, meta
            col_names = [str(x).strip() if not pd.isna(x) else "" for x in raw.iloc[r_idx, row_levels:]]
            col_levels = 1  # for symmetry in explanation

        # --- Row index ---
        if row_levels > 0:
            row_label_block = raw.iloc[col_levels:, :row_levels].copy()
            row_label_block = row_label_block.ffill(axis=0)
            row_index = []
            for i in range(row_label_block.shape[0]):
                parts = [str(v).strip() for v in row_label_block.iloc[i, :] if not pd.isna(v) and str(v).strip()]
                label = ".".join(parts) if parts else self.row_label_empty_fallback
                row_index.append(label)
        else:
            row_index = [f"row_{i}" for i in range(raw.shape[0] - col_levels)]

        # --- Data block ---
        data_block = raw.iloc[col_levels:, row_levels:].copy()
        for c in data_block.columns:
            data_block[c] = pd.to_numeric(data_block[c], errors="ignore")

        # Filter columns
        keep_cols_mask = pd.Series([True] * data_block.shape[1], index=data_block.columns)
        if not self.keep_all_columns:
            keep_cols_mask = ~data_block.isna().all(axis=0)
        data_block = data_block.loc[:, keep_cols_mask]
        flat_cols = [col_names[j] for j, keep in enumerate(keep_cols_mask.tolist()) if keep]
        flat_cols = uniquify([c if c != "" else "unnamed" for c in flat_cols])

        # Final DataFrame
        df_out = data_block.copy()
        df_out.columns = flat_cols
        df_out.index = row_index
        df_out.index.name = "Index"

        # Ensure at least one column
        if df_out.shape[1] == 0:
            df_out["(no_data)"] = pd.Series([np.nan] * len(df_out), index=df_out.index)

        # Explanation
        meta["explanation"] = (
            "Levels inferred from leading nulls:\n"
            f"- Skipped {meta['blank_top_rows']} fully blank top row(s) (spacing).\n"
            f"- Column-header levels = {meta['col_levels']}.\n"
            f"- Row-header levels = {meta['row_levels']}.\n"
            f"- Ignored {meta['blank_left_cols']} fully blank left column(s) as spacing.\n"
            "Headers were forward-filled and dot-joined into flat labels.\n"
            "Rows with all-null data are preserved."
        )
        return df_out, meta

