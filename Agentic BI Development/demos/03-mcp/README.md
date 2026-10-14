# Example 3: MCP (36 to 42, recording, to decide then record)

**What you show:** an agent connected to the real model, so it stops guessing, and then what that connection lets
it do with nothing in the way.
**Point:** ground truth without process.

## Decide first
Which MCP: the Power BI modeling MCP or a Fabric MCP. Criteria: works offline-to-recorded with no id on screen,
reads tables and measures, can write a measure (so you can show the unguarded write), needs auth you can do
beforehand. Record the choice and version here once made.

## What goes on screen, in order
1. (0:30) The MCP connected; its tools listed. No tenant, subscription or workspace id visible.
2. (0:20) Paste [../BRIEF.md](../BRIEF.md) unchanged.
3. (1:30) It reads the real model first: actual table names, the actual date table, existing measures.
4. (1:00) **Repeat Example 1's follow-up** ("what is the date table called?") and show it answering correctly.
5. (1:30) It writes a measure into the model. Show the model changed.
6. (1:00) **The unguarded part:** there was no staging copy, no approval and no record of why. Ask: who signed this?

## Say
- Example 1 guessed the names; this one looks them up. That is the missing ground truth.
- Look at what changed: it can now write to the real thing. Capability, with no process around it.
- [Fill in after recording: one specific thing it got right and one thing nothing stopped.]

Pro: live ground truth. Con: no gate on what it writes; setup and auth. Deploys into folder `03 MCP` once run.
