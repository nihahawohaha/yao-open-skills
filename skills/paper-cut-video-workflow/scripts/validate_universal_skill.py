#!/usr/bin/env python3

import json
import re
import sys
from pathlib import Path


REQUIRED_PATHS = (
    "SKILL.md",
    "manifest.json",
    "references/platform-compatibility.md",
    "adapters/cursor/paper-cut-video-workflow.mdc",
    "adapters/generic/AGENTS.md",
    "scripts/plan_scene_durations.py",
    "scripts/make_delivery_manifest.py",
)


def fail(message):
    print("ERROR: " + message)
    return 1


def main():
    root = Path(__file__).resolve().parents[1]
    missing = [path for path in REQUIRED_PATHS if not (root / path).is_file()]
    if missing:
        return fail("missing required files: " + ", ".join(missing))

    skill_text = (root / "SKILL.md").read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\s*\n(.*?)\n---\s*\n", skill_text, re.DOTALL)
    if not frontmatter:
        return fail("SKILL.md has no valid YAML frontmatter block")

    metadata = frontmatter.group(1)
    if not re.search(r"^name:\s*paper-cut-video-workflow\s*$", metadata, re.MULTILINE):
        return fail("SKILL.md name does not match the folder")
    if not re.search(r"^description:\s*\S+", metadata, re.MULTILINE):
        return fail("SKILL.md description is missing")

    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    expected = {"codex", "claude-code", "trae", "cursor", "generic"}
    actual = set(manifest.get("platforms", []))
    if actual != expected:
        return fail("manifest platforms do not match the supported set")

    local_paths = re.findall(r"`((?:references|assets|scripts|adapters)/[^`]+)`", skill_text)
    broken = sorted(set(path for path in local_paths if not (root / path).exists()))
    if broken:
        return fail("SKILL.md contains broken relative paths: " + ", ".join(broken))

    forbidden_patterns = (
        r"[A-Za-z]:\\Users\\",
        r"ghp" + r"_[A-Za-z0-9]+",
        r"sk" + r"-[A-Za-z0-9]{16,}",
        r"BEGIN (?:RSA |OPENSSH )?PRIVATE KEY",
    )
    public_files = [path for path in root.rglob("*") if path.is_file()]
    leaks = []
    for path in public_files:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if any(re.search(pattern, text) for pattern in forbidden_patterns):
            leaks.append(str(path.relative_to(root)))
    if leaks:
        return fail("possible private data found in: " + ", ".join(sorted(leaks)))

    print("Universal skill validation passed for 5 platform targets.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
