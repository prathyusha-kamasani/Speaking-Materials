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


def fnode(t, d, cls=""):
    return f'<div class="fnode {cls}"><div class="small strong">{t}</div><div class="label" style="margin-top:8px">{d}</div></div>'


# ---- 1 Title ---------------------------------------------------------------------------------------------
slide("""
<div class="center-v">
  <div class="h1">Agentic BI Development</div>
</div>
""", "60 minutes. Who I am, the agenda, then concepts, then the trade balance report built three ways. The refrain for the hour: what would you have to check?", dark=True)

# ---- 2 About me, and the close: one profile, so the two slides always say the same -------------------------
FACTS = [("briefcase", "Solopreneur @ Data Nova, specialising in Microsoft Fabric and Power BI"), ("award", "Microsoft MVP"),
         ("users", "London Microsoft Fabric User Group organiser"), ("mic", "Blogger, speaker and budding YouTuber"),
         ("map-pin", "Remote first, lives in the UK and the Netherlands")]


def profile(eyebrow):
    facts = "".join(f'<div class="fact">{icon(ic, "ink-accent", "icon")}<div class="body">{t}</div></div>' for ic, t in FACTS)
    return f"""
<div class="bye">
  <div class="portrait-ring"><img class="portrait" src="assets/prathy.webp" alt="Prathy Kamasani"></div>
  <div class="bye-text">
    <div class="eyebrow">{eyebrow}</div>
    <div class="h1c" style="margin-top:16px">Prathy Kamasani</div>
    <div class="facts stagger" style="margin-top:40px">{facts}</div>
    <div class="contact" style="margin-top:48px">
      <div class="body">{icon("globe", "ink-accent")}data-nova.io</div>
      <div class="body">{icon("user-round", "ink-accent")}linkedin.com/in/prathy</div>
    </div>
  </div>
</div>
"""


slide(profile("About me"), "Hello everyone. I am Prathy Kamasani: a solopreneur at Data Nova, specialising in Microsoft Fabric and Power BI. Microsoft MVP, I organise the London Microsoft Fabric User Group, I blog, I speak, and I am a budding YouTuber. Remote first, living in the UK and the Netherlands. Everything else is on LinkedIn and my website.")

# ---- 2a The session: title again, and what it covers, from the abstract ---------------------------------------
slide("""
<div class="center-v">
  <div class="eyebrow">This session</div>
  <div class="h1c" style="margin-top:24px">Agentic BI Development</div>
  <div class="h4 ink-accent" style="margin-top:24px">Letting AI agents build your Fabric semantic models and reports</div>
  <div class="body stagger" style="margin-top:48px;max-width:1400px;line-height:1.5">
    <div>An AI agent can build a real semantic model and report from a written spec, if you know how to brief it and how to check its work.</div>
    <div style="margin-top:24px">The interesting part is not the prompt. It is a spec it can act on without guessing, a quality bar set before it starts, and a proper review of what it built.</div>
  </div>
</div>
""", "The title again, and what the hour covers. From the abstract: an agent building a real semantic model and report from a written spec, and the parts that make it reliable. Everyone should leave knowing what to check before they trust an agent's work, and where it still needs a person.")

# ---- 2b Hands up: one question per slide; the first question glides up when the second arrives ---------------
q1, q2 = "Who uses AI for anything: recipes, holiday plans, emails?", "Who uses it for BI work?"
slide(f"""
<div class="center-v">
  <div class="eyebrow">Hands up</div>
  <div class="h2" style="margin-top:48px;max-width:1500px"><span data-morph="hands-q1" style="display:inline-block">{q1}</span></div>
</div>
""", "Old-fashioned show of hands. First: who uses AI for anything at all, recipes, holiday prep, emails? Most hands go up.")
slide(f"""
<div class="center-v">
  <div class="eyebrow">Hands up</div>
  <div class="body muted" style="margin-top:48px;max-width:1500px"><span data-morph="hands-q1" style="display:inline-block">{q1}</span></div>
  <div class="h2 fresh" style="margin-top:40px;max-width:1500px">{q2}</div>
</div>
""", "Then: who uses it in their BI work? Fewer hands. Use the gap between the two to set up the session: today is about closing it.")

# ---- 3 Agenda --------------------------------------------------------------------------------------------
chapters = [("01", "What is BI development?", "Six steps from a question to a trusted report"),
            ("02", "Working with AI", "Context, skills, rules, algorithms, loops, hooks, gates, MCP"),
            ("03", "Agent roles", "Operator, builder, orchestrator, and you"),
            ("04", "Building the trade balance report", "Chat, Fabric skills, MCP, my setup, full delegation"),
            ("05", "How I built the tool", "Specs, engine, tests, prompts, deliverables"),
            ("06", "Cost and limits", "Time, tokens, and what still needs a person")]
slide(f"""
<div class="eyebrow">Agenda</div>
<div class="agenda-list dense">{"".join(f'<div class="chap"><div class="chap-num"><span data-morph="chap-{n}" style="display:inline-block">{n}</span></div><div><div class="h3"><span data-morph="chapt-{n}" style="display:inline-block">{t}</span></div><div class="small muted" style="margin-top:4px">{d}</div></div></div>' for n, t, d in chapters)}</div>
""", "Six parts. What BI development is. Working with AI: the building blocks you use to tell it how you work. The roles an agent plays, and where you stay in the loop. Then one brief, worked through chat, Fabric skills, MCP, my own setup, and full delegation.", dark=True)


def section(num, title, sub, notes):
    # editorial divider: a giant numeral with the title laid over its right-hand digit
    slide(f"""
<div class="sect">
  <div class="sect-num" aria-hidden="true"><span data-morph="chap-{num}" style="display:inline-block">{num}</span></div>
  <div class="sect-title"><div class="h1c">{title}</div><div class="body sect-sub">{sub}</div></div>
</div>
""", notes, dark=True)


# ---- 3 Section: BI development ---------------------------------------------------------------------------
section("01", "What is BI development?", "Six steps, and most of the time is not in the visuals.",
        "Set up the lifecycle before talking about agents. Most delivery time is not building the visual: it is requirements, model fixes, testing, rework after feedback, and sign-off. [Add your own example of where the hours really go.]")

# ---- 4 Lifecycle -----------------------------------------------------------------------------------------
steps = [("01", "Discovery", "Users, questions, acceptance criteria"), ("02", "Design", "Layout, sketch, mockup"),
         ("03", "Build", "Model changes, pages, visuals, theme"), ("04", "Test", "Numbers, render, interaction"),
         ("05", "Deploy", "Workspace, binding, refresh"), ("06", "Govern", "Sign-off, audit trail, changes")]
cards = "".join(card(f'<div class="label">{n}</div><div class="h4" style="margin-top:16px">{t}</div><div class="small" style="margin-top:16px">{d}</div>') for n, t, d in steps)
slide(f"""
<div class="eyebrow">01 &middot; BI development</div>
<div class="h2">From a question to a trusted report</div>
<div class="grid3 mt48" style="grid-template-rows:repeat(2, 1fr);gap:48px">{cards}</div>
""", "Every BI report goes through these six steps, with or without an agent. Discovery: who it is for, what they decide with it, how we will know it is right. Design: the layout and the mockup, signed before anything is built. Build: the model changes and the pages. Test: the numbers, the render, the interactions. Deploy: the right workspace, the right model, survives a refresh. Govern: sign-off, who approved what, changes after go-live. Ask who does each one today. Then flag Discovery, Test and Govern: they are where trust is earned, and where agents are weakest. Most of the time is not in Build.")

# ---- Section 02: working with AI -------------------------------------------------------------------
section("02", "Working with AI", "A capable graduate on day one",
        "So that is the job: discovery, design, build, test, deploy and govern. An AI agent can now help with every one of those steps. Before we hand it any of them, it is worth thinking about what kind of colleague we are handing them to.")

grad = [("graduation-cap", "", "Knows a lot", "DAX, Power BI, Fabric, public documentation"),
        ("building-2", "", "Not how you work", "Your model, your names, your rules, your sign-offs"),
        ("list-checks", "ink-accent", "So you give it", "Context, recipes, limits, and someone who checks")]
slide(f"""
<div class="eyebrow">02 &middot; Working with AI</div>
<div class="h2">Treat it like a new graduate</div>
<div class="grid3 mt48 stagger" style="align-items:stretch">{"".join(card(f'{icon(ic, cls, "icon-xl")}<div class="h4" style="margin-top:32px">{t}</div><div class="small" style="margin-top:16px">{d}</div>', "roomy") for ic, cls, t, d in grad)}</div>
""", "Think of a new graduate on day one. They know a lot: DAX, Power BI, Fabric, the public documentation. What they do not know is how you work: your model, your naming, your rules, who signs off what. You would not let a graduate run discovery or sign off a deploy on day one. You tell them how you work, give them recipes, set limits, and check their work. An agent is the same. First, what most of us do today: plain chat, with no context at all.")

# ---- Examples: the helper, then Example 1 (plain chat), shown early as the way everyone starts ---------------------------------
def viewer(slot_id, image, alt, link=None, link_label="Open the live report"):
    """A render at full width: scrolls in its frame, E or the button expands it, the button opens the live report."""
    bar = f'<button class="vbtn" type="button" data-expand>{icon("maximize-2", "", "icon-sm")}Expand</button>'
    if link:
        bar += f'<button class="vbtn" type="button" data-href="{link}">{icon("external-link", "", "icon-sm")}{link_label}</button>'
    return (f'<div class="viewer" data-slot="{slot_id}"><div class="viewer-scroll" tabindex="0">'
            f'<img src="{image}" alt="{alt}"></div><div class="viewer-bar">{bar}</div></div>')


def outcome(n, label, model_count, model_unit, model_note, names, report_line, notes, image=None, alt="", link=None, no_report="", fit=False, slot_html=None):
    """After each example: what it changed in the model, and the report it made (or that it made none)."""
    if slot_html:
        slot = slot_html
    elif image:
        slot = viewer(f"outcome-{n}", image, alt, link)
        if fit:  # a portrait page: show it whole, not its top third
            slot = slot.replace('class="viewer"', 'class="viewer fit"', 1)
    else:
        slot = (f'<div class="shot live">{icon("file-x", "muted", "icon-xl")}<div class="h4">No report</div>'
                f'<div class="small muted" style="max-width:640px;text-align:center">{no_report}</div></div>')
    shown = names[:3]
    chips = "".join(f'<span class="mchip">{x}</span>' for x in shown) + (f'<span class="mchip more">+{len(names) - len(shown)} more</span>' if len(names) > len(shown) else "")
    right = card(f'<div class="label">The model</div>'
                 f'<div class="row g16" style="margin-top:8px;align-items:baseline"><div class="h2 ink-accent" style="margin:0" data-countup>{model_count}</div><div class="small strong">{model_unit}</div></div>'
                 f'<div class="cap muted">{model_note}</div>'
                 + (f'<div class="row" style="margin-top:12px;gap:8px;flex-wrap:wrap">{chips}</div>' if names else "")
                 + f'<div class="split"><div class="label">The report</div><div class="small" style="margin-top:8px;line-height:1.4">{report_line}</div></div>',
                 "roomy stretch")
    slide(f"""
<div class="eyebrow">{label}</div>
<div class="h2">What it changed</div>
<div class="ex mt48 wide"><div class="stack">{slot}</div>{right}</div>
""", notes)


