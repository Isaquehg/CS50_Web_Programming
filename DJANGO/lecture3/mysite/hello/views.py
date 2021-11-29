from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")
def isaque(request):
    return HttpResponse("Hello, Isaque!")
def bruna(request):
    return HttpResponse("Hello, Bruna!")
#this will create a dynamic response to all names and capitalize it
def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")