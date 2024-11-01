from django.shortcuts import render, redirect, reverse
from django.contrib import messages
import stripe
import os

from .forms import OrderForm

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': os.getenv('STRIPE_PUBLISHABLE_KEY')
    }

    return render(request, template, context)