from django.contrib import admin
from django.urls import path, include
from . import views
from .views import login_view, logout_view
from .views import search_videos


urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('login/', login_view, name="login"),
    path('register/', views.register, name='register'),
    path('logout', views.logout_view, name="logout"),
    path('blog/', views.blog, name="blog"),
    path('search/', views.search_videos, name='search_videos'),
    path('reservation/', views.make_reservartion, name='reservartion'),
    path('profile/', views.profile, name='profile'),   
    path('update_profile/', views.update_profile, name='Profile Update'),  

]



