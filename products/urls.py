# products urls

from django.urls import path
from .views import all_brands, show_games, show_consoles

urlpatterns = [
    path('all_brands', all_brands, name="all_brands"),
    path('<brand>', show_consoles, name="show_consoles"),
    path('show_games/<console>', show_games, name="show_games")
]