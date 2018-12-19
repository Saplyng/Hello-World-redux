var images = [
 "img/chick.jpg",
 "img/class.jpg",
 "img/iphonexs.jpg",
 "img/jamaica.jpg",
 "img/mathproblem.jpg",
 "img/mississippi.jpg",
 "img/pope-rope.jpg",
 "img/pringles.jpg",
 "img/spooktober-meme.jpg",
 "img/underage.jpg"];

var titles = [
 "Apparently you get a lot of karma for old memes",
 "I think we can all relate",
 "Sorry but no",
 "Pls make it stop ;-;",
 "that's right",
 "missippi",
 "Holy Moly",
 "Gotta get them all",
 "You guys do spooktober, right?",
 "We have all been there"];

var caption = [
  "Someone's got PTSD",
  "I know I can",
  "But you know screw iphone >.>",
  "I'm not on board but don't care either way",
  "I know I've been the proprieter of several apples",
  "you were so close",
  "gotta be chilly up there",
  "They're almost like pokemon, the last ones are legendaries",
  "Really though, who doesnt?",
  "finally getting to the big kids table"];

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
  var path = $("control").src;
  var testState = new RegExp("play");
  if(testState.test(path)){
    $("control").src = "img/pause.png";
    displayImage().slidedown(2000);
    }
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
