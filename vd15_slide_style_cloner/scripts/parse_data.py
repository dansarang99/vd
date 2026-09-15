#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Insight Extractor (CSV & Tabular Data)
Quickly extracts key statistical metrics, percentages, rankings, and trends from CSV files
so the agent can ground Metric 4-Cards, Quadrants, and Charts with authentic numbers.
"""

import sys
import os
import csv
import json
import argparse
from typing import Dict, Any, List

def analyze_csv(file_path: str, max_rows: int = 1000) -> Dict[str, Any]:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found: {file_path}")

    encodings = ["utf-8", "cp949", "euc-kr", "utf-8-sig"]
    rows = []
    headers = []
    selected_enc = None

    for enc in encodings:
        try:
            with open(file_path, "r", encoding=enc) as f:
                reader = csv.reader(f)
                headers = next(reader, [])
                headers = [h.strip() for h in headers if h.strip()]
                for i, row in enumerate(reader):
                    if i >= max_rows:
                        break
                    if any(row):
                        rows.append(row)
                selected_enc = enc
                break
        except (UnicodeDecodeError, Exception):
            continue

    if not selected_enc:
        raise ValueError(f"Unable to read CSV with common encodings: {file_path}")

    total_rows = len(rows)
    col_summaries: Dict[str, Any] = {}

    for col_idx, col_name in enumerate(headers):
        values = []
        numeric_values = []
        for r in rows:
            if col_idx < len(r):
                val = r[col_idx].strip()
                if val:
                    values.append(val)
                    clean_val = val.replace(",", "").replace("%", "")
                    try:
                        num = float(clean_val)
                        numeric_values.append(num)
                    except ValueError:
                        pass

        if numeric_values and len(numeric_values) >= len(values) * 0.7:
            # Numeric column
            numeric_values.sort()
            col_summaries[col_name] = {
                "type": "numeric",
                "sample_count": len(numeric_values),
                "min": round(numeric_values[0], 2),
                "max": round(numeric_values[-1], 2),
                "avg": round(sum(numeric_values) / len(numeric_values), 2),
                "median": round(numeric_values[len(numeric_values) // 2], 2),
                "latest_or_prominent": round(numeric_values[-1], 2)
            }
        else:
            # Categorical column
            freq: Dict[str, int] = {}
            for v in values:
                freq[v] = freq.get(v, 0) + 1
            sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
            col_summaries[col_name] = {
                "type": "categorical",
                "unique_values": len(freq),
                "top_5": [{"value": k, "count": v, "share": f"{round(v / max(1, len(values)) * 100, 1)}%"} for k, v in sorted_freq[:5]]
            }

    return {
        "file_name": os.path.basename(file_path),
        "encoding": selected_enc,
        "total_rows_sampled": total_rows,
        "columns": headers,
        "column_summaries": col_summaries
    }

def main():
    parser = argparse.ArgumentParser(description="Extract statistical insights and metrics from tabular CSV data.")
    parser.add_argument("-i", "--input", required=True, help="Path to CSV file.")
    parser.add_argument("-o", "--output", default=None, help="Path to save output JSON (optional).")

    args = parser.parse_args()
    res = analyze_csv(args.input)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(res, f, ensure_ascii=False, indent=2)
        print(f"[+] Data summary saved to: {args.output}")
    else:
        print(json.dumps(res, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
