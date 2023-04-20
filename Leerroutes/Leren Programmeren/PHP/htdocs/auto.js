function getPersonButtonServer_clicked(event){
    console.dir(this.response);
}
let request = new XMLHttpRequest();
request.open('GET','auto.php');
request.responseType = 'json';
request.onload = load;
request.send();

