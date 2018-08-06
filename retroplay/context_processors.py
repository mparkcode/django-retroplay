from django.shortcuts import render
from django.http import HttpResponse
from products.models import Brand, Console
from products.forms import GameSearchForm

def get_brands(request):
    brands = Brand.objects.all()
    return{"all_brands":brands}
    
def get_consoles(request):
    consoles = Console.objects.all()
    return{"all_consoles":consoles}
    
def search_games(request):
    game_search_form = GameSearchForm()
    return {'game_search_form':game_search_form}