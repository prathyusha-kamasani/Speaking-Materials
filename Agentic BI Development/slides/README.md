# Slides

**The deck is `deck/index.html`**: 45 slides on the Data Alchemy Studio palette (the colour layer of the Data Nova design system), self-contained and offline (fonts,
icons, logo and tokens are all bundled). Open it in Chrome or Edge.

```bash
open slides/deck/index.html
```

| Key | Does |
|---|---|
| Arrow keys, Space, PageUp/Down | next, previous |
| Home / End | first, last |
| A | overview: every slide as a tile, click one to go there |
| S | presenter view in a second window: notes, next slide, timer, shortcuts (S or Esc closes it) |
| B or . | black screen |
| P | play or pause the slide's video |
| E | expand the slide's image (slide 27) |
| F | fullscreen |
| N | speaker notes in this window |

`index.html?all` shows every slide at full size, for the checker and for printing to PDF. The slide number is in
the URL (`#7`), so a refresh keeps your place.

The deck runtime, the patterns, how Prathy likes a deck and the checker now live in the `slide-decks` skill of
the design system (`skills/slide-decks`). Check this deck with its `scripts/check-deck.js`.

## How it is built

`deck/build.py` writes `index.html` from the slide list in that file. Edit the slides there, then:

```bash
python3 slides/deck/build.py
```

Covers, dividers and the close use the rose-gold full-bleed opener; content slides use the warm-white field with a rose-gold band for the takeaway line; emphasis cards are ink. The palette is light only, so there are no navy slides. `deck/alchemy/` holds the vendored colour layer; `deck/styles.css` imports it after Data Nova's tokens.

`deck/deck.css` is the deck layer (tokens only, no literal colours or fonts). Everything else in `deck/` is a
vendored snapshot of the Data Nova design system (`styles.css`, `base.css`, `tokens/`, the logo, `rules/check.js`)
plus the three typefaces (General Sans, Inter, JetBrains Mono, Latin subset) and Lucide icons. The design system's
home is `github.com/prathyusha-kamasani/data-nova-design-system`; re-vendor from `skills/data-nova-design/` there
if it changes.

## Checking

The design system's checker (`deck/rules/check.js`) measures 16 of its 18 rules. Result on 2026-10-10: **100, 16 of
16**. The other two (background sets the ink, one shared left edge) are judged by eye. To re-run it, load
`index.html?all` in a browser, add `rules/check.js`, and call `DataNovaRules.check()`.

## Earlier versions

`deck/index.data-nova-navy.html` (built by `deck/build.data-nova-navy.py`) is the same deck in Data Nova's navy and teal, before the switch to Data Alchemy.

## The older pptx

`agentic-bi-development.pptx` (built by `build_deck.js`) is the first version, before the design system was found.
It uses Arial and Calibri, not the brand fonts, and does not meet the system's rules. Kept as a fallback only.
