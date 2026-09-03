// TITLE SCREEN LOGIC
const loginTrigger = document.getElementById("login-trigger");
const loginForm = document.getElementById("login-form");
const passwordInput = document.getElementById("password-input");
const enterBtn = document.getElementById("enter-btn");
const screenTitle = document.getElementById("screen-title");
const screenMain = document.getElementById("screen-main");

loginTrigger.addEventListener("click", () => {
  loginTrigger.classList.add("hidden");
  loginForm.classList.remove("hidden");
  passwordInput.focus();
});

function attemptLogin() {
  if (passwordInput.value === "01052026") {
    screenTitle.classList.remove("active");
    screenTitle.classList.add("hidden");
    screenMain.classList.remove("hidden");
    screenMain.classList.add("active");
  } else {
    alert("Password salah!");
    passwordInput.value = "";
    passwordInput.focus();
  }
}

enterBtn.addEventListener("click", attemptLogin);
passwordInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") attemptLogin();
});

// DROPDOWN LOGIC
const dropdowns = document.querySelectorAll(".dropdown-group");

function closeDropdown(group) {
  const toggle = group.querySelector(".dropdown-toggle");
  const menu = group.querySelector(".dropdown-menu");
  toggle.setAttribute("aria-expanded", "false");
  menu.hidden = true;
}

dropdowns.forEach((group) => {
  const toggle = group.querySelector(".dropdown-toggle");
  const menu = group.querySelector(".dropdown-menu");
  toggle.addEventListener("click", () => {
    const isOpen = toggle.getAttribute("aria-expanded") === "true";
    dropdowns.forEach(closeDropdown);
    if (!isOpen) {
      toggle.setAttribute("aria-expanded", "true");
      menu.hidden = false;
    }
  });
});

document.addEventListener("click", (event) => {
  if (!event.target.closest(".dropdown-group"))
    dropdowns.forEach(closeDropdown);
});
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") dropdowns.forEach(closeDropdown);
});
document.querySelector("#new-story").addEventListener("click", () => {
  document.querySelector("#archive-message").textContent =
    "Quest baru dibuat! Pilih hari, tempat, dan mari mulai menyimpan momen berikutnya.";
});
document.querySelector("#continue-story").addEventListener("click", () => {
  document.querySelector("#archive-message").textContent =
    "Save data loaded: petualangan kita berlanjut dari kenangan terakhir.";
});

// SIDEBAR TAB LOGIC
const archiveScreen = document.getElementById("archive-screen");
const contentScreenTitle = document.getElementById("content-screen-title");
const backToHub = document.getElementById("back-to-hub");
const mainHub = document.querySelector(".main-hub");

const screenData = {
  random: "RANDOM IMAGES: Koleksi foto acak yang diambil dari keseharian kita.",
  romance: "ROMANCE IMAGES: Momen romantis yang tertangkap oleh kamera.",
  photobooth: "PHOTOBOOTH IMAGES: Hasil jepretan seru di photobooth.",
  alpha: "PH ALPHA GZ PROFILE: Informasi tentang Alpha.",
  partner: "PARTNER PROFILE: Informasi tentang pasangan.",
};

document
  .querySelectorAll(".dropdown-menu button[data-screen]")
  .forEach((btn) => {
    btn.addEventListener("click", () => {
      const screenId = btn.dataset.screen;
      const title = btn.textContent;
      const introText = screenData[screenId] || "Galeri " + title;

      contentScreenTitle.textContent = title.trim();
      document.getElementById("screen-intro").textContent = introText;

      mainHub.hidden = true;
      archiveScreen.hidden = false;

      // close dropdowns
      dropdowns.forEach(closeDropdown);
    });
  });

backToHub.addEventListener("click", () => {
  archiveScreen.hidden = true;
  mainHub.hidden = false;
});
