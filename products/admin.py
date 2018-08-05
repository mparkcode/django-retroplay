from django.contrib import admin
from .models import Game, Brand, Console

# Register your models here.
admin.site.register(Game)
admin.site.register(Brand)
admin.site.register(Console)