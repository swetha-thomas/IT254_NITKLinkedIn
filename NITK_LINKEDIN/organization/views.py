from django.shortcuts import render

# Create your views here.

def organizationHome(request):
  return render(request, 'organization_home.html')

def organizationJobs(request):
  return render(request, 'organization_jobs.html')

def organizationProfile(request):
  return render(request, 'view_myorg_profile.html')

def organizationEditProfile(request):
  return render(request, 'edit_myorg_profile.html')