# This file contains the logic for handling HTTP requests and returning responses

from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404



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
            return redirect('add_student')
    else:
        form = StudentForm()
    students = Student.objects.all()
    return render(request, 'form.html', {'form': form,'students': students})


def success(request):
    students = Student.objects.all()
    return render(request, 'success.html', {'students': students})

def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('add_student')

    return render(request, 'form.html', {'form': form, 'students': Student.objects.all()})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('add_student')

