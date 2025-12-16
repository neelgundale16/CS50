from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/form.html")

def neel(request):
    return HttpResponse("Hello, Neel!")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")