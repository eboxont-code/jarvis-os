# Capabilities

Procedures for the main agent. Plugin ids live in [README.md](../README.md). Rules live in [REQUIREMENTS.md](../REQUIREMENTS.md). Every row is unverified until this session's tools show a result.

| # | Job | Do this | Missing |
|---|---|---|---|
| 1 | Mail | Use `imap` after a mailbox is connected. Search and draft first. Send or delete only after a tier-3 yes. | Say `imap` is not connected. Sign-in uses the `browser` tool and the mail-in-chat skill. |
| 2 | Calendar | Run the local-productivity draft script. It writes an ICS file and does not invite anyone. | Say the draft script is unavailable. |
| 3 | Build | Hand the repo to ACP agent `opencode`. Wait for the diff and the test exit code. | Say `acpx` is not enabled. |
| 4 | GitHub | Use `github` for public reads. Push, merge, and close only inside the authorised repo, with tests run. No force-push and no history rewrite. | Say GitHub writes are not authorised. |
| 5 | Hosting | Read logs or serve a loopback file the user already asked to serve. | Say deployment is not available at zero cost. |
| 6 | Database | Open SQLite read-only. Writes use a disposable file. | Say no database tool is connected. |
| 7 | DNS | Read a zone the user opened. Apply a change only after a tier-3 yes. | Say DNS is not connected. |
| 8 | Errors | Read the local log or trace the user points at. | Say no error tracker is connected. |
| 9 | Files | `workspace_create_file` for a new DOCX, PDF, XLSX, or PPTX. `document-extract` to read one. Reopen the file and check the contents. | Say that tool is absent. |
| 10 | Images | `image_generate` on local ComfyUI with SDXL base 1.0. Flux only as a Q4 or Q5 GGUF. | Say `comfy` is not connected. |
| 11 | Social | `web_search` for public posts. Send a post or DM only after a tier-3 yes that includes the exact text. | Say search is unavailable. |
| 12 | Secrets | Tell the user to type the secret into the provider page. Keep it out of chat, screenshots, and logs. | `vault` stays disabled. |
| 13 | Desktop | Follow [WINDOWS_COMPUTER_CONTROL.md](WINDOWS_COMPUTER_CONTROL.md). Playwright for DOM. `computer` for windows. | Name which of the two is absent. |
| 14 | Research | `web_search`, then `web-readability` on the page. Record the source and the time. A purchase waits for a tier-3 yes. | Say SearXNG is unavailable. |
| 15 | Messages | Draft in the chat. Send only after a tier-3 yes. | Say no delivery channel is connected. |
| 16 | Meetings | Join only a meeting the user opened. Transcribe with `whisper-cli`. | Say transcription or the meeting tool is absent. |
| 17 | Cron | Create a job only when `commands.ownerAllowFrom` or a channel owner exists. Confirm the timezone and the destination. | Say the owner route is unset. |
| 18 | Memory | Save the rule and its scope with `memory-core`. Read it back in a later turn. A revoked rule stays revoked. | Say `memory-core` is disabled. |
| 19 | Tasks | Track work on `workboard` under the main agent. Coding spawn is `opencode` only. | Say `workboard` or `acpx` is disabled. |
| 20 | Phone | Use a paired OpenClaw node from `device-pair`. Check each permission with one test action. | Say no node is paired. |

Report one operation at a time: **Connected**, **Available but not connected**, **Not possible**, or **Unverified**. A read does not grant a write.
