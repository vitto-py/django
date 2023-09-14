from django.urls import path
from . import views

urlpatterns = [
  #looks for the integer in the path and calls it IDZ
    path("<int:idz>", views.index, name="index"),
    path("", views.home, name="home")
    
]
