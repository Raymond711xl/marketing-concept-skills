# Agent Working Guide

This repository is the `慢策 / Marketing Concept Skill` bundle. It contains multiple Codex skills that work together as one package.

## Package Identity

- Chinese name: `慢策`
- English/package name: `Marketing Concept Skill`
- Slogan: `写方案的前半程，有 AI 陪你慢慢跑。`
- Version: `0.7.0`
- Status: Draft / Alpha
- License: MIT

## Skill Bundle Structure

- `concept-strategy-controller/`: entry controller skill.
- `web-evidence-collector/`: evidence collection skill.
- `evidence-summary-analysis/`: evidence normalization and summary skill.
- `insight-strategy/`: insight strategy and Idea Platform skill.
- `dossiers/`: exported backstage dossiers for real projects.

## Working Rules For Agents

- Treat this as a skill bundle, not a single standalone skill.
- Keep the default working language Chinese unless the user asks otherwise or specifies an overseas market.
- Preserve English schema labels used for handoff contracts, such as `Evidence Pool`, `Confidence`, `Raw quote`, `Insight Map`, and `Idea Platform Record`.
- Do not use `@` as a stage-control syntax. Use explicit commands such as `进入：证据摘要`, `进入：Idea Platform`, `查看：资料池`, and `继续`.
- The current system ends at Concept. Do not automatically add copywriting, visual design, proposal, or execution behavior unless a new downstream skill is explicitly added.
- Do not bind this bundle to external agency-role skills. Keep this package self-contained.
- Preserve user-provided source wording and evidence trails.
- Keep `web-evidence-collector` and `evidence-summary-analysis` as separate skills, but make the default controller experience run them continuously as one Evidence Preparation stage.
- In Evidence Preparation default mode, show frontstage content strips and an evidence brief box with a dossier link; do not print the full evidence pool unless requested.
- In Evidence Preparation audit mode, stop after the evidence brief and ask the user to confirm, supplement, or name missing evidence before summary.
- Treat brand philosophy, vision, slogan, chronology, founder statements, product proof, service proof, brand behavior, and competitor distinction as Level 4 hard-data leads. If absent from the brief, collect public candidates and mark them as needing user confirmation.
- Do not remove draft review files unless the user explicitly asks to prepare a public release cleanup.

## Editing Rules

- Use `apply_patch` for manual edits.
- Avoid unrelated refactors.
- Keep `README.md` user-facing.
- Keep `AGENTS.md` agent-facing.
- Keep each skill's `SKILL.md` focused on execution behavior.
- Keep UI metadata in `agents/openai.yaml`.
- Keep package metadata in `skill-package.json`.

## Validation

After changing any skill folder, run:

```bash
python3 /Users/raymond7/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/raymond7/Documents/Vibe一下/concept-strategy-controller
python3 /Users/raymond7/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/raymond7/Documents/Vibe一下/web-evidence-collector
python3 /Users/raymond7/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/raymond7/Documents/Vibe一下/evidence-summary-analysis
python3 /Users/raymond7/.codex/skills/.system/skill-creator/scripts/quick_validate.py /Users/raymond7/Documents/Vibe一下/insight-strategy
```

If only root packaging files changed, still check file consistency manually.

## Release Notes

Before a public release:

- Confirm license and copyright holder.
- Clean or move draft review files.
- Add real project examples.
- Validate migration metadata for the target platform.
- Decide whether to extract shared language rules into `shared-references/chinese-working-protocol.md`.
