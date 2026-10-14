# Before you walk on

```bash
lsof -ti :8199 | xargs kill          # kill strays from an earlier run
```

- **Tab 1:** `cd` into `agentic-bi-demo` on `main`. Example 4 lives here.
- **Tab 2:** `cd` into `agentic-bi-demo-model`, only if you show the same-recipe glimpse.
- **Tab 3:** `python3 scripts/mission_control.py serve` in `agentic-bi-demo`. The deck's Mission Control slide
  opens `http://127.0.0.1:8199/?client=uk-trade-data` (the `?client=` part matters: without it the page is empty).
- Font size up. `clear` every tab.

## Re-run these before the session (last verified 2026-10-14, on main)

| Command | Expected |
|---|---|
| `python3 scripts/check_phase_order.py --config clients/uk-trade-data/3-Develop/reports/what-we-trade.yaml` | blocks: `✗ DESIGN: no sign-off`, names the missing `APPROVED.md` |
| `python3 scripts/check_phase_order.py --config clients/uk-trade-data/3-Develop/reports/the-balance.yaml` | passes: `Discovery captured, Design signed off + current` |
| `python3 scripts/run_pipeline.py clients/uk-trade-data/3-Develop/reports/the-balance.yaml --until gates` | GREEN, 5 stages, advisories, `ship-with-caveats`. Green on a second run too |
| `python3 scripts/mission_control.py go-nogo --client uk-trade-data` | 07 Trade Stripes: GO FOR LAUNCH (needs PRs #58 and #59 merged) |
| `python3 -m pytest -q` | all pass (3,099 on 2026-10-14) |

Demo C writes run logs into the engagement folder (`operations.jsonl`, `AUDIT.md`, `decisions.json`). After a
rehearsal, `git checkout -- clients/ && git clean -fd clients/uk-trade-data/3-Develop/deliverables/uk-trade-the-balance/logs/`
puts the tree back.

## Two folders the model tool needs

`agentic-bi-demo-model` is set up for the Taylor Swift model. `agentic-bi-demo-model-ukt` is the same repo set up
for UK Trade (its `config/settings.yaml` is local only, never on GitHub). The report repo's
`clients/uk-trade-data/workspaces.yaml` points `model_tool` at the second one; without it, the rail's
model-alignment step fails and Mission Control shows page 07 as not done. Keep both.

## If Demo A stops blocking

If `what-we-trade` has been signed off since, Demo A passes both commands and the demo disappears. Fallback:
`pre-commit run --all-files`, or point at a different unsigned surface.

Port 8199 busy: `lsof -ti :8199 | xargs kill`, or `serve --port 8210` (then change the link on the slide).
Runs on system Python, no venv, no auth, no network.
