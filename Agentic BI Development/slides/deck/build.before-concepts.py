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
<div class="center-v">
  <div class="eyebrow">60-minute session</div>
  <div class="h1" style="margin-top:32px">Agentic BI Development</div>
  <div class="body mt32" style="max-width:1300px">What to check before you trust an agent's work</div>
</div>
""", "60 minutes. Who I am, the agenda, then concepts, then the trade balance report built three ways. The refrain for the hour: what would you have to check?", dark=True)

# ---- 2 About me ------------------------------------------------------------------------------------------
facts = ["Microsoft Data Platform MVP", "Founder of Data Nova, consulting on Microsoft Fabric and Power BI", "Runs the London Microsoft Fabric User Group"]
slide(f"""
<div class="bye">
  <img class="portrait" src="assets/prathy.webp" alt="Prathy Kamasani">
  <div class="bye-text">
    <div class="eyebrow">About me</div>
    <div class="h1c" style="margin-top:24px">Prathy Kamasani</div>
    <div class="lines" style="margin-top:40px">{"".join(f'<div class="line"><div class="body">{t}</div></div>' for t in facts)}</div>
  </div>
</div>
""", "Who I am, briefly. Microsoft Data Platform MVP. Data Nova is my consultancy, working on Microsoft Fabric and Power BI. I run the London Microsoft Fabric User Group. [Check these three lines are current before the day.]")

# ---- 3 Agenda --------------------------------------------------------------------------------------------
chapters = [("01", "What is BI development?", "Six steps from a question to a trusted report"),
            ("02", "What is agentic BI development?", "Where agents fit, starting from plain chat"),
            ("03", "Six building blocks", "Instructions, skills, hooks, loops, gates, MCP"),
            ("04", "Building the trade balance report", "Fabric skills, MCP, and my own")]
slide(f"""
<div class="eyebrow">Agenda</div>
<div class="agenda-list">{"".join(f'<div class="chap"><div class="chap-num">{n}</div><div><div class="h3">{t}</div><div class="small muted" style="margin-top:4px">{d}</div></div></div>' for n, t, d in chapters)}</div>
""", "Four parts. What BI development is. What agentic BI development is, starting from the plain chat everyone already uses. The six building blocks that make an agent trustworthy. Then one brief, worked through Fabric skills, MCP, and my own setup.", dark=True)


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

# ---- Section 02: what is agentic BI development ---------------------------------------------------------
section("02", "What is agentic BI development?", "An agent does the delivery work. You approve it.",
        "Set up the term before the demos. Agentic BI development is not a chatbot that answers questions about your data: it is an agent that does BI delivery work, using tools, checking its own results, and stopping for a person at the points that matter.")

agent_steps = [("Discover", "Drafts user stories from the requirements", "Sign off the requirements"),
               ("Model", "Profiles the model, proposes joins and measures", "Approve the model changes"),
               ("Build", "Writes the report files", "Sign the design before it builds"),
               ("Test", "Runs data, render and layout checks", "Drive the interactions"),
               ("Deploy", "Deploys through a gated pipeline", "Approve the release"),
               ("Govern", "Records who approved what, and when", "Accept the result")]
rows = "".join(f'<tr><td>{t}</td><td>{a}</td><td>{y}</td></tr>' for t, a, y in agent_steps)
slide(f"""
<div class="eyebrow">02 &middot; Agentic BI development</div>
<div class="h2">Who does what, step by step</div>
<table class="cmp who" style="margin-top:32px"><thead><tr><th>Step</th>
<th><span class="row g16">{icon("bot", "")}<span>The agent</span></span></th>
<th><span class="row g16">{icon("user-check", "ink-accent")}<span class="ink-accent">You</span></span></th></tr></thead><tbody>{rows}</tbody></table>
""", "The same six steps as two slides ago, split by who does the work. The agent drafts, profiles, writes, checks, deploys and records. You sign off the requirements, approve the model changes, sign the design before it builds, drive the interactions, approve the release, and accept the result. Every line in both columns is a step my own setup has today; the demos later show it.")

# ---- 5 Chat vs agentic -----------------------------------------------------------------------------------
chat_items = "".join(f'<div class="small">{t}</div>' for t in ["You ask", "It answers", "You copy and paste", "Nothing is checked"])
loop_items = "".join(f'<div class="small">{t}</div>' for t in ["Plan", "Act with tools", "Observe the result", "Try again, or stop"])
slide(f"""
<div class="eyebrow">02 &middot; Agentic</div>
<div class="h2">How chat differs from an agent</div>
<div class="grid2 mt48" style="grid-template-columns:5fr 6fr;align-items:stretch">
  {card(f'<div class="h4">Chat</div><div class="list" style="margin-top:32px;gap:24px">{chat_items}</div>')}
  <div class="card inkcard">
    <div class="h4">Agentic</div>
    <div class="list" style="margin-top:32px;gap:24px">{loop_items}</div>
    <div class="small rose" style="margin-top:24px">A human approves at the gates</div>
  </div>
