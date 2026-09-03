/* ==========================================================================
   Majestic Excalibur — contact-form.js
   Accessible client-side validation for the contact form. This is a STATIC
   site, so there is no server submit; on success we show a confirmation and
   reset. Wire the `submitForm()` promise to a real endpoint (Formspree, your
   own API, etc.) when deploying — see README for details.
   ========================================================================== */
(function () {
  "use strict";

  var form = document.getElementById("contact-form");
  if (!form) return;

  var status = form.querySelector(".form-status");

  var validators = {
    required: function (v) { return v.trim().length > 0; },
    email: function (v) { return /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v.trim()); },
    phone: function (v) { return v.trim() === "" || /^[+()\-\s\d]{7,20}$/.test(v.trim()); },
    minlen: function (v, n) { return v.trim().length >= n; }
  };

  function showError(field, message) {
    field.classList.add("field--error");
    var input = field.querySelector("input, select, textarea");
    var msg = field.querySelector(".field__error");
    if (input) input.setAttribute("aria-invalid", "true");
    if (msg) msg.textContent = message;
  }

  function clearError(field) {
    field.classList.remove("field--error");
    var input = field.querySelector("input, select, textarea");
    var msg = field.querySelector(".field__error");
    if (input) input.removeAttribute("aria-invalid");
    if (msg) msg.textContent = "";
  }

  function validateField(input) {
    var field = input.closest(".field");
    if (!field) return true;
    var value = input.value;
    var name = input.getAttribute("name");

    if (input.hasAttribute("required") && !validators.required(value)) {
      showError(field, "This field is required.");
      return false;
    }
    if (input.type === "email" && value && !validators.email(value)) {
      showError(field, "Please enter a valid email address.");
      return false;
    }
    if (name === "phone" && !validators.phone(value)) {
      showError(field, "Please enter a valid phone number.");
      return false;
    }
    if (name === "message" && value && !validators.minlen(value, 10)) {
      showError(field, "Please provide a little more detail (min 10 characters).");
      return false;
    }
    clearError(field);
    return true;
  }

  // Validate a field on blur once the user has interacted with it.
  form.querySelectorAll("input, select, textarea").forEach(function (input) {
    input.addEventListener("blur", function () { validateField(input); });
    input.addEventListener("input", function () {
      if (input.closest(".field").classList.contains("field--error")) validateField(input);
    });
  });

  // Placeholder submit — replace with a real POST to your endpoint.
  function submitForm(data) {
    return new Promise(function (resolve) {
      setTimeout(resolve, 900); // simulate network latency
    });
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    if (status) { status.className = "form-status"; status.textContent = ""; }

    var inputs = form.querySelectorAll("input, select, textarea");
    var valid = true;
    var firstInvalid = null;

    inputs.forEach(function (input) {
      if (!validateField(input)) {
        valid = false;
        if (!firstInvalid) firstInvalid = input;
      }
    });

    if (!valid) {
      if (status) {
        status.className = "form-status is-error";
        status.textContent = "Please fix the highlighted fields and try again.";
      }
      if (firstInvalid) firstInvalid.focus();
      return;
    }

    var btn = form.querySelector('[type="submit"]');
    var original = btn ? btn.textContent : "";
    if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }

    var data = Object.fromEntries(new FormData(form).entries());

    submitForm(data)
      .then(function () {
        form.reset();
        if (status) {
          status.className = "form-status is-success";
          status.textContent =
            "Thank you — your enquiry has been received. Our trading desk will respond within one business day.";
          status.focus && status.focus();
        }
      })
      .catch(function () {
        if (status) {
          status.className = "form-status is-error";
          status.textContent = "Something went wrong. Please email info@majesticexcalibur.com directly.";
        }
      })
      .finally(function () {
        if (btn) { btn.disabled = false; btn.textContent = original; }
      });
  });
})();
