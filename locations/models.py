from pyexpat import model
from django.db import models


# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Terminal(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, related_name='state', on_delete=models.CASCADE)
    description = models.TextField(default='')

    def __str__(self):
        return self.name


class Trips(models.Model):
    image_url = models.URLField()
    departure = models.CharField(max_length=200)
    arrival = models.CharField(max_length=200)
    transport_fee = models.CharField(max_length=50,)
    created_at = models.DateTimeField(auto_now_add=True)

