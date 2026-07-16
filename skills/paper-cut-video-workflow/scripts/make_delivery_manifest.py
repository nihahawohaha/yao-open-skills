#!/usr/bin/env python3
"""Create a Markdown delivery manifest for a video project folder."""

import argparse
from datetime import datetime
from pathlib import Path


CATEGORIES = {
    "video": {".mp4", ".mov", ".webm", ".mkv"},
    "audio": {".wav", ".mp3", ".m4a", ".aac", ".flac"},
    "image": {".png", ".jpg", ".jpeg", ".webp"},
    "subtitle": {".srt", ".ass", ".vtt"},
    "project": {".prproj", ".aep", ".blend", ".json", ".csv", ".md"},
}


def category_for(path):
    suffix = path.suffix.lower()
    for category, suffixes in CATEGORIES.items():
        if suffix in suffixes:
            return category
    return "other"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("output_md", type=Path)
    args = parser.parse_args()

    if not args.project_dir.exists():
        raise SystemExit(f"project directory not found: {args.project_dir}")

    files = [
        p for p in args.project_dir.rglob("*")
        if p.is_file() and p.resolve() != args.output_md.resolve()
    ]
    grouped = {}
    for file_path in files:
        grouped.setdefault(category_for(file_path), []).append(file_path)

    lines = [
        "# Delivery Manifest",
        "",
        f"- Project: `{args.project_dir}`",
        f"- Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
    ]

    for category in ["video", "audio", "image", "subtitle", "project", "other"]:
        items = sorted(grouped.get(category, []))
        if not items:
            continue
        lines.append(f"## {category.title()}")
        lines.append("")
        for item in items:
            rel = item.relative_to(args.project_dir)
            size_mb = item.stat().st_size / (1024 * 1024)
            lines.append(f"- `{rel}` ({size_mb:.2f} MB)")
        lines.append("")

    lines.extend([
        "## Manual Checks",
        "",
        "- [ ] Final master video opens and plays fully.",
        "- [ ] Platform export matches required aspect ratio and size.",
        "- [ ] Voice rights and music/SFX license notes are included.",
        "- [ ] Subtitles/text are readable inside safe areas.",
        "- [ ] Prompt log and layered assets are included when required.",
        "",
    ])

    args.output_md.parent.mkdir(parents=True, exist_ok=True)
    args.output_md.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {args.output_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