</div>
""", "Chat: you ask, it answers, you copy and paste. Agentic: a model, plus tools, plus a loop, plus a human. It acts, looks at what happened, and tries again. That loop is the power and the risk: it can fix its own errors, and it can confidently build on its own mistake.")

# ---- Examples: the helper, then Example 1 (plain chat), shown early as the way everyone starts ---------------------------------
def example(n, title, setup, pro, con, notes, videos=None, eyebrow=None, rates=None):
    if videos:  # plays in order; P plays or pauses, the native controls also work
        slot = (f'<video class="clip" data-slot="example-{n}" data-playlist="{",".join(videos)}" data-rates="{",".join(str(r) for r in (rates or [1] * len(videos)))}" src="{videos[0]}#t=0.5" '
                f'controls preload="auto" playsinline></video>')
    else:
        slot = (f'<div class="shot" data-slot="example-{n}">{icon("image", "muted", "icon-xl")}'
                f'<div class="label">Screenshot</div></div>')
    right = card(f'<div class="label">Setup</div><div class="body" style="margin-top:12px;line-height:1.4">{setup}</div>'
                 f'<div class="split"><div class="label ink-ok">Pro</div><div class="body" style="margin-top:12px;line-height:1.4">{pro}</div></div>'
                 f'<div class="split"><div class="label ink-warn">Con</div><div class="body" style="margin-top:12px;line-height:1.4">{con}</div></div>',
                 "roomy stretch")
    slide(f"""
<div class="eyebrow">{eyebrow or f"04 &middot; Example {n}"}</div>
<div class="h2">{title}</div>
<div class="ex mt48{' wide' if videos else ''}"><div class="stack">{slot}</div>{right}</div>
""", notes)

example(1, "Plain chat", "Claude Code, no skills, no access to the model",
        "Zero setup, fast for DAX", "Guesses table and column names",
        "Two clips play in order. First (22s): asking what is preinstalled; no skills are configured. Then (92s): prompt 1 asks for a trade balance measure and a card colour measure with no model; it invents 'Trade'[Exports] and 'Trade'[Imports]. Prompt 2 pastes the real tables and columns and it rewrites them correctly. For a single measure this is genuinely the right tool. The catch: I had to paste the schema by hand, and it goes stale when the model changes. Press P to play or pause.",
        videos=["media/ClaudeNoSkills.mov", "media/Demo1_chat.mov"], eyebrow="02 &middot; Starting point")
# ---- Example 1, side by side ---------------------------------------------------------------------------
p1 = """Trade Balance =
SUM(<mark>'Trade'[Exports]</mark>) - SUM(<mark>'Trade'[Imports]</mark>)"""
p2 = """Trade Balance =
VAR Exports =
  CALCULATE(
    SUM('Trade Total Monthly'[Value GBP Millions]),
    Flow[Direction] = "Export"
  )
