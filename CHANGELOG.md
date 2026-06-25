# Changelog

## 0.7.0

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
