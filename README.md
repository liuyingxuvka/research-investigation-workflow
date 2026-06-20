# Research Investigation Workflow

<!-- README HERO START -->
<p align="center">
  <img src="./assets/readme-hero/hero.png" alt="Research Investigation Workflow concept hero image showing evidence sources flowing through SourceGuard, TraceGuard, LogicGuard, and FlowGuard into a report and history ledger" width="100%" />
</p>

<p align="center">
  <strong>A Codex skill for deep investigations where evidence, traces, reasoning, and final wording must stay separate.</strong>
</p>
<!-- README HERO END -->

| Current Version | Skill | Runtime | License |
| --- | --- | --- | --- |
| `v0.4.4` | `research-investigation-workflow` | Codex skill repository | MIT |

English comes first. A Chinese mirror follows below.

## What It Is

Research Investigation Workflow is a Codex skill for deep, multi-round investigation work.

It is built for questions where a quick search summary is not enough: policy rumors, technical claims, competitor signals, incident chains, research leads, source conflicts, causal claims, market or stakeholder effects, and report-grade conclusions.

The workflow coordinates SourceGuard, TraceGuard, LogicGuard, FlowGuard, and a local history ledger. It keeps source discovery, event facts, actor claims, interpretation, causal links, counterevidence, report structure, and final wording in separate lanes so an agent does not turn partial evidence into a confident story too early.

## The Problem

Most failed investigations do not fail because there was no information. They fail because different layers get collapsed:

1. A source says something happened, but the report writes that it caused an outcome.
2. An announcement is treated as implementation evidence.
3. Local evidence is stretched into a broader-sector claim.
4. A clean storyline hides a live alternative explanation.
5. A report has citations, but the source role does not match the claim wording.
6. A search round finds some evidence and the agent stops before checking counterevidence.
7. Useful investigation lessons disappear instead of becoming reusable history.

This workflow exists to prevent that collapse.

## How It Works

The core route is:

```text
question
-> source discovery plan
-> evidence intake
-> TraceGuard lead and effect chains
-> LogicGuard claim and source-fit model
-> Research Reasoning Atlas
-> FlowGuard closure check
-> report or briefing synthesis
-> history ledger write-back
```

In plain language:

- **SourceGuard** plans what evidence roles are needed, not just what keywords to search.
- **TraceGuard** separates event facts, explanation, execution, outcome, counterevidence, and future triggers.
- **LogicGuard** checks whether the written conclusion is structurally licensed by evidence, warrants, assumptions, limitations, and rebuttals.
- **Research Reasoning Atlas** keeps alternatives, opposition, model lenses, confidence boundaries, and future falsifiers visible.
- **FlowGuard** checks process order, stale evidence, skipped gates, and final completion claims.
- **History ledger** preserves reusable investigation patterns without turning private working notes into public claims.

## What It Produces

| Investigation need | Workflow output |
| --- | --- |
| Know what to search next | Source discovery plan and missing evidence roles |
| Keep source facts separate | Source portfolio and key-claim ledger |
| Reconstruct what happened | TraceGuard event, execution, outcome, and counter chains |
| Avoid causal overclaim | Weakest-link and scope-transfer warnings |
| Compare live explanations | Research Reasoning Atlas and conclusion tournament |
| Write a report safely | Claim-source fit checks and artifact-native synthesis |
| Know whether the task is done | Guard closure report with stale/skipped/missing rows |
| Reuse lessons later | Local history ledger entries |

## Good Fit

Use this workflow when:

- the answer depends on source quality, source role, timing, or missing counterevidence;
- the claim involves causality, implementation, outcome, scope transfer, or stakeholder effect;
- the final output is a report, briefing, memo, research note, or structured investigation summary;
- several Guard-family tools must coordinate without losing evidence boundaries;
- you need a reusable record of how the investigation was done.

## Not A Fit

Do not use it for:

- quick factual lookups;
- casual summaries where source roles and claim strength do not matter;
- private or access-gated claims that cannot be checked and should not be inferred;
- existing thesis or paper revision that needs DOCX editing and marked prose integration. Use `academic-thesis-revision-workflow` for that upper-level route.

## Quick Start

Install the skill folder into your Codex skills directory:

```powershell
Copy-Item -Recurse -Force .\skills\research-investigation-workflow "$env:USERPROFILE\.codex\skills\research-investigation-workflow"
```

