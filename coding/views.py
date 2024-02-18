from django.shortcuts import render

# Create your views here.


def loadHomeScreen(request):
    return render(request, "home.html");


 