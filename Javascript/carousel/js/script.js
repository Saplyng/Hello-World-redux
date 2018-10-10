$(document).ready(function(){

    "use strict";
    var nextSlide = $("#slides img:first-child");
    var nextCaption;
    var nextSlideSource;




    $("#side-right").click(function(){
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
    });



    $("#side-left").click(function(){
        $("#caption").fadeOut("slow");
        $("#slide").fadeOut("slow", function(){
            if(nextSlide.prev().length === 0){
                nextSlide = $("#slides img:last-child");
            } else{
                nextSlide = nextSlide.prev();
            }

            nextSlideSource = /*"../" + */ nextSlide.attr("src"); //if images dont come up, use that
            nextCaption = nextSlide.attr("alt");

            $("#slide").attr("src", nextSlideSource).fadeIn("slow");
            $("#caption").text(nextCaption).fadeIn("slow");

        });
    });

});
