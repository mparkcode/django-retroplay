# info urls

from django.urls import path
from .views import contact, shipping, faq

urlpatterns = [
    path('contact', contact, name='contact'),
    path('shipping', shipping, name='shipping'),
    path('faq', faq, name='faq')
]