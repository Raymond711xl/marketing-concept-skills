# Changelog

## 0.9.0

- 版本升级：`skill-package.json`、双端 plugin manifest、根 marketplace 清单、README 中英双份与 AGENTS.md 同步升至 0.9.0；`release_artifact` 指向 0.9.0 ZIP。
- 四份 `agents/openai.yaml` 的 `short_description` 与 `default_prompt` 改为中文优先（display_name 保持 canonical 英文名）。
- description 触发实测：以四份 name+description 做路由判别测试并按结果微调。
- 总控 SKILL.md 瘦身：将「分层职责」六个阶段细则、Concept 十项固定输出顺序与 Message House 定义下沉到新增的 `references/stage-playbooks.md`，SKILL.md 保留阶段速览表与读取指令（422 行 / 25.3KB 降至约 295 行 / 22.1KB）。
- 消除重复维护的固定文案：startup-packet 的介入说明改为指向 SKILL.md 单一来源；采集 skill 的 subagent 同意话术改为指向 `10-subagent-collection-mode.md` 单一来源（此前两份副本已出现措辞漂移）。
- 对齐跨 skill 契约漂移：前台五个内容条名称统一为 `evidence-summary-analysis` 版本；`01-evidence-pool-schema.md` 的 Confidence Rules 措辞对齐 `Evidence Pool v1` 规范文本。
- 四个 skill 的 description 增补中文触发词（慢策、证据采集、竞品调研、资料整理、洞察策略、文化张力等），改善中文语境下的触发率。
- 采集 SKILL.md 的 23 项扩展字段清单收敛为要点加指针，完整清单以 `04-evidence-pool-contract.md` 为准。
- validator 升级为防漂移守护：新增 Allowed Values / Confidence Rules 双份 schema 同步检查、内容条名称跨 skill 检查、介入说明与 Concept 十项锚点检查、description 长度（≤1024）与中文触发词检查、SKILL.md 字节数预警。
- Insight Strategy 完成 Evidence Pool v1 对齐：统一 Audience、Observation、稳定 ID、Readiness 状态映射与 Strategy Readiness Pack 双形态等价规则，强化基于 Insight Reality 的策略推导链路。
- 使用真实公开品牌证据包和 128 行中文平台原声完成上游交接验证，补充 Unavailable / Provisional / Final 判断锚点与 8 项自动回归检查。
- 基于真实语料扩充中文停用词、同义词、情绪、动机和平台俚语词库，并强化 CSV / TSV / TXT、词库加载、工作目录无关性与 `.xls` 防误用 smoke test。
- 固化 Idea Platform 与 Concept Card 的命名偏好、Message House 三层双语字段，以及推荐 Concept、备选方向和 proof gaps 的 dossier 写回合同。
- 新增包级触发测试工具与同步报告；真实客户或品牌的校准原始材料继续保留在被忽略的 `drafts/real-materials/` 中，不进入插件和仓库。

## 0.8.9

- 将四个 Skill 封装为一个标准可安装的 `marketing-concept-skill` 插件。
- 新增 Codex `.codex-plugin/plugin.json` 与仓库级 marketplace 清单。
- 新增 Claude Code `.claude-plugin/plugin.json` 与 marketplace 清单，四个 Skill 共用同一份源码。
- 将正式 Skill 源码统一迁移到 `plugins/marketing-concept-skill/skills/`，并保留根目录兼容入口。
- 将内部中文审阅稿与 Insight Strategy backlog 移出用户安装包。
- 新增 Codex、Claude Code 的安装与调用说明。
- 新增便携式 package validator、release ZIP builder 与 GitHub Actions 校验流程。
- 在隔离环境中完成 Codex 与 Claude Code 的 marketplace 添加、插件安装和解压后复验。
- 增加四份独立 Skill 修改需求，供对应工作对话继续完善内容链路。
- 统一四个 Skill 的跨阶段合同：Research Lens 与 Delivery Mode 从启动包贯穿到证据摘要，Evidence Pool 追踪字段无损交接，Insight Strategy 负责 Idea Platform 后的 Concept Package，并按总控 dossier 的固定章节写回。

## 0.7.9

- 完成 `慢策 / Marketing Concept Skill` 组合包的整体结构搭建。
- 完成前期提案所需的策略结构和策略工具结构，包括总控、证据采集、证据摘要、洞察策略、Idea Platform 和 Concept 路径。
- 持续优化 prompt 对策略工具的执行引导，减少无效推进和过长上下文依赖。
- 增加中文优先、中文网络环境优先的工作规则。
- 增加阶段指令，避免使用 `@` 造成 Codex 或其他工具的 mention 机制混淆。
- 增加后台资料池机制，用于保留真实项目中的完整推导记录。
- 明确证据采集和证据摘要不合并，但默认作为连续的「证据准备」阶段运行，并通过内容条、证据准备简报和 dossier 链接呈现。
- 将品牌理念、愿景、slogan、编年史、创始人表达、产品/服务证明、品牌行为和竞品差异前置为 Level 4 硬信息采集线索。
- 强化 `web-evidence-collector` 的证据准备输出，补充品牌硬信息线索、campaign linkage、来源覆盖统计、证据缺口和下游 handoff 结构。
- 扩展 `insight-strategy` 的 Level 4 支撑材料，新增 Brand Facts Pack 模板，用于承接 brand truth、proof edge、品牌行为和竞品差异。
- 新增可选 Strategy Models Library，并明确它只作为 Level 4 的模型选择和对照工具；默认治理逻辑仍为 `Idea Platform = Cultural Tension x Brand Truth x Proof Edge`。
- 新增 Concept and Message House 工作指南，将 Idea Platform 之后的 Concept、Roof、Pillars、Foundation 和 proof 结构纳入后续概念展开。
- 展开 Idea Platform Record 与 Concept Record 模板，增加字段命名偏好、推导路线、证据来源、Message House、评估维度和 provisional/final 判断。
- 增加中文情绪、动机、同义词和平台黑话的 starter lexicon 体系，并补充真实项目语料扩词与授权边界说明。
- 增加 skincare 构造样例、Brand Facts Pack 样例、golden case 与 regression case 模板，用于后续真实项目回归测试。
- 记录 Insight Strategy 后续 backlog，包括真实 Evidence Pool、真实品牌资料包、旧策略卡片样式、真实匿名项目和行业语料补充。
- 增加 README、AGENTS、MIT License、package metadata 和 dossier 目录说明。
