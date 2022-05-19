function homeBtn() {
  document.location.href = "index.html";
}

function replayBtn() {
  window.location.href = "replays.html";
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
  var hiddenBuild = document.getElementById("hiddenBuild")
  var race = document.getElementById("raceInput")
  for (var key in json){
    if(json[key].name == selection){
      raceValue = (json[key].pick_race)
      inc = 0;
      for (i = 0; i < json[key].buildOrder.length; i++){
        time = (json[key].buildOrder[i].time);
        unit = (json[key].buildOrder[i].name);
        supply = (json[key].buildOrder[i].supply);
        if (unit != 'SCV' && unit != 'Drone' && unit != 'Probe' && inc < 30){
          inc += 1;
          hiddenBuild.value += time + " " + unit + " " + supply + ", ";
          build.innerHTML = build.innerHTML + "<li>" + time + " " + unit + " " + supply + "</li>";
          race.value = raceValue
        }
        else{
          console.log('Worker Found')
        }
      }
      //document.getElementById("order").innerHTML = build;
      //console.log(json[key].buildOrder.length);
    }
    else{
      console.log("hello")
    }
    console.log(hiddenBuild.value)
    console.log(raceValue)
    //request.send('hiddenBuild = ' + hiddenBuild.innerHTML)
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