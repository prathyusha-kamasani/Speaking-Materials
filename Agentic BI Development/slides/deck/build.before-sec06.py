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
            ("02", "Working with an agent", "Context, skills, rules, algorithms, loops, hooks, gates"),
            ("03", "Agent roles", "Operator, builder, orchestrator, and you"),
            ("04", "Building the trade balance report", "Chat, Fabric skills, MCP, my own, full delegation"),
            ("05", "How I built the tool", "Specs, engine, checks, prompts, deliverables")]
slide(f"""
<div class="eyebrow">Agenda</div>
<div class="agenda-list dense">{"".join(f'<div class="chap"><div class="chap-num">{n}</div><div><div class="h3">{t}</div><div class="small muted" style="margin-top:4px">{d}</div></div></div>' for n, t, d in chapters)}</div>
""", "Four parts so far. What BI development is. Working with an agent: the building blocks you use to tell it how you work. The roles an agent plays, and where you stay in the loop. Then one brief, worked through chat, Fabric skills, MCP, my own setup, and full delegation.", dark=True)


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

# ---- Section 02: working with an agent -------------------------------------------------------------------
section("02", "Working with an agent", "A capable graduate on day one",
        "Before any tool: how to think about working with an agent. Then the building blocks you use to tell it how you work.")

grad = [("graduation-cap", "", "Knows a lot", "DAX, Power BI, Fabric, every public document"),
        ("building-2", "", "Not how you work", "Your model, your names, your rules, your sign-offs"),
        ("list-checks", "ink-accent", "So you give it", "Context, recipes, limits, and someone who checks")]
slide(f"""
<div class="eyebrow">02 &middot; Working with an agent</div>
<div class="h2">Treat it like a new graduate</div>
<div class="grid3 mt48" style="align-items:stretch">{"".join(card(f'{icon(ic, cls, "icon-xl")}<div class="h4" style="margin-top:32px">{t}</div><div class="small" style="margin-top:16px">{d}</div>', "roomy") for ic, cls, t, d in grad)}</div>
""", "A new graduate joins knowing a lot: languages, tools, the public documentation. What they do not know is how you work here: your model, your names, your rules, who signs off what. Nobody expects them to guess. You tell them, you give them recipes, you set limits, and someone checks their work. An agent is the same, and the rest of this section is the set of ways you tell it.")

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

# ---- 02 The building blocks, and where each lives in my setup --------------------------------------------
rows = [("Context", "Advisory", "CLAUDE.md, AGENTS.md", "Standing rules for every session"),
        ("Skills", "Advisory", ".claude/skills/ (10)", "A repeatable recipe for one job"),
        ("Rules", "Advisory", "PRINCIPLES.md", "What good looks like, in words"),
        ("Algorithms", "Structure", "algorithms/ (19)", "The steps of each phase"),
        ("Loops", "Blocking", "render-fix and QA loops", "Repeat until a check passes"),
        ("Hooks", "Blocking", "pre-commit (29), edit hooks", "Refuse one action, on an event"),
        ("Gates", "Blocking", "the rail: 44 steps", "No sign-off, no next phase"),
        ("MCP", "Reach", "an MCP server", "Live access to tools and data")]
kind_cls = {"Advisory": "ink-violet", "Reach": "muted", "Blocking": "ink-accent", "Structure": ""}
tr = "".join(f'<tr><td>{a}</td><td><span class="label {kind_cls[b]}">{b}</span></td><td class="mono nowrap">{c}</td><td>{d}</td></tr>' for a, b, c, d in rows)
slide(f"""
<div class="eyebrow">02 &middot; The building blocks</div>
<div class="h2">The building blocks, and where each lives</div>
<table class="cmp tight vocab vtight" style="margin-top:16px"><thead><tr><th>Block</th><th>Kind</th><th>In my setup</th><th>What it does</th></tr></thead><tbody>{tr}</tbody></table>
""", "Context: CLAUDE.md for Claude, AGENTS.md for any tool, copilot-instructions.md for GitHub Copilot; standing rules read every session. Skills: public ones, like Microsoft's Fabric skills, or your own; mine are ten, in .claude/skills. Rules: what good looks like, written down; on their own they are advice. Algorithms: the steps of each phase, in order, some of them in parallel; mine are nineteen specs. Loops: repeat until a check passes, not until the agent feels done. Hooks: fire on an event and refuse that one action; twenty-nine run on every commit. Gates: a step that will not advance without evidence or a signature. MCP: live, typed access to a tool or data. Show the third column live in VS Code, 20 seconds each. Check what is on screen before projecting: no client names.")

