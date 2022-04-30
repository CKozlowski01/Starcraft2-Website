/*fetch("upload.html").then(response => response.json()).then(data =>{
    console.log(data)
})*/

/*fetch("C:/xampp/htdocs/Starcraft2-Website/test").then(response => {
    if (!response.ok) {
        throw new Error("HTTP error " + response.status);
    }
    console.log;
})*/

fetch('../static/test.json')
   .then(response => {
       if (!response.ok) {
           throw new Error("HTTP error " + response.status);
       }
       return response.json();
   })
   .then(json => {
       console.log(json.players.5.buildOrder.0.name);
   })
   .catch(function () {
       this.dataError = true;
   })