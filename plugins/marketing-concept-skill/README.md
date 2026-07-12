# 慢策 | Marketing Concept Skill

写方案的前半程，有 AI 陪你慢慢跑。

Version: 0.8.9
Status: Draft / Alpha
License: MIT

这是慢策的可安装插件目录，包含四个协作 Skill：

- `concept-strategy-controller`
- `web-evidence-collector`
- `evidence-summary-analysis`
- `insight-strategy`

默认入口是 `concept-strategy-controller`。完整使用说明、安装方法和版本记录见项目主页：

[Marketing Concept Skills](https://github.com/Raymond711xl/marketing-concept-skills)

本地加载：

```bash
# 在包含 .agents/plugins/marketplace.json 的仓库根目录添加 Codex marketplace
codex plugin marketplace add /absolute/path/to/marketing-concept-skills
codex plugin add marketing-concept-skill@man-ce

# 直接临时加载 Claude Code 插件
claude --plugin-dir /absolute/path/to/marketing-concept-skills/plugins/marketing-concept-skill
```

调用总控：

```text
Codex: $concept-strategy-controller
Claude Code: /marketing-concept-skill:concept-strategy-controller
```
