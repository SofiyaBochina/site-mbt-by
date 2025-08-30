document.addEventListener("DOMContentLoaded", () => {

    document.querySelectorAll('.goods__item').forEach(item => {
        item.addEventListener('click', () => {
            item.classList.toggle('flipped');
        });
    });

    const burger = document.getElementById("burgerBtn");
    const nav = document.getElementById("nav");

    burger.addEventListener("click", (e) => {
        e.stopPropagation();
        nav.classList.toggle("open");
    });

    nav.querySelectorAll("a").forEach(link => {
        link.addEventListener("click", () => {
            nav.classList.remove("open");
        });
    });

    document.addEventListener("click", (e) => {
        if (!nav.contains(e.target) && !burger.contains(e.target)) {
            nav.classList.remove("open");
        }
    });
});