def example(n, title, setup, pro, con, notes, videos=None, eyebrow=None, rates=None, image=None, alt="", link=None, live=None, start=0.5):
    if image:
        slot = viewer(f"example-{n}", image, alt, link)
    elif live:  # a live demo in the terminal: the slide only says so
        slot = (f'<div class="shot live" data-slot="example-{n}">{icon("square-terminal", "ink-accent", "icon-xl")}'
                f'<div class="h4">Live demo</div><div class="small muted" style="max-width:640px;text-align:center">{live}</div></div>')
    elif videos:  # plays in order; P plays or pauses, the native controls also work
        slot = (f'<video class="clip" data-slot="example-{n}" data-playlist="{",".join(videos)}" data-rates="{",".join(str(r) for r in (rates or [1] * len(videos)))}" src="{videos[0]}#t={start}" '
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
<div class="ex mt48{' wide' if videos or image or live else ''}"><div class="stack">{slot}</div>{right}</div>
""", notes)

example(1, "Plain chat", "Claude Code, no skills, no access to the model",
        "Zero setup, fast for DAX", "Guesses table and column names",
        "One clip, 81 seconds, highlights marked. First: asking what is preinstalled; no skills are configured. Then the first prompt asks for a trade balance measure and a card colour measure with no model; it invents 'Trade'[Exports] and 'Trade'[Imports] (first box). The second prompt pastes the real tables, columns and relationships, and it rewrites both measures correctly (second box). For a single measure this is genuinely the right tool. The catch: I had to paste the schema by hand, and it goes stale when the model changes. Press P to play or pause.",
        videos=["media/chatVideo.m4v"], eyebrow="02 &middot; Example 1")
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
<div class="eyebrow">02 &middot; Example 1</div>
<div class="h2">Without the schema, then with it</div>
<div class="grid2 mt32" style="gap:32px;align-items:stretch">
  <div class="card codecard"><div class="label">Prompt 1: no model</div><pre class="code">{p1}</pre></div>
  <div class="card codecard"><div class="label">Prompt 2: real names pasted in</div><pre class="code">{p2}</pre></div>
</div>
""", "Left: prompt 1, the ask on its own. The highlighted names, 'Trade'[Exports] and 'Trade'[Imports], do not exist in the model: it invented them. Right: prompt 2, after pasting the real tables and columns. It now sums Value GBP Millions and splits exports from imports on Flow[Direction]. Only the Trade Balance measure is shown. The Balance Card Colour measure came out the same both times (IF the balance is 0 or more, \"#2E7D32\", else \"#C62828\"), because it does not depend on any names. The fix worked, but I had to paste the schema by hand, and it goes stale the moment the model changes. The Flow[Direction] values it assumed, Export and Import, are the real ones; the Fabric skills run confirmed them against the data. Code is shown as pasted, with the indentation in the right-hand answer tidied to fit.")

CHAT_DAX = """Trade Balance =
VAR Exports =
  CALCULATE(SUM('Trade Total Monthly'[Value GBP Millions]),
    Flow[Direction] = "Export")
VAR Imports =
  CALCULATE(SUM('Trade Total Monthly'[Value GBP Millions]),
    Flow[Direction] = "Import")
RETURN Exports - Imports

Balance Card Colour =
IF([Trade Balance] >= 0, "#2E7D32", "#C62828")"""
outcome(1, "02 &middot; Example 1: Plain chat", "0", "changes", "It cannot reach the model", [],
        "None. Two measures as text, to paste in by hand.",
        "What chat changed: nothing. It has no access to the model, so it cannot add a measure or build a page. What you get is DAX as text, and you do the rest by hand.",
        slot_html=f'<div class="card codecard" style="height:100%;box-sizing:border-box"><div class="label">What you get: text to paste</div><pre class="code" style="white-space:pre-wrap;margin-top:16px">{CHAT_DAX}</pre></div>')

# ---- 5 Chat vs agentic -----------------------------------------------------------------------------------
def lnode(t, d, area):
    return f'<div class="lnode" style="grid-area:{area}"><div class="small strong">{t}</div><div class="cap muted">{d}</div></div>'
def larr(name, area):
    return f'<div class="larr" style="grid-area:{area}">{icon(name, "muted")}</div>'
down = f'<div class="farrow col">{icon("arrow-down", "muted")}</div>'
def cnode(t, d):
    return f'<div class="fnode"><div class="small strong">{t}</div><div class="cap muted">{d}</div></div>'
chat_line = down.join([cnode("You ask", "A measure for the balance"), cnode("It answers", "From what it has seen before"),
                       cnode("You paste it in", "And find out if it works")])
# the loop in DOM order (so it draws in order), placed on a 3x3 grid: plan, act, observe, try again, back to plan
loop = "".join([lnode("Plan", "Which table holds exports?", "a"), larr("arrow-right", "ab"),
                lnode("Act with tools", "Reads the model, runs a DAX query", "b"), larr("arrow-down", "bc"),
                lnode("Observe the result", "Compares the figure with the source", "c"), larr("arrow-left", "cd"),
                lnode("Try again, or stop", "Fixes and reruns, or hands back", "d"), larr("arrow-up", "da")])
slide(f"""
<div class="eyebrow">02 &middot; Working with AI</div>
<div class="h2">How chat differs from an agent</div>
<div class="grid2" style="margin-top:24px;grid-template-columns:5fr 7fr;align-items:stretch">
  <div class="card">
    <div class="h4">Chat: once through</div>
    <div class="stack seq chatline" style="margin-top:24px;gap:4px">{chat_line}</div>
  </div>
  <div class="card inkcard">
    <div class="h4">Agent: a loop</div>
    <div class="loop seq" style="margin-top:24px">{loop}</div>
    <div class="small rose later" style="margin-top:20px">{icon("user-check", "rose")} You approve before it ships</div>
  </div>
</div>
<div class="takeaway">Chat answers once. An agent checks its own work, and you check the agent.</div>
""", "That was chat. Under the hood an agent is the same kind of model, an LLM; what makes it an agent is the tools and the loop. Chat goes through once: you ask, it answers from what it has seen before, you paste it in and find out. In the clip, that is where the invented table names came from. An agent goes round a loop: it plans, acts with tools, reads the real model and runs a DAX query, observes the result against the source, and tries again or stops. It does by itself what I had to do by hand in the video. That loop is the power and the risk: it can fix its own errors, and it can confidently build on its own mistake. So the loop needs a gate, and the gate is you.")

# ---- 02 The building blocks, and where each lives in my setup --------------------------------------------
BLOCK_ROWS = [("Context", "Advisory", "CLAUDE.md, AGENTS.md", "Standing rules for every session"),
        ("Skills", "Advisory", ".claude/skills/ (9)", "A repeatable recipe for one job"),
        ("Rules", "Advisory", "PRINCIPLES.md", "What good looks like, in words"),
        ("Algorithms", "Structure", "algorithms/ (19)", "The steps of each phase"),
        ("Loops", "Blocking", "render-fix and QA loops", "Repeat until a check passes"),
        ("Hooks", "Blocking", "pre-commit (29), edit hooks", "Block one action, on an event"),
        ("Gates", "Blocking", "the rail: 44 steps", "No sign-off, no next phase"),
        ("MCP", "Reach", "none: REST and XMLA queries", "Live access to tools and data")]
KIND_MORPH = {"Context": ' data-morph="kind-advisory" style="display:inline-block"', "Hooks": ' data-morph="kind-hook" style="display:inline-block"', "Gates": ' data-morph="kind-gate" style="display:inline-block"'}
BLOCK_KIND = {"Advisory": "ink-violet", "Reach": "muted", "Blocking": "ink-accent", "Structure": ""}
def blocks_table(step, eyebrow, title, notes):
    # one table, built up a column at a time: names, then kind, then what it does, then (later) where it lives in my setup.
    # Hidden columns keep their width, so the table never jumps; the column added on this step fades in.
    def cell(col, html, cls=""):
        state = " hold" if col > step else (" fresh" if col == step and step > 1 else "")
        return f'<td class="{cls}{state}">{html}</td>'
    def th(col, label):
        state = "hold" if col > step else ("fresh" if col == step and step > 1 else "")
        return f'<th class="{state}">{label}</th>'
    body = "".join("<tr>" + cell(1, f'<span class="blkname" data-morph="blk-{a}">{a}</span>') + cell(2, f'<span class="label {BLOCK_KIND[b]}"{KIND_MORPH.get(a, "")}>{b}</span>') + cell(3, d)
                   + (cell(4, c, "mono nowrap") if step >= 4 else "") + "</tr>" for a, b, c, d in BLOCK_ROWS)
    head = "<tr>" + th(1, "Block") + th(2, "Kind") + th(3, "What it does") + (th(4, "In my setup") if step >= 4 else "") + "</tr>"
    slide(f"""
<div class="eyebrow">{eyebrow}</div>
<div class="h2">{title}</div>
<table class="cmp tight vocab vtight" style="margin-top:16px"><thead class="morph-fade">{head}</thead><tbody>{body}</tbody></table>
""", notes)

BLOCK_ICONS = {"Context": "file-text", "Skills": "book-open", "Rules": "scale", "Algorithms": "list-ordered",
               "Loops": "repeat", "Hooks": "zap", "Gates": "door-closed", "MCP": "plug"}
tiles = "".join(f'<div class="tile">{icon(BLOCK_ICONS[a], "ink-accent", "icon-xl")}<div class="name" data-morph="blk-{a}">{a}</div></div>' for a, b, c, d in BLOCK_ROWS)
slide(f"""
<div class="eyebrow">02 &middot; Working with AI</div>
<div class="h2">The building blocks</div>
<div class="tiles">{tiles}</div>
""", "Eight building blocks. Most people know two or three of them: context, skills, rules, algorithms, loops, hooks, gates, MCP. On the next slide they line up into a table, and over two slides we add what kind each one is, then what it does.")
blocks_table(2, "02 &middot; Working with AI", "What kind each one is",
             "Now the kind. Context, skills and rules are advisory: the agent can skip them. Algorithms give the work its structure. Loops, hooks and gates are blocking: the agent cannot walk past them. MCP is reach: it gives the agent live access, and on its own it neither advises nor blocks.")
