// get id from html and use them
var $ = function (id) {
  "use strict"
    return document.getElementById(id);
}


var calculate_cost = function () {
  "use strict"
    // we have to parse - or change - the values to floats. Form values are strings by default.
    var length = parseFloat($("frontlength").value);
    var width = parseFloat($("frontwidth").value);
    var backlength = parseFloat($("backlength").value);
    var backwidth = parseFloat($("backwidth").value);
    var sidelength = parseFloat($("sidelength").value);
    var sidewidth = parseFloat($("sidewidth").value);
    var sidelength2 = parseFloat($("sidelength2").value);
    var sidewidth2 = parseFloat($("sidewidth2").value);
    console.log(sidewidth2);

    if (isNaN(length) || isNaN(width) | isNaN(backlength) | isNaN(backwidth) | isNaN(sidelength) | isNaN(sidewidth) | isNaN(sidelength2) | isNaN(sidewidth2)){
        alert("You have an invalid value. Correct and click submit")
    }
    else {
        var total = ((length * width) + (backlength * backwidth) + (sidelength * sidewidth) + (sidelength2 * sidewidth2));//50 cents per square foot
        total = total.toFixed(2);
        $("paintingcost").value = "$ " + total;
        console.log(total);
    }
}
window.onload = function () {
  "use strict"
    $("submit").onclick = calculate_cost;
    console.log(calculate_cost);
    
}