from django.shortcuts import render
from job.models import Job

# Create your views here.

def studentJob(request):
    return render(request, "student_jobs.html", {'jobs' : Job.objects.all()})