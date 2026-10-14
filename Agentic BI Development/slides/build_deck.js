// Builds agentic-bi-development.pptx. Run: node build_deck.js
// Brand: Data Nova (navy, teal, violet). Fonts are constants so they can be swapped for Outfit/Inter in one place.
const pptxgen = require("pptxgenjs");
const path = require("path");
let applyTheme = null; // optional: needs the pptx skill's scripts/apply_theme.js (set PPTX_SKILL_DIR and NODE_PATH)
try {
  if (process.env.PPTX_SKILL_DIR) applyTheme = require(path.join(process.env.PPTX_SKILL_DIR, "scripts/apply_theme.js")).applyTheme;
} catch (e) { /* theme step skipped */ }

const HEAD = "Arial"; // brand: Outfit
const BODY = "Calibri"; // brand: Inter
const MONO = "Courier New"; // brand: JetBrains Mono

const THEME = {
  name: "Data Nova",
  headFontFace: HEAD,
  bodyFontFace: BODY,
  colors: {
    dk1: "4A4A4A", lt1: "FFFFFF", dk2: "1A1530", lt2: "F2F2F2",
    accent1: "20B8A8", accent2: "5C4E8A", accent3: "F7B731",
    accent4: "2ECC71", accent5: "E74C3C", accent6: "C9BFBA",
    hlink: "20B8A8", folHlink: "5C4E8A",
  },
};

const pres = new pptxgen();
pres.layout = "LAYOUT_16x9"; // 10 x 5.625 in
pres.theme = { headFontFace: HEAD, bodyFontFace: BODY };
pres.title = "Agentic BI Development";
pres.author = "Prathy Kamasani";
pres.company = "Data Nova";
const C = pres.SchemeColor;

const NAVY = C.text2, TEXT = C.text1, WHITE = C.background1, OFF = C.background2;
const TEAL = C.accent1, VIOLET = C.accent2, GOLD = C.accent3, GREEN = C.accent4, RED = C.accent5;
const LAV = "F0EEF8";

const shadow = () => ({ type: "outer", color: "1A1530", opacity: 0.1, blur: 6, offset: 2, angle: 90 });

// ---------- layouts ----------
pres.defineSlideMaster({
  title: "TITLE", background: { color: NAVY },
  objects: [],
  slideNumber: undefined,
});
pres.defineSlideMaster({
  title: "SECTION", background: { color: NAVY },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.6, y: 1.5, w: 8.6, h: 1.5, fontFace: HEAD, fontSize: 40, bold: true, color: WHITE, valign: "bottom", align: "left", margin: 0 }, text: "" } },
    { placeholder: { options: { name: "body", type: "body", x: 0.6, y: 3.2, w: 7.6, h: 1.0, fontFace: BODY, fontSize: 18, color: LAV, valign: "top", align: "left", margin: 0 }, text: "" } },
  ],
});
pres.defineSlideMaster({
  title: "CONTENT", background: { color: OFF },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: 0.5, y: 0.3, w: 9, h: 0.8, fontFace: HEAD, fontSize: 30, bold: true, color: NAVY, valign: "middle", align: "left", margin: 0 }, text: "" } },
    { text: { text: "Agentic BI Development  |  Prathy Kamasani, Data Nova", options: { x: 0.5, y: 5.2, w: 6, h: 0.25, fontFace: BODY, fontSize: 10, color: "888888", margin: 0 } } },
  ],
  slideNumber: { x: 9.0, y: 5.2, w: 0.5, h: 0.25, fontFace: BODY, fontSize: 10, color: "888888" },
});