# ---- 02 Advisory, hook or gate -----------------------------------------------------------------------------
kinds = [("Advisory", "ink-violet", "Context, skills, rules", "The agent decides whether to follow them. Nothing fails if it does not.", "", "card"),
         ("Hook", "ink-accent", "Fires on an event", "A commit or an edit. It refuses that one action.", "An edit to the engine from a report branch", "card"),
         ("Gate", "rose", "A checkpoint in the flow", "No evidence or signature, no next phase.", "No signed design, no build", "card inkcard")]
def kind_card(name, cls, head, body, ex, klass):
    exl = f'<div class="split"><div class="label">Example</div><div class="small" style="margin-top:12px">{ex}</div></div>' if ex else ""
    return (f'<div class="{klass}"><div class="h4 {cls}">{name}</div><div class="body strong" style="margin-top:24px">{head}</div>'
            f'<div class="small" style="margin-top:16px;line-height:1.4">{body}</div>{exl}</div>')
slide(f"""
<div class="eyebrow">02 &middot; The hinge</div>
<div class="h2">Advisory, hook or gate?</div>
<div class="grid3 mt48" style="align-items:stretch">{"".join(kind_card(*k) for k in kinds)}</div>
<div class="takeaway">The prompt said not to edit the engine, and it did. Now a hook refuses the edit.</div>
""", "Context, skills and rules are advisory: the agent can skip them on any run. A hook fires on an event, a commit or an edit, and refuses that one action. A gate is a checkpoint in the flow: the next phase will not start without evidence or a signature. The story at the bottom is real: in a delegated run the prompt said never edit the engine, and the agent edited it anyway. The fix was not a stronger prompt. It was a hook that refuses an engine edit from a report branch. Every example later sits somewhere between advisory and blocking.")

# ---- 02 An algorithm for each phase -------------------------------------------------------------------------
phases = [("01", "Discovery", "13 steps", "Requirements, stories, feasibility, profile, proof points", "Discovery gate"),
          ("02", "Design", "15 steps", "Contract, layout, sketch, visuals, mockup", "Design gate"),
          ("03", "Develop", "2 steps", "Build, offline gates", ""),
          ("04", "Verify and QA", "6 steps", "Canary, live render, render review, QA", "QA gate"),
          ("05", "Ship", "5 steps", "Ship approval, client deploy, deliverable pack", "Ship approval"),
          ("06", "Govern", "3 steps", "Audit trail, tidy, owner acceptance", "Owner acceptance")]
pc = "".join(card(f'<div class="label">{n} &middot; {c}</div><div class="h4" style="margin-top:16px">{t}</div><div class="small" style="margin-top:16px">{d}</div>'
                  + (f'<div class="small ink-accent strong" style="margin-top:12px">Gate: {g}</div>' if g else '')) for n, t, c, d, g in phases)
slide(f"""
<div class="eyebrow">02 &middot; Algorithms</div>
<div class="h2">An algorithm for each phase</div>
<div class="grid3" style="margin-top:32px;grid-template-rows:repeat(2, 1fr);gap:32px">{pc}</div>
""", "This is the rail: 44 steps across six phases, each phase written down as an algorithm the agent follows in order. Some steps run in parallel: while one model reads a draft and decides, the agent prepares the next draft; a decision and its second check run side by side. Five steps are gates, named at the bottom of each card: the phase does not finish until its gate is decided. Show the rail live in Mission Control if there is time.")

# ---- Section 03: agent roles --------------------------------------------------------------------------------
section("03", "Agent roles", "Operator, builder, orchestrator, and you",
        "Who does what once the building blocks are in place. Four roles; the same model can play more than one, but never at the same time.")

