# Insight Strategy 修改需求

将下面内容作为该 Skill 对话的修改任务。只修改 `insight-strategy`，不要改其他 Skill、插件 manifest、README 或版本号。

正式路径：`plugins/marketing-concept-skill/skills/insight-strategy/`

## 目标

把已有 Insight Reality 路径真正闭环到 Concept Package，并修复模型模板、lexicon、原始数据脚本和回归测试之间尚未接通的部分。

## 必须修改

1. 补齐最终 Concept Package。
   - 最终报告不能停在 Idea Platform。
   - 加入推荐 Concept、备选 Concept、Message House、证据支撑、Proof gaps、风险和 Final / Provisional 状态。
   - 输出格式应能直接写入总控 backstage dossier。
2. 对齐 Message House。
   - 每个 Concept 保留 `Roof`、2-3 个 `Pillars`、`Foundation` 和证据 ID。
   - Foundation 不能只写形容词，必须回到产品、服务、品牌行为或证据。
3. 完整接入 Strategy Models Library。
   - `Idea Platform Record` 的 `Derivation route` 覆盖已公开支持的路线。
   - 模型只作为 Level 4 推导路线，默认治理逻辑仍为 `Cultural Tension x Brand Truth x Proof Edge`。
4. 修复原始数据适配器。
   - 命令路径相对当前 Skill 目录解析，不假设用户位于插件目录。
   - 明确 CSV/TSV/TXT 的无依赖支持；修正 `.xls` 与 `openpyxl` 的错误预期。
   - 明确 `openpyxl`、`jieba` 的可选依赖和缺失时行为。
5. 真正加载 bundled lexicons。
   - 脚本应使用 stopwords、emotion、motive、synonym、tension domain、platform slang 等已有资产，或删除“脚本已使用”的错误说明。
   - 保持授权干净，不捆绑来源不明的第三方词典。
6. 整理 examples 与 eval。
   - 明确 golden case 在何时读取，或将纯开发样例排除在运行资源之外。
   - 增加零资料不可用、证据薄弱必须 Provisional、完整 Concept + Message House 三类回归检查。

## 边界

- 不自行执行开放网络调研。
- 不把高频词直接当作 insight。
- 不为了得到 Final 而虚构 brand truth、proof edge 或 competitor difference。

## 验收

- 从 Strategy Readiness Pack 能稳定产出 Level 1-4、Idea Platform 和 Concept Package。
- 每个主要判断和 Message House Foundation 都能回指 Evidence ID。
- 脚本 smoke test、Skill validator 和至少一个端到端回归场景通过。
- 报告修改文件、测试结果和仍需用户提供的真实材料。
