from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from .models import ToDoList, Item
from .forms import createNew


def index(response, idz):
    # page # = one list
    ls = ToDoList.objects.get(id=idz)
    return render(response, "pages/list.html", {"ls": ls})


def home(response):
    return render(response, "pages/main.html", {})


def create(response):
    # post is fired when you hit submit 
    if response.method == "POST":
        resp = createNew(response.POST)  # get the data from the SUBMIT
        if resp.is_valid():
            # unencript and give me the field name of the form
            n = resp.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()  # like in the shell

        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = createNew()
    return render(response, "pages/newform.html", {"form": form})
