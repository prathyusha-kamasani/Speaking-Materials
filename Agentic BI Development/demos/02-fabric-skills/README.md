# Example 2: Fabric skills (30 to 36, recording, to record)

**What you show:** the same brief through Microsoft's own skills, producing a real report file.
**Point:** grounded and quick, but it advises and does not block.

## Before recording
- Install Microsoft's Fabric Skills per Microsoft's documentation. Write the version and date in `SETUP.md`
  here, and show it on screen for 5 seconds: it is the evidence you set it up fairly.
- Use the same Fabric Friday Demo workspace. This example deploys by the skill's own route, not
  `run_pipeline`: that contrast is the lesson. Move the result into the Fabric folder `02 Fabric skills`
  (`POST workspaces/{ws}/items/{item}/move`, as used on 2026-10-08).

## What goes on screen, in order
1. (0:30) The skills installed; version and date.
2. (0:20) Paste [../BRIEF.md](../BRIEF.md) unchanged.
3. (2:30) The agent works: reads the skill, builds report files. Do not narrate every step.
4. (1:00) The report opens in the Service. Click through the page.
5. (1:30) **The checks you would have to do.** Does the card colour flip on a negative balance? Does the slicer
   change the measure? Is there a date dimension? Show how you would find out (by hand).

## Say
- Microsoft's skills are good and a first draft arrives far faster than anything I build. Concede it loudly.
- The point is not quality. It is that the skill advises. Nothing here would have stopped a bad report, and
  nothing records who approved it.
- If you ran it twice, you may get two different reports. [Only say this if you recorded a second run.]

Pro: Microsoft-maintained, grounded in real formats. Con: advisory, generic, no audit trail.
