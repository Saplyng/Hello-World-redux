var $ = function(id){
  return document.getElementById(id);
}

function changeText() {
  $("changeMe").innerHTML = "Goodbye";
}

function swapPH(){
$("imgSwap").src="http://via.placeholder.com/250x250";

}

function swapMurray(){
$("imgSwap").src= "http://fillmurray.com/250/250"
}
