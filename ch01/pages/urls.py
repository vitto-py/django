from django.urls import path
from . import views

urlpatterns = [
    path("<int:idz>", views.index, name="index"),
    #looks for the integer in the path and calls it IDZ
]
