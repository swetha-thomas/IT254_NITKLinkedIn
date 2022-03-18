var student = document.getElementById("student");
var organization = document.getElementById("organization");

function validateInput() {
    var email, regex, password;
    if(student!=null) {
        email = document.getElementById("email");
        regex = /^[a-z][a-z]+\.[0-9]{3}[a-z]{2}[0-9]{3}@nitk\.edu\.in$/;
        if(!regex.test(email.value)) {
            return false;
        }
    }
    else {
        email = document.getElementById("email");
        regex = /^[a-zA-Z0-9][a-zA-Z0-9\._\-]*@[a-zA-Z0-9\-\.]+\.[a-z]+$/
        if(!regex.test(email.value)) {
            return false;
        }        
    }
   
}
function signInButton()
{
        if(student)
        {
            console.log("hi")

            location.replace = '../templates/student_home.html';
        }
        else
        {
        console.log("hi")
            location.replace = '../templates/organization_home.html';
        }
    
}