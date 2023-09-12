from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(response):
    return HttpResponse("<h1>Hello, World!</h1>")


def v1(response):
    return HttpResponse("<h1>you are in V1!</h1>")


def v2(response):
    return HttpResponse("<h1>You are in V2!</h1>")
