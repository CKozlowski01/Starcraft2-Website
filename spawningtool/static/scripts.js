function homeBtn() {
  document.location.href = "index.html";
}

function replayBtn() {
  document.location.href = "replays.html";
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

  var select = document.getElementById("sel");
  selection = select.options[select.selectedIndex].value
  console.log(selection);

  fetch('../static/buildOrder.json')
.then(response => {
   if (!response.ok) {
       throw new Error("HTTP error " + response.status);
   }
   return response.json();
})
.then(json => json.players).then(json => {
  var build = document.getElementById("order");
  for (var key in json){
    if(json[key].name == selection){
      for (i = 0; i < json[key].buildOrder.length; i++){
      //for (i = 0; i < 20; i++){
        time = (json[key].buildOrder[i].time);
        unit = (json[key].buildOrder[i].name);
        supply = (json[key].buildOrder[i].supply);
        build.innerHTML = build.innerHTML + "<li>" + time + " " + unit + " " + supply + "</li>";
        //build = build + "\n" + time + " " + unit + " " + supply;
        //var div = document.createElement("h2");
        //div.innerHTML = innerHTML + time + " " + unit + " " + supply + "\n";
        //var build = time + " " + unit + " " + supply + "\n";
        //document.getElementById("order").value = build;
        //document.getElementById("order").innerHTML = innerHTML + time + " " + unit + " " + supply + "\n";
      }
      //document.getElementById("order").innerHTML = build;
      //console.log(json[key].buildOrder.length);
    }
    else{
      console.log("hello")
    }
  }
})
//.then(json => json.players[selection])
//.then(players => buildOrder)
//.then(buildOrder)

.catch(function () {
   this.dataError = true;
})
}

var ele = document.getElementById('sel');

fetch('../static/buildOrder.json')
.then(response => {
   if (!response.ok) {
       throw new Error("HTTP error " + response.status);
   }
   //console.log(response);
   return response.json();
})
.then(json => json.players).then(json => {
    for (var key in json){
        ele.innerHTML = ele.innerHTML +
            '<option value="' + json[key].name + '">' + json[key].name + '</option>';
    }
})
.catch(function () {
   this.dataError = true;
})



//document.getElementById("confirm").addEventListener("click", bOrder());

//var confirmBtn = document.getElementById("confirm");

//confirmBtn.addEventListener("click", function () {
  //console.log(test);

//})