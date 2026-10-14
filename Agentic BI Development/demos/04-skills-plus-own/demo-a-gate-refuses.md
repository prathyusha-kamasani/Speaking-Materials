# Demo A: the gate refuses (42 to 44, live, offline)

**What you show:** the same command on two reports. One is blocked by a human sign-off that is missing, one passes.
**Point:** human in the loop is code. A gate the loop cannot walk past, not a person watching.
**Verified 2026-10-08** on a clean checkout of main.

## Run, in tab 1
```bash
python3 scripts/check_phase_order.py --config clients/uk-trade-data/3-Develop/reports/what-we-trade.yaml
```
**On screen:** a red `✗ DESIGN: no sign-off`, naming `2-Design/wireframes/03-what-we-trade/APPROVED.md` as absent,
then `1 surface(s) not ready for Develop`.

```bash
python3 scripts/check_phase_order.py --config clients/uk-trade-data/3-Develop/reports/the-balance.yaml
```
**On screen:** `Discovery captured, Design signed off + current`. A grey `RAIL` advisory line also prints; read past it.

## Say
- Same command, two reports. One is blocked.
- The blocked one has no `APPROVED.md`: nobody has signed the design off. The agent cannot start building it.
  Not "should not". Cannot.
- That is what I mean by human in the loop.

## Optional extension (30 s)
Show what "current" means: the sign-off goes stale if the mockup is committed after it. That is the rule behind
the green line. (`sed -n 15,20p scripts/check_phase_order.py`)

## Risk and fallback
Disappears if `what-we-trade` is signed off before the session: both commands then pass. Fallback: point at any
unsigned surface, or run `pre-commit run --all-files` and read three hook names.
