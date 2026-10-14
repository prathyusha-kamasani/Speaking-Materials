/* Deck runtime: scale to fit, keyboard navigation, speaker notes, overview, presenter view, black screen. */
(function () {
  var slides = Array.prototype.slice.call(document.querySelectorAll('.slide'));
  var frame = document.getElementById('frame');
  var notes = document.getElementById('notes');
  var cur = 0;
  // presenter view: index.html?presenter, opened by S from the audience window. The two windows keep each other in step
  // with postMessage (it works between file:// pages, where storage-based channels may not)
  var box = null;
  var presenter = /[?&]presenter\b/.test(location.search), peer = presenter ? window.opener : null, black = false;
  function send(msg) {
    msg.deck = 1;
    try { if (peer && !peer.closed) peer.postMessage(msg, '*'); } catch (err) { /* the other window is gone */ }
  }

  function fit() {
    if (document.body.classList.contains('all') || document.body.classList.contains('grid')) { frame.style.transform = ''; return; }
    if (presenter) { layoutPresenter(); return; }
    var s = Math.min(window.innerWidth / 1920, window.innerHeight / 1080);
    frame.style.transform = 'translate(-50%, -50%) scale(' + s + ')';
  }
  // morph: an element marked data-morph="key" on the slide you leave glides to the element with the same key on the slide
  // you open (FLIP: measure both, start the new one where the old one was, then let it travel home)
  function morphRects(el) {
    var out = {};
    if (!el || document.body.classList.contains('all') || document.body.classList.contains('grid')) return out;
    el.querySelectorAll('[data-morph]').forEach(function (m) { out[m.getAttribute('data-morph')] = m.getBoundingClientRect(); });
    return out;
  }
  function morph(from, to) {
    var keys = Object.keys(from);
    if (!keys.length || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    var s = frame.getBoundingClientRect().width / 1920 || 1, moved = 0, matched = 0;
    to.querySelectorAll('[data-morph]').forEach(function (m) {
      var a = from[m.getAttribute('data-morph')]; if (!a) return;
      matched += 1;  // a shared element that stays put still makes this slide a continuation: no entrance replay
      var b = m.getBoundingClientRect();
      var dx = (a.left - b.left) / s, dy = (a.top - b.top) / s, sc = b.width ? a.width / b.width : 1;
      if (Math.abs(dx) < 1 && Math.abs(dy) < 1 && Math.abs(sc - 1) < 0.01) return;
      moved += 1;
      m.style.transition = 'none'; m.style.transformOrigin = 'top left';
      m.style.transform = 'translate(' + dx + 'px,' + dy + 'px) scale(' + sc + ')';
      m.getBoundingClientRect();
      m.style.transition = 'transform 0.7s cubic-bezier(0.2, 0.7, 0.2, 1)'; m.style.transform = '';
    });
    if (moved || matched) to.classList.add('morphed');  // stays until the slide is left, so the entrance builds never replay
  }
  function show(i, quiet) {
    document.querySelectorAll('video').forEach(function (v) { v.pause(); });
    if (box) collapse();
    var before = morphRects(slides[cur]);
    cur = Math.max(0, Math.min(slides.length - 1, i));
    slides.forEach(function (el, k) { el.classList.toggle('active', k === cur); el.classList.remove('morphed'); });
    morph(before, slides[cur]);
    countUp(slides[cur]);
    var t = slides[cur].querySelector('template.notes');
    notes.textContent = t ? t.content.textContent : '';
    history.replaceState(null, '', '#' + (cur + 1));
    if (presenter) updatePresenter();
    if (!quiet) send({ go: cur });
  }
  function setAll(on) {
    document.body.classList.toggle('all', on);
    fit();
  }
  // overview: A shows every slide as a tile (the current one outlined); click a tile, or press A or Esc, to go back
  function setGrid(on) {
    document.body.classList.toggle('grid', on);
    slides.forEach(function (el, k) { el.classList.toggle('current', on && k === cur); });
    if (on) { document.querySelectorAll('video').forEach(function (v) { v.pause(); }); slides[cur].scrollIntoView({ block: 'center' }); }
    else window.scrollTo(0, 0);
    fit();
  }
  slides.forEach(function (el, k) {
    el.addEventListener('click', function () { if (document.body.classList.contains('grid')) { setGrid(false); show(k); } });
  });
  // image viewer: the expand button (or E) opens the slide's image full screen; Esc, E or a click closes it
  box = document.createElement('div'); box.className = 'lightbox';
  box.innerHTML = '<img alt=""><button class="vbtn" type="button">Close</button>';
  document.body.appendChild(box);
  function expand(slide) {
    var img = slide && slide.querySelector('.viewer img'); if (!img) return false;
    box.querySelector('img').src = img.src; box.querySelector('img').alt = img.alt;
    box.classList.add('on'); box.scrollTop = 0; box.focus(); return true;
  }
  function collapse() { box.classList.remove('on'); }
  // a link button keeps its address in data-href: a real href would show the URL (with its IDs) on the projector on hover
  document.querySelectorAll('[data-href]').forEach(function (b) {
    b.addEventListener('click', function () { window.open(b.getAttribute('data-href'), '_blank', 'noopener'); });
  });
  box.addEventListener('click', function (e) { if (e.target.tagName !== 'IMG') collapse(); });
  document.querySelectorAll('.viewer [data-expand], .viewer img').forEach(function (b) {
    b.addEventListener('click', function () { if (presenter) send({ key: 'E' }); else expand(b.closest('.slide')); });
  });
  document.addEventListener('keydown', function (e) {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    var k = e.key;
    if (box.classList.contains('on')) {  // while expanded, arrows and space scroll the image, not the deck
      if (k === 'Escape' || k === 'e' || k === 'E') { e.preventDefault(); collapse(); }
      return;
    }
    if (document.body.classList.contains('grid')) {  // overview: arrows move the outline, Enter opens it, A or Esc closes
      var step = { ArrowRight: 1, ArrowLeft: -1, ArrowDown: 0, ArrowUp: 0 }[k];
      if (step !== undefined) {
        e.preventDefault();
        if (!step) {  // up and down move a whole row
          var top0 = slides[0].getBoundingClientRect().top, per = slides.filter(function (el) { return el.getBoundingClientRect().top === top0; }).length;
          step = k === 'ArrowDown' ? per : -per;
        }
        var n = Math.max(0, Math.min(slides.length - 1, cur + step));
        slides[cur].classList.remove('current'); cur = n; slides[cur].classList.add('current');
        slides[cur].scrollIntoView({ block: 'nearest' });
      }
      else if (k === 'Enter') { e.preventDefault(); setGrid(false); show(cur); }
      else if (k === 'Escape' || k === 'a' || k === 'A') { setGrid(false); show(cur); }
      return;
    }
    if (k === 'b' || k === 'B' || k === '.') { e.preventDefault(); setBlack(!black); send({ black: black }); return; }
    if (k === 's' || k === 'S' || (presenter && k === 'Escape')) { if (presenter) window.close(); else openPresenter(); return; }
    if (presenter && (k === 'p' || k === 'P' || k === 'e' || k === 'E')) { e.preventDefault(); send({ key: k.toUpperCase() }); return; }
    if (k === 'e' || k === 'E') { if (expand(slides[cur])) e.preventDefault(); return; }
    if (k === 'ArrowRight' || k === 'ArrowDown' || k === 'PageDown' || k === ' ') { e.preventDefault(); show(cur + 1); }
    else if (k === 'ArrowLeft' || k === 'ArrowUp' || k === 'PageUp') { e.preventDefault(); show(cur - 1); }
    else if (k === 'Home') show(0);
    else if (k === 'End') show(slides.length - 1);
    else if (k === 'n' || k === 'N') notes.classList.toggle('on');
    else if (k === 'p' || k === 'P') playPause();
    else if (k === 'a' || k === 'A') setGrid(!document.body.classList.contains('grid'));
    else if (k === 'f' || k === 'F') {
      if (document.fullscreenElement) document.exitFullscreen(); else document.documentElement.requestFullscreen();
    }
  });
  function playPause() {
    var v = slides[cur].querySelector('video');
    if (v) { if (v.paused) v.play(); else v.pause(); }
  }
  // black screen: B (or the full stop many clickers send) blanks the audience screen; the presenter view only shows a flag
  var blackout = document.createElement('div'); blackout.id = 'black'; document.body.appendChild(blackout);
  function setBlack(on) { black = on; document.body.classList.toggle('black', on); }
  // S with a second screen attached: this window goes fullscreen on the projector and the presenter window opens on the
  // laptop, from one key press (the Window Management API; the browser asks once). Without it, or on one screen, the
  // presenter window simply opens and you drag it where it belongs.
  var toastEl = document.createElement('div'); toastEl.id = 'toast'; document.body.appendChild(toastEl);
  function toast(msg) {
    toastEl.textContent = msg; toastEl.classList.add('on');
    clearTimeout(toast.t); toast.t = setTimeout(function () { toastEl.classList.remove('on'); }, 5000);
  }
  function presenterUrl() { return location.pathname + '?presenter#' + (cur + 1); }
  function openPlain() {
    var w = window.open(presenterUrl(), 'deck-presenter', 'popup,width=1440,height=900');
    if (w) peer = w; else toast('The browser blocked the presenter window. Allow pop-ups for this page, then press S again.');
  }
  async function openPresenter() {
    var state = 'unsupported';
    if ('getScreenDetails' in window) {
      try { state = (await navigator.permissions.query({ name: 'window-management' })).state; } catch (err) { state = 'unsupported'; }
    }
    if (state === 'prompt') {  // the permission prompt uses up this key press, so the windows are placed on the next S
      try { await window.getScreenDetails(); toast('Thanks. Press S again to place the windows.'); }
      catch (err) { openPlain(); }
      return;
    }
    if (state !== 'granted') { openPlain(); return; }
    var sd = await window.getScreenDetails();
    if (sd.screens.length < 2) { openPlain(); return; }
    var laptop = sd.screens.find(function (x) { return x.isInternal; }) || sd.currentScreen;
    var projector = sd.screens.find(function (x) { return x !== laptop; });
    try { await document.documentElement.requestFullscreen({ screen: projector }); } catch (err) { toast('Press F to go fullscreen on the projector.'); }
    var w = window.open(presenterUrl(), 'deck-presenter', 'popup,left=' + laptop.availLeft + ',top=' + laptop.availTop +
      ',width=' + laptop.availWidth + ',height=' + laptop.availHeight);
    if (w) peer = w; else toast('The browser blocked the presenter window. Allow pop-ups for this page, then press S again.');
  }
  window.addEventListener('message', function (e) {
    var d = e.data; if (!d || !d.deck) return;
    if (!presenter && !peer && e.source) peer = e.source;
    if (d.hello) { send({ go: cur, black: black }); return; }
    if (document.body.classList.contains('grid')) setGrid(false);
    if (typeof d.go === 'number' && d.go !== cur) show(d.go, true);
    if (typeof d.black === 'boolean') setBlack(d.black);
    if (d.key === 'P') playPause();
    if (d.key === 'E') { if (box.classList.contains('on')) collapse(); else expand(slides[cur]); }
    if (presenter && typeof d.playing === 'boolean') {  // mirror the audience video, muted, so you see what they see
      var v = slides[cur].querySelector('video');
      if (v && d.src && v.getAttribute('src') !== d.src) v.src = d.src;
      if (v) { v.muted = true; if (Math.abs(v.currentTime - d.t) > 1) v.currentTime = d.t; if (d.playing) v.play(); else v.pause(); }
    }
  });
  if (!presenter) document.querySelectorAll('video').forEach(function (v) {
    ['play', 'pause', 'seeked'].forEach(function (ev) { v.addEventListener(ev, function () { send({ playing: !v.paused, t: v.currentTime, src: v.getAttribute('src') }); }); });
  });
  // presenter layout: the current slide large on the left; the next slide, the notes, a timer and the clock on the right
  var pbar, pnext, pnotes, pkeys, pcount, ptimer, pclock, pflag, t0 = Date.now();
  if (presenter) {
    document.body.classList.add('presenter');
    document.title = 'Presenter: ' + document.title;
    pbar = document.createElement('div'); pbar.id = 'pbar';
    pbar.innerHTML = '<span id="pcount"></span><button type="button" id="ptimer" title="Click to restart">00:00</button>' +
      '<span id="pclock"></span><span id="pflag">Screen is black (B)</span>';
    pnext = document.createElement('div'); pnext.id = 'pnext';
    pnotes = document.createElement('div'); pnotes.id = 'pnotes';
    pkeys = document.createElement('div'); pkeys.id = 'pkeys';
    pkeys.innerHTML = [['&rarr; &larr;', 'next, back'], ['A', 'overview'], ['P', 'play or pause video'], ['E', 'expand image'],
      ['B', 'black screen'], ['F', 'fullscreen'], ['Home End', 'first, last'], ['S Esc', 'close this view']]
      .map(function (k) { return '<span>' + k[0].split(' ').map(function (x) { return '<kbd>' + x + '</kbd>'; }).join('') + k[1] + '</span>'; }).join('');
    document.body.appendChild(pbar); document.body.appendChild(pnext); document.body.appendChild(pnotes); document.body.appendChild(pkeys);
    pcount = pbar.querySelector('#pcount'); ptimer = pbar.querySelector('#ptimer'); pclock = pbar.querySelector('#pclock');
    ptimer.addEventListener('click', function () { t0 = Date.now(); tick(); });
    document.querySelectorAll('video').forEach(function (v) { v.muted = true; });
    setInterval(tick, 1000);
  }
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function tick() {
    var sec = Math.floor((Date.now() - t0) / 1000), now = new Date();
    ptimer.textContent = pad(Math.floor(sec / 60)) + ':' + pad(sec % 60);
    pclock.textContent = pad(now.getHours()) + ':' + pad(now.getMinutes());
  }
  function layoutPresenter() {
    var gap = 24, top = 72, W = window.innerWidth, H = window.innerHeight;
    var leftW = Math.round(W * 0.62) - gap * 1.5, rightW = W - leftW - gap * 3;
    var s = Math.min(leftW / 1920, (H - top - gap) / 1080);
    frame.style.transform = 'scale(' + s + ')';
    pkeys.style.top = (top + 1080 * s + gap) + 'px'; pkeys.style.width = (1920 * s) + 'px';
    pnext.style.left = (gap * 2 + 1920 * s) + 'px'; pnext.style.width = rightW + 'px';
    var nz = rightW / 1920, nh = Math.round(1080 * nz);
    var c = pnext.querySelector('.slide'); if (c) c.style.zoom = nz;
    pnext.style.height = (nh + 28) + 'px';
    pnotes.style.left = pnext.style.left; pnotes.style.width = rightW + 'px'; pnotes.style.top = (top + nh + 28 + gap) + 'px';
  }
  function updatePresenter() {
    pcount.textContent = (cur + 1) + ' / ' + slides.length;
    pnext.innerHTML = '<div class="plabel">' + (cur + 1 < slides.length ? 'Next' : 'End of the deck') + '</div>';
    if (cur + 1 < slides.length) {
      var c = slides[cur + 1].cloneNode(true);
      c.removeAttribute('id'); c.classList.add('active');
      c.querySelectorAll('video').forEach(function (v) { v.removeAttribute('src'); v.removeAttribute('data-playlist'); v.preload = 'none'; });
      pnext.appendChild(c);
    }
    var t = slides[cur].querySelector('template.notes');
    pnotes.textContent = t ? t.content.textContent : 'No notes for this slide.';
    pnotes.scrollTop = 0;
    if (pbar) tick();
    layoutPresenter();
  }
  window.addEventListener('resize', fit);
  // a slot with a playlist plays its clips in order
  document.querySelectorAll('video[data-playlist]').forEach(function (v) {
    var list = v.getAttribute('data-playlist').split(','), idx = 0;
    var rates = (v.getAttribute('data-rates') || '').split(',').map(Number);
    function applyRate() { var r = rates[idx] || 1; v.defaultPlaybackRate = r; v.playbackRate = r; }
    v.addEventListener('loadedmetadata', applyRate);
    v.addEventListener('play', applyRate);
    v.addEventListener('ended', function () {
      if (idx < list.length - 1) { idx += 1; v.src = list[idx]; v.play(); }
    });
  });
  // builds: number the children of each stagger or sequence, and each table row and cell, for the CSS delays
  document.querySelectorAll('.stagger, .seq').forEach(function (g) {
    Array.prototype.forEach.call(g.children, function (c, i) { c.style.setProperty('--i', i); });
  });
  document.querySelectorAll('table.autoplay tbody tr').forEach(function (tr, r) {
    var rows = tr.parentNode.children, ri = Array.prototype.indexOf.call(rows, tr);
    Array.prototype.forEach.call(tr.children, function (td, c) { td.style.setProperty('--r', ri); td.style.setProperty('--c', c); });
  });
  // count-up: a figure marked data-countup rolls up from zero when its slide opens, then settles on the real text
  function countUp(slide) {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    slide.querySelectorAll('[data-countup]').forEach(function (el, k) {
      var final = el.getAttribute('data-final') || el.textContent; el.setAttribute('data-final', final);
      var parts = final.split(/(\d+(?:,\d{3})*)/), t0 = null, dur = 1100, delay = 650 + k * 120;  // after its card has landed (stagger: .25s + i * .12s, .6s rise)
      function frame(ts) {
        if (t0 === null) t0 = ts;
        var p = Math.min(1, Math.max(0, (ts - t0 - delay) / dur)), e = 1 - Math.pow(1 - p, 3);
        el.textContent = parts.map(function (s) { return /^\d/.test(s) ? Math.round(parseInt(s.replace(/,/g, ''), 10) * e).toLocaleString('en-GB') : s; }).join('');
        if (p < 1) requestAnimationFrame(frame); else el.textContent = final;
      }
      requestAnimationFrame(frame);
    });
  }
  if (window.lucide) window.lucide.createIcons();
  var start = parseInt((location.hash || '').slice(1), 10);
  show(isNaN(start) ? 0 : start - 1, true);
  if (presenter) send({ hello: 1 });
  if (/[?&]all\b/.test(location.search)) setAll(true);
  fit();
})();
