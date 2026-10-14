I need a one-page Power BI report on the UK trade balance.

Who it is for
Executives who glance at it to see whether the UK is in surplus or deficit and which way it is moving,
and analysts who check where the numbers come from.

The data
Use the semantic model SM_UKT_Import in the Fabric workspace "UK Trade Data". Do not change the model.
- Headline figures and the trend: 'Trade Total Monthly'[Value GBP Millions]. Exports and imports are
  separate rows, split by Flow[Direction].
- These measures already exist, use them: [Total Exports (GBP bn)], [Total Imports (GBP bn)],
  [Trade Balance (GBP bn)].
- 'Date' is a reserved word in DAX, so always quote it.
- Never sum across Basis or Period Type. Filter to one basis (seasonally adjusted balance of payments)
  and one period type.
- The partner and commodity breakdown comes from 'Trade Goods Monthly', which is not seasonally adjusted.
  It will not add up to the headline, so show it as a separate ranking.

What to build
1. A headline balance card that changes colour when the balance turns from a surplus to a deficit.
2. A trend of exports, imports and the balance by month.
3. A breakdown by partner country or commodity.
4. A slicer that switches the trend between exports, imports and total trade.

Done means
- For the 12 months to March 2026: exports £937.0bn, imports £980.4bn, balance minus £43.4bn (a deficit).
- The card colour comes from a measure, so it still flips if the balance changes sign after a refresh.
- Changing the slicer changes the plotted measure.
- Every table, column and measure the report uses exists in the model.

Constraints
- One page, 1920 x 1080.
- Colours from the report theme, not typed into visuals.
- Native Power BI visuals only.

Out of scope
Drill-through, extra pages, services and FDI data, and any change to the model.

What to hand back
- The report as Power BI project (PBIP) files in one folder.
- A screenshot of the page.
- The checks you ran and what each one returned.

If a table, column or value you need is not in the model, ask me before you guess.
