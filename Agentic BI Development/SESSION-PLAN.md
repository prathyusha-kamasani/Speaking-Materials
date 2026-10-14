# Agentic BI Development, 60 minute session plan

Status: restructured 2026-10-08 (concepts first, then a ladder of four examples on one brief).
Supersedes the 2026-09-15 plan. Offline demo spine rehearsed and green on Prathy's machine.

**Demo from these two repos, never from the production ones:**
- `agentic-bi-demo`, the report automation tool. Offline pipeline GREEN.
- `agentic-bi-demo-model`, the semantic model tool.

Both are private local extracts with client work removed and client names scrubbed. They are two
repos on purpose: Example 4's claim is "same recipe, different tool", and that needs two.

Upstream (do not demo from these, they contain client engagements):
- `/Volumes/Data Alchemy/ReportAutomationAgent`
- `/Volumes/Data Alchemy/GitHub/PowerHour/semantic-model-agent`

Fixes made in a demo repo must be ported back upstream by hand. Each demo repo's `JOURNAL.md`
records what is outstanding.

---

## 1. The claim

Agent output looks right and is not. The talk is not "look what AI can build". It is:

1. what BI development is, and which parts of it an agent can safely do;
2. the handful of concepts that turn a chat model into a worker you can trust;
3. the same brief run four ways, each rung adding grounding or control, and only the last adding both.

The refrain for the hour: **what would you have to check?**

---

## 2. The shared brief

One brief, used in all four examples so the pros and cons are comparable, not anecdotal.

**UK Trade, "the balance" report.** Open ONS data, so nothing confidential. In prose, verbatim in
every example: a one-page report on the UK trade balance (exports less imports) over time, a
headline balance card that must flip colour when the balance turns from surplus to deficit, a trend
by month, a breakdown by partner country or commodity, and a slicer to switch the measure.

Written once as `demos/BRIEF.md` (prose, not config) and pasted unchanged into Examples 1 to 3.
Example 4 gets the same requirement through the tool's own intake.

The brief is chosen because it contains the traps worth showing: the colour that cannot flip on
refresh (`R-SURVIVES-REFRESH`), a field-parameter slicer (G-05), and a model with no date dimension.

---

## 3. Minute by minute

| Min | Section | Content | Medium |
|---|---|---|---|
| 0-3 | Hook | Agent output that looks right and is not. Set the question. | slides |
| 3-8 | **What is BI development** | The lifecycle: discover, model, build, test, deploy, govern. Who does each step today, where the time goes. | slides |
| 8-12 | **What "agentic" means** | A model, plus tools, plus a loop, plus a human. It differs from chat in that it acts, observes the result and tries again. | slides |
| 12-16 | **Which bits agents can do** | One traffic-light table across the lifecycle (section 4). | slides |
| 16-24 | **Key concepts** | `CLAUDE.md`, skills, hooks, loops, gates, MCP. One slide each, each tied to a BI step (section 5). | slides, quick repo glimpses |
| 24-30 | **Example 1: chat agent** | The brief into plain chat. | recording |
| 30-36 | **Example 2: Fabric skills** | The same brief through Microsoft's Fabric skills. | recording |
| 36-42 | **Example 3: MCP** | The same brief with an agent connected live to the model and workspace. | recording |
| 42-49 | **Example 4: Fabric skills + personal skills** | Our repo: skills, scripts, gates, human sign-offs. Demo A (the gate refuses) and Demo C (one command, GREEN) live. | repo + terminal |
| 49-56 | **Pros and cons, side by side** | The table (section 7) and the mistake every check passed (Demo D). | slides + recording |
| 56-60 | Close | What to check before you trust it. Where you stay in the loop. | slides |

Time is tight: each example is 6 to 7 minutes, so run them as recordings cut to length except Example 4.
Only Demo A and Demo C are live. A live agent run is the riskiest demo there is.

---

## 4. Which bits of BI development agents can do

| Step | Agent-ready? | Notes |
|---|---|---|
| Requirements, discovery | Amber | Agent drafts questions and structures answers. A human owns what the business actually needs. |
| Model profiling, relationships, date dimension | Green | Profile, propose, operator approves, tool writes (Demo B). Creating tables from raw files is NOT real yet (`ALG-SEMANTIC-MODEL` is draft, writes nothing). |
| Measures, DAX | Green | Verified against the real model. |
| Report layout and design | Amber | Agent proposes from a catalogue, a human decides and signs the mockup. |
| Building the report files (PBIP/PBIR) | Green | Deterministic engine, schema validated. |
| Testing: data, render | Green | Gates and scripts. |
| Testing: interaction (slicers, drill, tooltips) | Red | Still a person driving the Service. This is the closing line. |
| Deploy | Green, gated | Only by the blessed path, never by hand. |
| Governance, sign-off, acceptance | Red | The human decision, recorded with actor and digest. |

