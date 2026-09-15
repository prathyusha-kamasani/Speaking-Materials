# The comparison: Microsoft Fabric Skills versus the scaffolded tool

Status: plan agreed 2026-09-15. Not yet run.

Answers the question the room will actually ask: **why build all this when Microsoft ships Fabric
Skills?** That question is no longer hypothetical. Microsoft ships Fabric Skills for GitHub Copilot,
Claude and the CLI, including the Power BI Report Authoring Agent Skills from Build 2026, which
design, build, validate and publish reports from a description or a screenshot.

Ignoring that in the session reads as evasion. Answering it badly reads as defensiveness. So we run
it and publish the result.

---

## The reframe that makes this work

The claim is **not** "my engine beats Microsoft's skills". That is unwinnable and a bit grubby, and
half the room uses those skills happily.

The claim is: **here is how you would know, either way.**

The gates are the referee. They are reusable by anyone, including a person who only ever uses
Copilot. That turns the session from a pitch into something the audience can take home and apply to
whatever tool they already use.

---

## Five rules for a fair test

1. **Same brief, same dataset.** The Microsoft skills get the same UK Trade requirement the
   scaffolded tool gets, written as prose rather than config. Not a thinner one.
2. **Set them up properly**, following Microsoft's own install documentation. A half-configured
   competitor is a strawman, and an audience that uses these daily will spot it in seconds.
3. **Run it three to five times.** One run proves nothing either way. If one brief produces five
   materially different models, that is the finding, and it is a fair one.
4. **The gates judge, not opinion.** Run `check_report`, the preflight binding check, and the
   advisory rules over whatever comes out. Publish the scorecard.
5. **Say where Microsoft wins, out loud.** It will reach a first draft far faster, it needs no repo
   and no engine, and for most people most of the time that is the correct trade.

---

## What gets recorded and kept

Commit into `agentic-bi-demo` under `comparison/`:

```
comparison/
├── BRIEF.md              the prose requirement given to the MS skills, verbatim
├── SETUP.md              how the skills were installed and configured, with versions and dates
├── runs/run-01..05/      the artefacts each run produced
├── SCORECARD.md          each run scored by the same gates, plus the scaffolded build for reference
└── FINDINGS.md           what varied between runs, what the gates caught, where MS won
```

`SETUP.md` matters more than it sounds. It is the evidence that the test was fair, and it is the
first thing a sceptic will ask for.

---

## On stage

**Do not run the Microsoft skills live.** A live agent run is the riskiest demo there is: slow,
non-deterministic, and dependent on the network. Record the runs beforehand.

What happens live is the **scorecard**, because that is the fast, legible part: same brief, here is
what came out, here is what the gates said about each. Thirty seconds of terminal, and the audience
draws its own conclusion.

---

## The honest answer, if the result is not what we expect

If the Microsoft skills produce something the gates pass cleanly, **say so and keep the slide in.**
That is a more interesting talk, not a worse one, and it is the only version that survives someone
in the audience going home and trying it.

The argument does not actually depend on the skills producing bad output. It depends on there being
no way to *know* without a gate. A clean pass proves the gate works, which is the point.

---

## Where the objection is right, and should be conceded early

For a single measure, an ad-hoc analysis, a prototype, or one report that will never be rebuilt,
Copilot and the Fabric Skills win outright, and this scaffolding is absurd. It is 1818 tests and 30
gates. Nobody should build that to ship one report.

The line is not AI versus engineering. It is **advisory versus blocking**. You only need blocking
when the output carries your name to someone else, repeatedly, to a standard you have to defend.

The evidence for that line is already in the repo's own history (`STATE.md`, 2026-07-15): a cold
Copilot session, with all the knowledge files present, shipped a bad report and deployed it by the
wrong path. The diagnosis recorded at the time was that the repo's knowledge was
**opt-in, advisory, tool-specific and runtime-bypassable**. Those four words are the slide.

---

## Risks

| Risk | Mitigation |
|---|---|
| Reads as a hit piece on Microsoft | Concede the win early, publish the setup, let the gates speak |
| One unlucky run misrepresents the skills | Three to five runs, publish all of them |
| Skills improve between now and the session | Date the runs and say the version. Re-run close to the date. |
| Comparison eats the session | It is one 5 minute beat plus a framing beat. Recorded, not live. |
| It becomes a second project | Cap it: one report, one brief, five runs, one scorecard. |

---

## Sequencing

Do the comparison **before** the staged checkpoints. The checkpoints teach the method, which is
valuable. The comparison answers the question the room will definitely ask, which is essential.
