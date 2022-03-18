var student = document.getElementById("flexRadioDefault1");
var organiser = document.getElementById("flexRadioDefault2");


// student.addEventListener('click', function (params) {
//     document.getElementById("exampleInputEmail1").pattern = "^[a-z][a-z]+\.[0-9]{3}[a-z]{2}[0-9]{3}@nitk\.edu\.in$";
// });

// organiser.addEventListener('click', function() {
//     document.getElementById("exampleInputEmail1").pattern = "^[a-z][a-z]{2,}@[a-z]{3,}\.org";
// })

function validateInput() {
    var email, regex, password;
    if(student.checked == "true") {
        email = document.getElementById("exampleInputEmail1");
        regex = /^[a-z][a-z]+\.\d{3}[a-z]{2}\d{3}@nitk\.edu\.in$/;
        if(!regex.test(email.value)) {
            return false;
        }
    }
    else {
        email = document.getElementById("exampleInputEmail1");
        regex = /^[a-z][a-z]{2,}@[a-z]{3,}\.org/
        if(!regex.test(email.value)) {
            return false;
        }        
    }
    password = document.getElementById("exampleInputPassword1");
    // regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#\$%\^&\*])(?=.{8,20})/
    // regex = /^(?=.*\d)(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,16}$/;
    regex = /^[a-z][a-z]+\.\d{3}[a-z]{2}\d{3}@nitk\.edu\.in$/;
    if(!regex.test(password.value)) {
        return false;
    }
    return true;
}
var signinBtn = document.getElementById("signin");
signinBtn.addEventListener('click', () => {
    if(validateInput()) {
        if(student.checked)
            signinBtn.onclick = "location.href = 'www.youtube.com';";
        else
            signinBtn.onclick = "organization_home.html";
    }
})