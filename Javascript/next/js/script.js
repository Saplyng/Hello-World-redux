$(document).ready(function(){

    "use strict";
    var nextSlide = $("#slides img:first-child");
    var nextCaption;
    var nextSlideSource;


    var runSlideShow = function(){
        $("#caption").fadeOut("slow");
        $("#slide").fadeOut("slow", function(){
            if(nextSlide.next().length === 0){
                nextSlide = $("#slides img:first-child");
            } else{
                nextSlide = nextSlide.next();
            }

            nextSlideSource = /*"../" + */ nextSlide.attr("src"); //if images dont come up, use that
            nextCaption = nextSlide.attr("alt");

            $("#slide").attr("src", nextSlideSource).fadeIn("slow");
            $("#caption").text(nextCaption).fadeIn("slow");

        });
    };

    var timer1 = setInterval(runSlideShow, 5000);

    $("#slide").hover(function(){

        if(timer1 !== null){
            clearInterval(timer1);
            timer1 = null;
        } else{
            timer1 = setInterval(runSlideShow, 4000);
        }
    });



});
