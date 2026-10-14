# Report Spec

## Report identity
- Report name: UK Trade Balance
- Semantic model: SM_UKT_DirectLake
- Audience: Executives (glance at balance/trend) and Analysts (data source verification)
- Primary purpose: Monitor UK trade balance status and trend
- Delivery target: Local PBIP first, then publish to Fabric workspace "UK Trade Data"

## Semantic model binding
- Entry mode: Live Connected Model
- Workspace name: UK Trade Data
- Workspace ID: c13c3b0f-908c-47e8-97a5-4b770a0df2c8
- Model name: SM_UKT_DirectLake
- Model ID: ffac1347-8ac8-4019-9dd7-6d38dc941df7
- connectionString: Data Source=powerbi://api.powerbi.com/v1.0/myorg/UK Trade Data;Initial Catalog=SM_UKT_DirectLake;Integrated Security=ClaimsToken

## User decisions and constraints
- Scope: One page, focused executive dashboard
- Page count: 1
- Interactivity: Bookmark navigator to switch trend view (Exports/Imports/Total Trade); no drillthrough
- Design direction: Professional executive with clear surplus/deficit signaling
- Publishing: PBIP files first, optional Fabric publish after validation
- Tooling: Power BI Desktop preview required
- Model edit permissions: None - do not change the model
- Accessibility: WCAG AA minimum contrast; alt text on all visuals
- Data caveats:
  - 'Trade Goods Monthly' breakdown won't match headline (different basis)
  - Filter to basis="BoP (SA)" and period_type="Monthly" for headline
  - 'Date' is reserved in DAX - always quote it

## Narrative
- Core story: Is the UK in trade surplus or deficit, and which direction is it moving?
- Audience promise: At a glance, see the balance, the trend, and the top partners/commodities
- Key questions answered:
  1. What is the current trade balance?
  2. Are exports/imports trending up or down?
  3. Who are the top trading partners?

## Design identity
- Tone: Executive Newsroom - clear headlines, decisive color signals, minimal decoration
- Signature: Conditional color on balance card (green surplus / red deficit) as the page hero signal
- Brownfield delta: N/A (greenfield report)

## Page plan
1. **UK Trade Balance**
   - Archetype: Executive Summary
   - Layout variant: B (KPI strip + trend hero + ranking breakdown)
   - Variant rationale: Balance metric is the headline; trend shows trajectory; breakdown shows detail
   - Purpose: Answer "surplus or deficit?" immediately, then show trend and drivers
   - Visuals:
     - Balance card (conditional color via `_Colour Balance` measure)
     - Exports card
     - Imports card
     - Line chart showing exports/imports/balance by month
     - Bar chart showing top partners OR commodities
     - Bookmark navigator slicer to switch trend view
   - Fields/measures:
     - `fact_trade_total_monthly[value_gbp_millions]`
     - `[Total Exports (GBP bn)]`, `[Total Imports (GBP bn)]`, `[Trade Balance (GBP bn)]`
     - `[_Colour Balance]` for card conditional formatting
     - `dim_date[date]` or `dim_date[year_month]` for trend axis
     - `dim_country[country_name]` for partner breakdown
     - `dim_commodity[sitc1_description]` for commodity breakdown (alternative)
   - Slicers/interactions:
     - Bookmark navigator to switch between Exports/Imports/Total Trade trend view
   - Filters (page-level, hidden):
     - `dim_basis[basis_name] = "BoP (SA)"`
     - `dim_period_type[period_type_name] = "Monthly"`

