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
  function show(i) {
    document.querySelectorAll('video').forEach(function (v) { v.pause(); });
    cur = Math.max(0, Math.min(slides.length - 1, i));
    slides.forEach(function (el, k) { el.classList.toggle('active', k === cur); });
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
