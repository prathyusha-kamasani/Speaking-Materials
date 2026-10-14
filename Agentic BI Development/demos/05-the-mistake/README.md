# Demo D: the mistake every check passed (49 to 56, recording)

**What you show:** a field-parameter slicer that looks perfect and drives nothing, found only by clicking it.
**Point:** automated checks catch what they were written to catch. The interaction layer is still yours.

## The facts (from `BUGS.md` BUG-02-001 and `ENGINE-GAPS.md` G-05)
- Report `02-trading-partners`: the Flow Control slicer (Total / Exports / Imports) and the partner ranking bar.
- Found 2026-07-20 by driving the report in the Service. Selecting a flow left the bar on "Top 15 partners by
  total goods trade" with identical values and an unchanged title.
- Cause: the engine emitted the slicer but never the binding on the chart that consumes it, so the chart stayed on
  one fixed measure. Gates, DAX and render-match all passed.
- **It is fixed**: G-05 closed and render-confirmed 2026-07-20.

## Problem to solve before recording
Because it is fixed, the live deployment no longer shows the failure. Options, best first:
1. Rebuild the report from the commit before the fix into a scratch location and record the broken slicer there.
2. Use the evidence already on file (BUGS.md text, any screenshots) and tell it as a story over the config.
3. Reverse it: show it working, then the line of config that makes it work, and tell what was missing.
Check the recording for tenant, subscription and workspace ids either way.

## On screen
1. (0:30) The slicer and the bar. Click Exports, then Imports.
2. (0:30) Nothing moves. Say what you expected.
3. (1:00) The gates from that day: all green. Read the list.
4. (1:00) The one-line cause, and the fix in the engine.

## Say
- Everything was green. The slicer rendered and accepted a selection, and it drove nothing.
- No headless check could see it. A person clicking found it in a minute.
- That is where you stay in the loop.

Backup mistake: **G-02b**, a guessed custom-visual GUID that rendered blank cards. The fix was to capture the real
shape, never guess.
