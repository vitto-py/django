from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import createNew


def index(response, idz):
    # page # = one list
    ls = ToDoList.objects.get(id=idz)
    return render(response, "pages/list.html", {"ls": ls})


def home(response):
    return render(response, "pages/main.html", {})


def create(response):
    form = createNew()
    return render(response, "pages/newform.html", {"form": form})
