# products urls

from django.urls import path
from .views import all_brands, all_nintendo, show_games

urlpatterns = [
    path('all_brands', all_brands, name="all_brands"),
    path('all_nintendo', all_nintendo, name="all_nintendo"),
    path('show_games/<console>', show_games, name="show_games")
]