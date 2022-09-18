from django import views
from django.urls import path 
from . import views #imports the view code 
urlpatterns = [
    path("", views.portal,name="portal"),
    path("loginpage/", views.loginpage,name="loginpage"),
    path("dashboard/", views.dashboard,name="dashboard"),
    path("logoutview/", views.logoutview ,name="logoutview"),
]
