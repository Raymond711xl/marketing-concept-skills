#!/usr/bin/env python3
"""Validate the portable Marketing Concept Skill package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKAGE_META = ROOT / "skill-package.json"
PLUGIN_ROOT = ROOT / "plugins" / "marketing-concept-skill"
SKILLS_ROOT = PLUGIN_ROOT / "skills"
SKILL_NAMES = (
    "concept-strategy-controller",
    "web-evidence-collector",
    "evidence-summary-analysis",
    "insight-strategy",
)


def load_json(path: Path, errors: list[str]) -> dict:
    if not path.is_file():
        errors.append(f"Missing JSON file: {path.relative_to(ROOT)}")
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")
        return {}
    if not isinstance(value, dict):
        errors.append(f"JSON root must be an object: {path.relative_to(ROOT)}")
        return {}
    return value


def require_text(path: Path, needle: str, errors: list[str]) -> None:
    if not path.is_file():
        errors.append(f"Missing file: {path.relative_to(ROOT)}")
        return
    if needle not in path.read_text(encoding="utf-8"):
        errors.append(f"{path.relative_to(ROOT)} does not contain {needle!r}")


def validate_skill(skill_root: Path, errors: list[str], warnings: list[str]) -> None:
    skill_md = skill_root / "SKILL.md"
    if not skill_md.is_file():
        errors.append(f"Missing SKILL.md: {skill_root.relative_to(ROOT)}")
        return

    text = skill_md.read_text(encoding="utf-8")
    frontmatter = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not frontmatter:
        errors.append(f"Invalid frontmatter: {skill_md.relative_to(ROOT)}")
        return

    header = frontmatter.group(1)
    name_match = re.search(r"^name:\s*([^\n]+)$", header, re.MULTILINE)
    description_match = re.search(r"^description:\s*([^\n]+)$", header, re.MULTILINE)
    expected_name = skill_root.name
    if not name_match or name_match.group(1).strip().strip('"\'') != expected_name:
        errors.append(f"Skill name does not match folder: {skill_md.relative_to(ROOT)}")
    if not description_match or not description_match.group(1).strip():
        errors.append(f"Missing skill description: {skill_md.relative_to(ROOT)}")

    if not (skill_root / "agents" / "openai.yaml").is_file():
        errors.append(f"Missing agents/openai.yaml: {skill_root.relative_to(ROOT)}")

    resource_pattern = re.compile(r"`((?:references|assets|scripts|examples)/[^`]+)`")
    for resource in sorted(set(resource_pattern.findall(text))):
        if not (skill_root / resource).exists():
            errors.append(
                f"Missing referenced resource {resource!r} in {skill_root.relative_to(ROOT)}"
            )

    line_count = len(text.splitlines())
    if line_count >= 500:
        warnings.append(
            f"{skill_md.relative_to(ROOT)} has {line_count} lines; move detail to references."
        )


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    package = load_json(PACKAGE_META, errors)
    version = package.get("version")
    if not isinstance(version, str) or not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append("skill-package.json version must be strict semver")
        version = "unknown"

    codex_manifest = load_json(PLUGIN_ROOT / ".codex-plugin" / "plugin.json", errors)
    claude_manifest = load_json(PLUGIN_ROOT / ".claude-plugin" / "plugin.json", errors)
    codex_marketplace = load_json(ROOT / ".agents" / "plugins" / "marketplace.json", errors)
    claude_marketplace = load_json(ROOT / ".claude-plugin" / "marketplace.json", errors)

    for label, manifest in (
        ("Codex manifest", codex_manifest),
        ("Claude manifest", claude_manifest),
    ):
        if manifest.get("name") != "marketing-concept-skill":
            errors.append(f"{label} has the wrong plugin name")
        if manifest.get("version") != version:
            errors.append(f"{label} version does not match {version}")
        if manifest.get("skills", "./skills/").rstrip("/") != "./skills":
            errors.append(f"{label} must point skills to ./skills/")

    codex_plugins = codex_marketplace.get("plugins", [])
    if not codex_plugins or codex_plugins[0].get("source", {}).get("path") != "./plugins/marketing-concept-skill":
        errors.append("Codex marketplace does not point to the packaged plugin")

    claude_plugins = claude_marketplace.get("plugins", [])
    if not claude_plugins or claude_plugins[0].get("source") != "./plugins/marketing-concept-skill":
        errors.append("Claude marketplace does not point to the packaged plugin")

    require_text(ROOT / "README.md", f"Version: {version}", errors)
    require_text(ROOT / "README.en.md", f"Version: {version}", errors)
    require_text(ROOT / "AGENTS.md", f"Version: `{version}`", errors)
    require_text(ROOT / "CHANGELOG.md", f"## {version}", errors)
    require_text(PLUGIN_ROOT / "README.md", f"Version: {version}", errors)

    if not (PLUGIN_ROOT / "LICENSE").is_file():
        errors.append("Installable plugin is missing LICENSE")

    forbidden_names = {
        "TODO-backlog.md",
        "web-evidence-collector_中文审阅稿.md",
        "evidence-summary-analysis-中文说明.md",
    }
    for path in PLUGIN_ROOT.rglob("*"):
        if path.name in forbidden_names:
            errors.append(f"Internal draft leaked into plugin: {path.relative_to(ROOT)}")

    for skill_name in SKILL_NAMES:
        skill_root = SKILLS_ROOT / skill_name
        if not skill_root.is_dir():
            errors.append(f"Missing packaged skill: {skill_name}")
            continue
        validate_skill(skill_root, errors, warnings)

    if errors:
        print("Package validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Package validation passed: marketing-concept-skill {version}")
    for warning in warnings:
        print(f"Warning: {warning}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
