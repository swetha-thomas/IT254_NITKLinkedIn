from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login as login_user
from django.views.decorators.csrf import csrf_protect

from organization.models import Organization
from student.models import Student
import re


# Create your views here.

@csrf_protect
def login(request):
  if request.method == 'POST':
    if request.POST.get('user_role') == 'student':
      # email = request.POST["email"]
      password = request.POST["password"]
      username = request.POST["username"]
      user = authenticate(username=username, password=password)
      if user is not None:
        login_user(request, user)
        print(Student.objects.filter(user=user))
        
        if Student.objects.filter(user=user).count() != 0:
          return redirect('studentHome')
        else:
          messages.info(request, "Student Doesnt Exist for this user")
          return redirect('login')
      else:
        messages.info(request, "Invalid Credentials")
        return redirect('login')
    else:
      # email = request.POST["email"]
      password = request.POST["password"]
      username = request.POST["username"]
      user = authenticate(username=username, password=password)
      if user is not None:
        login_user(request, user)
        print(Organization.objects.filter(user=user))
        
        if Organization.objects.filter(user=user).count() != 0:
          return redirect('organizationHome')
        else:
          messages.info(request, "Organization Doesnt Exist for this user")
          return redirect('login')
      else:
        messages.info(request, "Invalid Credentials")
        return redirect('login')
    
  return render(request, 'login_page.html')

def logout(request):
  # logout user and finish up all loose ends
  auth.logout(request)
  return redirect('login')

@csrf_protect
def register(request):
  if request.method == 'POST':
    if request.POST.get('register_type') == 'student':
      username = request.POST['username'].strip()
      fullName = request.POST["fullName"].strip().split(" ")
      email = request.POST["email"]
      password = request.POST["password"]
      conf_password = request.POST["conf_password"]
      
      if(re.search('^[a-z][a-z]+\.[0-9]{3}[a-z]{2}[0-9]{3}@nitk\.edu\.in$', email) is None):
        messages.info(request, "Email regex mismatch!!")
        return redirect('register')
      
      if(User.objects.filter(username=username).exists()):
        messages.info(request, "Please choose another username, it already exists")
        return redirect('register')
      elif User.objects.filter(email=email).exists():
        messages.info(request, "Email already has an account")
        return redirect('register')
      elif password != conf_password:
        messages.info(request, "Passwords do not match")
        return redirect('register')
      else:
        user = User.objects.create_user(username=username, first_name=fullName[0], email=email, password=password) 
        user.save()
        student = Student(user=user, first_name=fullName[0], last_name=fullName[-1]);
        student.save()
        messages.info("Successfully Registered!!")
        return redirect('login')
    else:
      username = request.POST['username'].strip()
      org_name = request.POST['fullName'].strip()
      email = request.POST['email']
      password = request.POST["password"].strip()
      conf_password = request.POST["conf_password"].strip()
      
      if User.objects.filter(email=email).exists():
        messages.info(request, "Email already has an account")
        return redirect('register')
      elif password != conf_password:
        messages.info(request, "Passwords do not match")
        return redirect('register')
      else:
        user = User.objects.create_user(username=username, first_name=org_name, email=email, password=password) 
        user.save()
        organization = Organization(user=user, org_name=org_name)
        organization.save()
        return redirect('login')
  return render(request, 'register_page.html')