blocks_table(3, "02 &middot; Working with AI", "What each one does",
             "Context: standing rules, read every session; CLAUDE.md for Claude, AGENTS.md for any tool, copilot-instructions.md for GitHub Copilot. Skills: a repeatable recipe for one job, public like Microsoft's Fabric skills or your own. Rules: what good looks like, written down. Algorithms: the steps of each phase, some in parallel. Loops: repeat until a check passes, not until the agent feels done. Hooks: refuse one action when an event fires. Gates: no sign-off, no next phase. MCP: live, typed access to a tool or data. Where each lives in my setup comes later, when we open it.")

# ---- 02 Advisory, hook or gate -----------------------------------------------------------------------------
kinds = [("Advisory", "ink-violet", "Context, skills, rules", "The agent decides whether to follow them. Nothing fails if it does not.", "A line in CLAUDE.md: never name a client", "card"),
         ("Hook", "ink-accent", "Fires on an event", "A commit or an edit. It blocks that one action.", "An edit to the engine from a report branch", "card"),
         ("Gate", "rose", "A checkpoint in the flow", "No evidence or signature, no next phase.", "No signed design, no build", "card inkcard")]
def kind_card(name, cls, head, body, ex, klass):
    exl = f'<div class="split"><div class="label">Example</div><div class="small" style="margin-top:12px">{ex}</div></div>' if ex else ""
    return (f'<div class="{klass}"><div class="h4 {cls}"><span data-morph="kind-{name.lower()}" style="display:inline-block">{name}</span></div><div class="body strong" style="margin-top:24px">{head}</div>'
            f'<div class="small" style="margin-top:16px;line-height:1.4">{body}</div>{exl}</div>')
slide(f"""
<div class="eyebrow">02 &middot; Working with AI</div>
<div class="h2">Advisory, hook or gate?</div>
<div class="grid3 mt48 stagger" style="align-items:stretch">{"".join(kind_card(*k) for k in kinds)}</div>
<div class="takeaway">An agent edited the engine from a report branch. Now a hook blocks the edit.</div>
""", "Context, skills and rules are advisory: the agent can skip them on any run. A hook fires on an event, a commit or an edit, and blocks that one action. A gate is a checkpoint in the flow: the next phase will not start without evidence or a signature. The story at the bottom is real: in a delegated run, the agent building a report started changing the engine itself. A rule in the prompt came next, and it was not enough on its own; now a hook blocks an engine edit from a report branch. Every example later sits somewhere between advisory and blocking.")

# ---- 02 An algorithm for each phase -------------------------------------------------------------------------
phases = [("01", "Discovery", "13 steps", "Requirements, stories, feasibility, profile, proof points", "Discovery gate"),
          ("02", "Design", "15 steps", "Contract, layout, sketch, visuals, mockup", "Design gate"),
          ("03", "Develop", "2 steps", "Build, offline gates", ""),
          ("04", "Verify and QA", "6 steps", "Canary, live render, render review, QA", "QA passes"),
          ("05", "Ship", "5 steps", "Ship approval, client deploy, deliverable pack", "Ship approval"),
          ("06", "Govern", "3 steps", "Audit trail, tidy, owner acceptance", "Owner acceptance")]
STEP_NAME = {"01": "Discovery", "02": "Design", "03": "Build", "04": "Test", "05": "Deploy", "06": "Govern"}  # the six BI steps, as slide 8 names them
pc = "".join(card(f'<div class="row" style="justify-content:space-between;align-items:flex-start"><div><div class="label">{n} &middot; {STEP_NAME[n]}</div><div class="h4" style="margin-top:8px">{t}</div></div>'
                  f'<div class="stepcount"><div class="h2 ink-accent" data-countup>{c.split()[0]}</div><div class="label">steps</div></div></div>'
                  f'<div class="small" style="margin-top:12px">{d}</div>'
                  + (f'<div class="small ink-accent strong" style="margin-top:12px">{g}</div>' if g else '')) for n, t, c, d, g in phases)
slide(f"""
<div class="eyebrow">02 &middot; Working with AI</div>
<div class="h2">An algorithm for each phase</div>
<div class="grid3 stagger" style="margin-top:32px;grid-template-rows:repeat(2, 1fr);gap:32px">{pc}</div>
""", "This is the rail: 44 steps across six phases, each phase written down as an algorithm the agent follows in order. Some steps run in parallel: while one model reads a draft and decides, the agent prepares the next draft; a decision and its second check run side by side. Five steps are gates, named at the bottom of each card: the phase does not finish until its gate is decided. Show the rail live in Mission Control if there is time.")

# ---- Section 03: agent roles --------------------------------------------------------------------------------
section("03", "Agent roles", "Operator, builder, orchestrator, and you",
        "Who does what once the building blocks are in place. Four roles; the same model can play more than one, but never at the same time.")

ROLE = {"You": ("user-check", "r-you"), "Operator": ("play", "r-op"), "Builder": ("wrench", "r-build"),
        "Orchestrator": ("network", "r-orch"), "Gate": ("door-closed", "r-gate")}
roles = [("play", "", "Operator", "Runs the tool on a brief", "Writes only the deliverables. Logs what the tool cannot do.", "card"),
         ("wrench", "", "Builder", "Changes the tool", "On its own branch, with tests. You review each change.", "card"),
         ("network", "", "Orchestrator", "Plans and hands out work", "Sends each decision to a delegate and a checker, in order.", "card"),
         ("user-check", "rose", "You", "Signs the gates", "Decides what may be delegated. Keeps the client deploy unless you grant it.", "card inkcard")]
slide(f"""
<div class="eyebrow">03 &middot; Agent roles</div>
<div class="h2">Four roles</div>
<div class="grid4 mt48 stagger">{"".join(f'<div class="{k}"><div class="rbadge {ROLE.get(n, ROLE["You"])[1]}">{icon(ic, "", "icon-lg")}</div><div class="h4" style="margin-top:32px">{n}</div><div class="body strong" style="margin-top:16px;line-height:1.3">{h}</div><div class="small" style="margin-top:16px;line-height:1.4">{d}</div></div>' for ic, c, n, h, d, k in roles)}</div>
""", "Operator: runs the tool on a brief and writes only the deliverables; when the tool cannot do something it logs a gap and uses the nearest supported option. Builder: changes the tool itself, on its own branch, with tests; every change is a pull request I review. Orchestrator: plans the work and hands each decision to a delegate and a second checker, in the order the rail requires. The human gate: decides what may be delegated, signs what matters, and keeps the one thing I never delegate, the client deploy. In the last run, the operator logged ten gaps and ten builders fixed them while it carried on.")

# ---- 03 Who does what -----

agent_steps = [("Discovery", "Drafts user stories from the requirements", "Sign off the requirements"),
               ("Design", "Profiles the model, drafts the layout and mockup", "Sign the design before it builds"),
               ("Build", "Writes the model changes and the report files", "Review the model changes"),
               ("Test", "Runs data, render and layout checks", "Click what automated QA cannot"),
               ("Deploy", "Deploys through a gated pipeline", "Approve the release"),
               ("Govern", "Records who approved what, and when", "Accept the result")]
rows = "".join(f'<tr><td>{t}</td><td>{a}</td><td>{y}</td></tr>' for t, a, y in agent_steps)
slide(f"""
<div class="eyebrow">03 &middot; Agent roles</div>
<div class="h2">Who does what, step by step</div>
<table class="cmp who autoplay" style="margin-top:32px"><thead><tr><th>Step</th>
<th><span class="row g16">{icon("bot", "")}<span>The agent</span></span></th>
<th><span class="row g16">{icon("user-check", "ink-accent")}<span class="ink-accent">You</span></span></th></tr></thead><tbody>{rows}</tbody></table>
""", "The same six steps from the start of the talk, split by who does the work. The agent drafts the stories, profiles the model and drafts the layout, writes the model changes and the report, runs the checks, deploys and records. You sign off the requirements, sign the design before it builds, approve the model changes, drive the interactions, approve the release, and accept the result. Every line in both columns is a step my own setup has today; the demos later show it.")

# ---- 03 The flow -------------------------------------------------------------------------------------------
arrow = f'<div class="farrow">{icon("arrow-right", "muted")}</div>'
def rnode(t, role, cls=""):
    ic, rc = ROLE[role]
    return f'<div class="fnode rnode {cls}"><div class="small strong">{t}</div><span class="rchip {rc}">{icon(ic, "", "icon-sm")}{role}</span></div>'
main = arrow.join([rnode("Requirement", "You", "you"), rnode("Drafts and improves it", "Operator"),
                   rnode("Approve or question", "Gate", "gate"), rnode("Builds and checks", "Operator"),
                   rnode("Test deploy (canary)", "Operator"), rnode("Client deploy", "You", "you")])
side = arrow.join([rnode("Tool cannot do it", "Operator"), rnode("Gap logged", "Operator"),
                   rnode("Fix on a branch", "Builder"), rnode("Review the change", "You", "you")])
slide(f"""
<div class="eyebrow">03 &middot; Agent roles</div>
<div class="h2">How a report gets made</div>
<div class="flowgrid mt48 seq">{main}<div class="backloop"><div class="bl-line"></div><div class="bl-label">A question sends it back to the operator</div></div></div>
<div class="label later" style="margin-top:40px">Alongside</div>
<div class="flow seq later" style="margin-top:16px">{side}</div>
""", "Read it left to right. I write the requirement. The operator drafts it properly: stories, acceptance tests, the data it needs. At the gate it is approved or questioned; a question sends it back to the operator, and that loop runs until it is approved. The same loop repeats at every gate: design, QA, ship. The operator builds, checks and deploys to a canary. The client deploy stays with me. Underneath, the second lane: whenever the tool cannot do something, the operator logs a gap and carries on, and a builder fixes it separately as a change I review.")

# ---- 03 Who holds the gate -----------------------------------------------------------------------------------
human = ('<div class="card roomy" data-morph="gate-human"><div class="h4">Human gate</div><div class="body strong" style="margin-top:24px">You sign four gates</div>'
         '<div class="small" style="margin-top:16px;line-height:1.4">Discovery, design, ship and acceptance. QA is a check that runs. Slow, and you are always in the loop.</div></div>')
