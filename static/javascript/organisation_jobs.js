
const targetDiv = document.getElementById("left-side");
const createBtn = document.getElementById("create-new-job-btn");
const saveBtn = document.getElementById("savebtn");

createBtn.addEventListener('click', function() {
    targetDiv.style.display = "block";
});
saveBtn.addEventListener('click', function() {
        
    var ul = document.getElementById("list-of-saved-jobs");
    var li = document.createElement("li");
    li.setAttribute("class", "job");
    var image = document.createElement("img");
    image.src = "../static/img/job-company-1.jpg";
    image.classList.add("company-logo-img");
    image.alt = "compant logo";
    li.appendChild(image);

    var jobDescDiv = document.createElement("div")
    jobDescDiv.classList.add("job-title-company-location");
    var jobTitle = document.createElement("h5");
    jobTitle.classList.add("job-title")
    jobTitle.textContent = "Graphic Designer";
    jobDescDiv.appendChild(jobTitle);
    var jobCompany = document.createElement('p');
    jobCompany.classList.add("job-company");
    jobCompany.textContent = "Amazon Web Services";
    jobDescDiv.appendChild(jobCompany);
    var jobAdd = document.createElement('p');
    jobAdd.classList.add("job-address");
    jobAdd.textContent = "Bengaluru, India";
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
});
