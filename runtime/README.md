# JARVIS Project Controller — Windows

The controller connects the private eboxont-code/jarvis-os master checklist to the installed OpenJarvis configuration without editing or replacing the OpenJarvis source checkout.

## What it does

1. Refreshes the private repository main branch with git fetch and git merge --ff-only.
2. Stops if AGENTS.md or MASTER_TODO.md contains uncommitted local edits. It never runs reset, clean, force-pull or destructive cleanup.
3. Generates a local prompt containing the complete AGENTS.md and latest MASTER_TODO.md.
4. Backs up the current OpenJarvis config.toml before adding [agent].system_prompt_path.
5. Creates a desktop shortcut which repeats the sync before each project session.
6. Provides a task-status helper which marks a task WORKING or finishes it as VERIFIED, PARTIAL or BLOCKED, commits only MASTER_TODO.md, pushes main, then compares the remote read-back with the local file.

All Git subprocesses have a 45-second timeout. Git credential prompts are disabled inside the launcher so missing credentials fail rather than hanging. Authenticate Git once with the normal Git Credential Manager before using the shortcut.

## One-time install

Clone the private repository to a stable location. The example uses %USERPROFILE%\jarvis-os:

    git clone https://github.com/eboxont-code/jarvis-os.git "$HOME\jarvis-os"
    Set-Location "$HOME\jarvis-os"
    powershell -NoLogo -NoProfile -ExecutionPolicy Bypass -File .\runtime\Install-JARVIS-ProjectController.ps1

The install script checks PowerShell syntax, creates the JARVIS Project Session desktop shortcut, performs the initial sync and configures the OpenJarvis prompt path.

Keep this clone in the same location after creating the shortcut. If you move it, rerun the installer from the new location.

## Every project session

1. Fully close OpenJarvis the first time so it reloads its config.
2. Double-click JARVIS Project Session on the desktop.
3. The controller fetches the newest private master files, regenerates the prompt, then tries to launch the OpenJarvis Start-menu entry.
4. If no unique Start-menu entry is found, it still completes the sync; open OpenJarvis manually.
5. Start a new JARVIS project chat. The project instructions and full master plan are supplied through the configured system-prompt file.

The launcher never terminates a running OpenJarvis process. If OpenJarvis is already open, close it fully and relaunch it so the updated prompt is loaded.

If OpenJarvis is installed outside the Start menu, run the launcher with its exact executable path:

    powershell -NoProfile -ExecutionPolicy Bypass -File .\runtime\Start-JARVIS-Project.ps1 -AppPath "C:\exact\path\OpenJarvis.exe"

The system prompt is loaded by the OpenJarvis runtime at application/session initialization; this first use must be tested on the installed desktop build. Upstream OpenJarvis documents [agent].system_prompt_path as the external .txt or .md prompt setting. If the installed desktop build does not honour it, do not mark runtime integration VERIFIED; inspect that build's backend/config path before making source changes.

## Task status updates from an AI session

Use the status helper from the local clone. TaskText must uniquely identify one checkbox in MASTER_TODO.md.

Start before implementation:

    powershell -NoProfile -ExecutionPolicy Bypass -File .\runtime\Update-JARVIS-TaskStatus.ps1 -Action Start -TaskText "distinctive task wording"

Finish with evidence:

    powershell -NoProfile -ExecutionPolicy Bypass -File .\runtime\Update-JARVIS-TaskStatus.ps1 -Action Finish -TaskText "same distinctive task wording" -Status VERIFIED -Evidence "test command and actual passing result"

For unfinished work, use -Status PARTIAL -Done "what works" -Remaining "what remains" -NextAction "next executable step".

For a blocker, use -Status BLOCKED -Evidence "specific blocker" -NextAction "next executable step".

When a matching live-status summary row exists in MASTER_TODO.md, add -StatusRowLabel "exact row label" to both Start and Finish. The updater changes that row in the same commit.

The updater refuses ambiguous task matches, refuses a second active WORKING checkbox, and refuses VERIFIED without evidence. It only stages/commits MASTER_TODO.md; unrelated working-tree changes are not added. If push or remote read-back fails, it leaves the local state intact and reports the failure.

## Safety and limitations

- No paid service, API, subscription, token purchase or cloud inference is used.
- No GitHub token is embedded in scripts. Git uses the user's existing credential manager.
- No changes are made to the existing C:\Users\Boxont\OpenJarvis source repository.
- The only OpenJarvis config change is a backed-up system_prompt_path setting. A non-empty inline system_prompt or a different existing system_prompt_path causes the launcher to stop rather than overwrite custom instructions.
- The controller cannot guarantee that every generic AI chat automatically has GitHub or local shell access. The OpenJarvis agent must have permission to execute the status helper; otherwise it must report the limitation and use an available connected GitHub capability or mark the task blocked.
- The first live prompt-load test on the installed Windows desktop app remains outstanding. Creating these files is not proof of a working runtime integration.