Abstract wording to adjust: replace "model the dimensions" with the profile-and-propose framing. Everything else stands.

---

## 5. Key concepts (one slide each, one BI example each)

| Concept | One line | BI example in the repo |
|---|---|---|
| `CLAUDE.md` / `AGENTS.md` | Standing instructions the agent reads every session. | The repo's rules: never name a client, fixes go in the engine, read the journal first. |
| Skills | A repeatable recipe the agent loads when the task matches. | `new-report`, `report-test-loop`, `render-fix-loop` in `.claude/skills/`. |
| Hooks | Things that run whether or not the agent remembers. | 28 named pre-commit hooks, each enforcing one principle. |
| Loops | Iterate until a check passes, not until the agent feels done. | The render-fix loop: compare mockup to the Service render, fix, repeat. |
| Gates | A step that refuses to advance without a pass or a human signature. | `check_phase_order.py` blocks a build with no APPROVED stamp. |
| MCP | Live, typed access to a tool or data source. | An agent reading the real model instead of guessing its column names. |

The hinge for the room: skills and `CLAUDE.md` are **advisory**, hooks and gates are **blocking**.

---

## 6. The four examples

Each example: setup (30 seconds), the brief goes in, what came out, what it got wrong, what we had to check.

### Example 1, chat agent
Paste the brief into a plain chat. It writes DAX and describes a layout.
- Shows: speed, and how good chat is at DAX and explaining.
- Trap: it guesses table and column names it cannot see. Nothing is checked, nothing is repeatable.

### Example 2, Fabric skills
Microsoft's Fabric Skills (including the Power BI report authoring skills) given the brief.
Set up per Microsoft's own docs, and note the version and date. Run it more than once to show run-to-run variation.
- Shows: grounded in real formats and APIs, a first draft far faster than building a tool.
- Trap: advisory and opt-in. Run the same brief five times and see what varies.
- Concede early where Microsoft wins: for a single measure, a prototype, or one report that is never rebuilt, this is the right answer.

### Example 3, MCP
An agent connected live to the model and workspace.
**To decide before rehearsal:** which MCP (Power BI modeling MCP or a Fabric MCP), what auth it needs on stage.
- Shows: ground truth. It reads the real model and can act on it.
- Trap: capability without process. It can write to the real thing with no gate in the way.

### Example 4, Fabric skills plus personal skills
The same recipe, our scaffolding. The brief goes in through intake.
- **Demo A (live, offline), the gate refuses:** `check_phase_order.py` blocks a build because the wireframe is not stamped APPROVED. The human gate is code, not a promise. *Needs a throwaway config with the stamp removed. Not yet rehearsed.* Fallback: `pre-commit run --all-files`.
- **Demo C (live, offline), one command, the whole build:**
  `python3 scripts/run_pipeline.py clients/uk-trade-data/3-Develop/reports/the-balance.yaml --until gates`
  Rehearsed 2026-09-15, overall GREEN, five stages, nine advisory warnings. Read out one advisory, because it is the whole talk in one line:
  > `R-SURVIVES-REFRESH`: `_Card Balance` is painted a fixed colour, so the colour cannot flip when the sign flips on refresh. A deficit keeps the surplus colour.
  Also show `ship-with-caveats (2.69/3)`: the tool grades its own output and does not pretend.
  Runs with system Python 3.13, no venv, no auth, no network.
- **Demo B (recorded), flat tables to a wired star:** `cache_model_schema.py`, `profile_model.py` (raises `isolated-table`, `no-date-dimension`, `no-measures`), operator approves, `add_relationship.py`, `apply_model_requests.py`, `MODEL_CHANGELOG.md` entry. Needs Fabric auth, so record it. Start from flat imported tables with no relationships; agreed framing is "raw data in, dimensional model out" with no ingestion step.
- Cost: upfront build, maintenance, and it only covers what you encoded. Say so.

### Demo D (recorded, in the side-by-side beat), the mistake
**G-05 / BUG-02-001.** The field-parameter slicer rendered, accepted selections, and drove nothing. `universal.py` emitted no field-parameter `queryRoles`. Gates passed, DAX passed, render-match passed. Only a human driving the slicer in the Service caught it.
Closing line: automated checks catch what they were written to catch. The interaction layer is still yours.
Backup mistake: **G-02b**, a guessed OKViz GUID that rendered blank cards. Fix was capture the real shape, never guess.

