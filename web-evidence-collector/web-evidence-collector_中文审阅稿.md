# web-evidence-collector 中文审阅稿

> 说明：本文档只用于人工审阅，不接入 Skill 工作流，不被 `SKILL.md` 引用。正式执行仍以英文 `SKILL.md` 与 `references/` 文件为准。

## 1. Skill 定位

`web-evidence-collector` 是整个品牌、营销、竞品、传播调研体系里的第一层资料收集 Skill。

它的核心任务不是做洞察、策略或创意判断，而是从公开网络资料中收集、核验、整理证据，并输出可交给下游 Skill 使用的结构化 Evidence Pool。

当前体系中的位置是：

```text
concept-strategy-controller
-> web-evidence-collector
-> evidence-summary-analysis
-> insight-strategy
```

它负责把“网上可以找到什么、证据来自哪里、可信度如何、哪些内容互相关联、哪些地方缺失”整理清楚。

它不负责回答“这意味着什么”“品牌应该怎么做”“应该提炼什么洞察”“Idea Platform 是什么”。

## 2. 能力边界

### 2.1 它应该做什么

- 收集品牌、campaign、竞品、事件、市场、传播动作的公开证据。
- 覆盖视觉物料、视频、线下活动、营销动作、PR、社媒线索、报告和市场背景。
- 记录每条证据的来源、链接、发布日期、访问日期、短引用、摘要、类别、可信度和限制。
- 对同一个 campaign 或 message 下的跨渠道物料建立关联关系。
- 标记资料偏科、来源偏科、平台受限、素材缺失等问题。
- 在社媒或动态平台受限时，保留一句可见关键文字、链接、平台信息和用户需自行核验的说明。
- 主动采集品牌硬信息候选，包括品牌理念、愿景、slogan、编年史、创始人表达、产品证明、服务证明、品牌行为和竞品差异。
- 为下游 `evidence-summary-analysis` 和 `insight-strategy` 输出统一的 Evidence Pool。

### 2.2 它不应该做什么

- 不做最终洞察。
- 不做战略判断。
- 不做品牌定位、Idea Platform、传播主张或 campaign 建议。
- 不把品牌官方说法直接当成用户真实反馈。
- 不把搜索结果摘要、聚合页、平台 snippet 当成强事实。
- 不绕过登录、付费墙、验证码、反爬、访问控制或平台条款。
- 不批量复制全文文章、全文报告、完整评论区或完整社媒内容。

## 3. 输入方式

优先由总控 Skill 提供任务包，而不是让 `web-evidence-collector` 再做大量前置提问。

推荐任务包结构如下：

```markdown
## Collection Task Packet

- Target:
- Research purpose:
- Time range:
- Geography / language:
- Priority platforms:
- Excluded platforms / sources:
- Categories:
- Depth: light / standard / deep / exhaustive
- Existing materials:
- Brand hard data leads:
- Downstream destination:
- Subagent mode approved: yes / no / ask user
- Notes:
```

如果总控 Skill 已经给出这些内容，`web-evidence-collector` 应直接进入采集，不重复询问用户。

如果信息不足，只问最多三个必要问题：

1. 调研对象是什么：品牌、campaign、事件、竞品、产品、行业，还是平台行为？
2. 需要哪些资料类别和采集深度：视觉、视频、线下、营销、PR、社媒、报告；轻量、标准、深度，还是穷尽？
3. 用户已有资料和限制是什么：链接、截图、导出文件、官方品牌资料、关键词、平台、地区、时间范围、禁用来源？

如果用户没有提供品牌官方资料，不应阻塞采集。默认把品牌理念、愿景、slogan、编年史、创始人表达、产品/服务证明、品牌行为和竞品差异列为公开资料采集线，并标注为“待用户确认”。

## 4. 调研深度

由于用户通常无法预估网络上到底有多少资料，所以 Skill 应允许用户选择深度，也可以在用户不确定时使用默认值。

| 深度 | 使用场景 | 目标资料量 |
| --- | --- | --- |
| Light | 快速了解、早期探索、小型 brief | 8-15 条证据 |
| Standard | 常规提案、竞品扫描、campaign 输入 | 20-35 条证据 |
| Deep | 策略提案、年度 campaign、品类审计 | 40-70 条证据 |
| Exhaustive | 用户明确需要大型资料库 | 70+ 条，取决于公开资料是否足够 |

默认建议：

```text
若用户没有指定深度，默认采用 Standard：
Visual 5 条、Video 3 条、Offline 3 条、Marketing 5 条、PR 5 条、Social leads 5-10 条。
同时标记缺失类别和平台限制。
```

