from django.shortcuts import render

# Create your views here.

def organizationHome(request):
  return render(request, 'organization_home.html')

def organizationJobs(request):
  return render(request, 'organization_jobs.html')