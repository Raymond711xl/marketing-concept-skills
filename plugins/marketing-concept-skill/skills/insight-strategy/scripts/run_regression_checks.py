#!/usr/bin/env python3
"""Run development-only contract regressions for Insight Strategy."""

from __future__ import annotations

import re
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
EXAMPLES_DIR = SKILL_DIR / "examples"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require(text: str, *needles: str) -> None:
    missing = [needle for needle in needles if needle not in text]
    if missing:
        raise AssertionError(f"Missing required content: {missing}")


def concept_block(text: str, concept_id: str, next_id: str | None) -> str:
    start_marker = f"### Concept {concept_id}"
    start = text.index(start_marker)
    if next_id:
        end = text.index(f"### Concept {next_id}", start)
    else:
        end_marker = "### Comparison And Status"
        end = text.index(end_marker, start)
    return text[start:end]


def check_message_house(block: str) -> None:
    require(
        block,
        "#### Message House",
        "- Roof:",
        "- Roof Evidence IDs:",
        "| Pillar 1 |",
        "| Pillar 2 |",
        "| Foundation item |",
        "| F1 |",
        "- Proof gaps:",
        "- Risks:",
        "Concept status: **Provisional**",
    )
    evidence_id = re.compile(r"\b(?:E\d+|BF-\d+|CP-\d+|BR-\d+|RAW-\d+)\b")
    pillar_rows = [line for line in block.splitlines() if re.match(r"\| Pillar [123]", line)]
    if len(pillar_rows) not in {2, 3}:
        raise AssertionError(f"Expected 2-3 Pillars, found {len(pillar_rows)}")
    for row in pillar_rows:
        if not evidence_id.search(row):
            raise AssertionError(f"Pillar lacks Evidence ID: {row}")
    foundation_rows = [line for line in block.splitlines() if re.match(r"\| F\d+ \|", line)]
    if not foundation_rows:
        raise AssertionError("Message House has no Foundation rows")
    for row in foundation_rows:
        cells = [cell.strip() for cell in row.strip("|").split("|")]
        if len(cells) < 5 or not cells[1] or not cells[2]:
            raise AssertionError(f"Foundation lacks proof type or exact fact: {row}")
        if not evidence_id.search(cells[3]):
            raise AssertionError(f"Foundation lacks Evidence ID: {row}")


def check_zero_material() -> None:
    text = read(EXAMPLES_DIR / "regression-zero-material-unavailable.md")
    require(
        text,
        "Input Readiness: Unavailable",
        "Overall status: Unavailable",
        "Decision: stop before Level 1",
        "do not generate themes",
    )
    if "- Overall status: Final" in text or "- Overall status: Provisional" in text:
        raise AssertionError("Zero-material case must not produce a strategy status")


def check_thin_evidence() -> None:
    text = read(EXAMPLES_DIR / "regression-thin-evidence-provisional.md")
    require(
        text,
        "Input Readiness: Partial",
        "Overall status: Provisional",
        "Recommended Concept status: Provisional",
        "Alternative Concept status: Provisional",
        "Rollback path: evidence and competitor",
        "Evidence ID E001",
        "Brand fact BF-001",
    )
    if "- Overall status: Final" in text:
        raise AssertionError("Thin-evidence case incorrectly reached Final")


def check_golden_end_to_end() -> None:
    text = read(EXAMPLES_DIR / "golden-case-01-yubai-skincare.md")
    require(
        text,
        "## Level 1",
        "## Level 2",
        "## Level 3",
        "## Level 4",
        "### Candidate Idea Platforms",
        "## Concept Package",
        "### Package Decision",
        "Package role: Recommended",
        "Package role: Alternative",
        "Overall Concept Package status: **Provisional**",
    )
    check_message_house(concept_block(text, "C-01", "C-02"))
    check_message_house(concept_block(text, "C-02", "C-03"))
    check_message_house(concept_block(text, "C-03", None))


def check_model_route_coverage() -> None:
    library = read(SKILL_DIR / "references" / "10-strategy-models-library.md")
    template = read(SKILL_DIR / "assets" / "templates" / "idea-platform-record-template.md")
    route_ids = set(re.findall(r"^\| `([^`]+)` \|", library, flags=re.MULTILINE))
    if not route_ids:
        raise AssertionError("No published strategy route IDs found")
    missing = sorted(route_id for route_id in route_ids if f"`{route_id}`" not in template)
    if missing:
        raise AssertionError(f"Idea Platform template misses route IDs: {missing}")


def check_dossier_contract_shape() -> None:
    template = read(SKILL_DIR / "assets" / "templates" / "final-strategy-report-template.md")
    require(
        template,
        "## 5. Insight Strategy",
        "## 6. Idea Platform Records",
        "## 7. Concept Records",
        "one recommended Concept",
        "alternative Concepts",
        "Evidence IDs for every Roof, Pillar, and Foundation item",
    )


def main() -> None:
    checks = [
        ("zero-material-unavailable", check_zero_material),
        ("thin-evidence-provisional", check_thin_evidence),
        ("end-to-end-level1-to-concept", check_golden_end_to_end),
        ("strategy-model-route-coverage", check_model_route_coverage),
        ("dossier-writeback-shape", check_dossier_contract_shape),
    ]
    for name, check in checks:
        check()
        print(f"PASS {name}")
    print(f"{len(checks)} regression checks passed")


if __name__ == "__main__":
    main()