// ---------- helpers ----------
function card(s, x, y, w, h, opts = {}) {
  s.addShape(pres.ShapeType.roundRect, {
    x, y, w, h, rectRadius: 0.1,
    fill: { color: opts.fill || WHITE },
    line: { color: opts.line || "E3E0EE", width: 0.75 },
    shadow: opts.noShadow ? undefined : shadow(),
    objectName: opts.name || "card",
  });
}
function txt(s, text, o) {
  s.addText(text, Object.assign({ isTextBox: true, margin: 0, fontFace: BODY, fontSize: 14, color: TEXT, valign: "top" }, o));
}
function heading(s, text, o) {
  txt(s, text, Object.assign({ fontFace: HEAD, bold: true, color: NAVY, fontSize: 16 }, o));
}
function dot(s, x, y, d, color, label, labelColor) {
  s.addShape(pres.ShapeType.ellipse, { x, y, w: d, h: d, fill: { color }, line: { color, width: 0 }, objectName: "dot" });
  if (label !== undefined)
    s.addText(String(label), { x, y, w: d, h: d, isTextBox: true, align: "center", valign: "middle", margin: 0, fontFace: HEAD, bold: true, fontSize: Math.round(d * 28), color: labelColor || WHITE });
}
function pill(s, x, y, w, text, fill, color) {
  s.addShape(pres.ShapeType.roundRect, { x, y, w, h: 0.3, rectRadius: 0.15, fill: { color: fill }, line: { color: fill, width: 0 }, objectName: "pill" });
  s.addText(text, { x, y, w, h: 0.3, isTextBox: true, align: "center", valign: "middle", margin: 0, fontFace: MONO, fontSize: 12, bold: true, color: color || WHITE });
}
function content(title, notes) {
  const s = pres.addSlide({ masterName: "CONTENT" });
  s.addText(title, { placeholder: "title" });
  if (notes) s.addNotes(notes);
  return s;
}
function section(title, sub, notes) {
  const s = pres.addSlide({ masterName: "SECTION" });
  s.addText(title, { placeholder: "title" });
  if (sub) s.addText(sub, { placeholder: "body" });
  if (notes) s.addNotes(notes);
  return s;
}

// ================= 1. Title =================
{
  const s = pres.addSlide({ masterName: "TITLE" });
  txt(s, "Agentic BI Development", { x: 0.6, y: 0.9, w: 6.1, h: 1.7, fontFace: HEAD, bold: true, fontSize: 44, color: WHITE, valign: "bottom" });
  txt(s, "What an agent can build, what you still have to check, and four ways to work with one", { x: 0.6, y: 2.8, w: 6.0, h: 1.2, fontSize: 18, color: LAV });
  txt(s, "Prathy Kamasani  |  Data Nova", { x: 0.6, y: 4.55, w: 6, h: 0.35, fontSize: 16, color: TEAL, bold: true });
  // orbit motif, echoing the logo
  s.addShape(pres.ShapeType.ellipse, { x: 7.0, y: 0.7, w: 2.6, h: 2.6, fill: { color: NAVY }, line: { color: VIOLET, width: 2.5 }, objectName: "orbit" });
  s.addShape(pres.ShapeType.ellipse, { x: 7.65, y: 1.35, w: 1.3, h: 1.3, fill: { color: NAVY }, line: { color: TEAL, width: 2.5 }, objectName: "orbit-inner" });
  s.addShape(pres.ShapeType.ellipse, { x: 8.15, y: 1.85, w: 0.3, h: 0.3, fill: { color: TEAL }, line: { color: TEAL, width: 0 }, objectName: "orbit-core" });
  s.addNotes("60 minutes. Hook first, then concepts, then one brief run four ways. The refrain for the hour: what would you have to check?");
}

// ================= 2. Hook =================
{
  const s = section("It looks right.", "Is it right?", "An agent will write you a semantic model and a report, and it will look right. The DAX runs. The visuals render. Nothing errors. Looking right and being right are different things, and you cannot tell them apart by looking. So the question for the hour is not 'can AI build this'. It is 'what would you have to check before you trusted it'.");
  const items = ["The DAX runs", "The visuals render", "Nothing errors"];
  items.forEach((t, i) => {
    pill(s, 6.4, 1.55 + i * 0.5, 2.9, t.toUpperCase(), TEAL, NAVY);
  });
}

// ================= 3. Section: BI development =================
section("What is BI development?", "Six steps, and most of the time is not in the visuals", "Set up the lifecycle before talking about agents. Most delivery time is not building the visual: it is requirements, model fixes, testing, rework after feedback, and sign-off. [Add your own example of where the hours really go.]");

