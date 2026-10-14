# Example 1: chat agent (24 to 30, recording, to record)

**What you show:** the cheapest way to get an answer, and exactly where it is blind.
**Point:** fast and fluent, but it cannot see your model, so every name is a guess.

## What goes on screen, in order
1. (0:20) A plain chat window. No tools, no files, no connectors. Say so.
2. (0:20) Paste [../BRIEF.md](../BRIEF.md) unchanged.
3. (1:30) It answers: a page layout, some DAX for the balance, a colour rule for the card.
4. (2:30) **Pick out the guesses.** Highlight every table and column name (`'Trade'[Exports]`, `Date[Month]` and
   so on). Ask the room: do these exist in your model? It has never seen one.
5. (1:00) Ask it the follow-up that exposes it: "what is the name of the date table in my model?" It either
   guesses again or asks you to paste the schema.

## Say
- For one measure, or a "how would I write this", chat is the right tool. Concede it.
- Every name here is invented. It reads well, so you only find out when you paste it into Power BI.
- Nothing was checked, and tomorrow it will not give the same answer.

## Record
`recording.mp4` and `transcript.md` in this folder. Pro: zero setup, fast for DAX. Con: blind, unrepeatable.
No deployment, so no Fabric folder.
