import argparse
import logging
import sys
from pathlib import Path
import pandas as pd
import numpy as np
import re
import json
from typing import List, Tuple, Dict, Optional
from utils import *
from column_cleaner import ColumnCleaner
from excel_reader import ExcelReader

# ----------------- Workbook Processor -----------------
class WorkbookCleaner:
    """
    Processes a single Excel workbook: cleans all sheet column names.
    """

    def __init__(self, output_dir: Path):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.column_cleaner = ColumnCleaner()
        self.reader = ExcelReader()

    def clean(self, input_path: Path) -> Optional[Dict]:
        """
        Clean all sheets in a workbook and save to output directory.

        Returns:
            Summary dict if successful, None otherwise.
        """
        try:
            xl = pd.ExcelFile(input_path, engine="openpyxl")
        except Exception as e:
            logger.error(f"Cannot open {input_path.name}: {e}")
            return None

        output_path = self.output_dir / input_path.name
        summary = {
            "input": str(input_path),
            "output": str(output_path),
            "sheets": []
        }
        any_changes = False

        with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
            for sheet_name in xl.sheet_names:
                try:
                    df = self.reader.read_sheet(input_path, sheet_name)
                    df_clean, changes = self.column_cleaner.clean_columns(df)

                    # Write cleaned DataFrame (preserve index if it exists)
                    df_clean.to_excel(writer, sheet_name=sheet_name, index=True)

                    sheet_summary = {
                        "sheet": sheet_name,
                        "column_changes": len(changes)
                    }
                    if changes:
                        any_changes = True
                        sheet_summary["sample_changes"] = changes[:3]  # Log first 3 changes
                    summary["sheets"].append(sheet_summary)

                except Exception as e:
                    logger.error(f"Failed to process sheet '{sheet_name}' in {input_path.name}: {e}")
                    continue

        status = "modified" if any_changes else "unchanged"
        logger.info(f"✔ Saved: {output_path} ({status})")
        for s in summary["sheets"]:
            logger.info(f"  - [{s['sheet']}] {s['column_changes']} column name changes")

        return summary