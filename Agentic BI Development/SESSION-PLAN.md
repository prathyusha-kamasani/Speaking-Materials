# Agentic BI Development, 60 minute session plan

Status: plan agreed 2026-09-15. Offline demo spine rehearsed and green on Prathy's machine.

**Demo from these two repos, never from the production ones:**
- `PowerHour/agentic-bi-demo` — the report automation tool. 1818 tests pass, offline pipeline GREEN.
- `PowerHour/agentic-bi-demo-model` — the semantic model tool. 215 tests pass offline.

Both are private local extracts with client work removed and client names scrubbed. They are two
repos on purpose: Act 1's claim is "same recipe, different tool", and that needs two.

Upstream (do not demo from these, they contain client engagements):
- `/Volumes/Data Alchemy/ReportAutomationAgent`
- `/Volumes/Data Alchemy/GitHub/PowerHour/semantic-model-agent`

Fixes made in a demo repo must be ported back upstream by hand. Each demo repo's `JOURNAL.md`
records what is outstanding.

---

## 1. The spine

Two processes, in order. Everything in the session hangs off these.

**Process 1, build the tool.** Create skills, create scripts, create process, create gates. What you get is a tool that runs agentic loops with human intervention and produces a consistent deliverable, with tests and validation attached.

**Process 2, deliver a project.** Gather requirements. The tool reads them, uses what you built, and produces the deliverable. You are the operator: you answer when it asks.

The talk is not "look what AI can build". It is "here is the scaffolding that makes agent output trustworthy, and here is what happens when you run a real project through it".

---

## 2. Abstract, one change needed

The published abstract says the agent will "model the dimensions, wire up the relationships, write the DAX, and generate the PBIP files".

**Relationships, DAX and PBIP are real and demoable.** Creating tables and columns from raw files is not: `ALG-SEMANTIC-MODEL` is `status: draft`, `version: 0.1`, `writes: []`, and UK Trade's tables were built outside the agent.

**Agreed demo framing:** start from flat imported tables with no relationships. The agent profiles the model, reports the isolated tables and the missing date dimension, proposes the star, Prathy approves as operator, and `add_relationship.py` wires the joins. From the audience's seat this is "raw data in, dimensional model out". No ingestion step, no reopening of the data engineering scope lock.

Abstract wording to adjust: replace "model the dimensions" with the profile-and-propose framing. Everything else stands.

---

## 3. Minute by minute

| Time | Beat | On screen |
|---|---|---|
| 0-4 | Agent output that looks right and is not. Set the question: what would you have to check? | slides |
| 4-9 | **"Why not just use the Fabric skills?"** Conceded early, answered with the four words from `STATE.md`: opt-in, advisory, tool-specific, runtime-bypassable. | slides |
| 9-30 | **Process 1, build the tool**: skills, scripts, process, gates. Then the gate that refuses a build, and the loop that cannot advance itself. | repo + terminal |
| 30-50 | **Process 2, deliver a project**: requirements in, the model contract, one command to build and gate, the operator's queue, and the mistake every check passed. | terminal + 2 recordings |
| 50-55 | **The same brief through Microsoft's skills**, scored by the same gates. | scorecard |
| 55-60 | What to check before you trust it. Where you stay in the loop. | slides |

> `DEMO-SCRIPT.md` is authoritative for timings, commands and talking points. This table is the shape.

Microsoft now ships Fabric Skills for Copilot, Claude and the CLI, including report authoring from a
description or a screenshot. That question gets conceded at minute 4 and answered with evidence at
minute 50. Method in `COMPARISON-PLAN.md`.

---

## 4. Demos

### Demo A, the gate refuses (Act 1, live, offline)
`check_phase_order.py` blocking a build because the wireframe is not stamped APPROVED.
Point: the human gate is code, not a promise.
**Status: not yet rehearsed.** Needs a throwaway config with the stamp removed.
Fallback: `pre-commit run --all-files`, showing the 30+ named hooks, each enforcing one principle.

### Demo B, flat tables to a wired star (Act 2, recorded)
1. `cache_model_schema.py` snapshots the model
2. `profile_model.py` raises `isolated-table`, `no-date-dimension`, `no-measures`
3. Operator reads the proposal and approves
4. `add_relationship.py` writes the join, additive and idempotent, stable uuid5 ids
5. `apply_model_requests.py` lands the measures, `MODEL_CHANGELOG.md` gets the entry

