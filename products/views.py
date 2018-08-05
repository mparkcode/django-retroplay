from django.shortcuts import render
from django.http import HttpResponse
from .models import Game, Console, Brand

# Create your views here.
def index(request):
    return render(request, "products/index.html")
    
def all_brands(request):
    brands = Brand.objects.all()
    return render(request, "products/all_brands.html", {"brands":brands})
    
def all_nintendo(request):
    return render(request, "products/all_nintendo.html")
    
def show_games(request, console):
    console_type = Console.objects.get(console_type=console)
    games=Game.objects.filter(console=console_type)
    return render(request, "products/show_games.html", {"games":games})