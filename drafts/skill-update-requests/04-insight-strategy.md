# Insight Strategy 修改需求

将下面内容作为该 Skill 对话的修改任务。只修改 `insight-strategy`，不要改其他 Skill、插件 manifest、README 或版本号。

正式路径：`plugins/marketing-concept-skill/skills/insight-strategy/`

> **2026-07-13 状态更新**：原六项必改任务经真实物料验证后 **全部完成**（逐项核销见下）。
> 真实物料验证过程新发现三项待办（见「新增待办」），另有若干用户侧设计决策不属于本文件范围。
> 完整验证报告：`04-insight-strategy-sync-report-2026-07-13.md`（同目录）。

## 目标

把已有 Insight Reality 路径真正闭环到 Concept Package，并修复模型模板、lexicon、原始数据脚本和回归测试之间尚未接通的部分。

## 原必改任务（2026-07-13 逐项核销）

1. ~~补齐最终 Concept Package~~ ✅ 完成。`concept-package-template.md` + `concept-record-template.md` 就位，
   回归 `end-to-end-level1-to-concept` 与 `dossier-writeback-shape` 通过；真实品牌全流程试跑（公开数据案例）
   产出完整 Package（推荐+备选、Message House、proof gaps PG-01–04、风险 R-01–04、Provisional 状态判定）。
2. ~~对齐 Message House~~ ✅ 完成。Roof/Pillars/Foundation + Evidence ID 结构在真实案例中验证；
   卡片命名偏好已由用户确认并固化进模板 §0（概念卡 Concept Card；核心主张 (Roof)/支撑点 (Pillar)/RTB (Foundation)；双语；Campaign 风概念命名）。
3. ~~完整接入 Strategy Models Library~~ ✅ 完成（工程侧）。`Derivation route` 12 路线枚举，回归
   `strategy-model-route-coverage` 通过。⚠️ 用户侧设计决策仍开放：支持模型清单的最终 enumerate 与
   Concept usage models 定义（TODO backlog §A/§D，非本文件范围）。
4. ~~修复原始数据适配器~~ ✅ 完成。smoke test 断言 cwd 无关性、CSV/TSV/TXT 无依赖、`.xls` guard、可选依赖行为，通过。
5. ~~真正加载 bundled lexicons~~ ✅ 完成（本条在验证时发现早已实现，属过期任务）。现行脚本加载全部 7 项词库资产并输出 load summary。
   另：2026-07-13 词库已用真实语料扩充（用户逐项批准，license-clean）：停用词 14→18、同义词 5→21、
   情绪 38→44、动机 27→33、平台俚语 7→19；扫描命中率显著提升（情绪 5→10、动机 0→5、俚语 2→12）。
6. ~~整理 examples 与 eval~~ ✅ 完成。SKILL.md 已声明 examples 为开发资源不在运行时读取；
   三类回归（zero-material-unavailable / thin-evidence-provisional / 完整 Concept 链）全部存在并通过。

## 新增待办（真实交接验证发现，2026-07-13）

依据：`drafts/review-notes/real-handoff-validation-proya.md`

1. **Schema 漂移修复**：`examples/sample-evidence-pool*.md` 与 `assets/templates/evidence-pool-template.md`
   与 collector 的 `Evidence Pool v1` 契约不一致——`Audience / segment` 应为 `Audience`、缺 `Observation`、
   使用无前缀 `E001` ID、混入下游 coding 字段（`Insight lens`/`Matched keywords`）。
   二选一：对齐 v1 契约，或在模板顶部显式声明「本地简化形，真实交接以 collector 契约为准」。
2. **Readiness 状态词表映射声明**：三套词表并存（evidence-summary：`ready / ready with caveats / needs more evidence`；
   输入契约：`Ready / Partial / Unavailable`；brand-facts-pack：`Ready / Partial / Thin`）。
   在 `01-input-package-contract.md` 增加一段显式映射，避免下游各自解释。
3. **Strategy Readiness Pack 双形态等价声明**：上游 6 列表格形态 vs `input-package-template.md` 字段列表形态，
   语义一致但契约未声明等价——补一句声明即可。

## 边界（不变）

- 不自行执行开放网络调研。
- 不把高频词直接当作 insight。
- 不为了得到 Final 而虚构 brand truth、proof edge 或 competitor difference。
- **新增**：`drafts/real-materials/` 为本地校准资产（已 gitignore），不得移入 examples/、不得随插件分发、不得写入 SKILL.md 叙述。

## 验收（2026-07-13 实测状态）

- ✅ 从 Strategy Readiness Pack 稳定产出 Level 1-4、Idea Platform 和 Concept Package（真实公开品牌案例全流程验证）
- ✅ 主要判断与 Foundation 均回指 Evidence ID
- ✅ `validate_package.py` 通过（0.8.9）；5 项回归通过；smoke test 通过
- ✅ 真实物料清单（物料 1/3/5）全部交付，判断尺度现有五个锚点（详见 sync report）
- 仍需用户决策（非工程）：TODO backlog §A（推导模型清单/Concept usage models）、§D 勾销确认、
  §C（极简 sample-evidence-pool.md 去留）、卡片单页版式与新旧措辞偏好
