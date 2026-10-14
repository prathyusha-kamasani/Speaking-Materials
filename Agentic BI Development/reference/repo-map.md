# The two demo repos

Both are private, local extracts with client work removed and client names scrubbed. Demo from these, never
from the upstream repos. Fixes made in a demo repo must be ported back by hand (each `JOURNAL.md` says what is owed).

## `agentic-bi-demo`: builds reports

`engine/` (deterministic generator), `algorithms/` (the `ALG-*` specs), `bundle/` (visuals and layouts),
`scripts/` (pipeline, gates, Mission Control), `knowledge/`, `schemas/`, `tests/`, `.claude/skills/`,
`.pre-commit-config.yaml`, and the engagement `clients/uk-trade-data` (open ONS data).

Key entry points: `scripts/run_pipeline.py`, `scripts/check_phase_order.py`, `scripts/mission_control.py`.

## `agentic-bi-demo-model`: enriches and verifies semantic models

Same shape (`knowledge/`, `prompts/`, `scripts/`, `architecture/`). Works on descriptions, synonyms, renames and
Copilot readiness. Safety rule: it writes to a staging copy, you verify, then you promote; it never writes to
the live model. Key entry points: `cache_model_schema.py`, `profile_model.py`, `add_relationship.py`,
`apply_model_requests.py`, `verify_model.py`.

## Why two repos

The claim is "same recipe, different tool", and that is only demonstrable as two repos.
