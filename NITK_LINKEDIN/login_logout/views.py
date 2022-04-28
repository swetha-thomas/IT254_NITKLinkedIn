from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_user

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