// ================= 4. Lifecycle =================
{
  const s = content("From a question to a trusted report", "Walk the six steps quickly. For each, ask who does it today. Flag Test and Govern: they are where trust is earned, and where agents are weakest.");
  const steps = [
    ["Discover", "Users, questions, acceptance criteria"],
    ["Model", "Tables, relationships, measures"],
    ["Build", "Pages, visuals, theme, layout"],
    ["Test", "Numbers, render, interaction"],
    ["Deploy", "Workspace, binding, refresh"],
    ["Govern", "Sign-off, audit trail, changes"],
  ];
  steps.forEach((st, i) => {
    const col = i % 3, row = Math.floor(i / 3);
    const x = 0.5 + col * 3.05, y = 1.35 + row * 1.85, w = 2.9, h = 1.7;
    card(s, x, y, w, h);
    dot(s, x + 0.2, y + 0.2, 0.42, i % 2 === 0 ? NAVY : VIOLET, i + 1);
    heading(s, st[0], { x: x + 0.75, y: y + 0.22, w: w - 0.9, h: 0.4, fontSize: 20, valign: "middle" });
    txt(s, st[1], { x: x + 0.2, y: y + 0.85, w: w - 0.4, h: 0.7, fontSize: 15 });
  });
}

// ================= 5. Agentic =================
{
  const s = content("Chat answers. An agent acts.", "Chat: you ask, it answers, you copy and paste. Agentic: a model, plus tools, plus a loop, plus a human. It acts, looks at what happened, and tries again. That loop is the power and the risk: it can fix its own errors, and it can confidently build on its own mistake.");
  card(s, 0.5, 1.3, 3.6, 3.2);
  heading(s, "Chat", { x: 0.75, y: 1.5, w: 3.1, h: 0.4, fontSize: 22 });
  const chat = ["You ask", "It answers", "You copy and paste", "Nothing is checked"];
  txt(s, chat.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i < chat.length - 1, paraSpaceAfter: 8 } })), { x: 0.75, y: 2.1, w: 3.1, h: 2.2, fontSize: 16 });

  card(s, 4.4, 1.3, 5.1, 3.2, { fill: NAVY, line: "1A1530" });
  heading(s, "Agentic", { x: 4.7, y: 1.5, w: 4.5, h: 0.4, fontSize: 22, color: WHITE });
  const loop = ["Plan", "Act with tools", "Observe the result", "Try again, or stop"];
  loop.forEach((t, i) => {
    dot(s, 4.7, 2.15 + i * 0.52, 0.36, TEAL, i + 1, NAVY);
    txt(s, t, { x: 5.2, y: 2.15 + i * 0.52, w: 3.0, h: 0.36, fontSize: 16, color: WHITE, valign: "middle" });
  });
  pill(s, 7.55, 2.2, 1.65, "A HUMAN", VIOLET, WHITE);
  txt(s, "approves at the gates", { x: 7.55, y: 2.55, w: 1.75, h: 0.6, fontSize: 14, color: LAV });
  txt(s, "The loop is the power and the risk.", { x: 0.5, y: 4.65, w: 9, h: 0.4, fontSize: 18, bold: true, color: VIOLET });
}

// ================= 6. Which bits =================
{
  const s = content("Which bits can an agent do?", "Green: profiling a model, relationships, measures, building report files, data and render tests, gated deploy. Amber: requirements and layout, the agent drafts and a human decides. Red: interaction testing and sign-off. One honest caveat: it can propose and wire a star schema from imported tables, but creating tables from raw files is not something this tool does. Do not imply it.");
  const cols = [
    { head: "Agent does it", color: GREEN, items: ["Profile the model", "Relationships, measures", "Build the report files", "Data and render tests", "Gated deploy"] },
    { head: "Agent drafts, you decide", color: GOLD, items: ["Requirements and discovery", "Page layout and design", "Fixes for what the tests find"] },
    { head: "Stays with a person", color: RED, items: ["Interaction testing", "Sign-off and acceptance", "Deciding what good means"] },
  ];
  cols.forEach((c, i) => {
    const x = 0.5 + i * 3.05, w = 2.9;
    card(s, x, 1.3, w, 3.3);
    dot(s, x + 0.2, 1.5, 0.3, c.color);
    heading(s, c.head, { x: x + 0.62, y: 1.48, w: w - 0.75, h: 0.34, fontSize: 16, valign: "middle" });
    txt(s, c.items.map((t, j) => ({ text: t, options: { bullet: true, breakLine: j < c.items.length - 1, paraSpaceAfter: 6 } })), { x: x + 0.2, y: 2.1, w: w - 0.4, h: 2.4, fontSize: 15 });
  });
  txt(s, "Creating tables from raw files is not covered by this tool: it profiles and wires what is already imported.", { x: 0.5, y: 4.72, w: 9, h: 0.4, fontSize: 14, color: "6B6B6B" });
}

