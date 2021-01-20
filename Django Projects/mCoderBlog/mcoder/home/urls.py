from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('contact/', views.contact ),
    path('about/', views.about ),
    path('search/', views.search ),
	path('signup/', views.handleSignup ),
    path('login/', views.handleLogin ),
	path('logout/', views.handleLogout ),
	path('', views.home,name='home'),
]

