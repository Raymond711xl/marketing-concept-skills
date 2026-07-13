# Stage Playbooks

本文件保存各阶段的详细职责、前台输出要求和硬边界。总控 SKILL.md 只保留速览表；在以下两个时机必须读取本文件中对应阶段的小节：

1. 组装 `Downstream Handoff Packet`、准备把任务交给下层 skill 时。
2. 接收下层返回物、按输出契约验收并做前台压缩时。

## Contents

1. Brief 与问题框定
2. 证据采集
3. 证据摘要
4. 洞察策略
5. Idea Platform
6. Concept 与 Message House（含前台固定输出顺序）

## 1. Brief 与问题框定

由总控 skill 处理。

输出：

- 工作 brief
- 已知事实
- 用户目标
- 当前要判断的问题
- 品牌硬信息状态
- 缺失输入
- 推荐路线

这一阶段要短。它用于启动和定向，不要变成冗长的 AE 项目文档。

## 2. 证据采集

需要新公开资料时使用 `web-evidence-collector`。

要求它保留完整 evidence pool，但前台输出压缩为：

- 证据是否就绪
- 来源覆盖
- 关键 campaign 或竞品链路
- 品牌硬信息候选
- 主要缺口与限制
- 结构化 evidence pool 作为后台资料

采集层不得产出最终洞察、策略、定位、Idea Platform 或 Concept。

## 3. 证据摘要

已有资料但需要清洗、分类、归纳模式时使用 `evidence-summary-analysis`。

摘要层只做证据整理和证据模式，不做人性解释、文化判断或策略判断。它的“模式”是指材料、来源、渠道、话术、视觉、活动机制、PR角度、平台分布等可直接从证据看到的重复结构；不是 `insight-strategy` Level 1 的 insight theme。

要求它区分：

- Fact
- Observation
- Low-level source/material inference
- Unknown

前台输出聚焦：

- 证据准备内容条
- 证据准备简报
- Evidence pattern inventory
- Category summary
- Research Configuration 与 Research Lens Summary
- Strong evidence patterns / weak collection leads
- Evidence gaps
- Strategy Readiness Pack
- Cleaned evidence pool 作为后台资料

摘要层不得产出 insight theme、human truth、cultural tension、最终策略决定、定位、Idea Platform 或 Concept。

## 4. 洞察策略

证据足够进入洞察和策略推导时使用 `insight-strategy` focused pass，并在 Downstream Handoff Packet 中明确 `Task boundary: stop after Level 4`。

必须遵守四层梯子：

```text
Level 1: Fact Layer
Level 2: Motive Inference
Level 3: Cultural Judgment
Level 4: Strategic Decision
```

`insight-strategy` 应消费上游的 `Strategy Readiness Pack`。如果 brand truth、proof edge、品牌行为或竞品差异仍然不足，Level 4 可以继续推导，但必须标记为 provisional，并说明需要回到哪条品牌硬信息采集线或用户确认点。

## 5. Idea Platform

`insight-strategy` 产出足够战略依据后，由 `insight-strategy` focused pass 收束 Idea Platform；总控只负责交接、验收、前台压缩和保存。这里沿用 `insight-strategy` 的 Idea Platform 体系；用户若使用旧称 Big Idea，也按 Idea Platform 处理。

Idea Platform 输出包含：

- Idea Platform statement
- 回应的 cultural tension
- 使用的 brand truth
- proof edge
- 为什么品牌能拥有它
- 情绪强度
- 策略含义
- 风险或薄弱假设
- 进入 Concept 前必须验证的问题

## 6. Concept 与 Message House

核心链路结束于 Concept。

Concept 的专业推导由 `insight-strategy` 完成。总控必须把选定的 Idea Platform Record、相关 Level 1-4 依据、Strategy Readiness Pack、完整证据入口、用户原始 brief 和已确认决定交给它，并接收完整 Concept Package。总控只负责验收、选择性前台压缩、用户决策组织和 dossier 写回，不得另起一套平行 Concept 或 Message House。

后台 dossier 保存一个推荐 Concept、1-2 个有实质差异且有证据支撑的备选 Concept、比较理由和 package-level proof gaps。前台默认只展示推荐 Concept、紧凑 Message House、为什么推荐，以及备选方向的名称与保留理由；用户要求比较时再展开完整备选记录。

Concept 输出包含：

- Concept name
- One-line concept
- Human / cultural tension
- Brand belief
- Audience role
- Proof mechanism
- Expression territory
- 必须保持一致的东西
- 必须避免的东西
- Risk
- Confidence
- Open questions
- Message House：`Roof`、`Pillars`、`Foundation`、`Proof gaps`

Message House 不是额外的执行文案，而是 Concept 的可验证信息结构：

- `Roof`：Concept 对受众成立时最核心的一句话承诺或组织性表达。
- `Pillars`：支撑 Roof 的 2-3 个信息支柱，每个支柱说明其作用与受众意义。
- `Foundation`：让 Pillars 可信的品牌事实、产品/服务证明、品牌行为和证据来源。
- `Proof gaps`：Foundation 尚不能支持、仍待用户确认或补证的主张。

### Concept 前台固定输出顺序

Concept 前台结果必须同时展示 Concept 核心字段和紧凑的 Message House。完整版本写入 dossier；证据不足时保留结构并把相应字段标为 provisional，不用漂亮措辞掩盖 Proof gaps。

使用以下固定顺序输出推荐 Concept，不得用相近字段替代或省略：

1. `Concept name`
2. `One-line concept`
3. `Audience role`
4. `Expression territory`
5. `Risk`
6. `Confidence`
7. `Roof`
8. `Pillars`
9. `Foundation`
10. `Proof gaps`

只有这十项都已明确显示，Concept 前台结果才算完成。Human / cultural tension、Brand belief、Proof mechanism、must stay consistent、must avoid 和 open questions 继续保留为扩展字段。

除非用户要求继续，不自动写 campaign copy、KV prompt、脚本、设计系统或 deck 页面。
