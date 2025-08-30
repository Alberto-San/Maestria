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

class ColumnCleaner:
    """
    Cleans and deduplicates hierarchical column names in DataFrames.
    """

    @staticmethod
    def clean_columns(df: pd.DataFrame) -> Tuple[pd.DataFrame, List[Tuple[str, str]]]:
        """
        Returns a cleaned DataFrame and a list of (old, new) column name changes.
        """
        df_clean = df.copy()
        old_cols = [str(c) for c in df_clean.columns]
        normalized = [normalize_label(c) for c in old_cols]
        unique_cols = uniquify(normalized)

        df_clean.columns = unique_cols

        changes = [(old, new) for old, new in zip(old_cols, unique_cols) if old != new]
        return df_clean, changes