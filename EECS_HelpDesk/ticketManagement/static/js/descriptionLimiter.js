let descriptions = document.getElementsByClassName("ticketDescription");

for (let x = 0; x < descriptions.length; x++) {
    descriptions[x].innerHTML = String(descriptions[x].innerHTML).slice(0, 50) + "..."
}