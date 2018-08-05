from django.db import models
from django.db.models import Avg

# Create your models here.

        
class Brand(models.Model):
    name = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name
        
class Console(models.Model):
    console_type = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to='images')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.console_type
    
class Game(models.Model):
    title = models.CharField(max_length=254, default='')
    image = models.CharField(max_length=254, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    console = models.ForeignKey(Console, on_delete=models.CASCADE)

    def __str__(self):
        return self.title