VAR Imports =
  CALCULATE(
    SUM('Trade Total Monthly'[Value GBP Millions]),
    Flow[Direction] = "Import"
  )
RETURN
  Exports - Imports"""
slide(f"""
<div class="eyebrow">02 &middot; Starting point</div>
<div class="h2">Without the schema, then with it</div>
<div class="grid2 mt32" style="gap:32px;align-items:stretch">
  <div class="card codecard"><div class="label">Prompt 1: no model</div><pre class="code">{p1}</pre></div>
  <div class="card codecard"><div class="label">Prompt 2: real names pasted in</div><pre class="code">{p2}</pre></div>
</div>
""", "Left: prompt 1, the ask on its own. The highlighted names, 'Trade'[Exports] and 'Trade'[Imports], do not exist in the model: it invented them. Right: prompt 2, after pasting the real tables and columns. It now sums Value GBP Millions and splits exports from imports on Flow[Direction]. Only the Trade Balance measure is shown. The Balance Card Colour measure came out the same both times (IF the balance is 0 or more, \"#2E7D32\", else \"#C62828\"), because it does not depend on any names. The fix worked, but I had to paste the schema by hand, and it goes stale the moment the model changes. Note: the Flow[Direction] values (Export, Import) in the right-hand answer are the chat's assumption, not checked against the data. Code is shown as pasted, with the indentation in the right-hand answer tidied to fit.")

# ---- 6 Which bits ----------------------------------------------------------------------------------------
def col(ic, cls, head, items):
    li = "".join(f'<div class="small">{t}</div>' for t in items)
    return card(f'<div class="h4 {cls}" style="min-height:48px">{head}</div><div class="list mt24" style="margin-top:24px">{li}</div>')
slide(f"""
<div class="eyebrow">02 &middot; What agents can do</div>
<div class="h2">Which bits can an agent do?</div>
<div class="grid3 mt48" style="align-items:stretch">
  {col("circle-check", "", "Agent does it", ["Profile the model", "Relationships, measures", "Build the report files", "Data and render tests", "Gated deploy"])}
  {col("pencil-line", "ink-violet", "Agent drafts", ["Requirements and discovery", "Page layout and design", "Fixes for what tests find"])}
  {col("user-check", "ink-accent", "You decide", ["Sign-off and acceptance", "Interaction testing", "What good means"])}
</div>
""", "Teal is the agent, violet is you. The agent does profiling a model, relationships, measures, building report files, data and render tests, and gated deploy. It drafts requirements and layout, and you decide. Interaction testing and sign-off stay with a person. One honest caveat: it can propose and wire a star schema from imported tables, but it does not create tables from raw files. It profiles and wires tables already in the model. Do not imply more.")

# ---- 7 Section: ideas ------------------------------------------------------------------------------------
section("03", "Six building blocks", "Instructions, skills, hooks, loops, gates, MCP",
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
<div class="eyebrow">03 &middot; The building blocks</div>
<div class="h2">Six building blocks, and where each lives</div>
<table class="cmp tight vocab" style="margin-top:32px"><thead><tr><th>Block</th><th>Kind</th><th>Where it lives</th><th>What it does</th></tr></thead><tbody>{tr}</tbody></table>
""", "Instructions (AGENTS.md, or CLAUDE.md for Claude): standing rules read every session. Skills: a repeatable recipe loaded when the task matches. MCP: live typed access to a tool or data source. Hooks: run on every commit whether or not the agent remembers. Loops: iterate until a check passes, not until the agent feels done. Gates: a step that refuses to advance without a pass or a human signature. Show the 'where it lives' column only as glimpses, 20 to 30 seconds each, from the repo. Check what is on screen before projecting: no client names. Do not open the top of CLAUDE.md in the demo repo, it carries the extract banner; use AGENTS.md. The pre-commit file has 28 named hooks.")

