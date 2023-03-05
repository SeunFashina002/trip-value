from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.
class Testimonial(models.Model):
    testimony = models.TextField()
    image = models.URLField()
    name = models.CharField(max_length=200)