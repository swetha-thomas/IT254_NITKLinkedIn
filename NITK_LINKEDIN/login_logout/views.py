from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_user
from django import forms

# from .models import CustomUser
# from student.models import Student

temp_name = ""


# Create your views here.
# def check_login_regex(user, email, password, username):
#   # organisation email regex no need
  
#   if(user== 'student'):
#     if(re.search("^[a-z][a-z]+\.[0-9]{3}[a-z]{2}[0-9]{3}@nitk\.edu\.in$", email) is None):
#       print("email regex does not match")
#       return False
    
#   # password and username regex check is same for org and student
#   if(re.search("^[a-zA-Z]([_-](?![_-])|[a-zA-Z0-9]){3,18}[a-zA-Z0-9]$", username) is None):
#     print("username regex doesnot match")
#     return False
  
#   if(re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,20})", password) is None):
#       print("password regex doesnt match")
#       return False
  
#   return True
  
def login(request):
  if request.method == 'POST':
    if request.POST.get('flexRadioDefault') == 'student':
      email = request.POST["email"]
      password = request.POST["password"]
      user = authenticate(username=temp_name, email=email, password=password)
      if user is not None:
        login_user(request, user)
        return redirect('studentHome')
      else:
        messages.info(request, "Invalid Credentials")
        return redirect('login')
    else:
      print("regex doesnt match")
    
  return render(request, 'login_page.html')

def logout(request):
  # logout user and finish up all loose ends
  return redirect('login')

def register(request):
  if request.method == 'POST':
    if request.POST.get('register_type') == 'student':
      username = request.POST['username'].strip().lower()
      fullName = request.POST["fullName"].strip()
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
        temp_name = fullName
        user = User.objects.create_user(username=fullName, first_name=fullName.split(" ")[0], last_name=fullName.split(" ")[-1], email=email, password=password) 
        user.save()
    return redirect('login')
  return render(request, 'register_page.html')