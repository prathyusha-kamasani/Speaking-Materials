// Replaces every <i data-lucide="name" class="..."></i> with the icon's SVG, from the vendored Lucide build.
// Used by build.py --web, so the website copy ships no icon library. Reads HTML on stdin, writes it to stdout.
const vm = require('vm'), fs = require('fs'), path = require('path');
const ctx = { window: {}, self: {} }; ctx.globalThis = ctx; vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(__dirname, '..', 'vendor', 'lucide.min.js'), 'utf8'), ctx);
const icons = (ctx.lucide || ctx.window.lucide || ctx.self.lucide).icons;
const pascal = n => n.split('-').map(s => s.charAt(0).toUpperCase() + s.slice(1)).join('');
const attrs = o => Object.entries(o).map(([k, v]) => `${k}="${v}"`).join(' ');
let html = fs.readFileSync(0, 'utf8'), missing = new Set();
html = html.replace(/<i data-lucide="([a-z0-9-]+)" class="([^"]*)"><\/i>/g, (m, name, cls) => {
  const node = icons[pascal(name)];
  if (!node) { missing.add(name); return m; }
  const inner = node.map(([tag, a]) => `<${tag} ${attrs(a)}/>`).join('');
  return `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-${name} ${cls}" aria-hidden="true">${inner}</svg>`;
});
if (missing.size) { console.error('missing icons: ' + [...missing].join(', ')); process.exit(1); }
process.stdout.write(html);
