# bible views

from django.shortcuts import render, redirect
import requests
import os
from datetime import datetime
from .forms import IgdbSearchForm

ENDPOINT = os.environ.get('ENDPOINT')
USER_KEY = os.environ.get('IGDB_API_KEY_V3')

# Create your views here.
def get_games(request):
    search_query = request.GET.get("query")
    if search_query:
        query = search_query
        return redirect('search_results', query)
    form = IgdbSearchForm()
    games=[]
    igdb_search = request.GET.get("igdb_search")
    if igdb_search:
        response = requests.get(ENDPOINT, headers={'user-key': USER_KEY}, params={'search': igdb_search, 'fields' :'*'})
        for game in response.json():
            if game.get('first_release_date'):
                game['first_release_date'] = datetime.utcfromtimestamp(int(game['first_release_date'])).strftime('%Y/%m/%d')
            cover_query = requests.get(ENDPOINT, headers={'user-key': USER_KEY}, params={'fields': 'cover.*; where id = {}'.format(game['id'])})
            if cover_query.json()[0].get('cover'):
                game['cover_url'] = cover_query.json()[0]['cover']['url']
            games.append(game)
        return render(request, "bible/search_bible.html", {'games':games, 'form':form})    
    return render(request, "bible/search_bible.html", {'games':games, 'form':form})
    
def game_detail(request):
    search_query = request.GET.get("query")
    if search_query:
        query = search_query
        return redirect('search_results', query)
    
    game_id = request.GET.get("game_id")
    if game_id:
        form = IgdbSearchForm()
        response = requests.get(ENDPOINT, headers={'user-key': USER_KEY}, params={'fields': '*; where id = {}'.format(game_id)})
        game = response.json()[0]
        if 'cover' in game:
            cover_query = requests.get(ENDPOINT, headers={'user-key': USER_KEY}, params={'fields': 'cover.*; where id = {}'.format(game_id)})
            game['cover_url'] = cover_query.json()[0]['cover']['url'].replace("t_thumb","t_cover_big")
        if 'first_release_date' in game:
            game['first_release_date'] = datetime.utcfromtimestamp(int(game['first_release_date'])).strftime('%Y/%m/%d')
        if 'rating' in game:
            game['rating'] = round(game['rating'])
        if 'screenshots' in game:
            screenshot_query = requests.get(ENDPOINT, headers={'user-key': USER_KEY}, params={'fields': 'screenshots.*; where id = {}'.format(game_id)})
            game['screenshots'] = screenshot_query.json()[0]['screenshots']
            for i in game['screenshots']:
                i['url']=i['url'].replace("t_thumb","t_original")
        return render(request, "bible/game_detail.html", {'game':game, 'form':form})
    return redirect('get_games')