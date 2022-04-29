from django.shortcuts import render

from student.models import Student

# Create your views here.

def studentHome(request):
  student = Student.objects.get(user=request.user)
  return render(request, 'student_home.html', {
    'studentName': student.username,
    'studentProfilePic': student.profile_pic,
  })

def studentJobs(request):
  return render(request, 'student_jobs.html')

def studentProfile(request):
  return render(request, 'view_mystudent_profile.html')

def studentEditProfile(request):
  return render(request, 'edit_mystudent_profile.html')
