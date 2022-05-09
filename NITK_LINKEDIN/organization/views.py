from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Sum
from django.template.defaulttags import register

from datetime import date
import datetime as dt

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
    
    if len(Student.objects.all().filter(year_of_pass_out=date.today().year-i))==0:
      past_7_years[i]['avg_cgpa'] = 0.00
      past_7_years[i]['branches'] = ['']
      past_7_years[i]['marks'] = {'': 0.00}
      number_of_students_of_this_year = 0
      continue
    
    if i != 0:
      past_7_years[i]['branches'] = ['']
      past_7_years[i]['marks'] = {'': 0.00}
      students_of_this_year = Student.objects.all().filter(year_of_pass_out=date.today().year-i)
      branches_of_this_year = students_of_this_year.order_by().values('branch').distinct()
      number_of_students_of_this_year = students_of_this_year.count()
      past_7_years[i]['avg_cgpa'] = round(students_of_this_year.aggregate(Sum('cgpa'))['cgpa__sum'] / number_of_students_of_this_year, 2)
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
    'numOfStudentsInBatch': past_7_years[0]['num_students'],
    'numOfStudentsFromCollegeInOrg': organization.num_alumni,
    'avgCGPAOfStudents': past_7_years[0]['avg_cgpa'],
    'branches': past_7_years[0]['branches'],
    'marks': past_7_years[0]['marks'],
    'num_of_years': len(past_7_years),
    'past_years': past_7_years,
    'jobs_of_company': jobs_of_company,
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
    if org.company_size=='':
      company_size_selected = ""
      company_size_list.insert(0,company_size_selected)
    else:
      company_size_selected = org.company_size
      ind = company_size_list.index(company_size_selected)
      company_size_list.insert(0,company_size_selected)
      company_size_list.pop(ind+1)
    
    company_type_list=["Educational","Government Agency","Non profit","Partnership","Privately held","Public Company","Self Employeed","Self Owned"]
    if org.company_type=='':
      company_type_selected = ""
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
      posted_on = dt.datetime.now().replace(tzinfo=None)
    )
    job.save()
    # form = dict(request.POST)
    # print(form)
  organization=Organization.objects.get(user=request.user)
  jobs=Job.objects.all().filter(company=Organization.objects.get(user=request.user))
  return render(request, 'organization_jobs.html',{
    'jobs':jobs, 'role':'create', 
    'user':request.user,
    'orgName': organization.org_name,
    'organizationProfilePic': organization.profile_pic,
  })


def deleteJob(request, job_id):
  Job.objects.get(id=job_id).delete()
  return redirect('organizationJob')

def editJob(request, job_id):
  if request.method == 'POST':
    job_type = request.POST["job_type"]
    job_level = request.POST["job_level"]
    job_name = request.POST["job_name"]
    qualification = request.POST["qualification"] 
    onsite_remote = request.POST["onsite_remote"] 
    location_of_work = request.POST["location_of_work"]
    job_description = request.POST["job_description"]    
    Job.objects.filter(id=job_id).update(job_type=job_type, job_level=job_level, job_name=job_name, qualification=qualification, onsite_remote = onsite_remote, location_of_work=location_of_work, job_description=job_description)
    return redirect('organizationJob')

  job_obj = Job.objects.get(id=job_id)
  job_level_list=["Internship","Job","Freelance"]
  if job_obj.job_level=='':
    level_selected = ""
    job_level_list.insert(0,level_selected)
  else:
    level_selected = job_obj.job_level
    ind = job_level_list.index(level_selected)
    job_level_list.insert(0,level_selected)
    job_level_list.pop(ind+1)

  job_type_list=["Part-Time","Full-Time"]
  if job_obj.job_type=='':
    type_selected = ""
    job_type_list.insert(0,type_selected)
  else:
    type_selected = job_obj.job_type
    ind = job_type_list.index(type_selected)
    job_type_list.insert(0,type_selected)
    job_type_list.pop(ind+1)
  
  job_name_list=["Software Development Engineer (SDE)", "Digital Media & Content Strategist", "Business Analyst", "Product Manager"]
  if job_obj.job_name=='':
    name_selected = ""
    job_name_list.insert(0,name_selected)
  else:
    name_selected = job_obj.job_name
    ind = job_name_list.index(name_selected)
    job_name_list.insert(0,name_selected)
    job_name_list.pop(ind+1)

  onsite_remote_list=["On-Site","Remote"]
  if job_obj.onsite_remote=='':
    onsite_remote_selected = ""
    onsite_remote_list.insert(0,onsite_remote_selected)
  else:
    onsite_remote_selected = job_obj.onsite_remote
    ind = onsite_remote_list.index(onsite_remote_selected)
    onsite_remote_list.insert(0,onsite_remote_selected)
    onsite_remote_list.pop(ind+1)
  return render(request, 'organization_jobs.html', {'display_job':job_obj, 'jobs':Job.objects.all().filter(company=Organization.objects.get(user=request.user)), 'role':'edit', 'job_level_list':job_level_list, 'job_type_list':job_type_list, 'job_name_list':job_name_list, 'onsite_remote_list': onsite_remote_list})

def viewJob(request, job_id):
  return render(request, 'organization_jobs.html', {'display_job':Job.objects.get(id=job_id), 'jobs':Job.objects.all().filter(company=Organization.objects.get(user=request.user)), 'role':'view'})

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
  
@register.filter
def get_date_but_not_time(value):
  return str(value).strip().split(" ")[0]