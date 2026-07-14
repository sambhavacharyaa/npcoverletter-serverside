const personalBtn = document.getElementById("personal-btn");
const businessBtn = document.getElementById("business-btn");

const personalForm = document.getElementById("personal-form");
const businessForm = document.getElementById("business-form");


personalBtn.addEventListener("click", () => {

    // Show personal form
    personalForm.classList.remove("hidden");
    businessForm.classList.add("hidden");

    // Change active button
    personalBtn.classList.add("active");
    businessBtn.classList.remove("active");

});


businessBtn.addEventListener("click", () => {

    // Show business form
    businessForm.classList.remove("hidden");
    personalForm.classList.add("hidden");

    // Change active button
    businessBtn.classList.add("active");
    personalBtn.classList.remove("active");

});

const menuBtn = document.getElementById("menu-btn");
const menu = document.getElementById("mobile-menu");

menuBtn.addEventListener("click", () => {

    // Toggle mobile menu visibility
    menu.classList.toggle("hidden");

});