let descriptions = document.getElementsByClassName("descriptionLimited");

for (let x = 0; x < descriptions.length; x++) {
    if (String(descriptions[x].innerHTML).length > 50) {
        descriptions[x].innerHTML = String(descriptions[x].innerHTML).slice(0, 50) + "..."
    }
}