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
from batch_processor import BatchColumnCleaner

# ----------------- CLI Interface -----------------
def main():
    parser = argparse.ArgumentParser(
        description="""
        Clean duplicate/degenerate column labels in flattened Excel files.
        - Fixes: 'A..B', 'X.T.T', ' Foo . Bar . Bar ' → 'A.B', 'X.T', 'Foo.Bar'
        - Ensures all column names are unique.
        Output is saved to a new folder.
        """
    )
    parser.add_argument(
        "--input_dir", type=str, required=True,
        help="Directory containing flattened Excel files."
    )
    parser.add_argument(
        "--output_dir", type=str,
        help="Output directory (default: input_dir/cleaned_columns)."
    )
    parser.add_argument(
        "--verbose", action="store_true",
        help="Print detailed change logs."
    )

    args = parser.parse_args()

    input_dir = Path(args.input_dir).resolve()
    output_dir = Path(args.output_dir).resolve() if args.output_dir else input_dir / "cleaned_columns"

    try:
        processor = BatchColumnCleaner(input_dir=input_dir, output_dir=output_dir)
        summaries = processor.run()

        # Final summary
        print("\n" + "=" * 60)
        print("CLEANING SUMMARY")
        print("=" * 60)
        if not summaries:
            print("No files were processed.")
        else:
            total_sheets = sum(len(s["sheets"]) for s in summaries)
            total_changes = sum(
                sum(sheet["column_changes"] for sheet in s["sheets"])
                for s in summaries
            )
            print(f"✅ Processed {len(summaries)} file(s), {total_sheets} sheet(s).")
            print(f"🔄 Total column name changes: {total_changes}")
            print(f"📁 Output saved to: {output_dir}")

            if args.verbose:
                print("\nDetailed per-file:")
                for s in summaries:
                    print(f"\nInput:  {s['input']}")
                    print(f"Output: {s['output']}")
                    for sheet in s["sheets"]:
                        if sheet["column_changes"] > 0:
                            print(f"  - [{sheet['sheet']}] {sheet['column_changes']} changes")

        # Save summary to JSON
        summary_file = output_dir / "cleaning_summary.json"
        with open(summary_file, "w", encoding="utf-8") as f:
            json.dump(summaries, f, indent=2, ensure_ascii=False)
        logger.info(f"Summary saved to {summary_file}")

    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()