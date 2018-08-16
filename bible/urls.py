# bible urls

from django.urls import path
from .views import get_games, game_detail

urlpatterns = [
    path('', get_games, name="get_games"),
    path('game_detail', game_detail, name="game_detail")
]