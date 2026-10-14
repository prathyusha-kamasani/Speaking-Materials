# Build path plan: showing how the tool got made

Status: draft 2026-09-15, awaiting sign-off.

Companion to `SESSION-PLAN.md`. That file plans the 60 minutes. This one plans the artefact the
session needs and does not yet have: a way to show **how you get there**, not just the finished tool.

---

## The problem

`agentic-bi-demo` is the end state. It works: 1818 tests pass, the offline pipeline is green, Mission
Control is clean. But a tour of a finished repo teaches nobody how to build one, and the talk's whole
claim is that the scaffolding is what makes agent output trustworthy.

The repo also has a fresh `git init`, so the real build history is not recoverable from it. The path
has to be authored deliberately.

---

## Three checkpoints

Each checkpoint is a repo a person could be handed, that runs, and that proves one layer earns its
place. Mapped to the four things you build: process, scripts, skills, gates.

### Checkpoint 1: process before code
**Contains:** `PRINCIPLES.md`, one `ALG-*` spec, one `report.yaml`, one validator.
**Proves:** `python3 scripts/check_report_config.py <report.yaml>`
**The point:** you can gate a specification before you own an engine. The spec is the contract the
agent works to, and it is checkable on day one.

### Checkpoint 2: scripts and a consistent deliverable
**Contains:** the engine that turns that spec into PBIR, one output shape, first tests.
**Proves:** `python3 scripts/run_pipeline.py <report.yaml> --until build`
**The point:** one path in, one shape out. The agent stops improvising the deliverable.

### Checkpoint 3: gates and the loop
**Contains:** the gate suite, the advisory wall, the human sign-off.
**Proves:** `run_pipeline.py --until gates`, then a `phase-order` block on an unapproved wireframe.
**The point:** the quality bar is set before the agent starts, and the loop cannot advance itself.

---

## How to build them

**By addition, in a separate minimal tree. Not by stripping the demo repo back three times.**

This is the lesson of 2026-09-15: subtracting from the working repo cascades. Removing one engagement
surfaced two governance failures, and a fuller strip produced 40 failures and 13 errors because the
gallery surface is anchored in production code. Building up from empty is slower to start and far more
predictable, and every checkpoint stays genuinely runnable.

Each checkpoint gets a tag in its own repo, and a one-page `WHAT-CHANGED.md` naming the single idea it
adds.

---

## Local or cloud

| Work | Where | Why |
|---|---|---|
| Building the three checkpoints | **local** | Needs fast iteration against a running suite. Cascading failures are the norm, and a sandbox that cannot verify quickly will flail. |
| Deck narrative, demo script prose, abstract rewrite | **cloud** | Text work, no repo execution needed. Parallelises cleanly. |
| Rehearsing and recording demos | **local** | Needs the Service, Fabric auth and a screen. |

Cloud needs the repo on GitHub first. `gh` is authenticated with `repo` scope, so a private repo plus
push is one command. That is an IP decision, not a technical one: private on GitHub is still yours, but
it leaves the machine. Not required for the local path.

---

## Order of work

1. Checkpoint 1 built and rehearsed
2. Checkpoint 2 built and rehearsed
3. Checkpoint 3 built and rehearsed
4. Demo script written against the three, plus the end state
5. Slides last, structure only, once the demos are fixed

Slides last on purpose. Writing them before the demos are settled means rewriting them.

---

## Risks

| Risk | Mitigation |
|---|---|
| Checkpoints become a second project | Three, not seven. Each one adds a single idea and nothing else. |
| Checkpoint code drifts from the real tool | Copy from `agentic-bi-demo` rather than writing fresh. Each file is the real file, minus what does not exist yet. |
| Live checkout between checkpoints eats time | Three terminal tabs, one per checkpoint, opened before the session starts. |
| 60 minutes will not hold three checkpoints plus the end state | Checkpoints are Act 1 and stay under 3 minutes each. If pressed, checkpoint 2 becomes a slide. |

---

## Open questions

1. Does the audience see the checkpoints as three repos, or one repo at three tags? Tags read as
   history, which is the honest framing, but a checkout on stage is a moment where things go wrong.
2. Does checkpoint 1 use the UK Trade report, or a smaller throwaway spec? Smaller is clearer to read
   on a projector; UK Trade means one story across all three.