// ================= 7. Section: concepts =================
section("Six ideas that matter", "Instructions, skills, hooks, loops, gates, MCP", "Do not linger: the examples are where these come alive. One slide of definitions, one on the hinge, one with what each looks like in a real repo.");

// ================= 8. Concepts overview =================
{
  const s = content("The vocabulary", "CLAUDE.md or AGENTS.md: standing instructions read every session. Skills: a repeatable recipe loaded when the task matches. Hooks: run whether or not the agent remembers. Loops: iterate until a check passes, not until the agent feels done. Gates: a step that refuses to advance without a pass or a human signature. MCP: live typed access to a tool or data source.");
  const items = [
    ["CLAUDE.md", "Standing instructions, read every session", "ADVISORY", VIOLET],
    ["Skills", "A repeatable recipe for one kind of job", "ADVISORY", VIOLET],
    ["MCP", "Live, typed access to tools and data", "REACH", NAVY],
    ["Hooks", "Run on every commit, remembered or not", "BLOCKING", TEAL],
    ["Loops", "Repeat until a check passes", "BLOCKING", TEAL],
    ["Gates", "Refuse to advance without a pass or a signature", "BLOCKING", TEAL],
  ];
  items.forEach((it, i) => {
    const col = i % 3, row = Math.floor(i / 3);
    const x = 0.5 + col * 3.05, y = 1.3 + row * 1.9, w = 2.9, h = 1.75;
    card(s, x, y, w, h);
    pill(s, x + 0.2, y + 0.2, 1.1, it[2], it[3], it[3] === TEAL ? NAVY : WHITE);
    heading(s, it[0], { x: x + 0.2, y: y + 0.6, w: w - 0.4, h: 0.4, fontSize: 20, valign: "middle" });
    txt(s, it[1], { x: x + 0.2, y: y + 1.05, w: w - 0.4, h: 0.6, fontSize: 14 });
  });
}

// ================= 9. Advisory vs blocking =================
{
  const s = content("Advisory or blocking?", "Skills and CLAUDE.md are advisory: the agent can ignore them. Hooks and gates are blocking: it cannot. That is the hinge for everything that follows. Each example sits at a different point on advisory versus blocking, and on blind versus grounded. Reference: a cold Copilot session with all the knowledge files present shipped a bad report and deployed it by the wrong path. The knowledge was opt-in, advisory, tool-specific, runtime-bypassable.");
  card(s, 0.5, 1.3, 4.3, 2.55, { fill: LAV });
  heading(s, "Advisory", { x: 0.8, y: 1.5, w: 3.7, h: 0.4, fontSize: 24, color: VIOLET });
  txt(s, "Instructions and skills.", { x: 0.8, y: 2.05, w: 3.7, h: 0.4, fontSize: 16, bold: true });
  txt(s, "The agent decides whether to read them. Nothing fails if it does not.", { x: 0.8, y: 2.5, w: 3.7, h: 1.2, fontSize: 16 });
  card(s, 5.2, 1.3, 4.3, 2.55, { fill: NAVY, line: "1A1530" });
  heading(s, "Blocking", { x: 5.5, y: 1.5, w: 3.7, h: 0.4, fontSize: 24, color: TEAL });
  txt(s, "Hooks and gates.", { x: 5.5, y: 2.05, w: 3.7, h: 0.4, fontSize: 16, bold: true, color: WHITE });
  txt(s, "The agent cannot walk past them. A failing check stops the build.", { x: 5.5, y: 2.5, w: 3.7, h: 1.2, fontSize: 16, color: WHITE });
  s.addShape(pres.ShapeType.rightArrow, { x: 4.55, y: 2.35, w: 0.9, h: 0.45, fill: { color: TEAL }, line: { color: TEAL, width: 0 }, objectName: "arrow" });
  txt(s, "Opt-in, advisory, tool-specific, runtime-bypassable: why knowledge files alone are not enough.", { x: 0.5, y: 4.15, w: 9, h: 0.7, fontSize: 17, bold: true, color: NAVY });
}

