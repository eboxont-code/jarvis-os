# OpenClaw Windows Gateway multi-listener repair candidate

**Status:** Proposed patch preserved; not applied upstream, not built, not installed, not tested on Windows.
**Base repository:** `openclaw/openclaw-windows-packaging`
**Base commit:** `7185d5ea504643e0799f3ae665f64180261d5da5`
**Upstream discussion:** https://github.com/openclaw/openclaw-windows-node/issues/1691#issuecomment-6818699921

## Proposed source change

The GatewayStatus callback in `src/OpenClaw.Launcher/Program.cs` uses a count-only observed listener selection. Replace only that expression with the existing `Gateway.GatewayAddress.ResolvePort(result.Record)` helper.

The helper's existing tested policy:
- If fresh observed listeners are absent, use the explicitly configured port when present.
- If the configured port appears among fresh observations, select it even when other listeners exist.
- If no configured port matches and exactly one listener is observed, use that one.
- If multiple listeners remain unclassified, return null rather than guessing.

This mirrors the existing top-level `clawctl status` path. The selected port also gates the producer's serialized `gateway.ownership` block, so preserving a valid configured port allows ownership serialization to proceed through the existing required identity/listener checks. No ownership checks are bypassed.

## Regression coverage required

Add or extend a command-level test in `tests/OpenClaw.Launcher.Tests/ProgramTests.cs` driving the actual `gateway-service status --json` command and serialization:

1. **Configured match among multiple listeners:** record configured port 50368 and observed listeners [50368, 50370]. Assert state is running, `gateway.port` is 50368 and `gateway.ownership` is present with the expected sandbox, agent SID and listener identity. Use test fixture values only.
2. **Ambiguous unpinned control:** no configured port and multiple observed listeners [50368, 50370]. Assert `gateway.port` and `gateway.ownership` remain absent.
3. **Single listener control:** configured or sole observed port resolves as before.
4. **Nonmatching configured port control:** configured 50368 but observed listeners [50370, 50371] must not return 50368; multiple unclassified listeners remain unresolved.
5. Preserve all existing process ID, process start-time and sequence-number requirements. The port selection change must not weaken listener ownership validation.

The existing `GatewayAddressTests` already cover the helper's configured-port-among-multiple and ambiguous-unpinned semantics. Command-level coverage is still needed to exercise GatewayStatus callback wiring and `ClawCtlJson.FromOwnership`.

## Do not bundle without separate review

- Do not change the separate count-only selector used by dashboard environment setup without analyzing its distinct environment/URL semantics.
- Do not choose the first observed listener.
- Do not infer the upstream default port.
- Do not bypass Companion credential preflight, listener loopback/address validation or process sequence attestation.
- Do not use Gateway restart as a fix; the upstream reproduction reports it clears the auxiliary browser listener only temporarily.

## Evidence and limitations

The upstream issue describes an auxiliary listener created by packaged `openclaw browser status --json`, after which Gateway service status loses `gateway.port` and `gateway.ownership`. A later report cites the same Gateway MSIX and Companion stable versions as the user's installation. The user's own last status snapshot had one listener and complete fields, so this multi-listener state has not been captured in the user's failing Companion invocation.

The linked GitHub connection has read/comment but no push permission on the upstream packaging repository (branch creation returned HTTP 403). The exact proposed repair and command-level regression cases were posted publicly at [issue #1691 comment](https://github.com/openclaw/openclaw-windows-node/issues/1691#issuecomment-6818699921) for maintainer review. The linked GitHub account has `pull=true`, `push=false` on the packaging repository; no upstream branch or PR could be created. No upstream code, release, Windows install, user data, token or pairing was changed.
