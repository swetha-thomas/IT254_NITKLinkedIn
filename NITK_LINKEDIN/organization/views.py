import datetime
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.template.defaulttags import register

from datetime import date, datetime

from organization.models import Organization
from student.models import Student
from job.models import Job
# Create your views here.

def organizationHome(request):
  organization = Organization.objects.get(user=request.user)
  students = Student.objects.all()
  number_of_students = students.count()
  branchesDict = Student.objects.order_by().values('branch').distinct()
  branches = []
  for branch in branchesDict:
    branches.append(branch['branch'])
  
  past_7_years = {}
  for i in range(7):
    past_7_years[i] = {'year_number': date.today().year - i}
    
    if len(Student.objects.all().filter(year_of_pass_out=date.today().year-i))==0 or i != 0:
      past_7_years[i]['avg_cgpa'] = 0.00
      past_7_years[i]['branches'] = ['']
      past_7_years[i]['marks'] = {'': 0.00}
      number_of_students_of_this_year = 0
      continue
    
    students_of_this_year = Student.objects.all().filter(year_of_pass_out=date.today().year-i)
    branches_of_this_year = students_of_this_year.order_by().values('branch').distinct()
    number_of_students_of_this_year = students_of_this_year.count()
    avg_cgpa_of_students_of_this_year = round(students_of_this_year.aggregate(Sum('cgpa'))['cgpa__sum'] / number_of_students_of_this_year, 2)
    marks_of_this_year = {}
    for branch in branches_of_this_year:
      if branch['branch'] not in marks_of_this_year.keys():
        marks_of_this_year[branch['branch']] = 0
        number_of_students_of_this_branch_of_this_year = students_of_this_year.filter(branch=branch['branch']).count()
        marks_of_this_year[branch['branch']] += round(students_of_this_year.filter(branch=branch['branch']).aggregate(Sum('cgpa'))['cgpa__sum'] / number_of_students_of_this_branch_of_this_year, 2)
    
    past_7_years[i]['students'] = students_of_this_year
    past_7_years[i]['branches'] = branches_of_this_year
    past_7_years[i]['num_students'] = number_of_students_of_this_year
    past_7_years[i]['avg_cgpa'] = avg_cgpa_of_students_of_this_year
    past_7_years[i]['marks'] = marks_of_this_year
  
  # print(past_7_years, sep="\n", end="\n")
  
  jobs_of_company = Job.objects.filter(company=organization)
  
  print(jobs_of_company)
  
  return render(request, 'organization_home.html', {
    'orgName': organization.org_name,
    'organizationProfilePic': organization.profile_pic,
    'numOfStudentsInBatch': number_of_students_of_this_year,
    'numOfStudentsFromCollegeInOrg': organization.num_alumni,
    'avgCGPAOfStudents': past_7_years[0]['avg_cgpa'],
    'branches': past_7_years[0]['branches'],
    'marks': past_7_years[0]['marks'],
    'num_of_years': len(past_7_years),
    'past_years': past_7_years,
    
  })


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

    return render(request, 'edit_myorg_profile.html', {
      'orgName':org.org_name, 
      'industry':org.industry, 
      'company_size':org.company_size, 
      'company_type': org.company_type, 
      'locations':org.locations, 
      'web_url': org.website_url, 
      'contact_no': org.contact_no, 
      'desc':org.company_desc, 
      'size_list':company_size_list, 
      'type_list':company_type_list
    })

def organizationJob(request):
  if(request.method == 'POST'):
    
    job_level = request.POST['job_level']
    job_type = request.POST['job_type']
    job_name = request.POST['job_name'].strip()
    qualification = request.POST['qualification'].strip()
    onsite_remote = request.POST['onsite_remote']
    location = request.POST['location_of_work']
    job_description = request.POST['job_description']
    skills_required = request.POST['skills_required'].strip()
    
    job = Job.objects.create(
      job_name = job_name,
      company = Organization.objects.get(user=request.user),
      job_description = job_description,
      job_level = job_level,
      job_type = job_type,
      onsite_remote = onsite_remote,
      location_of_work = location,
      site_url = Organization.objects.get(user=request.user).website_url,
      qualification = qualification,
      skills_required = skills_required,
      posted_on = datetime.datetime.now().replace(tzinfo=None)
    )
    job.save()
    # form = dict(request.POST)
    # print(form)
  return render(request, 'organization_jobs.html')

def organizationProfile(request):
  org=Organization.objects.get(user=request.user)
  return render(request, 'view_myorg_profile.html', 
      {'orgName':org.org_name, 'industry':org.industry, 'company_size':org.company_size, 
      'company_type': org.company_type, 'locations':org.locations, 'web_url': org.website_url, 
      'contact_no': org.contact_no, 'desc':org.company_desc})

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
  
@register.filter
def div( value, arg ):
    try:
        value = int( value )
        arg = int( arg )
        if arg: return value / arg
    except: pass
    return ''