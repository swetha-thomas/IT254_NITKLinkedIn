function job_desc(id) {
    console.log(id);
    let all_col = document.getElementsByClassName("job-desc-container")
        // console.log(all_col);

    for (let i of all_col) {
        console.log(i);
        i.style.display = "none";
    }
    let job_desc_col = document.getElementById(`job-${id}`);
    job_desc_col.style.display = "block";
}