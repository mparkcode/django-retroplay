#  cart/utils
from django.shortcuts import get_object_or_404
from products.models import Game
from decimal import Decimal

def get_cart_items_and_total(cart):
    cart_total = 0
    cart_items = []
    number_of_items = 0
    for p in cart:
        game = get_object_or_404(Game, pk=p)
        cart_item = {
            'game' : game,
            'quantity' : cart[p],
            'total': Decimal(game.price * cart[p])
        }
        number_of_items += cart_item['quantity']
        cart_items.append(cart_item)
        cart_total += cart_item['total']
    return {'cart': cart_items, 'total': cart_total, 'number_of_items':number_of_items}