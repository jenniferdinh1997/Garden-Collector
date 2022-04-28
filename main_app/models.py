from django.db import models
from django.urls import reverse

# Create your models here.
class Pot(models.Model):
    name = models.CharField(max_length = 50)
    color = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pots_detail', kwargs={'pk': self.id})
        
class Plant(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    pots = models.ManyToManyField(Pot)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'plant_id': self.id})

WATER = (
    ('1', '1 Cup'),
    ('2', '2 Cup'),
    ('3', '3 Cup')
)

class Water(models.Model):
    date = models.DateField('water date')
    water = models.CharField(
        max_length = 1,
        choices = WATER,
        default = WATER[0][0]
    )

    plant = models.ForeignKey(Plant, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.get_water_display()} on {self.date}"

    class Meta:
        ordering = ['-date']