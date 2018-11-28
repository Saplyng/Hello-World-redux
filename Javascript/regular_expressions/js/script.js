$(document).ready(function(){

    var nNum = 0;
    while(nNum <=50){
        nNum += 1;
        if (nNum % 2 == 0){
            continue;
        }
        $("#demo").append("<br>" + nNum);
    }





});