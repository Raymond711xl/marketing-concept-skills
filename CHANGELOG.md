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
- 增加 README、AGENTS、MIT License、package metadata 和 dossier 目录说明。
