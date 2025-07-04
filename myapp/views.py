# This file contains the logic for handling HTTP requests and returning responses

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("This is home ")

def about(request):
    return HttpResponse("This is about section ")
def profile(request,name):
    return HttpResponse(f"Hello {name}")