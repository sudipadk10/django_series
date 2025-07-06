# This file contains the logic for handling HTTP requests and returning responses

from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render,redirect

from myapp.form import StudentForm
from myapp.models import Student

# Create your views here.
def index(request):
    return render(request, 'index.html')
def home(request):
    context = {
        'message': 'Welcome to the Home Page!',
        'items': ['Apple', 'Banana', 'Cherry'],
        'name' : 'Sudip Adhikari',
        'products' : {
            'pen' : 100,
            'Bag' : 1100,
            'Laptop':90000,
         }
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
        return redirect('home')     # Redirect after processing
    return render(request, 'form.html')

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)  # Bind form data
        if form.is_valid():
            form.save()  # Save student data to the database
            return redirect('success')  # Redirect to student list page
    else:
        form = StudentForm()

    return render(request, 'form.html', {'form': form})
def success(request):
    students = Student.objects.all()
    return render(request, 'success.html', {'students': students})
