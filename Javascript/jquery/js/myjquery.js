$(document).ready(function(){
    //jQuery methods go here....

    $("#btn-Text").click(function(){
        $("#textExample").text($("#iText").text());
        //$("#iText").html



    });

    $("#btn-anchor").click(function(){
        $("#anchor1").attr("href","https://www.bing.com");
        $("#anchor1").text("Bing");



    });

    $("#img1").dblclick(function(){
        $("#img1").attr({
            "src": "https://via.placeholder.com/125x125?text=2",
            "alt": "ph2"
        });

    });

});
