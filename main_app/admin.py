from django.contrib import admin
from .models import Plant, Water

# Register your models here.
admin.site.register(Plant) #have to register models in order to manipulate the data
admin.site.register(Water)