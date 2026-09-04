/* Majestic Excalibur — site interactions */
(function () {
  "use strict";

  // ---- Mobile nav toggle ----
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      links.classList.toggle("open");
      toggle.classList.toggle("is-active");
    });
  }

  // ---- Mobile dropdown (tap to open Services submenu) ----
  document.querySelectorAll(".has-dropdown > a").forEach(function (a) {
    a.addEventListener("click", function (e) {
      if (window.innerWidth <= 760) {
        e.preventDefault();
        a.parentElement.classList.toggle("open-sub");
        var dd = a.parentElement.querySelector(".dropdown");
        if (dd) dd.style.display = dd.style.display === "block" ? "none" : "block";
      }
    });
  });

  // ---- FAQ accordion ----
  document.querySelectorAll(".faq-q").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var item = btn.closest(".faq-item");
      var isOpen = item.classList.contains("open");
      document.querySelectorAll(".faq-item.open").forEach(function (o) {
        o.classList.remove("open");
        var i = o.querySelector(".ico"); if (i) i.textContent = "+";
      });
      if (!isOpen) {
        item.classList.add("open");
        var ico = item.querySelector(".ico"); if (ico) ico.textContent = "–";
      }
    });
  });

  // ---- Contact / consultation forms (client-side, no backend) ----
  document.querySelectorAll("form[data-contact]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var note = form.querySelector(".form-note");
      var required = form.querySelectorAll("[required]");
      var ok = true;
      required.forEach(function (f) {
        if (!f.value.trim()) { ok = false; f.style.borderColor = "#c0392b"; }
        else { f.style.borderColor = ""; }
      });
      if (!note) {
        note = document.createElement("p");
        note.className = "form-note";
        form.appendChild(note);
      }
      if (!ok) {
        note.className = "form-note err";
        note.textContent = "Please fill in all required fields.";
        return;
      }
      note.className = "form-note ok";
      note.textContent = "Thank you — your message has been received. Our team will get back to you shortly.";
      form.reset();
    });
  });

  // ---- Active nav link based on current page ----
  var path = location.pathname.split("/").pop() || "index.html";
  document.querySelectorAll(".nav-links a").forEach(function (a) {
    var href = a.getAttribute("href");
    if (href === path) a.classList.add("active");
  });
})();
