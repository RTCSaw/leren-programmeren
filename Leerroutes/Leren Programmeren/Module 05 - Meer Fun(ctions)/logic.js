alert('nu zit je in de logic');

function clicked(event){
    console.log('clicked');
    var div = document.getElementById('result');
    div.innerHTML = "hallo vanuit de button"
}

button = document.getElementById('start')


console.dir(button);

// clicked(1);