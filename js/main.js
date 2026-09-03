/* ==========================================================================
   Majestic Excalibur — main.js
   Core interactions: mobile nav, sticky-header state, back-to-top,
   accordions, and the dynamic footer year.
   Loaded with `defer`; no dependencies.
   ========================================================================== */
(function () {
  "use strict";

  /* ---------- Mobile navigation ------------------------------------------ */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("primary-nav");

  function closeNav() {
    if (!nav || !toggle) return;
    nav.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
    document.body.style.removeProperty("overflow");
  }

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
      // Lock scroll while the full-screen menu is open on mobile.
      document.body.style.overflow = open ? "hidden" : "";
    });

    // Close when a link is chosen or when resizing back to desktop.
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) closeNav();
    });
    window.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeNav();
    });
    var mq = window.matchMedia("(min-width: 901px)");
    (mq.addEventListener ? mq.addEventListener.bind(mq, "change") : mq.addListener.bind(mq))(closeNav);
  }

  /* ---------- Sticky header shadow on scroll ----------------------------- */
  var header = document.querySelector(".site-header");
  var toTop = document.querySelector(".to-top");

  function onScroll() {
    var y = window.scrollY || window.pageYOffset;
    if (header) header.classList.toggle("is-scrolled", y > 8);
    if (toTop) toTop.classList.toggle("is-visible", y > 600);
  }
  onScroll();
  window.addEventListener("scroll", onScroll, { passive: true });

  /* ---------- Back to top ------------------------------------------------- */
  if (toTop) {
    toTop.addEventListener("click", function () {
      var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      window.scrollTo({ top: 0, behavior: reduce ? "auto" : "smooth" });
    });
  }

  /* ---------- Accordions (FAQ) ------------------------------------------- */
  var triggers = document.querySelectorAll(".accordion__trigger");
  triggers.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var expanded = btn.getAttribute("aria-expanded") === "true";
      var panel = document.getElementById(btn.getAttribute("aria-controls"));
      btn.setAttribute("aria-expanded", String(!expanded));
      if (panel) panel.style.maxHeight = expanded ? null : panel.scrollHeight + "px";
    });
  });

  /* ---------- Dynamic footer year ---------------------------------------- */
  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();
})();