## 5. 采集类别

### 5.1 Visual Materials

视觉物料不是狭义设计分析，而是所有营销和传播物料的视觉呈现。

包括：

- 海报
- KV
- Campaign landing page
- 包装页
- 产品页
- 社媒视觉
- 活动视觉
- 视频封面
- 案例图
- 截图

重点记录：

- 物料类型
- 来源和 URL
- 截图状态
- 视觉观察：构图、层级、色彩、字体、图像、CTA
- 所属 campaign/message
- 平台/渠道
- 关联证据
- 访问限制

### 5.2 Video

包括：

- TVC
- 视频广告
- Campaign film
- 短视频
- 直播片段
- 产品片
- 品牌片

重点记录：

- 视频标题或资产名称
- 平台和 URL
- 发布时间
- 品牌/campaign
- 可见短口号或关键句
- 观察：开头 hook、叙事结构、产品角色、视觉风格
- 可见数据：播放、点赞、评论、转发、奖项、媒体提及
- 与 PR、社媒、落地页、线下活动的关联

### 5.3 Offline Activation

包括：

- Pop-up
- 展览
- 零售活动
- 装置
- 快闪
- 路演
- 校园/社区活动
- 体验式营销

重点记录：

- 活动名称
- 地点和时间
- 来源和 URL
- 参与机制
- 空间或视觉物料
- 社交分享触发点
- 线上放大证据
- 可见数据：参与人数、发帖量、媒体报道数、排队时间、访客量
- 与视频、PR、营销、社媒的关联

### 5.4 Marketing

包括：

- 新品上市
- 联名
- 促销
- 电商节点
- 会员动作
- 私域动作
- KOL/KOC
- UGC 挑战
- 平台机制
- 转化路径

重点记录：

- 机制
- 渠道
- 利益点或 incentive
- 合作方/达人/平台
- 时间窗口
- 可见数据：销量宣称、优惠券使用、话题量、互动量
- 与视频、线下、PR、视觉物料的关联

### 5.5 PR

包括：

- 新闻稿
- 媒体报道
- 采访
- 公告
- 奖项
- 争议
- 危机声明
- 公共议题回应
- 声誉事件

重点记录：

- 新闻角度
- 发声人/机构
- 媒体来源分布
- 信息框架
- 日期和发布机构
- 短引用
- 公开回应信号
- 风险或争议证据
- 与视频、线下、营销、社媒的关联

### 5.6 Social Leads

包括：

- 小红书
- 微博
- 抖音
- 知乎
- B站
- 公众号
- 贴吧
- TikTok
- Instagram
- YouTube
- X
- Reddit
- 其他公开社媒或论坛

重点记录：

- 平台
- 账号/作者
- 日期
- 一句短关键文字
- 链接
- 可见数据
- 限制说明
- 是否需要用户自行打开平台核验

社媒处理原则：

```text
如果平台无法稳定访问、无法完整截图或不适合引用全文，只保留：
平台 + 链接 + 一句短可见关键文字 + 限制说明 + 用户需核验标记。
```

### 5.7 Reports / Market Context

报告只在对任务范围有帮助时采集。

包括：

- 政府报告
- 行业白皮书
- 年报
- 公开 PDF
- 研报摘要
- 公开数据页

重点记录：

- 报告标题
- 发布机构
- 日期
- URL 或文件页码
- 短引用或关键数据
- 摘要
- 来源等级
- 限制说明

## 6. 来源可信度分层

| 层级 | 来源 | 处理方式 |
| --- | --- | --- |
| L1 | 官网、政府页面、上市公司公告、品牌新闻稿、官方 campaign 页面 | 强事实来源，可直接摘要，保留链接，只使用短引用 |
| L2 | 新闻报道、行业媒体、公开报道、贸易媒体 | 提取事实、观点、发布日期和媒体叙事框架 |
| L3 | 公开 PDF、白皮书、报告摘要、年报、用户有权提供的 deck | 摘要关键点，标注文件或页码，不复制大段内容 |
| L4 | 搜索结果摘要、新闻聚合页、目录页、平台搜索结果 | 只作为线索，尽量追到 L1-L3 或可访问原始页面 |
| L5 | 电商评价、App Store 评论、论坛、公开评论页 | 只使用少量代表性短引用，标注采样限制 |
| L6 | 小红书、微博、抖音、知乎、B站、TikTok、Instagram、YouTube 评论、公众号等动态平台 | 使用公开页面、官方 API、平台导出或用户截图；受限时保留短句、链接和限制 |
| L7 | 付费报告、会员页面、私域社群、登录后内容、私密小组 | 不自动采集，只处理用户授权提供的截图、导出或摘录 |
| L8 | 明确禁止、技术阻断或不允许采集的内容 | 不采集，只保留链接元信息和限制原因 |

