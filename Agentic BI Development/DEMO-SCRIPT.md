# Demo script: Agentic BI Development, 60 minutes

Restructured 2026-10-08 to match `SESSION-PLAN.md`: concepts first, then four examples on one brief.

**Status of the commands.** Those marked VERIFIED were run on Prathy's machine on 2026-09-15 and produced
the output described. The rest is not yet run or recorded and is marked TO RECORD or TO DECIDE. Test
counts and the pipeline run predate the Taylor Swift and engine work since, so re-run everything in
"Verified" before the session and update the numbers.

Talking points are prompts, not a script. Say them your way.

---

## Pre-flight brief

**Audience.** Fabric and Power BI practitioners, mixed seniority, who have tried Copilot or an AI
agent and were either burned or unconvinced. They read DAX. They do not run agent pipelines.

**Outcome.** They leave able to say what part of BI development an agent can do, name the concepts
that make an agent trustworthy (instructions, skills, hooks, loops, gates, MCP), choose between four
ways of working with an agent, and name the checks that catch an agent being confidently wrong.

**Format.** 60 minutes. Concepts (slides, with short repo glimpses), then four examples on ONE brief,
then the side-by-side. Terminal carries the evidence in Example 4, slides carry structure.

**The brief (verbatim in Examples 1 to 3).** UK Trade, "the balance": a one-page report on the UK
trade balance (exports less imports) over time, a headline balance card that flips colour when the
balance turns from surplus to deficit, a trend by month, a breakdown by partner country or commodity,
and a slicer to switch the measure. Lives in `demos/BRIEF.md`.

**Assumptions.** Demo from `agentic-bi-demo` and `agentic-bi-demo-model`, never the production repos.
Everything live is offline: system Python, no venv, no Fabric auth, no network. Everything that needs
the Service, or a live agent run, is pre-recorded.

**Exclusions.** No data engineering or pipelines. No client names anywhere, in any file, terminal
scrollback, or recording. No tenant, subscription or workspace ids on screen.

---

## Setup, before you walk on

```bash
lsof -ti :8199 | xargs kill          # kill strays from an earlier run
```

