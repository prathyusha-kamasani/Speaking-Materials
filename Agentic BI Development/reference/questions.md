# Likely questions

**Why not just use Microsoft's Fabric skills?** For one measure, a prototype or a report you will never rebuild,
do. The difference is advisory versus blocking: you only need blocking when the output carries your name to
someone else, repeatedly, to a standard you have to defend.

**Can it create the tables from raw files?** Not with this tool. It profiles imported tables, proposes the
star schema and wires the relationships. Creating tables is outside its scope.

**What stops it writing to the live model?** The model tool writes to a staging copy, you verify, then you
promote. With a bare MCP connection, nothing does: that is the Example 3 point.

**Does this work with Copilot or another model?** The gates are plain scripts, so they run over any tool's
output. The skills and instructions are Claude-specific, which is part of why they are advisory elsewhere.

**How long did the scaffolding take?** [Answer from your own experience.] It is real upfront cost, and only
worth it for work you will repeat to a standard you must defend.

**What did it get wrong?** The field-parameter slicer (G-05): everything passed, and it drove nothing.
