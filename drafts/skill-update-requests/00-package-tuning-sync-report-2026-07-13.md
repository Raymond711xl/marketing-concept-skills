# 组合包整体调优同步报告（四 Skill 通用）

日期：2026-07-13 ｜ 面向：四个 Skill 工作对话 + 包级维护 ｜ 范围：`plugins/marketing-concept-skill/` 全部四个 skill + `scripts/validate_package.py`

结论先行：**本轮为包级调优，所有改动已直接落盘到正式源码并通过全部校验，各 Skill 对话无需执行任何修改任务。**
本报告的作用是同步认知：各对话继续工作前，请先重读自己 skill 的 SKILL.md 现状，并遵守 §3 新增的跨 Skill 约束（validator 已强制）。

使用方式：把本文件整份（或「§2 本 skill 小节 + §3」）贴给对应 Skill 对话即可。

编号对照：0 号 = concept-strategy-controller（工作文件 01）｜1 号 = web-evidence-collector（02）｜2 号 = evidence-summary-analysis（03）｜3 号 = insight-strategy（04）

## 1. 验证状态（实测，2026-07-13，改动后）

| 检查 | 结果 |
|---|---|
| `scripts/validate_package.py`（含本轮新增防漂移守护） | PASS（第一轮时为 0.8.9；第二轮升版后以 0.9.0 复验通过，含改名后新路径） |
| `insight-strategy/scripts/smoke_test_prepare_raw_evidence.py` | PASS |
| `insight-strategy/scripts/run_regression_checks.py` | 8/8 PASS |
| 四个 description 长度 | 966 / 766 / 776 / 620 字符（上限 1024；总控含第二轮新增排除句） |
| 防漂移守护负向测试（人为制造漂移应报错） | 已验证会拦截 |

## 2. 已落盘变更（按 skill）

### 2.1 concept-strategy-controller（0 号）

- **新增 `references/stage-playbooks.md`**：原 SKILL.md「分层职责」六个阶段细则、Concept 十项固定输出顺序、Message House 定义整体迁入。SKILL.md 原文 422 行 / 25.3KB 瘦身至 295 行 / 22.1KB。
- SKILL.md「分层职责」替换为**速览表**，并规定：组装 Downstream Handoff Packet 前、验收下层返回物时，必须读取 playbooks 对应小节（下层调用协议第 3 步与 Reference Map 已同步更新）。
- 「压缩契约」中重复罗列的 Concept 十字段删除，改为指向 playbooks 单一权威版本。
- 前台五个内容条名称对齐 `evidence-summary-analysis` 版本（`品牌硬信息内容条`、`进入策略判断内容条`；原「品牌硬信息候选内容条」「是否进入策略洞察内容条」为漂移写法，已废弃）。
- `references/startup-packet.md` 中与 SKILL.md 逐字重复的「介入说明」固定文案改为指针；**该文案唯一来源 = SKILL.md「第一次 Brief 反馈」**，validator 已锚定。
- description 增补触发词：慢策、品牌策略、传播策略、接 brief / 新项目启动。

### 2.2 web-evidence-collector（1 号）

- SKILL.md「Output Contract」中 23 项扩展字段清单收敛为要点 + 指针；**完整清单与允许值唯一来源 = `references/04-evidence-pool-contract.md`**。
- 「Intake Defaults」中 subagent 同意话术副本删除（该副本已与 `references/10-subagent-collection-mode.md` 发生措辞漂移：cost/use）；**同意话术唯一来源 = 10 号文件**。
- description 增补触发词：证据采集、竞品调研、品牌调研、社媒调研、舆情素材收集、案头调研、找资料/收集资料。

### 2.3 evidence-summary-analysis（2 号）

- SKILL.md §4 五个内容条名称下新增声明：**这五个名称是与总控的前台显示契约，必须逐字稳定**（validator 已在两个 SKILL.md 双向锚定）。
- `references/01-evidence-pool-schema.md` Confidence Rules 两处措辞对齐 collector `Evidence Pool v1` 规范文本（"only one weak source"、"not confirmed"）。
- description 增补触发词：证据摘要、资料整理、资料清洗、调研资料归纳、证据分类、客户版研究报告。

### 2.4 insight-strategy（3 号）

- description 增补触发词：洞察策略、人性洞察、文化张力、策略推导、品牌真相、概念推导、Big Idea。
- Resource Map 中 lexicon 逐文件列表并为一条目录级描述（文件本身未动）。
- 本轮**未触碰**：模板、examples、词库内容、回归脚本——2026-07-13 真实物料校准工作（见 04 号同步报告）完好。

