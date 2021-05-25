from django.shortcuts import render
from cart.models import CartItem
from checkout.models import Summary
from contacts.models import ContactInfo


def cart(request):

    summary = Summary.objects.first()

    cartItems = CartItem.objects.all()

    contactInfo = ContactInfo.objects.first()

    return render(request, 'cart/cart.html', {'summary': summary, 'cartItems': cartItems, 'contactInfo': contactInfo})
