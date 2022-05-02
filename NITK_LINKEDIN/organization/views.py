from django.shortcuts import render, redirect

from organization.models import Organization

# Create your views here.

def organizationHome(request):
  organization = Organization.objects.get(user=request.user)
  return render(request, 'organization_home.html', {'orgName':organization.org_name})

def organizationEditProfile(request):
  if request.method == 'POST':
    industry = request.POST["industry"]
    company_size = request.POST["company_size"]
    company_type = request.POST["company_type"]
    locations = request.POST["location"] 
    website_url = request.POST["web_url"]
    contact_no = request.POST["contact"]
    desc = request.POST["aboutme"]
    Organization.objects.filter(user=request.user).update(industry=industry, company_size=company_size, company_type=company_type, locations=locations, website_url=website_url, contact_no=contact_no, company_desc=desc)
    return redirect('organizationProfile')
  
  elif request.method == 'GET':
    org=Organization.objects.get(user=request.user)
    return render(request, 'edit_myorg_profile.html', 
      {'orgName':org.org_name, 'industry':org.industry, 'company_size':org.company_size, 
      'company_type': org.company_type, 'locations':org.locations, 'web_url': org.website_url, 
      'contact_no': org.contact_no, 'desc':org.company_desc})

def organizationJobs(request):
  return render(request, 'organization_jobs.html')

def organizationProfile(request):
  org=Organization.objects.get(user=request.user)
  return render(request, 'view_myorg_profile.html', 
      {'orgName':org.org_name, 'industry':org.industry, 'company_size':org.company_size, 
      'company_type': org.company_type, 'locations':org.locations, 'web_url': org.website_url, 
      'contact_no': org.contact_no, 'desc':org.company_desc})

