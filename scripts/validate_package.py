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


def require_all_text(path: Path, needles: tuple[str, ...], errors: list[str]) -> None:
    for needle in needles:
        require_text(path, needle, errors)


def section_text(path: Path, heading: str, errors: list[str]) -> str:
    if not path.is_file():
        errors.append(f"Missing file: {path.relative_to(ROOT)}")
        return ""
    text = path.read_text(encoding="utf-8")
    match = re.search(
        rf"^## {re.escape(heading)}\n(.*?)(?=^## |\Z)",
        text,
        re.DOTALL | re.MULTILINE,
    )
    if not match:
        errors.append(f"{path.relative_to(ROOT)} is missing section '## {heading}'")
        return ""
    return match.group(1)


def require_synced_section(
    path_a: Path, path_b: Path, heading: str, errors: list[str]
) -> None:
    """Duplicated contract sections must stay word-identical across skills."""
    text_a = section_text(path_a, heading, errors)
    text_b = section_text(path_b, heading, errors)
    if text_a and text_b and " ".join(text_a.split()) != " ".join(text_b.split()):
        errors.append(
            f"Section '## {heading}' has drifted between "
            f"{path_a.relative_to(ROOT)} and {path_b.relative_to(ROOT)}"
        )


def validate_cross_skill_contracts(errors: list[str]) -> None:
    controller = SKILLS_ROOT / "concept-strategy-controller"
    collector = SKILLS_ROOT / "web-evidence-collector"
    summary = SKILLS_ROOT / "evidence-summary-analysis"
    insight = SKILLS_ROOT / "insight-strategy"

    research_configuration = (
        "Primary Research Lens",
        "Supporting Research Lens",
        "Delivery Mode",
    )
    for path in (
        controller / "references" / "startup-packet.md",
        controller / "references" / "dossier-contract.md",
        collector / "references" / "09-output-template.md",
        summary / "SKILL.md",
    ):
        require_all_text(path, research_configuration, errors)

    collector_traceability_fields = (
        "Evidence ID",
        "Source type",
        "Source name",
        "Date",
        "URL or citation",
        "Raw quote",
        "Observation",
        "Summary",
        "Topic tag",
        "Audience",
        "Confidence",
        "Brand hard data status",
        "Shard ID",
        "Shard source scope",
        "Merged from evidence IDs",
    )
    require_all_text(
        summary / "references" / "01-evidence-pool-schema.md",
        collector_traceability_fields,
        errors,
    )
    require_all_text(
        insight / "assets" / "templates" / "input-package-template.md",
        ("Evidence ID", "Raw quote", "Observation", "Confidence"),
        errors,
    )
    require_all_text(
        insight / "assets" / "templates" / "concept-record-template.md",
        (
            "Concept name",
            "One-line concept",
            "Audience role",
            "Expression territory",
            "Risk",
            "Confidence",
            "Roof",
            "Pillar",
            "Foundation",
            "Proof gaps",
        ),
        errors,
    )
    require_all_text(
        insight / "assets" / "templates" / "idea-platform-record-template.md",
        (
            "Idea Platform Statement",
            "Statement",
            "Cultural Tension",
            "Cultural tension answered",
            "Brand Truth",
            "Brand truth used",
            "Proof Edge",
            "Why the brand can own it",
            "Emotional charge",
            "Strategic implications",
            "Risks / weak assumptions",
            "Validation needed",
        ),
        errors,
    )

    dossier_sections = (
        "## 6. Insight Strategy",
        "## 7. Idea Platform Records",
        "## 8. Concept Records",
    )
    require_all_text(
        controller / "references" / "dossier-contract.md",
        dossier_sections,
        errors,
    )
    require_all_text(
        controller / "references" / "dossier-contract.md",
        (
            "Concept Package Decision",
            "Recommended Concept",
            "Alternative Concepts",
            "Concept Comparison",
        ),
        errors,
    )
    require_all_text(
        insight / "assets" / "templates" / "final-strategy-report-template.md",
        dossier_sections,
        errors,
    )
    require_all_text(
        insight / "references" / "08-final-report-template.md",
        dossier_sections,
        errors,
    )
    require_text(
        controller / "SKILL.md",
        "`insight-strategy` 拥有洞察策略、Idea Platform、Concept Package 与 Message House 的专业推导。",
        errors,
    )

    # The Evidence Pool schema is intentionally duplicated in the collector and
    # summary skills so each loads standalone; these blocks must never drift.
    for heading in ("Allowed Values", "Confidence Rules"):
        require_synced_section(
            collector / "references" / "04-evidence-pool-contract.md",
            summary / "references" / "01-evidence-pool-schema.md",
            heading,
            errors,
        )

    # Frontstage strip names are a display contract between summary and controller.
    frontstage_strips = (
        "来源覆盖内容条",
        "强证据模式内容条",
        "品牌硬信息内容条",
        "证据缺口内容条",
        "进入策略判断内容条",
    )
    require_all_text(controller / "SKILL.md", frontstage_strips, errors)
    require_all_text(summary / "SKILL.md", frontstage_strips, errors)

    # startup-packet.md points at this canonical first-response text block.
    require_text(
        controller / "SKILL.md",
        "你可以随时输入阶段指令来单独深入讨论",
        errors,
    )

    # Concept frontstage fixed output order now lives in stage-playbooks.md.
    require_all_text(
        controller / "references" / "stage-playbooks.md",
        (
            "Concept name",
            "One-line concept",
            "Audience role",
            "Expression territory",
            "Risk",
            "Confidence",
            "Roof",
            "Pillars",
            "Foundation",
            "Proof gaps",
        ),
        errors,
    )


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
    else:
        description = description_match.group(1).strip()
        if len(description) > 1024:
            errors.append(
                f"Skill description exceeds 1024 characters ({len(description)}): "
                f"{skill_md.relative_to(ROOT)}"
            )
        if not re.search(r"[一-鿿]", description):
            warnings.append(
                f"{skill_md.relative_to(ROOT)} description has no Chinese trigger "
                "terms; Chinese-first users may fail to trigger this skill."
            )

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
    byte_count = len(text.encode("utf-8"))
    if byte_count > 24_000:
        warnings.append(
            f"{skill_md.relative_to(ROOT)} is {byte_count} bytes; the whole body "
            "loads on every trigger - move stage detail into references/."
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

    validate_cross_skill_contracts(errors)

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
