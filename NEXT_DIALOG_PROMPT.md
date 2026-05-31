# Prompt For The Next Codex Conversation

Use this in a new Codex conversation after opening this project folder:

```text
请用中文和我交流。

工作目录是：
<workspace-root>

我要开始实现一个新的 Codex skill，名字叫：
research-investigation-workflow

请先阅读这个项目里的 README.md、PLAN.md、docs/guard-family-basis.md、
docs/history-ledger.md 和 docs/implementation-roadmap.md。

目标：
创建一个新的 Codex skill，用来统筹 TraceGuard、LogicGuard 和 FlowGuard
完成多轮调查研究工作。它必须基于现有 Guard-family 工作流，不要凭空新造
推理引擎。它还需要自己的 Research Investigation History Ledger，用于
记录每次调查运行历史，方便未来相似任务复用经验。

请按项目计划直接开始实施，不要只停留在讨论计划。先做必要的
KB / FlowGuard / skill-creator 预检，然后创建 skill 骨架和 reference 文档。
持续推进直到这个新 skill 完成、通过基础验证、并给出清楚的完成说明。

不要把它做成 UI，不要合并 TraceGuard Case Library 和 LogicGuard Source Library。
如果中途遇到真正无法绕过的 blocker，再明确告诉我卡在哪里、为什么卡住、
默认建议怎么处理。
```
