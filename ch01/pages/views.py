from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import ToDoList, Item


def index(response, idz):
    # page # = one list
    ls = ToDoList.objects.get(id=idz)
    return render(response, "pages/list.html", {"ls": ls})


def home(response):
    return render(response, "pages/main.html", {})
