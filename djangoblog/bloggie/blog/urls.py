from . import views
from django.urls import path

urlpatterns=[
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('register/', views.register, name='blog-register'),
    path('login/', views.login_page, name='blog-login'),
    path("logout/",views.logout_page, name='blog-logout')
]