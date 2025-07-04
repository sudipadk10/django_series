# This file contains the logic for handling HTTP requests and returning responses

from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')
def home(request):
    context = {
        'message': 'Welcome to the Home Page!',
        'items': ['Apple', 'Banana', 'Cherry'],
    }
    return render(request,'home.html',context)
def greet(request):
    if request.method == 'GET':
        return HttpResponse("Make a post request")
    elif request.method == 'POST':
        name = request.POST.get('name' , 'Guest')
        return HttpResponse(f"Hello {name}")
        

def about(request):
    return HttpResponse("This is about section ")
def profile(request,username):
    return HttpResponse(f"Hello {username}")

def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        # Process the data (e.g., save to the database)
        return redirect('home')  # Redirect after processing
    return render(request, 'form.html')