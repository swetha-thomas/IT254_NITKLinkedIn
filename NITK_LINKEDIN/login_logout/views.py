from django.shortcuts import redirect, render

# Create your views here.

def login(request):
  if request.method == 'POST':
    if request.POST.get('flexRadioDefault') == 'student':
      return redirect('studentHome')
    return redirect('organizationHome')
  return render(request, 'login_page.html')

def logout(request):
  # logout user and finish up all loose ends
  return redirect('login')

def register(request):
  if request.method == 'POST':
    return redirect('login')
  return render(request, 'register_page.html')