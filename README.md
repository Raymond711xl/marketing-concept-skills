# 慢策｜Marketing Concept Skill

中文｜[English](README.en.md)

写方案的前半程，有 AI 陪你慢慢跑。

Version: 0.7.9  
Status: Draft / Alpha  
License: MIT

慢策是一个面向中文品牌、中文网络环境和营销策略工作的 Skill 组合包。它不是用来直接生成一句广告语，而是帮助你把方案前半程跑扎实：从一个不完整的 brief 出发，经过证据准备、洞察策略、Idea Platform 和 Concept，逐步形成一个有证据、有判断、有可讨论空间的品牌或传播概念。

当前版本 `0.7.9` 重点升级了 `insight-strategy`：围绕 Insight Reality 能力，强化从事实、动机、文化张力到战略选择的推导路径，并加入 Strategy Models Library 与 Message House，使策略不只停在洞察总结，而能继续进入可表达、可证明、可讨论的 Concept 结构。

## 核心路径

```text
Brief
  -> 证据采集
  -> 证据摘要
  -> 洞察策略
  -> Idea Platform
  -> Concept
```

慢策只处理方案的前半程。Concept 之后的广告文案、KV、视觉设计、脚本、提案页和执行物料，暂时不属于当前系统。

## 包含哪些 Skill

- `concept-strategy-controller`：总控。负责读 brief、判断路线、压缩阶段输出、维护后台资料池，并把任务交给合适的下层 skill。
- `web-evidence-collector`：证据采集。负责从公开网络、中文平台、社媒、竞品、品牌官方内容和 campaign 线索中整理 evidence pool。
- `evidence-summary-analysis`：证据摘要。负责清洗资料、分类、归纳证据模式、输出 Strategy Readiness Pack，不做最终策略判断。
- `insight-strategy`：洞察策略。负责从证据进入 human truth、cultural tension、brand truth、proof edge、Idea Platform 和 Concept 前的策略判断。

## 适合什么场景

- 从零开始做一个品牌、campaign、品类或传播问题的策略研究。
- 已经有链接、截图、评论、报告、竞品资料，需要整理成可用资料池。
- 想从社媒、竞品、PR、视频、视觉物料中归纳证据模式。
- 想把消费者语言、品牌事实和竞品差异推导成洞察策略。
- 想生成或比较 Idea Platform，并继续收束成 Concept。
- 想在某个阶段停下来，单独讨论、修改、回退或查看完整资料池。

## 不适合什么场景

- 不适合跳过证据和策略，直接要求最终广告语。
- 不负责最终文案、视觉、KV、脚本、提案页或执行物料。
- 不绕过登录、付费墙、反爬、私域社群或平台限制。
- 不把品牌自己的说法直接当成消费者真实想法。

## 默认语言和市场规则

- 默认使用中文工作和输出。
- 中文品牌、中文品类、中国市场项目，优先使用中文搜索词、中文平台和中文网络语境。
- 如果 brief 明确指定海外市场、英文交付、国际竞品、全球平台或跨境语境，再切换到英文或海外调研路径。
- 用户原话、证据原文、slogan、帖子标题、消费者评论尽量保留原语言。
- 跨 skill 的结构字段可以保留英文，例如 `Evidence Pool`、`Confidence`、`Raw quote`、`Insight Map`、`Idea Platform Record`，方便后续迁移和交接。

## 如何开始

你可以直接给总控一个 brief：

```text
我想为一个新中式茶饮品牌做品牌策略，目标是让它在年轻白领中建立“更轻松的日常奖励”心智。现在没有资料，希望先从竞品和社媒调研开始。
```

总控会先返回一个轻量启动判断：

- `Brief 快照`：复述你真正要解决的问题。
- `起点判断`：判断你是从零开始、有零散资料、有结构化资料，还是已有洞察/概念。
- `推荐路径`：说明下一步该进入证据采集、证据摘要、洞察策略、Idea Platform 还是 Concept。
- `证据准备模式`：默认连续完成证据采集和证据摘要；需要时可改为先审计证据。
- `如何介入`：告诉你如何暂停、深入、回退或查看资料池。
- `当前需要补充的信息`：最多问三个问题；不阻塞的问题会先标注默认假设继续推进。

