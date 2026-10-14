# What the Fabric skills run did, step by step

Recorded 2026-10-10. Claude Code v2.0.69, Opus 4.5, account Prathy_C, folder `~/demo-fabric-skills` (now `workdir/` beside this file),
plugin `powerbi-authoring@fabric-collection` 0.3.19 (skills: `powerbi-report-cli`, `semantic-model-authoring`).
Prompt: `Build the report described in @BRIEF.md`.

## 1. Read the brief and load the skill
1. Read `BRIEF.md` (45 lines).
2. Loaded the `powerbi-report-cli` skill.
3. Read the skill's planning guidance (two reference files, about 730 lines).
4. Decided the brief was complete enough for the skill's fast planning path.

## 2. Find the workspace and the model
5. Checked for local PBIP or semantic model files. Found none.
6. Checked the Azure login (`az account show`): signed in as prathy@data-nova.io.
7. Listed Fabric workspaces through the Fabric REST API. The first call failed (missing `--resource`); it retried and found "UK Trade Data".
8. Listed the semantic models in that workspace. Found only `SM_UKT_DirectLake`, not `SM_UKT_Import` as the brief said.
9. Chose `SM_UKT_DirectLake` and carried on. It did not ask, although the brief said to ask before guessing.

## 3. Inspect the model
10. Loaded the `semantic-model-authoring` skill and read its metadata and REST API references (about 680 lines).
11. Ran DAX `INFO` queries through the REST API: 20 tables, 199 columns, 10 measures, 31 relationships.
12. Found the measures the brief named, plus `_Colour Balance` for the card colour.
13. Queried column values: `dim_flow[direction]` (Export, Import, Unknown), `dim_basis[basis_name]` ("BoP (SA)"), `dim_period_type[period_type_name]` (Monthly, Rolling 12 months, and others). One query failed on a wrong column name and it corrected it.
14. Looked for an existing field parameter. Two queries failed; it gave up and planned bookmarks instead.

## 4. Plan
15. Read the skill's design-brief references (about 530 lines).
16. Wrote a report spec to `_brief/report-spec.md` (281 lines): layout, bindings, page filters, validation targets.
17. Asked for approval of the spec. Approved.

## 5. Build
18. Read the skill's authoring references.
19. Found Microsoft's report CLI was not installed, and installed it globally (`npm install -g @microsoft/powerbi-report-authoring-cli`, version 0.5.0) without asking.
20. Scaffolded a PBIP project (`powerbi-report-author scaffold`).
21. Rebound the report from a local model to a live connection to `SM_UKT_DirectLake`.
22. Set the page to 1920 x 1080 and added two hidden page filters: basis "BoP (SA)" and period type "Monthly".
23. Wrote four visuals by hand as `visual.json` files: a title text box, a card visual (balance, exports, imports), a line chart (trend) and a bar chart (top partners). Backgrounds were typed as `#FFFFFF`.

## 6. Validate
24. Ran `powerbi-report-author validate`: 2 errors (an empty visual folder, a filter in the wrong place).
25. Fixed both; the second fix produced 2 new schema errors in a Top N filter.
26. Removed the Top N filter. Validation passed.
27. Desktop is not available on macOS, so it used the Service preview: rendered the local files in a headless browser against the live model, in create mode, without publishing.
28. Took a screenshot and reviewed it: the cards showed all-years totals, and the bar chart was empty.
29. Copied the screenshot into the folder and closed the preview.

## 7. Report back
30. Listed the deliverables and the checks it ran.
31. Listed four known issues: totals not filtered to 12 months, empty bar chart, no conditional card colour, no slicer.

## Result against the brief's "Done means"

| Check | Result |
|---|---|
| Exports £937.0bn, imports £980.4bn, balance minus £43.4bn | Failed: showed 30.3K, 31.6K, minus 1.3K (all years) |
| Card colour from a measure | Not done |
| Slicer changes the plotted measure | Not done (bookmarks planned, not built) |
| Every field exists in the model | Passed (schema validation) |

Note: the brief named the wrong workspace for `SM_UKT_Import` ("UK Trade Data" instead of "UK Trade Data Reports"),
which is why it found only `SM_UKT_DirectLake`.
