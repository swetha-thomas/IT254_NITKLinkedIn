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
    company_size_list=["0-1 employees","2-10 employees","11-50 employees","51-200 employees","201-500 employees","501-1000 employees","1001-5000 employees","5001-10000 employees","10001+ employees"]
    if org.company_size==None:
      company_size_selected = " --Please select an option --"
      company_size_list.insert(0,company_size_selected)
    else:
      company_size_selected = org.company_size
      ind = company_size_list.index(company_size_selected)
      company_size_list.insert(0,company_size_selected)
      company_size_list.pop(ind+1)
    
    company_type_list=["Educational","Government Agency","Non profit","Partnership","Privately held","Public Company","Self Employeed","Self Owned"]
    if org.company_type==None:
      company_type_selected = " --Please select an option --"
      company_type_list.insert(0,company_type_selected)
    else:
      company_type_selected = org.company_type
      ind = company_type_list.index(company_type_selected)
      company_type_list.insert(0,company_type_selected)
      company_type_list.pop(ind+1)

    return render(request, 'edit_myorg_profile.html', 
      {'orgName':org.org_name, 'industry':org.industry, 'company_size':org.company_size, 
      'company_type': org.company_type, 'locations':org.locations, 'web_url': org.website_url, 
      'contact_no': org.contact_no, 'desc':org.company_desc, 'size_list':company_size_list, 'type_list':company_type_list})

def organizationJobs(request):
  return render(request, 'organization_jobs.html')

def organizationProfile(request):
  org=Organization.objects.get(user=request.user)
  return render(request, 'view_myorg_profile.html', 
      {'orgName':org.org_name, 'industry':org.industry, 'company_size':org.company_size, 
      'company_type': org.company_type, 'locations':org.locations, 'web_url': org.website_url, 
      'contact_no': org.contact_no, 'desc':org.company_desc})

