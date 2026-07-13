#!/usr/bin/env python3
"""Smoke-test no-dependency formats, bundled lexicons, and path handling."""

from __future__ import annotations

import csv
import subprocess
import sys
import tempfile
from pathlib import Path


CORE_FIELDS = [
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
]


def first_evidence_block(text: str) -> str:
    block = text.split("### Evidence RAW-001", 1)[1]
    return block.split("\n### Evidence ", 1)[0]


def assert_v1_core(block: str) -> None:
    fields = [
        line[2:].split(":", 1)[0]
        for line in block.splitlines()
        if line.startswith("- ")
    ]
    assert fields[: len(CORE_FIELDS)] == CORE_FIELDS
    assert "- Source type: social" in block
    assert "- Observation: not applicable - text-only source" in block
    assert "Audience / segment:" not in block
    assert "Insight lens:" not in block
    assert "Matched keywords:" not in block


def run_adapter(script: Path, cwd: Path, input_path: Path, output_path: Path) -> str:
    subprocess.check_call(
        [
            sys.executable,
            str(script),
            str(input_path),
            str(output_path),
            "--source",
            "小红书",
            "--brand",
            "Sample Brand",
            "--tokenizer",
            "stdlib",
        ],
        cwd=cwd,
    )
    return output_path.read_text(encoding="utf-8")


def main() -> None:
    script = Path(__file__).resolve().parent / "prepare_raw_evidence.py"
    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)

        csv_input = tmpdir / "sample.csv"
        with csv_input.open("w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["评论", "点赞数"])
            writer.writeheader()
            writer.writerow(
                {
                    "评论": "这种松弛感让我放心，也想休息，不想再被催。",
                    "点赞数": "12",
                }
            )
            writer.writerow(
                {
                    "评论": "这个真的可以闭眼入，终于有安全感。",
                    "点赞数": "8",
                }
            )
        csv_text = run_adapter(script, tmpdir, csv_input, tmpdir / "csv.md")
        assert "Bundled Lexicon Use" in csv_text
        assert "Emotion Marker Scan" in csv_text and "松弛" in csv_text
        assert "Motive Marker Scan" in csv_text and "想休息" in csv_text
        assert "放心 -> 安心" in csv_text
        assert "Platform Slang Scan" in csv_text and "闭眼入" in csv_text
        assert "Evidence ID: RAW-001" in csv_text
        assert "Tokenizer: stdlib fallback" in csv_text
        assert_v1_core(first_evidence_block(csv_text))

        tsv_input = tmpdir / "sample.tsv"
        tsv_input.write_text("text\tlikes\n我想简单一点，也怕踩雷\t3\n", encoding="utf-8")
        tsv_text = run_adapter(script, tmpdir, tsv_input, tmpdir / "tsv.md")
        assert "Evidence Pool Draft" in tsv_text and "怕踩雷" in tsv_text

        txt_input = tmpdir / "sample.txt"
        txt_input.write_text("第一条原始评论让我安心\n第二条原始评论有压力\n", encoding="utf-8")
        txt_text = run_adapter(script, tmpdir, txt_input, tmpdir / "txt.md")
        assert "Raw rows: 2" in txt_text and "Evidence ID: RAW-002" in txt_text

        xls_input = tmpdir / "legacy.xls"
        xls_input.write_bytes(b"legacy-placeholder")
        xls_result = subprocess.run(
            [sys.executable, str(script), str(xls_input), str(tmpdir / "xls.md")],
            cwd=tmpdir,
            capture_output=True,
            text=True,
            check=False,
        )
        assert xls_result.returncode != 0
        assert "not supported by openpyxl" in (xls_result.stdout + xls_result.stderr)

    print("smoke test passed: CSV/TSV/TXT, Evidence Pool v1, bundled lexicons, cwd independence, .xls guard")


if __name__ == "__main__":
    main()
