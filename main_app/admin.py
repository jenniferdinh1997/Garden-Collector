from django.contrib import admin
from .models import Plant, Water, Pot

# Register your models here.
admin.site.register(Plant) #have to register models in order to manipulate the data
admin.site.register(Water)
admin.site.register(Pot)