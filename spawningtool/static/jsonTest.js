    var ele = document.getElementById('sel');
    var order = document.getElementById('order');

    fetch('../static/buildOrder.json')
   .then(response => {
       if (!response.ok) {
           throw new Error("HTTP error " + response.status);
       }
       return response.json();
   })
   .then(json => json.players).then(json => {
        for (var key in json){
            ele.innerHTML = ele.innerHTML +
                '<option value="' + json[key]['name'] + '">' + json[key]['name'] + '</option>';
            console.log('<option value="' + json[key]['name'] + json[key]['name'] + '">' + '</option>')
            console.log(json[key]);
        }
   })
   .catch(function () {
       this.dataError = true;
   })
   //}