## 7. 采集工作流

### 7.1 Scope

先确认工作范围：

- 总控任务包
- 调研对象
- 时间范围和地域
- 资料类别和深度
- 用户已有链接、截图、导出或关键词
- 下游目的地

### 7.2 Query Plan

建立紧凑搜索计划：

- Official：品牌 + campaign/event/product + official / press release / landing page
- News：品牌/campaign + news / launch / PR / campaign / controversy / activation
- Visual：品牌/campaign + poster / KV / landing page / packaging / visual / screenshot
- Video：品牌/campaign + video / TVC / ad / film / short video / YouTube / Bilibili / Douyin
- Offline：品牌/campaign + pop-up / event / exhibition / roadshow / activation / installation
- Marketing：品牌/campaign + collaboration / promo / ecommerce / membership / KOL / UGC
- Social：平台名 + 品牌/campaign + slogan / hashtag / event name

### 7.3 Strong Sources First

优先顺序：

1. 官方来源或 campaign 页面
2. 新闻稿或品牌自有社媒
3. 行业/新闻报道
4. 公开报告或案例文章
5. 视觉、视频、案例库
6. 社媒线索和公开用户痕迹

### 7.4 Capture Evidence Item

每条证据都应保留：

- 来源路径
- URL 或 citation
- 日期和访问日期
- 短引用或观察
- 一句话事实摘要
- 类别和物料类型
- 可信度和来源等级
- 截图状态或平台限制
- 所属 campaign/message
- 关联证据

### 7.5 Verify And De-duplicate

- 去重转载、聚合、重复发布。
- 同一篇文章被多个站转载时，只保留最强或最早来源。
- 同一 campaign 出现在不同渠道或物料形态中时，应保留为不同证据。
- 只有搜索摘要支持的内容，降级为 lead，不当作强事实。

### 7.6 Link Related Evidence

当证据属于同一个 campaign、message、hashtag、活动或上市窗口时，设置共同的 `Campaign / message` 标签，并写入 `Related evidence`。

关联状态分为：

- confirmed：官方或强来源明确连接。
- likely：多项证据高度一致。
- tentative：基于时间、措辞或命名推测，需要下游谨慎使用。
- standalone：暂未发现关联。

## 8. 子代理采集模式

由于品牌整合营销资料经常跨平台、跨主题、跨物料类型，`web-evidence-collector` 支持推荐子代理模式。

### 8.1 什么时候建议启用

满足任一条件即可建议：

- 范围超过三个平台。
- 请求超过三个物料类别。
- 深度为 Deep 或 Exhaustive。
- 目标证据超过 25 条。
- 涉及多个 campaign、竞品、主题或产品线。
- 同时包含社媒、视频、视觉、新闻、报告、官方页面等多种来源。

### 8.2 启用前必须询问

因为子代理模式会增加 token 消耗，所以必须先向用户或总控 Skill 获取明确同意。

建议提示语：

```text
本次采集横跨多个平台/物料类型。我建议启用子代理采集模式，以提高每个平台证据的垂直度和清洁度，但会增加 token 消耗。是否启用？
```

### 8.3 默认拆分方式

优先按平台或来源族拆分，而不是一开始就按分析主题拆分。

| Shard | 范围 | 物料重点 | ID 前缀 |
| --- | --- | --- | --- |
| Official / brand-owned | 官网、campaign 页面、press room、自有账号 | 落地页、官方视觉、上市事实、官方说法 | OFF |
| News / PR / industry media | 新闻、行业媒体、PR wire、采访、奖项、争议 | PR、声誉、媒体框架 | NEW |
| Video platforms | YouTube、B站、抖音、TikTok、Vimeo、嵌入视频 | TVC、campaign film、短视频、可见数据 | VID |
| Social platforms | 小红书、微博、知乎、B站社区、公众号、论坛 | 社媒线索、UGC、公开反馈 | SOC |
| Visual / campaign archives | 图片搜索、创意案例库、设计平台、案例页 | 海报、KV、落地页、包装、活动视觉 | VIS |
| Reports / PDFs / market context | 公开报告、白皮书、年报、PDF | 市场事实、公开数字、品类背景 | RPT |

当某个平台过大时，可以继续拆成：

- `SOC-XHS`
- `SOC-WEIBO`
- `SOC-BILI`
- `VID-YOUTUBE`
- `VID-BILI`

