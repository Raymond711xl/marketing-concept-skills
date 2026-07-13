# 真实交接验证记录 — 珀莱雅 Evidence Pool（物料 1）

日期：2026-07-12。用真实公开调研数据（`drafts/real-materials/proya/`，30 条 Evidence Pool v1 +
Strategy Readiness Pack + Brand Facts Pack）走了一遍 insight-strategy 的输入契约验证。
本文只记录发现，不改 skill 逻辑。

## 验证结果

- `01-input-package-contract.md` Acceptance Check 9 项逐条核对：**7 项通过**；
  2 项如实标记缺口——无正式 brief（本次为校准演练，非客户任务）、无消费者原声
  （L6 渠道待授权采集，已记入 Evidence Pool 的 Gaps and Restrictions）。
- `run_regression_checks.py` 5 项全过；`smoke_test_prepare_raw_evidence.py` 通过
  （CSV/TSV/TXT、bundled lexicons、cwd 无关性、.xls guard）。
- 真实数据按 collector 的 `Evidence Pool v1` 契约产出**无障碍**：11 核心字段 +
  扩展字段够用；`Observation: not applicable - text-only source` 约定对新闻类证据很顺；
  Brand Hard Data Track 表在真实品牌上填得满、有区分度。

## Schema 摩擦（真实数据暴露的漂移）

1. **examples/templates 与 collector 契约不一致**（已知问题，真实数据下确认成立）：
   - `examples/sample-evidence-pool-skincare.md`、`examples/sample-evidence-pool.md`、
     `assets/templates/evidence-pool-template.md` 用 `Audience / segment`（契约为 `Audience`）、
     **缺 `Observation`**、混入下游 coding 字段 `Insight lens` / `Matched keywords`、
     用 `E001` 无前缀 ID（契约要求 `WEB-001` 式前缀且稳定）。
   - 后果：拿真实 collector 输出对照 examples 学格式的人会学错。建议后续把
     examples 对齐 v1，或在模板顶部声明「此为 insight-strategy 本地简化形，
     真实交接以 collector 契约为准」。
2. **Readiness 状态词表三套并存**，映射关系只在 controller 里隐式存在：
   - evidence-summary 侧：`ready / ready with caveats / needs more evidence`
   - insight-strategy 输入契约：`Ready / Partial / Unavailable`
   - brand-facts-pack 模板：`Ready / Partial / Thin`
   - 本次真实交接的处理：Readiness Pack 用上游词表（ready with caveats），
     Brand Facts Pack 用本地词表（Partial）。可用，但三套词表值得在某处集中声明映射。
3. **Strategy Readiness Pack 两种形态**：上游模板是 6 列表格（本次采用），
   `input-package-template.md` 里是字段列表。语义一致、形态不同，契约未声明二者等价。
4. **疑似过期的 update request**：`drafts/skill-update-requests/04-insight-strategy.md`
   第 5 条要求「真正加载 bundled lexicons」，但现行 `prepare_raw_evidence.py` 已加载
   全部 7 个词库资产（smoke test 有断言）。该条可关闭或改为文档核对。

## 结论

Evidence Pool v1 契约本身经得起真实数据：字段、词表、ID 规则、反向证据的容纳
（conflicting / Limitation 字段）都够用。主要债务在 examples/模板与契约的一致性，
不在契约设计。物料 1 的「格式验证」部分完成；「社媒原声」部分待 Step 2
（小红书/天猫采集）后补充 `SOC-XHS-###` / `ECOM-TM-###` 分片再次验证。
