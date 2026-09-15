# Demo script: Agentic BI Development, 60 minutes

Every command below was run on Prathy's machine on 2026-09-15 and produced the output described.
Nothing here is aspirational. Where a step needs Fabric, it is marked RECORDED.

Talking points are prompts, not a script. Say them your way.

---

## Pre-flight brief

**Audience.** Fabric and Power BI practitioners, mixed seniority, who have tried Copilot or an AI
agent and were either burned or unconvinced. They read DAX. They do not run agent pipelines.

**Outcome.** They leave able to name the four things you build before letting an agent near a
deliverable, and the specific checks that catch an agent being confidently wrong.

**Format.** 60 minutes. Two acts, matching the two processes: build the tool, then deliver a project.
Terminal carries the evidence, slides carry structure only.

**Assumptions.** Demo from `agentic-bi-demo` and `agentic-bi-demo-model`, never the production repos.
Everything live is offline: system Python, no venv, no Fabric auth, no network. Anything needing the
Service is pre-recorded.

**Exclusions.** No data engineering or pipelines. No client names anywhere, in any file, terminal
scrollback, or recording.

---

## Setup, before you walk on

```bash
lsof -ti :8199 | xargs kill          # kill strays from an earlier run
```

- **Tab 1:** `cd .../agentic-bi-demo`, the report tool. Most of the demo lives here.
- **Tab 2:** `cd .../agentic-bi-demo-model`, the model tool. Act 1 step 6 and Act 2 step 2.
- **Tab 3:** `python3 scripts/mission_control.py serve` running, browser open on `127.0.0.1:8199`.
- Font size up. `clear` every tab. Recordings queued and ready.

A stale server on 8199 is the most likely thing to bite you. Kill it first, every time.

---

## 0 to 4 · The problem

No demo. Slides.

**Say**
- An agent will write you a semantic model and a report, and it will look right.
- The DAX runs. The visuals render. Nothing errors.
- That is exactly the problem. Looking right and being right are different things, and you cannot
  tell them apart by looking.
- So the question for the next hour is not "can AI build this". It is "what would you have to check
  before you trusted it".

---

## 4 to 9 · "Why not just use the Fabric skills?"

No demo. Slides. Get this out of the way early and honestly, before anyone has to ask it.

**Say**
- Microsoft ships Fabric Skills now. For Copilot, for Claude, for the CLI. The report authoring
  skills will build and publish a report from a description or a screenshot.
- They are good. For one measure, an ad-hoc analysis, a prototype, a report you will never rebuild,
  they win outright and what I am about to show you is absurd overkill.
- So let me be straight about where the line is, because it is not AI versus engineering.
- I tried the skills-only version. A cold Copilot session, with all my knowledge files sitting right
  there, shipped a bad report and deployed it by the wrong path.
- When I worked out why, it came down to four words. The knowledge was opt-in, advisory,
  tool-specific, and runtime-bypassable.
- Opt-in: the agent decides whether to read it. Advisory: nothing fails when it is ignored.
  Tool-specific: a Copilot session never sees my Claude skills. Bypassable: you can always just run
  the command yourself.
- Everything in the next hour is about turning advisory into blocking. And at the end I will run the
  same brief through Microsoft's skills and score it with the same gates, so you can judge it rather
  than take my word for it.

**Slide:** those four words. Nothing else on it.

---

# ACT 1 · Build the tool (9 to 30)

## Step 1.1 · The four things you build first (9 to 12)

```bash
ls .claude/skills
ls algorithms | head -12
ls scripts | grep -c '^check_'
```

**On screen** Five skills. Twenty-two `ALG-*` specs. Thirty-plus `check_*` scripts.

**Say**
- Before any agent ran, four things existed: skills, scripts, process, gates.
- Skills are how the agent does a job. Specs are the process. The check scripts are the gates.
- None of this is the AI. This is the scaffolding the AI works inside.

## Step 1.2 · Process is a spec, not a prompt (12 to 15)

```bash
head -30 algorithms/ALG-DISCOVERY.md
```

**On screen** Frontmatter: `inputs`, `preconditions`, `gate`, `signoff`, `invariants`, `tests`.

**Say**
- Every behaviour is a versioned spec. It declares its inputs, its gate, who signs it off, and its
  invariants.
- An invariant is a promise the code must keep. It has a test name next to it.
- This is the difference between a prompt and a process. A prompt is a wish. This is checkable.

