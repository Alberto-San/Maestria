# flatten_excel.py

import argparse
import json
import logging
import sys
from utils import *
from batch_processor import BatchProcessor

# ----------------- Logging Setup -----------------
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


# ----------------- CLI Interface -----------------
def main():
    parser = argparse.ArgumentParser(
        description="Flatten hierarchical Excel headers (rows & columns), preserving all-null rows. Batch processes a folder."
    )
    parser.add_argument("--input_dir", type=str, required=True, help="Input directory containing Excel files.")
    parser.add_argument("--output_subdir", type=str, default="flattened", help="Subdirectory name for output files.")
    parser.add_argument("--keep_all_columns", action="store_true", help="Keep columns that are all NaN.")
    parser.add_argument("--verbose", action="store_true", help="Include detailed explanations in output.")
    parser.add_argument("--patterns", nargs="*", default=[".xlsx", ".xlsm"],
                        help="File extensions to include (e.g., .xlsx .xlsm).")

    args = parser.parse_args()

    try:
        processor = BatchProcessor(
            input_dir=args.input_dir,
            output_subdir=args.output_subdir,
            keep_all_columns=args.keep_all_columns,
            verbose=args.verbose
        )
        summaries = processor.process(include_patterns=args.patterns)

        # Final summary
        print("\n" + "="*50)
        print("BATCH PROCESSING SUMMARY")
        print("="*50)
        if not summaries:
            print("No files were processed.")
        else:
            for s in summaries:
                print(f"Input:  {s['input']}")
                print(f"Output: {s['output']}")
                for sh in s["sheets"]:
                    print(f"  - {sh['sheet']}: {sh['rows']}×{sh['cols']} "
                          f"(row_levels={sh['row_levels']}, col_levels={sh['col_levels']})")
            print(f"\n✅ Processed {len(summaries)} file(s). Outputs in '{processor.out_dir}'.")

        # Optionally save summary as JSON
        summary_file = processor.out_dir / "processing_summary.json"
        with open(summary_file, "w", encoding="utf-8") as f:
            json.dump(summaries, f, indent=2)
        logger.info(f"Summary saved to {summary_file}")

    except Exception as e:
        logger.error(f"Error during processing: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()