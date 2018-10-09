$( function() {
    "use strict";
    $(".box1").hide();
    $('.box2').hide();

    $( ".button" ).click( function() {
        "use strict";
        $('.box2').hide()

      $( ".box1" ).animate({height: "toggle"}, 300);
    });

    $(".button2").click(function(){
            "use strict"
            $(".box1").hide();
            $(".box2").hide();

            $(".box2").animate({//height: "toggle",
                                deg: 360},
                {duration: 1200,
                step: function(now){
                // You are using jquery to set the left position of the element to the value passed as argument. It is the step function for jquery.animate() .
                // The function will be called for each step of the animation. step Type: Function( Number now, PlainObject fx ) A function to be called after
                // each step of the animation.
                $(".box2").css({ transform: 'rotate(' + now + 'deg)' });


                }


            })





        });
      });
