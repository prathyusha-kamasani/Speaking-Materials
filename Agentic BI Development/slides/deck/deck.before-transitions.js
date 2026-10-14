/* Deck runtime: scale to fit, keyboard navigation, speaker notes, all-slides view. */
(function () {
  var slides = Array.prototype.slice.call(document.querySelectorAll('.slide'));
  var frame = document.getElementById('frame');
  var notes = document.getElementById('notes');
  var cur = 0;

  function fit() {
    if (document.body.classList.contains('all')) { frame.style.transform = ''; return; }
    var s = Math.min(window.innerWidth / 1920, window.innerHeight / 1080);
    frame.style.transform = 'translate(-50%, -50%) scale(' + s + ')';
  }
  // morph: an element marked data-morph="key" on the slide you leave glides to the element with the same key on the slide
  // you open (FLIP: measure both, start the new one where the old one was, then let it travel home)
  function morphRects(el) {
    var out = {};
    if (!el || document.body.classList.contains('all')) return out;
    el.querySelectorAll('[data-morph]').forEach(function (m) { out[m.getAttribute('data-morph')] = m.getBoundingClientRect(); });
    return out;
  }
  function morph(from, to) {
    var keys = Object.keys(from);
    if (!keys.length || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    var s = frame.getBoundingClientRect().width / 1920 || 1, moved = 0;
    to.querySelectorAll('[data-morph]').forEach(function (m) {
      var a = from[m.getAttribute('data-morph')]; if (!a) return;
      var b = m.getBoundingClientRect();
      var dx = (a.left - b.left) / s, dy = (a.top - b.top) / s, sc = b.width ? a.width / b.width : 1;
      if (Math.abs(dx) < 1 && Math.abs(dy) < 1 && Math.abs(sc - 1) < 0.01) return;
      moved += 1;
      m.style.transition = 'none'; m.style.transformOrigin = 'top left';
      m.style.transform = 'translate(' + dx + 'px,' + dy + 'px) scale(' + sc + ')';
      m.getBoundingClientRect();
      m.style.transition = 'transform 0.7s cubic-bezier(0.2, 0.7, 0.2, 1)'; m.style.transform = '';
    });
    if (moved) { to.classList.add('morphing'); setTimeout(function () { to.classList.remove('morphing'); }, 1100); }
  }
  function show(i) {
    document.querySelectorAll('video').forEach(function (v) { v.pause(); });
    var before = morphRects(slides[cur]);
    cur = Math.max(0, Math.min(slides.length - 1, i));
    slides.forEach(function (el, k) { el.classList.toggle('active', k === cur); });
    morph(before, slides[cur]);
    var t = slides[cur].querySelector('template.notes');
    notes.textContent = t ? t.content.textContent : '';
    history.replaceState(null, '', '#' + (cur + 1));
  }
  function setAll(on) {
    document.body.classList.toggle('all', on);
    fit();
  }
  document.addEventListener('keydown', function (e) {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    var k = e.key;
    if (k === 'ArrowRight' || k === 'ArrowDown' || k === 'PageDown' || k === ' ') { e.preventDefault(); show(cur + 1); }
    else if (k === 'ArrowLeft' || k === 'ArrowUp' || k === 'PageUp') { e.preventDefault(); show(cur - 1); }
    else if (k === 'Home') show(0);
    else if (k === 'End') show(slides.length - 1);
    else if (k === 'n' || k === 'N') notes.classList.toggle('on');
    else if (k === 'p' || k === 'P') {
      var v = slides[cur].querySelector('video');
      if (v) { if (v.paused) v.play(); else v.pause(); }
    }
    else if (k === 'a' || k === 'A') setAll(!document.body.classList.contains('all'));
    else if (k === 'f' || k === 'F') {
      if (document.fullscreenElement) document.exitFullscreen(); else document.documentElement.requestFullscreen();
    }
  });
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
  if (window.lucide) window.lucide.createIcons();
  var start = parseInt((location.hash || '').slice(1), 10);
  show(isNaN(start) ? 0 : start - 1);
  if (/[?&]all\b/.test(location.search)) setAll(true);
  fit();
})();
