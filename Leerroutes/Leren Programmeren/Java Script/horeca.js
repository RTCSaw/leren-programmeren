let boodschappen = {};
loop = true
while (loop) {
    let drinken = prompt("Wat wilt u bestellen?");
    if(drinken == "bier" || drinken =="wijn" || drinken =="fris" ){
        console.log("dit ken ik")
        let aantal = prompt("Hoeveel "+ drinken +" wilt u?");
        boodschappen[drinken]= aantal

    }else if (drinken == "stop"){
        loop = false 
    }
    else if (drinken in boodschappen){
        boodschappen[drinken]+= aantal
    }
    else{
        console.log("dit ken ik niet... probeer iets anders")
    }
};
for (key in boodschappen){
    console.log(boodschappen[key])
    document.getElementById("horeca").innerHTML += key + " " + boodschappen[key]+"<br>";
}
