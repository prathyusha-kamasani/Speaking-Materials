# Demo B: the model half, same recipe (48 to 49, recorded, optional, to record)

**What you show:** flat imported tables become a wired star, with you approving the joins.
**Point:** the agent finds candidates and proposes; you decide; the tool records what it did.
**Needs Fabric auth, so record it.** Work in tab 2 (`agentic-bi-demo-model`) and tab 1 for the report side.

## Starting state
Flat imported tables with no relationships ("raw data in, dimensional model out", with no ingestion step: that
part is not real, so do not imply it). Build this state on the UK Trade open data first.

## On screen, in order
1. (0:10) `cache_model_schema.py` takes a snapshot of the model.
2. (0:15) `profile_model.py` prints `isolated-table`, `no-date-dimension`, `no-measures`.
3. (0:15) The proposed joins listed. **You say yes out loud.** This approval is the point.
4. (0:15) `add_relationship.py` writes them: idempotent, stable ids.
5. (0:15) `apply_model_requests.py` lands the measures and appends to `MODEL_CHANGELOG.md`.

## Say
- The profiler found the isolated tables and the missing date dimension. It proposes. I approve. Then it writes.
- The report side never edits the model. It files a request with a status (proposed, acknowledged, implemented,
  verified), and the model tool's verify gate checks the model contains what was asked for. Two tools, one
  contract.

## Glimpse of the contract
```bash
sed -n '/^measures:/,+14p' clients/uk-trade-data/1-Discovery/model_requests.yaml
```
Do NOT show the top of that file: its header carries a workspace id.

Cut first if short on time.
