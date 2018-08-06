# products urls

from django.urls import path
from .views import all_brands, show_games, show_consoles, search_results


urlpatterns = [
    path('all_brands', all_brands, name="all_brands"),
    path('search_results/<query>', search_results, name="search_results"),
    path('<brand>', show_consoles, name="show_consoles"),
    path('show_games/<console>', show_games, name="show_games"),
    
]