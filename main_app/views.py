from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Plant, Pot
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import WaterForm

# Create your views here.
class PlantCreate(CreateView):
    model = Plant
    fields = ['name', 'species', 'description', 'age']
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
    pots_plant_doesnt_have = Pot.objects.exclude(id__in = plant.pots.all().values_list('id'))
    water_form = WaterForm()
    return render(request, 'plants/detail.html', {'plant': plant, 'water_form': water_form, 'pots': pots_plant_doesnt_have})

def add_water(request, plant_id):
    form = WaterForm(request.POST)
    if form.is_valid():
        new_water = form.save(commit = False)
        new_water.plant_id = plant_id
        new_water.save()
    return redirect('detail', plant_id = plant_id)

class PotList(ListView):
    model = Pot

class PotDetail(DetailView):
    model = Pot

class PotCreate(CreateView):
    model = Pot
    fields = '__all__'

class PotUpdate(UpdateView):
    model = Pot
    fields = ['name', 'color']

class PotDelete(DeleteView):
    model = Pot
    success_url = '/pots/'

def assoc_pot(request, plant_id, pot_id):
    Plant.objects.get(id=plant_id).pots.add(pot_id)
    return redirect('detail', plant_id=plant_id)