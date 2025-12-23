from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Car(models.Model):

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cars/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(choices=[(
        'sedan', 'Sedan'), ('suv', 'SUV'), ('hatchback', 'Hatchback'), ('coupe', 'Coupe')])
    doors = models.IntegerField(choices=[(4, '4 Doors'), (6, '6 Doors')])
    passengers = models.IntegerField(choices=[(
        2, '2 Passengers'), (4, '4 Passengers'), (6, '6 Passengers'), (8, '8 Passengers')])
    transmission = models.CharField(choices=[(
        'manual', 'Manual'), ('automatic', 'Automatic'), ('semi-automatic', 'Semi-Automatic')])
    fuel = models.CharField(choices=[(
        'petrol', 'Petrol'), ('diesel', 'Diesel'), ('electric', 'Electric'), ('hybrid', 'Hybrid')])
    year = models.IntegerField()
    available = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
