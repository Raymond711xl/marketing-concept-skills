# Evidence Summary Analysis 中文说明

> 这是给人看的中文审阅版，不参与 Skill 工作流。正式运行仍以 `evidence-summary-analysis/SKILL.md` 为准。

## 1. 这个 Skill 的定位

`evidence-summary-analysis` 是一个证据摘要与整理 Skill。

它位于资料采集和洞察策略之间：

```text
web-evidence-collector -> evidence-summary-analysis -> insight-strategy
```

它的核心任务不是做策略，也不是做人性洞察，而是把已经收集到的材料整理成一个干净、可追溯、可交接的证据摘要层。

一句话定义：

```text
把零散资料整理成结构化证据池，并提取可直接从证据中看到的证据模式，交给后续策略 Skill 使用。
```

## 2. 它解决什么问题

很多调研材料在进入策略判断前会很乱：

- 有链接，但没有摘要
- 有截图，但没有来源信息
- 有社媒内容，但平台访问受限
- 有竞品案例，但没有分类
- 有视频、PR、活动、营销、视觉物料，但混在一起
- 有一些强信号，但还没有整理出可分析结构
- 有些资料是品牌自己说的，有些是第三方媒体说的，有些是用户说的，不能混为一谈

这个 Skill 的工作就是先把材料整理好：

- 按来源整理
- 按类别整理
- 按证据强弱整理
- 按物料类型整理
- 标出缺口
- 标出限制
- 保留原始出处
- 输出可交接的 cleaned evidence pool

在总控工作流中，它通常会自动接在 `web-evidence-collector` 后面执行，作为统一的「证据准备」阶段。采集和摘要仍然是两个独立 Skill，但默认体验上不要求用户手动分两次触发。

前台呈现的关键不是长报告，而是内容条：

- 来源覆盖内容条
- 强证据模式内容条
- 品牌硬信息内容条
- 证据缺口内容条
- 进入策略判断内容条

完整证据池仍然保存在后台 dossier 中，用户需要时可以打开查看。

## 3. 它不做什么

这个 Skill 必须克制。

它不做：

- 不做开放网页搜索
- 不绕过登录、付费墙、验证码、反爬、私域或平台限制
- 不复制全文文章、全文报告、完整评论串或完整社媒内容
- 不把品牌自说自话当成消费者真实想法
- 不创建 insight theme
- 不做人性洞察
- 不推断深层动机
- 不做文化判断
- 不做战略建议
- 不做定位
- 不做 Idea Platform
- 不做 Concept

这些内容都应该留给 `insight-strategy` 或更后面的策略/概念 Skill。

## 4. 和 insight-strategy 的边界

这是当前最重要的边界。

`evidence-summary-analysis` 只做“证据模式”。

“证据模式”指的是可以直接从资料中看到的重复结构，例如：

- 哪些来源反复出现
- 哪些平台证据更多
- 哪些物料类型更集中
- 哪些话术被重复使用
- 哪些视觉形式反复出现
- 哪些活动机制被复用
- 哪些 PR 角度被强调
- 哪些渠道承担主要传播作用
- 哪些证据来自品牌自有渠道
- 哪些证据来自第三方媒体
- 哪些证据来自用户或社媒

`insight-strategy` 才负责：

- Level 1: Fact Layer，生成 themes / signals
- Level 2: Motive Inference，推断情绪、需求、恐惧、欲望
- Level 3: Cultural Judgment，判断文化张力
- Level 4: Strategic Decision，提出战略选择、Idea Platform 候选

所以 Summary 层不能写：

```text
消费者真正焦虑的是……
这个现象背后的文化矛盾是……
品牌应该选择……
这个 Campaign 的 Idea Platform 是……
```

Summary 层只能写：

```text
证据显示，多个来源都在重复使用“效率/陪伴/安全感”类表达。
证据集中来自品牌自有渠道，缺少消费者侧验证。
社媒证据可见度有限，目前只能作为线索。
视频物料多采用人物叙事，线下活动多采用打卡机制。
```

## 5. 默认语言和市场语境

这个 Skill 默认用中文和用户沟通。

但证据字段名保持英文，因为后续 Skill 需要稳定读取字段。

处理规则：

- 用户中文输入，默认中文输出
- 中国品牌、中国品类、中国市场，按中文互联网、中文平台、中文消费者语境理解
- 用户要求英文、海外市场或国际竞品时，可以切换英文表达
- 原始引用、口号、帖子标题、短句可保留原文
- 不要为了中文解释而替换掉原始来源线索

## 6. 可接收的输入

它可以接收：

- `web-evidence-collector` 产出的 evidence pool
- 竞品设计或视觉调研结果
- 品牌 Campaign 调研笔记
- 市场或竞品研究摘要
- Social listening 初洗报告
- 访谈记录
- 评论
- 评价
- 问卷开放题
- 活动反馈
- 用户提供的截图、链接、导出表格或笔记

如果输入不是结构化的，它需要先整理成证据池。

