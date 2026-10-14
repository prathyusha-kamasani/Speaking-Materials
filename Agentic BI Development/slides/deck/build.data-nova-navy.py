#!/usr/bin/env python3
"""Builds index.html: the Agentic BI Development deck, on the Data Nova design system.

Run: python3 build.py   (writes index.html next to this file)
Edit the slides below, rebuild, then check with the design system's checker (see ../README.md).
Every colour, face and size comes from the tokens in styles.css and deck.css; nothing is hardcoded here.
"""
from pathlib import Path

CREDIT = '<div class="credit">Prathy Kamasani <span>&middot; Data Nova &middot; Data Alchemy</span></div>'
SLIDES = []  # (html, notes)


def icon(name, cls="ink-accent", size="icon"):
    return f'<i data-lucide="{name}" class="{size} {cls}"></i>'


def slide(body, notes, dark=False, light_extra=""):
    SLIDES.append((body, notes, dark))


def card(inner, extra=""):
    return f'<div class="card {extra}">{inner}</div>'


# ---- 1 Title ---------------------------------------------------------------------------------------------
slide("""
<img class="mark" src="assets/logo/data-nova-mark.png" alt="Data Nova">
<div class="eyebrow mt48">60-minute session</div>
<div class="h1">Agentic BI Development</div>
<div class="body mt32" style="max-width:1300px">What to check before you trust an agent's work.</div>
<div class="agenda">
  <div class="ag"><div class="label">01</div><div class="h4">What is BI development?</div></div>
  <div class="ag"><div class="label">02</div><div class="h4">Six ideas that matter</div></div>
  <div class="ag"><div class="label">03</div><div class="h4">One brief, four ways</div></div>
</div>
""", "60 minutes. Hook first, then concepts, then one brief run four ways. The refrain for the hour: what would you have to check?", dark=True)

# ---- 2 Hook ----------------------------------------------------------------------------------------------
slide(f"""
<div class="center-v" style="padding-bottom:96px">
  <div class="grid2" style="align-items:center">
    <div>
      <div class="h1c">It looks right.</div>
      <div class="body mt24">Is it right?</div>
    </div>
    <div class="list" style="gap:32px">
      <div class="item">{icon("check", "ink-accent", "icon-xl")}<div class="h4" style="padding-top:8px">The DAX runs</div></div>
      <div class="item">{icon("check", "ink-accent", "icon-xl")}<div class="h4" style="padding-top:8px">The visuals render</div></div>
      <div class="item">{icon("check", "ink-accent", "icon-xl")}<div class="h4" style="padding-top:8px">Nothing errors</div></div>
    </div>
  </div>
</div>
""", "An agent will write you a semantic model and a report, and it will look right. The DAX runs. The visuals render. Nothing errors. Looking right and being right are different things, and you cannot tell them apart by looking. So the question for the hour is not 'can AI build this'. It is 'what would you have to check before you trusted it'.", dark=True)


def section(num, title, sub, notes):
    # editorial divider: a giant numeral with the title laid over its right-hand digit
    slide(f"""
<div class="sect">
  <div class="sect-num" aria-hidden="true">{num}</div>
  <div class="sect-title"><div class="h1c">{title}</div><div class="body sect-sub">{sub}</div></div>
</div>
""", notes, dark=True)


# ---- 3 Section: BI development ---------------------------------------------------------------------------
section("01", "What is BI development?", "Six steps, and most of the time is not in the visuals.",
        "Set up the lifecycle before talking about agents. Most delivery time is not building the visual: it is requirements, model fixes, testing, rework after feedback, and sign-off. [Add your own example of where the hours really go.]")

# ---- 4 Lifecycle -----------------------------------------------------------------------------------------
steps = [("01", "Discover", "Users, questions, acceptance criteria"), ("02", "Model", "Tables, relationships, measures"),
         ("03", "Build", "Pages, visuals, theme, layout"), ("04", "Test", "Numbers, render, interaction"),
         ("05", "Deploy", "Workspace, binding, refresh"), ("06", "Govern", "Sign-off, audit trail, changes")]
cards = "".join(card(f'<div class="label">{n}</div><div class="h4" style="margin-top:16px">{t}</div><div class="small" style="margin-top:16px">{d}</div>') for n, t, d in steps)
slide(f"""
<div class="eyebrow">01 &middot; BI development</div>
<div class="h2">From a question to a trusted report</div>
<div class="grid3 mt48" style="grid-template-rows:repeat(2, 1fr);gap:48px">{cards}</div>
""", "Walk the six steps quickly. For each, ask who does it today. Flag Test and Govern: they are where trust is earned, and where agents are weakest. If time is tight, say this slide rather than show it: the room already knows it.")

