from django.shortcuts import render
from django.http import HttpResponse
from .models import Plant

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello World')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    return render(request, 'plants/index.html', {'plants': plants})

def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {'plants': plants})