let points = 0;
let multiplier = 1;
const upgradeCost = 10;

const clickButton = document.getElementById("clickButton");
const upgradeButton = document.getElementById("upgradeButton");
const pointsDisplay = document.getElementById("points");
const multiplierDisplay = document.getElementById("multiplier");

clickButton.addEventListener("click", () => {
    points += multiplier;
    pointsDisplay.textContent = points;
});

upgradeButton.addEventListener("click", () => {
    if (points >= upgradeCost) {
        points -= upgradeCost;
        multiplier++;
        pointsDisplay.textContent = points;
        multiplierDisplay.textContent = multiplier + "x";
        upgradeButton.textContent = "Upgrade (Cost: " + upgradeCost * multiplier + " points)";
    } else {
        alert("Not enough points to upgrade!");
    }
});