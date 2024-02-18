from . import views
from django.urls import path

urlpatterns = [
    path('hello/', views.loadHomeScreen, name = "home"),
    
]
