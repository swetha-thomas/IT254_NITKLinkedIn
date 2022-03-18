const targetDiv = document.getElementById("left-side");
const createBtn = document.getElementById("create-new-job-btn");
const saveBtn = document.getElementById("savebtn");

function validateForm(params) {
  // document.querySelector(".form-horizontal .form-control").childNodes[0].
}
createBtn.addEventListener("click", function () {
  targetDiv.style.display = "block";
});

function validateForm(params) {
  var ddl = document.querySelector("#job-type");
  var selectedValue = ddl.options[ddl.selectedIndex].value;
  if (selectedValue == "Job Type") {
    return false;
  }
  var jobRole = document.getElementById("exampleDataList");
  if (jobRole.value == "") {
    return false;
  }
  var qualification = document.getElementById("qualification");
  if (qualification.value == "") {
    return false;
  }
  var jobDescription = document.getElementById("job-desc");
  if (jobDescription.value == "") {
    return false;
  }
  var skills = document.getElementById("skills-required");
  if (skills.value == "") {
    return false;
  }
  var location = document.getElementById("location");
  if (location.value == "") {
    return false;
  }
  return true;
}
let postBtn = document.getElementById("postbtn");
postBtn.addEventListener("click", (event) => {
  if (validateForm()) {
    document.getElementById("invalid-input").innerHTML = "";
    var ddl = document.querySelector("#job-type");
    var selectedValue = ddl.options[ddl.selectedIndex].value;
    var jobRole = document.getElementById("exampleDataList").value;
    var qualification = document.getElementById("qualification").value;
    var location = document.getElementById("location").value;
    var jobDescription = document.getElementById("job-desc").value;
    var skills = document.getElementById("skills-required").value;

    var ul = document.getElementById("list-of-posted-jobs");
    var li = document.createElement("li");
    li.setAttribute("class", "job");
    var image = document.createElement("img");
    image.src = "../static/img/job-company-1.jpg";
    image.classList.add("company-logo-img");
    image.alt = "company logo";
    li.appendChild(image);

    var jobDescDiv = document.createElement("div");
    jobDescDiv.classList.add("job-title-company-location");
    var jobTitle = document.createElement("h5");
    jobTitle.classList.add("job-title");
    jobTitle.textContent = jobRole;
    jobDescDiv.appendChild(jobTitle);
    var jobCompany = document.createElement("p");
    jobCompany.classList.add("job-company");
    jobCompany.textContent = "Amazon Web Services";
    jobDescDiv.appendChild(jobCompany);
    var jobAdd = document.createElement("p");
    jobAdd.classList.add("job-address");
    jobAdd.textContent = location;
    jobDescDiv.appendChild(jobAdd);
    li.appendChild(jobDescDiv);
    // jobDescDiv.append(jobTitle, jobCompany, jobAdd);

    // var editBtnDiv = document.createElement('div');
    // editBtnDiv.classList.add("job-button-group");
    // for(let j=0; j<3; j++) {
    //     var editBtn = document.createElement('button');
    //     editBtn.type = "button";

    //     editBtn.id = j.toString();
    //     // editBtn.onclick("delete_row(this.id)")
    //     editBtn.style.fontSize = "17px";
    //     editBtn.classList.add("btn btn-outline-danger border-0");
    //     editBtn.dataset.toggle = "modal";
    //     editBtn.dataset.target = "#exampleModalCenter";
    //     var icon = document.createElement('i');
    //     icon.classList.add("fa fa-pencil");
    //     editBtn.textContent = "djfasdk";
    //     editBtnDiv.appendChild(editBtn);

    // }
    // li.appendChild(editBtnDiv);
    // li.append(image, jobDescDiv, editBtnDiv);

    ul.appendChild(li);
  } else {
    document.getElementById("invalid-input").innerHTML = "";
    document.getElementById("invalid-input").style.color = "red";
  }
});

saveBtn.addEventListener("click", function () {
  if (validateForm()) {
    document.getElementById("invalid-input").innerHTML = "Invalid Input";
    var ddl = document.querySelector("#job-type");
    var selectedValue = ddl.options[ddl.selectedIndex].value;
    var jobRole = document.getElementById("exampleDataList").value;
    var qualification = document.getElementById("qualification").value;
    var location = document.getElementById("location").value;
    var jobDescription = document.getElementById("job-desc").value;
    var skills = document.getElementById("skills-required").value;

    var ul = document.getElementById("list-of-saved-jobs");
    var li = document.createElement("li");
    li.setAttribute("class", "job");
    var image = document.createElement("img");
    image.src = "../static/img/job-company-1.jpg";
    image.classList.add("company-logo-img");
    image.alt = "compant logo";
    li.appendChild(image);

    var jobDescDiv = document.createElement("div");
    jobDescDiv.classList.add("job-title-company-location");
    var jobTitle = document.createElement("h5");
    jobTitle.classList.add("job-title");
    jobTitle.textContent = jobRole;
    jobDescDiv.appendChild(jobTitle);
    var jobCompany = document.createElement("p");
    jobCompany.classList.add("job-company");
    jobCompany.textContent = "Amazon Web Services";
    jobDescDiv.appendChild(jobCompany);
    var jobAdd = document.createElement("p");
    jobAdd.classList.add("job-address");
    jobAdd.textContent = location;
    jobDescDiv.appendChild(jobAdd);
    li.appendChild(jobDescDiv);
    // jobDescDiv.append(jobTitle, jobCompany, jobAdd);

    // var editBtnDiv = document.createElement('div');
    // editBtnDiv.classList.add("job-button-group");
    // for(let j=0; j<3; j++) {
    //     var editBtn = document.createElement('button');
    //     editBtn.type = "button";

    //     editBtn.id = j.toString();
    //     // editBtn.onclick("delete_row(this.id)")
    //     editBtn.style.fontSize = "17px";
    //     editBtn.classList.add("btn btn-outline-danger border-0");
    //     editBtn.dataset.toggle = "modal";
    //     editBtn.dataset.target = "#exampleModalCenter";
    //     var icon = document.createElement('i');
    //     icon.classList.add("fa fa-pencil");
    //     editBtn.textContent = "djfasdk";
    //     editBtnDiv.appendChild(editBtn);

    // }
    // li.appendChild(editBtnDiv);
    // li.append(image, jobDescDiv, editBtnDiv);

    ul.appendChild(li);
  } else {
    document.getElementById("invalid-input").innerHTML = "Invalid Input";
    document.getElementById("invalid-input").style.color = "red";
  }
});

let deleteBtn = document.querySelectorAll(".delete");
for (let i = 0; i < deleteBtn.length; i++) {
  document.querySelectorAll(".delete")[i].addEventListener("click", (event) => {
    event.preventDefault();
    document.querySelectorAll(".job")[i].remove();
  });
}

let editBtn = document.querySelectorAll(".pencil");
for (let i = 0; i < editBtn.length; i++) {
  document.querySelectorAll(".pencil")[i].addEventListener("click", (event) => {
    event.preventDefault();
    document.getElementById("left-side").style.display = "block";
  });
}

let viewBtn = document.querySelectorAll(".right-side a");
for (let i = 0; i < viewBtn.length; i++) {
  document
    .querySelectorAll(".right-side a")
    [i].addEventListener("click", (event) => {
      event.preventDefault();
      document.getElementById("left-side").style.display = "block";
    });
}