delegated = ('<div class="card inkcard roomy fresh"><div class="h4 rose">Full delegation</div><div class="body strong" style="margin-top:24px">A second model decides. At a gate, a third model checks.</div>'
             '<div class="small" style="margin-top:16px;line-height:1.4">The client deploy stays yours unless you grant it. You read the decisions afterwards.</div></div>')
# two slides, one build: the human gate first; then the same card stays put and full delegation arrives beside it
slide(f"""
<div class="eyebrow">03 &middot; Agent roles</div>
<div class="h2">Who signs the gates?</div>
<div class="grid2 mt48 gatepair" style="align-items:start">{human}<div></div></div>
""", "Two ways to run the same flow. First, the human gate: I sign every gate myself, discovery, design, QA, ship and acceptance. Safe, but I am in the loop all day.")
slide(f"""
<div class="eyebrow">03 &middot; Agent roles</div>
<div class="h2">Who signs the gates?</div>
<div class="grid2 mt48 gatepair" style="align-items:start">{human}{delegated}</div>
""", "The other way: full delegation. A different model decides each gate and a third model checks it, and I keep one gate, the client deploy, and read the recorded decisions afterwards. Be honest here: in my first delegated runs the deciding model was meant to be different but was quietly served the drafting model; only the checks were independent. The tool now proves which model answered and refuses a decision when it is the drafter's own. That is the last example in the next section.")

# ---- 10 Section: building the trade balance report -------------------------------------------------------------------------------
section("04", "Building the trade balance report", "One brief through different tools. Where a tool did not get it, the slide says so.",
        "For each example use the same four beats: setup, brief in, what came out, what we had to check. Do not declare a winner until the comparison slide.")

# ---- 11 The brief: what every example is asked for, and what it is checked against ------------------------------
build = [("paint-bucket", "Balance card", "Changes colour from surplus to deficit"),
         ("chart-line", "Monthly trend", "Exports, imports and the balance"),
         ("chart-bar", "Breakdown", "By partner country or commodity"),
         ("sliders-horizontal", "Slicer", "Switches the trend between measures")]
done = ["Card colour from a measure, not a fixed colour", "The slicer changes the plotted measure",
        "Every field it uses exists in the model"]
also = ["Who it is for", "The model, its tables and its rules", "One page, theme colours, native visuals",
        "What is out of scope", "What to hand back, with evidence", "Ask before guessing"]
tiles_b = "".join(f'<div class="btile">{icon(ic, "ink-accent", "icon-xl")}<div><div class="small strong">{t}</div><div class="cap muted">{d}</div></div></div>' for ic, t, d in build)
checks_b = "".join(f'<div class="row g16">{icon("circle-check", "rose", "icon")}<div class="small">{t}</div></div>' for t in done)
slide(f"""
<div class="eyebrow">04 &middot; Examples</div>
<div class="h2">UK trade, the balance</div>
<div class="body muted" style="margin-top:8px">The brief given to Fabric skills and MCP</div>
<div class="grid2" style="margin-top:32px;grid-template-columns:7fr 5fr;align-items:stretch">
  <div><div class="label">What to build</div><div class="btiles stagger" style="margin-top:16px">{tiles_b}</div>
    <div class="label later" style="margin-top:28px">Also in the brief</div>
    <div class="row later" style="margin-top:12px;gap:10px;flex-wrap:wrap">{"".join(f'<span class="bchip">{t}</span>' for t in also)}</div></div>
  <div class="card inkcard">
    <div class="label">Done means</div>
    <div class="row g32 seq" style="margin-top:16px;align-items:flex-end">
      <div><div class="h2 bfig" data-countup>£937.0bn</div><div class="cap">exports</div></div>
      <div><div class="h2 bfig" data-countup>£980.4bn</div><div class="cap">imports</div></div>
    </div>
    <div class="cap" style="margin-top:4px">12 months to March 2026, published figures</div>
    <div class="stack seq late" style="margin-top:24px;gap:14px">{checks_b}</div>
  </div>
</div>
""", "This is the brief, in full in demos/BRIEF.md. What each example got, honestly: Fabric skills and MCP got this brief, pasted unchanged, in an earlier copy that named the wrong workspace for the model. Plain chat got a single measure prompt, not the brief. My setup is shown with The Balance, which I built before this brief on the same model. Full delegation got a new brief on the same model. The brief follows Anthropic's guidance for briefing an agent: who it is for and why, the exact model and tables, what to build, what done means, the constraints, what is out of scope, what to hand back, and to ask before guessing. The figures are the published gov.uk UK Trade in Numbers totals for the 12 months to March 2026. Open ONS data, so nothing confidential.")

example(2, "Fabric skills", "Microsoft's Fabric skills, same brief",
        "Real file formats, a draft in minutes", "Advice the agent can skip, and no record of who approved",
        "Concede loudly: Microsoft's skills are good, and for a prototype, a single measure, or a report you will never rebuild, they are the right answer. Watch for: real file formats, and a first draft far sooner than you could build one. What to notice is not quality but that it is advisory and opt-in. Show the version and date of the setup. One recording of the whole run, played at 12 times speed from 2 minutes 30 seconds in (the first part shows my account details): it reads the brief, finds the model, queries it, writes a spec you approve, builds the report files, validates them, previews in the Service without publishing, and, after a second prompt asking it to, publishes to the Fabric Friday Demo workspace folder 02 Fabric skills. It built on SM_UKT_DirectLake, not SM_UKT_Import: the brief it was given named the wrong workspace, and it chose the model it could find instead of asking. Result against the brief: one of four done checks passed. Step by step is in demos/02-fabric-skills/run-steps.md. Press P to play or pause; the video controls also set speed.",
        videos=["media/Fabric skills-2.m4v"], rates=[12], start=150)
outcome(2, "04 &middot; Example 2: Fabric skills", "0", "changes", "It read the model with DAX queries and wrote nothing", [],
        "UK Trade Balance, published to folder 02. Brief: £937.0bn exports. Built: 30.3K, all years. One of four done checks.",
        "The model is untouched: it read it with DAX queries and used the measures that were there. The report is a real Power BI report in the workspace, built in minutes and published when asked, on SM_UKT_DirectLake because the brief named the wrong workspace, and you can see what went wrong: the cards show all-years totals, 30.3K and 31.6K instead of 937.0 and 980.4, the partners chart is empty, the card colour and the slicer were not built. One of the four done checks passed.",
        image="assets/fabric-skills-render.jpg", alt="The Fabric skills report as rendered by the Power BI Service", link="https://app.powerbi.com/groups/0c5685bd-1817-447c-8460-ac5858ebf133/reports/6e10d632-18ba-42bc-a239-151808d81289")


example(3, "MCP", "GitHub Copilot in VS Code, with Microsoft's Power BI authoring MCP",
        "Reads the real model", "Can change the model with your sign-in, and nothing records it. This run was read only.",
        "VS Code, GitHub Copilot in agent mode, Microsoft's hosted Power BI authoring MCP server (signed in with an az token). The clip is a slow scroll through the whole chat (1 minute 54 seconds, about 3 lines a second). What happens: it connects to SM_UKT_Import through MCP, runs DAX queries and gets the 12-month figures right (exports 936.967, imports 980.369, balance -43.402 GBP bn). It found the connection read-only, so it could not add a field parameter and asked how to handle the slicer. The MCP server cannot create report pages, so Copilot wrote the report as PBIP files itself, locally. It could not publish them: by its own account, the MCP tools cannot create or publish reports, and the Fabric import menu does not take PBIP. The item UK Trade Balance mcp in the Fabric Friday Demo folder 03 MCP is a Save a copy of the report already in the workspace (the Fabric skills one), made in the browser, not the report Copilot built. Point to make: MCP gave it the real model and the right numbers; it could not deliver a report. Press P to play or pause.",
        videos=["media/mcp-chat-scroll.mov"], rates=[1])
outcome(3, "04 &middot; Example 3: MCP", "0", "changes", "Read only: it could not add the field parameter the slicer needs", [],
        "None by Copilot. It wrote PBIP files on the laptop. I published them myself: next slide.",
        "MCP got the real numbers from the live model, but it changed nothing: the connection was read only, so the field parameter for the slicer could not be added. And there is no report in the workspace: Copilot wrote PBIP files locally, and the MCP tools cannot publish them. Say it clearly: with a writable connection, MCP can change the model directly, and nothing asks you first. This run's connection was read only.",
        no_report="PBIP files on the laptop. Copilot could not publish them.")

# ---- MCP: publishing what Copilot built --------------------------------------------------------------------------
MCP_ERRORS = ["No <code>.platform</code> file", "No schema line in the <code>.pbip</code>", "Card colours set as theme colours, not hex (2)", "A setting <code>report.json</code> does not allow"]
mcp_errs = "".join(f'<div class="cap">{e}</div>' for e in MCP_ERRORS)
mcp_card = card('<div class="label">As built</div><div class="small strong" style="margin-top:8px">The Service refused it</div>'
                "<div class=\"cap muted\" style=\"margin-top:16px\">Microsoft's validator, 5 errors:</div>"
                '<div class="stack" style="margin-top:4px;gap:2px">' + mcp_errs + '</div>'
                '<div class="split"><div class="label">After one fix</div><div class="small" style="margin-top:8px;line-height:1.4">'
                'I removed the setting by hand and it published. Every visual is empty, with or without filters.</div></div>', "stretch mcpcard")
mcp_view = viewer("mcp-publish", "assets/mcp-build-render.jpg", "The MCP-built report in the Power BI Service, every visual empty", "https://app.powerbi.com/groups/0c5685bd-1817-447c-8460-ac5858ebf133/reports/550a1971-7189-48c1-abae-08ecfe8cb97a")
slide(f"""
<div class="eyebrow">04 &middot; Example 3: MCP</div>
<div class="h2">Publishing the MCP report</div>
<div class="ex mt48 wide"><div class="stack">{mcp_view}</div>{mcp_card}</div>
""", "What happened when I published the files Copilot wrote. As built, the Power BI Service refused them: report.json has a setting, layoutOptimization, that the report format does not allow. Microsoft's own validator finds five errors: no .platform file, no schema line in the .pbip, the balance card's colour rule uses theme colours where the format needs hex values, twice, and that setting. I removed the one setting by hand, on a copy, and the Service accepted it. It is in folder 03 as UK Trade Balance (MCP build). Every visual on it is empty, with or without filters, and it never finishes loading. Copilot's own notes said it could not open the report anywhere to check it: there is no Power BI Desktop on a Mac. So the numbers it got from MCP were right, and the report it wrote does not work.")


