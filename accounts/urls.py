# from django.contrib import admin
from django.urls import path
from accounts import views
urlpatterns = [	    
	path("login",views.loginUser, name="login"),
	path("logout",views.logoutUser, name="logout"),
	path("register",views.register, name="register"),
    # path("register", views.registerUser, name='registerUser'),
    # path('accounts/register/customer/', , name='CustomerSignup'),
    path("register/seller", views.registerSeller, name='sellerSignup'),
]
