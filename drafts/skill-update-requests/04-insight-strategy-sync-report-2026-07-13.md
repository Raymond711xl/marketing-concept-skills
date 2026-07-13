# Insight Strategy 真实物料补齐 & 验证同步报告

日期：2026-07-13 ｜ 面向：Codex 协作 agent ｜ 范围：`plugins/marketing-concept-skill/skills/insight-strategy/`
结论先行：**原修改需求六项全部完成并经真实数据验证；真实物料清单（物料 1/3/5）清零；
新增三项小型工程待办（schema 对齐类）；其余为用户侧设计决策。**

## 1. 验证状态（实测，2026-07-13）

| 检查 | 结果 |
|---|---|
| `scripts/validate_package.py` | PASS（marketing-concept-skill 0.8.9） |
| `insight-strategy/scripts/run_regression_checks.py` | 5/5 PASS（zero-material / thin-evidence / e2e-concept / route-coverage / dossier-shape） |
| `insight-strategy/scripts/smoke_test_prepare_raw_evidence.py` | PASS（CSV/TSV/TXT、词库加载、cwd 无关、.xls guard） |
| 输入契约 Acceptance Check（真实数据） | 9 项中 7 项通过，2 项缺口如实标记（详见 §3） |

## 2. 本轮完成的工作

### 2.1 真实物料清单清零（TODO backlog §B）

- **物料 1（真实上游交接）**：用真实公开品牌（珀莱雅，纯公开网络数据）构建了 30 条
  `Evidence Pool v1` 合规证据池 + Strategy Readiness Pack + Brand Facts Pack，走通输入契约验证；
  另采集 128 行小红书/天猫真实评论经 `prepare_raw_evidence.py` 适配为 RAW-### 分片，双通道交接均验证。
- **物料 3（卡片命名）**：用户逐项确认并已固化进两个模板 §0——卡片标题 Idea Platform（保持英文）/
  概念卡 Concept Card；三层双语：核心主张 (Roof)、支撑点 (Pillar)、RTB (Foundation)；概念命名 Campaign 风。
  尾巴：单页版式与 preserve/avoid 措辞待用户后续确认。
- **物料 5（真实校准案例）**：两个真实项目匿名化后建成 GC-02、GC-03（代号说明见 §4）。

### 2.2 词库扩充（license-clean，全部用户批准）

真实语料（小红书 92 行 + 天猫 36 行）提取候选词 34 项入库：
停用词 14→18、同义词 5→21、情绪 38→44、动机 27→33、平台俚语 7→19。
适配器扫描命中率：情绪 5→10、动机 0→5、俚语 2→12。原声出处留存于候选审阅表。

### 2.3 判断尺度校准——现有五个锚点

| 锚点 | 输入特征 | 理想 status | 教学点 |
|---|---|---|---|
| regression-zero-material | 空输入 | Unavailable | 停在 Level 1 前 |
| GC-01 屿白（虚构） | Brand Facts Partial | Provisional | 不虚构补 Final |
| 珀莱雅真实公开包 | 品牌硬事实密、原声后补、关键项未核验 | Provisional | 证据漂亮也不虚报；升级路径明确（PG-01 已由语料解决，PG-02/03 待核验） |
| GC-02（真实中标案，匿名） | 品牌自供材料、客户已买单、人群洞察为分析师断言 | Provisional | **商业成功 ≠ 证据充分**；分析师断言 ≠ 消费者洞察 |
| GC-03（真实比稿案，匿名） | 张力证据在 brief 内（客户自供）、双平台候选、客户未拍板 | **平台 Final / 概念 Provisional** | 分层状态判定；**客户内部未决 ≠ 证据不足**；单推纪律 + 备选反超条件 |

GC-02/03 的镜像对照是核心校准资产：同一条规则（张力必须有输入包内证据）在两个方向上各有真实锚点。

## 3. 新增工程待办（建议 Codex 接手，小改动）

依据 `drafts/review-notes/real-handoff-validation-proya.md`（真实数据暴露）：

1. **Schema 漂移**：insight-strategy 的 examples 与本地 evidence-pool 模板和 collector `Evidence Pool v1`
   契约不一致（`Audience / segment`→`Audience`；缺 `Observation`；`E001` 无前缀 ID；混入下游 coding 字段）。
   修复方式二选一：对齐 v1，或模板顶部声明「本地简化形」。
2. **Readiness 词表三套并存**：在 `references/01-input-package-contract.md` 补显式映射
   （ready/ready with caveats/needs more evidence ↔ Ready/Partial/Unavailable ↔ Ready/Partial/Thin）。
3. **Strategy Readiness Pack 双形态**：表格形态与字段列表形态补一句等价声明。

已同步更新至工作文件 `04-insight-strategy.md`「新增待办」节。

## 4. 本地校准资产的边界（重要，请遵守）

- `drafts/real-materials/` 已加入 `.gitignore`（2026-07-13），包含：珀莱雅原始引文与语料、
  GC-02（跨境支付 × 国际网球赛事赞助，真实中标案匿名版）、GC-03（全球润滑油 × 顶级赛事周双轨激活，真实比稿案匿名版）。
- 按项目所有者要求：这些资产**不进 `examples/`、不随插件分发、不写入 SKILL.md 叙述**，仅在本机用于校准。
- 若需把 GC-02/03 纳入自动回归：建议在 `run_regression_checks.py` 增加「本地 case 目录存在则附加运行」的可选钩子，
  默认跳过、不打包——是否做由项目所有者决定，勿主动迁移文件。

## 5. 仍开放的用户侧决策（非工程任务，勿代做）

1. TODO backlog §A：Idea Platform 推导模型最终支持清单 + Concept usage models 定义
2. TODO backlog §D：确认 12 路线枚举已覆盖选定模型后勾销
3. TODO backlog §C：极简版 `examples/sample-evidence-pool.md`（2 条占位）去留
4. 卡片单页版式 vs 完整工作卡、旧卡 preserve/avoid 措辞
5. （可选）珀莱雅案例 PG-02/03 官方核验（专利/备案），用于演示 Provisional→Final 升级路径

## 6. 变更文件清单（本轮，插件内）

- `assets/templates/idea-platform-record-template.md` — §0 命名决策固化
- `assets/templates/concept-record-template.md` — §0 命名决策固化
- `assets/lexicons/{zh-stopwords.txt, synonym-map.csv, platform-slang.csv, emotion-taxonomy.csv, motive-taxonomy.csv}` — 语料扩充
- 插件外：`drafts/review-notes/`（验证记录 + backlog 勾销）、`drafts/skill-update-requests/04-insight-strategy.md`（状态核销）、`.gitignore`

回归全绿（§1），以上改动未破坏任何既有契约检查。