example(4, "My setup", "My skills, scripts, gates, and sign-offs",
        "Tested, gated, with an audit trail", "Upfront cost, covers only what I encoded",
        "Back to the terminal, tab 1. Demos A and C run live and offline. Demo A: check_phase_order blocks what-we-trade and passes the-balance. Demo C: run_pipeline until gates, five stages green, advisories, read R-SURVIVES-REFRESH aloud. Demo B (recorded, optional): the model half, same recipe. Say the cost out loud: it is overkill for one-off work. Where its grounding comes from: it builds offline against a cached snapshot of the live model, and the snapshot guard refuses a deploy if the snapshot is older than 7 days or no longer matches the live model. It does not create tables from raw files; it profiles and wires tables already in the model. The next slide shows what it changed in the model and the report it made.",
        live="Two steps in the terminal. A check stops a report whose design was not approved. Then one command builds the report and runs all the checks.")
# ---- Example 4: Mission Control, the rail and the gates for every page ------------------------------------------
mc_view = viewer("mission-control", "assets/mission-control.jpg", "Mission Control: 07 Trade Stripes, every phase done, go for launch",
                 "http://127.0.0.1:8199/?client=uk-trade-data", "Open Mission Control")
mc_lines = "".join(f'<div class="mcrow"><div class="small strong">{t}</div><div class="cap muted">{d}</div></div>' for t, d in [
    ("Every page", "Its phase, and green or red"),
    ("The rail", "44 steps over six phases, with the evidence for each"),
    ("Every gate", "Who decided it, and which model"),
    ("Go or no-go", "One call per station before a release")])
slide(f"""
<div class="eyebrow">04 &middot; Example 4</div>
<div class="h2">Mission Control</div>
<div class="ex mt48 wide"><div class="stack">{mc_view}</div>{card(f'<div class="label">What it shows</div>{mc_lines}', "stretch")}</div>
""", "")

outcome(4, "04 &middot; Example 4: My setup", "19", "measures added", "Plus 3 calculated columns, each verified on the live model", ['_Verdict', '_Colour Balance', '_Thesis Sentence', '_Card Exports', '_Card Imports', '_Card Balance', '_Chart Exports', '_Chart Imports', '_Chart Balance', '_Chart Import Gap', '_State Label', '_Period Label', '_Drilled Period Label', '_Is Latest FY', '_Is Latest FY Any Grain', 'Total Trade', 'Exports', 'Imports', 'Trade Balance'],
        "The Balance, built earlier on the same model. Against this brief: no slicer, no breakdown.",
        "What my setup changed: 19 measures and 3 calculated columns, every one requested in a file, written to the model, and verified against the live model before the page used it. The report is The Balance as the Power BI Service renders it. Be straight about it: I built it in July, before this brief, on the same model. It has the brief's figures, £937.0bn exports and £980.4bn imports, and the balance card coloured by a measure; against this brief it has no slicer and no partner or commodity breakdown, and it has drill-through pages the brief rules out. The run that used this exact brief, page 06, ended unpolished and never reached QA, so I am not showing it as a finished result.",
        image="assets/the-balance-render.jpg", alt="The Balance report as rendered by the Power BI Service", link="https://app.powerbi.com/groups/0c5685bd-1817-447c-8460-ac5858ebf133/reports/a6fa2842-ad87-4599-a826-af7d73747eb3")


example("4b", "Full delegation", "A new brief on the same model, every decision delegated",
        "Brief to client deploy, no questions", "5 hours, 10 engine gaps",
        "A new brief, on purpose: the balance report already existed, so a fresh page shows the setup building from nothing, on the same model. A different report on the same model: trade stripes, one column per month for the whole history. I wrote the brief and granted the delegation. Near the end I granted one more thing: the client deploy for this report. The clip is a replay of the whole session from its saved log (6 minutes 53 seconds, about 10 lines a second): the discovery gate at 37 minutes, the design gate at 62, the first canary at 68, then the render-fix loop the live-render check drove (the stripes first came out as 47 wide columns with a scrollbar), QA, ship approval and the client deploy. 5 hours 11 minutes on the clock, about 3 hours 9 minutes of work after a 2 hour usage-limit pause. Every engine limit it met, it logged instead of patching: 10 gaps, each fixed by a separate builder as its own pull request, reviewed and merged. Be honest about one thing: the delegate was asked for a different model but was served the drafter's own model; only the second checks were independent. That is now fixed in the tool. Press P to play or pause.",
        videos=["media/stripes-session-scroll.mov"], rates=[1], eyebrow="04 &middot; Example 5")
outcome("4b", "04 &middot; Example 5: Full delegation", "16", "measures added", "Plus 2 calculated columns, each verified on the live model", ['_Stripe Colour', '_Stripes Headline', '_Stripes Month Count', '_Stripes Deficit Months', '_Stripes Surplus Months', '_Stripes Period Label', '_Ann First Surplus Month', '_Ann First Surplus Value', '_Ann First Surplus Caption', '_Ann Largest Surplus Month', '_Ann Largest Surplus Value', '_Ann Largest Deficit Month', '_Ann Largest Deficit Value', '_Key Deficit Label', '_Key Surplus Label', '_Stripe Tooltip'],
        "Trade stripes, deployed to the client workspace. QA 34 of 34.",
        "Under full delegation: 16 measures and 2 calculated columns, the stripe colour, the headline, the annotations and the key, each verified against the live model. The report is Trade stripes, 315 months of the trade balance on one portrait page, deployed to the client workspace with QA at 34 of 34.",
        image="assets/trade-stripes-render.jpg", alt="The Trade stripes report as rendered by the Power BI Service", link="https://app.powerbi.com/groups/d0c6c169-2e38-4d56-b8e6-6b0fa2fa7420/reports/65bb19f3-04e4-4522-861a-b2d6734c7b80", fit=True)


# ---- 04 The four compared --------------------------------------------------------------------------------
comp = [("Chat", "No", "No", "No", "No, DAX as text"),
        ("Fabric skills", "Yes, it queries the model", "No", "No", "Published, 1 of 4 checks"),
        ("MCP", "Yes, live", "No", "No", "No, visuals empty"),
        ("My setup", "Yes, checked against live", "Yes, hooks and gates", "Yes, every decision", "Earlier build, same model"),
        ("Full delegation", "Yes, checked against live", "Yes, hooks and gates", "Yes, every decision", "Yes, its own brief, QA 34 of 34")]
yn = lambda v: f'<span class="{"ink-ok strong" if v.startswith("Yes") else "muted"}">{v}</span>'
tr = "".join(f'<tr><td>{a}</td><td>{yn(b)}</td><td>{yn(c)}</td><td>{yn(d)}</td><td>{yn(e)}</td></tr>' for a, b, c, d, e in comp)
slide(f"""
<div class="eyebrow">04 &middot; Examples</div>
<div class="h2">The five, compared</div>
<table class="cmp autoplay vtight" style="margin-top:32px"><thead><tr><th>Approach</th><th>Sees the model</th><th>Can be stopped</th><th>Records decisions</th><th>Report against the brief</th></tr></thead><tbody>{tr}</tbody></table>
""", "Three questions for each approach. Does it see the real model? Chat does not; Fabric skills query it; MCP reads it live; my setup builds against a snapshot that is checked against the live model before every deploy. Can anything stop it being wrong? Only in my setup, through hooks and gates; the other three advise. Is there a record of who decided what? Only in my setup. The gates are plain scripts, so the same idea works with any of the four.")

# ---- Section 05: how I built the tool -------------------------------------------------------------------------
section("05", "How I built the tool", "Specs first, then the engine, then the checks",
        "How the setup behind Example 4 is put together, so you can build your own version. Show the parts live in VS Code; every slide has a screenshot fallback.")

# ---- 05 One spine ---------------------------------------------------------------------------------------------
def snode(ic, t, d, cls=""):
    return f'<div class="fnode snode {cls}">{icon(ic, "ink-accent", "icon")}<div class="small strong" style="margin-top:12px">{t}</div><div class="cap muted">{d}</div></div>'
spine = arrow.join([snode("file-text", "Specs", "19 written algorithms"), snode("cog", "Engine", "One generator"),
                    snode("file-json", "Report files", "Checked against Microsoft's schemas"),
                    snode("shield-check", "Checks", "Hooks, gates and the pipeline", "gate"), snode("rocket", "Deploy", "Only through the pipeline", "you")])
feeds = "".join(snode(ic, t, d) for ic, t, d in [("book-open", "Knowledge", "Visuals, tricks, gotchas"),
                                                 ("wrench", "Microsoft tools", "CLI validator, sample report"),
                                                 ("sparkles", "Skills", "9 recipes for agents"),
                                                 ("briefcase", "Engagement", "Brief, model, decisions")])
slide(f"""
<div class="eyebrow">05 &middot; How I built the tool</div>
<div class="h2">How the tool fits together</div>
<div class="flow mt48 seq">{spine}</div>
<div class="label later" style="margin-top:56px">What feeds the engine</div>
<div class="grid4 later" style="margin-top:16px;gap:16px">{feeds}</div>
<div class="takeaway">A fix goes in the spec or the engine, never in a report file.</div>
""", "Every behaviour starts as a written spec, an algorithm. One engine turns a report config into Power BI report files, always the same way, and validates them against pinned schemas. Checks sit around it: hooks on every commit, the rail of gates, and the pipeline. The only way out is run_pipeline. Feeding it: a knowledge base of visuals and tricks, Microsoft's own CLI validator and sample report as ground truth, ten skills that tell an agent how to do each job, and the engagement itself, the brief, the model and every decision. The rule at the bottom is the one that makes it compound: when a report is wrong, the fix goes where it helps every future report.")

# ---- 05 The building blocks, in my setup ---------------------------------------------------------------------
blocks_table(4, "05 &middot; How I built the tool", "The building blocks, in my setup",
             "The table from the start of the talk, with a fourth column: where each block lives in my setup. Open these in VS Code for 20 seconds each: the render-review skill in .claude/skills; ALG-TEST.md in algorithms; PRINCIPLES.md; the pre-commit config, then the edit guard that stops a report branch editing the engine; step_evidence.py, the rail of 44 steps; engine/builders, one universal builder plus five special ones. Check what is on screen before projecting: no client names.")

# ---- 05 Testing -------------------------------------------------------------------------------------------------
tests = [("0 &middot; Repo", "The engine still behaves", "About 3,100 tests on every push"),
         ("1 &middot; Contract", "The config matches the design", "Blocking rules, Microsoft's validator"),
         ("2 &middot; Data", "Every measure resolves, with plausible values", "Queried live after each deploy"),
         ("3 &middot; Render", "Every text whole, the page reviewed", "Live page measured, reviewed by another model"),
         ("4 &middot; Interaction", "Clicks and hovers do what was promised", "A headless QA runner, a person as fallback")]