# ---- 5 Chat vs agentic -----------------------------------------------------------------------------------
chat_items = "".join(f'<div class="small">{t}</div>' for t in ["You ask", "It answers", "You copy and paste", "Nothing is checked"])
loop_items = "".join(f'<div class="small">{t}</div>' for t in ["Plan", "Act with tools", "Observe the result", "Try again, or stop"])
slide(f"""
<div class="eyebrow">01 &middot; Agentic</div>
<div class="h2">Chat answers. An agent acts.</div>
<div class="grid2 mt48" style="grid-template-columns:5fr 6fr;align-items:stretch">
  {card(f'<div class="h4">Chat</div><div class="list" style="margin-top:32px;gap:24px">{chat_items}</div>')}
  <div class="card" data-theme="dark" style="background:var(--dn-surface)">
    <div class="h4">Agentic</div>
    <div class="list" style="margin-top:32px;gap:24px">{loop_items}</div>
    <div class="small ink-violet" style="margin-top:24px">A human approves at the gates</div>
  </div>
</div>
<div class="takeaway">The loop is the power and the risk.</div>
""", "Chat: you ask, it answers, you copy and paste. Agentic: a model, plus tools, plus a loop, plus a human. It acts, looks at what happened, and tries again. That loop is the power and the risk: it can fix its own errors, and it can confidently build on its own mistake.")

# ---- 6 Which bits ----------------------------------------------------------------------------------------
def col(ic, cls, head, items):
    li = "".join(f'<div class="small">{t}</div>' for t in items)
    return card(f'<div class="h4 {cls}" style="min-height:48px">{head}</div><div class="list mt24" style="margin-top:24px">{li}</div>')
slide(f"""
<div class="eyebrow">01 &middot; What agents can do</div>
<div class="h2">Which bits can an agent do?</div>
<div class="grid3 mt48" style="align-items:stretch">
  {col("circle-check", "ink-accent", "Agent does it", ["Profile the model", "Relationships, measures", "Build the report files", "Data and render tests", "Gated deploy"])}
  {col("pencil-line", "ink-violet", "Agent drafts", ["Requirements and discovery", "Page layout and design", "Fixes for what tests find"])}
  {col("user-check", "ink-violet", "You decide", ["Sign-off and acceptance", "Interaction testing", "What good means"])}
</div>
""", "Teal is the agent, violet is you. The agent does profiling a model, relationships, measures, building report files, data and render tests, and gated deploy. It drafts requirements and layout, and you decide. Interaction testing and sign-off stay with a person. One honest caveat: it can propose and wire a star schema from imported tables, but it does not create tables from raw files. It profiles and wires tables already in the model. Do not imply more.")

# ---- 7 Section: ideas ------------------------------------------------------------------------------------
section("02", "Six ideas that matter", "Instructions, skills, hooks, loops, gates, MCP.",
        "Do not linger: the examples are where these come alive. One table of definitions and where each lives, then one slide on the hinge.")

# ---- 8 Vocabulary + where it lives -----------------------------------------------------------------------
rows = [("Instructions", "Advisory", "AGENTS.md", "Standing rules, read every session"),
        ("Skills", "Advisory", ".claude/skills/", "A repeatable recipe for one job"),
        ("MCP", "Reach", "an MCP server", "Live, typed access to tools and data"),
        ("Hooks", "Blocking", ".pre-commit-config.yaml", "Run on every commit, even if the agent forgets"),
        ("Loops", "Blocking", "ALG-PIPELINE.md", "Repeat until a check passes"),
        ("Gates", "Blocking", "check_phase_order.py", "No APPROVED.md, no build")]
kind_cls = {"Advisory": "ink-violet", "Reach": "muted", "Blocking": "ink-accent"}
tr = "".join(f'<tr><td>{a}</td><td><span class="label {kind_cls[b]}">{b}</span></td><td class="mono nowrap">{c}</td><td>{d}</td></tr>' for a, b, c, d in rows)
slide(f"""
<div class="eyebrow">02 &middot; The vocabulary</div>
<div class="h2">Six ideas, and where each one lives</div>
<table class="cmp tight vocab" style="margin-top:32px"><thead><tr><th>Idea</th><th>Kind</th><th>Where it lives</th><th>What it does</th></tr></thead><tbody>{tr}</tbody></table>
""", "Instructions (AGENTS.md, or CLAUDE.md for Claude): standing rules read every session. Skills: a repeatable recipe loaded when the task matches. MCP: live typed access to a tool or data source. Hooks: run on every commit whether or not the agent remembers. Loops: iterate until a check passes, not until the agent feels done. Gates: a step that refuses to advance without a pass or a human signature. Show the 'where it lives' column only as glimpses, 20 to 30 seconds each, from the repo. Check what is on screen before projecting: no client names. Do not open the top of CLAUDE.md in the demo repo, it carries the extract banner; use AGENTS.md. The pre-commit file has 28 named hooks.")

