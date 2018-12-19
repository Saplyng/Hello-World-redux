var $ = function (id) {
    return document.getElementById(id);
};

//get today's day
function greeting() {
    var today = moment();
    var days = ["Weekend", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Weekend"];
    $("idGreeting").innerHTML = "Happy " + days[today.day()] + "!";
}

// Christmas countdown
function countdowndeath() {
    //get Christmas date
    var countDownDate = moment("2018-12-13 23:59:59");

    // Update the count down every 1 second
    var x = setInterval(function () {

        // Get todays date and time
        var now = moment();
        var lenOfTime = countDownDate - now;

        $("idDeadline").innerHTML = "<h2><em><b>" + moment(lenOfTime).subtract(6, "hour").format("hh:mm:ss")
        

        // If the count down is over
        if (lenOfTime < 0) {
            clearInterval(x);
            $("idDeadline").innerHTML = "EXPIRED";
        }
    }, 1000);

}

function apocalypse() {
    // world ended = december,21,2012
    var doomsday = moment("20121221", "YYYYMMDD").fromNow();

    $("idDoom").innerHTML = doomsday;
}

window.onload = function () {
    greeting();
    countdowndeath();
    apocalypse();
}