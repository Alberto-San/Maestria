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
from workbook_reader import WorkbookCleaner

# ----------------- Batch Processor -----------------
class BatchColumnCleaner:
    """
    Batch process all Excel files in a directory.
    """

    def __init__(self, input_dir: Path, output_dir: Path):
        self.input_dir = input_dir
        self.output_dir = output_dir

        if not self.input_dir.exists():
            raise FileNotFoundError(f"Input directory not found: {self.input_dir}")
        if not self.input_dir.is_dir():
            raise NotADirectoryError(f"Input path is not a directory: {self.input_dir}")

    def run(self) -> List[Dict]:
        """
        Process all Excel files and return a list of summaries.
        """
        input_files = [p for p in self.input_dir.iterdir() if p.is_file() and is_excel_file(p)]
        if not input_files:
            logger.info(f"No Excel files found in {self.input_dir}")
            return []

        logger.info(f"Found {len(input_files)} Excel file(s) to process.")
        workbook_cleaner = WorkbookCleaner(self.output_dir)
        summaries = []

        for file_path in sorted(input_files):
            summary = workbook_cleaner.clean(file_path)
            if summary:
                summaries.append(summary)

        return summaries
