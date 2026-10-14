# Example 4: Fabric skills plus your own skills

**Medium:** live and offline (A, C), recorded (B). Tab 1, `agentic-bi-demo`.

| Step | File | Min | Status |
|---|---|---|---|
| Demo A, the gate refuses | [demo-a-gate-refuses.md](demo-a-gate-refuses.md) | 2 | verified 2026-10-08 |
| Demo C, one command, the whole build | [demo-c-one-command.md](demo-c-one-command.md) | 3 to 4 | green on `contrast-accept` 2026-10-08 |
| Demo B, the model half | [demo-b-model-half.md](demo-b-model-half.md) | 1 to 2, optional | to record |

Pro: consistent, tested and gated, with an audit trail and your standards enforced.
Con: upfront cost and upkeep, covers only what you encoded, overkill for one-off work. Say it out loud.

Deployment: this one deploys through `run_pipeline.py --deploy`, never `fab import`, into its own folder in the
Fabric Friday Demo workspace (to be confirmed, see `../02-fabric-skills/README.md`).
