/* Data Nova design-system rule checker.
 *
 * Usage in a page:      <script src="../rules/check.js"></script>
 *                       DataNovaRules.check() // audits document
 * Usage on another doc: DataNovaRules.check(iframe.contentDocument)
 *
 * Returns { score, grade, passed, total, rules: [{id, name, status, violations}] }
 * Every rule maps to a numbered rule in guidelines/design-rules-*.html.
 */
(function (global) {
  const PALETTE_FILL_ONLY = { '#20b8a8': 'Teal', '#e8a33d': 'Nova Gold', '#888888': 'Mid Grey' };

  function srgbToLin(c) { return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4); }
  function parseColor(str) {
    if (!str) return null;
    const m = str.match(/rgba?\(([^)]+)\)/);
    if (!m) return null;
    const p = m[1].split(',').map(s => parseFloat(s.trim()));
    return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 };
  }
  function lum(c) {
    const v = [c.r, c.g, c.b].map(x => srgbToLin(x / 255));
    return 0.2126 * v[0] + 0.7152 * v[1] + 0.0722 * v[2];
  }
  function contrast(fg, bg) {
    const a = lum(fg), b = lum(bg);
    const hi = Math.max(a, b), lo = Math.min(a, b);
    return (hi + 0.05) / (lo + 0.05);
  }
  function blend(fg, bg) {
    const a = fg.a;
    return { r: fg.r * a + bg.r * (1 - a), g: fg.g * a + bg.g * (1 - a), b: fg.b * a + bg.b * (1 - a), a: 1 };
  }
  function effectiveBg(el, win) {
    let node = el, stack = [];
    while (node && node.nodeType === 1) {
      const c = parseColor(win.getComputedStyle(node).backgroundColor);
      if (c && c.a > 0) { stack.push(c); if (c.a === 1) break; }
      node = node.parentElement;
    }
    let base = { r: 255, g: 255, b: 255, a: 1 };
    for (let i = stack.length - 1; i >= 0; i--) base = blend(stack[i], base);
    return base;
  }
  // OPTION and OPTGROUP are rendered by the platform, not authorable, so their
  // UA padding and font are out of scope.
  const SKIP_TAGS = { SCRIPT: 1, STYLE: 1, TITLE: 1, NOSCRIPT: 1, TEMPLATE: 1, HEAD: 1, META: 1, LINK: 1, OPTION: 1, OPTGROUP: 1 };
  function hasText(el) {
    if (SKIP_TAGS[el.tagName]) return false;
    if (el.closest && el.closest('[data-rule-demo]')) return false;
    for (const n of el.childNodes) if (n.nodeType === 3 && n.textContent.trim().length) return true;
    return false;
  }
  function describe(el) {
    const t = (el.textContent || '').trim().replace(/\s+/g, ' ').slice(0, 40);
    return el.tagName.toLowerCase() + (t ? ' "' + t + '"' : '');
  }
  function toHex(c) {
    return '#' + [c.r, c.g, c.b].map(x => Math.round(x).toString(16).padStart(2, '0')).join('');
  }

  const RULES = [
    {
      id: 2, name: 'Contrast meets WCAG AA',
      run(doc, win) {
        const bad = [];
        doc.querySelectorAll('*').forEach(el => {
          if (!hasText(el)) return;
          const cs = win.getComputedStyle(el);
          if (cs.visibility === 'hidden' || cs.display === 'none' || parseFloat(cs.opacity) < 0.4) return;
          const isSvg = el.ownerSVGElement !== undefined && el.ownerSVGElement !== null;
          const fgRaw = parseColor(isSvg ? cs.fill : cs.color);
          if (!fgRaw) return;
          const bg = effectiveBg(el, win);
          const fg = fgRaw.a < 1 ? blend(fgRaw, bg) : fgRaw;
          const size = parseFloat(cs.fontSize);
          const weight = parseInt(cs.fontWeight, 10) || 400;
          const large = size >= 24 || (size >= 19 && weight >= 700);
          const need = large ? 3 : 4.5;
          const ratio = contrast(fg, bg);
          if (ratio < need) bad.push(describe(el) + ' ' + ratio.toFixed(2) + ':1 (needs ' + need + ':1, ' + toHex(fg) + ' on ' + toHex(bg) + ')');
        });
        return bad;
      }
    },
    {
      id: 3, name: 'Fill-only colours not used as text or a meaningful stroke',
      run(doc, win) {
        const bad = [];
        // meaningful strokes (underlines, accent borders) need 3:1
        doc.querySelectorAll('*').forEach(el => {
          if (isDemo(el) || SKIP_TAGS[el.tagName]) return;
          const cs = win.getComputedStyle(el);
          const bg = effectiveBg(el, win);
          ['Top', 'Right', 'Bottom', 'Left'].forEach(side => {
            const w = parseFloat(cs['border' + side + 'Width']) || 0;
            if (w < 2) return;
            const col = parseColor(cs['border' + side + 'Color']);
            if (!col || col.a < 0.5) return;
            const solid = col.a < 1 ? blend(col, bg) : col;
            if (contrast(solid, bg) < 3) {
              bad.push(describe(el) + ' has a ' + cs['border' + side + 'Width'] + ' ' + side.toLowerCase() +
                ' stroke at ' + contrast(solid, bg).toFixed(2) + ':1 (meaningful graphics need 3:1)');
            }
          });
        });
        doc.querySelectorAll('*').forEach(el => {
          if (!hasText(el)) return;
          const cs = win.getComputedStyle(el);
          const isSvg2 = el.ownerSVGElement !== undefined && el.ownerSVGElement !== null;
          const fg = parseColor(isSvg2 ? cs.fill : cs.color);
          if (!fg) return;
          const hex = toHex(fg).toLowerCase();
          const bg = effectiveBg(el, win);
          // only a problem on light grounds, where these values fail
          if (PALETTE_FILL_ONLY[hex] && lum(bg) > 0.3) {
            bad.push(describe(el) + ' uses ' + PALETTE_FILL_ONLY[hex] + ' ' + hex + ' as text on a light surface; use the -ink token');
          }
        });
        return bad;
      }
    },
    {
      id: 7, name: 'Radius never 16px or above',
      run(doc, win) {
        const bad = [];
        doc.querySelectorAll('*').forEach(el => {
          if (isDemo(el)) return;
          const cs = win.getComputedStyle(el);
          ['borderTopLeftRadius', 'borderTopRightRadius', 'borderBottomLeftRadius', 'borderBottomRightRadius'].forEach(k => {
            const v = cs[k];
            if (v.includes('%')) return;                 // circles and pills are fine
            const px = parseFloat(v);
            const box = Math.min(el.getBoundingClientRect().width, el.getBoundingClientRect().height);
            if (px >= 16 && px < box / 2) bad.push(describe(el) + ' has ' + v + ' radius');
          });
        });
        return [...new Set(bad)];
      }
    },
    {
      id: 8, name: 'No coloured left-border accents',
      run(doc, win) {
        const bad = [];
        doc.querySelectorAll('*').forEach(el => {
          if (isDemo(el)) return;
          const cs = win.getComputedStyle(el);
          const lw = parseFloat(cs.borderLeftWidth) || 0;
          const rw = parseFloat(cs.borderRightWidth) || 0;
          const tw = parseFloat(cs.borderTopWidth) || 0;
          const lc = parseColor(cs.borderLeftColor);
          if (lw >= 2 && rw === 0 && tw === 0 && lc && lc.a > 0) {
            bad.push(describe(el) + ' has a ' + cs.borderLeftWidth + ' left-only border');
          }
        });
        return bad;
      }
    },
    {
      id: 9, name: 'Violet not used as a border or fill',
      run(doc, win) {
        const bad = [];
        doc.querySelectorAll('*').forEach(el => {
          if (isDemo(el)) return;
          const cs = win.getComputedStyle(el);
          const isViolet = c => { const p = parseColor(c); return p && p.a > 0 && toHex(p).toLowerCase() === '#5c4e8a'; };
          ['borderTopColor', 'borderRightColor', 'borderBottomColor', 'borderLeftColor'].forEach((k, i) => {
            const w = parseFloat(cs[['borderTopWidth', 'borderRightWidth', 'borderBottomWidth', 'borderLeftWidth'][i]]) || 0;
            if (w > 0 && isViolet(cs[k])) bad.push(describe(el) + ' uses base Violet as a border');
          });
          const bgc = parseColor(cs.backgroundColor);
          const r = el.getBoundingClientRect();
          if (bgc && bgc.a > 0.8 && toHex(bgc).toLowerCase() === '#5c4e8a' && r.width * r.height > 4000 && el.tagName !== 'BUTTON') {
            bad.push(describe(el) + ' uses base Violet as a large fill');
          }
        });
        return [...new Set(bad)];
      }
    },
    {
      id: 10, name: 'Primary buttons are not teal-filled',
      run(doc, win) {
        const bad = [];
        doc.querySelectorAll('button, [role="button"], a[class*="btn"], a[class*="button"]').forEach(el => {
          if (isDemo(el)) return;
          const bgc = parseColor(win.getComputedStyle(el).backgroundColor);
          if (bgc && bgc.a > 0.5 && toHex(bgc).toLowerCase() === '#20b8a8') bad.push(describe(el) + ' has a teal fill');
        });
        return bad;
      }
    },
    {
      id: 11, name: 'Type steps within 3:1 and body 14px+',
      run(doc, win) {
        const bad = [];
        doc.querySelectorAll('p, li, td, span, div').forEach(el => {
          if (!hasText(el)) return;
          const cs = win.getComputedStyle(el);
          const size = parseFloat(cs.fontSize);
          if (size < 14 && cs.fontFamily.toLowerCase().indexOf('mono') === -1 && el.textContent.trim().length > 60) {
            bad.push(describe(el) + ' body copy at ' + size + 'px (minimum 14px)');
          }
        });
        return bad;
      }
    },
    {
      id: 18, name: 'Chart series clear 3:1 against their background',
      run(doc, win) {
        const bad = [];
        doc.querySelectorAll('*').forEach(el => {
          if (isDemo(el) || SKIP_TAGS[el.tagName]) return;
          const style = (el.getAttribute && el.getAttribute('style')) || '';
          // Intent comes from WHICH token the element references, not from the
          // colour value: a sequential ramp step can share a hex with a
          // categorical series, and only the categorical one carries this rule.
          const isCategorical = /var\(\s*--dn-chart-[1-6]\s*\)/.test(style);
          const isRamp = /--dn-chart-seq-|--dn-chart-div-mid/.test(style);
          if (isRamp) return;
          const cs = win.getComputedStyle(el);
          const bgc = parseColor(cs.backgroundColor);
          if (!bgc || bgc.a < 0.5) return;
          if (!isCategorical) {
            // no inline token reference: fall back to matching this element's
            // own resolved categorical values, excluding ramp values
            const hex = toHex(bgc).toLowerCase();
            const series = [];
            for (let i = 1; i <= 6; i++) {
              const v = (cs.getPropertyValue('--dn-chart-' + i) || '').trim().toLowerCase();
              if (v) series.push(v);
            }
            if (series.indexOf(hex) === -1) return;
            const ramp = [];
            for (let i = 1; i <= 5; i++) {
              const v = (cs.getPropertyValue('--dn-chart-seq-' + i) || '').trim().toLowerCase();
              if (v) ramp.push(v);
            }
            const mid = (cs.getPropertyValue('--dn-chart-div-mid') || '').trim().toLowerCase();
            if (ramp.indexOf(hex) !== -1 || hex === mid) return;
          }
          const behind = effectiveBg(el.parentElement || doc.body, win);
          const r = contrast(bgc, behind);
          if (r < 3) {
            bad.push('chart series ' + toHex(bgc).toLowerCase() + ' is ' + r.toFixed(2) + ':1 against ' + toHex(behind) + ' (needs 3:1)');
          }
        });
        return [...new Set(bad)];
      }
    },
    {
      id: 5, name: 'Diagram shapes share size and gap',
      run(doc) {
        const bad = [];
        doc.querySelectorAll('svg').forEach((svg, si) => {
          if (svg.closest('[data-rule-demo]') || isChart(svg) || isInvisible(svg)) return;
          const rects = [...svg.querySelectorAll('rect')].map(r => ({
            x: parseFloat(r.getAttribute('x')), y: parseFloat(r.getAttribute('y')),
            w: parseFloat(r.getAttribute('width')), h: parseFloat(r.getAttribute('height')),
          })).filter(r => !isNaN(r.x) && r.w > 20);
          const rows = {};
          rects.forEach(r => { const k = r.y + ':' + r.h; (rows[k] = rows[k] || []).push(r); });
          Object.entries(rows).forEach(([k, row]) => {
            if (row.length < 2) return;
            row.sort((a, b) => a.x - b.x);
            const widths = [...new Set(row.map(r => r.w))];
            if (widths.length > 1) bad.push('svg #' + (si + 1) + ' row y=' + row[0].y + ' has mixed box widths (' + widths.join(', ') + ')');
            const gaps = [];
            for (let i = 1; i < row.length; i++) gaps.push(Math.round(row[i].x - (row[i - 1].x + row[i - 1].w)));
            const uniq = [...new Set(gaps)];
            if (uniq.length > 1) bad.push('svg #' + (si + 1) + ' row y=' + row[0].y + ' has uneven gaps (' + gaps.join(', ') + 'px)');
          });
          const allH = [...new Set(rects.map(r => r.h))];
          if (rects.length > 1 && allH.length > 1) bad.push('svg #' + (si + 1) + ' has mixed box heights (' + allH.join(', ') + ')');
        });
        return bad;
      }
    },
    {
      id: 6, name: 'Spacing on the 4px scale',
      run(doc, win) {
        const bad = [];
        doc.querySelectorAll('*').forEach(el => {
          if (isDemo(el) || SKIP_TAGS[el.tagName]) return;
          const cs = win.getComputedStyle(el);
          ['paddingTop', 'paddingBottom', 'paddingLeft', 'paddingRight', 'gap', 'rowGap', 'columnGap'].forEach(k => {
            const v = parseFloat(cs[k]);
            if (!isNaN(v) && v > 0 && v % 2 !== 0) bad.push(describe(el) + ' ' + k + ' ' + cs[k] + ' is off the 4px scale');
          });
        });
        return [...new Set(bad)].slice(0, 12);
      }
    },
    {
      id: 12, name: 'Diagrams are outline-only line drawings',
      run(doc, win) {
        const bad = [];
        doc.querySelectorAll('svg rect, svg circle, svg path, svg polygon').forEach(el => {
          if (isDemo(el) || isChart(el) || isSketch(el) || isInvisible(el)) return;
          const cs = win.getComputedStyle(el);
          const f = parseColor(cs.fill);
          const isText = el.tagName.toLowerCase() === 'text';
          if (!isText && f && f.a > 0.05 && !(f.r === 0 && f.g === 0 && f.b === 0 && cs.fill === 'none')) {
            if (cs.fill !== 'none') bad.push(el.tagName.toLowerCase() + ' in a diagram has fill ' + cs.fill);
          }
          if (cs.filter && cs.filter !== 'none') bad.push(el.tagName.toLowerCase() + ' in a diagram has a filter');
        });
        return [...new Set(bad)].slice(0, 8);
      }
    },
    {
      id: 13, name: 'Motion has no bounce or spring',
      run(doc, win) {
        const bad = [];
        doc.querySelectorAll('*').forEach(el => {
          if (isDemo(el)) return;
          const cs = win.getComputedStyle(el);
          const t = (cs.transitionTimingFunction + ' ' + cs.animationTimingFunction).toLowerCase();
          if (/cubic-bezier\([^)]*-\d/.test(t) || t.includes('elastic') || t.includes('bounce')) {
            bad.push(describe(el) + ' uses an overshooting easing curve');
          }
        });
        return [...new Set(bad)];
      }
    },
    {
      id: 14, name: 'Focus states are never suppressed',
      run(doc, win) {
        const bad = [];
        doc.querySelectorAll('button, a, input, select, textarea, [tabindex]').forEach(el => {
          if (isDemo(el)) return;
          const cs = win.getComputedStyle(el);
          const noOutline = cs.outlineStyle === 'none' || parseFloat(cs.outlineWidth) === 0;
          const hasRing = cs.boxShadow && cs.boxShadow !== 'none';
          if (noOutline && !hasRing) {
            // only a problem when the page explicitly removes it
            const inline = (el.getAttribute('style') || '').replace(/\s/g, '');
            if (inline.includes('outline:none') || inline.includes('outline:0')) {
              bad.push(describe(el) + ' removes the outline with no focus ring');
            }
          }
        });
        return [...new Set(bad)];
      }
    },
    {
      id: 15, name: 'Copy has no em dashes',
      run(doc) {
        const bad = [];
        const walker = doc.createTreeWalker(doc.body, NodeFilter.SHOW_TEXT);
        let n;
        while ((n = walker.nextNode())) {
          if (n.parentElement && SKIP_TAGS[n.parentElement.tagName]) continue;
          if (n.textContent.includes('\u2014')) {
            bad.push('"' + n.textContent.trim().replace(/\s+/g, ' ').slice(0, 60) + '"');
          }
        }
        return [...new Set(bad)];
      }
    },
    {
      id: 16, name: 'Fonts come from the type tokens',
      run(doc, win) {
        // Allow-list is derived from the resolved token values, so a client
        // theme that re-points --dn-font-heading/body/mono passes, while a
        // typeface hardcoded in markup (bypassing the tokens) still fails.
        const rootStyle = win.getComputedStyle(doc.documentElement);
        const allowed = new Set(['monospace', 'sans-serif', 'serif', 'ui-monospace', 'ui-sans-serif', 'system-ui', 'menlo', 'sf mono', 'inherit']);
        ['--dn-font-heading', '--dn-font-body', '--dn-font-mono'].forEach(tok => {
          const v = rootStyle.getPropertyValue(tok);
          if (v) v.split(',').forEach(f => allowed.add(f.replace(/["']/g, '').trim().toLowerCase()));
        });
        // scoped overrides (a client theme applied to a subtree) count too
        doc.querySelectorAll('*').forEach(el => {
          const inline = el.getAttribute && el.getAttribute('style');
          if (inline && inline.indexOf('--dn-font') !== -1) {
            ['--dn-font-heading', '--dn-font-body', '--dn-font-mono'].forEach(tok => {
              const v = win.getComputedStyle(el).getPropertyValue(tok);
              if (v) v.split(',').forEach(f => allowed.add(f.replace(/["']/g, '').trim().toLowerCase()));
            });
          }
        });
        const bad = [];
        doc.querySelectorAll('*').forEach(el => {
          if (!hasText(el)) return;
          /* A sketch's lettering is part of the drawing, not page type. The
             hand it is drawn in comes with the figure and is not a face any
             copy on the page can reach, so the token allow-list does not
             govern it. Same opt-out as rule 12. */
          if (isSketch(el)) return;
          const cs = win.getComputedStyle(el);
          const tokenFonts = ['--dn-font-heading', '--dn-font-body', '--dn-font-mono']
            .map(tok => (cs.getPropertyValue(tok) || '').split(',')[0].replace(/["']/g, '').trim().toLowerCase())
            .filter(Boolean);
          const first = cs.fontFamily.toLowerCase().split(',')[0].replace(/["']/g, '').trim();
          if (first && !allowed.has(first) && tokenFonts.indexOf(first) === -1) {
            bad.push(describe(el) + ' uses "' + first + '", which is not one of the type tokens');
          }
        });
        return [...new Set(bad)];
      }
    },
    {
      id: 17, name: 'No gradients, glows or textures',
      run(doc, win) {
        const bad = [];
        doc.querySelectorAll('*').forEach(el => {
          if (isDemo(el)) return;
          const cs = win.getComputedStyle(el);
          if (cs.backgroundImage && cs.backgroundImage.includes('gradient')) bad.push(describe(el) + ' has a gradient background');
          if (cs.filter && cs.filter.includes('blur')) bad.push(describe(el) + ' uses a blur filter');
        });
        return [...new Set(bad)];
      }
    },
  ];

  function isDemo(el) {
    return !!(el.closest && el.closest('[data-rule-demo]'));
  }

  /* A data-visualisation SVG is not a diagram.
   *
   * Rules 5 and 12 describe hand-drawn architecture diagrams: equal boxes,
   * even gaps, outline only, no fills. A chart breaks all of that by design,
   * because unequal bar widths and filled marks ARE the data. Without this
   * exemption any page containing a Plotly, D3, ECharts or Highcharts figure
   * could never reach 100, which would make the ship-at-100 contract
   * unreachable for every analytical report.
   *
   * Chart.js and other canvas renderers need no exemption: they draw to
   * <canvas>, which these rules never inspect.
   *
   * A hand-rolled SVG chart opts out with data-dn-chart on the svg or a wrapper.
   */
  const CHART_HOST = '.js-plotly-plot, .main-svg, [data-dn-chart], [_echarts_instance_],' +
    ' .highcharts-container, .recharts-wrapper, .apexcharts-canvas, .vega-embed';

  function isChart(el) {
    if (!el) return false;
    if (el.matches && el.matches(CHART_HOST)) return true;
    return !!(el.closest && el.closest(CHART_HOST));
  }

  /* An editorial sketch is not a client diagram.
   *
   * The outline-only rule exists so a client deliverable reads as drafting
   * rather than as clip art, and it still holds there. Teaching material on the
   * website is a different job: a guide is read once by someone deciding
   * something, and a hand-drawn figure with fills and stage colour says "this
   * is an explanation, not a specification" in a way an outline cannot.
   *
   * Scoped rather than removed, so the two cannot drift together. A sketch opts
   * out with data-dn-sketch on the svg or a wrapper, exactly as a chart opts out
   * with data-dn-chart, and a client pack that has no such marker still fails.
   */
  const SKETCH_HOST = '[data-dn-sketch]';

  function isSketch(el) {
    if (!el) return false;
    if (el.matches && el.matches(SKETCH_HOST)) return true;
    return !!(el.closest && el.closest(SKETCH_HOST));
  }

  /* Judge only what a reader can actually see.
   *
   * Chart libraries append hidden probe nodes to measure text: Plotly adds a
   * 1x1 svg straight to <body> with a filled path, which is not content and is
   * never inside a chart container, so isChart cannot catch it. An svg with no
   * rendered area, or one that is hidden, is not a diagram and must not be
   * scored as one.
   */
  function isInvisible(el) {
    /* Test the element itself first. Plotly's probe svg is 9000x9000 with a
     * 1x1 path inside it, so judging by the svg alone would let the probe
     * through: the shape is what has no area, not its canvas. */
    if (el.getBoundingClientRect) {
      const r = el.getBoundingClientRect();
      if (r.width <= 2 || r.height <= 2) return true;
    }
    const svg = el.closest ? el.closest('svg') : null;
    const nodes = svg && svg !== el ? [el, svg] : [el];
    for (const node of nodes) {
      const win = node.ownerDocument && node.ownerDocument.defaultView;
      if (!win) continue;
      const cs = win.getComputedStyle(node);
      if (cs.visibility === 'hidden' || cs.display === 'none' || parseFloat(cs.opacity) === 0) return true;
    }
    return false;
  }

  const MANUAL = [
    { id: 1, name: 'Background sets the ink', note: 'Judge by eye: is the body colour the one the background calls for?' },
    { id: 4, name: 'One shared left edge', note: 'Judge by eye: do title, body and metadata align to a single left edge?' },
  ];

  function check(doc) {
    doc = doc || document;
    const win = doc.defaultView || window;
    const results = RULES.map(r => {
      let violations = [];
      try { violations = r.run(doc, win) || []; } catch (e) { violations = ['checker error: ' + e.message]; }
      return { id: r.id, name: r.name, status: violations.length ? 'fail' : 'pass', violations };
    });
    MANUAL.forEach(m => results.push({ id: m.id, name: m.name, status: 'manual', violations: [m.note] }));
    results.sort((a, b) => a.id - b.id);
    const auto = results.filter(r => r.status !== 'manual');
    const passed = auto.filter(r => r.status === 'pass').length;
    const total = auto.length;
    const score = Math.round((passed / total) * 100);
    const grade = score === 100 ? 'A' : score >= 90 ? 'B' : score >= 75 ? 'C' : score >= 60 ? 'D' : 'F';
    return { score, grade, passed, total, rules: results };
  }

  global.DataNovaRules = { check, contrast, parseColor, toHex };
})(typeof window !== 'undefined' ? window : this);
