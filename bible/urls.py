# bible urls

from django.urls import path
from .views import get_games

urlpatterns = [
    path('', get_games, name="get_games")
]