## Design system summary
- Theme name: UK Trade Theme (based on base.json)
- Color semantics:
  - Trade Balance positive (surplus): Green (#107C10)
  - Trade Balance negative (deficit): Red (#D13438)
  - Exports: Blue (#0078D4)
  - Imports: Orange (#FF8C00)
- Typography: Segoe UI (display + body)
- Layout: 12x12 grid, 32px margin, 24px gutter, 8px snap
- Accessibility: WCAG AA contrast; alt text on all data visuals

## Model requirements
- Existing measures (use as-is):
  - `[Total Exports (GBP bn)]`
  - `[Total Imports (GBP bn)]`
  - `[Trade Balance (GBP bn)]`
  - `[Total Trade (GBP bn)]`
  - `[_Colour Balance]`
- New measures: None (model changes out of scope)
- New calculated columns: None
- Relationship/sort requirements: None (existing relationships sufficient)

## Canonical design contract

```yaml
Design Brief:
  generated_by: powerbi-report-cli
  contract_version: 1
  mode: greenfield
  design_identity:
    tone: Executive Newsroom
    signature: Conditional color balance card as decisive surplus/deficit signal
  archetype: Executive Summary
  navigation_model: bookmark_navigator
  color_map:
    - measure: fact_trade_total_monthly[Trade Balance (GBP bn)]
      color: "#107C10"  # Surplus green (will flip to red via conditional formatting)
      tint: "#DFF6DD"
    - measure: fact_trade_total_monthly[Total Exports (GBP bn)]
      color: "#0078D4"
      tint: "#DEECF9"
    - measure: fact_trade_total_monthly[Total Imports (GBP bn)]
      color: "#FF8C00"
      tint: "#FFF4CE"
  pages:
    - name: UK Trade Balance
      role: landing
      archetype: Executive Summary
      layout_variant: B
      variant_rationale: Balance card as decisive headline; trend proves trajectory; breakdown shows drivers
      navigation:
        - element: bookmark_navigator
          action: Bookmark
          label: View Selector
      page_background: "#F3F2F1"
      layout_summary: "KPI strip at top with balance hero card flanked by exports/imports; trend chart below; partner breakdown at bottom; bookmark navigator in filters region"
      layout_contract:
        canvas:
          width: 1920
          height: 1080
          margin: 32
          gutter: 24
          snap: 8
        grid:
          columns: 12
          rows: 12
          regions:
            header:    [1,  1,  9,  2]
            filters:   [9,  1, 13,  2]
            kpis:      [1,  2, 13,  4]
            trend:     [1,  4, 13,  9]
            breakdown: [1,  9, 13, 13]
        placements:
          - id: page_title
            region: header
            kind: textbox
            text: "UK Trade Balance"
            purpose: "State the report subject"
          - id: view_selector
            region: filters
            kind: slicer
            field_bindings: Bookmarks
            slicer_type: bookmark_navigator
            purpose: "Switch between Exports, Imports, and Total Trade trend views"
          - id: balance_card
            region: kpis
            kind: cardVisual
            purpose: "What is the current trade balance?"
            field_bindings: fact_trade_total_monthly[Trade Balance (GBP bn)]
            color_strategy: semantic
            conditional_format:
              field: fact_trade_total_monthly[_Colour Balance]
              rules:
                - condition: "value >= 0"
                  background: "#107C10"
                - condition: "value < 0"
                  background: "#D13438"
            slot: 1
            of: 3
          - id: exports_card
            region: kpis
            kind: cardVisual
            purpose: "What are total exports?"
            field_bindings: fact_trade_total_monthly[Total Exports (GBP bn)]
            color_strategy: measure_match
            slot: 2
            of: 3
          - id: imports_card
            region: kpis
            kind: cardVisual
            purpose: "What are total imports?"
            field_bindings: fact_trade_total_monthly[Total Imports (GBP bn)]
            color_strategy: measure_match
            slot: 3
            of: 3
          - id: trend_chart
            region: trend
            kind: lineChart
            purpose: "How are exports, imports, and balance trending over time?"
            field_bindings:
              Category: dim_date[date]
              Y:
                - fact_trade_total_monthly[Total Exports (GBP bn)]
                - fact_trade_total_monthly[Total Imports (GBP bn)]
                - fact_trade_total_monthly[Trade Balance (GBP bn)]
            color_strategy: measure_match
            sort_policy: category_asc
          - id: partner_breakdown
            region: breakdown
            kind: barChart
            purpose: "Which partner countries drive the most trade?"
            field_bindings:
              Category: dim_country[country_name]
              Y: fact_trade_goods_monthly[value_gbp]
            sort_policy: value_desc
            color_strategy: gradient
            top_n: 10
        space_audit:
          content_cell_count: 132
          placed_cell_count: 132
          empty_cell_pct: 0
          unplaced_regions: []
          largest_region:
            name: trend
            pct_of_content: 45
          balance_rationale: "Trend chart is the hero showing trajectory over time; KPI strip provides immediate balance answer; breakdown shows drivers. No wasted space."
  interaction_pattern:
    drill_targets: []
    cross_filter_rules: "Filter from breakdown to trend; Highlight on cards"
  accessibility:
    alt_text_strategy: headline+trend
    contrast_notes: "Surplus green and deficit red both pass WCAG AA on white background"
  theme:
    base: "references/design/assets/base.json adapted"
    user_overrides: "None - greenfield"
  bookmarks:
    - name: Show Exports
      description: "Filter trend chart to show only exports measure"
      visual_state:
        trend_chart:
          visible_measures: [fact_trade_total_monthly[Total Exports (GBP bn)]]
    - name: Show Imports
      description: "Filter trend chart to show only imports measure"
      visual_state:
        trend_chart:
          visible_measures: [fact_trade_total_monthly[Total Imports (GBP bn)]]
    - name: Show Total Trade
      description: "Filter trend chart to show total trade measure"
      visual_state:
        trend_chart:
          visible_measures: [fact_trade_total_monthly[Total Trade (GBP bn)]]
    - name: Show All
      description: "Default view showing exports, imports, and balance"
      visual_state:
        trend_chart:
          visible_measures:
            - fact_trade_total_monthly[Total Exports (GBP bn)]
            - fact_trade_total_monthly[Total Imports (GBP bn)]
            - fact_trade_total_monthly[Trade Balance (GBP bn)]
  page_filters:
    - table: dim_basis
      column: basis_name
      operator: equals
      value: "BoP (SA)"
    - table: dim_period_type
      column: period_type_name
      operator: equals
      value: "Monthly"
```

## Implementation notes

- Model changes: None required (out of scope per brief)
- PBIR/report authoring:
  1. Scaffold PBIP structure with byConnection binding to SM_UKT_DirectLake
  2. Create report theme with surplus/deficit color semantics
  3. Build page with layout contract geometry
  4. Configure conditional formatting on balance card using `_Colour Balance` measure
  5. Create bookmarks for view switching
  6. Add bookmark navigator slicer
  7. Apply page-level filters for BoP (SA) and Monthly
- Validation:
  - Verify 12 months to March 2026: exports £937.0bn, imports £980.4bn, balance -£43.4bn
  - Verify card color flips when balance changes sign
  - Verify bookmark navigator switches the trend view
- Desktop screenshot verification: Required before publishing
- Publishing boundary: Local PBIP first; Fabric publish only after validation passes
- Risks:
  - Bookmark-based measure switching is less elegant than field parameter (but respects "no model changes" constraint)
  - Partner breakdown from Trade Goods Monthly won't match headline totals (different basis) - this is expected per brief
