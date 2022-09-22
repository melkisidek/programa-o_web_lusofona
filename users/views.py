# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect, render

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user)
           return redirect('portfolio:home')
 
        else:
            messages.success(request, (" erro no login"))
        return redirect('users:login')
    
    else:
        return render(request, 'users/login.html', {})


def logout_user (request):
    logout(request)
    messages.success(request, ("your logged out"))
    return redirect('portfolio:home')







