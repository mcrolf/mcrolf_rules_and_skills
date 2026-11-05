---
description: Delegate independent subtasks that will not interfere with work in progress. Pick the listed model that fits, including other providers, and keep expensive models off trivial work.
alwaysApply: true
---

# Parallel Delegation

Delegate independent subtasks to available subagents when the work can run in parallel without interfering with a task already in progress. Do not wait for the user to ask.

- Check active tasks, assignments, dependencies, and shared resources first. Use the runtime task inventory when it exists.
- Stay inside the user's authorized scope. Keep work sequential when it depends on an unfinished result, shares a file or resource, or coordination would cost more than it saves.
- Give each subagent one objective, the context it needs, ownership of files or resources, constraints, and a concrete result. Mention relevant work already in progress.
- Concurrent edits need separate files or components. Shared files, branches, browser sessions, services, databases, and external actions need runtime isolation or a single owner. If separation is uncertain, work sequentially.
- Keep working on other independent parts while subagents run. Do not redo their work, overwrite their changes, or preempt an active task.
- Match the subagent count to the work and to runtime limits. Follow that provider's delegation, permission, completion, and cancellation flow.
- Review, integrate, and validate delegated results before calling the task done. The parent agent owns the final result.
- If priorities or shared resources change, narrow or stop the affected delegated work first. Never cancel an unrelated task without authorization.

## Model choice

Choose the provider and model as deliberately as you choose to delegate. Codex, Claude, Cursor, and any other provider the runtime lists are in scope. Use another provider when its model fits better than the parent.

Use only listed models. If the user names a model or provider, use that. If the runtime lists one model, use it. Stay on the parent only when it is the best fit or no alternative is listed. Set the model explicitly when that is how the runtime selects a provider; an omitted model stays on the parent. Different subtasks in the same turn use different providers when their demands differ.

Fitness first: the model must be able to finish the subtask reliably. When two models are similarly capable, pick the cheaper one, including a cheaper model from another provider.

- Trivial or mechanical work (narrow lookup, inventory, formatting, extraction, boilerplate) uses a fast, inexpensive model. Leave frontier models for harder work.
- Bounded implementation uses a capable mid-tier model.
- Hard reasoning, ambiguous design, architecture, security-sensitive judgment, and subtle debugging use the strongest model that fits, including a stronger model from another provider.

Use a cheaper model than the parent when the subtask is easier, and a stronger model from another provider when the parent is not enough. A cheap model can look up docs while another provider implements a separate component. Keep dependent edits to the same file sequential unless the runtime isolates them.
