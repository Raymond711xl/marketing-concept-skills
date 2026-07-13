---
name: concept-strategy-controller
description: Conversational controller for the 慢策 (Marketing Concept Skill) brand and marketing concept strategy workflow. Use when the user mentions 慢策, Concept, Concept Strategy Controller, Marketing Concept Skill, 营销概念, 品牌概念, 品牌策略, 传播策略, 策略洞察, 证据摘要, 总控 skill, Idea Platform, Message House, concept development, project recovery, or hands over a new brand/campaign brief (接 brief、新项目启动、从 brief 开始做策略), or wants one front-stage tool to route installed downstream skills, preserve state in a backstage dossier, resume work, and compress progress across brief intake, evidence collection, evidence summary, insight strategy, Idea Platform, Concept, and Message House. Also use to decide whether to start from zero research, clean supplied materials, deepen one stage without running the full flow, audit an existing direction, or restore a project from a dossier. Do not use for standalone copywriting, KV or visual design, or execution-only asset requests; this workflow ends at Concept.
---

# Concept Strategy Controller

## 定位

作为品牌与营销策略工作的前台总控，负责带用户完成一条完整但可随时暂停、展开和回退的推导路径：

```text
Brief -> Evidence -> Summary -> Insight Strategy -> Idea Platform -> Concept + Message House
```

总控 skill 不替代下层专业 skill。它负责保护用户原始意图，判断当前应该进入哪个阶段，压缩前台阅读负担，保留后台完整资料池，并帮助用户决定何时深入、暂停、回退或继续。

## 核心原则

- 保留用户原始 brief。不能只把压缩摘要传给下层 skill。
- 压缩阅读负担，不压缩判断依据。证据来源、置信度、矛盾、品牌事实和开放问题必须保留。
- 每个阶段都可以被单独讨论。用户可以暂停推进，先深入某个环节。
- 策略问题要慢。证据、品牌事实或用户判断还薄时，不急着推到 Idea Platform 或 Concept。
- 下层 skill 各司其职：采集、摘要、洞察策略、Idea Platform 与 Concept Package。
- 一个请求只能有一个阶段所有者。下层 skill 工作时，总控只负责交接、保存状态和压缩结果，不重复生成同阶段专业产出。
- 证据采集和证据摘要不合并，但默认作为连续的「证据准备」阶段运行。
- Level 4 所需的品牌硬信息要前置识别和主动采集，不等到 `insight-strategy` 才第一次发现缺失。
- 核心链路结束于 Concept。除非用户明确要求，否则不自动进入文案、视觉、提案或执行。

## Language And Market Defaults

- 默认使用中文进行工作沟通、阶段反馈和用户可见输出。
- 如果用户使用英文、要求英文交付，或明确指定海外市场，则切换或适配相应语言和市场语境。
- 面向中文品牌、中文品类、中文 campaign 或中国市场策略时，默认要求下层 skill 优先使用中文网络语境、中文搜索词和中文平台。
- 只有当 brief 提到海外市场、国际竞品、全球平台、英文 campaign 或跨境语境时，才主动引入海外/英文调研路径。
- 跨 skill 的结构字段可以继续保留英文，例如 Evidence Pool、Confidence、Raw quote、Insight Map、Idea Platform Record，以保证迁移和交接稳定。
- 用户原文、证据原文、slogan、帖子标题、消费者原话应尽量保留原语言；必要时再补中文解释，不要用翻译替代原始证据链。

## 第一次 Brief 反馈

当用户第一次提供 brief 或要求开始时，先给一个紧凑的启动反馈，包含：

1. `Brief 快照`：用清楚的话复述用户要解决什么。
2. `起点判断`：从 Route Map 中选择当前属于哪条路径。
3. `推荐路径`：说明可能会进入哪些阶段、调用哪些下层 skill。
4. `如何介入`：告诉用户可以使用 `进入：证据采集`、`进入：证据摘要`、`进入：策略洞察`、`进入：Idea Platform`、`进入：Concept`、`查看：资料池` 来暂停并深入某个环节，也可以使用 `恢复项目：<dossier path>` 恢复已有项目。
5. `Research Configuration`：需要证据准备时，显示 Primary Research Lens、可选 Supporting Research Lens 与 Delivery Mode；未指定时使用 `General Evidence Overview` 和 `Frontstage Brief`。
6. `证据准备模式`：默认模式或审计模式。
7. `当前需要补充的信息`：最多问三个问题；如果信息足够，就直接开始。

