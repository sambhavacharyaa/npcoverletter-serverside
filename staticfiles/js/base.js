// Get elements
const menuBtn = document.getElementById("menu-btn");
const mobileMenu = document.getElementById("mobile-menu");
const menuIcon = document.getElementById("menu-icon");

// Toggle menu
menuBtn.addEventListener("click", () => {

    // Show/hide menu
    mobileMenu.classList.toggle("hidden");

    // Rotate hamburger icon
    menuIcon.classList.toggle("rotate-90");

});

const menuBtn = document.getElementById("menu-btn");
const mobileMenu = document.getElementById("mobile-menu");

menuBtn.addEventListener("click", () => {

    // Open/close mobile menu
    mobileMenu.classList.toggle("hidden");

});