### 2.5 包级

- `CHANGELOG.md` 新增「Unreleased」段记录本轮全部改动。
- `AGENTS.md` 校验命令清单补入 `run_regression_checks.py`。
- `scripts/validate_package.py` 升级，详见 §3。

## 3. 新增跨 Skill 约束（重要：后续任何修改必须满足，validator 强制）

1. **同步区块**：`web-evidence-collector/references/04-evidence-pool-contract.md` 与 `evidence-summary-analysis/references/01-evidence-pool-schema.md` 的 `## Allowed Values`、`## Confidence Rules` 两节必须逐词一致（忽略换行差异）。
   ⚠️ 这与各工作文件「只修改本 skill」的约束存在一个例外：**若要改这两节，必须同一轮镜像修改另一个 skill 的对应节**，或把改动上报包级维护统一处理。单边修改会导致 validator 失败。
2. **内容条名称**：五个内容条名称必须同时存在于总控和摘要两个 SKILL.md 中，逐字一致。
3. **固定文案锚点**：总控 SKILL.md 必须保留「你可以随时输入阶段指令来单独深入讨论……」介入说明；`stage-playbooks.md` 必须保留 Concept 十项字段名。
4. **description 规则**：≤1024 字符（超出即报错）；无中文字符会产生警告（中文优先包的触发要求）。
5. **体量预警**：SKILL.md 超过 24KB 产生警告（正文全量随触发进入上下文；新增细则请放 references/ 并写明读取时机）。
6. 原有锚点不变：总控职责声明句、Research Configuration 三字段、`Evidence Pool v1` 追踪字段等仍被锚定。

修改任何 skill 后照旧运行：`python3 scripts/validate_package.py`（现在会顺带守护以上全部约束）。

## 4. 用户侧决策状态（第二轮已处理，见 §6）

1. ✅ 版本升级 0.9.0 + 重跑 `build_release.py` —— 第二轮完成。
2. ✅ description 触发实测 —— 自动路测因本机 CLI 未登录暂缓（工具已入库，见 §6），已用人工边界审计替代并修复一处缺陷。
3. ✅ 文件夹改名、`agents/openai.yaml` 中文化 —— 第二轮完成；`firecrawl-cli-README.zh-CN.md` 按用户要求保留不动（另一 skill 的测试背景）。

## 5. 变更文件清单（第一轮）

- `concept-strategy-controller/SKILL.md`、`references/stage-playbooks.md`（新增）、`references/startup-packet.md`
- `web-evidence-collector/SKILL.md`
- `evidence-summary-analysis/SKILL.md`、`references/01-evidence-pool-schema.md`
- `insight-strategy/SKILL.md`
- 包级：`scripts/validate_package.py`、`CHANGELOG.md`、`AGENTS.md`

## 6. 第二轮增补（同日，版本发布向）

- **版本 0.8.9 → 0.9.0**：`skill-package.json`（含 release_artifact）、双端 plugin.json、根 `.claude-plugin/marketplace.json`、README 中英双份（含 0.9.0 发布更新章节与「当前状态」的诚实措辞：安装侧复验待重跑）、`plugins/.../README.md`、`AGENTS.md`、`CHANGELOG.md`（Unreleased 并入 0.9.0）。
- **`build_release.py` 产出** `dist/marketing-concept-skills-0.9.0.zip` + sha256（0.8.9 旧包保留）。
- **四份 `agents/openai.yaml`**：`short_description`、`default_prompt` 中文化；`display_name` 保持 canonical 英文名。
- **总控 description 补排除句**（人工边界审计发现：其余三个 skill 均有 not-for 子句，唯独总控没有，Concept 后的文案/KV/执行请求易被误路由给它）："Do not use for standalone copywriting, KV or visual design, or execution-only asset requests; this workflow ends at Concept."
- **`drafts/tools/trigger_test.py`（新增，插件外）**：16 条语料的 description 路由判别测试，路径无关。前置条件：终端先 `claude login` 一次。
- **仓库文件夹**由 `conpect skills` 改名为 `concept skills`。⚠️ 各工作对话如引用旧绝对路径需更新；如曾按绝对路径 add 本地 marketplace 需重新 add。

以上两轮改动均未 commit，可用 `git diff` 逐项审阅。
