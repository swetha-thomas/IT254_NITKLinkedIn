from datetime import datetime, timedelta
from django.shortcuts import render, redirect
from job.models import Job
from student.models import Student, WorkExperience, Clubs, Skills, Education, Courses

from django.http import QueryDict

# Create your views here.

def studentHome(request):
  student = Student.objects.get(user=request.user)
  # print(student.profile_pic.url)
  return render(request, 'student_home.html', {
    'studentFirstName': student.first_name,
    'studentLastName': student.last_name,
    'studentProfilePic': student.profile_pic,
    'studentSem': student.semester,
    'studentSemSuffix': student.semesterSuffix,
    'studentCGPA': student.cgpa,
    'studentBranch': student.branch,
  })

def studentJob(request):
  form = dict(request.POST)
  
  student=Student.objects.get(user=request.user)
  job_level = form.get('job_level')
  company = form.get('company')
  job_type = form.get('job_type')
  onsite_remote = form.get('onsite_remote')
  date = form.get('date')
  
  filtered_jobs = set({})
  for job in Job.objects.all():
    if ((job_level is None or job.job_level in job_level) and (company is None or job.company.org_name in company) and (job_type is None or job.job_type in job_type) and (onsite_remote is None or job.onsite_remote in onsite_remote)
        and (date is None or check_date(job.posted_on, date))):
      filtered_jobs.add(job)
      
  print()
  print(filtered_jobs)
  # print(form)
  
  return render(request, "student_jobs.html", {'jobs' : filtered_jobs, 'first_name':student.first_name, 'last_name':student.last_name})

def studentProfile(request):
  student = Student.objects.get(user=request.user)
  exp = WorkExperience.objects.all().filter(user=request.user)
  clubs = Clubs.objects.all().filter(user=request.user)
  skills = Skills.objects.all().filter(user=request.user)
  education = Education.objects.all().filter(user=request.user)
  courses = Courses.objects.all().filter(user=request.user)
  return render(request, 'view_mystudent_profile.html', 
      {'first_name':student.first_name, 'last_name':student.last_name, 'gender':student.gender, 'dob':student.dob, 'roll_no':student.roll_no, 
      'branch': student.branch, 'semester':student.semester, 'cgpa': student.cgpa, 'contact_no': student.contact, 'yop': student.year_of_pass_out, 'desc': student.aboutme, 'exp':exp, 'clubs':clubs, 
      'skills':skills, 'edu':education, 'courses': courses})


def studentEditProfile(request):
  if request.method == 'POST':
    gender = request.POST["gender"]
    dob = request.POST["dob"]
    roll_no = request.POST["roll_no"]
    branch = request.POST["branch"] 
    semester = request.POST["semester"]
    cgpa = request.POST["cgpa"]
    contact_no = request.POST["contact"]
    yop = request.POST["yop"]
    aboutme = request.POST["aboutme"]

    Student.objects.filter(user=request.user).update(gender=gender, dob=dob, roll_no=roll_no, branch=branch, semester=semester, cgpa=cgpa, contact=contact_no, year_of_pass_out=yop, aboutme=aboutme)
    return redirect('studentProfile')
  
  elif request.method == 'GET':
    student = Student.objects.get(user=request.user)
    exp = WorkExperience.objects.all().filter(user=request.user)
    clubs = Clubs.objects.all().filter(user=request.user)
    skills = Skills.objects.all().filter(user=request.user)
    education = Education.objects.all().filter(user=request.user)
    courses = Courses.objects.all().filter(user=request.user)
    branch_list=["Chemical Engineering","Civil Engineering","Computer Science and Engineering","Electrical and Electronics Engineering","Electronics and Communication Engineering","Information Technology","Mechanical Engineering","Metallurgical and Materials Engineering","Mining Engineering"]
    if student.branch=='':
      branch_selected = ""
      branch_list.insert(0,branch_selected)
    else:
      branch_selected = student.branch
      ind = branch_list.index(branch_selected)
      branch_list.insert(0,branch_selected)
      branch_list.pop(ind+1)
    return render(request, 'edit_mystudent_profile.html', 
      {'first_name':student.first_name, 'last_name':student.last_name, 'gender':student.gender, 'dob':student.dob, 'roll_no':student.roll_no, 
      'branch': student.branch, 'semester':student.semester, 'cgpa': student.cgpa, 
      'contact_no': student.contact, 'yop':student.year_of_pass_out, 'desc':student.aboutme, 'branch_list':branch_list, 'exp':exp, 'clubs':clubs, 'skills':skills, 'edu':education, 'courses': courses})



def studentAddExp(request):
  if request.method == 'POST':
    role = request.POST["role"]
    company = request.POST["company"]
    location = request.POST["location"]
    employment_type = request.POST["employment"]
    start_date = request.POST["start"]
    end_date = request.POST["end"]
    work_exp = WorkExperience(user=request.user, role=role, company=company, location=location, employment_type=employment_type, start_date=start_date, end_date=end_date)
    work_exp.save()
    return redirect('studentEditProfile')

def studentAddClub(request):
  if request.method == 'POST':
    role = request.POST["role"]
    club_name = request.POST["club_name"]
    start_date = request.POST["start"]
    end_date = request.POST["end"]
    club = Clubs(user=request.user, role=role, club_name=club_name, start_date=start_date, end_date=end_date)
    club.save()
    return redirect('studentEditProfile')
  
def studentAddSkills(request):
  if request.method == 'POST':
    skill_desc = request.POST["skills"]
    skill_obj = Skills(user=request.user, skill=skill_desc)
    skill_obj.save()
    return redirect('studentEditProfile')

def studentAddEducation(request):
  if request.method == 'POST':
    institute = request.POST["institute"]
    degree = request.POST["degree"]
    start_date = request.POST["start"]
    end_date = request.POST["end"]
    edu = Education(user=request.user, institute=institute, degree=degree, start_date=start_date, end_date=end_date)
    edu.save()
    return redirect('studentEditProfile')

def studentAddCourses(request):
  if request.method == 'POST':
    course_name = request.POST["course_name"]
    org = request.POST["organization"]
    start_date = request.POST["start"]
    end_date = request.POST["end"]
    course = Courses(user=request.user, course_name=course_name, organization=org, start_date=start_date, end_date=end_date)
    course.save()
    return redirect('studentEditProfile')
  
# helper
def check_date(posted_on, date):
  if(date[0] == "Any Time"):
    return True
  
  curr_date = datetime.now().date()
  delta = curr_date - posted_on.replace(tzinfo=None).date()
  if(delta.days < int(date[0])):
    return True
  return False