- **Tab 1:** `cd .../agentic-bi-demo`, the report tool. Example 4 lives here.
- **Tab 2:** `cd .../agentic-bi-demo-model`, the model tool. Only if you show the same-recipe glimpse.
- **Tab 3:** `python3 scripts/mission_control.py serve` running, browser open on `127.0.0.1:8199`
  (only needed if you show the operator's queue).
- Recordings for Examples 1, 2, 3 and Demos B, D queued and checked for ids.
- Font size up. `clear` every tab. Demo from a tagged commit, not the working tree.

A stale server on 8199 is the most likely thing to bite you. Kill it first, every time.

---

# PART 1 · Concepts (0 to 24)

## 0 to 3 · The hook

Slides.

**Say**
- An agent will write you a semantic model and a report, and it will look right.
- The DAX runs. The visuals render. Nothing errors.
- Looking right and being right are different things, and you cannot tell them apart by looking.
- So the question for the hour is not "can AI build this". It is "what would you have to check before
  you trusted it".

## 3 to 8 · What is BI development

Slides. One picture: the lifecycle, discover, model, build, test, deploy, govern.

**Say**
- Before agents, who does each step, and where does the time actually go.
- [Fill in from Prathy's own experience: where the hours go in a real engagement.]
- Note that most BI delivery time is not building the visual. It is requirements, model fixes, testing,
  rework after feedback, and sign-off.

## 8 to 12 · What "agentic" means

Slides.

**Say**
- Chat: you ask, it answers, you copy and paste.
- Agentic: a model, plus tools, plus a loop, plus a human. It acts, looks at what happened, and tries
  again.
- That loop is the power and the risk. It can fix its own errors. It can also confidently build on its
  own mistake.

## 12 to 16 · Which bits of BI development agents can do

Slides. The traffic-light table from `SESSION-PLAN.md` section 4.

**Say**
- Green: profiling a model, relationships, measures, building report files, data and render tests.
- Amber: requirements and layout. The agent drafts, a human decides.
- Red: interaction testing, and sign-off. Those stay with a person.
- One honest caveat for the abstract: it can propose and wire a star schema from imported tables, but
  creating tables from raw files is not something this tool does. Do not imply it.

## 16 to 24 · Key concepts

Slides, one per concept, each with a 20 to 30 second repo glimpse where it exists. Do not linger: the
examples are where these come alive.

| Concept | Slide line | Glimpse (VERIFIED unless noted) |
|---|---|---|
| `CLAUDE.md` / `AGENTS.md` | Standing instructions the agent reads every session. | Show the top of `AGENTS.md`. TO CHECK: read it first and pick lines with no client names. Do not show the top of `CLAUDE.md` on screen: it carries the extract banner. |
| Skills | A repeatable recipe loaded when the task matches. | `ls .claude/skills` |
| Hooks | Run whether or not the agent remembers. | `grep -c "id:" .pre-commit-config.yaml` (28 named hooks, each enforcing one principle) |
| Loops | Iterate until a check passes, not until the agent feels done. | `grep -n "autoadvance\|await developer sign-off" algorithms/ALG-PIPELINE.md` |
| Gates | A step that refuses to advance without a pass or a human signature. | Name only here. Shown live in Example 4. |
| MCP | Live, typed access to a tool or data source. | Name only here. Shown in Example 3. |

**Say**
- Skills and `CLAUDE.md` are advisory. The agent can ignore them. Hooks and gates are blocking. It
  cannot.
- That is the hinge for everything that follows: each example sits at a different point on advisory
  versus blocking, and on blind versus grounded.
- Process is a spec, not a prompt: every behaviour here is a versioned `ALG-*` spec with inputs, a
  gate, a sign-off and invariants, and an invariant has a test name next to it.
  (`head -30 algorithms/ALG-DISCOVERY.md` if you want to show one. VERIFIED.)
- One rule worth stealing: in the QA loop the developer never closes their own bug.

---

# PART 2 · One brief, four ways (24 to 49)

Same brief every time. For each example use the same four beats: **setup, brief in, what came out,
what we had to check.** Close each with one pro and one con, keyed to the table in the plan. Do not
declare a winner until minute 49.

## 24 to 30 · Example 1: chat agent

RECORDED. TO RECORD.

**Setup (30 s).** A plain chat. No tools, no access to the model.

**Do.** Paste `demos/BRIEF.md` unchanged.

**Look for on screen**
- Good DAX and a sensible layout description.
- Table and column names it could not know and guessed. Name the guesses out loud.

**Say**
- This is where most people start, and for a single measure it is genuinely the right tool.
- It cannot see your model, so every name is a guess. You copy and paste. Nothing is checked, and you
  cannot repeat it tomorrow and expect the same answer.

**Pro / con.** Zero setup and fast, against blind and unrepeatable.

## 30 to 36 · Example 2: Fabric skills

RECORDED. TO RECORD.

**Setup (30 s).** Microsoft's Fabric Skills, installed per Microsoft's own documentation. Show the
version and date on screen.

**Do.** Same brief, verbatim.

**Look for on screen**
- It is grounded in real formats and APIs. A first draft far faster than anything you build.
- Run-to-run variation, if you recorded more than one run: show two side by side.

**Say**
- Microsoft's skills are good. Concede it, loudly. For a prototype, a single measure, one report you
  will never rebuild, this is the right answer.
- What I want you to notice is not quality, it is that it is advisory and opt-in. Run it twice and
  you may get two different reports, and nothing tells you which is right.
- The four words: opt-in, advisory, tool-specific, runtime-bypassable. A cold Copilot session with all
  my knowledge files present shipped a bad report and deployed it by the wrong path
  (`STATE.md` 2026-07-15).

**Pro / con.** Grounded and fast, against advisory, generic and no record of who approved what.

## 36 to 42 · Example 3: MCP

RECORDED. TO DECIDE which MCP (the Power BI modeling MCP or a Fabric MCP), and what auth it needs.
TO RECORD once chosen. Check that no tenant or workspace id appears in the recording.

**Setup (30 s).** An agent connected live to the model and the workspace.

**Do.** Same brief, verbatim.

**Look for on screen**
- It reads the real model: actual table names, actual measures, real relationships.
- Ask it something the chat agent had to guess, and show it answering correctly from the live model.

**Say**
- This is the missing ground truth. Example 1 guessed names. This one looks them up.
- But look at what has changed: it can now write to the real thing. There is no staging copy, no
  approval, no record of why. That is capability without process.
- [Fill in once recorded: the specific thing it got right and the specific thing nothing stopped.]

**Pro / con.** Live ground truth, against capability with no gate in the way, and setup and auth.

## 42 to 49 · Example 4: Fabric skills plus personal skills

LIVE, offline. Back to **Tab 1**. This is the one example you do live, because it is the one that runs
offline. Three beats: the gate refuses, the one-command build, and (recorded) the model half.

### 4.1 · The gate refuses (42 to 44) · Demo A

```bash
python3 scripts/check_phase_order.py --config clients/uk-trade-data/3-Develop/reports/what-we-trade.yaml
```
**On screen**
```
✗ DESIGN: no sign-off — 2-Design/wireframes/03-what-we-trade/APPROVED.md absent.
  Finish Design (mockup · brief · wireframe · UX validation) and stamp the wireframe APPROVED
check_phase_order: 1 surface(s) not ready for Develop
```

```bash
python3 scripts/check_phase_order.py --config clients/uk-trade-data/3-Develop/reports/the-balance.yaml
```
**On screen**
```
check_phase_order: 1 surface(s) — Discovery captured, Design signed off + current
```

**Say**
- Same command, two reports. One is blocked, one is clear.
- The blocked one has no `APPROVED.md`: a human has not signed off the design. The agent cannot start
  building it. Not "should not". Cannot.
- That is human in the loop. Not a person watching. A gate the loop cannot walk past.

> Note: the 2026-09-15 session plan said Demo A needed a throwaway config with the stamp removed. This
> command pair already shows a real blocked report (`what-we-trade`) beside a clear one, so no
> throwaway is needed. Re-run both before the session: if `what-we-trade` has been signed off since,
> the first command will pass and the demo disappears. Fallback: `pre-commit run --all-files`.

### 4.2 · One command, the whole build (44 to 48) · Demo C

```bash
python3 scripts/run_pipeline.py clients/uk-trade-data/3-Develop/reports/the-balance.yaml --until gates
```

**On screen** Five stages green, then nine advisories, then `ship-with-caveats (2.69/3)`.
Re-run beforehand: the counts may have moved.

Zoom in and read this one out:

```
R-SURVIVES-REFRESH: '_Card Balance' is painted a fixed #C25A3C — the colour cannot flip
when the sign flips on refresh (a deficit keeps the surplus colour).
```

**Say**
- One command: sync, capture, phase order, build, gates. It passed, and it still has nine things to
  tell me.
- This is the one I would put on a poster. The report is correct today. After the next refresh, when
  that number goes negative, the colour stays the colour of a surplus.
- This is the trap in the brief: "a balance card that flips colour". Every other example would pass it
  on a screenshot.
- Nobody catches that by looking. A gate catches it because someone wrote down what "survives a
  refresh" means.
- And the tool grades itself: ship with caveats, 2.69 out of 3. It does not tell me it is finished.

Pre-zoom the terminal. Read one rule aloud. Do not scroll the advisory wall.

### 4.3 · The model half, same recipe (48 to 49) · Demo B

RECORDED, 60 to 90 seconds, or skip if running short. TO RECORD. Needs Fabric auth.

1. `cache_model_schema.py` takes a snapshot
2. `profile_model.py` reports `isolated-table`, `no-date-dimension`, `no-measures`
3. the agent proposes the joins, **you approve**
4. `add_relationship.py` writes them, idempotent, stable ids
5. `apply_model_requests.py` lands the measures and appends `MODEL_CHANGELOG.md`

**Say over the recording**
- Flat imported tables, no relationships. The profiler finds the isolated ones and the missing date
  dimension.
- It proposes. I approve. Then it writes. The agent is good at finding candidates. It should not be the
  one deciding.
- The report side never reaches into the model: it files a request, with a status (proposed,
  acknowledged, implemented, verified), and the model tool's verify gate checks the model contains what
  was asked for. Two tools, one contract, same recipe.
  (`sed -n '20,45p' clients/uk-trade-data/1-Discovery/model_requests.yaml`. VERIFIED.)

**Pro / con of Example 4.** Consistent, tested, gated, with an audit trail and your standards enforced,
against upfront cost, maintenance, covering only what you encoded, and overkill for one-off work. Say
the cost out loud.

---

# PART 3 · Side by side and close (49 to 60)

## 49 to 56 · Pros and cons, and the mistake

Slides for the table, recording for Demo D.

**The table** (from `SESSION-PLAN.md` section 7). Walk it row by row, in the order the audience has just
seen it. Land the message: each rung adds grounding or control, and only the last adds both.

**Demo D · The mistake (RECORDED, TO RECORD).** The field-parameter slicer on report 02 (G-05,
BUG-02-001).

**Say**
- Everything was green. Gates passed. DAX passed. The render matched the mockup.
- The slicer rendered. It accepted a selection. And it drove nothing at all.
- The engine never emitted the binding on the consuming chart, so the chart stayed on one fixed
  measure. No headless check could see it. A person clicking the slicer found it.
- Automated checks catch what they were written to catch. The interaction layer is still yours.

Backup mistake: G-02b, a guessed OKViz GUID that rendered blank cards. The fix was capture the real
shape, never guess.

## 56 to 60 · Close

Slides.

**Say**
- What to check before you trust an agent's work: does every measure resolve live, does the model
  contain what was actually asked for, and does the report survive a refresh.
- What makes it reliable is not the prompt. It is a spec it can be checked against, a bar set before it
  starts, and gates it cannot walk past.
- Where you stay: approving the design, approving the model changes, and driving the thing in the
  Service. The parts where judgement is the work.
- And you do not need my engine to start. Write down what "good" means for one report, turn it into one
  check that fails, and run it over whatever your agent produced. It works with Microsoft's skills as
  well as it works with mine.
- I would rather have a tool that tells me it shipped with caveats than one that tells me it is done.

---

## Fallbacks

| If | Then |
|---|---|
| No wifi | Everything live is already offline. Nothing changes. |
| Port 8199 busy | `lsof -ti :8199 \| xargs kill`, or `serve --port 8210` |
| Pipeline slow on the projector machine | Skip to the advisories, they are the point |
| Running short | Cut 4.3 (model recording), then trim the concepts glimpses. Never cut 4.1 or 4.2. |
| Running very short | Drop Example 3, say plainly it is covered in the notes, and keep chat, skills, and ours |
| `what-we-trade` was signed off since | Demo 4.1 now passes both. Use `pre-commit run --all-files` instead, or point at a different unsigned surface. |
| MCP example not ready | Say so, cut it, and keep the ladder as three rungs. Do not fake it. |
| A recording will not play | Each survives as a spoken story with the relevant file on screen |

---

## Verified on 2026-09-15 (re-run before the session)

| Command | Result then |
|---|---|
| `run_pipeline.py ... --until gates` | GREEN, 5 stages, 9 advisories, 2.69/3 |
| `check_phase_order.py --config what-we-trade.yaml` | blocks, names the missing APPROVED.md |
| `check_phase_order.py --config the-balance.yaml` | passes, signed off and current |
| `pytest -q` (report tool) | 1818 passed (the 2026-09-25 handoff records 2275: use the current number) |
| `pytest -q` (model tool) | 215 passed |
| `mission_control.py next` | per-report next action with the command |
| `mission_control.py serve` | clean, one engagement, no tracebacks |

## Still to do

- Example 1 recording (chat on the brief)
- Example 2 recording (Microsoft skills; note the version and date)
- Example 3: choose the MCP, set it up, record
- Demo B and Demo D recordings
- Slides: hook, lifecycle, agentic, traffic-light table, six concept slides, the four-way table, close
- Re-run every "Verified" command and update the numbers
