from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import ToDoList, Item


def index(response, idz):
    # page # = one list
    ls = ToDoList.objects.get(id=idz)
    # get erste item inside list ls
    item = ls.item_set.get(id=1)
    return HttpResponse(
        "<h1>%s</h1><br></br><p>%s</p>" % (ls.name, item.text))
