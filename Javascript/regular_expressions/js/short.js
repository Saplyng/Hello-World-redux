$(document).ready(function(){

    var oddOrEven = function(xNum){
        return (xNum % 2 == 0) ? "even" : "odd";

    }



    function isItOddOrEven(){

        var nNum;
        nNum = parseInt($("#text1").val()) || 0;
        while(nNum <=50-1){
            nNum += 1;
            $("#demo").append("<br>" + nNum + ": " + oddOrEven(nNum));
        }
    }

    $("#startMe").click(function(){

        $("#demo").text("");
        isItOddOrEven();
    });


});