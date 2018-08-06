from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Game, Console, Brand



# Create your views here.
def index(request):
    return render(request, "products/index.html")
    
    
def search_results(request, query):
    search_query = request.GET.get("query")
    if search_query:
        query = search_query
        return redirect('search_results', query)
    games= Game.objects.filter(title__icontains=query)
    return render(request, "products/search_results.html", {"games":games})
    
def all_brands(request):
    search_query = request.GET.get("query")
    if search_query:
        query = search_query
        return redirect('search_results', query)
    else:
        brands = Brand.objects.all()
        return render(request, "products/all_brands.html", {"brands":brands})
    
def show_consoles(request, brand):
    brand = get_object_or_404(Brand, name=brand)
    search_query = request.GET.get("query")
    if search_query:
        query = search_query
        return redirect('search_results', query)
    else:
        consoles = Console.objects.filter(brand = brand)
        return render(request, "products/show_consoles.html", {'consoles':consoles, 'brand':brand})
    
    
def show_games(request, console):
    console_type = Console.objects.get(console_type=console)
    search_query = request.GET.get("query")
    if search_query:
        query = search_query
        return redirect('search_results', query)
    else:
        
        games=Game.objects.filter(console=console_type)
        return render(request, "products/show_games.html", {"games":games, "console": console_type})
    
