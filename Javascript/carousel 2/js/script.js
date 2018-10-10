$(document).ready(function(){
    $("#side-right").click(function(){

        var currentSlide = $(".longLineOfImg").css("left");
        if( parseInt(currentSlide) < -1600){
            $(".longLineOfImg").css({left: 405});
        }
            $(".longLineOfImg").animate( {left: '-=405'}, 1000);




    });

    $("#side-left").click(function(){

        var currentSlide = $(".longLineOfImg").css("left");
        if( parseInt(currentSlide) >= 0){
            $(".longLineOfImg").css({left: -2023});
        }

        $(".longLineOfImg").animate( {left: '+=405'}, 1000);

    });

});
