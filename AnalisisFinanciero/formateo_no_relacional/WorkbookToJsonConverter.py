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
from SheetToJsonConverter import *

# ----------------- Logging Setup -----------------
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# ----------------- Workbook Processor -----------------
class WorkbookToJsonConverter:
    """Convert all sheets of a workbook into a single merged nested JSON tree."""

    def __init__(self):
        self.sheet_converter = SheetToJsonConverter()

    def convert(self, file_path: Path) -> Optional[Dict]:
        """
        Read all sheets and merge into one nested dict.
        Returns None if file cannot be read.
        """
        try:
            xl = pd.ExcelFile(file_path, engine="openpyxl")
        except Exception as e:
            logger.error(f"Failed to open {file_path.name}: {e}")
            return None

        merged_tree = {}

        for sheet_name in xl.sheet_names:
            try:
                # Try to read with index_col=0 (assumes "Index" column was written)
                df = pd.read_excel(
                    file_path, sheet_name=sheet_name,
                    engine="openpyxl", dtype=object, header=0, index_col=0
                )
            except Exception:
                logger.debug(f"Falling back to no index for sheet '{sheet_name}' in {file_path.name}")
                df = pd.read_excel(
                    file_path, sheet_name=sheet_name,
                    engine="openpyxl", dtype=object, header=0
                )

            sheet_tree = self.sheet_converter.convert(df)
            NestedDictBuilder.deep_merge(merged_tree, sheet_tree)
            logger.debug(f"Processed sheet: {sheet_name} ({len(df)} rows)")

        return merged_tree