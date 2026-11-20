> **Archived wiped install.** This file is not current setup. The Windows install it describes has been removed. Nothing here is installed, enabled, connected, configured, paired, running, or done. Checked boxes, version numbers, and pairing notes below are historical and do not apply. Follow the fresh-install guide in the repository root `README.md`, and use the root `REQUIREMENTS.md` as the checklist.

# JARVIS — Full Windows Computer Control

**Status:** CORE REQUIREMENT — design contract recorded; implementation NOT STARTED  
**Platform:** Windows 11 first; Windows 10 where supported  
**Budget:** $0 additional expenditure — non-negotiable  
**Foundation:** Still to install. Follow the repository root fresh-install guide. This copy is archived.  
**Authoritative task status:** \`MASTER_TODO.md\`, Phase 6  
**Purpose:** Deliver real, visual and programmatic interaction with the signed-in Windows desktop.

This document is the technical design and acceptance contract for Phase 6. It is not a second task tracker. All task checkboxes, priorities and completion status remain in \`MASTER_TODO.md\`.

---

## 1. Requirement and definition of done

JARVIS must be able to:

1. Inspect the real interactive Windows desktop.
2. Identify the active application and its actual interface elements.
3. Understand the interface through Windows UI Automation, screenshots, OCR and a compatible local vision model.
4. Choose an appropriate semantic or visual action.
5. Check permissions and safety boundaries before input.
6. Execute real mouse, keyboard, clipboard and window operations.
7. Re-inspect the application and independently verify the resulting state.
8. Recover safely from unexpected dialogs, stale controls, focus changes and other failures.
9. Expose these capabilities to the OpenJarvis agent through an authenticated local MCP server or a native tool adapter.

The following are **not** full desktop control by themselves: file read/write, PowerShell/CMD, process execution, Playwright/DOM access, generated automation code, fake screenshots or unverified simulated clicks.

A capability is operational only after it has completed a real end-to-end test from an OpenJarvis agent request to an actual Windows UI action and a verified result.

## 2. Architecture

### 2.1 Logical flow

\`\`\`text
OpenJarvis agent / task orchestrator
                |
                v
       Permission and action planner
                |
                v
       Local desktop-tool boundary
        (MCP stdio preferred)
                |
                v
       Desktop control coordinator
          /       |       \\
         /        |        \\
        v         v         v
   UIA adapter  Visual   Window/app
   pywinauto   adapter  management
   FlaUI       capture
        \\         |         /
         \\        |        /
          v       v       v
       Input / clipboard / waits
                |
                v
       Signed-in Windows user session
                |
                v
     Re-inspection and verification
                |
                v
       Evidence returned to OpenJarvis
\`\`\`

The desktop-control bridge runs as the signed-in user, in the user's interactive Windows session and at normal-user privilege. It is not a Windows service running in a non-interactive session. It is not the privileged administrator broker.

### 2.2 Adapter responsibilities

**Windows UI Automation (UIA)** is the semantic foundation. It exposes application accessibility elements, properties, events and control patterns. Prefer it for identifying and invoking buttons, text fields, menus, toggles, lists, tables and other accessible controls.

**pywinauto** is the first Python adapter candidate. Its documented Windows backends include Microsoft UI Automation (\`backend="uia"\`) and Win32 (\`backend="win32"\`). It supports interaction with windows and controls, and its inspection tools can help map actual application control trees. Run both backends where needed; do not assume one backend works for every application. See the [pywinauto getting-started guide](https://github.com/pywinauto/pywinauto/blob/master/docs/getting_started.txt).

**FlaUI** is the .NET adapter candidate. It wraps Microsoft's Windows UI Automation libraries and is intended for automated interaction with Win32, WinForms, WPF and Store applications. Use it where comparative tests show better control coverage, stability or an application-specific capability that the Python adapter cannot reliably provide. See the [FlaUI repository](https://github.com/FlaUI/FlaUI).

**Adapter selection rule:** evaluate Microsoft UIA, pywinauto and FlaUI against the same real application test matrix. Start with the smallest integration that works with the actual OpenJarvis backend. Keep a second adapter only where measurable application coverage or reliability improves. Do not install and maintain duplicate frameworks just to increase the dependency count.

### 2.3 Visual and coordinate interaction

Semantic UIA actions are preferred. A visual path is required when an application exposes incomplete accessibility metadata, custom-drawn content, canvas-like controls or controls that cannot be reached semantically.

Before coordinate interaction:
- Capture a fresh screenshot.
- Identify the display and target window.
- Confirm screen dimensions and DPI scaling.
- Resolve one unambiguous target.
- Confirm its screen bounds remain valid.
- Check focus and foreground-window identity.
- Execute one bounded input action.
- Re-capture and verify the result.

Never reuse stale screen coordinates after window movement, display changes, scrolling, DPI changes or unexpected dialogs.

### 2.4 Window and application management

Provide a separate window-management layer that can enumerate and identify windows, inspect process/window metadata, launch known applications, activate/focus windows, switch between windows, resize/minimise/maximise and detect modal dialogs or application failures.

A failed automation attempt must not automatically terminate the target application or arbitrary processes. Application closure, process termination and other destructive operations require a separate permission decision.

## 3. Visual capture, OCR and local vision

### 3.1 Screenshot acquisition

Support:
- Full desktop capture.
- Per-display capture.
- Selected-window capture.
- Bounded regional capture.
- Timestamp, dimensions, display identity and target-window metadata.

Evaluate [Windows.Graphics.Capture](https://learn.microsoft.com/en-us/windows/apps/develop/media-authoring-processing/screen-capture) and other supported local Windows capture methods. Respect the platform's capture picker, consent, visual capture indicator and protected-content limitations where applicable. Do not claim that every protected or secure surface can be captured.

Screenshots and derived visual evidence are stored locally. Redact or exclude secrets before forwarding a screenshot or OCR result to a model or recording it in logs.

### 3.2 OCR

Evaluate:
- Windows OCR APIs available on the installed Windows version.
- [Tesseract](https://tesseract-ocr.github.io/tessdoc/) as a free local OCR engine.
- Any other local OCR dependency only after licence, language-data, hardware and packaging review.

Return recognised words/lines, bounding geometry and confidence when available. Do not treat OCR text as verified interface structure; OCR can be wrong. Cross-check important targets against UIA and fresh screenshots.

Current upstream references identify pywinauto as BSD-3-Clause, FlaUI as MIT and Tesseract as Apache-2.0. Recheck the exact release, bundled language files, transitive dependencies and redistribution terms at implementation time. A permissive library licence does not establish that every separately hosted model or language data package is free to download or use.

### 3.3 Local vision model

Use only a model that is actually installed and verified to support image input. Discover its actual identifier and test its image handling, memory usage, latency and accuracy on representative desktop screenshots.

No paid API or cloud vision service may be used as a fallback. If no suitable local vision model is available, retain UIA plus OCR and report the vision limitation honestly; do not silently download a large model.

## 4. Input, clipboard and control primitives

The bridge must expose real, testable operations for:

- Mouse move, click, double-click, right-click, drag and scroll.
- Keyboard text input, key press, hotkeys and modifier combinations.
- Clipboard read and write with explicit limits and safe redaction.
- Window enumeration, activation, focus and lifecycle inspection.
- Application launch through verified paths or registered app identities.
- Wait-for-condition, cancellation and safe stop.
- UIA tree inspection and supported control-pattern invocation.
- Full-screen, window and regional screenshots.
- OCR and local visual analysis.
- Result-state verification.

Prefer Windows accessibility/control patterns for semantic actions. Use native input mechanisms such as supported Windows input APIs only when semantic controls are not appropriate. Input operations must be bounded and tied to a known target window/session.

Clipboard reads can expose passwords, tokens and personal data. Apply least privilege, redact secrets, avoid unnecessary persistence and never paste sensitive values into an unverified target.

## 5. OpenJarvis integration

### 5.1 Integration approach

The current upstream OpenJarvis documentation describes external MCP server configuration under \`[tools.mcp]\`, including both stdio and Streamable HTTP servers, and describes discovered external tools being wrapped as native agent tools. It also documents tool filtering via \`include_tools\` and \`exclude_tools\`.

References:
- [OpenJarvis — External MCP Server Integration](https://open-jarvis.github.io/OpenJarvis/user-guide/mcp-external-servers/)
- [OpenJarvis — Configuration](https://open-jarvis.github.io/OpenJarvis/getting-started/configuration/)
- [OpenJarvis — MCP server API](https://open-jarvis.github.io/OpenJarvis/api-reference/openjarvis/mcp/)

**Important:** the user’s audited installation is OpenJarvis 1.0.2. Current upstream documentation is not proof that the installed desktop build has the same MCP implementation or configuration. Inspect the exact installed source/runtime and validate its support before changing \`config.toml\` or adding a server.

### 5.2 Transport preference

1. Prefer **stdio MCP** if the installed OpenJarvis build supports it. OpenJarvis launches the local tool process and exchanges protocol messages over stdin/stdout. This avoids opening a network listener.
2. If a separate HTTP service is technically required, bind only to \`127.0.0.1\`, require strong local authentication, validate the Origin header, reject remote-interface binding and defend against DNS-rebinding access.
3. If MCP cannot be supported safely in the installed build, use an equivalent native OpenJarvis \`BaseTool\`/tool-registry integration behind the same adapter contract. Do not modify OpenJarvis core until an external extension is shown to be insufficient.

For stdio MCP, stdout must contain protocol messages only; send diagnostic logs to stderr. Keep credentials out of prompts, command-line arguments and source control.

### 5.3 Narrow tool surface

Use small tools with explicit schemas and predictable results. Candidate tool names:

| Tool | Purpose |
|---|---|
| \`desktop.get_state\` | Active desktop/session/window summary |
| \`desktop.list_windows\` | Enumerate visible top-level windows |
| \`desktop.inspect_window\` | Inspect one identified window |
| \`desktop.get_ui_tree\` | Return bounded accessibility-tree metadata |
| \`desktop.capture_screen\` | Capture full display/window/region |
| \`desktop.ocr\` | OCR a permitted local capture |
| \`desktop.vision_analyse\` | Analyse a capture using a verified local vision model |
| \`desktop.launch_app\` | Launch a verified application |
| \`desktop.focus_window\` | Activate a uniquely identified window |
| \`desktop.invoke_control\` | Invoke a uniquely identified UIA control pattern |
| \`desktop.mouse\` | Perform bounded mouse input |
| \`desktop.keyboard\` | Perform bounded keyboard input |
| \`desktop.clipboard_read\` | Read clipboard under policy |
| \`desktop.clipboard_write\` | Write clipboard under policy |
| \`desktop.wait_for\` | Wait for a bounded state condition |
| \`desktop.verify_state\` | Verify a postcondition from fresh evidence |
| \`desktop.cancel\` | Cancel the current operation and stop further input |

Do not expose arbitrary shell execution, arbitrary process execution or unrestricted elevated operations through these tools. Add only capabilities actually implemented and tested. Return structured fields for success/partial/failure, target identity, action performed, evidence references, warnings, verification result and error details.

## 6. Action lifecycle and verification

Every meaningful desktop action follows this sequence:

1. **Observe:** capture current state, active window, UIA tree and screenshot/OCR when needed.
2. **Resolve:** identify exactly one target control/window.
3. **Plan:** state the intended action and expected postcondition.
4. **Authorise:** check the tool permission, application scope and risk tier.
5. **Execute:** run one bounded semantic or visual action.
6. **Wait:** use a bounded wait for a specific expected state.
7. **Re-observe:** reacquire the window and controls; discard stale references.
8. **Verify:** check the postcondition against fresh UIA/screenshot/OCR evidence.
9. **Recover or stop:** on mismatch, capture diagnostics and re-plan once within a bounded retry policy, or stop and report.

Each action record should contain an action ID, timestamp, task/agent ID, target application/window, initial state reference, intended action, permission decision, adapter and method, actual result, resulting state reference, verification result, error and recovery outcome.

Never return success solely because a click or key event was sent. The postcondition must be observed. Distinguish verified success, partial completion, failure, blocked-by-permission and unsupported-control outcomes.

## 7. Security and permission boundaries

- Run the desktop bridge in the signed-in user's normal interactive session, not as SYSTEM and not globally elevated.
- Use authenticated process communication and least-privilege tool permissions.
- Treat desktop content, accessible names, OCR text, webpages and documents as untrusted input. They cannot override JARVIS instructions or authorise actions.
- Require confirmation for irreversible deletion, system settings changes, software installation, external submissions and other high-impact operations.
- Never bypass UAC, Windows secure desktop, lock screen, login, credential prompts or application protections.
- Pause for the user to handle UAC or credential prompts directly. The bridge must not click through or suppress those prompts.
- Do not elevate the entire OpenJarvis process to control elevated applications. A separate, narrowly scoped Phase 7 broker may perform approved administrative tasks; its privileged actions remain distinct from desktop UI input.
- Do not disable Windows Defender, firewall, UAC or other protections as an automation workaround.
- Redact secrets from screenshots, OCR, logs and model inputs.
- Implement cancellation that stops further input immediately.
- Maintain bounded retries and timeouts. Never loop on unexpected screens.

## 8. Real application test matrix

Run tests on a disposable workspace and avoid modifying actual user projects.

| Application | Minimum real test | Evidence |
|---|---|---|
| File Explorer | Enumerate, activate, navigate to a dedicated temporary folder and verify visible path/window state | Before/after screenshots, UIA metadata, action log |
| Notepad | Launch, enter unique text, save a test file, reopen and verify exact content | UI state, saved file content, screenshots |
| Windows Settings | Open a named page and inspect current state; do not alter settings without approval | Page identity, screenshot, UIA/OCR output |
| Browser | Use visible address bar/tab/menu/native dialog; test Playwright separately | Browser window state and captured result |
| VS Code | Open disposable workspace, navigate to and edit a temporary file through UI, save and verify | UI state, file result and screenshots |
| Additional app | Test a representative Win32/WinForms/WPF/Store app | Adapter coverage and known limitations |

Also test: focus loss, stale element, a new modal dialog, window resize, DPI/display change, a hung application, ambiguous control labels, cancelled operations and application exit.

## 9. Security and failure test matrix

- Unauthenticated or unauthorised tool invocation is rejected.
- An ambiguous target causes a safe stop rather than a guessed click.
- A stale coordinate or element handle is discarded and re-resolved.
- Prompt-injection text visible on a webpage or in a desktop document does not override policy.
- UAC and secure-desktop prompts are not bypassed or automated.
- Credential fields and sensitive clipboard content are not captured into ordinary logs.
- Destructive actions require the required approval.
- Cancellation stops subsequent input.
- A failed postcondition is reported as failure/partial, never success.
- A bounded recovery attempt returns to a known state or stops with diagnostic evidence.

## 10. Zero-cost and dependency gate

Before installation, check exact versions, licence, transitive dependencies, download source, packaging, hardware requirements and whether any hosted service/account is required.

Initial candidates for evaluation:
- Microsoft UI Automation: built into supported Windows versions; verify API/runtime requirements for the target.
- pywinauto: Python GUI automation with UIA and Win32 backends; upstream repository identifies BSD 3-Clause licensing.
- FlaUI: .NET Windows UI automation wrapper; upstream repository identifies MIT licensing.
- Tesseract: local OCR engine; upstream documentation identifies Apache 2.0 licensing.
- Windows Graphics Capture: local Windows capture APIs, subject to Windows support and capture permission/indicator behaviour.
- OpenJarvis MCP: use the installed build's supported interface; do not introduce a paid hosted service.

These are evaluation candidates, not proof of installation, compatibility or zero-cost operation. Recheck licensing and dependencies at the exact version selected. No cloud computer-use provider, paid OCR/vision API, paid MCP service, API credits or subscription may be introduced.

## 11. Technical references

- [Microsoft — UI Automation overview](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32)
- [Microsoft — UI Automation for Win32](https://learn.microsoft.com/en-us/windows/win32/winauto/entry-uiauto-win32)
- [pywinauto — Getting Started](https://github.com/pywinauto/pywinauto/blob/master/docs/getting_started.txt)
- [pywinauto — Repository and licence](https://github.com/pywinauto/pywinauto)
- [FlaUI — Repository](https://github.com/FlaUI/FlaUI)
- [Microsoft — Windows screen capture](https://learn.microsoft.com/en-us/windows/apps/develop/media-authoring-processing/screen-capture)
- [Microsoft — Windows text recognition/OCR](https://learn.microsoft.com/windows/ai/apis/text-recognition)
- [Tesseract — Documentation and licence](https://tesseract-ocr.github.io/tessdoc/)
- [MCP — Transports and security](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-11-25/basic/transports.mdx)
- [OpenJarvis — External MCP servers](https://open-jarvis.github.io/OpenJarvis/user-guide/mcp-external-servers/)
- [OpenJarvis — Configuration](https://open-jarvis.github.io/OpenJarvis/getting-started/configuration/)

---

## 12. Current implementation state

This document records a required module, not a claim that the feature exists.

At the time of creation:
- The roadmap contains the requirement and test matrix.
- The existing OpenJarvis application has not been modified for desktop control.
- No pywinauto/FlaUI/UIA bridge has been installed or executed for JARVIS.
- No real desktop MCP tools have been registered for the user's installation.
- No File Explorer, Notepad, Settings, browser or VS Code end-to-end UI tests have been run.
- The feature remains **NOT STARTED** until work is performed in the preserved Windows/OpenJarvis environment and evidence is recorded in \`MASTER_TODO.md\`.