# ---- 9 Advisory or blocking ------------------------------------------------------------------------------
slide(f"""
<div class="eyebrow">03 &middot; The hinge</div>
<div class="h2">Advisory or blocking?</div>
<div class="grid2 mt48" style="align-items:stretch">
  <div class="card">
    <div class="h4 ink-violet">Advisory</div>
    <div class="body strong" style="margin-top:24px">Instructions and skills</div>
    <div class="body" style="margin-top:16px;line-height:1.4">The agent decides whether to read them. Nothing fails if it does not.</div>
  </div>
  <div class="card inkcard">
    <div class="h4 rose">Blocking</div>
    <div class="body strong" style="margin-top:24px">Hooks and gates</div>
    <div class="body" style="margin-top:16px;line-height:1.4">The agent cannot walk past them. A failing check stops the build.</div>
  </div>
</div>
<div class="takeaway">A knowledge file is advice. Any tool can skip it, on any run. A check cannot be skipped.</div>
""", "Instructions and skills are advisory: the agent can ignore them. Hooks and gates are blocking: it cannot. That is the hinge for everything that follows. Each example sits at a different point on advisory versus blocking, and on blind versus grounded. Evidence from my own history: a cold Copilot session with all the knowledge files present shipped a bad report and deployed it by the wrong path. Any agent would have done the same; the files were the weak link, not the tool. The diagnosis was four words: the knowledge was opt-in, advisory, tool-specific, runtime-bypassable.")

# ---- 10 Section: building the trade balance report -------------------------------------------------------------------------------
section("04", "Building the trade balance report", "Same requirement every time, so the comparison is fair.",
        "For each example use the same four beats: setup, brief in, what came out, what we had to check. Do not declare a winner until the comparison slide.")

# ---- 11 The brief ----------------------------------------------------------------------------------------
build = ["Balance card that changes colour from surplus to deficit", "Monthly trend of exports, imports and the balance",
         "Breakdown by partner country or commodity", "Slicer that switches the trend between measures"]
done = ["12 months to March 2026: exports £937.0bn, imports £980.4bn", "Card colour from a measure, not a fixed colour",
        "The slicer changes the plotted measure", "Every field it uses exists in the model"]
also = ["Who it is for", "The model, its tables and its rules", "One page, theme colours, native visuals",
        "What is out of scope", "What to hand back, with evidence", "Ask before guessing"]
def brief_card(label, items, cls=""):
    li = "".join(f'<div class="small">{t}</div>' for t in items)
    return card(f'<div class="label {cls}">{label}</div><div class="list" style="margin-top:24px;gap:20px">{li}</div>')
slide(f"""
<div class="eyebrow">04 &middot; The brief</div>
<div class="h2">UK trade, the balance</div>
<div class="grid3 mt48" style="align-items:stretch">
  {brief_card("What to build", build)}
  {brief_card("Done means", done, "ink-accent")}
  {brief_card("Also in the brief", also)}
</div>
""", "Every tool in this section gets the same brief, pasted unchanged. The full text is in demos/BRIEF.md. It follows Anthropic's own guidance for briefing an agent: who it is for and why, the exact model and tables, what to build, what done means, the constraints, what is out of scope, what to hand back, and to ask before guessing. The things that went wrong in earlier runs are stated openly as checks: the card colour must come from a measure so it flips after a refresh, the slicer must change the plotted measure, and every field must exist in the model. The figures are the published gov.uk UK Trade in Numbers totals for the 12 months to March 2026. Open ONS data, so nothing confidential.")