启动包会保留用户原始 brief、当前判断、缺失输入和推荐路径，避免下层 skill 只收到压缩摘要而丢失原始意图。

## 两种起点

如果你没有资料，只给了品牌、品类或传播问题，慢策会从证据采集开始：

```text
Brief -> Evidence Collection -> Evidence Summary -> Insight Strategy -> Idea Platform -> Concept
```

如果你已经有链接、截图、调研笔记、评论导出或报告，慢策会先整理资料：

```text
Brief -> Evidence Summary / Normalize -> Insight Strategy -> Idea Platform -> Concept
```

如果你已经有 structured evidence pool、social listening 报告或已有洞察，慢策可以直接进入 `insight-strategy`，并在证据不足时标注 provisional，而不是假装已经有最终结论。

## 证据准备

证据准备由两个独立 skill 完成，但默认对用户呈现为一个连续阶段：

- `web-evidence-collector` 负责找资料、记录来源、建立 evidence pool。
- `evidence-summary-analysis` 负责清洗、分类、归纳证据模式和交付 Strategy Readiness Pack。

证据准备阶段不会产出最终洞察、定位、Idea Platform 或 Concept。它只回答：

- 证据是否足够进入策略判断？
- 来源覆盖了哪些平台和材料？
- 哪些证据强，哪些只是弱线索？
- 品牌硬信息是否足够支撑 Level 4？
- 还有哪些缺口需要用户确认？

默认输出会压缩成内容条和证据准备简报；完整资料保存在后台资料池中。

## Insight Reality 策略推导

0.7.9 的核心升级是 `insight-strategy`。它把策略推导拆成四层：

```text
Level 1: Fact Layer
Level 2: Motive Inference
Level 3: Cultural Judgment
Level 4: Strategic Decision
```

- `Fact Layer`：只看证据，整理主题、信号、原话和来源。
- `Motive Inference`：从证据推断情绪、需求、压力、恐惧、渴望和 human truth。
- `Cultural Judgment`：用 `What is / What should be / Why now` 提炼文化张力。
- `Strategic Decision`：把文化张力连接到品牌真相和可证明优势，形成策略选择。

默认治理逻辑是：

```text
Idea Platform = Cultural Tension x Brand Truth x Proof Edge
```

这意味着一个好的 Idea Platform 不是一句漂亮口号，而是三件事同时成立：

- 有真实的文化张力；
- 品牌有可信的立场或真相；
- 品牌能用产品、服务、行为、渠道或内容证明它。

如果品牌事实、产品 proof、品牌行为或竞品差异不够，系统会把策略标为 `Provisional`，并说明应该回到哪个上游环节补证据。

## Strategy Models Library

0.7.9 新增 Strategy Models Library。它不是用来替代默认模型，而是在 Level 4 需要对照、分歧或更清晰路线时，帮助选择推导方式。

当前可用的策略路线包括：

- `Default Idea Platform`：默认路线，用文化张力、品牌真相和 proof edge 生成战略平台。
- `奥美品牌大理想`：适合需要 belief-led、文化观点更强的品牌平台。
- `奥美品牌定位三角`：适合定位不清，需要明确 audience、category、reason-to-believe。
- `3C Strategy Triangle`：适合从 customer、company、competitor 检查战略适配。
- `奥美蝴蝶方阵 The Butterfly`：适合连接品牌定义、中心平台和表达系统。
- `USP / SMP / ESP`：适合把战略收紧成单一功能、情绪或传播主张。
- `Challenger Brand`：适合挑战者品牌打破品类惯例。
- `Cultural Branding`：适合由社会矛盾、身份压力或文化冲突驱动的项目。
- `Golden Circle`：适合创始人信念、品牌使命或 purpose 较强的品牌。
- `Brand Key / Essence`：适合压缩品牌核心。
- `Jobs To Be Done`：适合行为和需求驱动的证据包。
- `Get / To / By / So`：适合把策略转成行动导向的传播桥梁。