### 8.4 子代理返回内容

每个子代理只返回：

1. Shard Brief
2. Search Log
3. Evidence Pool Shard
4. Gaps And Restrictions

子代理不得做策略结论。

### 8.5 合并规则

主 Skill 合并时需要：

- 按 URL、citation、资产标题、campaign/物料身份去重。
- 同一 campaign 在不同渠道出现时保留为不同证据。
- 保留 shard 前缀，方便追溯来源。
- 保守合并 campaign/message 标签。
- 将关联关系标为 confirmed / likely / tentative。
- 对 search-only 或 access-limited 证据降低 confidence。
- 如果某一平台 shard 过度主导，需要标记平台偏科。

## 9. 已调整后的输出结构

正式英文文件现在采用两层输出：

1. 前台交付：给用户和总控 Skill 快速阅读。
2. 后台资料库：给 `evidence-summary-analysis` 和后续 `insight-strategy` 使用。

这次调整的核心不是删掉资料，而是把展示顺序变轻：

```text
前台轻摘要；
后台保留完整 Evidence Pool 和完整 dossier。
```

### 9.1 前台默认交付

前台默认只展示以下七个部分：

```markdown
# Web Evidence Collection: [Topic]

## 1. Collection Readiness

- Status: ready / partial / thin / blocked
- Target:
- Scope:
- Collection date:
- Requested categories:
- Requested depth:
- Evidence count:
- Source mix:
- Restricted / user-needed items:
- Linked campaign chains:
- Subagent mode:
- Downstream next step: evidence-summary-analysis

## 2. Evidence Brief Box

- Evidence readiness:
- Source coverage summary:
- Most reliable source groups:
- Brand hard-data candidates:
- Major restrictions:
- Missing evidence:
- Evidence pool status:

## 3. Source Coverage

| Area | Collected count | Source spread | Strongest source level | Confidence | Notes |
| --- | ---: | --- | --- | --- | --- |

## 4. Brand Hard Data Track

| Hard data type | Candidate evidence | Source / URL | Confidence | Needs user confirmation |
| --- | --- | --- | --- | --- |

## 5. Key Campaign / Competitor Linkage

| Campaign / message | Linkage status | Related evidence IDs | Channels represented | Missing channels |
| --- | --- | --- | --- | --- |

## 6. Gaps And Restrictions

| Gap / restriction | Why it matters | Suggested next action |
| --- | --- | --- |

## 7. Evidence Pool Handoff

- Evidence pool:
- Core schema compatibility: evidence-summary-analysis
- Do not skip next skill:
- Recommended next skill: evidence-summary-analysis
```

### 9.2 后台完整资料库

后台完整资料库保留以下结构：

- Collection Brief
- Depth And Query Plan
- Subagent Collection Plan
- Evidence Shards
- Evidence Brief Box
- Source Coverage
- Brand Hard Data Track
- Campaign Linkage Map
- Collection Statistics
- Campaign / Message Repetition Snapshot
- Skew And Completeness Check
- Gaps And Restrictions
- Evidence Pool

后台资料库用于审计、继续调研和下游 Skill 处理，不默认全部展示给用户。

### 9.3 前台统计压缩

前台只展示四项统计：

- total evidence items
- source mix
- restricted / user-needed items
- linked campaign chains

以下内容不默认展开：

- 长搜索计划
- 子代理详细任务表
- shard search log
- 完整 Collection Statistics
- 长表格形式的重复检查
- 全量 Evidence Pool 明细

这些内容保留在后台 dossier，用户要求“完整资料池”“全量 dossier”“调研过程”时再展开。

## 10. Campaign / Message Repetition Snapshot

正式英文文件已将旧的 `Concept Repetition Check` 改为：

```text
Campaign / Message Repetition Snapshot
```

这样做是为了避免它和后续 concept / strategy Skill 混淆。

这里的作用只是采集层判断：

- 同一个 campaign/message 是否在不同渠道重复出现。
- 一个 campaign 是否包含多个 message。
- 某个 message 是否被多个竞品重复使用。
- 是否只有 PR 多、视觉少，或只有社媒多、官方来源少。
- 跨渠道链路是否完整。

示例：

```markdown
| Campaign / message | Evidence count | Channels | Brands | Repetition pattern | Completeness |
| --- | ---: | --- | --- | --- | --- |
| New Year family reunion | 5 | video, PR, social | Brand A | repeated across launch materials | medium |
```

这不是洞察，也不是创意概念命名，只是证据整理和链路标注。

## 11. Evidence Pool 结构

Evidence Pool 现在被定义为真正的核心结果。

每条证据优先保留下游通用字段：

