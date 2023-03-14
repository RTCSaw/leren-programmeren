
loop = true
var drank ={"bier": {name: "bier",price: 2.50, amount:0}, "wijn": {name: "wijn",price: 2.80, amount:0}, "fris": {name: "fris",price: 2.05, amount:0}}
// var dranken =[{name: "bier",price: 2.50, amount:0}, {name: "wijn",price: 2.80, amount:0},  {name: "fris",price: 2.05, amount:0}]

// function haaldrankmetnaam (dranken,name){
//     for (let drankje of dranken){
//         if (drankje ["name"]== name)
//             return drankje
//     }
//     return null
// }
while (loop) {
    let drinken = prompt("Wat wilt u bestellen?");
    if(drinken in drank){
        console.log("dit ken ik")
        let aantal = prompt("Hoeveel "+ drinken +" wilt u?");
        drank[drinken].amount += parseInt(aantal);
    }else if (drinken == "stop"){
        loop = false 
    }
    else{
        console.log("dit ken ik niet... probeer iets anders")
    }
};
function bonnetje(drank){
    let totaal_bier = drank.bier.amount * drank.bier.price
    let totaal_wijn = drank.wijn.amount * drank.wijn.price
    let totaal_fris = drank.fris.amount * drank.fris.price

    let eindbedrag = Math.round(totaal_bier + totaal_wijn + totaal_fris)
    for (key in drank) {
        console.log(drank[key])
        document.getElementById("horeca").innerHTML += drank[key].name + ": " + drank[key].amount + " x " + drank[key].price.toFixed(2) + " euro" + "<br>";
    }
    document.getElementById("button").style.visibility="hidden";
    document.getElementById("horeca").innerHTML += "Eindbedrag: " + eindbedrag + " euro";

}
