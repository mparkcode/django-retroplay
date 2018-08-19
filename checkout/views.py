# checkout/views

from django.shortcuts import render, redirect
from .forms import OrderForm, MakePaymentForm
from cart.utils import get_cart_items_and_total
from django.utils import timezone
from django.contrib import messages
from .utils import save_order_items, charge_card
import stripe
from django.conf import settings
from .models import Order
# Create your views here.
def checkout(request):
    if request.method=="POST":
        order_form = OrderForm(request.POST)    
        payment_form = MakePaymentForm(request.POST)
        if order_form.is_valid() and payment_form.is_valid():
            # Save The Order
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
        
            # Save the Order Line Items
            cart = request.session.get('cart', {})
            save_order_items(order, cart)
        
            # Charge the Card
            items_and_total = get_cart_items_and_total(cart)
            total = items_and_total['total']
            stripe_token=payment_form.cleaned_data['stripe_id']

            try:
                customer = charge_card(stripe_token, total)
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "You have successfully paid")

                

                return redirect("confirmation")
            else:
                messages.error(request, "Unable to take payment")
    else:
        order_form = OrderForm()
        payment_form = MakePaymentForm()
        context = {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE }
        cart = request.session.get('cart', {})
        cart_items_and_total = get_cart_items_and_total(cart)
        if cart_items_and_total['total'] == 0:
            return redirect("index")
        context.update(cart_items_and_total)
        
    return render(request, "checkout/checkout.html", context)
    
def confirmation(request):
    cart = request.session.pop('cart', {})
    cart_items_and_total = get_cart_items_and_total(cart)
    if cart_items_and_total['total'] == 0:
        return redirect("index")
    context = get_cart_items_and_total(cart)
    billing_details = Order.objects.latest('id')
    context.update({'billing_details':billing_details})
    return render(request, "checkout/confirmation.html",  context)
