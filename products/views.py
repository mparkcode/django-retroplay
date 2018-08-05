from django.shortcuts import render
from django.http import HttpResponse
from .models import Game, Console, Brand

# Create your views here.
def index(request):
    return render(request, "products/index.html")
    
def all_brands(request):
    brands = Brand.objects.all()
    return render(request, "products/all_brands.html", {"brands":brands})
    
def show_consoles(request, brand):
    brand = Brand.objects.get(name=brand)
    consoles = Console.objects.filter(brand = brand)
    return render(request, "products/show_consoles.html", {'consoles':consoles, 'brand':brand})
    
    
def show_games(request, console):
    console_type = Console.objects.get(console_type=console)
    games=Game.objects.filter(console=console_type)
    return render(request, "products/show_games.html", {"games":games, "console": console_type})