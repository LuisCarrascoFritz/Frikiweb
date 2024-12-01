from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_post/', views.create_post, name='create_post'),
    path('view_posts/', views.view_posts, name='view_posts'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
]
