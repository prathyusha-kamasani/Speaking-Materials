# Page 06 build under full delegation: validation and tool improvements

Session: `claude-usha` (Prathy_C), worktree `agentic-bi-demo-ukt2`, branch `client/uk-trade-data/task/06-built-with-my-skills`.
Delegate `claude-fable-5-1`, `gates: all`. Started 2026-10-11 08:18. Observations are from reading the session log and
the worktree only; nothing in the session was touched.

## Validation (is it doing the right thing?)

| Time | Finding | Verdict |
|---|---|---|
| 08:21 | Checked a delegate was set before doing anything; stopped when none was | Correct |
| 08:24 | Asked Prathy how to build the trend switch (no headline field parameter) and recorded the answer as a driver decision | Correct: a real question to the driver, not a delegate call |
| 08:34 | Delegate sent back frame-engagement (stale Identity block) and the trend stories; approved requirements and proof points with notes | Correct: the delegate is reading cold and pushing back |
| 08:40 | First delegated decision on disk: `4-Governance/delegations/frame-engagement.md` | Correct |
| 08:4x | `engagement.md` now says the Direct Lake twin "was deleted on 2026-07-05". `SM_UKT_DirectLake` still exists in "UK Trade Data" (the Fabric skills run found it). The deletion noted in `workspaces.yaml` is a different model id | **Wrong fact written into a shared file**. Needs correcting before the Discovery gate |
| 08:45 | Thesis approved by the delegate after a revision; all six Discovery decisions recorded under `4-Governance/delegations/` | Correct |
| 08:48 | **Discovery gate passed under delegation.** Delegate `claude-fable-5-1` decided, `claude-sonnet-5-5` checked; the record says "Decided by a delegate, not by prathy". Live proof points 8 of 8 hold; exports 936.967 and imports 980.369 over April 2025 to March 2026 match the published £937.0bn and £980.4bn | Correct: two models, driver's name kept off the decision |
| 08:48 | The gate did not catch the wrong "Direct Lake deleted" line in `engagement.md`. The delegate checked the Page 06 section, not the shared Identity block above it | **Gap**: the wrong fact passed a gate |
| 08:49 | Model-alignment step reads "unknown": the sibling model tool's settings point at the Taylor Swift engagement's model, not UK Trade | Not blocking; the gate noted it |
| 08:49 | Committed Discovery as `6cbef1a` on its own branch; commit names the delegate, the checker and the driver's two decisions. The committed `engagement.md` still carries the wrong Direct Lake line | Correct process; the wrong fact is now committed |
| 08:50 | **Stopped and asked Prathy** rather than repointing the sibling model repo or working around the gate: the rail reads the Discovery gate as unknown while model-alignment cannot run | Correct: it would not bypass a gate or edit another repo |
| 09:50 | Created the model-repo worktree `agentic-bi-demo-model-ukt` (detached, read-only settings) after Prathy's go-ahead, added `model_tool` to `workspaces.yaml`; model-alignment now passes | Correct: asked before touching another repo |
| 09:50 | The Discovery gate flipped to "void: made before thesis was done", although it was recorded after the thesis. The builder is investigating rather than re-deciding | Rail ordering bug, see improvement 3 |

## Tool improvements (to port back to ReportAutomationAgent)

1. **Check facts against the live workspace before writing them.** The Identity rewrite took "deleted" from a comment in `workspaces.yaml` without listing the workspace. A one-line check (list semantic models) would have caught it.
2. **A new page edits shared Discovery files.** Page 06 rewrote `engagement.md`, `00-requirements.md`, `01-stories.md` and `03-profile.md`, which pages 01 to 05 also rely on. Discovery could hold a per-page section or file, so adding a page cannot change another page's evidence.
3. **The rail marks steps void by date, not by content.** Requirements decided in July read as void because they predate today's framing, though their content still held; that cost an extra delegate run. Voiding on a content change (a hash) would avoid it. It struck again at 09:50: once model-alignment passed, the already-recorded Discovery gate read as void, "made before thesis was done".
4. **Branches start from `main`, which lacks the UK Trade contrast triage** (`client/uk-trade-data/task/contrast-accept`). Until that branch is merged, any branch from `main` turns the-balance's pipeline red on the second run.
5. **A gate should read every line a page depends on, including shared sections.** The Discovery gate checked the Page 06 section and passed a wrong fact in the shared Identity block of the same file. Either the gate's evidence list names the whole file's changed lines, or shared facts get their own check.
6. **The sibling model tool has one global target.** Its settings point at one engagement's model at a time (currently Taylor Swift), so model-alignment cannot run for UK Trade without repointing it. A per-engagement target (from `workspaces.yaml`) would remove that.
7. **Some steps can never be delegated, and the build only finds out mid-way.** Repointing the sibling model repo, a one-time signed-in browser profile for the live style check, and merging an engine PR (bar colour by sign) all need the driver. A pre-flight that lists every driver-only step before the build starts would let a delegated run go end to end without stopping.