## 7. Evidence Pool 字段结构

核心字段需要兼容下游 `insight-strategy`。

建议格式：

```markdown
## Evidence Pool

### Evidence 1
- Evidence ID:
- Source type:
- Source name:
- Date:
- URL or citation:
- Raw quote:
- Summary:
- Topic tag:
- Audience:
- Confidence:
- Category:
- Source level:
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
- Limitation / restriction:
```

下游策略 Skill 最需要的字段是：

```text
source_type
source_name
date
url_or_citation
raw_quote
summary
topic_tag
audience
confidence
```

如果缺字段，不要丢掉证据，而是明确标注缺失。

## 8. 来源等级处理

证据来源按 L1 到 L8 分层。

| 等级 | 来源 | 处理方式 |
| --- | --- | --- |
| L1 | 官网、政府页面、上市公司公告、品牌通稿 | 可直接摘要，保留链接，只做短引用 |
| L2 | 新闻文章、公开报道、行业媒体 | 提取事实、观点、发布时间和媒体语境 |
| L3 | 公开 PDF、白皮书、报告节选 | 摘要关键数字，尽量标注页码或文件名 |
| L4 | 搜索摘要、聚合页、新闻索引 | 只作为线索，不能直接当最终事实 |
| L5 | 电商评价、App Store 评论、公开论坛 | 使用少量代表性短引用，不能批量复制 |
| L6 | 小红书、微博、抖音、知乎、B站、TikTok、Instagram 等动态或登录平台 | 只处理公开可见内容；受限时保留一句短语、链接和限制说明 |
| L7 | 付费报告、会员页面、私域社群、登录后内容 | 不自动采集，只分析用户有权提供的截图、摘录或导出 |
| L8 | 明确禁止或技术阻断内容 | 不采集，只保留链接元信息或用户授权材料 |

## 9. 输出数量规则

当用户要求按类别总结时，可以让用户选择数量。

类别包括：

- Video
- Offline activation
- Marketing
- PR
- Visual materials

默认数量：

| 类别 | 轻量 | 标准默认 | 深度 |
| --- | --- | --- | --- |
| Video | 1-2 条 | 3 条 | 6-10 条 |
| Offline activation | 1-2 个 | 3 个 | 6-10 个 |
| Marketing | 3 条 | 5 条 | 8-12 条 |
| PR | 3 条 | 5 条 | 8-12 条 |
| Visual materials | 3 条 | 5 条 | 8-12 条 |

如果用户没有指定数量，默认按标准量输出。证据不足时，输出现有内容，并标明缺口。

## 10. 工作流程

### 10.1 确认范围

确认：

- 目标品牌、Campaign、事件、产品、行业或竞品组
- 时间范围
- 地域或平台范围
- 需要分析的类别
- 输出数量
- 下游用途，例如内部 briefing、创意参考、策略输入、提案、竞品审计、证据交接

如果信息已经足够，不必反复追问。

### 10.2 标准化证据

把输入转成 evidence item。

需要区分四层：

```text
Fact：来源直接说了什么
Observation：材料中能直接看到什么
Low-level source/material inference：低层级来源或物料推断
Unknown：缺失或未验证的信息
```

这里的 inference 只能是很轻的材料层推断，不能进入动机、人性、文化或策略意义。

### 10.3 检查证据覆盖

在摘要前先检查：

- 请求的类别是否有足够证据
- 来源是否多样，还是集中在单一平台
- 品牌自有渠道和第三方/消费者渠道是否分开
- 日期和链接是否可追溯
- 视觉或社媒资料是否可访问
- 是否存在只来自搜索摘要的弱证据

证据薄时可以继续，但必须写 caveat。

### 10.4 按类别摘要

只总结用户要求的类别；如果用户没指定，就总结现有所有类别。

## 11. 分类摘要标准

### Video

用于视频广告、TVC、短视频、直播切片、Campaign film。

提取：

- 片名或素材名
- 来源和链接
- 核心信息或口号
- 脚本/叙事结构
- 主要受众
- 视觉风格和制作线索
- 产品角色
- 平台/渠道
- 有证据支持的表现指标
- 可复用模式
- 证据缺口

### Offline Activation

用于快闪、展览、零售活动、事件营销、路演、装置、校园活动、社群活动。

提取：

- 活动机制
- 地点和时间
- 参与路径
- 空间或视觉装置
- 互动机制
- 社交分享触发点
- 线上二次传播
- 受众角色
- 可复用模式
- 证据缺口

### Marketing

用于促销、上市、联名、电商节点、KOL/KOC、UGC、私域、会员、平台机制。

提取：

- 营销机制
- 目标受众
- 利益点、钩子或参与激励
- 渠道组合
- 内容格式
- 转化或互动路径
- 合作方或创作者角色
- 可复用模式
- 证据缺口

### PR

用于新闻稿、媒体报道、公共议题、奖项、争议、CEO 表态、社交讨论、声誉事件。

