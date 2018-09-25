var images = [
  "http://via.placeholder.com/350x467?text=1",
  "http://via.placeholder.com/350x467?text=2",
  "http://via.placeholder.com/350x467?text=3",
  "http://via.placeholder.com/350x467?text=4",
  "http://via.placeholder.com/350x467?text=5"];

var titles = [
  "This is Image 1",
  "This is Image 2",
  "This is Image 3",
  "This is Image 4",
  "This is Image 5"];

var caption = [
  "This is the caption of Image 1",
  "This is the caption of Image 2",
  "This is the caption of Image 3",
  "This is the caption of Image 4",
  "This is the caption of Image 5"];

var count = images.count;
var image = new Image();
var timer;
var currentSlide = 0;

var $ = function(id){
  return document.getElementById(id);}


var preload = function(){
  for(var i=0; i < count;i++){
    image.src = images[i];
    images.push(image);
  }
}


var slidecontrol = function(){
  var path=$("control").src;
  var testState = new RegExp("play");
  if(testState.test(path)){
    $("control").src = "img/pause.png";
    displayImage();}
  else{
    $("control").src = "img/play.png";
    clearTimeout(timer);
  }
}

var displayImage = function(){
  if(currentSlide > 4){
    currentSlide = 0;}

  $("main_image").src = images[currentSlide];
  $("title").innerHTML = titles[currentSlide];
  $("caption").innerHTML = caption[currentSlide];

  currentSlide++;

  timer = setTimeout(displayImage, 5000);
}

var displayImageInt = function(){
  if(currentSlide > 4){
    currentSlide = 0;}

  $("main_image").src = images[currentSlide];
  $("title").innerHTML = titles[currentSlide];
  $("caption").innerHTML = caption[currentSlide];

  currentSlide++;}

function pauseIt(){
  clearInterval(timer);
  console.log("cleared timer");}

function resumeIt(){
  timer = setInterval(displayImageInt, 5000);
  console.log("rusumed timer");}







window.onload = function(){
  preload();

  timer = setInterval(displayImageInt, 5000);

}
