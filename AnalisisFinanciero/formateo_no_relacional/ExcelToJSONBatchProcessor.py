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
from WorkbookToJsonConverter import *

# ----------------- Logging Setup -----------------
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


# ----------------- Batch Processor -----------------
class ExcelToJSONBatchProcessor:
    """Batch process all Excel files in a folder to JSON."""

    def __init__(self, input_dir: Path, output_dir: Path):
        self.input_dir = input_dir.resolve()
        self.output_dir = output_dir.resolve()

        if not self.input_dir.exists():
            raise FileNotFoundError(f"Input directory not found: {self.input_dir}")
        if not self.input_dir.is_dir():
            raise NotADirectoryError(f"Input path is not a directory: {self.input_dir}")

        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.converter = WorkbookToJsonConverter()

    def run(self) -> List[Dict[str, Any]]:
        """
        Process all Excel files and return a summary of operations.
        """
        files = [f for f in self.input_dir.iterdir() if f.is_file() and is_excel_file(f)]
        if not files:
            logger.info(f"No Excel files found in {self.input_dir}")
            return []

        logger.info(f"Processing {len(files)} Excel file(s)...")
        summaries = []

        for file_path in sorted(files):
            try:
                tree = self.converter.convert(file_path)
                if tree is None:
                    continue  # Error already logged

                output_path = self.output_dir / f"{file_path.stem}.json"
                with open(output_path, "w", encoding="utf-8") as f:
                    json.dump(tree, f, ensure_ascii=False, indent=2)

                summary = {
                    "input": str(file_path),
                    "output": str(output_path),
                    "status": "success"
                }
                logger.info(f"✔ JSON saved: {output_path}")
            except Exception as e:
                logger.error(f"Failed to process {file_path.name}: {e}")
                summary = {
                    "input": str(file_path),
                    "output": None,
                    "status": "failed",
                    "error": str(e)
                }

            summaries.append(summary)

        return summaries