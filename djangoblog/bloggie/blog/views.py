from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

# @login_required(login_url='blog-login')
# def home(request):
#     posts=models.Post.objects.all()
#     return render(request,'blog/home.html', {"posts":posts})

# def about(request):
#     return render(request, 'blog/about.html')


class PostListView(LoginRequiredMixin,ListView):
    model=models.Post
    template_name='blog/home.html'
    ordering=['-date_posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get the latest three posts separately
        latest_posts = models.Post.objects.order_by('-date_posted')[:3]
        
        # Add latest posts to the context
        context['latest_posts'] = latest_posts
        return context

class PostDetailView(LoginRequiredMixin,DetailView):
    model=models.Post

class PostCreate(LoginRequiredMixin,CreateView):
    model=models.Post  
    fields=['title','content']  

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
    
class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=models.Post    
    fields=['title','content'] 

    def form_valid(self, form):
        form.instance.author = self.request.user  
        return super().form_valid(form)
    
    def test_func(self) :
        post=self.get_object()
        if self.request.user==post.author :
            return True
        return False
    
class PostDelete(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model=models.Post
    success_url='/catalog/'

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
        