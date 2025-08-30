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

class ExcelReader:
    """
    Reads Excel sheets, handling indexed or non-indexed formats.
    """

    @staticmethod
    def read_sheet(path: Path, sheet_name: str) -> pd.DataFrame:
        """
        Read a single sheet. Tries to use index_col=0 (from flattener), falls back otherwise.
        """
        try:
            return pd.read_excel(
                path, sheet_name=sheet_name, engine="openpyxl",
                dtype=object, header=0, index_col=0
            )
        except Exception:
            logger.debug(f"Falling back to no index for {path.name}, sheet '{sheet_name}'")
            return pd.read_excel(
                path, sheet_name=sheet_name, engine="openpyxl",
                dtype=object, header=0, index_col=None
            )