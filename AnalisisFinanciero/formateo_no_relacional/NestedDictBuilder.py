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

# ----------------- Logging Setup -----------------
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# ----------------- Nested Dict Operations -----------------
class NestedDictBuilder:
    """Utilities for building and merging nested dictionaries."""

    @staticmethod
    def ensure_path(d: Dict, keys: List[str]) -> Dict:
        """Ensure d[keys[0]][keys[1]]... exists as dict; return the innermost dict."""
        cur = d
        for k in keys:
            if k not in cur or not isinstance(cur[k], dict):
                cur[k] = {}
            cur = cur[k]
        return cur

    @staticmethod
    def set_value(d: Dict, keys: List[str], value: Any):
        """Set d[k1][k2]...[kn] = value, creating intermediate dicts."""
        cur = d
        for k in keys[:-1]:
            cur = cur.setdefault(k, {})
        cur[keys[-1]] = value

    @staticmethod
    def deep_merge(target: Dict, source: Dict):
        """Merge source into target recursively."""
        for k, v in source.items():
            if k in target and isinstance(target[k], dict) and isinstance(v, dict):
                NestedDictBuilder.deep_merge(target[k], v)
            else:
                target[k] = v