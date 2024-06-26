from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import  ProfileUpdateForm, UserUpdateForm, ExampleForm
from django.contrib.auth.decorators import login_required

# Create your views here.

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
        return redirect('blog-register')

    return render(request, 'users/register.html')

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

    return render(request, 'users/login.html')

def logout_page(request):
    logout(request)
    return redirect('blog-login')

@login_required(login_url='blog-login')
def profile(request):
    return render(request, 'users/profile.html')

@login_required(login_url='blog-login')
def profile_update(request):
    if request.method=="POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect("blog-profile")
    else :      
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile) 
        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'users/profile_update.html', context)