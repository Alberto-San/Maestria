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
from ExcelToJSONBatchProcessor import *

# ----------------- Logging Setup -----------------
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

# ----------------- CLI Interface -----------------
def main():
    parser = argparse.ArgumentParser(
        description="""
        Convert flattened Excel files to nested JSON structure.
        - Input: Excel files with hierarchical row/column paths (dot-joined).
        - Output: One JSON file per workbook, with nested keys from row + column paths.
        - All sheets are merged into a single tree per workbook.
        - All-null rows still create empty branches (presence preserved).
        """
    )
    parser.add_argument(
        "--input_dir", type=str, required=True,
        help="Directory containing flattened Excel files."
    )
    parser.add_argument(
        "--output_dir", type=str,
        help="Output directory (default: input_dir/excel_to_json)."
    )

    args = parser.parse_args()

    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir) if args.output_dir else input_dir / "excel_to_json"

    try:
        processor = ExcelToJSONBatchProcessor(input_dir=input_dir, output_dir=output_dir)
        summaries = processor.run()

        # Final summary
        print("\n" + "=" * 60)
        print("EXCEL TO JSON CONVERSION SUMMARY")
        print("=" * 60)

        success_count = sum(1 for s in summaries if s["status"] == "success")
        fail_count = len(summaries) - success_count

        if not summaries:
            print("No files were processed.")
        else:
            print(f"✅ Success: {success_count}")
            print(f"❌ Failed:  {fail_count}")
            print(f"📁 Output:  {output_dir}")

            # Save summary
            summary_file = output_dir / "conversion_summary.json"
            with open(summary_file, "w", encoding="utf-8") as f:
                json.dump(summaries, f, indent=2, ensure_ascii=False)
            logger.info(f"Summary saved to {summary_file}")

    except Exception as e:
        logger.error(f"Fatal error during processing: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