# ---- 9 Advisory or blocking ------------------------------------------------------------------------------
slide(f"""
<div class="eyebrow">02 &middot; The hinge</div>
<div class="h2">Advisory or blocking?</div>
<div class="grid2 mt48" style="align-items:stretch">
  <div class="card">
    <div class="h4 ink-violet">Advisory</div>
    <div class="body strong" style="margin-top:24px">Instructions and skills.</div>
    <div class="body" style="margin-top:16px;line-height:1.4">The agent decides whether to read them. Nothing fails if it does not.</div>
  </div>
  <div class="card" data-theme="dark" style="background:var(--dn-surface)">
    <div class="h4 ink-accent">Blocking</div>
    <div class="body strong" style="margin-top:24px;color:var(--dn-text-strong)">Hooks and gates.</div>
    <div class="body" style="margin-top:16px;line-height:1.4">The agent cannot walk past them. A failing check stops the build.</div>
  </div>
</div>
<div class="takeaway">A knowledge file is advice. Any tool can skip it, on any run. A check cannot be skipped.</div>
""", "Instructions and skills are advisory: the agent can ignore them. Hooks and gates are blocking: it cannot. That is the hinge for everything that follows. Each example sits at a different point on advisory versus blocking, and on blind versus grounded. Evidence from my own history: a cold Copilot session with all the knowledge files present shipped a bad report and deployed it by the wrong path. Any agent would have done the same; the files were the weak link, not the tool. The diagnosis was four words: the knowledge was opt-in, advisory, tool-specific, runtime-bypassable.")

# ---- 10 Section: four ways -------------------------------------------------------------------------------
section("03", "One brief, four ways", "Same requirement every time, so the comparison is fair.",
        "For each example use the same four beats: setup, brief in, what came out, what we had to check. Do not declare a winner until the comparison slide.")

# ---- 11 The brief ----------------------------------------------------------------------------------------
brief = ["One page on the UK trade balance: exports less imports, over time", "A headline balance card that flips colour from surplus to deficit",
         "A trend by month", "A breakdown by partner country or commodity", "A slicer to switch the measure"]
bl = "".join(f'<div class="small">{t}</div>' for t in brief)
traps = [("Colour that must flip", "Correct today, wrong after the next refresh"), ("A slicer that drives a measure", "Renders fine. Drives nothing."),
         ("No date dimension", "The trend needs one")]
tl = "".join(f'<div class="trap"><div class="h4">{a}</div><div class="small" style="margin-top:8px">{b}</div></div>' for a, b in traps)
slide(f"""
<div class="eyebrow">03 &middot; The brief</div>
<div class="h2">UK trade, the balance</div>
<div class="grid2 mt48" style="grid-template-columns:6fr 5fr;align-items:stretch">
  {card(f'<div class="label">The brief</div><div class="list" style="margin-top:24px">{bl}</div>')}
  {card(f'<div class="label">Built-in traps</div><div class="list" style="margin-top:24px;gap:24px">{tl}</div>')}
</div>
""", "Open ONS data, so nothing confidential. The brief is chosen because it contains the traps worth showing: the colour that cannot flip on refresh, a field-parameter slicer, and a model with no date dimension. Paste it unchanged into Examples 1 to 3.")

# ---- 12-15 Examples (each has a slot for a screenshot of what came out) ---------------------------------
def example(n, title, setup, pro, con, notes):
    slot = (f'<div class="shot" data-slot="example-{n}">{icon("image", "muted", "icon-xl")}'
            f'<div class="label">Screenshot</div></div>')
    right = card(f'<div class="label">Setup</div><div class="body" style="margin-top:12px;line-height:1.4">{setup}</div>'
                 f'<div class="split"><div class="label ink-ok">Pro</div><div class="body" style="margin-top:12px;line-height:1.4">{pro}</div></div>'
                 f'<div class="split"><div class="label ink-warn">Con</div><div class="body" style="margin-top:12px;line-height:1.4">{con}</div></div>',
                 "roomy stretch")
    slide(f"""
<div class="eyebrow">03 &middot; Example {n}</div>
<div class="h2">{title}</div>
<div class="ex mt48"><div class="stack">{slot}</div>{right}</div>
""", notes)