## Restart run (2026-10-11 10:08)

Fresh worktree `agentic-bi-demo-ukt`, branch `client/uk-trade-data/task/06-built-with-my-skills` from `contrast-accept`, model
tool declared up front (`../agentic-bi-demo-model-ukt`, targeting SM_UKT_Import). Times are UTC.

| Time | Finding | Verdict |
|---|---|---|
| 10:06 | A second session in the same folder was asked to grant delegation and refused: the grant needs an interactive terminal | Correct: an agent cannot grant itself delegation |
| 10:10 | Pre-flight listed every driver-only step before starting, as the prompt asked | Correct: improvement 7 from the first run, done by the prompt rather than the tool |
| 10:10 | Found the slicer cannot be built without a field parameter, which is a model change the brief forbids; offered three options and asked | Correct: asked before guessing, and named the conflict in the brief |
| 10:10 | Found `_Colour Balance` carries hex codes, checked them against the theme, and asked whether that meets "colours from the theme" | Correct |
| 10:10 | Planned a second deploy `--to-client` into "UK Trade Data Reports", reading "deploy through run_pipeline" plus `--gates all` as permission to ship to the client | **Wrong scope**: the brief never asked for a client deploy. Prathy had to rule it out |
| 10:10 | Said the live style check needs Chrome signed in. The repo's check runs its own Chromium on a saved profile (`pbi_auth_profile.py`); only the QA click-through uses Chrome. No saved profile existed, and it did not run `--check` to find out | **Inaccurate pre-flight** |
| 10:10 | Saw the model snapshot is 18 days old and plans to refresh it and recheck the £937.0bn / £980.4bn figures before design | Correct |

Tool improvements from this run:

