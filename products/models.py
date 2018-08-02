from django.db import models
from django.db.models import Avg

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=254, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=50, default='')
    console = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.title