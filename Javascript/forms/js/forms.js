// get id from html and use them
var $ = function (id) {
  "use strict"
    return document.getElementById(id);
}


var calculate_cost = function () {
  "use strict"
    // we have to parse - or change - the values to floats. Form values are strings by default.
    var firstname = parseFloat($("firstname").value);
    var lastname = parseFloat($("lastname").value);
    var alias = parseFloat($("alias").value);
    var superName = parseFloat($("superName").value);
    var villianName = parseFloat($("villianName").value);
    var power1 = parseFloat($("power1").value);
    var power2 = parseFloat($("power2").value);
    var power3 = parseFloat($("power3").value);
    //console.log(sidewidth2);

    if (firstname instanceof String || lastname instanceof String | alias instanceof String | superName instanceof Boolean | villianName instanceof Boolean | power1 instanceof String | power2 instanceof String | power3 instanceof String) {
        alert("You have an invalid value. Correct and click submit")
    }
    else {
        var total = "ah, a " + $("superName").value + " well then " + firstname + " or should I say" + alias + " welcome to the world of supers, I am sure that " + power2 + " will come in handy."; 
        $("paintingcost").value = total;
        console.log(total);
    }
}
window.onload = function () {
  "use strict"
    $("submit").onclick = calculate_cost;
    console.log(calculate_cost);
    
}