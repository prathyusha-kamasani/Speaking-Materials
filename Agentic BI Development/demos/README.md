# Demos

One brief, four ways, in the order they run on stage. Times are from `../SESSION-PLAN.md`.

| Min | Folder | Medium | Status |
|---|---|---|---|
| 24-30 | [01-chat](01-chat/) | recording | to record |
| 30-36 | [02-fabric-skills](02-fabric-skills/) | recording | to record |
| 36-42 | [03-mcp](03-mcp/) | recording | MCP to decide, then record |
| 42-49 | [04-skills-plus-own](04-skills-plus-own/) | live, offline (A and C), recording (B) | A verified, C green on `contrast-accept`, B to record |
| 49-56 | [05-the-mistake](05-the-mistake/) | recording | to record |

Start with [00-setup](00-setup/) before you walk on, and [BRIEF.md](BRIEF.md) for the shared requirement.

Rules for everything in here: no client names, no tenant / subscription / workspace ids on screen, demo from a
tagged commit of `agentic-bi-demo` rather than the working tree. Only Demo A and Demo C run live, and both are
offline.

## Fabric Friday Demo workspace (dev / canary)

Folders created 2026-10-08, one per example that deploys. Example 1 (chat) has no folder.

| Folder | Holds | Status |
|---|---|---|
| `02 Fabric skills` | the report the Fabric skills produce | empty, waiting for the run |
| `03 MCP` | the report the MCP agent produces | empty, waiting for the MCP choice and the run |
| `04 Skills + your own` | `UK Trade - The Balance`, deployed via `run_pipeline --deploy` | report moved in; a redeploy was confirmed to keep it there (2026-10-08) |

`deploy_fabric.py` has no folder support. Moving an item is `POST workspaces/{ws}/items/{item}/move` with a
`targetFolderId` (worked on 2026-10-08). Other reports in the workspace (`One Word Per Era`, three `Gallery`
reports in `Other`) are unrelated to the session and will show on the projector.
