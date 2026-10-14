# Where the claims come from

| Claim | Evidence |
|---|---|
| Skills, scripts, process and gates all exist | `.claude/skills/`, `scripts/`, `algorithms/ALG-*.md`, `.pre-commit-config.yaml` |
| The loop cannot self-advance | `algorithms/ALG-PIPELINE.md`, `test_no_autoadvance_without_signoff` |
| The developer never closes their own bug | `clients/uk-trade-data/4-Governance/BUGS.md` |
| Owner approval is recorded | `scripts/approve_ship.py`; `STATE.md` ship-approval entry with actor and digest |
| The model contract is status-typed | `model_requests.yaml`, `scripts/check_model_requests.py` |
| Measures really landed | `MODEL_CHANGELOG.md` entries |
| The profiler finds the missing joins | `engine/profile/profiler.py`; `add_relationship.py` docstring |
| The offline pipeline is green | Run on 2026-09-15, re-run before the session |
| The mistake is real | `ENGINE-GAPS.md` G-05; `BUGS.md` BUG-02-001 |
| Advisory versus blocking | `STATE.md` 2026-07-15 (production repo): a cold Copilot session shipped a bad report |

All paths are in `agentic-bi-demo` unless noted. Counts (tests, hooks, advisories) change: re-run before quoting.