tr = "".join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in tests)
slide(f"""
<div class="eyebrow">05 &middot; How I built the tool</div>
<div class="h2">Testing in five layers</div>
<table class="cmp tight vtight autoplay" style="margin-top:24px"><thead><tr><th>Layer</th><th>Proves</th><th>How</th></tr></thead><tbody>{tr}</tbody></table>
""", "Each layer catches what the one before cannot. Repo: about three thousand tests run on every commit. Contract: the config is checked against the design and against Microsoft's own validator. Data: every measure is queried live after a deploy. Render: the deployed page is measured for clipped text and judged by a model that did not build it; that layer exists because a clipped card once passed every other check. Interaction: a headless runner clicks and hovers through every item; a person drives what it cannot. Two teams: QA never fixes, and the builder never closes its own bug.")

# ---- 05 UX principles -------------------------------------------------------------------------------------------
order = ["The surface: report, dashboard or app", "The person and their job", "Flow and empty states", "The canvas, then fixed",
         "Layout: one hero, the rest quiet", "Interaction: remove what you can", "Accessibility", "Data honesty", "Critique: cut what does not serve the job"]
enforced = ["Every text whole in the live render", "No em dashes in visible copy"]
warns = ["Text contrast"]
ol = "".join(f'<div class="small"><span class="label" style="margin-right:16px">{i}</span>{t}</div>' for i, t in enumerate(order))
el = ("".join(f'<div class="small">{icon("shield-check", "rose")} {t}</div>' for t in enforced)
      + '<div class="label" style="margin-top:16px">Warns only</div>'
      + "".join(f'<div class="small">{icon("triangle-alert", "rose")} {t}</div>' for t in warns))
slide(f"""
<div class="eyebrow">05 &middot; How I built the tool</div>
<div class="h2">Design rules</div>
<div class="grid2 mt32" style="grid-template-columns:3fr 2fr;align-items:stretch">
  {card(f'<div class="h4">The design order</div><div class="list" style="margin-top:24px;gap:14px">{ol}</div>')}
  <div class="card inkcard"><div class="h4 rose">Fails the build</div><div class="list" style="margin-top:24px;gap:24px">{el}</div></div>
</div>
""", "The design order every page follows, from the person and their goal down to pixels, never the reverse: the surface first, report, dashboard or app; then who the user is and the job they need done; flow and empty states; the canvas, fixed once chosen; layout with one hero and everything else quiet; the interaction you can remove; accessibility; data honesty; and a critique that cuts anything not serving the job. On the right, the ones that are not advice: each is a check that fails the build or the deploy.")

# ---- 05 Sample prompts: what each one says, and what it stops ----------------------------------------------------
PROMPTS = [("Operator", "play", "r-op",
            "New page for uk-trade-data, report name \"UK Trade - Trade stripes\". The brief is below. You are the operator: run the tool and write only under clients/. When the tool cannot do something, log a gap, use the nearest supported option, and carry on. Never ask me.",
            "The build session editing the engine, with a hook behind it"),
           ("Builder", "wrench", "r-build",
            "Fix this in the engine, never in a report file. Reproduce it, find the root cause, write the spec first if the behaviour has none, add a test that fails without the fix, and open a pull request. Do not merge.",
            "A fix in a report file that the next build overwrites"),
           ("Architecture", "compass", "r-orch",
            "Before you build anything new: is there a spec for it? If not, write the algorithm first, then the engine, then the check that enforces it. One generator, no second path.",
            "A second way of doing the same thing")]
pcards = "".join(card(f'<span class="rchip {rc}" style="margin-top:0">{icon(ic, "", "icon-sm")}{name}</span>'
                      f'<div class="prompt">{text}</div>'
                      f'<div class="split"><div class="label ink-accent">What it stops</div><div class="small strong" style="margin-top:8px">{stops}</div></div>', "stretch")
                 for name, ic, rc, text, stops in PROMPTS)
slide(f"""
<div class="eyebrow">05 &middot; How I built the tool</div>
<div class="h2">Three prompts</div>
<div class="grid3 mt32 stagger" style="gap:32px;align-items:stretch;grid-template-columns:repeat(3, minmax(0, 1fr))">{pcards}</div>
""", "Three prompts, shortened from the real ones. Operator: the opening of the Trade stripes prompt; the full text is in demos/04-skills-plus-own/prompt-trade-stripes.txt, with the brief underneath. Builder: the shape of every builder task, reproduce, root cause, spec first, a failing test, a pull request nobody merges without review. Architecture: the question I ask before anything new is built, which keeps the tool to one spine. Most of the length of a good prompt is the brief, not the instructions.")

# ---- 05 Deliverables --------------------------------------------------------------------------------------------
dels = [("Report", "On the canary and in the client workspace"), ("Design contract", "Challenged by a second model, then decided"),
        ("Mockup", "Drawn from a sample of live data"), ("Design brief", "Acceptance tests for every element"),
        ("Decision records", "16, each with its reasoning"), ("QA report", "34 of 34 items passed"),
        ("Deliverable pack", "Walkthrough, measures, proof points"), ("Report guide", "Plain English, for the reader; shown next")]
dl = "".join(f'<div class="line"><div class="h4">{t}</div><div class="small" style="margin-top:8px">{d}</div></div>' for t, d in dels)
slide(f"""
<div class="eyebrow">05 &middot; How I built the tool</div>
<div class="h2">Deliverables for one report</div>
<div class="grid2 mt32" style="gap:96px"><div class="lines stagger">{"".join(f'<div class="line"><div class="h4">{t}</div><div class="small" style="margin-top:8px">{d}</div></div>' for t, d in dels[:4])}</div><div class="lines stagger later">{"".join(f'<div class="line"><div class="h4">{t}</div><div class="small" style="margin-top:8px">{d}</div></div>' for t, d in dels[4:])}</div></div>
""", "Everything the Trade stripes run handed over, all generated and all in the engagement folder: the report itself, the design contract and the second model's challenge to it, a mockup drawn from real data, a design brief with an acceptance test per element, sixteen decision records with reasoning, the QA report, and the deliverable pack with a page walkthrough, the measure dictionary and every proof point. The next slide shows a report guide, the one for The Balance. The sixteen decision records name the model that was requested, claude-fable-5-1; the drafter's own model is the one that answered. Open the folder live if there is time.")

# ---- 05 Final documentation -------------------------------------------------------------------------------------
slide(f"""
<div class="eyebrow">05 &middot; How I built the tool</div>
<div class="h2">The report guide</div>
<div class="grid2 mt32" style="grid-template-columns:3fr 1fr;gap:48px;align-items:start">
  <div style="height:600px">{viewer("guide", "assets/report-guide.png", "The generated report guide for The Balance", "docs/the-balance/4-Governance/DOCUMENTATION-01-the-balance.html", "Open the report guide")}</div>
  <div class="lines"><div class="line"><div class="h4">For the reader</div><div class="small" style="margin-top:8px">Not for the people who built it</div></div>
  <div class="line"><div class="h4">Matches gov.uk</div><div class="small" style="margin-top:8px">Every figure, to within 0.005%</div></div>
  <div class="line"><div class="h4">Explains the design</div><div class="small" style="margin-top:8px">What it shows, and why it looks the way it does</div></div></div>
</div>
""", "The last deliverable: the report guide, written for the people who use the report, not the people who built it. Every figure on it matches the published gov.uk numbers to within 0.005%. It explains what the report tells you, the headline numbers, and the thinking behind the design. Open the HTML live: it has a dark mode and prints to PDF.")

# ---- Section 06: cost and limits -------------------------------------------------------------------------------
section("06", "Cost and limits", "Time, tokens, and what still needs a person",
        "The honest part. Numbers from the fully delegated run, then the limits, then when not to use any of this.")

# ---- 06 What one delegated report cost ------------------------------------------------------------------------
stats = [("5 h 11 min", "On the clock, brief to client deploy"), ("3 h 9 min", "Working, after a 2 hour usage-limit pause"),
         ("0", "Questions to me"), ("225 million", "Tokens read from cache, mostly the session re-reading its own history"),
         ("6", "Render fixes, none by me"), ("10", "Engine gaps logged, each fixed by a builder")]
sc = "".join(card(f'<div class="h2" style="margin:0" data-countup>{n}</div><div class="small" style="margin-top:16px">{d}</div>') for n, d in stats)
slide(f"""
<div class="eyebrow">06 &middot; Cost and limits</div>
<div class="h2">What one delegated report cost</div>
<div class="grid3 stagger" style="margin-top:32px;grid-template-rows:repeat(2, 1fr);gap:32px">{sc}</div>
""", "The Trade stripes run, measured. Five hours eleven on the clock, about three hours of work, because the account hit its usage limit for two hours in the middle. Nothing was asked of me. Most of the tokens are the session re-reading its own history on every step, 225 million reads from cache; splitting a run into a fresh session per phase is the obvious fix. Six render fixes, none of them by me: most driven by the live checks, one by QA, one the run's own readability call. Ten engine gaps logged, each fixed separately by a builder as a pull request, now reviewed and merged.")

# ---- 06 Where it still needs you ------------------------------------------------------------------------------
lims = [("A new kind of page finds gaps", "One page, ten engine gaps. The engine only does what it has been taught."),
        ("The deciding model was not the one asked for", "The delegate asked for one model and was served the drafting model. The tool now records which model answered and blocks the drafter's."),
        ("Approvals reopen on harmless changes", "A colour written as a hex instead of a name re-ran the whole sign-off chain."),
        ("Usage limits pause long runs", "Two hours of waiting in a five-hour run."),
        ("Someone has to own the grant", "What may be delegated, and the client deploy, stay with a person.")]
ll = "".join(f'<div class="line"><div class="h4">{t}</div><div class="small" style="margin-top:8px">{d}</div></div>' for t, d in lims)
slide(f"""
<div class="eyebrow">06 &middot; Cost and limits</div>
<div class="h2">Limits</div>
<div class="grid2" style="margin-top:32px;gap:96px"><div class="lines stagger">{"".join(f'<div class="line"><div class="h4">{a}</div><div class="small" style="margin-top:8px">{b}</div></div>' for a, b in lims[:3])}</div><div class="lines stagger later">{"".join(f'<div class="line"><div class="h4">{a}</div><div class="small" style="margin-top:8px">{b}</div></div>' for a, b in lims[3:])}</div></div>
""", "Five honest limits from the last two weeks. A new kind of page finds gaps: the engine only does what it has been taught, and one new page found ten. Proving which model decided: my delegate was asked for a different model and was quietly served the drafting one, so for a while the independent decision was not independent; the tool now reads which model actually answered and refuses otherwise. Approvals reopen on harmless changes: correct, but wasteful. Usage limits: plan for them. And someone owns the grant: what may be delegated, and the deploy to the client.")

