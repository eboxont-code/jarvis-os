# OpenClaw Workspace

A local Windows AI workspace with OpenClaw as the main assistant. Ollama serves the model on the same PC. OpenCode is available through ACP for coding tasks.

## Use the workspace

Open **OpenClaw Chat** from the desktop, or open Companion and choose the **main** agent. The Windows installation this repository supports uses **qwen3.8:27b**. The Ollama entry in the model picker starts a direct chat. The OpenCode (ACP) entry uses the same local model for a coding session.

This repository contains a read-only status tool for an existing installation. It requires Python 3 on Windows, the installed OpenClaw Gateway package with its qualified clawctl alias, and Ollama on its default loopback port.

## Check the connections

Run this from the repository root in PowerShell:

~~~powershell
python tools/check_workspace.py
~~~

The tool checks Ollama's local model list, the Windows Gateway service, authenticated Gateway health, and the paired Windows Node. It prints one result per check and returns exit code 1 if any check fails. A passing check verifies connectivity. To test inference, send a short prompt in OpenClaw Chat and wait for its answer.

If the Gateway is healthy but the Node is offline, open Companion Settings → Connection and reconnect the existing Native Gateway. Keep the existing pairing. Model downloads, live credentials, chat histories, and machine-specific configuration belong on the local PC.

## Project history

The previous project's tracked files are preserved under `legacy/jarvis-os/` for reference. Its launchers and installation instructions are retired. The active entry points are OpenClaw Chat and the status tool above.