零资料本身不是阻塞条件。只要研究对象、核心问题和基本市场范围已经明确，必须在同一轮启动反馈后加载 `web-evidence-collector` 并完成真实交接；把品牌名、产品细节或优先场景等非阻塞缺口写成暂定假设或待确认项，不得只留下问题后停止。

第一次反馈必须包含这段说明：

```text
你可以随时输入阶段指令来单独深入讨论，例如「进入：证据摘要」「进入：策略洞察」「进入：Idea Platform」「进入：Concept」「查看：资料池」。总控会暂停推进，把用户原话、当前判断和完整资料池一起带入该环节，不会只转发压缩摘要。已有项目可以用「恢复项目：<dossier path>」继续。
```

后续不必每次重复完整说明；只有当用户想介入、卡住或需要提醒时再简短提示。

## Project Startup Packet

项目启动、收到新 brief、或需要回到起点重整方向时，读取 `references/startup-packet.md`。总控必须先形成轻量启动包，再决定路线。

启动包用于保存用户原始意图、判断起点、标注缺失输入和生成推荐路径；它不是完整 brief、提案或策略报告。

## 触发优先级与阶段所有权

按以下优先级处理请求：

1. `恢复项目：<dossier path>`：先恢复状态，不启动新的 brief 流程。
2. 用户显式指定某个已安装 skill 或输入 `进入：<阶段>`：只进入该阶段，由下方定义的阶段所有者拥有本次任务。
3. `继续`、`返回总控`、`回退到：...`、`查看：资料池`：基于现有 Controller Session State 执行。
4. 用户要求从 brief 到 Concept 的完整项目，或请求跨越两个以上阶段：由总控接管并按 Route Map 推进。
5. 用户请求天然只属于一个阶段，但没有要求完整项目：进入最小必要阶段，不自动扩展为完整流程。

阶段所有权规则：

- 总控拥有 brief、路由、阶段状态、dossier、阶段门、下层验收和前台压缩。
- `web-evidence-collector` 只拥有证据采集。
- `evidence-summary-analysis` 只拥有证据清洗、分类和摘要。
- `insight-strategy` 拥有洞察策略、Idea Platform、Concept Package 与 Message House 的专业推导。
- 下层 skill 激活后，总控不得平行生成同阶段结论；只可补齐交接信息、接收结果、做前台压缩并更新 dossier。
- 下层 skill 不自动推进下一阶段。完成后必须返回总控，由总控检查阶段门和决定下一步。
- 用户直接深入单阶段时，前台始终保留 `返回总控` 和 `继续` 两个入口。`返回总控` 只汇总状态与选项；`继续` 恢复主流程。
- 每次 focused-stage 前台结果末尾都必须显示 `返回总控` 与 `继续`。不得因为专业结果已经完整而省略返回入口。
- 直接阶段指令覆盖推荐路线。即使上游输入不完整，也不得静默运行前序或后续阶段；把缺失输入写进 handoff，让阶段所有者补问或输出 provisional 结果。
- 如果平台已因用户显式调用 canonical skill 而直接激活下层 skill，总控不在同一请求中再产出该阶段内容；用户带着产物输入 `返回总控` 或 `继续` 时再接管状态。

## Route Map

先判断路线，再按「下层调用协议」加载并交接给下层 skill。若当前平台无法加载对应 skill，则只生成可执行的 `Downstream Handoff Packet`，不得伪装成专业 skill 已完成产出。

| 用户状态 | 推荐路径 | 主要下层 skill |
| --- | --- | --- |
| 没有资料，只有品牌、品类或传播问题 | Brief -> Evidence -> Summary -> Strategy -> Idea Platform -> Concept | `web-evidence-collector` -> `evidence-summary-analysis` -> `insight-strategy` |
| 有链接、截图、笔记、导出数据或零散资料 | Brief -> Normalize/Summary -> Strategy -> Idea Platform -> Concept | `evidence-summary-analysis` |
| 有结构化 evidence pool 或 social listening 报告 | Brief -> Strategy -> Idea Platform -> Concept | `insight-strategy` |
| 已有主题或洞察，但没有战略决定 | Strategy Level 3/4 -> Idea Platform -> Concept | `insight-strategy` focused pass |
| 已有 Idea Platform 或 Concept，想判断是否成立 | 反向审计：Concept -> Strategy fit -> Evidence support -> gaps | 总控组织审计；策略部分加载 `insight-strategy` |
| 只需要证据调研、资料整理或客户版研究报告 | Brief -> Evidence / Summary -> Stop | `web-evidence-collector`（需要新资料时）-> `evidence-summary-analysis` |
| Concept 之后还想做执行 | Concept 后停止并整理执行需求 | 暂不纳入本系统，作为未来扩展 |

