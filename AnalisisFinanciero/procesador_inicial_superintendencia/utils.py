import logging
import pandas as pd
import re

# ----------------- Logging Setup -----------------
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


# ----------------- Utilities -----------------
def is_blank(x):
    """True if cell is NaN or an empty/whitespace-only string."""
    if pd.isna(x):
        return True
    s = str(x).strip()
    return s == "" or s.lower() in {"nan", "none"}


def count_leading_nulls(seq):
    """Count consecutive leading blanks in a 1D sequence."""
    c = 0
    for v in seq:
        if is_blank(v):
            c += 1
        else:
            break
    return c


def first_nonempty_row_idx(df):
    """Return index of first row with any non-blank cell."""
    for i in range(len(df)):
        if (~df.iloc[i, :].apply(is_blank)).any():
            return i
    return None


def first_nonempty_col_idx(df):
    """Return index of first column with any non-blank cell."""
    for j in range(df.shape[1]):
        if (~df.iloc[:, j].apply(is_blank)).any():
            return j
    return None


def uniquify(seq, empty_label="unnamed"):
    """Ensure names are unique by appending suffixes for duplicates."""
    seen = {}
    out = []
    for s in seq:
        s = (s or "").strip()
        s = s if s != "" else empty_label
        if s not in seen:
            seen[s] = 1
            out.append(s)
        else:
            seen[s] += 1
            out.append(f"{s}__{seen[s]}")
    return out


def sanitize_sheet_name(name: str) -> str:
    """Make a valid Excel sheet name (<=31 chars, no special chars)."""
    name = re.sub(r'[:\\/?*\[\]]', '_', str(name))
    return name[:31]