// ================= 10. In the repo =================
{
  const s = content("What each one looks like in practice", "Show these only as glimpses, 20 to 30 seconds each, from the repo. Check what is on screen before projecting: no client names. Do not open the top of CLAUDE.md in the demo repo, it carries the extract banner; use AGENTS.md.");
  const rows = [
    ["Instructions", "AGENTS.md", "Never name a client. Fixes go in the engine."],
    ["Skills", ".claude/skills/", "new-report, report-test-loop, render-fix-loop"],
    ["Hooks", ".pre-commit-config.yaml", "30-odd named hooks, one principle each"],
    ["Loops", "ALG-PIPELINE.md", "A phase ends by waiting for a person"],
    ["Gates", "check_phase_order.py", "No APPROVED.md, no build"],
  ];
  rows.forEach((r, i) => {
    const y = 1.3 + i * 0.7;
    card(s, 0.5, y, 9, 0.6, { noShadow: true });
    heading(s, r[0], { x: 0.7, y, w: 1.6, h: 0.6, fontSize: 16, valign: "middle" });
    txt(s, r[1], { x: 2.4, y, w: 2.9, h: 0.6, fontFace: MONO, fontSize: 13, color: VIOLET, valign: "middle" });
    txt(s, r[2], { x: 5.4, y, w: 4.0, h: 0.6, fontSize: 14, valign: "middle" });
  });
}

// ================= 11. Section: four ways =================
section("One brief, four ways", "Same requirement every time, so the pros and cons are comparable", "For each example use the same four beats: setup, brief in, what came out, what we had to check. Do not declare a winner until the comparison slide.");

// ================= 12. The brief =================
{
  const s = content("The brief: UK trade, the balance", "Open ONS data, so nothing confidential. The brief is chosen because it contains the traps worth showing: the colour that cannot flip on refresh, a field-parameter slicer, and a model with no date dimension. Paste it unchanged into Examples 1 to 3.");
  card(s, 0.5, 1.3, 4.6, 3.45, { fill: LAV });
  pill(s, 0.75, 1.5, 1.4, "THE BRIEF", VIOLET, WHITE);
  const brief = ["One page on the UK trade balance: exports less imports, over time", "A headline balance card that flips colour from surplus to deficit", "A trend by month", "A breakdown by partner country or commodity", "A slicer to switch the measure"];
  txt(s, brief.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i < brief.length - 1, paraSpaceAfter: 7 } })), { x: 0.75, y: 2.0, w: 4.1, h: 2.6, fontSize: 15 });
  heading(s, "Built-in traps", { x: 5.4, y: 1.3, w: 4, h: 0.35, fontSize: 18 });
  const traps = [
    ["Colour that must flip", "Correct today, wrong after the next refresh"],
    ["A slicer that drives a measure", "Looks fine, can drive nothing"],
    ["No date dimension", "The trend needs one"],
  ];
  traps.forEach((t, i) => {
    const y = 1.8 + i * 1.0;
    card(s, 5.4, y, 4.1, 0.9);
    heading(s, t[0], { x: 5.6, y: y + 0.1, w: 3.7, h: 0.35, fontSize: 15 });
    txt(s, t[1], { x: 5.6, y: y + 0.47, w: 3.7, h: 0.35, fontSize: 14 });
  });
}