Point: the agent proposes, the operator decides, the tool records what happened.
**Needs Fabric auth, so record it.** Build the flat-table starting state first.

### Demo C, one command, the whole build (Act 2, live, offline)
```
python3 scripts/run_pipeline.py clients/uk-trade-data/3-Develop/reports/the-balance.yaml --until gates
```
**Rehearsed 2026-09-15, overall GREEN.** Five stages pass: mockup-sync, mockup-capture, phase-order, build, gates. Nine advisory warnings. Writes `result.json` with per-stage status and the routed fix home.

Best advisory to read out loud, because it is the whole talk in one line:

> `R-SURVIVES-REFRESH`: `_Card Balance` is painted a fixed colour, so the colour cannot flip when the sign flips on refresh. A deficit keeps the surplus colour.

The report is correct today and wrong after the next refresh. No human eyeballing a screenshot catches that. A gate does.

Also worth showing: `ship-with-caveats (2.69/3)`. The tool grades its own output and does not pretend.

Runs with system Python 3.13, no venv, no auth, no network.

### Demo D, the mistake (Act 2, recorded)
**G-05 / BUG-02-001.** The field-parameter slicer rendered, accepted selections, and drove nothing. `universal.py` emitted no field-parameter `queryRoles`, so the chart stayed bound to one fixed measure.

Gates passed. DAX passed. Render-match passed. It was only caught by a human driving the slicer in the Service.

Point, and the closing line of the session: automated checks catch what they were written to catch. The interaction layer is still yours.

Backup mistake: **G-02b**, a guessed OKViz GUID that rendered blank cards. Fix was capture the real shape, never guess.

---

## 5. Still to build

0. **The comparison** (`COMPARISON-PLAN.md`): brief, setup, 3-5 Microsoft skills runs, scorecard.
   Do this FIRST. It answers the question the room will definitely ask.
1. Flat-table starting state for Demo B, on an open dataset
2. Rehearse and record Demo B end to end
3. Rehearse Demo A, throwaway config with the APPROVED stamp removed
4. Record Demo D from the existing UK Trade 02 deployment
5. Slides. Structure only, the repo and terminal carry the evidence
6. Abstract wording update, then re-save to Notion

---

## 6. Risks

| Risk | Mitigation |
|---|---|
| Conference wifi, Fabric auth | Only Demo C is live. B and D are recorded |
| 60 minutes is tight with four demos | A and C are under 3 minutes each. B and D are recorded and cut to length |
| Advisory wall is dense on a projector | Pre-zoom the terminal, read one rule aloud, do not scroll |
| Repo is mid-flight, 73 uncommitted files | Demo from a tagged commit, not the working tree |

---

## 7. Confidentiality

The two client engagements that exist in the upstream repo must not appear in any slide, screenshot, terminal scrollback, file listing or recording. They were removed from the demo repos entirely and their names scrubbed from engine comments, knowledge references, docs and test fixtures, so demoing from `agentic-bi-demo` rather than upstream is what enforces this. The demo engagement is `uk-trade-data` (open ONS data).

---

## 8. Where the claims come from

| Claim | Evidence |
|---|---|
| Skills, scripts, process, gates all exist | `.claude/skills/`, `scripts/`, `algorithms/ALG-*.md`, `.pre-commit-config.yaml` |
| The loop cannot self-advance | `ALG-PIPELINE.md`, `test_no_autoadvance_without_signoff` |
| Dev never closes its own bug | `clients/uk-trade-data/4-Governance/BUGS.md` |
| Owner approval is recorded | `approve_ship.py`, `STATE.md` ship-approval entry with actor and digest |
| The model contract is status typed | `model_requests.yaml`, `check_model_requests.py`, WP-12 |
| Measures really landed | `04-deliver/MODEL_CHANGELOG.md`, 6 measures, 2026-07-05 |
| Profiler finds the missing joins | `engine/profile/profiler.py`, `add_relationship.py` docstring |
| Offline pipeline is green | Run `r-20260915-132406-61255`, this machine, 2026-09-15 |
| The mistake is real | `ENGINE-GAPS.md` G-05, `BUGS.md` BUG-02-001 |
