UserInput = parseInt(prompt("hoeveel"))
uitkomst="";
for (regel = 1; regel <= UserInput; regel++){
    for( count = 1; count <= regel; count++){
        if (count ==1 ){
            uitkomst+= count;
        }else{
            uitkomst+= '-'+count;
        }
    }
    uitkomst += "<br>\n" 
}
for (regel = UserInput- 1; regel >= 1; regel--){
    for( count = 1; count <= regel; count++){
        if (count ==1 ){
            uitkomst+= count;
        }else{
            uitkomst+= '-'+count;
        }    
    }
    uitkomst += "<br>\n"
}
console.log(uitkomst)
document.getElementById("ruitje").innerHTML=uitkomst;