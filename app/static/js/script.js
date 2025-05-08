function togglePassword(el) {
    const input = el.previousElementSibling;
    if (input.type === "password") {
      input.type = "text";
      el.textContent = "🙈";
    } else {
      input.type = "password";
      el.textContent = "👁️";
    }
  }
  