var role_student = document.getElementById("student");
var role_organiser = document.getElementById("organiser");

var full_name = document.getElementById("fullName");
var email = document.getElementById("email");
var username = document.getElementById("username");

role_organiser.addEventListener("click", displayOrganiserFields);
role_student.addEventListener("click", displayStudentFields);

function displayOrganiserFields() {
    // username_div[0].style.display = "none";
    username.placeholder = "username";
    full_name.placeholder = "Name of organisation";
    email.placeholder = "";
}

function displayStudentFields() {
    // username_div[0].style.display = "block";

    username.placeholder = "username";
    full_name.placeholder = "FirstName LastName";
    email.placeholder = "your_name.roll_no@nitk.edu.in";
}

// function validate() {
//     var regex_name = /^[A-Z][a-z]* [A-Z][a-z]*$/
//     if(!regex_name.test(full_name.value)) {
//         return false;
//     }

//     var regex_email;
//     if (role_student.checked) {
//         regex_email = /^[a-z][a-z]+\.[0-9]{3}[a-z]{2}[0-9]{3}@nitk\.edu\.in$/;
//     } else {
//         regex_email = /^[a-zA-Z0-9][a-zA-Z0-9\._\-]*@[a-zA-Z0-9\-\.]+\.[a-z]+$/;
//     }
//     if(!regex_email.test(email.value)) {
//         return false;
//     }

//     var regex_password = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,20})/;
//     var password = document.getElementById("password");
//     if(!regex_password.test(password.value)) {
//         return false;
//     }

//     var confirmPassword = document.getElementById("conf_password");
//     if(confirmPassword.value != password.value) {
//         return false;
//     }
//     return true;

// }