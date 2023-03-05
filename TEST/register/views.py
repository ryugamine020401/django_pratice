from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .form import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
# Create your views here.
# 首頁

@login_required(login_url="Login")
def register(request):
    return render(request, 'loginindex.html')

def sign_up(request):


    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/register/login')  # 重新導向到登入畫面
    context = {
        'form' : form
    }
    return render(request, 'register.html', context)

def sign_in(request):
    form = LoginForm()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/register')  # 重新導向到首頁
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

def log_out(request):
    logout(request)
    return redirect('/register/login') #重新導向到登入畫面