提取：

- 新闻角度
- 信息框架
- 发声人或机构
- 媒体/来源扩散情况
- 公众回应指标
- 风险或争议
- 声誉影响
- 可复用模式
- 证据缺口

### Visual Materials

用于海报、KV、落地页、包装、产品页、社媒视觉、活动视觉、截图。

提取：

- 物料类型
- 来源和截图状态
- 构图和信息层级
- 色彩、字体、图像、品牌资产使用
- 信息和 CTA
- 平台适配
- 跨触点视觉一致性
- 可复用模式
- 证据缺口

社媒平台无法完整访问时，只保留：

```text
一句关键短语 + 链接 + 平台 + 限制说明
```

例如：

```text
完整社媒内容需要平台访问；请用链接进行人工核验。
```

## 12. Evidence Pattern Inventory

类别摘要之后，输出证据模式清单。

可以整理：

- 重复出现的信息表达
- 证据里明确出现的受众标签
- 常见物料格式
- 可观察到的渠道逻辑
- 最强证据点
- 弱证据或未验证说法
- 互相矛盾的证据项
- 来源集中或偏斜
- 值得交给 `insight-strategy` 的证据模式

注意：这里不能命名 insight theme，不能推断动机，不能做人性洞察，不能做文化判断，不能跳到策略。

## 13. 推荐输出结构

```markdown
# Evidence Summary Analysis: [Topic]

## 1. Scope

- Target:
- Time range:
- Geography/platform:
- Requested categories:
- Requested volume:
- Evidence count:
- Main source types:

## 2. Evidence Coverage Check

| Area | Status | Notes |
| --- | --- | --- |
| Source diversity | strong / medium / weak | |
| Date traceability | strong / medium / weak | |
| URL/citation traceability | strong / medium / weak | |
| Brand-owned vs third-party separation | clear / mixed / weak | |
| Social/platform restrictions | none / some / significant | |
| Visual evidence coverage | strong / medium / weak | |

## 3. Category Summaries

### Video

| Item | Source | Message | Audience | Pattern | Confidence |
| --- | --- | --- | --- | --- | --- |

### Offline Activation

| Item | Source | Mechanism | Audience | Pattern | Confidence |
| --- | --- | --- | --- | --- | --- |

### Marketing

| Item | Source | Mechanism | Channel | Pattern | Confidence |
| --- | --- | --- | --- | --- | --- |

### PR

| Item | Source | News angle | Response/risk | Pattern | Confidence |
| --- | --- | --- | --- | --- | --- |

### Visual Materials

| Item | Material type | Source | Visual observation | Screenshot status | Confidence |
| --- | --- | --- | --- | --- | --- |

## 4. Evidence Pattern Inventory

### Pattern 1: [Name]

- Evidence support:
- What the evidence shows:
- What remains uncertain:
- Confidence:

## 5. Evidence Gaps

| Gap | Why it matters | Suggested collector task |
| --- | --- | --- |

## 6. Downstream Strategy Handoff

### Strong evidence patterns

- 

### Weak evidence patterns / collection leads

- 

### Evidence-only handoff notes

- 

## 7. Cleaned Evidence Pool

### Evidence 1
- Source type:
- Source name:
- Date:
- URL or citation:
- Raw quote:
- Summary:
- Topic tag:
- Audience:
- Confidence:
- Category:
- Source level:
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
- Limitation / restriction:
```

## 14. 质量规则

- 每个主要摘要都要能追溯到 evidence ID、source name 或 URL
- 不编造引用、链接、日期、数据、Campaign 名称或平台反应
- 不把一个生动例子放大成市场真相
- 不把品牌自有表达当成消费者信念
- 保留少数派或矛盾证据
- 不确定的内容标为 low 或 speculative
- 不解释人们为什么这么想
- 不判断文化要什么
- 不判断品牌应该怎么选
- 这些应该交给 `insight-strategy`
- 直接引用只保留短句
- 受限社媒内容只保留链接和短关键句，不复制全文

## 15. 最终交接顺序

建议按这个顺序交接给下游：

```text
1. Evidence coverage check
2. Category summaries
3. Evidence pattern inventory
4. Evidence gaps
5. Cleaned evidence pool
```

如果用户只要快速版，输出：

```text
Top evidence patterns
Category summary table
Evidence gaps
Cleaned evidence pool
```

## 16. 最简理解

这个 Skill 不是“洞察分析师”，而是“证据整理师”。

它应该回答：

```text
我们现在手上有什么证据？
证据来自哪里？
证据质量怎么样？
哪些类别有资料？
哪些类别缺资料？
材料中能直接看到什么重复模式？
哪些内容可以交给策略层继续判断？
```

它不应该回答：

```text
消费者内心真正渴望什么？
这背后的文化矛盾是什么？
品牌应该站在哪一边？
Idea Platform 应该是什么？
Concept 应该怎么写？
```

这些后者都交给 `insight-strategy` 和后续策略/概念 Skill。
