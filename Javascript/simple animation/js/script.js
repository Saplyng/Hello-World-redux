$(document).ready(function () {
    $("#side-right").click(function () {
        var currentSlide = $(".carouselImgsLine").css("left"); /*goes thru css and returns the left property*/
        if (parseInt(currentSlide) < -6000) { /*use parseInt to make integers and not pixels*/
            $(".carouselImgsLine").css({
                left: 705
            }); /*the five is the extra for margin*/
        }
        $(".carouselImgsLine").animate({
            left: '-=705'
        }, 1000);
    });

    $("#side-left").click(function () {
        var currentSlide = $(".carouselImgsLine").css("left");
        if (parseInt(currentSlide) >= 0) {
            $(".carouselImgsLine").css({
                left: -7045
            });
        }
        $(".carouselImgsLine").animate({
            left: '+=705'
        }, 1000);
    });

});