---

## 7. Pros and cons (draft, prove in rehearsal)

| | Pros | Cons |
|---|---|---|
| **Chat** | Zero setup. Fast for DAX, ideas, explanation. | Cannot see your model, so it guesses. Copy and paste everything. Nothing checked or repeatable. |
| **Fabric skills** | Microsoft-maintained, grounded in real APIs and formats. Quick start. | Generic. They advise but do not block, you opt in each time. No record of who approved what. |
| **MCP** | Live ground truth: reads the real model and can act on it. | Can write to the real thing with no gate. Capability without process. Needs auth and setup. |
| **Skills + personal skills** | Consistent, tested, gated output. Your standards enforced, with an audit trail. | Upfront cost. Maintenance. Covers only what you encoded. Overkill for one-off work. |

The ladder's message: each rung adds grounding or control, and only the last adds both.
The referee for all four is the same: the gates (`check_report`, preflight binding, advisory rules). They are reusable by anyone, including someone who only ever uses Copilot.

---

## 8. Still to build

Do 0 first: the recordings drive the rest.

0. **Examples 1 to 3 recordings** on `demos/BRIEF.md`: set up the Microsoft skills per their docs, record chat, Fabric skills and the MCP.
1. Decide Example 3's MCP, set it up, record a run of the same brief.
2. Record Example 1 (chat) on the same brief.
3. Flat-table starting state for Demo B, on the UK Trade open data. Rehearse and record end to end.
4. Rehearse Demo A (throwaway config with the APPROVED stamp removed).
5. Record Demo D from the existing UK Trade 02 deployment.
6. Slides. Concepts and structure only, the repo and terminal carry the evidence.
7. Abstract wording update, then re-save to Notion.

---

## 9. Risks

| Risk | Mitigation |
|---|---|
| Conference wifi, Fabric auth | Only Demo A and Demo C are live, both offline. Everything else recorded. |
| 60 minutes is tight: four examples plus concepts | Concepts are 24 minutes of slides, cap them. Each example 6 to 7 minutes, recorded and cut to length. |
| Reads as a hit piece on Microsoft | Concede the win early, publish the setup, let the gates speak. |
| One unlucky run misrepresents a tool | Record more than one run of Example 2, date it and give the version. Re-record near the date. |
| Advisory wall is dense on a projector | Pre-zoom the terminal, read one rule aloud, do not scroll. |
| Repo is mid-flight | Demo from a tagged commit, not the working tree. |

---

## 10. Confidentiality

The two client engagements that exist in the upstream repo must not appear in any slide, screenshot, terminal scrollback, file listing or recording. They were removed from the demo repos entirely and their names scrubbed, so demoing from `agentic-bi-demo` rather than upstream is what enforces this. The demo engagement is `uk-trade-data` (open ONS data). Check every recording for ids (tenant, subscription, workspace) before it goes on a slide.

---

## 11. Where the claims come from

| Claim | Evidence |
|---|---|
| Skills, scripts, process, gates all exist | `.claude/skills/`, `scripts/`, `algorithms/ALG-*.md`, `.pre-commit-config.yaml` |
| The loop cannot self-advance | `ALG-PIPELINE.md`, `test_no_autoadvance_without_signoff` |
| Dev never closes its own bug | `clients/uk-trade-data/4-Governance/BUGS.md` |
| Owner approval is recorded | `approve_ship.py`, `STATE.md` ship-approval entry with actor and digest |
| The model contract is status typed | `model_requests.yaml`, `check_model_requests.py`, WP-12 |
| Measures really landed | `04-deliver/MODEL_CHANGELOG.md`, 6 measures, 2026-07-05 |
| Profiler finds the missing joins | `engine/profile/profiler.py`, `add_relationship.py` docstring |
| Offline pipeline is green | Run `r-20260915-132406-61255`, this machine, 2026-09-15 (re-run before the session) |
| The mistake is real | `ENGINE-GAPS.md` G-05, `BUGS.md` BUG-02-001 |
| Advisory versus blocking | `STATE.md` 2026-07-15: a cold Copilot session shipped a bad report; knowledge was opt-in, advisory, tool-specific, runtime-bypassable |

> The deck is in `slides/`, the demos in `demos/`, reference material in `reference/`. The earlier plans
> (six-minute script, build path, comparison) are in `reference/archive/`.
