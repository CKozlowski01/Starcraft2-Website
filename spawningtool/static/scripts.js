function homeBtn() {
  document.location.href = "index.html";
}

function replayBtn() {
  document.location.href = "replays.html";
}

function order() {

  var select = document.getElementById("sel");
  console.log(select.options[select.selectedIndex].value);

}
var hide = document.getElementById("hide");
var show = document.getElementById("show");
var btn = document.getElementById("confirm");
  
btn.onclick = function () {
  if (hide.style.display === "block") {
    hide.style.display = "none";
    show.style.display = "block";
  } else {
    hide.style.display = "block";
    show.style.display = "none";
  }
}

var ele = document.getElementById('sel');

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
        //console.log('<option value="' + json[key]['name'] + json[key]['name'] + '">' + '</option>')
        //console.log(json[key]);
    }
})
.catch(function () {
   this.dataError = true;
})