// ---------- example template ----------
function example(n, title, tag, setup, watch, pro, con, notes) {
  const s = content(`Example ${n}: ${title}`, notes);
  pill(s, 0.5, 1.2, 1.7, tag, VIOLET, WHITE);
  card(s, 0.5, 1.65, 4.5, 3.1);
  heading(s, "Setup", { x: 0.75, y: 1.8, w: 4, h: 0.3, fontSize: 15, color: VIOLET });
  txt(s, setup, { x: 0.75, y: 2.12, w: 4.0, h: 0.9, fontSize: 15 });
  heading(s, "Watch for", { x: 0.75, y: 3.05, w: 4, h: 0.3, fontSize: 15, color: VIOLET });
  txt(s, watch, { x: 0.75, y: 3.37, w: 4.0, h: 1.3, fontSize: 15 });
  card(s, 5.3, 1.2, 4.2, 1.75, { fill: "E8F8F1", line: "BFE8D2" });
  heading(s, "Pro", { x: 5.55, y: 1.35, w: 3.7, h: 0.3, fontSize: 15, color: "1E8A57" });
  txt(s, pro, { x: 5.55, y: 1.7, w: 3.7, h: 1.15, fontSize: 15 });
  card(s, 5.3, 3.1, 4.2, 1.65, { fill: "FCEDEB", line: "F3CCC7" });
  heading(s, "Con", { x: 5.55, y: 3.25, w: 3.7, h: 0.3, fontSize: 15, color: "B83A2E" });
  txt(s, con, { x: 5.55, y: 3.6, w: 3.7, h: 1.05, fontSize: 15 });
  return s;
}

// ================= 13. Example 1 =================
example(1, "chat agent", "RECORDED", "A plain chat. No tools, no access to the model.", "Good DAX and a sensible layout. Table and column names it could not know, and guessed.",
  "Zero setup. Fast for DAX, ideas and explanation.", "Blind: every name is a guess. You copy and paste. Nothing is checked or repeatable.",
  "Paste the brief unchanged. For a single measure this is genuinely the right tool. Name the guessed table and column names out loud. It cannot see your model, you copy and paste, nothing is checked, and tomorrow it will not give the same answer.");

// ================= 14. Example 2 =================
example(2, "Fabric skills", "RECORDED", "Microsoft's Fabric Skills, installed per Microsoft's own docs. Same brief, verbatim.", "Real formats and APIs. A first draft far faster than anything you build. Variation between runs.",
  "Maintained by Microsoft, grounded in real formats. Quick to start.", "Advisory and generic. Opt-in each time, and no record of who approved what.",
  "Concede loudly: Microsoft's skills are good, and for a prototype, a single measure, or a report you will never rebuild, they are the right answer. What to notice is not quality but that it is advisory and opt-in. Show the version and date of the setup.");

// ================= 15. Example 3 =================
example(3, "MCP", "RECORDED", "An agent connected live to the model and the workspace. Same brief, verbatim.", "It reads the real model: actual tables, measures, relationships. It can also write to the real thing.",
  "Live ground truth. It looks names up instead of guessing.", "Capability without process: no staging copy, no approval, no record of why.",
  "Example 1 guessed names, this one looks them up. But it can now write to the real thing with nothing in the way. [Fill in after recording: what it got right, and what nothing stopped.] To decide before rehearsal: which MCP, and what auth it needs on stage.");

// ================= 16. Example 4 =================
{
  example(4, "Fabric skills + your own", "LIVE, OFFLINE", "Our scaffolding: skills, scripts, gates, human sign-offs. Live demos A and C, offline.", "A build refused for a missing sign-off. One command, green, with advisories it will not let you ignore.",
    "Consistent, tested and gated. Standards enforced, with an audit trail.", "Upfront cost and upkeep. Covers only what you encoded. Overkill for one-off work.",
    "Back to the terminal, tab 1. Demo A: check_phase_order blocks what-we-trade and passes the-balance. Demo C: run_pipeline until gates, five stages green, nine advisories, read R-SURVIVES-REFRESH aloud. Demo B (recorded, optional): the model half, same recipe. Say the cost out loud.");
}

// ================= 17. Comparison =================
{
  const s = content("Four ways, side by side", "Walk it row by row, in the order the audience has just seen it. Land the message: each rung adds grounding or control, and only the last adds both. Without the gates you have reports and a feeling. With them you have a number you can defend.");
  const hdr = (t) => ({ text: t, options: { bold: true, color: WHITE, fill: { color: NAVY }, fontFace: HEAD, fontSize: 14 } });
  const cell = (t, o = {}) => ({ text: t, options: Object.assign({ fontSize: 14, color: TEXT, fill: { color: WHITE } }, o) });
  const rowHead = (t) => ({ text: t, options: { bold: true, fontFace: HEAD, fontSize: 14, color: NAVY, fill: { color: LAV } } });
  s.addTable([
    [hdr("Approach"), hdr("Pro"), hdr("Con")],
    [rowHead("Chat"), cell("Zero setup, fast for DAX"), cell("Blind, unrepeatable")],
    [rowHead("Fabric skills"), cell("Grounded, quick start"), cell("Advisory, generic, no audit trail")],
    [rowHead("MCP"), cell("Live ground truth"), cell("No gate on what it writes")],
    [rowHead("Skills + your own"), cell("Gated, tested, audited"), cell("Upfront cost, upkeep")],
  ], { x: 0.5, y: 1.3, w: 9, colW: [2.2, 3.4, 3.4], rowH: 0.62, valign: "middle", border: { type: "solid", pt: 0.75, color: "E3E0EE" }, margin: [0, 0.12, 0, 0.12] });
  txt(s, "Each rung adds grounding or control. Only the last adds both.", { x: 0.5, y: 4.55, w: 9, h: 0.4, fontSize: 18, bold: true, color: VIOLET });
}

