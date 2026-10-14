# The agentic era: what you can actually build (6 minute talk)

Written 2026-09-30. Every number is from the real delivery in `agentic-bi-demo`: the Taylor Swift report
`01-one-word-per-era`, taken from requirements to owner acceptance (41 of 41 rail steps, 2026-09-28). About 830
spoken words, which fits six minutes at a relaxed pace. The longer, 60 minute session has its own `DEMO-SCRIPT.md`.

Say it your way: the words below are a draft of the points to land, not lines to recite.

---

## 0:00 to 0:30 · The hook
*On screen: a title slide, or nothing.*

> Every conference this year, every release note: agents, skills, copilots. Lots of talk. Today I'm not going to
> talk about what agents *might* do. I'm going to show you what I built with them. A real Power BI report and a real
> semantic model, delivered end to end, with agents doing the work and me making the decisions.

## 0:30 to 1:30 · What you could build
*On screen: the finished report in Power BI, three pages. Then the semantic model in Fabric.*

> This is the result. A three-page report on open data: one word per era, how each era sounds, how rich its
> vocabulary is. Every number on it was checked against the live model before any design started. Every pixel was
> checked against the approved design after it was deployed.
>
> And this is the semantic model behind it. The agents didn't just use it. They enriched it: new measures, cleaner
> names, missing pieces requested and verified in the model itself.
>
> Two tools, two repos, same recipe: one builds reports, one builds models.

## 1:30 to 2:15 · The steps to get there
*On screen: the phase flow (`docs/phase-flow.html`), Discovery to Govern.*

> How do you get from a sentence to this? Not with one prompt. With a process: Discovery, Design, Develop, Verify,
> Ship, Govern. Forty-one steps. Each step has an owner, whether that's an agent, the engine or me, and each one
> leaves evidence behind. Requirements, user stories, the thesis, 84 proof points, the design contract, the mockup,
> the build, the tests, the sign-offs. Nothing is "done" because an agent says so. It's done when the evidence
> exists.

## 2:15 to 3:15 · Fabric skills, and my skills on top
*On screen: a three-layer stack. Microsoft's Fabric skills and CLIs at the bottom, my skills and engine in the
middle, agents on top.*

> The foundation is Microsoft's own Fabric skills and CLIs. They're the ground truth for what Power BI actually
> accepts. Every report the agents build is validated against them.
>
> On top of that, my skills. That's years of report-building judgement written down so an agent can follow it: how
> to pick a page layout, how to choose a visual, how to fix a render, how to test a deployed report. Plus a bundle
> of every visual and trick, and a knowledge base of every gotcha I've hit.
>
> The agent isn't clever by itself. It's as good as the skills and the knowledge you give it.

## 3:15 to 4:15 · Agents, gates, hooks, and the human
*On screen: a delegation rationale, a challenge file, a hook blocking a commit.*

> Agents check agents. When one model drafts the design contract, a *different* model challenges it. When I
> delegate a decision, a separate agent reads the draft cold and approves it or sends it back. It sent this one back
> twice for a single stale sentence.
>
> Testing is two teams: one finds bugs, the other fixes them, and nobody closes their own bug.
>
> Hooks enforce the rules on every commit: layout checks, AI-slop checks, tests. An agent can't sneak anything past
> them.
>
> And the human? I sign four gates: discovery, design, ship, and acceptance. Everything else, I can delegate. The
> agent does the work. I own the decisions.

## 4:15 to 5:30 · Mission Control, and the recorded demo
*On screen: Mission Control (the rail, all green), then roll the recording.*

> This is Mission Control: one screen that shows every report, every step, what's running, what's waiting on me.
> Green means there's evidence, not an opinion.
>
> Let me show you it running.

*Roll the recording, about 60 seconds: both tools running at once, the model lane and the report lane, then a gate
catching a seeded defect and stopping the deploy until it is fixed.*

> Watch the gate. I planted a mistake. The agent didn't catch it by being careful. The process caught it, because a
> check sits between the agent and production.

## 5:30 to 6:00 · Close
*On screen: the report again.*

> So that's the agentic era, for real: agents doing the work, skills giving them judgement, gates and hooks keeping
> them honest, and a human signing what matters. Not a demo that works once. A process that ships.

---

## To prepare

**The recording.** The Fabric Friday trailer rig (`agentic-bi-demo/demo/`, run sheet `demo/RUNSHEET.md`) records
exactly the gate moment: both lanes at once, a seeded defect, the gate stopping the deploy. Cut it to about 60
seconds.

**Screens, in tab order:**
1. The live report in Power BI (the client copy of One Word Per Era, page 1).
2. The semantic model in Fabric (the Taylor Swift Analytics model).
3. `agentic-bi-demo/docs/phase-flow.html`.
4. The three-layer stack slide (to draw: Microsoft Fabric skills and CLIs / my skills, bundle, knowledge, engine /
   agents).
5. One delegation rationale (`clients/taylor-swift-analytics/4-Governance/delegations/design-contract__01-one-word-per-era.md`)
   and the challenge file beside the design contract (`2-Design/wireframes/01-one-word-per-era/design-contract.challenge.md`).
6. Mission Control: `python3 scripts/mission_control.py serve`, then `http://127.0.0.1:8199/?client=taylor-swift-analytics`
   (all 41 steps green; from a fresh clone this needs `agentic-bi-demo` PR #17, which commits the accepted pack).

**Projector rules** (the repo's): no ids on screen (workspace, dataset, tenant), no client names, and log in to Fabric
before walking on.

**Timing.** Rehearse twice with a timer. If you overrun, cut the hooks paragraph in 3:15 first, then the second half
of the skills beat.

## The facts behind the claims
| Claim | Where it lives |
|---|---|
| 41 steps, each with evidence | `python3 scripts/step_evidence.py clients/taylor-swift-analytics --surface 01-one-word-per-era` |
| 84 proof points checked live | `clients/taylor-swift-analytics/1-Discovery/checkpoints/05-proof-points.md` |
| A second model challenged the contract | `2-Design/wireframes/01-one-word-per-era/design-contract.challenge.md` |
| The delegate sent the contract back twice | `4-Governance/delegations/design-contract__01-one-word-per-era.md`, JOURNAL.md 2026-09-25 |
| Every pixel checked against the design | the Service style diff, 3 of 3 pages green (`3-Develop/deliverables/one-word-per-era/logs/service-dom/`) |
| QA by two teams, nobody closes their own bug | `4-Governance/TEST-REPORT.md` (45 of 45), `4-Governance/BUGS.md` (BUG-01-001) |
| Four human gates | `engine/SPEC-PROGRESS.md` (delegated decisions; the gates) |
| The model enriched and verified | `1-Discovery/model_requests.yaml` (GAP-1, GAP-5 to GAP-9, verified live) |
