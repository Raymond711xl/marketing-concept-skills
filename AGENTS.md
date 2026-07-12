# Agent Working Guide

This repository is the `慢策 / Marketing Concept Skill` bundle. It contains multiple Codex skills that work together as one package.

## Package Identity

- Chinese name: `慢策`
- English/package name: `Marketing Concept Skill`
- Slogan: `写方案的前半程，有 AI 陪你慢慢跑。`
- Version: `0.8.9`
- Status: Draft / Alpha
- License: MIT

## Skill Bundle Structure

- `plugins/marketing-concept-skill/`: installable Codex and Claude plugin root.
- `plugins/marketing-concept-skill/skills/concept-strategy-controller/`: entry controller skill.
- `plugins/marketing-concept-skill/skills/web-evidence-collector/`: evidence collection skill.
- `plugins/marketing-concept-skill/skills/evidence-summary-analysis/`: evidence normalization and summary skill.
- `plugins/marketing-concept-skill/skills/insight-strategy/`: insight strategy and Idea Platform skill.
- Root-level skill names are compatibility symlinks for existing local conversations.
- `drafts/`: internal review notes and per-skill update requests; excluded from the installable plugin.
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
- Keep Codex packaging metadata in `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json`.
- Keep Claude Code packaging metadata in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`.
- Treat `plugins/marketing-concept-skill/skills/` as the single source of truth. Do not create duplicate skill copies.

## Validation

After changing any skill folder or packaging file, run:

```bash
python3 scripts/validate_package.py
python3 plugins/marketing-concept-skill/skills/insight-strategy/scripts/smoke_test_prepare_raw_evidence.py
python3 scripts/build_release.py
```

When Codex and Claude CLIs are available, also run their plugin validators before release.

## Release Notes

Before a public release:

- Confirm license and copyright holder.
- Keep draft review files outside `plugins/marketing-concept-skill/`.
- Add real project examples.
- Validate migration metadata for the target platform.
- Decide whether to extract shared language rules into `shared-references/chinese-working-protocol.md`.
