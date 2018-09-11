var $ = function(id){
  return document.getElementById(id);
}

function displayInfo(){

  var name = $("first_name").value;
  if(!(name === "")){
    // var name = document.getElementById("first_name").value

    var nameLength = name.length;
    var index = name.indexOf(" ");
    var firstName = name.substr(0, index);
    $("f_name").innerHTML = firstName;

    //change to dollar figure
    var sales = $("sales_amount").value;
    sales = parseFloat(sales).toFixed(2);
    $("s_amt").innerHTML = sales;

    //objects
    var today = new Date;
    $("demo").innerHTML = today.toDateString();

    //use strict;
}else{
    alert("Please enter a name");
    console.log("User did not enter a name")
}




}
