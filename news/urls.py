# news urls

from django.urls import path
from .views import all_news, view_article

urlpatterns = [
    path('', all_news, name='all_news'),
    path('<int:pk>', view_article, name='view_article')
]