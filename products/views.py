from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Game, Console, Brand
import http.client
import urllib.request
import urllib.error
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    return render(request, "products/index.html")
    
    
def search_results(request, query):
    search_query = request.GET.get("query")
    if search_query:
        query = search_query
        return redirect('search_results', query)
    query_list = query.split(" ")
    games = Game.objects.all()
    for i in query_list:
        games = games.filter(title__icontains=i)
    for game in games:
        try:
            urllib.request.urlopen(game.image)
        except urllib.error.HTTPError as e:
            Game.objects.filter(title=game.title).delete()
        games = Game.objects.all()
    for i in query_list:
        games = games.filter(title__icontains=i)
        paginator = Paginator(games, 15)
        page = request.GET.get('page')
        games=paginator.get_page(page)
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
        paginator = Paginator(games, 15)
        page = request.GET.get('page')
        games=paginator.get_page(page)
        for game in games:
            try:
                urllib.request.urlopen(game.image)
            except urllib.error.HTTPError as e:
                Game.objects.filter(title=game.title).delete()
        return render(request, "products/show_games.html", {"games":games, "console": console_type})
    