## Step 1.3 · Gates are code, not intentions (15 to 20)

This is the beat. Run both, in this order.

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
- The blocked one has no `APPROVED.md`. A human has not signed off the design.
- The agent cannot start building it. Not "should not". Cannot.
- That is what I mean by human in the loop. Not a person watching. A gate the loop cannot walk past.

## Step 1.4 · The loop cannot advance itself (20 to 24)

```bash
grep -n "autoadvance\|await developer sign-off" algorithms/ALG-PIPELINE.md
```

**On screen** `test_no_autoadvance_without_signoff`, and a step that reads "await developer sign-off".

**Say**
- There is a test whose name is the rule: no auto-advance without sign-off.
- The pipeline's own spec ends a phase by waiting for a person.
- One more rule worth stealing: in the QA loop, the developer never closes their own bug. Someone
  else verifies it, against the live render.

## Step 1.5 · Tests and validation (24 to 27)

```bash
python3 -m pytest -q
grep -c "id:" .pre-commit-config.yaml
```

**On screen** `1818 passed`, and 30-odd named hooks.

**Say**
- Eighteen hundred tests, and thirty gates that run before a commit lands.
- Each gate enforces one principle. One blocks hand-placed layout. One blocks a raw deploy command.
  One checks that the knowledge files do not contradict a blocking rule.
- The point is not the number. The point is that the quality bar was set before the agent started,
  not argued about afterwards.

## Step 1.6 · Same recipe, second tool (27 to 30)

Switch to **Tab 2**.

```bash
ls
python3 -m pytest -q
python3 scripts/verify_model.py --help
```

**On screen** Same shape: `knowledge/`, `prompts/`, `scripts/`, `architecture/`. `215 passed`.
`verify_model` described as a read-only gate.

**Say**
- Different tool, different job. Same four things.
- This one works on semantic models: descriptions, synonyms, renames, Copilot readiness.
- Its safety rule is one line: it writes to a staging copy, you verify, then you promote. It never
  writes to the live model.
- That is the recipe repeating. Build it once, and the second tool is faster and safer than the
  first.

---

# ACT 2 · Deliver a project (30 to 55)

Back to **Tab 1**.

## Step 2.1 · Requirements in (30 to 34)

```bash
ls clients/uk-trade-data/1-Discovery/
sed -n '1,30p' clients/uk-trade-data/3-Develop/reports/the-balance.yaml
```

**Say**
- Real engagement, open data. UK trade figures from ONS.
- Discovery is user stories with acceptance criteria, and a profile of what the model already has.
- The config is the spec the agent works to. Not a chat message. A file, in version control, that a
  gate can read.
- If you want one takeaway on briefing an agent: write the thing it can be checked against.

## Step 2.2 · The model half, and the contract between the tools (34 to 39)

```bash
sed -n '20,45p' clients/uk-trade-data/1-Discovery/model_requests.yaml
```

**Say**
- The report side does not reach into the model and change it. It files a request.
- Every entry has a status: proposed, acknowledged, implemented, verified.
- A report binding a pending measure is a warning. Binding one that was never requested is a hard
  error.
- And the model tool's verify gate takes this same file, to check the model actually contains what
  was asked for. Two tools, one contract.

**RECORDED · the star gets wired**
1. `cache_model_schema.py` takes a snapshot
2. `profile_model.py` reports isolated tables and no date dimension
3. the agent proposes the joins, **you approve**
4. `add_relationship.py` writes them, idempotent, stable ids
5. `apply_model_requests.py` lands the measures and appends `MODEL_CHANGELOG.md`

**Say over the recording**
- Flat tables, no relationships. The profiler finds the ones that are isolated.
- It proposes. I approve. Then it writes.
- That approval is the whole point. The agent is good at finding candidates. It should not be the
  one deciding.

## Step 2.3 · The report half, one command (39 to 45)

```bash
python3 scripts/run_pipeline.py clients/uk-trade-data/3-Develop/reports/the-balance.yaml --until gates
```

**On screen** Five stages green, then nine advisories, then `ship-with-caveats (2.69/3)`.

Zoom in and read this one out:

```
R-SURVIVES-REFRESH: '_Card Balance' is painted a fixed #C25A3C — the colour cannot flip
when the sign flips on refresh (a deficit keeps the surplus colour).
```

