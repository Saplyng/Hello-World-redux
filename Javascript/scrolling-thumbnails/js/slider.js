var $ = function (id) {
    return document.getElementById(id);
}

//declare vars and array

var images = ["img/chick.jpg",
    "img/class.jpg",
    "img/iphonexs.jpg",
    "img/jamaica.jpg",
    "img/mathproblem.jpg",
    "img/mississippi.jpg",
    "img/pope-rope.jpg",
    "img/pringles.jpg",
    "img/spooktober-meme.jpg",
    "img/underage.jpg"];
var titles = ["Apparently you get a lot of karma for old memes",
    "I think we can all relate",
    "Sorry but no",
    "Pls make it stop ;-;",
    "that's right",
    "missippi",
    "Holy Moly",
    "Gotta get them all",
    "You guys do spooktober, right?",
    "We have all been there"];
var captions = ["Someone's got PTSD",
    "I know I can",
    "But you know screw iphone >.>",
    "I'm not on board but don't care either way",
    "I know I've been the proprieter of several apples",
    "you were so close",
    "gotta be chilly up there",
    "They're almost like pokemon, the last ones are legendaries",
    "Really though, who doesnt?",
    "finally getting to the big kids table"];

var image = new Image();// creates an image object
var count = images.length - 1;// will change if we add more items to the image array
var someOtherCount = 2;

var ViewableImg = [0,1,2,3,4];


function displayViewImg(){
    $("ViewImg1").src = images[ViewableImg[0]];
    $("ViewImg2").src = images[ViewableImg[1]];
    $("ViewImg3").src = images[ViewableImg[2]];
    $("ViewImg4").src = images[ViewableImg[3]];
    $("ViewImg5").src = images[ViewableImg[4]];
    $("large").src = images[ViewableImg[2]];

    someOtherCount++;

    $("title").innerHTML = titles[someOtherCount];
    $("caption").innerHTML = captions[someOtherCount];


}

function displayViewImgreverse(){
    $("ViewImg1").src = images[ViewableImg[0]];
    $("ViewImg2").src = images[ViewableImg[1]];
    $("ViewImg3").src = images[ViewableImg[2]];
    $("ViewImg4").src = images[ViewableImg[3]];
    $("ViewImg5").src = images[ViewableImg[4]];
    $("large").src = images[ViewableImg[2]];

    someOtherCount--;

    $("title").innerHTML = titles[someOtherCount-1];
    $("caption").innerHTML = captions[someOtherCount-1];

}

function moveLeft(){
    ViewableImg[4] = ViewableImg[3];
    ViewableImg[3] = ViewableImg[2];
    ViewableImg[2] = ViewableImg[1];
    ViewableImg[1] = ViewableImg[0];
    ViewableImg[0]--;
    if (ViewableImg[0] < 0){
        ViewableImg[0] = count-1;
    }
    if(someOtherCount<=1){
        someOtherCount = count+1}

    displayViewImgreverse();

}

function moveRight()x{

    ViewableImg[0] = ViewableImg[1];
    ViewableImg[1] = ViewableImg[2];
    ViewableImg[2] = ViewableImg[3];
    ViewableImg[3] = ViewableImg[4];
    ViewableImg[4]++;
    if (ViewableImg[4] >= count){
        ViewableImg[4] = 0;
    }
    displayViewImg();
}




// preloading the images for the slide show
var preload = function(){
    for (var i=0; i< count; i++){
        image.src = images[i];
        images.push(image);}}

window.onload = function()
{
    preload();
    displayViewImg();

}
