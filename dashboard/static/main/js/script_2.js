// Simple smooth scroll & UX hooks later
console.log("TechSpace Loaded Successfully");

document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll(".program-card");

    cards.forEach(card => {
        card.addEventListener("click", function () {

            // Close other cards
            cards.forEach(c => {
                if (c !== card) {
                    c.classList.remove("active");
                }
            });

            // Toggle current card
            card.classList.toggle("active");
        });
    });

    console.log("TechSpace interactive programs loaded");
});

