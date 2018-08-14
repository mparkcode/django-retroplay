#  checkout urls

from django.urls import path
from .views import checkout, confirmation

urlpatterns = [
    path('', checkout, name='checkout'),
    path('confirmation', confirmation, name='confirmation'),
]