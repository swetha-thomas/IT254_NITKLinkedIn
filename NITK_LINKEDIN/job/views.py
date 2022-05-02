from django.shortcuts import render
from job.models import Job

# Create your views here.

def studentJobs(request):
    print(Job.objects.all())
    return render(request, {'jobs' : Job.objects.all()})