Run representative closure and source checks:

```powershell
python .\skills\research-investigation-workflow\scripts\source_portfolio_check.py --input .\skills\research-investigation-workflow\references\templates\source_portfolio_template.yaml
python .\skills\research-investigation-workflow\scripts\key_claim_ledger_check.py --input .\skills\research-investigation-workflow\references\templates\key_claim_ledger_template.yaml
python .\skills\research-investigation-workflow\scripts\research_closure_check.py --ledger .\skills\research-investigation-workflow\references\templates\key_claim_ledger_template.yaml --json
```

The exact investigation will usually create its own source portfolio, trace rows, claim ledger, and final artifact plan. The templates are starting points, not proof.

## Relationship To The Guard Stack

| Tool | Role in this workflow |
| --- | --- |
| SourceGuard | Plans source discovery, evidence roles, access gaps, and candidate source actions |
| TraceGuard | Reconstructs event, execution, outcome, causal, counter, and effect chains |
| LogicGuard | Audits claim support, source fit, rebuttals, assumptions, and final wording strength |
| FlowGuard | Checks process gates, stale evidence, skipped checks, and final closure claims |
| Academic Thesis Revision Workflow | Owns existing thesis/paper revision when DOCX edits and academic prose integration are required |

## Repository Layout

```text
skills/research-investigation-workflow/     Installable Codex skill
skills/.../references/                      Workflow, source, trace, atlas, and output contracts
skills/.../references/templates/            Source portfolio, key-claim, and effect-chain templates
skills/.../scripts/                         Source, claim, role, and closure validators
docs/                                       Guard-family basis, roadmap, history, and adoption notes
openspec/                                   Change proposals and specs used to evolve the workflow
assets/readme-hero/                         README concept hero assets
VERSION                                     Current public version
CHANGELOG.md                                Release history
```

## Public Boundary

This repository contains the public workflow, templates, scripts, docs, and skill material.

It does not contain private investigation sources, confidential reports, personal notes, credentials, paid database exports, live source portfolios, local case libraries, or real history-ledger entries. The workflow can say that evidence is missing, partial, access-gated, contradicted, or not enough for a conclusion. It must not invent facts or convert a failed search into proof that something did not happen.

## License

No standalone `LICENSE` file is present in this repository snapshot. Add one before making a strong public reuse or redistribution claim.

---

# Research Investigation Workflow 中文说明

| 当前版本 | Skill | 运行形态 | 许可证 |
| --- | --- | --- | --- |
| `v0.4.4` | `research-investigation-workflow` | Codex skill 仓库 | MIT |

## 它是什么

Research Investigation Workflow 是一个用于深度、多轮调查研究的 Codex skill。

它适合“快速搜索总结不够”的问题：政策传闻、技术说法、竞品信号、事故链、研究线索、来源冲突、因果判断、市场或利益相关方影响，以及需要写成报告级结论的调查。

它协调 SourceGuard、TraceGuard、LogicGuard、FlowGuard 和本地 history ledger。它把来源发现、事件事实、行动方说法、解释、因果链、反证、报告结构和最终措辞分开，避免 agent 太早把局部证据写成确定故事。

## 为什么需要它

很多调查失败，不是因为没有信息，而是因为层级混在一起：

1. 来源只能证明发生了某事，报告却写成它导致了某个结果。
2. 公告被当成实施证据。
3. 局部证据被扩大成行业或全国范围结论。
4. 一个顺畅故事掩盖了仍然活着的替代解释。
5. 报告有引用，但来源角色支撑不了那句具体说法。
6. 搜到一些材料后，agent 没有继续查反证。
7. 有用的调查经验没有进入可复用 history。

这个 workflow 就是为了防止这些层级坍缩。

## 它怎么工作

核心路线是：

```text
question
-> source discovery plan
-> evidence intake
-> TraceGuard lead and effect chains
-> LogicGuard claim and source-fit model
-> Research Reasoning Atlas
-> FlowGuard closure check
-> report or briefing synthesis
-> history ledger write-back
```

翻成人话：

