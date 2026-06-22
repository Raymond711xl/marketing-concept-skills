# 慢策｜Marketing Concept Skill

写方案的前半程，有 AI 陪你慢慢跑。

Version: 0.7.0  
Status: Draft / Alpha  
License: MIT

慢策是一个面向中文品牌、中文网络环境和营销策略工作的 skill 组合包。它不急着直接给一句广告语，而是陪你把方案前半程跑扎实：从 brief 出发，经过证据采集、证据摘要、洞察策略和 Idea Platform 推导，最终形成一个可以继续讨论、修改和执行化的 Concept。

这里的 `Idea Platform` 可以理解为广告策略语境中常说的 Big Idea，但本系统统一使用 `Idea Platform`：它是从洞察策略进入 Concept 前的战略平台，不是最终创意概念本身。

当前版本是 `0.7.0`，仍处于 Draft / Alpha 阶段。它可以作为内部工作流使用，但正式公开发布前仍需要继续验证真实项目、整理示例和清理草稿文件。

## 核心路径

```text
Brief -> 证据采集 -> 证据摘要 -> 洞察策略 -> Idea Platform -> Concept
```

慢策只处理方案的前半程。Concept 之后的文案、视觉、KV、脚本、提案、执行物料暂时不属于当前系统。

## 包含哪些 Skill

- `concept-strategy-controller`：总控。负责读 brief、判断路线、压缩阶段输出、维护后台资料池，并把任务交给合适的下层 skill。
- `web-evidence-collector`：证据采集。负责公开网络资料、平台线索、素材、报道、社媒线索和 evidence pool。
- `evidence-summary-analysis`：证据摘要。负责清洗资料、分类、归纳证据模式，不做最终策略判断。
- `insight-strategy`：洞察策略。负责从证据进入 human truth、cultural tension、Idea Platform 和战略建议。

## 适合什么场景

- 从零开始做一个品牌或 campaign 的策略研究。
- 已有链接、截图、笔记、评论、报告，需要先整理成资料池。
- 想从竞品、社媒、PR、视频、视觉物料中提炼证据模式。
- 想从证据推导人群动机、文化张力、品牌立场和 Idea Platform。
- 想把 Idea Platform 收束成一个 Concept。
- 想在某个阶段停下来，单独讨论、修改或回退。

## 不适合什么场景

- 不适合直接跳过证据和策略，要求立刻产出最终广告语。
- 不负责最终文案、视觉、KV、脚本、提案页或执行物料。
- 不绕过登录、付费墙、反爬、私域社群或平台限制。
- 不把品牌自己的说法直接当成消费者真实想法。

## 默认语言和市场规则

- 默认用中文工作和输出。
- 中文品牌、中文品类、中国市场项目，优先使用中文搜索词、中文平台和中文网络语境。
- 如果 brief 明确指定海外市场、英文交付、国际竞品、全球平台或跨境语境，再切换到英文或海外调研路径。
- 证据原文、用户原话、slogan、帖子标题、消费者评论尽量保留原语言。
- 跨 skill 的结构字段可以保留英文，例如 `Evidence Pool`、`Confidence`、`Raw quote`、`Insight Map`、`Idea Platform Record`，方便后续迁移和交接。

## 如何开始

你可以直接给总控一个 brief，例如：

```text
我想为一个新中式茶饮品牌做品牌策略，目标是让它在年轻白领中建立“更轻松的日常奖励”心智。现在没有资料，希望先从竞品和社媒调研开始。
```

总控会先形成一个轻量项目启动包：

```markdown
- 用户原始 brief:
- 品牌 / 产品 / 品类:
- 市场 / 地域 / 语言:
- 商业问题:
- 传播目标:
- 目标人群:
- 已有资料:
- 证据状态:
- 目标终点:
- 品牌硬信息状态:
- 推荐路径:
- 缺失输入:
```

这个启动包会跟随后续阶段，避免下层 skill 只收到压缩摘要而丢失用户原始意图。

如果 brief 没有提供品牌理念、愿景、slogan、品牌编年史、创始人表达、产品证明、服务证明、品牌行为或竞品差异，总控不会阻塞项目，而是把这些列为 `品牌硬信息` 采集线索。采集阶段会主动从公开资料中寻找候选证据，并标注为 `待用户确认`。

## 如何暂停并深入某个阶段

使用明确的阶段指令，不使用 `@`，避免和 Codex 或其他工具的 mention 机制混淆。