roles = [("play", "", "Operator", "Runs the tool on a brief", "Writes only the deliverables. Logs what the tool cannot do.", "card"),
         ("wrench", "", "Builder", "Changes the tool", "On its own branch, with tests. You review each change.", "card"),
         ("network", "", "Orchestrator", "Plans and hands out work", "Sends each decision to a delegate and a checker, in order.", "card"),
         ("user-check", "rose", "Human gate", "Signs what matters", "Decides what may be delegated. Keeps the client deploy.", "card inkcard")]
slide(f"""
<div class="eyebrow">03 &middot; Agent roles</div>
<div class="h2">Four roles</div>
<div class="grid4 mt48">{"".join(f'<div class="{k}">{icon(ic, c or "ink-accent", "icon-xl")}<div class="h4" style="margin-top:32px">{n}</div><div class="body strong" style="margin-top:16px;line-height:1.3">{h}</div><div class="small" style="margin-top:16px;line-height:1.4">{d}</div></div>' for ic, c, n, h, d, k in roles)}</div>
""", "Operator: runs the tool on a brief and writes only the deliverables; when the tool cannot do something it logs a gap and uses the nearest supported option. Builder: changes the tool itself, on its own branch, with tests; every change is a pull request I review. Orchestrator: plans the work and hands each decision to a delegate and a second checker, in the order the rail requires. The human gate: decides what may be delegated, signs what matters, and keeps the one thing I never delegate, the client deploy. In the last run, the operator logged ten gaps and ten builders fixed them while it carried on.")

# ---- 03 Who does what -----

agent_steps = [("Discover", "Drafts user stories from the requirements", "Sign off the requirements"),
               ("Model", "Profiles the model, proposes joins and measures", "Approve the model changes"),
               ("Build", "Writes the report files", "Sign the design before it builds"),
               ("Test", "Runs data, render and layout checks", "Drive the interactions"),
               ("Deploy", "Deploys through a gated pipeline", "Approve the release"),
               ("Govern", "Records who approved what, and when", "Accept the result")]
rows = "".join(f'<tr><td>{t}</td><td>{a}</td><td>{y}</td></tr>' for t, a, y in agent_steps)
slide(f"""
<div class="eyebrow">03 &middot; Roles</div>
<div class="h2">Who does what, step by step</div>
<table class="cmp who" style="margin-top:32px"><thead><tr><th>Step</th>
<th><span class="row g16">{icon("bot", "")}<span>The agent</span></span></th>
<th><span class="row g16">{icon("user-check", "ink-accent")}<span class="ink-accent">You</span></span></th></tr></thead><tbody>{rows}</tbody></table>
""", "The same six steps as two slides ago, split by who does the work. The agent drafts, profiles, writes, checks, deploys and records. You sign off the requirements, approve the model changes, sign the design before it builds, drive the interactions, approve the release, and accept the result. Every line in both columns is a step my own setup has today; the demos later show it.")

# ---- 03 The flow -------------------------------------------------------------------------------------------
def fnode(t, d, cls=""):
    return f'<div class="fnode {cls}"><div class="small strong">{t}</div><div class="label" style="margin-top:8px">{d}</div></div>'
arrow = f'<div class="farrow">{icon("arrow-right", "muted")}</div>'
main = arrow.join([fnode("Requirement", "You", "you"), fnode("Drafts and improves it", "Operator"),
                   fnode("Approve or question", "Gate", "gate"), fnode("Builds and checks", "Operator"),
                   fnode("Canary deploy", "Operator"), fnode("Client deploy", "You", "you")])
side = arrow.join([fnode("Tool cannot do it", "Operator"), fnode("Gap logged", "Operator"),
                   fnode("Fix on a branch", "Builder"), fnode("Review the change", "You", "you")])
slide(f"""
<div class="eyebrow">03 &middot; The flow</div>
<div class="h2">How a report gets made</div>
<div class="flow mt48">{main}</div>
<div class="small muted" style="margin-top:24px;margin-left:640px">{icon("rotate-ccw", "muted")} A question sends it back to the operator, until approved</div>
<div class="label" style="margin-top:56px">Alongside</div>
<div class="flow" style="margin-top:16px">{side}</div>
""", "Read it left to right. I write the requirement. The operator drafts it properly: stories, acceptance tests, the data it needs. At the gate it is approved or questioned; a question sends it back to the operator, and that loop runs until it is approved. The same loop repeats at every gate: design, QA, ship. The operator builds, checks and deploys to a canary. The client deploy stays with me. Underneath, the second lane: whenever the tool cannot do something, the operator logs a gap and carries on, and a builder fixes it separately as a change I review.")