**Say**
- One command. Sync, capture, phase order, build, gates.
- It passed. And it still has nine things to tell me.
- This is the one I would put on a poster. The report is correct today. After the next refresh,
  when that number goes negative, the colour stays the colour of a surplus.
- Nobody catches that by looking at a screenshot. The report looks perfect. A gate catches it
  because someone wrote down what "survives a refresh" means.
- And notice the tool grades itself: ship with caveats, 2.69 out of 3. It is not telling me it is
  finished.

## Step 2.4 · The operator's queue (45 to 47)

```bash
python3 scripts/mission_control.py next
```

**On screen** Per report, the next action and the literal command, including
`add .../wireframes/04-eu-vs-world/APPROVED.md`.

**Say**
- This is what operating it actually feels like.
- It tells me what is next, for each surface, and gives me the exact command.
- Two of these are blocked on data that is not mine to fix. It says so, and it says design can carry
  on anyway.
- And where it needs me, it asks. That line is my sign-off. The work stops there until I do it.

## Step 2.5 · The mistake (47 to 50)

**RECORDED.** The field-parameter slicer on report 02.

**Say**
- Everything was green. Gates passed. DAX passed. The render matched the mockup.
- The slicer rendered. It accepted a selection. And it drove nothing at all.
- The engine never emitted the binding on the consuming chart, so the chart stayed on one fixed
  measure.
- No headless check could see it. It was found by a person clicking the slicer and noticing the bar
  chart did not move.
- That is the honest edge of this. Automated checks catch what they were written to catch. The
  interaction layer is still yours.

---

## Step 2.6 · The same brief, through Microsoft's skills (50 to 55)

RECORDED runs. LIVE scorecard.

```bash
cat comparison/SCORECARD.md
```

**On screen** Five Microsoft skills runs and the scaffolded build, each scored by the same gates.

**Say**
- Same brief, same dataset. Microsoft's Fabric Skills, set up properly, run five times.
- Here is what came out, and here is what the same gates said about each one.
- [Read it honestly, including anywhere Microsoft passed clean.]
- What I want you to notice is not which column wins. It is that there is a column at all.
- Without the gates you have five reports and a feeling. With them you have five reports and a
  number you can defend to whoever signs this off.
- If you take one thing home, take the gates. They work on whatever tool you already use.

---

## 55 to 60 · Close

Slides.

**Say**
- What to check before you trust an agent's semantic model: does every measure resolve live, does
  the model contain what was actually asked for, and does the report survive a refresh.
- What makes it reliable is not the prompt. It is a spec it can be checked against, a bar set before
  it starts, and gates it cannot walk past.
- Where you stay: approving the design, approving the model changes, and driving the thing in the
  Service. The parts where judgement is the work.
- And you do not need my engine to start. Write down what "good" means for one report, turn it into
  one check that fails, and run it over whatever your agent produced. That is the whole idea, and it
  works with Microsoft's skills as well as it works with mine.
- I would rather have a tool that tells me it shipped with caveats than one that tells me it is done.

---

## Fallbacks

| If | Then |
|---|---|
| No wifi | Everything live is already offline. Nothing changes. |
| Port 8199 busy | `lsof -ti :8199 \| xargs kill`, or `serve --port 8210` |
| Pipeline slow on the projector machine | Skip to the advisories, they are the point |
| Running short | Cut 1.5 (tests) and 2.4 (queue). Never cut 1.3, 2.3 or 2.6. |
| Running very short | Act 2 alone still works: spec in, gates out, the mistake, the scorecard |
| Comparison runs not finished in time | Keep the 4 to 9 framing beat, drop 2.6, and say plainly that the comparison is still running. Do not show a partial scorecard. |
| A recording will not play | 2.2 and 2.5 both survive as spoken stories with the config on screen |

---

## Verified on 2026-09-15

| Command | Result |
|---|---|
| `run_pipeline.py ... --until gates` | GREEN, 5 stages, 9 advisories, 2.69/3 |
| `check_phase_order.py --config what-we-trade.yaml` | blocks, names the missing APPROVED.md |
| `check_phase_order.py --config the-balance.yaml` | passes, signed off and current |
| `pytest -q` (report tool) | 1818 passed |
| `pytest -q` (model tool) | 215 passed |
| `mission_control.py next` | per-report next action with the command |
| `mission_control.py serve` | clean, one engagement, no tracebacks |

Still to do:
- the two recordings (2.2 and 2.5)
- the comparison runs and scorecard (2.6), method in `COMPARISON-PLAN.md`
