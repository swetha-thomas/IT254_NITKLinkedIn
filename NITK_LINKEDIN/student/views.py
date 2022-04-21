from django.shortcuts import render

# Create your views here.

def studentHome(request):
  return render(request, 'student_home.html')

def studentJobs(request):
  return render(request, 'student_jobs.html')

def studentProfile(request):
  return render(request, 'view_mystudent_profile.html')

def studentEditProfile(request):
  return render(request, 'edit_mystudent_profile.html')
