from . import views
from django.urls import path
from users import views as user_views



urlpatterns=[
    path('', views.PostListView.as_view(), name='blog-home'),
    path('blog/<int:pk>/', views.PostDetailView.as_view(), name='blog-detail'),
    path('blog/new/', views.PostCreate.as_view(), name='blog-create'),
    path('blog/update/<int:pk>/', views.PostUpdate.as_view(), name='blog-update'),
    path('blog/delete/<int:pk>/', views.PostDelete.as_view(), name='blog-delete'),
    # path('about/', views.about, name='blog-about'),
    path('register/', user_views.register, name='blog-register'),
    path('login/', user_views.login_page, name='blog-login'),
    path("logout/",user_views.logout_page, name='blog-logout'),
    path('profile/', user_views.profile, name='blog-profile'),
    path('profileUpdate/', user_views.profile_update, name='blog-profileUpdate')
] 