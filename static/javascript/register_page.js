var role_student = document.querySelector("#flexRadioDefault1");
var role_organiser = document.querySelector("#flexRadioDefault2");

var username = document.getElementById("fullName");
var email = document.getElementById("exampleInputEmail1");

role_organiser.addEventListener("click", displayOrganiserFields);
role_student.addEventListener("click", displayStudentFields);

function displayOrganiserFields(params) {
    username.placeholder = "Name of your organisation";

    email.placeholder = "your_name@company.org";
    email.pattern = "^[a-z][a-z]{2,}@[a-z]{3,}\.org";
}

function displayStudentFields(params) {
    
    username.placeholder = "FirstName LastName";
    username.pattern = "^[A-Z][a-z]* [A-Z][a-z]*{2,30}$";

    email.pattern = "^[a-z][a-z]+\.[0-9]{3}[a-z]{2}[0-9]{3}@nitk\.edu\.in$";
}

function validate(params) {
    var regex_name = /^[A-Z][a-z]* [A-Z][a-z]*{2,30}$/
    if(!regex_name.test(username.value)) {
        return false;
    }

    var regex_email;
    if (role_student.checked) {
        regex_email = /^[a-z][a-z]+\.[0-9]{3}[a-z]{2}[0-9]{3}@nitk\.edu\.in$/;
    } else {
        regex_email = /^[a-z][a-z]{2,}@[a-z]{3,}\.org/;
    }
    if(!regex_email.test(email.value)) {
        return false;
    }

    var regex_password = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,20})/;
    var password = document.getElementById("exampleInputPassword1");
    if(!regex_password.test(password.value)) {
        return false;
    }

    var confirmPassword = document.getElementById("exampleInputPassword2");
    if(confirmPassword.value != password.value) {
        return false;
    }
    return true;
    
}