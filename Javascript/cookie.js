$(document).ready(function(){
    var setCookie = function(name, value, days){
        var cookie = name + "=" + encodeURIComponent(value);
        if(days != undefined){
            cookie += "; max-age=" + days * 24 * 60 * 60;
        }
        cookie += "; path=/";
    };

    var deleteCookie = function(name){
        document.cookie = name + "= ''; max-age=0; path=/";
    };

    var getCookieByName = function(name){
        var cookies = document.cookie;

        var start = cookies.indexOf(name + "=");

        if(start === -1){return "";}
        else{
            start = start + (name.length + 1);
            var end = cookies.indexOf(";", start);
            if (end === -1){end = cookie.length;}

            var cookieValue = cookies.substr(start, end);
            return decodeURIComponent(cookieValue);
        }
    };

    function DoSomething(){
        setCookie("username","John Smith",30);
        setCookie("job", "Programmer", 30);

        localStorage.setItem("email", "hunter2@gmail.com");
        localStorage.email = "hunter2@gmail.com"

        var email = localStorage.email;
        var email = localStorage.getItem("email");

        localStorage.removeItem("email");
        localStorage.clear(); //clears everything

        sessionStorage // the same thing as localstorage but for one session
    };


});