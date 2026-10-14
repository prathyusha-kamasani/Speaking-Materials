# The shared brief: building the trade balance report

DRAFT, 2026-10-10. Paste the block below unchanged into the Fabric skills, MCP and my own setup examples.
Open ONS data, so nothing confidential. Structure follows Anthropic's guidance: context and the reason, the
specific data, what to build, what "done" means, constraints, out of scope, what to hand back, and ask
before guessing.

```
I need a one-page Power BI report on the UK trade balance.

Who it is for
Executives who glance at it to see whether the UK is in surplus or deficit and which way it is moving,
and analysts who check where the numbers come from.

The data
Use the semantic model SM_UKT_Import in the Fabric workspace "UK Trade Data Reports". Do not change the model.
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
```

## Where each line comes from

| Line | Source |
|---|---|
| Audience (executives and analysts) | `clients/uk-trade-data/1-Discovery/engagement.md`, "Audience & delivery" |
| Model, tables, columns, measures | `1-Discovery/model_schema/SM_UKT_Import-schema.md` |
| Never sum across Basis or Period Type; goods breakdown is not seasonally adjusted | `engagement.md`, "GOTCHAS" 1, 2 and 4 |
| Seasonally adjusted balance of payments basis | `2-Design/wireframes/01-the-balance/design-brief.md`, "Basis" |
| £937.0bn, £980.4bn, minus £43.4bn | `engagement.md`, "Validated ground-truth figures" (gov.uk UK Trade in Numbers) |
| 1920 x 1080 | `design-brief.md`, "Canvas" |

All paths are in `agentic-bi-demo`. The slicer line (exports, imports and total trade) is a choice for this
brief, not taken from a source.

## What changed from the first version

The first version was one paragraph: what to build, nothing else. The three "traps" (the colour that has to
flip, the slicer that has to drive the measure, exports and imports as rows) were hidden tests. They are now
stated as requirements and acceptance checks, so each tool is judged on a clear brief, not on guessing.

First version, for reference:

> Build a one-page Power BI report on the UK trade balance (exports less imports) over time.
> It needs a headline balance card that changes colour when the balance turns from a surplus to a deficit,
> a trend by month, a breakdown by partner country or commodity, and a slicer to switch the measure.
