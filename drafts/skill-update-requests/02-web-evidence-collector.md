# Web Evidence Collector 修改需求

将下面内容作为该 Skill 对话的修改任务。只修改 `web-evidence-collector`，不要改其他 Skill、插件 manifest、README 或版本号。

正式路径：`plugins/marketing-concept-skill/skills/web-evidence-collector/`

## 目标

让采集结果在 Codex 与 Claude Code 中都能稳定执行、清楚降级，并通过统一 Evidence Pool 无损交给证据摘要。

## 必须修改

1. 固化 Evidence Pool 核心字段。
   - 每条证据必须保留稳定的 `Evidence ID`。
   - 同时保留 `Raw quote`、`Observation`、`Summary`、来源、日期、URL/citation、Audience 和 Confidence。
   - 视觉证据不能因为没有原话而丢失 `Observation`。
2. 对齐下游 handoff。
   - 明确哪些字段不得被 `evidence-summary-analysis` 删除或改名。
   - `Brand Hard Data Track` 中的每个候选都带来源 Evidence ID、状态和 `Needs user confirmation`。
3. 增加能力探测与降级。
   - 有 web search、浏览器、connector 或授权导出时按优先级使用。
   - 没有联网或平台能力时，输出 source plan、缺口和用户需提供的材料，不伪造已完成采集。
4. 保持跨平台的工具抽象。
   - 不把流程绑定到某个专属工具名。
   - 平台受限时保留短线索、链接和 restriction，不绕过登录、付费墙或反爬。
5. 校准 subagent 模式。
   - 只有宽范围任务才建议，并继续要求用户确认。
   - subagent 不可用时按同一 shard plan 顺序采集。
   - 合并时去重并保留各 shard 的来源范围。
6. 增加最小回归样例或检查清单。
   - 覆盖公开官方资料、动态社媒受限、视觉观察、品牌硬信息和无联网降级。

## 边界

- 不产出 human truth、cultural tension、定位、Idea Platform 或 Concept。
- 不把品牌自述当作消费者真相。
- 不因前台压缩而丢失后台 Evidence Pool。

## 验收

- 输出可直接交给 `evidence-summary-analysis`，Evidence ID 和 Observation 不丢失。
- 无联网能力时明确标记未采集，而不是给出模拟证据。
- 运行 Skill validator，并报告修改文件与测试结果。
