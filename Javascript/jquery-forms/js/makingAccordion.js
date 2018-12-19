var accord = document.getElementsByClassName("accordion");
var icounter = 0;

for (icounter = 0; icounter < accord.length; icounter++){
  accord[icounter].addEventListener("click", function(){
    this.classList.toggle("active");

    var panel = this.nextElementSibling;
    if(panel.style.display == "block"){
      panel.style.display = "none";
    }else {
      panel.style.display = "block";
    }

  });
}
