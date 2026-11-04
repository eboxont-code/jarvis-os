# JARVIS — Portable Session Bootstrap

Use this file only when your AI tool does not automatically load repository instruction files.

**Copy/paste this prompt into the AI session:**

You are now working on Project JARVIS in the private GitHub repository `eboxont-code/jarvis-os`.

1. Open and read the complete `AGENTS.md`.
2. Open and read the complete `MASTER_TODO.md`. Do not rely on memory, summaries or partial snippets.
3. Confirm the repository and branch you are using, and fetch the latest version before editing.
4. Identify the current milestone, dependencies, next eligible task and acceptance criteria.
5. Mark exactly one task `WORKING` in `MASTER_TODO.md` before implementation.
6. Work one task at a time unless I explicitly authorise a batch.
7. Respect the $0 additional-expenditure rule, Windows-first policy, OpenJarvis preservation rules and security/approval boundaries.
8. Only mark a task `[x] VERIFIED` after real tests pass and evidence is recorded. Otherwise mark it `PARTIAL` or `BLOCKED` and state the next action.
9. Before finishing, update the phase/live status and dated Execution Log in `MASTER_TODO.md`, commit/synchronise it if authorised, then read it back from GitHub to verify.
10. Tell me what changed, what was actually tested, what remains and the next task.

If you cannot access the private repository or edit its master file, say so clearly. Do not pretend you read or updated anything.

## Windows OpenJarvis runtime bootstrap
If working from the installed Windows OpenJarvis app and the local controller is installed, start sessions using the desktop shortcut **JARVIS Project Session**. It refreshes the private repository and supplies the full current AGENTS.md and MASTER_TODO.md through the supported OpenJarvis system-prompt path.

When the local clone is available, use runtime/Update-JARVIS-TaskStatus.ps1 to mark the selected checkbox WORKING before implementation and to record VERIFIED/PARTIAL/BLOCKED with evidence at the end. The helper pushes only MASTER_TODO.md and performs a remote read-back. Follow runtime/README.md for installation and command syntax.

If the OpenJarvis agent has no local shell capability, do not pretend the helper ran. Use a connected GitHub capability where available; otherwise report the blocker and keep the task incomplete.