// ================= 18. The ladder map =================
{
  const s = content("Grounding and control", "Vertical: does the agent see the real model (grounding). Horizontal: can anything stop it being wrong (control). Chat is blind and unchecked. Fabric skills know the formats but advise only. MCP is grounded but unguarded. Skills plus your own is the only one in the top right corner.");
  const px = 1.3, py = 1.2, pw = 7.6, ph = 3.5;
  card(s, px, py, pw, ph, { noShadow: true });
  s.addShape(pres.ShapeType.line, { x: px + pw / 2, y: py, w: 0, h: ph, line: { color: "D5D1E4", width: 1, dashType: "dash" } });
  s.addShape(pres.ShapeType.line, { x: px, y: py + ph / 2, w: pw, h: 0, line: { color: "D5D1E4", width: 1, dashType: "dash" } });
  txt(s, "More grounded", { x: 0.2, y: py, w: 1.05, h: 0.5, fontSize: 12, color: "6B6B6B", align: "right" });
  txt(s, "Blind", { x: 0.4, y: py + ph - 0.3, w: 0.85, h: 0.3, fontSize: 12, color: "6B6B6B", align: "right" });
  txt(s, "Advisory", { x: px, y: py + ph + 0.05, w: 1.5, h: 0.3, fontSize: 12, color: "6B6B6B" });
  txt(s, "Blocking", { x: px + pw - 1.5, y: py + ph + 0.05, w: 1.5, h: 0.3, fontSize: 12, color: "6B6B6B", align: "right" });
  const pts = [
    ["1", "Chat", 1.0, 3.05, VIOLET],
    ["2", "Fabric skills", 2.1, 2.2, VIOLET],
    ["3", "MCP", 1.9, 1.15, VIOLET],
    ["4", "Skills + your own", 5.3, 1.1, TEAL],
  ];
  pts.forEach((p) => {
    const x = px + p[2], y = py + p[3] - 0.2;
    dot(s, x, y, 0.4, p[4], p[0], p[4] === TEAL ? NAVY : WHITE);
    txt(s, p[1], { x: x + 0.5, y, w: 2.2, h: 0.4, fontSize: 15, bold: true, color: NAVY, valign: "middle" });
  });
}

// ================= 19. The mistake =================
{
  const s = content("The mistake every check passed", "G-05 / BUG-02-001. The field-parameter slicer rendered, accepted a selection, and drove nothing at all. The engine never emitted the binding on the consuming chart, so the chart stayed on one fixed measure. Gates passed, DAX passed, render-match passed. A person clicking the slicer found it. Show the recording. Backup mistake: G-02b, a guessed custom-visual GUID that rendered blank cards; the fix was to capture the real shape, never guess.");
  ["Gates passed", "DAX passed", "Render matched the mockup"].forEach((t, i) => {
    const y = 1.35 + i * 0.9;
    card(s, 0.5, y, 4.3, 0.75, { noShadow: true });
    dot(s, 0.7, y + 0.17, 0.4, GREEN, "✓", WHITE);
    heading(s, t, { x: 1.3, y, w: 3.4, h: 0.75, fontSize: 17, valign: "middle" });
  });
  card(s, 5.2, 1.35, 4.3, 2.55, { fill: NAVY, line: "1A1530" });
  txt(s, "The slicer drove nothing.", { x: 5.5, y: 1.6, w: 3.7, h: 1.0, fontFace: HEAD, bold: true, fontSize: 26, color: WHITE });
  txt(s, "Found by a person clicking it and noticing the chart did not move.", { x: 5.5, y: 2.65, w: 3.7, h: 1.0, fontSize: 16, color: LAV });
  txt(s, "Automated checks catch what they were written to catch. The interaction layer is still yours.", { x: 0.5, y: 4.15, w: 9, h: 0.7, fontSize: 18, bold: true, color: VIOLET });
}

