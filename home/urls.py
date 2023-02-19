from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
	path("",views.index, name="home"),
	    
	path("listProperty",views.listProperty, name="listProperty"),
	path("reviews",views.reviews, name="reviews"),
	path("contact",views.contact, name="contact "), 
	path("cityRooms",views.cityRooms, name="cityRooms"),
]
