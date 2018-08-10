# cart urls

from django.urls import path
from .views import view_cart, add_to_cart, remove_from_cart, update_quantity

urlpatterns = [
    path('view', view_cart, name='view_cart'),
    path('add', add_to_cart, name='add_to_cart'),
    path('remove', remove_from_cart, name='remove_from_cart'),
    path('update', update_quantity, name='update_quantity'),
]