// ================= 20. What to check =================
{
  const s = content("What to check before you trust it", "Does every measure resolve live. Does the model contain what was actually asked for. Does the report survive a refresh. And does it work when a person drives it. What makes it reliable is not the prompt: it is a spec it can be checked against, a bar set before it starts, and gates it cannot walk past.");
  const items = [
    ["Measures resolve live", "Every one, against the real model"],
    ["The model has what was asked", "Compare to the request, not to memory"],
    ["It survives a refresh", "Colours, sorts and filters on new data"],
    ["It works when driven", "Click the slicer. Hover the tooltip."],
  ];
  items.forEach((it, i) => {
    const col = i % 2, row = Math.floor(i / 2);
    const x = 0.5 + col * 4.6, y = 1.3 + row * 1.7, w = 4.4, h = 1.55;
    card(s, x, y, w, h);
    dot(s, x + 0.25, y + 0.25, 0.45, i === 3 ? RED : TEAL, i + 1, i === 3 ? WHITE : NAVY);
    heading(s, it[0], { x: x + 0.9, y: y + 0.22, w: w - 1.1, h: 0.5, fontSize: 17, valign: "middle" });
    txt(s, it[1], { x: x + 0.9, y: y + 0.8, w: w - 1.1, h: 0.65, fontSize: 15 });
  });
}

// ================= 21. Where you stay =================
{
  const s = content("Where you stay in the loop", "Approving the design, approving the model changes, and driving the thing in the Service: the parts where judgement is the work. I would rather have a tool that tells me it shipped with caveats than one that tells me it is done.");
  const items = [
    ["Approve the design", "Sign the mockup before anything is built."],
    ["Approve model changes", "The agent proposes joins and measures. You decide."],
    ["Drive it in the Service", "Interaction testing is still a human job."],
  ];
  items.forEach((it, i) => {
    const x = 0.5 + i * 3.05, y = 1.4, w = 2.9, h = 2.7;
    card(s, x, y, w, h);
    dot(s, x + 0.25, y + 0.25, 0.5, VIOLET, i + 1);
    heading(s, it[0], { x: x + 0.25, y: y + 0.95, w: w - 0.5, h: 0.7, fontSize: 18 });
    txt(s, it[1], { x: x + 0.25, y: y + 1.7, w: w - 0.5, h: 0.9, fontSize: 15 });
  });
  txt(s, "A tool that says it shipped with caveats beats one that says it is done.", { x: 0.5, y: 4.3, w: 9, h: 0.5, fontSize: 18, bold: true, color: VIOLET });
}

// ================= 22. Close =================
{
  const s = pres.addSlide({ masterName: "TITLE" });
  txt(s, "Take one thing home", { x: 0.6, y: 0.9, w: 8.4, h: 0.6, fontFace: HEAD, bold: true, fontSize: 20, color: TEAL });
  txt(s, "Write down what “good” means for one report. Turn it into one check that fails.", { x: 0.6, y: 1.6, w: 8.2, h: 1.7, fontFace: HEAD, bold: true, fontSize: 36, color: WHITE });
  txt(s, "Run it over whatever your agent produced. It works with Microsoft's skills as well as it works with mine.", { x: 0.6, y: 3.5, w: 7.6, h: 0.9, fontSize: 18, color: LAV });
  txt(s, "Questions", { x: 0.6, y: 4.7, w: 3, h: 0.35, fontSize: 16, bold: true, color: TEAL });
  s.addNotes("The close. Everything in the hour reduces to this: a spec it can be checked against, a bar set before it starts, and gates it cannot walk past. You do not need my engine to start.");
}

const out = path.join(__dirname, "agentic-bi-development.pptx");
pres.writeFile({ fileName: out }).then(async () => {
  if (applyTheme) await applyTheme(out, THEME);
  console.log("wrote", out);
});
