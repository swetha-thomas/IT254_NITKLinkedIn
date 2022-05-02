from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login as login_user

from organization.models import Organization
from student.models import Student


# Create your views here.
  
def login(request):
  if request.method == 'POST':
    if request.POST.get('user_role') == 'student':
      email = request.POST["email"]
      password = request.POST["password"]
      username = request.POST["username"]
      user = authenticate(username=username, email=email, password=password)
      if user is not None:
        login_user(request, user)
        print(Student.objects.filter(user=user))
        return redirect('studentHome')
      else:
        messages.info(request, "Invalid Credentials")
        return redirect('login')
    else:
      print("regex doesnt match")
    
  return render(request, 'login_page.html')

def logout(request):
  # logout user and finish up all loose ends
  auth.logout(request)
  return redirect('login')

def register(request):
  if request.method == 'POST':
    if request.POST.get('register_type') == 'student':
      username = request.POST['username'].strip().lower()
      fullName = request.POST["fullName"].strip().split(" ")
      email = request.POST["email"]
      password = request.POST["password"]
      conf_password = request.POST["conf_password"]
      
      if User.objects.filter(email=email).exists():
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
        return redirect('login')
    else:
      username = request.POST['username'].strip().lower()
      org_name = request.POST['org_name'].strip()
      email = request.POST['email']
      
      if User.objects.filter(email=email).exists():
        messages.info(request, "Email already has an account")
        return redirect('register')
      elif password != conf_password:
        messages.info(request, "Passwords do not match")
        return redirect('register')
      else:
        user = User.objects.create_user(username=username, first_name=org_name, email=email, password=password) 
        user.save()
        organization = Organization(user=user, org_name=org_name);
        organization.save()
        return redirect('login')
  return render(request, 'register_page.html')