```markdown
### Evidence 1

- Evidence ID:
- Source type:
- Source name:
- Date:
- URL or citation:
- Raw quote:
- Observation:
- Summary:
- Topic tag:
- Audience:
- Confidence:
```

然后添加采集层扩展字段：

```markdown
- Source level:
- Category:
- Publisher / platform:
- Author / account:
- Access date:
- Brand / event:
- Campaign / message:
- Channel:
- Material type:
- Visual material:
- Screenshot status:
- Key fact:
- Evidence value:
- Brand hard data type:
- Needs user confirmation:
- Related evidence:
- Linkage status:
- Metric / count:
- Limitation / restriction:
```

字段含义：

- `Raw quote`：短引用，不复制全文。
- `Observation`：适用于视觉、视频、活动等没有直接文字引用的证据。
- `Summary`：一句话说明这条证据说明了什么。
- `Topic tag`：资料主题标签，不是洞察。
- `Audience`：如果能从资料看出面向人群，则记录；不能判断则留空或 unknown。
- `Confidence`：high / medium / low / speculative。
- `Campaign / message`：采集层标签，不等于最终策略概念。
- `Brand hard data type`：品牌硬信息类型，例如 slogan、vision、founder statement、product proof 等。
- `Needs user confirmation`：标记该品牌信息是否需要用户确认。
- `Related evidence`：说明它和哪些证据属于同一 campaign 或链路。
- `Limitation / restriction`：平台限制、截图限制、登录限制、版权限制等。

## 12. 下游承接规则

正式流程现在明确为：

```text
web-evidence-collector
-> evidence-summary-analysis
-> insight-strategy
```

也就是说：

- `web-evidence-collector` 负责收集和控制证据。
- `evidence-summary-analysis` 负责读 Evidence Pool，做归纳、整理、摘要和结构化总结。
- `insight-strategy` 再基于总结后的材料做洞察和策略。

即使用户最终想要策略，也不应默认跳过 `evidence-summary-analysis`。

只有当用户明确要求绕过第二个 Skill 时，才可以直接把 Evidence Pool 交给策略层。

## 13. 社媒与版权边界

操作原则：

1. 不绕过登录、付费墙、验证码、反爬、访问控制。
2. 不批量复制文章全文、评论全文、报告全文、社媒全文。
3. 优先保存链接、标题、作者/机构、发布时间、访问时间、核心事实摘要。
4. 直接引用只保留短句，并标注来源。
5. 截图用于证明“该内容存在/该页面如何展示”，不是素材库。
6. 遇到受限平台，改用用户提供截图、平台导出、官方 API、公开搜索摘要或人工采样。

动态平台处理策略：

- 能公开访问：提取少量短引用、链接、发布日期、可见数据。
- 需要登录或不稳定：保留短关键文字、链接、平台、限制说明。
- 用户能提供截图/导出：按用户提供材料处理，但仍标注来源和 confidence。
- 明确禁止或技术阻断：停止自动采集。

## 14. 当前结构是否成立

这套 Skill 成立，并且现在边界更清晰。

成立原因：

- 它只做证据收集，不做策略判断。
- 它能承接总控 Skill 的任务包。
- 它能把多平台、多物料、多来源证据整理成 Evidence Pool。
- 它保留了视觉、视频、线下、营销、PR、社媒、报告和品牌硬信息候选。
- 它通过 Source Coverage、Gaps、Campaign Linkage 和 Evidence Pool 支撑第二层总结 Skill。
- 它明确了前台轻展示和后台完整资料库的区别。
- 它没有跳过 `evidence-summary-analysis`，因此和后续策略 Skill 的分工更稳。

## 15. 本次正式调整已落地

本次已经落地到正式英文文件的六项调整是：

1. `SKILL.md` 的 Output Contract 已拆成：
   - Default Frontstage Handoff
   - Backend Dossier
2. `references/09-output-template.md` 已改成前台轻量模板优先。
3. `Concept Repetition Check` 已改名为 `Campaign / Message Repetition Snapshot`。
4. `Collection Statistics` 在前台压缩为四项：
   - total evidence items
   - source mix
   - restricted / user-needed items
   - linked campaign chains
5. 完整 Evidence Pool 被保留为核心结果。
6. 正式文件已明确：`evidence-summary-analysis` 必须承接 Evidence Pool，不应被默认跳过。

## 16. 一句话总结

`web-evidence-collector` 现在是一个“公开资料采集与证据池控制器”：前台给总控和用户快速判断资料是否够用，后台保留完整 Evidence Pool 给第二个总结 Skill 使用。