# ---- 17 The mistake --------------------------------------------------------------------------------------
TICKS = "".join(f'<span class="tick">{icon("circle-check", "ink-ok", "icon-sm")}{t}</span>' for t in ["Gates", "DAX", "Mockup match"])


def bug_card(head, what, found):
    return card(f'<div class="h4">{head}</div><div class="small" style="margin-top:12px;line-height:1.4">{what}</div>'
                f'<div class="label" style="margin-top:28px">Checks that passed</div><div class="row g16" style="margin-top:12px;flex-wrap:wrap">{TICKS}</div>'
                f'<div class="split"><div class="label ink-accent">How it was found</div><div class="small strong" style="margin-top:8px">{found}</div></div>', "roomy")
slide(f"""
<div class="eyebrow">06 &middot; Cost and limits</div>
<div class="h2">Two bugs the checks missed</div>
<div class="grid2 mt48 stagger" style="align-items:stretch">
  {bug_card("The slicer did not filter the chart", "It was on the page and you could click it. The chart never changed.", "Clicking it in the Service.")}
  {bug_card("The headline card clipped its figures", "The figures were clipped inside the card.", "A person looked at the published page, after it had gone out three times.")}
</div>
<div class="takeaway">No check read the published page.</div>
""", "G-05 / BUG-02-001. The field-parameter slicer rendered, accepted a selection, and drove nothing at all. The engine never emitted the binding on the consuming chart, so the chart stayed on one fixed measure. Gates passed, DAX passed, render-match passed. A person clicking the slicer found it. Second story, from the delegated runs: the headline card clipped its own figures and labels, and went out to the canary three times with every check green, because nothing measured the deployed page. The fixes: a live check that measures every text on the deployed page and fails a clipped one, a review of the rendered page by a model that did not build it, and a headless QA runner that clicks the slicer. Both mistakes would now be caught.")

# ---- 06 When to use which -------------------------------------------------------------------------------------
uses = [("Chat", "One measure or a quick question", "No setup, nothing checked"),
        ("Fabric skills", "A prototype, or a report you will not rebuild", "Real file formats, advice only"),
        ("MCP", "You need the live model's real answers", "Real figures, but nothing stops a wrong write"),
        ("My setup", "Reports you rebuild, check and hand over", "Upfront cost and upkeep")]
tr = "".join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in uses)
slide(f"""
<div class="eyebrow">06 &middot; Cost and limits</div>
<div class="h2">Which approach, when</div>
<table class="cmp autoplay" style="margin-top:32px"><thead><tr><th>Use</th><th>When</th><th>Trade-off</th></tr></thead><tbody>{tr}</tbody></table>
""", "None of this replaces the others. For one measure, plain chat is the right tool. For a prototype or a report you will never rebuild, Microsoft's Fabric skills are quick and good. When you need the real numbers from the live model, MCP. My own setup only pays back for reports you rebuild, check and hand over with an audit trail: it is overkill for one-off work, and I say so.")

# ---- 18 What to check, and what stays yours --------------------------------------------------------------
def item(t, d):
    return f'<div class="line"><div class="h4">{t}</div><div class="small" style="margin-top:8px">{d}</div></div>'
checks = [("Measures resolve live", "Every one, against the real model"),
          ("Every text whole", "Measured on the deployed page"),
          ("It survives a refresh", "Colours, sorts, and filters on new data")]
yours = [("Write the brief", "Who it is for, and what done means"),
         ("Decide what to delegate", "Which gates, and never the client deploy by default"),
         ("Review what the builder changed", "Every engine fix is yours to merge")]
slide(f"""
<div class="eyebrow">06 &middot; Cost and limits</div>
<div class="h2">What to check, and what you do yourself</div>
<div class="grid2 mt48" style="gap:96px;align-items:start">
  <div><div class="label">A check that runs</div><div class="lines">{"".join(item(*c) for c in checks)}</div></div>
  <div><div class="label ink-accent">You</div><div class="lines">{"".join(item(*c) for c in yours)}</div></div>
</div>
<div class="takeaway">Checks find the mistakes. You decide what done means.</div>
""", "Does every measure resolve live. Does the model contain what was actually asked for. Does the report survive a refresh. Those can be checks that run. The three on the right are yours even under full delegation: writing the brief, deciding what may be delegated, and reviewing every change the builder makes to the tool. They are the parts where judgement is the work. What makes it reliable is not the prompt: it is a spec it can be checked against, a bar set before it starts, and gates it cannot walk past. I would rather have a tool that tells me it shipped with caveats than one that tells me it is done.")

# ---- Close: three things to try ---------------------------------------------------------------------------------
monday = [("01", "Write down how you work", "A CLAUDE.md or AGENTS.md: your model, your names, your rules"),
          ("02", "Add one hook", "Block the one mistake you have made twice"),
          ("03", "Ask for a check before every deploy", "And read it before you approve")]
mc = "".join(card(f'<div class="label">{n}</div><div class="h4" style="margin-top:16px">{t}</div><div class="small" style="margin-top:16px">{d}</div>', "roomy") for n, t, d in monday)
slide(f"""
<div class="eyebrow">Next steps</div>
<div class="h2">Three things to try</div>
<div class="grid3 mt48 stagger" style="align-items:stretch">{mc}</div>
""", "Three small steps, none needs my setup. Write down how you work, in a CLAUDE.md or AGENTS.md: your model, your names, your rules. Add one hook that refuses the one mistake you have made twice. And ask for a check before every deploy, and read it before you approve. That is the whole idea in miniature: advice, then something that blocks, then a person at the gate.")


# ---- 19 Close: the same profile as the opening, on the rose-gold close --------------------------------------
slide(profile("Thank you"), "Thank you. Same as at the start: data-nova.io and linkedin.com/in/prathy. Check both links before the day.", dark=True)

# ---- Feedback: a QR code to the form, last, so it can stay up during questions -----------------------------------
slide("""
<div class="feedback">
  <div class="qrbox"><img src="assets/feedback-qr.svg" alt="QR code for the session feedback form"></div>
  <div>
    <div class="eyebrow">Feedback</div>
    <div class="h1c" style="margin-top:16px">How was this session?</div>
    <div class="body" style="margin-top:32px">Scan the code to fill in the feedback form.</div>
    <div class="small muted" style="margin-top:16px">data-nova.notion.site</div>
  </div>
</div>
""", "", dark=True)