# ---- 03 Who holds the gate -----------------------------------------------------------------------------------
slide(f"""
<div class="eyebrow">03 &middot; The gate</div>
<div class="h2">Who holds the gate?</div>
<div class="grid2 mt48" style="align-items:stretch">
  {card('<div class="h4">Human gate</div><div class="body strong" style="margin-top:24px">You sign every gate</div><div class="small" style="margin-top:16px;line-height:1.4">Discovery, design, QA, ship and acceptance. Slow, and you are always in the loop.</div>', "roomy")}
  <div class="card inkcard roomy">
    <div class="h4 rose">Full delegation</div>
    <div class="body strong" style="margin-top:24px">A second model decides, a third checks</div>
    <div class="small" style="margin-top:16px;line-height:1.4">You keep one gate: the deploy to the client. You read the decisions afterwards.</div>
  </div>
</div>
""", "Two ways to run the same flow. With a human gate, I sign every gate myself: safe, but I am in the loop all day. With full delegation, a different model decides each gate and a third model checks it, and I keep one gate, the client deploy, and read the recorded decisions afterwards. Be honest here: in my first delegated runs the deciding model was meant to be different but was quietly served the drafting model; only the checks were independent. The tool now proves which model answered and refuses a decision when it is the drafter's own. That is the last example in the next section.")

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

# ---- Section 05: how I built the tool -------------------------------------------------------------------------
section("05", "How I built the tool", "Specs first, then the engine, then the checks",
        "How the setup behind Example 4 is put together, so you can build your own version. Show the parts live in VS Code; every slide has a screenshot fallback.")

# ---- 05 One spine ---------------------------------------------------------------------------------------------
spine = arrow.join([fnode("Specs", "algorithms/ (19)"), fnode("Engine", "One generator"), fnode("Report files", "Pinned schemas"),
                    fnode("Checks", "Hooks, rail, pipeline", "gate"), fnode("Deploy", "run_pipeline only", "you")])
feeds = arrow.join([fnode("Knowledge", "Visuals, tricks, gotchas"), fnode("Microsoft's own", "CLI validator, sample report"),
                    fnode("Skills", "10 recipes for agents"), fnode("Engagement", "Brief, model, decisions")])
slide(f"""
<div class="eyebrow">05 &middot; Architecture</div>
<div class="h2">One spine</div>
<div class="flow mt48">{spine}</div>
<div class="label" style="margin-top:56px">What feeds it</div>
<div class="flow" style="margin-top:16px">{feeds}</div>
<div class="takeaway">A fix goes in the spec or the engine, never in a report file.</div>
""", "Every behaviour starts as a written spec, an algorithm. One engine turns a report config into Power BI report files, always the same way, and validates them against pinned schemas. Checks sit around it: hooks on every commit, the rail of gates, and the pipeline. The only way out is run_pipeline. Feeding it: a knowledge base of visuals and tricks, Microsoft's own CLI validator and sample report as ground truth, ten skills that tell an agent how to do each job, and the engagement itself, the brief, the model and every decision. The rule at the bottom is the one that makes it compound: when a report is wrong, the fix goes where it helps every future report.")

# ---- 05 The parts, live -----------------------------------------------------------------------------------------
parts = [("Skills", ".claude/skills/render-review/", "The checklist a second model uses on a live page"),
         ("Algorithms", "algorithms/ALG-TEST.md", "What each test tier proves, and what blocks"),
         ("Rules", "PRINCIPLES.md", "Twelve principles, from one spine to the render is the quality bar"),
         ("Hooks", ".pre-commit-config.yaml", "29 hooks, including the edit guard on report branches"),
         ("Gates", "scripts/step_evidence.py", "The rail: 44 steps, each with its evidence"),
         ("Engine", "engine/builders/", "One builder per visual family")]
