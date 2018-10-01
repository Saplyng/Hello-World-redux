var $ = function (id) {
    return document.getElementById(id);
}

//declare vars and array

var images = ["http://via.placeholder.com/125x125?text=1","http://via.placeholder.com/125x125?text=2", "http://via.placeholder.com/125x125?text=3","http://via.placeholder.com/125x125?text=4", "http://via.placeholder.com/125x125?text=5"];
var titles = ["This is Image 1","This is Image 2", "This is Image 3", "This is Image 4", "This is Image 5"];
var captions = ["This is the caption of image 1.","This is the caption of image 2.","This is the caption of image 3.","This is the caption of image 4.","This is the caption of image 5."];

var image = new Image();// creates an image object
var count = images.length;// will change if we add more items to the image array
var someOtherCount = 0

var ViewableImg = [0,1,2];


function displayViewImg(){
    $("ViewImg1").src = images[ViewableImg[0]];
    $("ViewImg2").src = images[ViewableImg[1]];
    $("ViewImg3").src = images[ViewableImg[2]];
    $("large").src = images[ViewableImg[1]];
}

function moveLeft(){
    //TODO move all images left 1 spot
    ViewableImg[2] = ViewableImg[1];
    ViewableImg[1] = ViewableImg[0];
    ViewableImg[0]--;
    if (ViewableImg[0] <= count){
        // ViewableImg[0] = images[someOtherCount];
    }
    displayViewImg();
    someOtherCount--

}

function moveRight(){

    ViewableImg[0] = ViewableImg[1];
    ViewableImg[1] = ViewableImg[2];
    ViewableImg[2]++;
    if (ViewableImg[2] >= count){
        ViewableImg[2] = 0;
    }
    displayViewImg();
    someOtherCount++
}




// preloading the images for the slide show
var preload = function()
{
    for (var i=0; i< count; i++)
    {
        image.src = images[i];
        images.push(image);
    }
}

window.onload = function()
{
    preload();
    displayViewImg();

}
