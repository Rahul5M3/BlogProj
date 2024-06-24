from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='blog-login')
def home(request):
    posts=models.Post.objects.all()
    return render(request,'blog/home.html', {"posts":posts})

def about(request):
    return render(request, 'blog/about.html')

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exist")
            return redirect('blog-register')

        user=User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        messages.success(request, "Successfull Registered")
        return redirect('register/')

    return render(request, 'blog/register.html')

def login_page(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if User.objects.filter(username=username).exists()==False:
            messages.error(request, "No such username exist")
            return redirect('blog-login')
        
        if authenticate(username=username, password=password) is None:
            messages.error(request, "Invalid username or password")
            return redirect('blog-login')

        else :
            login(request,authenticate(username=username, password=password))
            return redirect('blog-home')

    return render(request, 'blog/login.html')

def logout_page(request):
    logout(request)
    return redirect('blog-login')