# ---- speaker notes: short pointers per slide, in order. Each entry names text its slide must contain, so a moved
# or new slide stops the build instead of getting the wrong notes. The long notes are in the v1 snapshot.
POINTERS = [
    ("Agentic BI Development", "Welcome\nWhat it takes to trust an agent's BI work"),
    ("About me", "Solopreneur at Data Nova: Fabric and Power BI\nMVP, London Fabric user group, blog, talks, YouTube\nEverything else is on LinkedIn"),
    ("This session", "An agent can build a real model and report from a spec\nWhat makes it reliable: a clear spec, a bar set before it starts, a proper review\nYou leave knowing what to check"),
    ("Who uses AI for anything", "Show of hands: AI for anything at all\nMost hands go up"),
    ("Who uses it for BI work", "Now: AI in your BI work\nFewer hands. That gap is today"),
    ("Agenda", "Six parts\nConcepts first, then one brief through different tools, then how I built mine\nLast: cost, and what still needs a person"),
    ("What is BI development?", "Before agents: what the job is"),
    ("From a question to a trusted report", "Six steps, with or without an agent\nAsk who does each one today\nDiscovery, Test and Govern are where trust is earned, and where agents are weakest\nMost of the time is not in Build"),
    ("A capable graduate on day one", "An agent can help with every step\nFirst: what kind of colleague are we handing work to"),
    ("Treat it like a new graduate", "Knows the tools and the public docs\nDoes not know your model, your names, your sign-offs\nSo you tell it, give it recipes, set limits, check its work"),
    ("Plain chat", "What most of us do today. P to play\nNo skills, no access to the model\nFirst prompt invents table names. With the schema pasted, it gets them right"),
    ("Without the schema, then with it", "Left: invented names. 'Trade'[Exports] does not exist\nRight: real names, after I pasted the schema\nIt works, but I pasted it by hand, and it goes stale"),
    ("What you get: text to paste", "Model: nothing. It cannot reach it\nReport: none. DAX as text, the rest by hand\nFine for one measure"),
    ("How chat differs from an agent", "Chat answers once\nAn agent loops: plan, act with tools, check the result, go again\nIt can fix its own mistakes, and build on them\nThe loop needs a gate. That is you"),
    ("The building blocks</div>", "Eight ways to tell an agent how you work\nMost people know two or three\nNext: what kind each one is"),
    ("What kind each one is", "Advisory: it can skip them\nStructure: algorithms set the order of the work\nBlocking: loops, hooks, gates. It cannot walk past them\nMCP is reach, not control"),
    ("What each one does", "One line each\nWhere each one lives in my setup comes later"),
    ("Advisory, hook or gate?", "Advisory: it decides. Hook: blocks one action. Gate: no evidence, no next phase\nReal story: an agent changed the engine from a report branch\nA rule in the prompt was not enough. A hook fixed it"),
    ("An algorithm for each phase", "44 steps across six phases, each one written down\nThe labels map back to the six steps\nFive gates, named on the cards"),
    ("Operator, builder, orchestrator, and you", "Who does what once the blocks are in place"),
    ("Four roles", "Operator runs the tool and writes only the deliverables\nBuilder changes the tool, on a branch, with tests\nOrchestrator hands out decisions in order\nYou decide what can be delegated"),
    ("Who does what, step by step", "The same six steps, split by who does the work\nThe agent drafts, builds, checks, deploys and records\nYou sign off, review and accept"),
    ("How a report gets made", "Left to right: requirement to client deploy\nA question at the gate sends it back\nUnderneath: a gap gets logged, a builder fixes it, I review"),
    ("You sign four gates", "Human gate: I sign four gates\nQA is a check that runs\nSafe, but I am in the loop all day"),
    ("Full delegation</div>", "Full delegation: another model decides, a third checks the gates\nThe client deploy stays mine unless I grant it\nIn my runs the deciding model was the drafter's own. The tool now catches that"),
    ("Building the trade balance report", "One brief through different tools, then full delegation"),
    ("UK trade, the balance", "The brief: four things to build, three done checks\nThe figures to match: £937.0bn exports, £980.4bn imports\nChat got one prompt. Full delegation got a new brief"),
    ("Microsoft's Fabric skills, same brief", "Microsoft's Fabric skills. P to play, 12 times speed\nReal file formats, a draft in minutes\nAdvisory and opt-in"),
    ("Example 2: Fabric skills", "Model: nothing written\nReport: published when asked, on the DirectLake model\nOne of four checks met: all-years totals, empty partners chart"),
    ("Power BI authoring MCP", "Copilot in VS Code with Microsoft's Power BI MCP. P to play\nIt read the real model and got the figures right"),
    ("PBIP files on the laptop", "Model: nothing. The connection was read only\nReport: PBIP files on the laptop. It could not publish\nWith a writable connection it can change the model, and nothing asks you first"),
    ("Publishing the MCP report", "As built, the Service refused it. Five validator errors\nOne line removed by hand, and it published\nEvery visual is empty: right numbers, a report that does not work"),
    ("Live demo", "My setup, live in the terminal\nFirst: a check stops a report whose design was not approved\nThen one command builds the report and runs every check"),
    ("Open Mission Control", "Where every page stands, in one view\nThe rail: 44 steps, the evidence for each, who decided each gate\nOpen it live: python3 scripts/mission_control.py serve, then the button\nPage 07 reads go for launch"),
    ("Example 4: My setup", "19 measures and 3 columns, each verified on the live model\nThe Balance was built before this brief, on the same model\nAgainst this brief: no slicer, no breakdown"),
    ("A new brief on the same model", "A new brief, every decision delegated. P to play\nDiscovery gate at 37 minutes, design gate at 62, first canary at 68\nEngine limits logged, not patched: 10 gaps"),
    ("Example 5: Full delegation", "16 measures and 2 columns, each verified on the live model\nTrade stripes: 315 months on one page\nClient workspace, QA 34 of 34"),
    ("The five, compared", "Four questions for each approach\nOnly my setup can be stopped and records its decisions\nFull delegation met its own brief; The Balance predates this one\nThe upfront cost is real"),
    ("Specs first, then the engine, then the checks", "How my setup is built, so you can build your own"),
    ("How the tool fits together", "Specs, then the engine, then checks, then deploy\nKnowledge, Microsoft's tools, skills and the engagement feed the engine\nA fix goes in the spec or the engine, never in a report file"),
    ("The building blocks, in my setup", "The same table, plus where each one lives\nOpen two or three in VS Code"),
    ("Testing in five layers", "Five layers, from the repo to the interactions\nEach catches what the layer before cannot"),
    ("Design rules", "The order every page follows: the person first, pixels last\nTwo checks block a build. Contrast is advisory"),
    ("Three prompts", "Shortened from the real ones\nEach one guards against one mistake"),
    ("Deliverables for one report", "Everything one run hands over\nAll in the engagement folder"),
    ("The report guide", "For the people who use the report\nEvery figure matches gov.uk\nOpen it with the button"),
    ("Time, tokens, and what still needs a person", "The honest part"),
    ("What one delegated report cost", "5 h 11 on the clock, about 3 h of work\nMost tokens are the session re-reading its own history\nNo questions to me. 10 gaps, all fixed by builders"),
    ("Limits</div>", "A new kind of page finds gaps\nProve which model decided\nUsage limits pause long runs\nSomeone owns the grant"),
    ("Two bugs the checks missed", "Both passed every check\nNo check read the published page\nNow: a live text check, a render review, and QA that clicks"),
    ("Which approach, when", "Chat for one measure\nFabric skills for a prototype\nMCP for live answers\nMy setup for reports you rebuild and hand over"),
    ("What to check, and what you do yourself", "Left: checks that can run\nRight: yours, even under full delegation"),
    ("Three things to try", "Write down how you work\nAdd one hook\nAsk for a check before every deploy"),
    ("Thank you", "Thank you. Questions\ndata-nova.io and LinkedIn"),
    ("How was this session?", "Leave this up during questions\nAsk them to scan it now"),
]
assert len(POINTERS) == len(SLIDES), f"{len(POINTERS)} notes for {len(SLIDES)} slides"
for k, (must, text) in enumerate(POINTERS):
    body, _notes, dark = SLIDES[k]
    assert must in body, f"slide {k + 1}: notes for '{must}' do not match this slide"
    SLIDES[k] = (body, "\n".join("• " + line for line in text.split("\n")), dark)

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
<div id="hint">arrows: move &nbsp; N: notes &nbsp; P: play video &nbsp; F: fullscreen &nbsp; A: overview &nbsp; S: presenter view &nbsp; B: black &nbsp; E: expand image</div>
<script src="vendor/lucide.min.js"></script>
<script src="deck.js"></script>
</body></html>
"""
Path(__file__).with_name("index.html").write_text(html)
print(f"wrote index.html: {total} slides")


# ---- web: a copy for the Data Nova website ----------------------------------------------------------------------
# python3 build.py --web writes web/: the same deck for a public page under the site's strict Content Security
# Policy (style-src 'self', no inline style). Every style="..." becomes a class in web.css. Speaker notes, the
# presenter view and the key hint go; so do buttons that only work on this laptop (Mission Control) or need a
# sign-in (the Power BI reports) and the report guide (its page loads fonts and a chart library from other hosts).
# A video becomes an unlisted YouTube player when its ID is in YOUTUBE, and a still frame until then.
YOUTUBE = {  # media file -> (unlisted YouTube video ID, start second)
    "media/chatVideo.m4v": ("gPYhDnthTUo", 0),
    "media/Fabric skills-2.m4v": ("F2uZcREfzN8", 0),  # the 12x, cropped cut: starts after the account details
    "media/mcp-chat-scroll.mov": ("SfxBXoHRhRU", 0),
    "media/stripes-session-scroll.mov": ("l_4nHIu0M5k", 0),
}
WEB_STILLS = {"media/chatVideo.m4v": 40, "media/Fabric skills-2.m4v": 900, "media/mcp-chat-scroll.mov": 60,
              "media/stripes-session-scroll.mov": 200}  # second to take the still from

import re as _re
import shutil as _shutil
import subprocess as _sp
import sys as _sys

if "--web" in _sys.argv:
    here = Path(__file__).parent
    WEB_SLUG = "agentic-bi-development"
    web = here / "web"
    if web.exists():
        _shutil.rmtree(web)
    out = web / WEB_SLUG
    out.mkdir(parents=True)
    w = html
    w = _re.sub(r'<template class="notes">.*?</template>', "", w, flags=_re.S)
    w = _re.sub(r'<div id="hint">.*?</div>\n', "", w, flags=_re.S)
    w = w.replace('<body data-type-context="slide">', '<body data-type-context="slide" data-web>')
    # buttons that cannot work for a visitor
    w = _re.sub(r'<button class="vbtn" type="button" data-href="(?:http://127\.0\.0\.1[^"]*|https://app\.powerbi\.com[^"]*|docs/[^"]*)">.*?</button>', "", w, flags=_re.S)
    (out / "assets" / "web").mkdir(parents=True)

    def video(m):
        tag = m.group(0)
        src = _re.search(r'data-playlist="([^",]+)', tag).group(1)
        yt = YOUTUBE.get(src)
        if yt:
            vid, start = yt
            return (f'<div class="ytwrap"><iframe src="https://www.youtube-nocookie.com/embed/{vid}?start={start}&amp;rel=0" '
                    f'title="Session recording" loading="lazy" allow="encrypted-media; picture-in-picture; fullscreen" allowfullscreen></iframe></div>')
        still = f"assets/web/{Path(src).stem.replace(' ', '-')}.jpg"
        png = out / "assets" / "web" / (Path(src).stem.replace(" ", "-") + ".png")
        grab = Path("/private/tmp/claude-501/-Users-prathy-agentic-bi-demo/29b832f4-a377-4247-95db-0a3809151666/scratchpad/replay/grab")
        t = WEB_STILLS.get(src, 30)
        _sp.run([str(grab), str(here / src), str(png)[:-len(f"{t}.png")] if False else str(png.with_suffix("")), str(t)], capture_output=True)
        made = png.with_name(png.stem + f"{t}.png")
        if made.exists():
            _sp.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "82", "--resampleWidth", "1600", str(made), "--out", str(out / still)], capture_output=True)
            made.unlink()
        return f'<img class="clip still" src="{still}" alt="A still from the session recording">'
    w = _re.sub(r'<video [^>]*data-playlist="[^"]*"[^>]*></video>', video, w)
    # inline styles become classes
    styles = {}

    def cls(m):
        st = m.group(1).strip().rstrip(";")
        name = styles.setdefault(st, f"w{len(styles) + 1}")
        return f' data-w="{name}"'
    w = _re.sub(r' style="([^"]*)"', cls, w)
    w = _re.sub(r'(<[a-zA-Z][^>]*?) class="([^"]*)"([^>]*?) data-w="(w\d+)"', r'\1 class="\2 \4"\3', w)
    w = _re.sub(r' data-w="(w\d+)"', r' class="\1"', w)
    leftover = _re.findall(r' style="', w)
    assert not leftover, f"{len(leftover)} inline styles left in the web copy"
    css = "/* generated by build.py --web: the deck's inline styles as classes */\n" + "\n".join(
        f".{n} {{ {st}; }}" for st, n in styles.items())
    css += "\n.ytwrap { position: relative; width: 100%; height: 100%; border-radius: 12px; overflow: hidden; background: var(--das-ink); }\n" \
           ".ytwrap iframe { position: absolute; inset: 0; width: 100%; height: 100%; border: 0; }\n" \
           ".clip.still { object-fit: contain; }\n"
    (out / "web.css").write_text(css)
    w = w.replace('<link rel="stylesheet" href="deck.css">', '<link rel="stylesheet" href="deck.css">\n<link rel="stylesheet" href="web.css">')
    w = w.replace('<script src="vendor/lucide.min.js"></script>\n', "")
    w = _sp.run(["node", str(here / "tools" / "inline-icons.js")], input=w, capture_output=True, text=True, check=True).stdout
    # the site serves this page at /talks/<slug> (no trailing slash); its files sit in the folder of the same name
    w = w.replace("<head>", f'<head>\n<base href="/talks/{WEB_SLUG}/">', 1)
    (web / f"{WEB_SLUG}.html").write_text(w)
    for f in ["styles.css", "base.css", "deck.css", "deck.js"]:
        _shutil.copy(here / f, out / f)
    for d in ["tokens", "alchemy", "fonts", "components"]:
        _shutil.copytree(here / d, out / d)
    for f in sorted((here / "assets").rglob("*")):
        if f.is_file():
            (out / f.relative_to(here)).parent.mkdir(parents=True, exist_ok=True)
            _shutil.copy(f, out / f.relative_to(here))
    print(f"wrote web/{WEB_SLUG}.html and web/{WEB_SLUG}/: {total} slides, {len(styles)} inline styles moved to web.css")
