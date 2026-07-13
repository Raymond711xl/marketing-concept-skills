#!/usr/bin/env python3
"""四份 skill description 的触发判别测试（轻量版）。

用法：
    1. 终端先登录一次 CLI：claude login
    2. python3 drafts/tools/trigger_test.py

原理：从磁盘实时读取四份 SKILL.md 的 description，用 haiku 模型对 16 条
真实语料做「该路由给哪个 skill / 都不路由」的判别。期望全绿；失败项即为
description 判别边界薄弱处。语料含刻意的边界混淆用例与三条应拒绝用例。
路径相对本脚本解析，仓库改名或移动后无需修改。
"""
import concurrent.futures
import pathlib
import re
import subprocess

REPO_ROOT = pathlib.Path(__file__).resolve().parents[2]
SKILLS_ROOT = REPO_ROOT / "plugins" / "marketing-concept-skill" / "skills"
NAMES = [
    "concept-strategy-controller",
    "web-evidence-collector",
    "evidence-summary-analysis",
    "insight-strategy",
]

descs = {}
for n in NAMES:
    text = (SKILLS_ROOT / n / "SKILL.md").read_text(encoding="utf-8")
    descs[n] = re.search(r"^description:\s*(.+)$", text, re.M).group(1).strip()

# (query, primary expected, also-acceptable)
CASES = [
    ("我想为一个新中式茶饮品牌做整体品牌策略，从调研到最终概念都要，现在手上什么资料都没有", "concept-strategy-controller", set()),
    ("用慢策帮我跑一个防晒品类的项目", "concept-strategy-controller", set()),
    ("接了个 brief，客户是宠物冻干粮，想让年轻人觉得喂冻干是爱的表现，帮我从头推到 concept", "concept-strategy-controller", set()),
    ("恢复项目：dossiers/proya-2026/backstage-dossier.md，继续上次的进度", "concept-strategy-controller", set()),
    ("帮我收集一下珀莱雅最近一年的 campaign 物料和社媒声量素材，要有来源链接", "web-evidence-collector", set()),
    ("做一份瑞幸咖啡的竞品调研，主要看小红书和微博上的公开内容", "web-evidence-collector", set()),
    ("我需要电解质水品类的公开资料，官网、新闻、报告都行，整理成证据池", "web-evidence-collector", set()),
    ("这里有一堆截图、链接和访谈笔记，帮我清洗整理成结构化的证据池，先不要下任何结论", "evidence-summary-analysis", set()),
    ("把这份 evidence pool 按消费者证据的角度整理成客户版研究报告", "evidence-summary-analysis", set()),
    ("这些小红书评论导出，帮我分类归纳一下证据模式", "evidence-summary-analysis", set()),
    ("证据池已经准备好了，帮我推导 human truth 和文化张力，给出 Idea Platform", "insight-strategy", set()),
    ("基于这份 Strategy Readiness Pack 做 Level 4 战略决策和概念包", "insight-strategy", set()),
    ("帮我把这些调研发现推导成品牌策略，要有 Message House", "insight-strategy", {"concept-strategy-controller"}),
    ("帮我写三条小红书种草文案，推广我们的新款吹风机", "none", set()),
    ("把这个 PPT 里的品牌介绍翻译成英文", "none", set()),
    ("帮我P一下这张 KV 图，把背景换成海边", "none", set()),
]

skill_list = "\n".join(f"- {n}: {d}" for n, d in descs.items())


def ask(case):
    query, expected, acceptable = case
    prompt = (
        "你是一个 skill 路由器。下面是已安装的四个 skill 的 name 和 description：\n\n"
        f"{skill_list}\n\n"
        f"用户输入：\n「{query}」\n\n"
        "如果应该调用其中一个 skill 来处理这个请求，只输出该 skill 的 name；"
        "如果四个都不适合处理这个请求，只输出 none。不要输出任何其他文字。"
    )
    r = subprocess.run(
        ["claude", "-p", "--model", "haiku", prompt],
        capture_output=True, text=True, timeout=180, cwd="/tmp",
    )
    answer = r.stdout.strip().split()[-1] if r.stdout.strip() else f"ERROR:{r.stderr.strip()[:80]}"
    ok = answer == expected or answer in acceptable
    return query, expected, answer, ok


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(ask, CASES))

    passed = sum(1 for *_, ok in results if ok)
    for query, expected, answer, ok in results:
        mark = "PASS" if ok else "FAIL"
        print(f"[{mark}] expect={expected:28s} got={answer:28s} | {query[:38]}")
    print(f"\n{passed}/{len(results)} passed")