- `进入：证据采集`：调整调研范围、平台、深度、证据缺口。
- `进入：证据摘要`：讨论分类、材料模式、来源偏斜、弱信号。
- `进入：策略洞察`：讨论 human truth、cultural tension、brand truth、proof edge、战略选择。
- `进入：Idea Platform`：展开、比较、压力测试或重写 Idea Platform。用户说 `进入：Big Idea` 时，按旧称兼容处理。
- `进入：Concept`：展开、比较、压力测试或重写 Concept。
- `查看：资料池`：查看、重组、审计完整后台资料。
- `回退到：证据摘要`：退回某个阶段重新处理。
- `继续`：恢复主流程。

当用户输入这些指令时，总控会暂停继续推进，把用户原话、当前判断和相关资料池一起带入该环节。

## 前台输出和后台资料池

每个阶段都分成两层：

- `前台输出`：对话中直接给用户看的短结果，用来判断下一步。
- `后台资料池`：总控维护的结构化项目记忆，保留证据、摘要、洞察图、策略候选、Idea Platform 和 Concept 记录。

总控压缩的是阅读负担，不压缩证据、判断依据、矛盾、置信度和开放问题。

真实项目默认会导出或维护 Markdown 资料池文件，但不会在对话中刷出全文。它有三种呈现方式：

1. 默认导出或维护 Markdown 资料池文件，用于保存完整项目记录。
2. 默认在对话中只展示关键变化和当前结论，避免消耗过多上下文。
3. 当用户输入 `查看：资料池` 时，总控可以在对话中展开完整资料池或某个部分。

---

# Man Ce｜Marketing Concept Skill

The first half of proposal writing, paced slowly with AI.

Version: 0.7.0  
Status: Draft / Alpha  
License: MIT

Man Ce is a Chinese-first skill bundle for brand strategy and marketing concept development. It helps users move from a rough brief to evidence collection, evidence summary, insight strategy, Idea Platform, and finally a discussable Concept.

In this system, `Idea Platform` is the strategic platform before Concept. It is close to what advertising teams often call a Big Idea, but it is not the final creative concept itself.

This project is currently a `0.7.0` draft. It can be used as an internal workflow, but should still be validated on real projects before public release.

## Core Flow

```text
Brief -> Evidence Collection -> Evidence Summary -> Insight Strategy -> Idea Platform -> Concept
```

Man Ce only covers the first half of proposal work. Copywriting, visual design, scripts, proposal decks, and execution assets after Concept are outside the current system.

## Skills

- `concept-strategy-controller`: the front-stage controller. It reads the brief, chooses the route, compresses stage progress, and maintains the backstage dossier.
- `web-evidence-collector`: collects traceable public web evidence and creates an evidence pool.
- `evidence-summary-analysis`: cleans, classifies, and summarizes evidence patterns without making final strategy decisions.
- `insight-strategy`: turns a prepared evidence package into fact-layer themes, human truths, cultural tensions, Idea Platform candidates, and strategic recommendations.

## Good For

- Starting brand or campaign strategy research from zero.
- Organizing links, screenshots, notes, comments, reports, or messy research.
- Extracting evidence patterns from competitors, social platforms, PR, videos, and visual materials.
- Deriving audience motives, cultural tensions, brand stance, and Idea Platform.
- Turning an Idea Platform into a discussable Concept.
- Pausing, deepening, revising, or returning to a specific stage.

## Not For

- Jumping straight to final advertising copy without evidence or strategy.
- Producing final copywriting, visual design, KV, scripts, proposal pages, or execution assets.
- Bypassing logins, paywalls, anti-bot controls, private groups, or platform restrictions.
- Treating brand-owned claims as consumer truth.

## Language And Market Defaults

- Default working language and user-facing output: Chinese.
- For China-market work, prioritize Chinese web context, Chinese search queries, and Chinese platforms.
- Switch or adapt to English / overseas research when the brief specifies English deliverables, overseas markets, international competitors, global platforms, or cross-border context.
- Preserve original source wording where possible.
- Keep shared schema fields in English where they work as handoff contracts, such as `Evidence Pool`, `Confidence`, `Raw quote`, `Insight Map`, and `Idea Platform Record`.

## Stage Commands

Use explicit stage commands instead of `@` mentions:

- `进入：证据采集`
- `进入：证据摘要`
- `进入：策略洞察`
- `进入：Idea Platform`
- `进入：Concept`
- `查看：资料池`
- `回退到：证据摘要`
- `继续`

## Output Layers

- `Frontstage Output`: short, decision-oriented responses shown in chat.
- `Backstage Dossier`: structured project memory containing brief, evidence, summaries, insights, strategy candidates, Idea Platform records, Concept records, and open questions.

For real projects, the controller should export or maintain a Markdown dossier by default, but it should not print the whole dossier into chat unless the user asks to view it.
