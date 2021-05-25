from checkout.models import DeliveryAddress, DeliveryOption, PaymentMethod, Summary
from cart.models import CartItem
from django.shortcuts import render
from contacts.models import ContactInfo


def checkout(request):

    cartItems = CartItem.objects.all()

    summary = Summary.objects.first()

    dAddresses = DeliveryAddress.objects.all()

    dOptions = DeliveryOption.objects.all()

    pMethods = PaymentMethod.objects.all()

    contactInfo = ContactInfo.objects.first()

    return render(request, 'checkout/checkout.html', {'cartItems': cartItems, 'summary': summary, 'dAddresses': dAddresses, 'dOptions': dOptions, 'pMethods': pMethods, 'contactInfo': contactInfo})
