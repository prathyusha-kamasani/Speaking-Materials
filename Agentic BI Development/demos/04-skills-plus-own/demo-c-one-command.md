# Demo C: one command, the whole build (44 to 48, live, offline)

**What you show:** one command runs five stages and still has things to say. One advisory is the whole talk.
**Point:** the report is right today and wrong after the next refresh. No one catches that by looking.
**Verified 2026-10-10** on `client/uk-trade-data/task/contrast-accept`: GREEN, twice in a row (13 advisories, 2.62/3).

## Run, in tab 1
```bash
python3 scripts/run_pipeline.py clients/uk-trade-data/3-Develop/reports/the-balance.yaml --until gates
```
**On screen, in order:** `mockup-sync`, `mockup-capture`, `phase-order`, `build`, `gates`, all green; then
`13 advisory warning(s)`; then `ship-with-caveats (2.62/3)`. Takes about a minute. Offline, no auth.

## The one to read aloud
Zoom in on `R-SURVIVES-REFRESH`: the tiles `detail_kpis` and `tt_kpis` paint `_Card Balance` a fixed `#C25A3C`, so
the colour cannot flip when the balance does.

## Say
- Five stages, one command. It passed, and it still has thirteen things to tell me.
- This is the one I would put on a poster. Today the card is the deficit colour and the number is negative: fine.
  After the next refresh, if the balance turns positive, the card is still the deficit colour.
- No one catches that from a screenshot. A gate catches it because someone wrote down what "survives a refresh"
  means.
- The hero card on this page DOES flip, because it uses a colour measure. These two tiles cannot yet: that is a
  known gap (`ENGINE-GAPS.md` G-07), tracked, not worked around.
- And the tool grades itself: ship with caveats, 2.62 out of 3. It does not say it is finished.

## Do not
Run it more than once before going on stage without reading the next section. Do not scroll the advisory wall:
pre-zoom, read one line, move on.

## Why this was red on 2026-10-08 (and the fix)
`check_ux_validation` reads the previous run's advisories. `R-TEXT-CONTRAST` (three faint greys at 3.03:1 and the
clay chip at 4.36:1) was firing with no line in `UX-VALIDATION.md`, so main was green on the first run and red
afterwards. Use branch `client/uk-trade-data/task/contrast-accept`: one accepted line, GREEN twice in a row. The
alternative (darkening the greys in the mockup) was tried and abandoned: it reopens the design sign-off, and
re-stamping it pulls the page into the full rail. See `../00-setup/README.md`.

## Also available
`python3 scripts/mission_control.py next` prints each report's next action with the literal command. Cut first if
short on time.