example(1, "Plain chat", "A plain chat window. No tools, no model access.",
        "Zero setup. Fast for DAX.", "It guesses table and column names.",
        "Paste the brief unchanged. For a single measure this is genuinely the right tool. Watch for: good DAX and a sensible layout, and table and column names it could not know. Name the guessed ones out loud. Tomorrow it will not give the same answer. Screenshot slot: the chat output with the invented names highlighted.")
example(2, "Fabric skills", "Microsoft's Fabric skills. Same brief.",
        "Real file formats. A draft in minutes.", "Opt-in. No record of who approved.",
        "Concede loudly: Microsoft's skills are good, and for a prototype, a single measure, or a report you will never rebuild, they are the right answer. Watch for: real file formats, and a first draft far sooner than you could build one. What to notice is not quality but that it is advisory and opt-in. Show the version and date of the setup. Screenshot slot: the report the skill produced, opened in the Service.")
example(3, "MCP", "An agent connected to the live model. Same brief.",
        "Reads the real model.", "Can write to it. No approval step.",
        "Example 1 guessed names, this one looks them up. Watch for: it reads actual tables, measures and relationships, and it can also write to the real thing with nothing in the way. [Fill in after recording: what it got right, and what nothing stopped.] To decide before rehearsal: which MCP, and what auth it needs on stage. Screenshot slot: the agent reading the real model, with no workspace or tenant id visible.")
example(4, "Fabric skills + your own", "My skills, scripts, gates, and sign-offs.",
        "Tested, gated, with an audit trail.", "Upfront cost. Covers only what I encoded.",
        "Back to the terminal, tab 1. Demos A and C run live and offline. Demo A: check_phase_order blocks what-we-trade and passes the-balance. Demo C: run_pipeline until gates, five stages green, advisories, read R-SURVIVES-REFRESH aloud. Demo B (recorded, optional): the model half, same recipe. Say the cost out loud: it is overkill for one-off work. Where its grounding comes from: it builds offline against a cached snapshot of the live model, and the snapshot guard refuses a deploy if the snapshot is older than 7 days or no longer matches the live model. It does not create tables from raw files; it profiles and wires tables already in the model. Screenshot slot: the green pipeline run, or the refused build.")

# ---- 16 Map ----------------------------------------------------------------------------------------------
slide("""
<div class="eyebrow">03 &middot; Side by side</div>
<div class="h2">Grounding and control</div>
<div class="plot">
  <div class="box"></div><div class="vline"></div><div class="hline"></div>
  <div class="ax" style="left:0;top:0;width:192px;text-align:right">Grounded</div>
  <div class="ax" style="left:0;top:488px;width:192px;text-align:right">Blind</div>
  <div class="ax" style="left:208px;top:592px">Advisory</div>
  <div class="ax" style="right:0;top:592px">Blocking</div>
  <div class="pt" style="left:280px;top:400px"><b>1</b>Chat</div>
  <div class="pt" style="left:400px;top:196px"><b>2</b>Fabric skills</div>
  <div class="pt" style="left:320px;top:52px"><b>3</b>MCP</div>
  <div class="pt hot" style="left:1060px;top:72px"><b>4</b>Fabric skills + your own</div>
</div>
""", "Vertical: does the agent see the real model (grounding). Horizontal: can anything stop it being wrong (control). Chat is blind and unchecked. Fabric skills know the file formats but advise only. MCP is grounded live but unguarded. Fabric skills plus your own is the only one in the top right, and the gates are what put it there: they are plain scripts, so the same idea works on any of the four. Pro and con summary, row by row. Chat: zero setup and fast for DAX, but blind and unrepeatable. Fabric skills: grounded, quick start, but advisory, generic, no audit trail. MCP: live ground truth, but no gate on what it writes. Fabric skills plus your own: gated, tested, audited, but upfront cost and upkeep. Without the gates you have reports and a feeling. With them you have a number you can defend.")

