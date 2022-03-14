var student = document.getElementById("flexRadioDefault1");
var organiser = document.getElementById("flexRadioDefault2");

student.addEventListener('click', function (params) {
    document.getElementById("exampleInputEmail1").pattern = "^[a-z][a-z]+\.[0-9]{3}[a-z]{2}[0-9]{3}@nitk\.edu\.in$";
});

organiser.addEventListener('click', function() {
    document.getElementById("exampleInputEmail1").pattern = "^[a-z][a-z]{2,}@[a-z]{3,}\.org";
})