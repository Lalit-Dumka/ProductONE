from django.contrib import admin
from django.urls import path
from accounts import views
urlpatterns = [	    
	path("login",views.loginUser, name="loginUser"),
	path("logout",views.logoutUser, name="logoutUser"),
	path("register",views.register, name="register"),
]
