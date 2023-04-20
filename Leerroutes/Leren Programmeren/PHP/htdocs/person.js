
persons = [
  {id: 12, name: 'Cathy Mill', role: 'manager', gender: 'female', age: 26},
  {id: 45, name: 'Mohamed Johnson', role: 'client', gender: 'male', age: 11},
  {id: 3, name: 'Rose Ogene', role: 'designer', gender: 'female', age: 21},
]
//console dir
function showPerson(person){
    console.dir(person);
    let personWindow = document.getElementById('person');
    personWindow.innerText = `name: ${person.name}\n role: ${person.role}`;
}
//servercom button
function load(event){
    person = this.response;
    showPerson(person);
}
getPersonButtonServer = document.getElementById('get-person-serverside')

function getPersonButtonServerclicked(event){
    console.log('second button clicked');
    let request = new XMLHttpRequest();
    request.open('GET','person.php');
    request.responseType = 'json';
    request.onload = load;
    //showPerson(persons[0]);
    request.send();
}
getPersonButtonServer.onclick = getPersonButtonServerclicked;

// niet server com button
getPersonButton = document.getElementById('get-person')

function getPersonButton_clicked(event){
    console.log('clicked');
  
    showPerson(persons[1]);
}
getPersonButton.onclick = getPersonButton_clicked;