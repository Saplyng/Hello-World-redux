// quick getelementbyid
var $ = function(id){
    return document.getElementById(id);
}

//declare and initialize array

    var game = ["BATMAN","WONDER WOMAN","SPIDERMAN","RORSCHACH"]
    var choice = Math.floor(Math.random()*4);
    var answer = game[choice];
    var myLength = answer.length;
    var display = [myLength];
    var win = myLength;
    var letters = answer.split('');
    var attemptsLeft = myLength * 2;
    var output = "";
    var userLetter = "";


var setup = function(){
    for (var i in answer.length){
        display[i] = "_ ";
        output = output + display[i];
    }
    $("game").innerHTML = output;
    output = "";
}



var submit = function(){

    output = "";
    userLetter = $("letter").nodeValue;
    $("letter").value = "";

    for(var c in answer.length){
        alert(letters[c]);
        if(userLetter.toUpperCase() == letters[c]){
            display[c] = userLetter.toUpperCase();
            win--;
        }
        output = output + display[c] + " ";
    }
    document.getElementById("game").innerHTML = output;
    output = "";
    attemptsLeft--;

    if (win < 1){
        document.getElementById("guesses").innerHTML = "YOU WIN!!!";
    }
    else if (attemptsLeft < 1){
        document.getElementById("guesses").innerHTML = "YOU LOSE!!!";
    }
    else {
        document.getElementById("guesses").innerHTML = "You have " + attemptsLeft + " guesses left";
    }
}



window.onload = function(){
    setup();
}