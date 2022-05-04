from django.shortcuts import render
from job.models import Job
from student.models import Student
from django.http import QueryDict

# Create your views here.

def studentHome(request):
  student = Student.objects.get(user=request.user)
  return render(request, 'student_home.html', {
    'studentName': student.username,
    'studentProfilePic': student.profile_pic,
    'studentSem': student.semester,
    'studentSemSuffix': student.semesterSuffix,
    'studentCGPA': student.cgpa,
    'studentBranch': student.branch,
  })

def studentJob(request):
  
  form = dict(request.POST)
  # print(form)
  
  experience_level = form.get('experience_level')
  company = form.get('company')
  # print(company)
  job_type = form.get('job_type')
  onsite_remote = form.get('onsite_remote')
  
  filtered_jobs = set({})
  for job in Job.objects.all():
    # print(job.job_type)
    # print(job.company)
    # print(job.job_level)
    # print()
    # print()
    
    # onsite_remote has to be added to models.py of job because currently its is just location_of_work, so cannot match with that
    if ((experience_level is None or job.job_level in experience_level) and (company is None or job.company in company) and (job_type is None or job.job_type in job_type) and (onsite_remote is None or job.onsite_remote in onsite_remote)):
      # print(job)
      # print(job.company)
      filtered_jobs.add(job)
  print()
  print(filtered_jobs)
  
  return render(request, "student_jobs.html", {'jobs' : filtered_jobs})
# {'filtered_jobs': filtered_jobs}

def studentProfile(request):
  return render(request, 'view_mystudent_profile.html')

def studentEditProfile(request):
  return render(request, 'edit_mystudent_profile.html')
