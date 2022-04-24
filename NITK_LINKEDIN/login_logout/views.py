from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_user
from numpy import full


# Create your views here.

def login(request):
  if request.method == 'POST':
    if request.POST.get('flexRadioDefault') == 'student':
      email = request.POST["email"]
      password = request.POST["password"]
      user = authenticate(username="akheel", email=email, password=password)
      if user is not None:
        login_user(request, user)
        return redirect('studentHome')
      else:
        messages.info(request, "Invalid Credentials")
        return redirect('login')
    else:
      return redirect('organizationHome')
  return render(request, 'login_page.html')

def logout(request):
  # logout user and finish up all loose ends
  return redirect('login')

def register(request):
  if request.method == 'POST':
    fullName = request.POST["fullName"]
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
      user = User.objects.create_user(username=fullName, first_name=fullName.split(" ")[0], last_name=fullName.split(" ")[-1], email=email, password=password) 
      user.save()
    
    return redirect('login')
  return render(request, 'register_page.html')