tr = "".join(f'<tr><td>{a}</td><td class="mono nowrap">{b}</td><td>{c}</td></tr>' for a, b, c in parts)
slide(f"""
<div class="eyebrow">05 &middot; In VS Code</div>
<div class="h2">The parts, and what to open</div>
<table class="cmp tight vtight" style="margin-top:24px"><thead><tr><th>Part</th><th>Open</th><th>What you will see</th></tr></thead><tbody>{tr}</tbody></table>
""", "Switch to VS Code and open each file for 20 to 30 seconds. Skills: the render-review skill, a checklist a model that did not build the page uses to judge it. Algorithms: ALG-TEST, what each test tier proves. Rules: PRINCIPLES.md. Hooks: the pre-commit config, then the edit guard that stops a report branch editing the engine. Gates: step_evidence, the rail, every step with the evidence that proves it. Engine: one builder per visual family. Before projecting, check no client name is on screen. If VS Code misbehaves, the screenshots are in the backup slides.")

# ---- 05 Testing -------------------------------------------------------------------------------------------------
tests = [("0 &middot; Repo", "The engine still behaves", "About 3,000 tests on every commit"),
         ("1 &middot; Contract", "The config matches the design", "Blocking rules, Microsoft's validator"),
         ("2 &middot; Data", "Every measure resolves, with sane values", "Queried live after each deploy"),
         ("3 &middot; Render", "Every text whole, the page judged", "Live page measured, reviewed by another model"),
         ("4 &middot; Interaction", "Clicks and hovers do what was promised", "A headless QA runner, a person as fallback")]
tr = "".join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in tests)
slide(f"""
<div class="eyebrow">05 &middot; Testing</div>
<div class="h2">Five layers, cheapest first</div>
<table class="cmp tight vtight" style="margin-top:24px"><thead><tr><th>Layer</th><th>Proves</th><th>How</th></tr></thead><tbody>{tr}</tbody></table>
""", "Each layer catches what the one before cannot. Repo: about three thousand tests run on every commit. Contract: the config is checked against the design and against Microsoft's own validator. Data: every measure is queried live after a deploy. Render: the deployed page is measured for clipped text and judged by a model that did not build it; that layer exists because a clipped card once passed every other check. Interaction: a headless runner clicks and hovers through every item; a person drives what it cannot. Two teams: QA never fixes, and the builder never closes its own bug.")

# ---- 05 UX principles -------------------------------------------------------------------------------------------
order = ["The surface: report, dashboard or app", "The person and their job", "Flow and empty states", "The canvas, then fixed",
         "Layout: one hero, the rest quiet", "Interaction: remove what you can", "Accessibility", "Data honesty", "Critique: cut what does not serve the job"]
enforced = ["Text contrast, on every visual", "Every text whole in the live render", "Colours from the theme only", "No em dashes in visible copy"]
ol = "".join(f'<div class="small"><span class="label" style="margin-right:16px">{i}</span>{t}</div>' for i, t in enumerate(order))
el = "".join(f'<div class="small">{icon("shield-check", "rose")} {t}</div>' for t in enforced)
slide(f"""
<div class="eyebrow">05 &middot; UX principles</div>
<div class="h2">Design from the person down</div>
<div class="grid2 mt32" style="grid-template-columns:3fr 2fr;align-items:stretch">
  {card(f'<div class="h4">The design order</div><div class="list" style="margin-top:24px;gap:14px">{ol}</div>')}
  <div class="card inkcard"><div class="h4 rose">Enforced, not advised</div><div class="list" style="margin-top:24px;gap:24px">{el}</div></div>
</div>
""", "The design order every page follows, from the person and their goal down to pixels, never the reverse: the surface first, report, dashboard or app; then who the user is and the job they need done; flow and empty states; the canvas, fixed once chosen; layout with one hero and everything else quiet; the interaction you can remove; accessibility; data honesty; and a critique that cuts anything not serving the job. On the right, the ones that are not advice: each is a check that fails the build or the deploy.")

