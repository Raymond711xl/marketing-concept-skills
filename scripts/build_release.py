#!/usr/bin/env python3
"""Build a clean, downloadable plugin ZIP and SHA-256 checksum."""

from __future__ import annotations

import hashlib
import json
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT / "plugins" / "marketing-concept-skill"
DIST = ROOT / "dist"
EXCLUDED_NAMES = {".DS_Store", "__pycache__"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo"}


def should_include(path: Path) -> bool:
    if any(part in EXCLUDED_NAMES for part in path.parts):
        return False
    return path.suffix not in EXCLUDED_SUFFIXES


def main() -> None:
    package = json.loads((ROOT / "skill-package.json").read_text(encoding="utf-8"))
    version = package["version"]
    DIST.mkdir(parents=True, exist_ok=True)

    archive = DIST / f"marketing-concept-skills-{version}.zip"
    checksum = DIST / f"marketing-concept-skills-{version}.sha256"
    for stale in DIST.glob("marketing-concept-skill-*"):
        if stale.is_file():
            stale.unlink()
    if archive.exists():
        archive.unlink()

    bundle_root = Path("marketing-concept-skills")
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as output:
        for path in sorted(PLUGIN_ROOT.rglob("*")):
            if not path.is_file() or not should_include(path.relative_to(PLUGIN_ROOT)):
                continue
            relative = path.relative_to(PLUGIN_ROOT)
            output.write(
                path,
                bundle_root / "plugins" / "marketing-concept-skill" / relative,
            )

        root_files = (
            "README.md",
            "README.en.md",
            "CHANGELOG.md",
            "LICENSE",
            "skill-package.json",
            ".agents/plugins/marketplace.json",
            ".claude-plugin/marketplace.json",
        )
        for relative_name in root_files:
            output.write(ROOT / relative_name, bundle_root / relative_name)

    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    checksum.write_text(f"{digest}  {archive.name}\n", encoding="ascii")
    print(f"Built: {archive}")
    print(f"Checksum: {checksum}")


if __name__ == "__main__":
    main()
