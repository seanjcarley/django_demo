from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "There is noting in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key':'pk_test_51GxDaLKvL3qeWmYYuqe998bUtp27wtzfDnfw86C3Rory3jeru4OKHwZGRbRczfMUWsVPfwkX5C34aegLXiWUjiTb00EF5fay8O',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
