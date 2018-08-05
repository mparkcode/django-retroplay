from django.shortcuts import render
from django.http import HttpResponse
from .models import Game

# Create your views here.
def index(request):
    return render(request, "products/index.html")
    
def all_brands(request):
    return render(request, "products/all_brands.html")
    
def all_nintendo(request):
    return render(request, "products/all_nintendo.html")
    
def show_games(request, console):
    games=Game.objects.filter(console=console)
    return render(request, "products/show_games.html", {"games":games})