# To do

## Slides
- [ ] Slide 14 (Advisory or blocking?): rewrite the bottom line. Current text: "A knowledge file is advice. Any tool can skip it, on any run. A check cannot be skipped." It reads as wordplay and uses "knowledge file", which the slide never defines. Option on the table: the Copilot story from `STATE.md` 2026-07-15 ("A Copilot session had every instruction file, and still shipped a bad report and deployed it by hand. The layout mistakes it made now fail the build."), after checking which three layout anti-patterns were made blocking.
- [ ] Slides 17 to 19: decide whether to renumber Example 2, 3, 4 to 1, 2, 3 now that plain chat sits in section 02.
- [ ] Slide 2: confirm the three About me lines are current.
- [ ] Slide 23: check the three links open (data-nova.io, linkedin.com/in/prathy, github.com/prathyusha-kamasani).

## Recordings
- [ ] Fabric skills, MCP and my own setup: record and drop into `slides/deck/media/`.
- [ ] Plain chat: check the real values of `Flow[Direction]` match "Export" and "Import" used in the second answer.

## Tool improvements (after the session)
- [ ] Build the 13 improvements captured in `demos/04-skills-plus-own/build-observations.md` (status table at the end), each as its own `engine/` PR, then port back to ReportAutomationAgent. Start with 12, 8, 1 and 5, 4.

## Polished output under full delegation (after the session)
Detail: `demos/04-skills-plus-own/build-observations.md`, section "Why full delegation did not deliver a polished page".
- [ ] Blocking live-render gate: a second model reviews each canary's Service image against the principles and acceptance tests, plus a live DOM check for clipped or overflowing text (finish WP-09)
- [ ] Close G-27: mockup renderers for line, column, field-parameter slicer and multi-measure card, so the mockup is a real contract and the design gate can be delegated
- [ ] Delegated render-fix loop (improvement 17): no driver signature per layout nudge
- [ ] QA click-through in the repo's own Playwright browser (saved Power BI profile), not the Chrome extension
- [ ] Feasibility pass before design: every visual and acceptance criterion checked against what the engine can build (improvements 11, 14)
- [ ] Void rail steps by content, not date (improvement 3; G-23, G-29, G-30)
- [ ] Mockup follow-ups found while building the renderers: (1) a text box bound to a measure shows the gallery sample "£1.80M", invented data, must show an honest placeholder; (2) line and column plots draw empty unless proof points carry monthly or per-category values: add a Discovery data sample (captured from the live model) so the mockup can plot real data; (3) Power BI draws bar/column axis text at about 12.5pt where the theme says 15pt, unexplained; (4) the 16pt chart title band is about 6 px taller in the mockup than the render
- [ ] Page 06 polish: card tiles half empty, (43.4) instead of minus 43.4 (G-31), rotated month labels; QA click-through still to run

## Engine follow-ups from the skills-for-fabric review (merged as PR #44)
Detail: `knowledge/references/skills-for-fabric-drift-2026-09.md` in agentic-bi-demo.
- [ ] Decide: `scripts/verify_rendered.py` (local Desktop bridge, not used on macOS): rewrite to `powerbi-report-author preview --host desktop` (needs a .pbip) or retire it
- [ ] Decide: should the CLI's service preview become a check before the canary deploy?
- [ ] Decide: should gates pass `--no-schema` to `validate`, so `--until gates` stays fully offline (CLI 0.5.0 fetches remote JSON Schema by default)?
- [ ] Engine fixes, each its own engine/ branch: `formatString` on emitted measures; `_fx_selector` by visual family, deferring to a declared selector; repoint the table web-URL trick; button state ids and shape `text.show` (render-checked); `fmt="PBIR"` on deploy getDefinition calls; then smaller fixes, knowledge fixes, and canaries for the three render-verified shapes
- [ ] Remove the 7 stale entries from the PBIR validate baseline

## Process improvements from the Trade stripes run (detail: build-observations.md, improvements 18 to 24)
- [ ] 18 Prove the delegate model: record the answering model, refuse a fallback or the drafter's model (in progress)
- [ ] Slides: do not claim "a different model decided" until 18 is fixed; this run's first decisions were on the drafter's model
- [ ] 19 A fresh session per phase, handing over through the rail
- [ ] 20 Render spike for unproven properties during Design
- [ ] 21 Route render fixes through delegate_step --render-fix
- [ ] 22 Tool launches builders; gap ids allocated from main
- [ ] 23 Brief template names allowed model objects; only the sign-off script writes APPROVED.md
- [ ] 24 One generated port-back list for ReportAutomationAgent
- [ ] Review and merge builder PRs #45 to #53 (gap-id clash: #45 and #46 both use G-42)

## Clean-up after the session
- [ ] Delete the Entra app registration "Power BI MCP - VS Code" (client ID 8e906d0a-3505-4b87-9f8b-48c020d21b19), created 2026-10-10 and no longer used: `az ad app delete --id 8e906d0a-3505-4b87-9f8b-48c020d21b19`
- [ ] Decide whether to keep the Fabric tenant setting "Users can use the Power BI Model Context Protocol server endpoints (preview)" enabled (switched on 2026-10-10 for the MCP demo).
