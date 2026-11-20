> **Archived wiped install.** This file is not current setup. The Windows install it describes has been removed. Nothing here is installed, enabled, connected, configured, paired, running, or done. Checked boxes, version numbers, and pairing notes below are historical and do not apply. Follow the fresh-install guide in the repository root `README.md`, and use the root `REQUIREMENTS.md` as the checklist.

# Existing Windows stack: restart and recovery procedure

Project status and acceptance evidence belong only in `MASTER_TODO.md`.
This procedure uses the existing installations and requires explicit restart approval.
It grants no permission to reset, reinstall, change security/pairing, override runtime
paths or download models.

1. Read the current master and agent rules. Record application PIDs/start times,
   endpoint owners, protected configuration hashes and the relevant saved session
   histories. Check **all active inference sessions**, including the main session;
   checking only the task's coordinator and ACP child is insufficient. Identify any
   unexpected active turn before stopping it; preserve its transcript.
2. Stop the Gateway with the installed `clawctl gateway-service stop`. Close the
   existing desktop applications. Check for backend children left after desktop
   closure; stop only exact verified children under the restart approval. Confirm
   the existing service ports are closed before relaunching.
3. Launch the existing Ollama and OpenJarvis applications and start the Gateway
   using `clawctl gateway-service start`. Read status until authenticated health
   succeeds. A `starting` acknowledgement is not readiness. Do not duplicate a
   pending start, clear locks, provision a profile or reset a connection.
4. Before starting ACP, require the package's status to provide the intended port
   and listener ownership. Reconnect the saved Companion connection normally and
   verify one paired online Node plus an actual `device.status` result. Leave
   additional capability declarations unapproved.
5. Verify unchanged configuration hashes and recovered task histories. Run a small
   sequential local completion and a real retained MCP health call. Run exactly
   one scoped ACP verification task with its project rules, exact cwd/test command
   and explicit time budget. Check native tool results and test exit codes; queued
   or accepted messages do not establish completion. Do not overlap long local
   agent turns on the shared inference runtime.
6. Close only the completed/failed test ACP session through the supported native
   operator control. Confirm its backend exits and the Gateway again supplies its
   port/ownership proof. Verify the Node and refresh the existing status report.
   Stop when a test fails; record the actual failure rather than reporting that
   all applications passed.

## Installed packaging limitation observed on 18 November 2026

The installed Gateway packaging source at commit
`30b5db3407a0a89b867ca9dc4ea9a8aa5604434e`,
`src/OpenClaw.Launcher/Program.cs`, selects a status port only when exactly one
port is observed. The installed Companion 2026.11.3 requires a port and ownership
proof before handing credentials to a Node. During this test an OpenCode backend
introduced another listening port; package status omitted the port/ownership
fields, and Companion refused the native handshake. Closing that exact ACP
session restored one listener and the valid status proof. Normal Reconnect then
restored the Node; `device.status` succeeded.

This procedure is supported lifecycle sequencing, not a permanent package repair.
It does not establish that a new native connection will work while an ACP backend
is listening. Never fabricate the missing proof, bypass ownership inspection or
change security settings to mask the failure.

## Inference recovery caveat

An automatic main-session recovery continuation competed with the scoped tests.
After its instruction and state were identified, its turn was cancelled while
the transcript was retained. A subsequent direct existing-model 27B check returned
the exact marker in 14.99 seconds. GPU offload remained 25/66 layers, so offload
alone did not establish the timeout cause. Do not present a model reload or a
single successful reply as a permanent server fix.

The supplied local report uses only fixed loopback health/model GET endpoints;
refreshing it does not run inference. OpenClaw/OpenCode evidence in it is dated,
not a live health assertion for those applications.
