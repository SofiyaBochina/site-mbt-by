document.addEventListener("DOMContentLoaded", () => {

    document.querySelectorAll('.goods__item').forEach(item => {
        item.addEventListener('click', () => {
            item.classList.toggle('flipped');
        });
    });

    const burger = document.getElementById("burgerBtn");
    const nav = document.getElementById("nav");

    burger.addEventListener("click", () => {
        nav.classList.toggle("open");
    });
});