example(2, "Fabric skills", "Microsoft's Fabric skills, same brief",
        "Real file formats, a draft in minutes", "Opt-in, no record of who approved",
        "Concede loudly: Microsoft's skills are good, and for a prototype, a single measure, or a report you will never rebuild, they are the right answer. Watch for: real file formats, and a first draft far sooner than you could build one. What to notice is not quality but that it is advisory and opt-in. Show the version and date of the setup. Two clips play in order. First (51s, normal speed): installing Microsoft's powerbi-authoring plugin and asking what skills it has. Then a slow scroll through the whole session (5 minutes 20 seconds, 3 lines a second): it reads the brief, finds the model, queries it, writes a spec you approve, builds the report files, validates them, previews in the Service, and publishes to the Fabric Friday Demo workspace folder 02 Fabric skills. Result against the brief: one of four done checks passed. Step by step is in demos/02-fabric-skills/run-steps.md. Press P to play or pause; the video controls also set speed.",
        videos=["media/FabricSkill-1.m4v", "media/fabric-skills-scroll.mov"], rates=[1, 1])

example(3, "MCP", "VS Code with GitHub Copilot, connected to Microsoft's hosted Power BI authoring MCP",
        "Reads the real model", "Can write to it, no approval step",
        "VS Code, GitHub Copilot in agent mode, Microsoft's hosted Power BI authoring MCP server (signed in with an az token). The clip is a slow scroll through the whole chat (1 minute 54 seconds, about 3 lines a second). What happens: it connects to SM_UKT_Import through MCP, runs DAX queries and gets the 12-month figures right (exports 936.967, imports 980.369, balance -43.402 GBP bn). It found the connection read-only, so it could not add a field parameter and asked how to handle the slicer. The MCP server cannot create report pages, so Copilot wrote the report as PBIP files itself, locally. It could not publish them: by its own account, the MCP tools cannot create or publish reports, and the Fabric import menu does not take PBIP. The item UK Trade Balance mcp in the Fabric Friday Demo folder 03 MCP is a Save a copy of the report already in the workspace (the Fabric skills one), made in the browser, not the report Copilot built. Point to make: MCP gave it the real model and the right numbers; it could not deliver a report. Press P to play or pause.",
        videos=["media/mcp-chat-scroll.mov"], rates=[1])

example(4, "Fabric skills + your own", "My skills, scripts, gates, and sign-offs",
        "Tested, gated, with an audit trail", "Upfront cost, covers only what I encoded",
        "Back to the terminal, tab 1. Demos A and C run live and offline. Demo A: check_phase_order blocks what-we-trade and passes the-balance. Demo C: run_pipeline until gates, five stages green, advisories, read R-SURVIVES-REFRESH aloud. Demo B (recorded, optional): the model half, same recipe. Say the cost out loud: it is overkill for one-off work. Where its grounding comes from: it builds offline against a cached snapshot of the live model, and the snapshot guard refuses a deploy if the snapshot is older than 7 days or no longer matches the live model. It does not create tables from raw files; it profiles and wires tables already in the model. Screenshot slot: the green pipeline run, or the refused build.")

example("4b", "Then I let it run alone", "One brief, every decision delegated",
        "Brief to client deploy, no questions", "5 hours, 10 engine gaps",
        "A different report on the same model: trade stripes, one column per month for the whole history. I wrote the brief, granted the delegation and did not touch it again. The clip is a replay of the whole session from its saved log (6 minutes 53 seconds, about 10 lines a second): Discovery in 19 minutes, Design in 22, the first canary at 1 hour 8, then the render-fix loop the live-render check drove (the stripes first came out as 47 wide columns with a scrollbar), QA, ship approval and the client deploy. 5 hours 11 minutes on the clock, about 3 hours 9 minutes of work after a 2 hour usage-limit pause. Every engine limit it met, it logged instead of patching: 10 gaps, each fixed by a separate builder as its own pull request for me to review. Be honest about one thing: the delegate was asked for a different model but was served the drafter's own model; only the second checks were independent. That is now fixed in the tool. Press P to play or pause.",
        videos=["media/stripes-session-scroll.mov"], rates=[1], eyebrow="04 &middot; Example 4, run alone")

