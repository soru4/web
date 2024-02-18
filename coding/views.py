from django.shortcuts import render
from django.contrib.auth import authenticate
# Create your views here.
from django.contrib.auth import login

def loadHomeScreen(request):
    return render(request, "home.html");

from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def register(response):
    if response.method == "POST":
	    form = RegisterForm(response.POST)
	    if form.is_valid():
	        form.save()
	    return redirect("home")
    else:
	    form = RegisterForm()
    return render(response, "register.html", {"form":form})
 