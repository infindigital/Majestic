/* ==========================================================================
   Majestic Excalibur — counters.js
   Animates any element with [data-count] from 0 to its target when it first
   scrolls into view. Format: <span data-count="120" data-suffix="+">0</span>.
   ========================================================================== */
(function () {
  "use strict";

  var counters = document.querySelectorAll("[data-count]");
  if (!counters.length) return;

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function setFinal(el) {
    var target = parseFloat(el.getAttribute("data-count")) || 0;
    el.textContent = formatNumber(target, el);
  }

  function formatNumber(value, el) {
    var decimals = parseInt(el.getAttribute("data-decimals") || "0", 10);
    return value.toLocaleString(undefined, {
      minimumFractionDigits: decimals,
      maximumFractionDigits: decimals
    });
  }

  function animate(el) {
    var target = parseFloat(el.getAttribute("data-count")) || 0;
    var duration = parseInt(el.getAttribute("data-duration") || "1600", 10);
    var start = null;

    function tick(now) {
      if (start === null) start = now;
      var progress = Math.min((now - start) / duration, 1);
      // easeOutCubic for a natural deceleration
      var eased = 1 - Math.pow(1 - progress, 3);
      el.textContent = formatNumber(target * eased, el);
      if (progress < 1) requestAnimationFrame(tick);
      else setFinal(el);
    }
    requestAnimationFrame(tick);
  }

  if (reduce || !("IntersectionObserver" in window)) {
    counters.forEach(setFinal);
    return;
  }

  var observer = new IntersectionObserver(function (entries, obs) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        animate(entry.target);
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(function (el) { observer.observe(el); });
})();