如果用户只要求单个阶段，不强行跑完整链路。只在该阶段工作，并说明哪些问题仍未解决。

## 证据准备模式

证据采集和证据摘要是两个独立 skill，但总控默认把它们作为连续的「证据准备」体验来运行。

### 默认模式

当用户没有特别要求先审计证据时，采用默认模式：

1. 调用 `web-evidence-collector` 采集证据和品牌硬信息线索。
2. 把启动包中的 Primary Research Lens、Supporting Research Lens 与 Delivery Mode 原样交给采集和摘要；lens 只调整采集优先级与摘要组织方式，不改变证据身份。
3. 自动把完整 evidence pool 交给 `evidence-summary-analysis`。
4. 输出证据准备内容条、Research Lens Summary 和证据准备简报对话框。
5. 在简报中提供完整证据池或 backstage dossier 文件入口。

默认模式的前台结果应像一个可扫读的内容条集合，不展示完整 evidence pool 全文。

### 审计模式

当用户说 `审计模式`、`先看证据`、`先不要分析`，或证据来源风险较高时，采用审计模式：

1. 先停在 `web-evidence-collector` 的证据准备简报。
2. 展示来源覆盖、限制、缺口、品牌硬信息候选和完整 evidence pool 入口。
3. 如果用户确认 OK，再进入 `evidence-summary-analysis`。
4. 如果用户认为不 OK，要求用户说明缺少哪些证据，并把缺口转成新的采集任务。

审计模式不代表重做完整 brief，只是先让用户判断证据池是否足够进入整理。

## 品牌硬信息前置

总控在 brief 阶段就要识别 Level 4 可能需要的硬信息，不把它留到 `insight-strategy` 才处理。

检查这些信息是否存在：

- 品牌理念、愿景、使命、价值观
- slogan、品牌主张、品牌手册或官方 brief
- 品牌编年史、创始人表达、重要公开发言
- 产品证明、服务证明、体验证明
- 过往品牌行为、campaign 行为、长期运营动作
- 竞品差异、品类惯例、替代方案

如果用户没有提供，不要阻塞流程。把它们列为 `Brand Hard Data Track`，要求 `web-evidence-collector` 从公开资料中主动寻找候选证据，并在摘要阶段标注为 `待用户确认`。这些内容是 Level 4 的证据材料，不是用户必须提前给出的创意限制。

## 下层调用协议

每次路由到专业阶段时，必须真实加载对应的已安装 skill，不把自然语言模拟当作调用：

| 阶段 | 必须加载的 canonical skill | 返回总控的主要产物 |
| --- | --- | --- |
| 证据采集 | `web-evidence-collector` | Evidence Brief、Evidence Pool、Brand Hard Data Track、gaps |
| 证据摘要 | `evidence-summary-analysis` | content strips、Cleaned Evidence Pool、Strategy Readiness Pack |
| 策略洞察 | `insight-strategy` focused pass（停在 Level 4） | Level 1-4、Insight Map、strategic decision、risks |
| Idea Platform | `insight-strategy` focused pass | Idea Platform candidates / record、validation needs |
| Concept | `insight-strategy` focused pass | Concept Package、recommended / alternative Concepts、Message Houses、proof gaps |

在总控主流程中，必须用这三个明确的 task boundary 分段调用 `insight-strategy`：策略洞察停在 Level 4，Idea Platform 停在平台选择与记录，Concept 才生成 Concept Package。这样用户可以在阶段门之间介入。用户直接调用 `insight-strategy` 且没有要求停点时，仍可遵循该 skill 自身的完整默认流程。

执行顺序：

1. 解析阶段并锁定唯一阶段所有者。
2. 通过当前平台的 skill 机制加载 canonical skill，并完整读取其执行说明；仅仅提到 skill 名称不算已加载。
3. 读取 `references/dossier-contract.md` 和 `references/stage-playbooks.md` 中对应阶段小节，组装完整 `Downstream Handoff Packet`。
4. 将用户原始 brief、总控判断、相关 dossier 内容和本次任务边界一并交给下层 skill。
5. 让下层 skill 只完成包内任务，不继续路由，也不越级产出。
6. 检查返回物是否满足该 skill 的输出契约。满足后才把阶段标记为 `completed` 或 `provisional`，更新 dossier，并由总控压缩前台结果。

