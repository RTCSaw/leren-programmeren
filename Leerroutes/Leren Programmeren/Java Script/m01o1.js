let uitleg = "In een parkeergarage passen 80 auto's op de begane grond en 120 op een verdieping.\n"+
"Vraag het gewenste aantal auto's in de garage en bereken het aantal verdiepingen wat je nodig hebt.";

alert(uitleg);
let gewenste_aantal_autos = prompt("Hoeveel autos wilt u kwijt in de parkeergarage?");
// Berekenen hier het aantal verdiepingen
if (gewenste_aantal_autos > 80){
    floors = Math.ceil((gewenste_aantal_autos - 80) / 120);
    var antwoord = "U heeft" + floors + "verdiepingen nodig";
} else {
    var antwoord = "Je hebt geen extra verdiepining nodig, alleen de begaande grond.";
};

antwoord = "U heeft" + floors + "verdiepingen nodig";
document.getElementById("antwoord").innerText = antwoord;

