from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'stripe_public_key': 'pk_test_51IzL7OAdTWS0jaZOaD3oFSrFiEXmFF2mQqEo6uTA786V9HzFYKONYvufuq3FhtLqneWGOclkg8GP2Yv6g8pSG2P800gBNJUCR4',
        'client_secret': 'test client secret',
        'order_form': order_form,
    }

    return render(request, template, context)