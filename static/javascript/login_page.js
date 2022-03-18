var student = document.getElementById("student");
var organiser = document.getElementById("organizer");

student.addEventListener('click', function (params) {
    document.getElementById("email").pattern = "^[a-z][a-z]+\.[0-9]{3}[a-z]{2}[0-9]{3}@nitk\.edu\.in$";
});

organiser.addEventListener('click', function() {
    document.getElementById("eamil").pattern = "^[a-z][a-z]{2,}@[a-z]{3,}\.org";
})