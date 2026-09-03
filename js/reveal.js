/* ==========================================================================
   Majestic Excalibur — reveal.js
   Reveals elements with the `.reveal` class as they scroll into view,
   using IntersectionObserver. Respects prefers-reduced-motion and degrades
   gracefully (everything shows) when the API is unavailable.
   ========================================================================== */
(function () {
  "use strict";

  var items = document.querySelectorAll(".reveal");
  if (!items.length) return;

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (reduce || !("IntersectionObserver" in window)) {
    items.forEach(function (el) { el.classList.add("is-visible"); });
    return;
  }

  var observer = new IntersectionObserver(function (entries, obs) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.14, rootMargin: "0px 0px -8% 0px" });

  items.forEach(function (el) { observer.observe(el); });
})();
