#!/usr/bin/env python3
"""Estimate shot durations from a CSV shot list.

Input CSV should contain at least: shot,narration
Output CSV adds estimated_duration and suggested_timecode columns.
"""

import argparse
import csv
import math
from pathlib import Path


def estimate_seconds(text, chars_per_second, min_seconds):
    cleaned = "".join(ch for ch in text.strip() if not ch.isspace())
    if not cleaned:
        return min_seconds
    return max(min_seconds, len(cleaned) / chars_per_second)


def format_time(seconds):
    minutes = int(seconds // 60)
    rest = seconds - minutes * 60
    return f"{minutes:02d}:{rest:04.1f}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("output_csv", type=Path)
    parser.add_argument("--chars-per-second", type=float, default=4.8)
    parser.add_argument("--min-shot-seconds", type=float, default=2.2)
    parser.add_argument("--padding-seconds", type=float, default=0.35)
    args = parser.parse_args()

    with args.input_csv.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    if not rows:
        raise SystemExit("input CSV has no rows")

    fieldnames = list(rows[0].keys())
    for name in ["estimated_duration", "suggested_timecode"]:
        if name not in fieldnames:
            fieldnames.append(name)

    cursor = 0.0
    for row in rows:
        narration = row.get("narration", "")
        duration = estimate_seconds(
            narration,
            args.chars_per_second,
            args.min_shot_seconds,
        )
        duration = math.ceil((duration + args.padding_seconds) * 10) / 10
        start = cursor
        end = cursor + duration
        row["estimated_duration"] = f"{duration:.1f}"
        row["suggested_timecode"] = f"{format_time(start)}-{format_time(end)}"
        cursor = end

    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.output_csv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {args.output_csv} ({cursor:.1f}s total)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
