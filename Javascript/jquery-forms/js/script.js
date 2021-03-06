 $(document).ready(function () {
     $("#myForm").submit(function (event) {
         isValidForm = true;
         var emailPattern = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}\b/;
         var phonePattern = /^\d{3}-\d{3}-\d{4}$/;
         var passwordPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})/;
         var zipPattern = /^\d{5}(?:[-\s]\d{4})?$/;


         var email = $("#emailAddress").val().trim();

         if (email === "") {
             $("#emailAddress").next().text("* Invalid");
             isValidForm = false;
         } else if (!emailPattern.test(email)) {
             $("#emailAddress").next().text("* Invalid");
             isValidForm = false;
         } else {
             // it is true, do something
         }



         var phoneNum = $("#phoneNumber").val().trim();

         if (phoneNum === "") {
             $("#phoneNumber").next().text("* Invalid");
             isValidForm = false;
         } else if (!phonePattern.test(phoneNum)) {
             $("#phoneNumber").next().text("* Invalid, please include \"-\"");
             isValidForm = false;
         } else {
             // it is true, do something
         }


         var zipcode = $("#zip").val().trim();

         if (zipcode === "") {
             $("#zip").next().text("* Invalid");
             isValidForm = false;
         } else if (!zipPattern.test(zipcode)) {
             $("#zip").next().text("* Invalid");
             isValidForm = false;
         } else {
             // it is true, do something
         }

         if (isValidForm == false) {
             event.preventDefault();
         }

     });


     $("#btnGetValue").click(function () {
         var selValue = $("input[name=rbg1]:checked").attr("value");

         $("p").html("<b> Selected radio button is: " + selValue + '<br>');
     });

     $("#chk1").change(function () {
         if (this.checked) {
             $(":radio").attr("disabled", true);
             $("#btnGetValue").attr("disabled", true);
         } else {
             $(":radio").attr("disabled", false);
             $("#btnGetValue").attr("disabled", false);
         }
     });


 });