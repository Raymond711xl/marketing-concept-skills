#!/usr/bin/env python3
"""Create a tiny CSV and run the optional social listening cleaner."""

from __future__ import annotations

import csv
import subprocess
import sys
import tempfile
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    script = root / "phase1_social_listening_cleaning.py"
    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        sample = tmpdir / "sample.csv"
        output = tmpdir / "out.md"
        with sample.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["评论", "点赞数"])
            writer.writeheader()
            writer.writerow({"评论": "我喜欢这种松弛感，不想一直被效率追着跑", "点赞数": "12"})
            writer.writerow({"评论": "这个品牌让我有安全感，好像被看见了", "点赞数": "8"})
        subprocess.check_call(
            [
                sys.executable,
                str(script),
                str(sample),
                str(output),
                "--source",
                "sample",
                "--brand",
                "Sample Brand",
            ]
        )
        text = output.read_text(encoding="utf-8")
        assert "Evidence Pool Draft" in text
        assert "松弛" in text
    print("smoke test passed")


if __name__ == "__main__":
    main()