# ---- 05 Sample prompts ------------------------------------------------------------------------------------------
op = """New page for uk-trade-data, report name
"UK Trade - Trade stripes". The brief is below.

You are the operator: run the tool and write
only under clients/. When the tool cannot do
something, log a gap, use the nearest supported
option, and carry on. Never ask me."""
bd = """Fix this in the engine, never in a
report file. Reproduce it, find the root
cause, write the spec first if the
behaviour has none, add a test that fails
without the fix, and open a pull request.
Do not merge."""
ar = """Before you build anything new: is
there a spec for it? If not, write the
algorithm first, then the engine, then
the check that enforces it. One generator,
no second path."""
slide(f"""
<div class="eyebrow">05 &middot; Prompts</div>
<div class="h2">Three prompts</div>
<div class="grid3 mt32" style="gap:32px;align-items:stretch;grid-template-columns:repeat(3, minmax(0, 1fr))">
  <div class="card codecard"><div class="label">Operator</div><pre class="code" style="white-space:pre-wrap">{op}</pre></div>
  <div class="card codecard"><div class="label">Builder</div><pre class="code" style="white-space:pre-wrap">{bd}</pre></div>
  <div class="card codecard"><div class="label">Architecture</div><pre class="code" style="white-space:pre-wrap">{ar}</pre></div>
</div>
""", "Three prompts, shortened from the real ones. Operator: the opening of the Trade stripes prompt; the full text is in demos/04-skills-plus-own/prompt-trade-stripes.txt, with the brief underneath. Builder: the shape of every builder task, reproduce, root cause, spec first, a failing test, a pull request nobody merges without review. Architecture: the question I ask before anything new is built, which keeps the tool to one spine. Most of the length of a good prompt is the brief, not the instructions.")

# ---- 05 Deliverables --------------------------------------------------------------------------------------------
dels = [("Report", "On the canary and in the client workspace"), ("Design contract", "Challenged by a second model, then decided"),
        ("Mockup", "Drawn from a sample of live data"), ("Design brief", "Acceptance tests for every element"),
        ("Decision records", "16, each with its reasoning"), ("QA report", "34 of 34 items passed"),
        ("Deliverable pack", "Walkthrough, measures, proof points"), ("Report guide", "Plain English, for the reader; shown next")]
dl = "".join(f'<div class="line"><div class="h4">{t}</div><div class="small" style="margin-top:8px">{d}</div></div>' for t, d in dels)
slide(f"""
<div class="eyebrow">05 &middot; Deliverables</div>
<div class="h2">What one report hands over</div>
<div class="grid2 mt32" style="gap:96px"><div class="lines">{"".join(f'<div class="line"><div class="h4">{t}</div><div class="small" style="margin-top:8px">{d}</div></div>' for t, d in dels[:4])}</div><div class="lines">{"".join(f'<div class="line"><div class="h4">{t}</div><div class="small" style="margin-top:8px">{d}</div></div>' for t, d in dels[4:])}</div></div>
""", "Everything the Trade stripes run handed over, all generated and all in the engagement folder: the report itself, the design contract and the second model's challenge to it, a mockup drawn from real data, a design brief with an acceptance test per element, sixteen decision records with reasoning, the QA report, and the deliverable pack with a page walkthrough, the measure dictionary and every proof point. The report guide is generated the same way; the next slide shows the one for The Balance, because the Trade stripes run finished before the guide generator was merged. Open the folder live if there is time.")

# ---- 05 Final documentation -------------------------------------------------------------------------------------
slide(f"""
<div class="eyebrow">05 &middot; Documentation</div>
<div class="h2">The report guide</div>
<div class="grid2 mt32" style="grid-template-columns:3fr 1fr;gap:48px;align-items:start">
  <img src="assets/report-guide.png" alt="The generated report guide for The Balance" style="width:100%;height:600px;object-fit:cover;object-position:top;border-radius:12px;border:1px solid var(--dn-border);box-shadow:var(--dn-shadow-card)">
  <div class="lines"><div class="line"><div class="h4">Generated</div><div class="small" style="margin-top:8px">From the config and the live model</div></div>
  <div class="line"><div class="h4">Checked</div><div class="small" style="margin-top:8px">Every figure against gov.uk</div></div>
  <div class="line"><div class="h4">For the reader</div><div class="small" style="margin-top:8px">What it shows, and why it looks the way it does</div></div></div>
</div>
""", "The last deliverable: the report guide, written for the people who use the report, not the people who built it. It is generated from the report config, the design decisions and the live model, so it cannot drift from what shipped: every figure on it matches the published gov.uk numbers. It explains what the report tells you, the headline numbers, and the thinking behind the design. Open the HTML live: it has a dark mode and prints to PDF.")

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