无论使用哪条模型路线，最终都会回到统一的 `Idea Platform Record`，避免模型越多，输出越散。

## Idea Platform 与 Concept

慢策区分 `Idea Platform` 和 `Concept`。

- `Idea Platform` 是战略平台，回答品牌应该代表什么、回应什么张力、凭什么能拥有这个方向。
- `Concept` 是表达路线，回答某个 campaign、内容、体验、活动或触点应该怎么说、怎么做。

用户说 `Big Idea` 时，系统会兼容理解，但正式工作术语统一为 `Idea Platform`。

## Message House

0.7.9 新增 Concept and Message House 工作指南。它用于 Idea Platform 之后，把 Concept 变成更清晰的信息结构。

```text
Idea Platform
  -> Concept A -> Message House
  -> Concept B -> Message House
  -> Concept C -> Message House
```

每个 Concept 使用一个 Message House：

- `Roof`：这个 Concept 的单一核心主张。
- `Pillars`：2-3 个支撑主张，解释 Roof 为什么成立。
- `Foundation`：支持 Pillars 的事实、产品 proof、品牌行为、证据来源或案例。

如果 Roof 没有 Foundation 支撑，Concept 会被标为薄弱或 provisional。Message House 的作用不是写执行文案，而是确保概念表达有结构、有证据、有边界。

## 如何暂停并深入某个阶段

使用明确的阶段指令，不使用 `@`，避免和 Codex 或其他工具的 mention 机制混淆。

- `进入：证据采集`：调整调研范围、平台、深度、证据缺口。
- `进入：证据摘要`：讨论分类、材料模式、来源偏斜、弱信号。
- `进入：策略洞察`：讨论 human truth、cultural tension、brand truth、proof edge、战略选择。
- `进入：Idea Platform`：展开、比较、压力测试或重写 Idea Platform。
- `进入：Concept`：展开、比较、压力测试或重写 Concept。
- `查看：资料池`：查看、重组或审计完整后台资料。
- `回退到：证据摘要`：退回某个阶段重新处理。
- `继续`：恢复主流程。

当用户输入这些指令时，总控会暂停继续推进，把用户原话、当前判断和相关资料池一起带入该环节。

## 前台输出和后台资料池

每个阶段都分成两层：

- `前台输出`：对话中直接给用户看的短结果，用来判断下一步。
- `后台资料池`：总控维护的结构化项目记忆，保留证据、摘要、洞察图、策略候选、Idea Platform、Concept 记录和开放问题。

总控压缩的是阅读负担，不压缩证据、判断依据、矛盾、置信度和开放问题。

真实项目默认会导出或维护 Markdown 资料池文件，但不会在对话中刷出全文。用户输入 `查看：资料池` 时，可以展开完整资料池或某个部分。

## 0.7.9 新增内容

- 升级基于 Insight Reality 能力的策略推导模型，强化从事实层、动机推断、文化张力到战略选择的完整路径。
- 新增 Strategy Models Library，用于在 Level 4 阶段进行策略模型选择、对照和推导。
- 新增 Concept and Message House 工作指南，将 Idea Platform 之后的 Concept 展开为 Roof、Pillars、Foundation 和 proof 结构。
- 扩展 Brand Facts Pack、Idea Platform Record 与 Concept Record 模板，增强策略判断、概念记录和 provisional/final 判断。
- 增加中文情绪、动机、同义词和平台黑话 starter lexicon，以及真实项目语料扩词说明。
- 强化 `web-evidence-collector` 的证据准备输出、品牌硬信息线索、来源覆盖统计和下游 handoff。

## 当前状态

慢策仍处于 Draft / Alpha 阶段。它已经可以作为内部工作流测试，但正式公开发布前仍建议继续补充真实 Evidence Pool、真实品牌资料包、旧策略卡片样式、真实匿名项目和行业语料。