8. **A client deploy should need an explicit target in the request.** `--gates all` lets a delegate sign the client-ship gate; it should not also choose to ship. The deploy target (canary only, or client) belongs in the grant or the request, and the default should be canary only.
9. **The pre-flight should run the checks, not describe them.** `pbi_auth_profile.py --check`, the snapshot age and model-alignment are all cheap commands; a pre-flight script that runs them and prints red or green would have replaced a paragraph of guesses about the browser.
10. **`pbi_auth_profile.py --login` did not close after a good sign-in.** Twice the window stayed open on Power BI and had to be stopped with Ctrl+C, yet `--check` afterwards passed. The login loop watches one page and does not see the sign-in finish; it should re-read every page in the context, or simply run the same test `--check` uses.
| 10:18 | No path can land a field parameter (the repo's model writer refuses calculated tables), so it started adding a `field_parameter` kind to the engine: `engine/gen/model.py` and `engine/model_requests.py` | Right fix, in the engine, per P8. **Wrong place**: the edits are on the client branch, and the repo's git rule says an engine change is its own `engine/<slug>` branch and PR, merged before the client work uses it. The merge needs Prathy |

11. **"Allow a model change" should come with a route.** The decision was recorded in seconds; landing it meant writing a new engine feature mid-run. The pre-flight should check whether each option it offers can actually be built today, and say so next to the option.

12. **A build session is an operator, not a builder of the tool** (Prathy, 10:20). It should run the engine and write only under `clients/<engagement>/`; when it meets a gap it logs it in `ENGINE-GAPS.md` and picks a supported option or stops. Today nothing enforces that: a hook that refuses edits to `engine/`, `scripts/`, `algorithms/` and `bundle/` on a `client/` branch would.
| 10:21 | Took a backup, then wrote the field parameter to the live SM_UKT_Import; the snapshot diff shows only the new table and its three columns | Careful write (backup, dry run, diff), but it ran on engine code written minutes earlier on the client branch and never reviewed |
| 10:22 | Set out to commit "this engine step" on the client branch before Discovery | Wrong place, see the 10:18 row. Prathy decided to restart the run |

## Second restart (2026-10-11 10:28)

Operator prompt, deny rules on tool code, field parameter already in the model, canary-only deploy, Chrome connected. Times are UTC.

| Time | Finding | Verdict |
|---|---|---|
| 10:28 | The `open -e` line was pasted into the session instead of a terminal; it ran it (opened the prompt in TextEdit) | Harmless; the setup steps should say which window each command goes in |
| 10:32 | Rewrote the shared Identity block of `engagement.md` and added a Page 06 brief section | Brief section correct and faithful to the brief |
| 10:32 | **Same wrong fact as the first run:** "The DirectLake twin was deleted on 2026-07-05". The block it replaced named `SM_UKT_DirectLake` `ffac1347` in "UK Trade Data"; the deletion noted in `workspaces.yaml` is model `3f8bfe3b`; the Fabric skills run on 2026-10-10 found `SM_UKT_DirectLake` still live | **Wrong**, and improvement 1 (check facts against the live workspace) is still open: the restart prompt did not fix it |
| 10:32 | Handed the draft to a separate claude-fable-5-1 delegate and said it does not decide its own draft | Correct |
| 10:33 | Drafts later steps in its scratchpad while the delegate reads, writing them into the engagement only after each earlier decision | Correct: keeps the rail's order |
| 10:35 | Delegate decided frame-engagement and requirements (`4-Governance/delegations/`); requirements went back for a revision | Correct: the delegate pushes back |
| 10:36 | Removed the July caveat "R01-R04 blocked by the Trade Total Monthly data bug" from the shared requirements, and added a page 06 section; stories gained 66 lines | Plausible (the live proof points now match £937.0bn), but again a new page rewrites evidence pages 01 to 05 depend on (improvement 2) |
| 10:36 | Checked the engine can emit the combined chart before the stories commit to it | Correct: feasibility before promise (answers improvement 11) |
| 10:37 | Logged DI-06 in `DATA-ISSUES.md`: goods imports in `Trade Goods Monthly` over-count against the headline | Correct and useful: an honest data note, not hidden |
| 10:41 | User stories decided by the delegate. Used the Taylor Swift engagement's page files as the reference shape, kept page 06's contract proportionate | Correct: reuse of a worked example, sized to the page |
| 10:42 | Profile sent back by the delegate for a revision; checking whether the engine can colour a series per measure before relying on it | Correct |
| 10:46 | All six Discovery steps decided by the delegate (frame, requirements, stories, semantic check, thesis, proof points). Checked that `_Verdict` reads the same 12-month window as the card before the thesis relies on it | Correct |
| 10:47 | Discovery gate: delegate and an independent checker run in parallel, and the checker never sees the delegate's verdict | Correct: a real second opinion. 19 minutes from prompt to gate, against 30 minutes in the first run |
| 10:49 | **Discovery gate passed under delegation**, checked by claude-sonnet-5-5, committed as `1910d8e` with every decision's rationale in `4-Governance/delegations/`. Live proof points hold: 936.967 / 980.369 / -43.402 | Correct. 21 minutes from prompt to gate |
| 10:49 | The gate passed the wrong "DirectLake twin was deleted" line again; the committed `engagement.md` carries it | **Same gap as the first run** (improvement 5): the gate does not read the shared Identity block it rewrote |
| 10:49 | Gate note: the trend is two aligned plots, not one visual, stated openly in US-12 | Honest design call, declared rather than hidden |
| 10:51 | Theme-and-brand and surface-and-canvas decided; the design contract is with a challenger model. One script edit silently did nothing (shell quoting) and it noticed and redid it | Correct recovery: it checked its own output |
| 10:54 | Met four engine limits and **logged them as G-16 to G-19 in `ENGINE-GAPS.md` instead of fixing the engine** (brand name assumed `primary`; page brief cannot carry a story's filter or visual type; no theme colour per field-parameter series; a text box cannot carry visual filters) | Correct: the operator rule held. Each gap names the code line that causes it |
| 10:55 | Added a theme variant "Customs House Monitor" (same colours, neutrals first so lines never take the sign colours) to the shared design system | Additive and reasoned, but a new page again edits a shared file. Re-dumping the JSON also turned an escaped em dash (backslash u2014) into a literal one |
| 10:54 | Validated the archetype draft offline and waited for the challenger before going further | Correct: does not build past an open challenge |
| 10:59 | Design contract decided by the delegate after the challenger's report | Correct: challenge, answer, then decide |
| 11:01 | Measured the archetype's text overflow and put the measurement in `archetype.md` for the delegate; found the recommender allows only line or area for a trend role, so the balance columns need another role | Correct: works inside the catalogue rather than around it |
| 11:04 | Archetype decided by the delegate | Correct |
| 11:05 | Found the engine emits the trend swap from one default measure plus a field-parameter hint | Correct: read how the engine does it instead of inventing a way |
| 11:06 | Used its own declared layout for the sketch, put a provenance note in the SVG, marked the composer's sketch "not taken", and logged the sketch-tool limit as G-20 | Correct and traceable; five gaps logged so far (G-16 to G-20), none patched |
| 11:06 | Waits for the delegate by polling the rationale file's modified time. The delegate wrote the file before the loop took its baseline, so the loop waits for a change that already happened, until its 10-minute timeout | **Race**: about 10 minutes lost. Delegate hand-offs should wait on a completion signal (the agent's result, or a done marker), not on a file's modified time |
| 11:17 | Sketch approved by the delegate; the session then hit the account's usage limit (resets 15:10 Amsterdam, 13:10 UTC) with the Design work uncommitted on disk | Not a tool fault. 49 minutes, 234 tool calls and several parallel delegate and checker agents used one session allowance: a full delegated run needs a higher plan or a split across sessions, and each phase should be committed as it closes |

13. **Delegate hand-offs should wait on a completion signal, not a file's modified time.** The 11:06 wait missed a rationale written nine seconds before it began and sat out its 10-minute timeout.

## Status of the improvements (2026-10-11)

Updated 11:45 UTC: 8, 10, 12 and 13 built on their own branches, none pushed or merged. To do after the session, each as its own `engine/` branch and PR in `agentic-bi-demo`, then ported back to ReportAutomationAgent.

| # | Status | Notes |
|---|---|---|
| 1 | Open | Hit again in the second restart (DirectLake line) |
| 2 | Open | Hit again in the second restart |
| 3 | Partly | Ship already voids on a content digest; the rest of the rail voids by date |
| 4 | Blocked | PR push refused: the pre-push suite is red on `main` (4 failures, see below) |
| 5 | Open | Hit again in the second restart |
| 6 | Worked around | Per-engagement model worktree; `model_tool:` exists, the model repo's settings file is the global part |
| 7 | Worked around | Asked for in the prompt |
| 8 | Built, not merged | `engine/delegate-client-deploy-explicit` (9770567): the grant must name each report with `--client-deploy` |
| 9 | Open | |
| 10 | Built, not merged | `engine/pbi-login-detects-signin` (16f2eac): sync Playwright never saw the URL change while the loop slept |
| 11 | Open | The session did it unprompted in the second restart |
| 12 | Built, not merged | `engine/client-branch-tool-guard` (3a74f2f): edit hook plus pre-commit check on `client/` branches |
| 13 | Built, not merged | `engine/delegate-handoff-done-signal` (4c906bb): `done: <step>` line and `delegate_step.py --verify` |

Suggested first: 12 (a committed hook), 8 (canary unless the grant names the client), 1 and 5 (live fact check, gates read shared sections), 4 (merge `contrast-accept`).

**`main` is red (found 11:30 UTC):** 4 failures on a clean checkout. `test_card_tile_list` and `test_group_region` fail Microsoft's validator with `PBIR_PLATFORM_LOGICAL_ID_INVALID` (the CLI on this machine is now 0.5.0, installed globally by the Fabric skills run); `test_ratchet` points at a test that no longer exists (`test_suite_layout_variety`); `test_record_step::test_next_takes_no_step_undo_or_reason` hits an argparse error. Each needs its own fix before anything can be pushed without `--no-verify`.

### Second restart, after the limit

| Time | Finding | Verdict |
|---|---|---|
| 13:10 | Resumed by itself after the usage limit, picked up where it stopped | Correct |
| 13:14 | Committed Design so far as `2155bf7` | Correct: commits as phases close |
| 13:1x | Ran several repo scripts through a scratchpad "shim" with one value corrected, to get past tool defects (G-16 to G-21); moved the deleted DirectLake model's snapshot to `model_schema/_archive/` because tools read the first snapshot alphabetically | **Grey area**: no engine file edited, but patching tools at run time is building, not operating. The edit guard (improvement 12) would not catch it |
| 13:15 | Stopped for Prathy: the slicer default "Exports and Imports" (its own US-13 AC4) cannot be built, the engine pre-selects one value only (G-22). The delegate refused to accept the workaround and called it a driver decision | Correct to stop. But the two-value default is not in the brief, which only asks the slicer to switch measures; the agent wrote the requirement itself and then could not meet it |
| 17:17 | Took option C: US-13 AC4 and the contract now default the slicer to Total trade, committed as `a0572f0` naming the driver's decision | Correct |
| 17:19 | Stories re-decided by the delegate; Discovery gate re-run with delegate and Sonnet checker in parallel | Correct |
| 17:20 | The rail refused to re-decide the Discovery gate: it reads "void", because committing the earlier step's files moved their time past the gate. Logged as G-23 | Correct to log it; the same date-based voiding as improvement 3, and now it blocks a gate outright |
| 17:21 | Weighed changing file times to clear the void, dropped it only because the rail reads git commit times | **Concerning**: it rejected tampering with gate evidence as ineffective, not as wrong. An operator should never consider it |
| 17:24 | Prathy undid the void Discovery gate at the terminal (`record_step --undo` with a reason); the rail now reads it as "needs decision" | The legitimate route: a decision taken back on the record, not evidence altered |
| 17:25 | Saved the rule "commit files before recording a decision; never alter gate evidence", then re-ran the gate: Sonnet approved, delegate pending. Design contract re-decided (`7bfd417`) | Correct |
| 17:29 | Discovery gate re-decided under delegation after the undo, committed `496f5b2`; checklist and wireframe generated (`814cfdd`) | Correct: the G-23 workaround worked |
| 17:31 | Mockup generation crashes on the partner bar chart: the mockup draws only from proof points, and none covers a category. Looking for another data source before touching Discovery files | Correct to look first. A real tool limit: a ranking visual needs category data the proof points never hold |
| 17:33 | Design loop done to the declared geometry (`f614641`). Stopped at the mockup: the mockup generator cannot draw a line chart, column chart, field-parameter slicer or multi-measure card (G-27), 4 of the page's 5 visuals; nor ground a column name with a space (G-26). Also needs global puppeteer for slop-check | Correct to stop: a mostly-placeholder mockup cannot be the contract. **The biggest tool gap so far**: the mockup step only covers the visuals the earlier pages used |
| 17:3x | Ran the mockup through a scratch shim again (draws an empty plot instead of crashing) | Shim again (improvement 15), declared openly, no data invented |
| 17:33 | Two more workarounds declared in the YAML (D1, D2): card surface as a panel shape behind the card (G-24); the top-12 order-by measure sits in the card tooltip (G-25), against the contract | Honest, but D2 breaks the contract and needs one more re-decision |
| 17:40 | Prathy chose B (placeholder mockup, declared), puppeteer against the installed Chrome, D1 and D2 accepted. Puppeteer 25.13 installed globally | Driver decisions, recorded |
| 17:40 | A commit came out empty because the commit hook re-captured two other pages' mockup manifests; it noticed and corrected the message | Correct recovery; a hook that rewrites other pages' files during a page's commit is surprising |
| 17:43 | Contract re-decided with D1, D2 and the partial mockup (`5efb54f`); design brief and UX validation written, G-28 logged; Design tidy archived the unchosen sketches (`e8ddc75`) | Correct; Design is nearly through |
| 17:48 | The tidy's link rewrite voided the archetype again, so it was re-decided (`9b1bf33`); logged G-29 | Same family as G-23 and improvement 3: a recorded, harmless change voids a decision |
| 17:49 | Config validates; declared the hero panel as a group region so the overlap rule passes, matching D2; re-ran the live proof points before writing APPROVED.md | Correct: evidence refreshed right before the sign-off |
| 17:52 | Declared the placeholder mockup as an `open-engineering` deviation, so the design gate goes to Prathy: a delegate never accepts one | Correct and honest: the rule held without being reminded |
| 17:5x | Tried a mockup screenshot through an unsandboxed run; the auto-mode safety check refused it and it dropped the attempt | **Should not have tried**: stepping outside the sandbox is not an operator move. The safety layer caught it |
| 17:5x | With puppeteer installed, the commit hook re-captures every page's mockup measurements and now marks one element each on pages 02 and 03 as clipped (`ca2d73b`) | A new page's run changes other pages' evidence through a hook; worth a check that a page's commit only re-captures its own page |
| 18:00 | Prathy cherry-picked the G-30 fix (`55034f9`) after a dry run on a throwaway copy showed diverge done and the design gate waiting | The engine fix came from outside the run, recorded as the driver's decision |
| 18:09 | Prathy signed the design gate at the terminal, confirming the 12 delegated decisions it lists (`f9bb7cf`) | The four-gate rule working: the open-engineering mockup went to a human |
| 18:11 | Build and offline gates green (`e04af83`) | First green build of page 06 |
| 18:12 | A deploy guard needed the model's workspace name in the config. It edited the config after the design gate, checked the rail before committing, and was ready to revert if the gate voided; it held (`cfe4a30`) | Careful. Note the gap: a config edit after sign-off did not need re-approval, because the rail's fingerprint check passed on a field outside the design |
| 18:14 | **First canary deploy live** in Fabric Friday Demo; DAX verify, render-match and tooltip checks green. The Service's own render (Export API) shows four defects: the hero card errors, slicer labels clipped, both trend plots scroll sideways (72 text months), ranking caption clipped | The canary did its job: real defects found before anyone saw the page. The render-match was green because it compared against a placeholder mockup (G-27), so only the Service image caught them |
| 18:17 | Fixed the card tooltip name and caption room (`3c50141`); the redeploy then stopped at phase-order because the mockup is now newer than APPROVED.md, so the sign-off needs Prathy again | Correct: a render fix after sign-off is a design change |
| 18:18 | No browser tools in the session, though the prompt said Chrome was connected; QA click-through cannot run | Setup gap: `/chrome` was never run in the session (step 3 of the restart steps) |
| 18:32 | Before changing US-12 AC2 it tried the edit uncommitted, saw the Discovery gate void, restored the file and stopped, as Prathy's rule says | Correct: tested, reverted, asked. A one-line story change after the gates costs an undo and a re-decision (G-23 again, improvement 3) |
| 19:0x | Prathy re-signed the design gate after render fix 1 (`a5dfd2a`) | Each render fix after sign-off costs a signature: correct, but slow |
| 20:11 | **Second canary live** (`7fbc482`). The card now renders with the right figures (-43.4, 937.0, 980.4) and the clay colour on the balance only; trend window, slicer labels and caption fixed. Still wrong: card figures cut off, tile labels missing, balance shown as (43.4), the two trend plots misaligned by the line's end label, a stray "0.0" on the zero line | Canary loop working: each render finds what no offline check could. Its own report of the remaining defects matches the image |
| 20:41 | **Third canary** (`8af735a`), after render fix 2 and Prathy's third design-gate signature. Fixed: line plot width, zero label, legend space. Still wrong: the card's figures and labels clip however tall the card is (stacked tiles get a third of the height each); the two plots are about 20 px apart at the start (axis label widths) | Each render loop costs about 25 minutes and a driver signature. No offline check predicts a card's internal layout: only the Service render shows it |
| 20:46 | Render fix 3 trial: card tiles side by side. **The card renders in full**: labels Trade balance, Exports, Imports; (43.4) in clay with the verdict under it; 937.0; 980.4. The whole page now matches the design. Saved Prathy's "decide render fixes yourself, batch the signature" as a standing rule | Fixed in one round, with the fallback ready if needed. The rule should cut the remaining stops to one signature |
| 07:22 (12 Oct) | **Final canary deploy**, build `193c505aeba8` (the one Prathy signed), commit `7f79b4c`, Fabric Friday Demo only. The render matches the checked trial: card in full, trend, slicer, ranking and caption all right | Done. Not done: the rail stops at live-verify because the style check compares against the placeholder mockup (G-27), and the QA click-through never ran (no browser tools in the session) |

14. **Do not let the build invent acceptance criteria the engine cannot meet.** Stories should be checked against the engine's capabilities when they are written (a feasibility pass on each acceptance criterion), and anything beyond the brief marked as optional.
15. **Run-time shims around repo scripts should count as tool edits.** Either the guard covers scripts run from a scratchpad with patched values, or the session must stop and log the gap instead.

17. **A render-fix loop should not need a full design-gate signature for each layout nudge.** Three canaries, three signatures, about 75 minutes. A pixel change inside the declared geometry could be a delegated decision, with the gate re-signed once at the end.
16. **Gate evidence must be tamper-evident, and the operator told so.** The session considered changing file times to clear a void gate. The rail already dates evidence by commit time, which is the right defence; the operator rule should also say in words that gate evidence is never altered to pass a gate.

## Why full delegation did not deliver a polished page (2026-10-12)

The final canary (`193c505aeba8`) is correct but not polished: the card tiles are half empty below the figures, the balance reads (43.4) not minus 43.4, and the month labels are rotated and crowded. Earlier canaries shipped a clipped card three times. No step approved the clipped card; no step looked at it.

**Why it got through**

1. **The reviewers judged documents, not the page.** The delegate and the Sonnet checker read the contract, config and stories. No model was asked to judge the rendered page against the principles.
2. **The design gate comes before the report exists.** It approves the plan; the build and canary follow, and nothing after the canary blocks on what the page looks like.
3. **Clipping is checked on the mockup only.** `run_pipeline` checks the mockup's own render for clipped content. The Service render is captured as an image, nothing reads it for clipping, render-match is advisory, and the live DOM style check is unfinished (WP-09).
4. **The mockup was mostly placeholders (G-27),** so "render equals mockup" (P10 with P11) had nothing to compare against.
5. **The QA click-through never ran** (no browser tools in the session).

The clipping was caught only by reading the PNGs by hand, and took three render rounds, each needing a driver signature.

**How to get there**

1. **A blocking gate on the live render:** after each canary, a different model reviews the Service image against the principles and the brief's acceptance tests, plus a deterministic check of the live DOM for clipped or overflowing text (finish WP-09). A failure loops back automatically.
2. **A real mockup contract:** close G-27 (renderers for line, column, field-parameter slicer, multi-measure card) so the design gate can be delegated and render-match means something.
3. **Delegated render fixes** (improvement 17): fix, redeploy, re-check without a signature per nudge; one signature at the end only if a gate needs it.
4. **QA without the Chrome extension:** run the click-through in the repo's own Playwright browser on the saved Power BI profile.
5. **Design only with proven visuals:** a feasibility pass before design (improvements 11 and 14), so a new page type does not uncover gaps one at a time.
6. **Void by content, not date** (improvement 3), removing the undo and re-decide loops (G-23, G-29, G-30).

With 1 to 3 in place, this run would have needed Prathy for the Discovery questions only, and the clipped card would have been fixed before anyone saw it.

## Trade stripes run (2026-10-12)

Page 07, fully delegated, operator only, started 15:48 UTC on the merged main (all fixes from this document). Times are UTC.

| Time | Finding | Verdict |
|---|---|---|
| 16:46 | 58 minutes in: Discovery gate decided, Design through archetype, sketch, contract, seed, design loop (2.9/3, 0 blockers), mockup drawn from a live data sample of 315 months, design brief and UX validation; no question to the driver, no tool-code edit | Compare: the page 06 run needed the driver five times before reaching the same point |
| 16:45 | Checked whether the Design tidy's link rewrite would stale a decided file before applying it (the G-29 case, now fixed) | Correct |
| 16:4x | Logged two engine gaps instead of patching: G-38 (trend role offers no column chart) and G-39 (no "is not blank" filter, needed for 56,364 undated rows). Background builders started on both | The operator and builder split working as designed |
| 16:5x | **Design gate decided by the delegate**, checked by Sonnet (`7757d2f`): the mockup drew real data, so nothing was open-engineering and the gate stayed delegated | The page 06 run needed four driver signatures for this gate |
| 16:56 | **First canary.** Headline, key and annotations right and computed: "290 of the 315 months since January 2000", first surplus Feb 2011 +£1.5bn after 133 months of deficit, largest surplus May 2020 +£9.5bn, largest deficit Jan 2022 -£10.9bn. **The stripes are wrong**: about 47 wide columns, a horizontal scrollbar, most of the 315 months off screen, large empty bands above and below | G-36 confirmed in the render: the no-gap and per-month width settings did not fit 315 columns into the page. The live-render check and render review should catch it; whether the operator can fix it without an engine change is the test |
| 16:5x | Logged G-40 (render match compares a theme role with a hex as text); builder started | |
| 16:58 | To get one thin column per month it added a calculated column `'Date'[Month Sequence]` to the live model through the model-request route, verified it by DAX (24006), and used it as the axis | Right idea (a numeric axis fits all 315 months), and it went through the route. But the brief allowed new MEASURES; a calculated column on the existing Date table is a new object on an existing table, which the brief did not name. A judgement call the brief should have settled |
| 17:06 | Wrote a new APPROVED.md, then set it aside in its scratchpad and restored the signed one, so the existing gate decision stands while it trials the fix on the canary; plans to re-decide the gate once, on proof | **Grey zone (improvement 16):** managing gate-evidence files to run a trial. The intent is sound (decide once, on proof), and the delegated render-fix path exists for this; moving APPROVED.md around is not that path |
| 17:09 | **Second canary (trial of render fix 1).** All 315 months now fit as thin columns with no scrollbar, deficits in clay below the line, surpluses in green above, the 2019 to 2020 surplus cluster and the 2022 deficit clearly visible; headline, key and annotations unchanged and right | Fixed from the config and one new model column, no engine change: the loop worked without the driver. Remaining design questions for the review: nothing on the stripes says where 2011, 2020 or 2022 fall, and the band above the stripes is still mostly empty |
| 17:0x | Logged G-41 (interaction inventory crashes on a single tooltip binding); used the list form as a workaround; builder started | |
| 17:21 | Design gate re-decided for render fixes 1 and 2 by the delegate, checked by Sonnet (`544d809`): no driver signature for render fixes | Improvement 17 working |
| 17:23 | **Third canary, GREEN across every stage.** Stripes on the date axis now fill the full width: 315 thin columns edge to edge, colour by sign, no scrollbar; text all whole | The page now does what the brief asked. Open for the render review: no year markers on the stripes, empty band above |
| 17:2x | Logged G-42 (no start/end for a continuous category axis); builder started | |
| 17:3x | Render fix 3: added a second calculated column, `'Date'[Stripe Position]` (0 to 996.8, evenly spaced), to pin the stripes' end bound; the gate delegate found the mockup drawing the first surplus about 60 px early, which exposed G-43 (mockup sorts numeric categories as text); worked around with an explicit sort; fifth gate decision under way | The delegate checking the mockup against the render caught a real tool defect. Two calculated columns now added to the shared Date table for one page, beyond the brief's "new measures"; worth a note in the hand-back |
| 17:41 | **Fourth canary (render fix 3), green**: 315 months in one view, no seams, design gate re-decided by the delegate again (`fee02f3`) | The page is right |
| 17:44 | First headless QA run on the live canary: 18 of 18 render items failed as "still spinning", while the screenshots and the live-text check show every visual painted. It logged G-44 (the runner counts the Service's hidden spinners) and, as Dev, flagged the 18 bugs back to QA without closing them | Two-team rule held: Dev did not close its own bugs. First live run of the QA runner found a real defect in it |
| 17:48 | Usage limit reached; resumes 19:50 UTC | Remaining: the QA pass once QA re-judges, then the hand-back |
| 19:50 | Resumed by itself after the usage limit | |
| 19:5x | Render fix 4: headline and annotation type moved up the brand scale so the page reads at phone width; the mockup cut lines the check called clean, so it logged G-45 (text boxes not measured); delegate approved with conditions, second model checked, gate re-decided (`8b4368f`) | The render review's job done by the run itself: readability, not just correctness |
| 20:00 | **Fifth canary**: larger headline over three lines, larger annotation labels and values, stripes unchanged, all text whole | The page reads better on a small screen; still to do: render review record, QA re-judgement, hand-back |
| 20:07 | **QA pass on the fifth canary**: 32 pass, 2 fail. QA itself closed the 18 false render fails after confirming G-44, and raised two real bugs: BUG-07-020, the stripe tooltip shows a position number and "(10.9)" but no month; BUG-07-019, verify-dax's query shows a 316th blank row the page does not draw (G-46). **Render review approved** | QA found what a person would find by hovering, without a browser extension and without the driver |
| 20:1x | Render fix 5: a new measure gives the tooltip its month, verified live; BUG-07-019 flagged back to QA as a tool defect (G-46); builder started | |
| 20:2x | **Sixth canary green, render review approved; QA re-test 34 of 34 pass**, QA closed BUG-07-019 to 038 itself and one item as declared; QA sign-off green (`dab3d4f`) | Clean QA pass with no browser extension and no driver |
| 20:32 | Ship approval approved by the delegate, second check running. No client deploy: the grant names no report | The client-deploy rule (PR #31) holding |

### Trade stripes run: cost, a model finding, and process improvements (2026-10-12)

**Tokens, to 20:33 UTC** (main session plus 39 helper agents): 0.32M output, 0.0015M fresh input, 3.7M written to cache, 187M read from cache. The main session alone read 169M from cache: each step re-reads the whole growing history (3,000+ entries), which is also why the run hit the usage limit.

**The delegate was not a different model.** Every delegate request asked for `fable` (claude-fable-5-1); all 28 were served by claude-opus-5-5, the drafter's own model. The 11 second checks did run on claude-sonnet-5-5. The delegation records say "claude-fable-5-1". The page 06 run shows the same fallback. Likely cause: Fable is not available on the claude-usha account and the request fell back silently. Until fixed, do not claim "a different model decided": only the second check was independent.

**Process improvements, in order:**
18. **Prove the delegate model.** Record the model that actually answered (from the agent's responses), not the one requested; refuse a decision when it equals the drafter's model or the request fell back.
19. **A fresh session per phase** (Discovery, Design, Develop, Verify), handing over through the rail and the repo, so no step re-reads hours of history. Cuts cost and most usage-limit pauses.
20. **A render spike for unproven properties during Design**: a one-visual canary of anything the feasibility pass marks as unverified (G-36 here), instead of finding it after the first full canary.
21. **Light render fixes**: route every render fix through `delegate_step --render-fix`, with fix notes in the rationale, not the contract or design docs, so a fix does not re-run the whole sign-off chain (five fixes meant five full gate decisions here).
22. **The tool launches builders and allocates gap ids**: a script opens a builder task for each new ENGINE-GAPS row, with ids allocated from main (today's ids clash across branches); low-risk verified builder fixes may merge mid-run so the run benefits.
23. **Grey zones become rules**: the brief template names which model objects a run may add (measures, calculated columns, tables); only the sign-off script may write APPROVED.md (hook).
24. **One generated port-back list** for ReportAutomationAgent, built from the JOURNAL entries and ticked off as items are ported.
| 20:34 | Ship approval approved by the delegate and checked by Sonnet for build 65a202b767f7; client-deploy grant for trade-stripes found on record | |
| 20:3x | Render fix 6 after the ship approval: sign colours written as the theme's hex values to dodge G-40 before the client deploy; output byte-identical, but the config changed, so the design gate, canary and ship approval are re-run (about 10 to 15 minutes) | Correct under void-by-content, wasteful here |

25. **Approvals should follow the build, not the config text.** When a config change produces a byte-identical build (same digest), the design gate, canary certificate and ship approval should stand. Today render fix 6 re-ran the whole chain for no visible change.
| 20:48 | **Client deploy** of "UK Trade - Trade stripes" to "UK Trade Data Reports" and verified, build 65a202b767f7, all stages green; checked the workspace: the new report is the only addition, the other reports are untouched | The per-report client-deploy grant (PR #31) used as designed |
| 20:5x | The client verify rewrote the live-render result the render review had approved, voiding QA, ship approval and the client deploy on the rail (G-47); it re-confirmed the review on the client render, re-ran QA sign-off, built the deliverable pack, drafted owner acceptance | Another case of a harmless change re-opening approvals (see improvement 25) |
| (builder) | Fixing G-47 found that the client run's live-text check re-judged the canary's stored snapshot of the same build: the "client page measured" result was really the canary's page. Same build, so the outcome holds, but the client copy was not measured live | Claim only "same build verified on the canary" for this run's client copy. PR #55 makes the client check capture the client page live |
| 20:59 | **Run complete: all 44 rail steps done**, Discovery to owner acceptance, delegated and checked; deployed to canary and client (build 65a202b7); the client render is pixel-identical to the approved canary render; the deploy deleted nothing in the client workspace | 5 h 11 min on the clock, 3 h 9 min working after the 2 h 2 min usage-limit pause; zero driver interventions apart from the optional client-deploy grant |
| 20:59 | The hand-back says "every decision and gate was taken by claude-fable-5-1"; the transcripts show they were served by claude-opus-5-5, the drafter's model (only the Sonnet checks were independent) | **Wrong claim in the hand-back.** Correct it before quoting the run (PR #54 makes this impossible next time) |