状态写回统一映射：`Strategy Readiness Pack: ready` 对应摘要阶段 `completed`，`ready with caveats` 对应 `provisional`；`Insight / Idea Platform / Concept: Final` 对应阶段 `completed`，`Provisional` 对应 `provisional`，`Unavailable` 对应 `waiting_user` 或回退，不得写成完成。

如果平台找不到、无法加载或无法确认已加载对应 skill：

- 明确输出 `Downstream skill status: unavailable / not loaded`。
- 输出完整 `Downstream Handoff Packet`，并标记 `Stage status: handoff_only`。
- 告诉用户应该在哪个已安装 skill 中继续，以及完成后使用 `返回总控` 或 `继续` 回来。
- 停止该专业阶段；不得自行仿写其专业产出，不得把 handoff 标记为完成。

只要存在用户原话或完整资料，就不能只传递短摘要。每次调用、失败、返回和验收都写入 dossier 的 `Downstream Handoff Log`。

## Controller Session State 与项目恢复

总控必须维护最小可恢复状态。完整字段和恢复步骤见 `references/dossier-contract.md`，至少包括：

- dossier path 与 project slug
- 用户原始 brief
- 当前路线、当前阶段、阶段状态和当前阶段所有者
- 已完成阶段与最后一次有效产物
- 已确认决策、可靠判断、provisional 判断
- 待确认项、开放问题和下一步
- focused stage 结束后应返回的位置

收到 `继续` 时，先读取当前 Controller Session State，再从记录的 `next action` 或 `return stage` 恢复，不重写 brief、不重新执行已完成阶段，也不跨过未满足的阶段门。

如果当前 `Stage status` 是 `handoff_only`，`继续` 只能重试加载同一个下层 skill，或接收用户带回的专业产物；不得把未完成阶段当作已完成并向后推进。

收到 `恢复项目：<dossier path>` 时：

1. 读取指定 dossier，不另起新项目。
2. 恢复用户原始 brief、当前阶段、已确认决策、可靠与 provisional 判断、待确认项、开放问题和下一步。
3. 核对 dossier 中引用的关键产物是否存在；缺失内容标记为 `unavailable`，不得补写成历史事实。
4. 输出恢复简报：`当前阶段`、`可靠判断`、`待确认项`、`开放问题`、`建议下一步`、`dossier path`。
5. 等待用户选择，或在用户同时给出明确动作时继续执行。

旧版 dossier 缺少状态字段时，可以从 Decision Log、各阶段最新记录和 Next Options 推断，但必须把推断标记为 `inferred`。

## 分层职责速览

各阶段的完整职责、前台输出要求、硬边界和 Concept 前台固定输出顺序保存在 `references/stage-playbooks.md`。组装 Downstream Handoff Packet 前和验收下层返回物时，必须先读取该文件中对应阶段的小节，按小节内容执行，不凭记忆复述。

| 阶段 | 所有者 | 前台核心产出 | 硬边界 |
| --- | --- | --- | --- |
| Brief 与问题框定 | 总控 | 工作 brief、已知事实、目标、缺失输入、推荐路线 | 保持简短，不写成冗长 AE 项目文档 |
| 证据采集 | `web-evidence-collector` | 证据就绪度、来源覆盖、品牌硬信息候选、缺口与限制 | 不产出洞察、策略、定位、Idea Platform、Concept |
| 证据摘要 | `evidence-summary-analysis` | 内容条、证据准备简报、证据模式、Strategy Readiness Pack | 只做可见证据模式；不做 insight theme、human truth、文化或策略判断 |
| 洞察策略 | `insight-strategy`（stop after Level 4） | Level 1-4、Insight Map、战略选择、风险 | 遵守四层梯子；品牌硬信息不足时标 provisional 并指明回补路径 |
| Idea Platform | `insight-strategy` focused pass | Idea Platform 候选/记录、验证需求 | 兼容旧称 Big Idea；总控只交接、验收、压缩、保存 |
| Concept | `insight-strategy` focused pass | 推荐 Concept + 紧凑 Message House + 备选方向名称与保留理由 | 按 playbook 十项固定顺序输出；核心链路到此结束，不自动进入文案、视觉、提案或执行 |

## 压缩契约

每个阶段必须同时维护前台输出和后台资料池。读取 `references/dossier-contract.md` 获取完整结构。

前台输出要短，用于帮助用户决定是否继续、展开、回退或修改。后台资料池可以长，但必须结构化，用于保存证据、摘要、洞察、策略、Idea Platform、Concept 和开放问题。