- **SourceGuard** 先规划需要哪些证据角色，而不是只列搜索关键词。
- **TraceGuard** 区分事件事实、解释、执行、结果、反证和未来触发条件。
- **LogicGuard** 检查最终结论是否真的被证据、warrant、assumption、limitation 和 rebuttal 支撑。
- **Research Reasoning Atlas** 保留替代解释、反方论证、模型视角、信心边界和未来证伪点。
- **FlowGuard** 检查流程顺序、旧证据、跳过的门槛和最终完成声明。
- **History ledger** 保存可复用调查经验，但不把私人工作记录写成公开结论。

## 它会产出什么

| 调查需求 | Workflow 产出 |
| --- | --- |
| 知道下一步该搜什么 | source discovery plan 和 missing evidence roles |
| 区分来源事实 | source portfolio 和 key-claim ledger |
| 重建发生了什么 | TraceGuard event / execution / outcome / counter chains |
| 避免因果过度声明 | weakest-link 和 scope-transfer warning |
| 比较多个解释 | Research Reasoning Atlas 和 conclusion tournament |
| 安全写报告 | claim-source fit check 和 artifact-native synthesis |
| 判断任务是否完成 | Guard closure report |
| 下次复用经验 | local history ledger entry |

## 适合什么任务

适合：

- 答案取决于来源质量、来源角色、时间或反证；
- claim 涉及因果、实施、结果、范围迁移或 stakeholder effect；
- 最终产物是 report、briefing、memo、research note 或结构化调查总结；
- 多个 Guard-family 工具需要协作；
- 你需要保留调查过程的可复用记录。

不适合：

- 简单事实查询；
- 不需要来源角色和 claim strength 的普通总结；
- 无法检查、也不应该推断的私有或权限受限 claim；
- 需要 DOCX 修改和学术正文融合的已有 thesis/paper 修订。这类工作交给 `academic-thesis-revision-workflow`。

## 快速开始

把 skill 文件夹复制到 Codex skills 目录：

```powershell
Copy-Item -Recurse -Force .\skills\research-investigation-workflow "$env:USERPROFILE\.codex\skills\research-investigation-workflow"
```

运行代表性检查：

```powershell
python .\skills\research-investigation-workflow\scripts\source_portfolio_check.py --input .\skills\research-investigation-workflow\references\templates\source_portfolio_template.yaml
python .\skills\research-investigation-workflow\scripts\key_claim_ledger_check.py --input .\skills\research-investigation-workflow\references\templates\key_claim_ledger_template.yaml
python .\skills\research-investigation-workflow\scripts\research_closure_check.py --ledger .\skills\research-investigation-workflow\references\templates\key_claim_ledger_template.yaml --json
```

真实调查通常会生成自己的 source portfolio、trace rows、claim ledger 和 final artifact plan。模板只是起点，不是证据。

## Guard Stack 关系

| 工具 | 在本 workflow 里的角色 |
| --- | --- |
| SourceGuard | 规划来源发现、证据角色、访问缺口和候选搜索动作 |
| TraceGuard | 重建事件、执行、结果、因果、反证和影响链 |
| LogicGuard | 审查 claim 支撑、source fit、反驳、假设和最终措辞强度 |
| FlowGuard | 检查流程门槛、旧证据、跳过检查和最终 closure claim |
| Academic Thesis Revision Workflow | 当已有 thesis/paper 需要 DOCX 编辑和学术正文融合时接管 |

## 仓库结构

```text
skills/research-investigation-workflow/     可安装 Codex skill
skills/.../references/                      workflow、source、trace、atlas 和 output contracts
skills/.../references/templates/            source portfolio、key-claim 和 effect-chain 模板
skills/.../scripts/                         source、claim、role 和 closure 验证脚本
docs/                                       Guard-family basis、roadmap、history 和 adoption notes
openspec/                                   workflow 演进 proposal/spec
assets/readme-hero/                         README hero 素材
VERSION                                     当前公开版本
CHANGELOG.md                                发布历史
```

## 公开边界

这个仓库包含公开 workflow、模板、脚本、文档和 skill material。

它不包含私人调查来源、机密报告、个人笔记、credential、付费数据库导出、真实 source portfolio、本地 case library 或真实 history-ledger entry。workflow 可以说明证据缺失、部分支持、权限受限、互相矛盾或不足以支持结论。它不能编造事实，也不能把没有搜到结果当成“事情不存在”的证明。

## 许可证

当前仓库快照中没有独立 `LICENSE` 文件。公开声称可复用或可再分发之前，应先补上明确许可证。