# ---- 16 Map ----------------------------------------------------------------------------------------------
slide("""
<div class="eyebrow">04 &middot; Side by side</div>
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
<div class="eyebrow">04 &middot; The mistake</div>
<div class="h2">All checks passed, and the slicer was broken</div>
<div class="grid2 mt48" style="height:360px;align-items:stretch">
  <div class="stack g16" style="justify-content:space-between">{passed}</div>
  <div class="card inkcard" style="display:flex;flex-direction:column;justify-content:center;padding:48px">
    <div class="h3">The slicer did not filter the chart.</div>
    <div class="body" style="margin-top:24px;line-height:1.4">A person found it by clicking the slicer and noticing the chart did not move.</div>
  </div>
</div>
<div class="takeaway">Interaction testing is still a manual job.</div>
""", "G-05 / BUG-02-001. The field-parameter slicer rendered, accepted a selection, and drove nothing at all. The engine never emitted the binding on the consuming chart, so the chart stayed on one fixed measure. Gates passed, DAX passed, render-match passed. A person clicking the slicer found it. Show the recording. Backup mistake: G-02b, a guessed custom-visual GUID that rendered blank cards; the fix was to capture the real shape, never guess.")

# ---- 18 What to check, and what stays yours --------------------------------------------------------------
def item(t, d):
    return f'<div class="line"><div class="h4">{t}</div><div class="small" style="margin-top:8px">{d}</div></div>'
checks = [("Measures resolve live", "Every one, against the real model"),
          ("The model matches the request", "Checked against the request, not memory"),
          ("It survives a refresh", "Colours, sorts, and filters on new data")]
yours = [("Approve the design", "Sign the mockup before anything is built"),
         ("Approve model changes", "The agent proposes, you decide"),
         ("Drive it in the Service", "Click the slicer, hover the tooltip")]
slide(f"""
<div class="eyebrow">04 &middot; Before you trust it</div>
<div class="h2">What to check, and what you do yourself</div>
<div class="grid2 mt48" style="gap:96px;align-items:start">
  <div><div class="label">A check that runs</div><div class="lines">{"".join(item(*c) for c in checks)}</div></div>
  <div><div class="label ink-accent">You</div><div class="lines">{"".join(item(*c) for c in yours)}</div></div>
</div>
""", "Does every measure resolve live. Does the model contain what was actually asked for. Does the report survive a refresh. Those can be checks that run. The three on the right are yours: approving the design, approving the model changes, and driving the thing in the Service. They are the parts where judgement is the work. What makes it reliable is not the prompt: it is a spec it can be checked against, a bar set before it starts, and gates it cannot walk past. I would rather have a tool that tells me it shipped with caveats than one that tells me it is done.")

# ---- 19 Close: who to find ---------------------------------------------------------------------------------
links = [("Web", "data-nova.io"), ("LinkedIn", "linkedin.com/in/prathy"), ("GitHub", "github.com/prathyusha-kamasani")]
rows = "".join(f'<div class="link"><div class="label">{k}</div><div class="mono-url">{v}</div></div>' for k, v in links)
slide(f"""
<div class="bye">
  <div class="bye-text">
    <div class="eyebrow">Thank you</div>
    <div class="h1c" style="margin-top:24px">Prathy Kamasani</div>
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
    theme = ' data-surface="warm"' if dark else ""
    cls = "slide opener" if dark else "slide"
    parts.append(
        f'<section class="{cls}" id="s{i}"{theme}>{body}{CREDIT}<div class="pageno">{i:02d} / {total}</div>'
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
<div id="hint">arrows: move &nbsp; N: notes &nbsp; P: play video &nbsp; F: fullscreen &nbsp; A: all slides</div>
<script src="vendor/lucide.min.js"></script>
<script src="deck.js"></script>
</body></html>
"""
Path(__file__).with_name("index.html").write_text(html)
print(f"wrote index.html: {total} slides")
