# flatten_excel.py

import logging
from pathlib import Path
import pandas as pd
from utils import *
from excel_flattener import ExcelFlattener

# ----------------- Logging Setup -----------------
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class BatchProcessor:
    """Processes a folder of Excel files and flattens all sheets."""

    def __init__(self, input_dir, output_subdir="flattened", keep_all_columns=False, verbose=False):
        self.input_dir = Path(input_dir)
        self.output_subdir = output_subdir
        self.keep_all_columns = keep_all_columns
        self.verbose = verbose
        self.flattener = ExcelFlattener(keep_all_columns=keep_all_columns)

        if not self.input_dir.exists():
            raise FileNotFoundError(f"Input directory not found: {self.input_dir}")

        self.out_dir = self.input_dir / output_subdir
        self.out_dir.mkdir(parents=True, exist_ok=True)

    def process(self, include_patterns=(".xlsx", ".xlsm")):
        """Process all matching files."""
        files = [p for p in self.input_dir.iterdir() if p.is_file() and p.suffix.lower() in include_patterns]
        if not files:
            logger.info(f"No files found with patterns {include_patterns} in {self.input_dir}")
            return []

        summaries = []

        for f in sorted(files):
            try:
                xl = pd.ExcelFile(f, engine="openpyxl")
            except Exception as e:
                logger.error(f"Skipping {f.name}: cannot open → {e}")
                continue

            out_path = self.out_dir / (f.stem + "_flattened.xlsx")
            sheet_summaries = []

            with pd.ExcelWriter(out_path, engine="openpyxl") as writer:
                for sheet in xl.sheet_names:
                    try:
                        df_flat, meta = self.flattener.flatten(f, sheet_name=sheet)
                        sheetname = sanitize_sheet_name(f"flattened_{sheet}")
                        df_flat.to_excel(writer, sheet_name=sheetname)

                        sheet_summary = {
                            "sheet": sheet,
                            "rows": int(df_flat.shape[0]),
                            "cols": int(df_flat.shape[1]),
                            "row_levels": int(meta.get("row_levels", 0)),
                            "col_levels": int(meta.get("col_levels", 0)),
                        }
                        if self.verbose:
                            sheet_summary["explanation"] = meta.get("explanation", "")
                        sheet_summaries.append(sheet_summary)

                    except Exception as e:
                        logger.error(f"Failed to process sheet '{sheet}' in {f.name}: {e}")
                        continue

            summary = {
                "input": str(f),
                "output": str(out_path),
                "sheets": sheet_summaries
            }
            summaries.append(summary)

            logger.info(f"✔ Saved: {out_path}")
            for s in sheet_summaries:
                logger.info(
                    f"  - [{s['sheet']}] {s['rows']}×{s['cols']} "
                    f"(row_levels={s['row_levels']}, col_levels={s['col_levels']})"
                )

        return summaries

