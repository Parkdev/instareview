from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import LoginForm, SignupForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('posts:post-list')
        else:
            pass

    else:
        form = LoginForm()
        context = {
            'form':form
        }
        return render(request, 'members/login.html', context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('posts:post-list')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if username == User.objects.filter(username=username).exists():
            return HttpResponse('존재하는 아이디입니다.')
        elif password1 != password2:
            return HttpResponse('비밀번호가 다릅니다.')
        user = User.objects.create_user(username=username, password=password1)
        login(request, user)
        return redirect('posts:post-list')
    else:
        form = SignupForm()
        context = {
            'form' : form
        }
        return render(request,'members/signup.html', context)