# ---- 17 The mistake --------------------------------------------------------------------------------------
passed = "".join(card(f'<div class="row g24">{icon("circle-check", "ink-ok", "icon-xl")}<div class="h4">{t}</div></div>', "flat roomy") for t in ["Gates passed", "DAX passed", "Render matched the mockup"])
slide(f"""
<div class="eyebrow">03 &middot; The mistake</div>
<div class="h2">The mistake every check passed</div>
<div class="grid2 mt48" style="height:440px;align-items:stretch">
  <div class="stack g24" style="justify-content:space-between">{passed}</div>
  <div class="card" data-theme="dark" style="background:var(--dn-surface);display:flex;flex-direction:column;justify-content:center;padding:48px">
    <div class="h3">The slicer drove nothing.</div>
    <div class="body" style="margin-top:24px;line-height:1.4">Found by a person clicking it and noticing the chart did not move.</div>
  </div>
</div>
<div class="takeaway">Automated checks catch what they were written to catch. The interaction layer is still yours.</div>
""", "G-05 / BUG-02-001. The field-parameter slicer rendered, accepted a selection, and drove nothing at all. The engine never emitted the binding on the consuming chart, so the chart stayed on one fixed measure. Gates passed, DAX passed, render-match passed. A person clicking the slicer found it. Show the recording. Backup mistake: G-02b, a guessed custom-visual GUID that rendered blank cards; the fix was to capture the real shape, never guess.")

# ---- 18 What to check, and what stays yours --------------------------------------------------------------
def item(t, d):
    return f'<div class="line"><div class="h4">{t}</div><div class="small" style="margin-top:8px">{d}</div></div>'
checks = [("Measures resolve live", "Every one, against the real model."),
          ("The model matches the request", "Compare to what was asked, not to memory."),
          ("It survives a refresh", "Colours, sorts, and filters on new data.")]
yours = [("Approve the design", "Sign the mockup before anything is built."),
         ("Approve model changes", "The agent proposes. You decide."),
         ("Drive it in the Service", "Click the slicer. Hover the tooltip.")]
slide(f"""
<div class="eyebrow">03 &middot; Before you trust it</div>
<div class="h2">What to check, and what stays yours</div>
<div class="grid2 mt48" style="gap:96px;align-items:start">
  <div><div class="label ink-accent">A check that runs</div><div class="lines">{"".join(item(*c) for c in checks)}</div></div>
  <div><div class="label ink-violet">Yours</div><div class="lines">{"".join(item(*c) for c in yours)}</div></div>
</div>
""", "Does every measure resolve live. Does the model contain what was actually asked for. Does the report survive a refresh. Those can be checks that run. The three on the right are yours: approving the design, approving the model changes, and driving the thing in the Service. They are the parts where judgement is the work. What makes it reliable is not the prompt: it is a spec it can be checked against, a bar set before it starts, and gates it cannot walk past. I would rather have a tool that tells me it shipped with caveats than one that tells me it is done.")

# ---- 19 Close: who to find ---------------------------------------------------------------------------------
links = [("Web", "data-nova.io"), ("LinkedIn", "linkedin.com/in/prathy"), ("GitHub", "github.com/prathyusha-kamasani")]
rows = "".join(f'<div class="link"><div class="label">{k}</div><div class="mono-url">{v}</div></div>' for k, v in links)
slide(f"""
<div class="bye">
  <img class="portrait" src="assets/prathy.webp" alt="Prathy Kamasani">
  <div class="bye-text">
    <div class="h1c">Prathy Kamasani</div>
    <div class="body" style="margin-top:24px">Founder, Data Nova</div>
    <div class="small muted" style="margin-top:8px">Design-led data analytics with purpose</div>
    <div class="links">{rows}</div>
  </div>
</div>
""", "The close. Name, company and where to find me. Contact lines: data-nova.io, linkedin.com/in/prathy, github.com/prathyusha-kamasani. Check each before the day.", dark=True)

# ---- assemble --------------------------------------------------------------------------------------------
total = len(SLIDES)
parts = []
for i, (body, notes, dark) in enumerate(SLIDES, 1):
    theme = ' data-theme="dark"' if dark else ""
    parts.append(
        f'<section class="slide" id="s{i}"{theme}>{body}{CREDIT}<div class="pageno">{i:02d} / {total}</div>'
        f'<template class="notes">{notes}</template></section>')

html = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Agentic BI Development</title>
<link rel="stylesheet" href="styles.css">
<link rel="stylesheet" href="deck.css">
</head>
<body data-type-context="slide">
<div class="frame" id="frame">
{chr(10).join(parts)}
</div>
<div id="notes"></div>
<div id="hint">arrows: move &nbsp; N: notes &nbsp; F: fullscreen &nbsp; A: all slides</div>
<script src="vendor/lucide.min.js"></script>
<script src="deck.js"></script>
</body></html>
"""
Path(__file__).with_name("index.html").write_text(html)
print(f"wrote index.html: {total} slides")
