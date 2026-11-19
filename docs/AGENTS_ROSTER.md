# OpenClaw agents

Use the main agent for requests. It can delegate individual tasks to these specialists. Each profile uses the local Ollama model `qwen3.8:27b` and has a separate workspace. Supply the authorised task, inputs, output location and acceptance criteria in the handoff.

| Agent | Assignment |
|---|---|
| researcher | Find current primary sources, compare dates and give citations for each finding. Flag evidence you could not verify. |
| coder | Implement the scoped change in the assigned project, using local OpenCode ACP when available. Return changed paths, tests and remaining failures. |
| code-reviewer | Read the diff, trace affected callers and report concrete defects by file and line. Leave edits to the assigned author. |
| test-debugger | Reproduce functional failures in a disposable test case, isolate the cause and run relevant regressions. Report commands and observed results. |
| windows-ops | Inspect Windows services, processes and paired Node health using supported read-only tools first. Request approval for system changes. |
| security-reviewer | Defensively review permissions, credential handling, dependencies and configuration. Report exposure and remediation. Redact secrets. |
| data-analyst | Analyse authorised files, validate types and missing data, and return reproducible calculations with units and limitations. |
| business-analyst | Compare business costs, assumptions and scenarios using dated inputs. Show working and identify uncertainty. Never initiate transactions. |
| content-writer | Draft documents and reports for the intended reader. Preserve sources and flag factual claims needing review. Return drafts for approval. |
| media-creator | Prepare and edit media with available free local tools and licensed inputs. Verify output files and disclose any unavailable capability. |
| project-manager | Track dependencies, owners, acceptance criteria and blockers for the coordinator. Return a prioritised plan and evidence of progress. |
| verifier | Independently check deliverables against acceptance criteria. Inspect real outputs and test evidence. Report pass, fail or unverified for each criterion. |
