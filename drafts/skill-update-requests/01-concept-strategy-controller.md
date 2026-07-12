# Concept Strategy Controller 修改需求

将下面内容作为该 Skill 对话的修改任务。只修改 `concept-strategy-controller`，不要改其他 Skill、插件 manifest、README 或版本号。

正式路径：`plugins/marketing-concept-skill/skills/concept-strategy-controller/`

## 目标

让总控在安装后的多 Skill 环境中稳定路由、保存状态、恢复项目，并完整承接 Concept 与 Message House，而不是只靠自然语言暗示“调用了下层 Skill”。

## 必须修改

1. 增加明确的下层调用协议。
   - 路由到某一阶段时，明确要求加载对应已安装 Skill。
   - 如果平台无法加载，输出 `Downstream Handoff Packet`，不得假装专业 Skill 已完成。
   - 保留用户原始 brief、总控判断、相关 dossier 和本次任务边界。
2. 增加触发优先级与直接深入规则。
   - 完整项目默认由总控接管。
   - 用户明确进入单阶段时，允许直接使用对应下层 Skill，并保留回到总控的入口。
   - 避免总控和下层 Skill 对同一请求重复产出。
3. 对齐 Concept 与 Message House。
   - Concept 前台结果和 dossier 中都加入 `Roof`、`Pillars`、`Foundation`、`Proof gaps`。
   - 保留 Concept name、one-line concept、audience role、expression territory、risk 和 confidence。
4. 增加项目恢复协议。
   - 支持从已有 backstage dossier 恢复当前阶段、已确认决策、开放问题和下一步。
   - 增加明确动作，例如 `恢复项目：<dossier path>`。
5. 明确 dossier 输出位置。
   - 默认写到用户当前工作区的 `dossiers/[project-slug]/`。
   - 不写入插件安装目录或插件缓存。
   - 无文件写入能力时退化为结构化对话记忆。
6. 删除或更新“未来再打包”的旧提醒，因为 0.8.9 已完成 Codex / Claude 插件封装。

## 验收场景

- 零资料 brief 能进入证据采集并真实交接。
- 用户输入 `进入：策略洞察` 后只聚焦该阶段。
- 用户输入 `继续` 后恢复主流程而不丢原始 brief。
- 从 dossier 恢复后能说清当前阶段、可靠判断、待确认项与下一步。
- Concept 输出与 backstage dossier 都完整保留 Message House。
- 运行 Skill validator 并报告修改文件与测试结果。
