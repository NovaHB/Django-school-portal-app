import email
from multiprocessing import context
from re import template
from django.shortcuts import render
#import auth and user
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#import others
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginPage
from .models import Students
# Create your views here.
def portal(request):
    return redirect("loginpage")

def loginpage(request):
    form=LoginPage()
    if request.method == "POST":
        form=LoginPage(request.POST)
    if form.is_valid():
      #gets the inputted details
      username1=form.cleaned_data["email"]
      password1=form.cleaned_data["password"]
      #authenticate credentials
      user=authenticate(username=username1, password=password1)
      if user is not None:
        print("User Authenticated")
        #login the user
        login(request, user)
        return redirect("dashboard")
      else:
        print("failed to authenticate user")
        messages.info(request,"Invalid Username or Password") #prompts a message over at template
    else:
        print("'FORM NOT VALID")
        print(form.errors.as_data())
        
    template= "loginpage.html"
    context={
"form":form        
    }
    return render(request,template,context)


@login_required(login_url="/loginpage/")
def dashboard(request):
    templates="dashboard.html"
    #gets the current user
    current_user=request.user #returns the username 
    stud_deets=Students.objects.filter(email=current_user)
   
    
    context={
        "username":current_user,
        "stud":stud_deets
    }
    return render(request,templates,context)

def logoutview(request):
  logout(request)
  return redirect("loginpage")