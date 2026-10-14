# UK Trade Balance report checks

## Model checks

- Confirmed the report connection targets `SM_UKT_Import` in `UK Trade Data Reports` (semantic model ID `cb882e01-dca5-4cca-9129-b27bf3d85b13`).
- Queried the 12 months from April 2025 through March 2026 with `Basis[Basis Name] = "BoP (SA)"` and `Period Type[Period Type Name] = "Monthly"`: exports `936.967`, imports `980.369`, balance `-43.402` GBP billions. Rounded to one decimal, these are £937.0bn, £980.4bn, and -£43.4bn.
- Queried the rolling measures under the same filters: last data month `2026-03-01`, exports `936.967`, imports `980.369`, balance `-43.402` GBP billions.
- Queried `Trade Goods Monthly` for the same date window: the only returned combination was `IMTS (NSA)` / `Monthly`, with £1,154.3051bn total goods trade. The partner ranking is separately filtered to `IMTS (NSA)` and does not reconcile to the BoP headline.
- Confirmed `_Flow Parameter[Parameter]` contains `Total`, `Exports`, and `Imports`; its field parameter targets goods measures. The report-level `Headline Trend` measure maps those labels to the existing headline measures instead.
- Executed the report-level `Headline Trend` switch expression under BoP (SA)/Monthly filters. Returned exports `936.967`, imports `980.369`, and total trade `1917.336` GBP billions for the three slicer labels.
- Executed the balance-state expression under BoP (SA)/Monthly filters. Returned rolling balance `-43.402` and state `0` (deficit).
- Ran the goods Top 10 aggregation under IMTS (NSA)/Monthly filters for April 2025 through March 2026. Returned, in order: United States `134.241`, Germany `110.7627`, China `87.691`, Netherlands `74.5885`, Switzerland `68.4459`, France `59.734`, Belgium `45.3662`, Ireland `42.752`, Canada `39.8162`, Spain `33.6854` GBP billions.
- Attempted the user-approved semantic-model field parameter addition. The XMLA context rejected writes as read-only; a follow-up query confirmed no model change was saved.

## Project checks

- The project uses a live, read-only connection to the confirmed semantic model.
- One page is defined at 1920 x 1080. The page is filtered to `Monthly`; headline visuals use `BoP (SA)`, while the partner ranking uses `IMTS (NSA)`.
- The report uses native card, slicer, line-chart, and clustered-bar-chart visuals. The partner visual is configured as a descending Top 10 ranking.
- The headline color-state measure uses the rolling balance sign. Its fill uses the report theme palette; no color hex values are set in visual formatting.
- `jq empty` parsed every generated PBIP/PBIR JSON file successfully.
- Project-wide VS Code diagnostics returned no errors; seven native visual definition files were found.
- A native Power BI screenshot was not captured in this macOS environment. Power BI Desktop is required to render and verify the PBIP, and Microsoft documents the Desktop workflow for Windows.

## Remaining verification

- Open the PBIP in a current Power BI Desktop release and confirm the report loads, the `Headline Trend` report measure is accepted, the card switches theme color, and the selector changes the monthly headline series.
- Screenshot capture and Power BI Desktop validation remain pending because Desktop is unavailable in this environment.
