# The six building blocks

| Concept | One line | Advisory or blocking | In `agentic-bi-demo` |
|---|---|---|---|
| `CLAUDE.md` / `AGENTS.md` | Standing instructions the agent reads every session | Advisory | `AGENTS.md`: the report-build and deploy law. Do not show the top of `CLAUDE.md` on screen (it carries the extract banner). |
| Skills | A repeatable recipe loaded when the task matches | Advisory | `.claude/skills/`: `new-report`, `report-test-loop`, `render-fix-loop`, `grounded-layout`, `delegate-decision` and others |
| Hooks | Run whether or not the agent remembers | Blocking | `.pre-commit-config.yaml`: 28 named hooks, each enforcing one principle |
| Loops | Iterate until a check passes, not until the agent feels done | Blocking when the exit is a check | `render-fix-loop` (mockup versus Service render); `report-test-loop` (two-team QA, the developer never closes their own bug) |
| Gates | A step that refuses to advance without a pass or a signature | Blocking | `check_phase_order.py`; the four human gates (discovery, design, ship approval, owner acceptance) |
| MCP | Live, typed access to a tool or data source | Neither: it is reach | Example 3 |

## The hinge

Skills and instructions are advisory: the agent can ignore them. Hooks and gates are blocking: it cannot.
The diagnosis behind it, from the production repo's history (2026-07-15): a cold Copilot session, with every
knowledge file present, shipped a bad report and deployed it by the wrong path. The knowledge was **opt-in,
advisory, tool-specific and runtime-bypassable**.

## Process is a spec, not a prompt

Every behaviour is a versioned `ALG-*` spec in `algorithms/` that declares its inputs, preconditions, gate,
sign-off, invariants and tests. An invariant is a promise the code keeps, with a test name next to it.
Example: `head -30 algorithms/ALG-DISCOVERY.md`.
