# Evidence Summary Analysis 修改需求

将下面内容作为该 Skill 对话的修改任务。只修改 `evidence-summary-analysis`，不要改其他 Skill、插件 manifest、README 或版本号。

正式路径：`plugins/marketing-concept-skill/skills/evidence-summary-analysis/`

## 目标

在不进入策略解释的前提下，完成无损清洗、可追溯摘要和紧凑 handoff，同时明显降低 Skill 本体的上下文长度。

## 必须修改

1. 修复 Evidence Pool 字段断点。
   - 输入与 cleaned output 都必须保留 `Evidence ID`。
   - 增加并保留 `Observation`，尤其用于视觉、活动和页面材料。
   - 统一字段命名，不在 Title Case 与 snake_case 之间无说明切换。
2. 强化 Strategy Readiness Pack 的可追溯性。
   - Brand truth candidate、Proof edge、Brand behavior、Competitor distinction 都附 Evidence ID 和 Confidence。
   - 明确 confirmed、reported、inferred、missing。
3. 精简 `SKILL.md`。
   - 将完整 Evidence Pool schema、体量表和长输出模板拆入 `references/`。
   - `SKILL.md` 只保留边界、主流程、选择逻辑、handoff 和 reference map。
   - 目标控制在 300 行左右，至少低于 500 行。
4. 保持 Evidence Pattern 与 Insight Theme 的边界。
   - 只描述材料、来源、渠道、话术、视觉和活动机制的重复结构。
   - 不解释人为什么这样想，不生成 human truth 或 cultural tension。
5. 增加输入适配与回退。
   - 接收 collector 输出、杂乱笔记和结构化 evidence pool。
   - 缺少新资料时只生成 collector task，不自行假装完成外部研究。
6. 增加回归样例。
   - 验证 Evidence ID、Observation、矛盾证据和品牌硬信息在清洗后仍存在。

## 验收

- collector 的核心字段能够无损进入 cleaned evidence pool。
- Strategy Readiness Pack 的每个关键候选能回指来源。
- 快速版仍必须包含可供下游使用的 cleaned evidence pool 或明确文件入口。
- 运行 Skill validator，并报告行数变化、修改文件与测试结果。
