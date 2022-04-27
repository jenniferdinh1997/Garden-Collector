from django.urls import path
from . import views #referring to the views file

urlpatterns = [ #defines a root path using an empty string and maps it to the view.home function (name='home') references the URL in other parts of the app
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('plants/', views.plants_index, name='index'),
    path('plants/<int:plant_id>', views.plants_detail, name='detail'),
]