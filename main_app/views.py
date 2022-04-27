from django.shortcuts import render
from django.http import HttpResponse
from .models import Plant
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class PlantCreate(CreateView):
    model = Plant
    fields = '__all__'
    success_url = '/plants/'

class PlantUpdate(UpdateView):
    model = Plant
    fields = ['species', 'description', 'age']

class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants/'

def home(request):
    return HttpResponse('<h1>Hello World')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    return render(request, 'plants/index.html', {'plants': plants})

def plants_index(request):
    plants = Plant.objects.all()
    return render(request, 'plants/index.html', {'plants': plants})

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    return render(request, 'plants/detail.html', {'plant': plant})