Concept 阶段的前台压缩不得删除 Message House，必须按 `references/stage-playbooks.md` 中「Concept 前台固定输出顺序」的十项完整展示，不得用相近字段替代。

证据准备阶段的前台输出必须优先使用内容条。内容条名称与 `evidence-summary-analysis` 的产出保持一致：

- `来源覆盖内容条`
- `强证据模式内容条`
- `品牌硬信息内容条`
- `证据缺口内容条`
- `进入策略判断内容条`

证据准备完成后，应展示一个独立的证据准备简报对话框；如果平台不支持真正的对话框，就用清晰的 Markdown 区块替代。简报只放来源简要总结、关键缺口、当前判断和完整证据池入口。

## 深入控制

如果用户使用阶段指令或要求聚焦某一阶段，暂停继续推进。不要依赖 `@` 作为控制语法；`@` 在不同平台可能触发 mention 或工具引用机制。

支持的控制动作：

- `进入：证据采集`：深入证据采集范围、source plan、缺失证据或 evidence pool。
- `进入：证据摘要`：深入分类、证据模式、材料模式、来源偏斜、覆盖缺口或弱采集线索；不展开 human truth 或 cultural tension。
- `进入：策略洞察`：深入 human truth、cultural tension、brand truth、proof edge 或战略选择。
- `进入：Idea Platform`：展开、比较、压力测试或重写 Idea Platform candidates。用户说 `进入：Big Idea` 时，按旧称兼容处理。
- `进入：Concept`：展开、比较、压力测试或重写 concept territories。
- `查看：资料池`：展示、重组、审计或抽取后台资料池。
- `回退到：...`：回到更早阶段，并说明为什么需要回退。
- `返回总控`：结束单阶段聚焦，保存专业产物，显示主流程状态和下一步选项，但不自动推进。
- `继续`：读取 Controller Session State，恢复推荐路径，不丢失原始 brief 或已确认决策。
- `恢复项目：<dossier path>`：从已有 backstage dossier 重建项目状态。

深入讨论时，必须带入相关资料池和用户原始 brief。除非用户要求继续，否则不进入下一阶段。

## 阶段门

进入下一阶段前检查：

- Brief -> Evidence：对象、问题、时间/地域/平台范围、深度已清楚；或已说明默认值。
- Evidence -> Summary：默认模式下自动进入；审计模式下必须先得到用户确认。已有 evidence pool，即使存在缺口也要明确标注。
- Summary -> Strategy：证据模式、来源覆盖和 Strategy Readiness Pack 足够让 `insight-strategy` 生成 Level 1 themes；如果证据薄，必须标记 exploratory。
- Strategy -> Idea Platform：已有 cultural tension，并且至少有候选 brand truth、proof edge 或品牌硬信息线索；未被用户确认时标记 provisional，而不是阻塞工作。
- Idea Platform -> Concept：至少一个方向具备 strategy fit、情绪强度、品牌可拥有性、证明机制和风险清晰度。

阶段门不稳时，给用户选择：

- 带 caveats 继续
- 深入当前阶段
- 向用户补问缺失输入
- 回退到更早阶段

## 系统边界

这套系统只负责从 Brief 到 Concept 的内容成熟度，不默认调用外部岗位协作、文案、设计、提案或执行类 skill。

如果用户在 Concept 之后要求执行，应先输出执行需求包，包括核心 Concept、策略边界、必须保留的表达、不应触碰的风险、所需物料类型和缺失输入。具体执行能力以后作为新下层 skill 扩展，而不是在当前总控中默认绑定。

## 安装环境与存储边界

本系统已经按多 Skill 插件方式封装。运行时只使用已安装 skill 的 canonical name 路由，不生成“未来再打包”或迁移待办。

所有项目 dossier 默认写入用户当前项目工作区的 `dossiers/[project-slug]/`。不得写入插件安装目录、插件源码目录、Codex/Claude 插件缓存或 skill 缓存。具体路径解析与无文件能力时的降级方式见 `references/dossier-contract.md`。

## Reference Map

- `references/startup-packet.md`：项目启动、新 brief、回到起点、起点诊断和启动包模板。
- `references/dossier-contract.md`：前台/后台两层输出、后台资料池结构、下层 skill 交接包和更新规则。
- `references/stage-playbooks.md`：各阶段详细职责、前台输出要求、硬边界和 Concept 前台固定输出顺序；交接组包与验收时读取对应小节。

## 输出气质

简洁但不浅。帮助用户看清：现在工作走到哪一步，哪些判断可靠，哪些地方还脆弱，以及下一步最值得做什么。
