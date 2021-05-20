from checkout.models import DeliveryAddress, DeliveryOption, PaymentMethod, Summary
from cart.models import CartItem
from django.shortcuts import render
from contacts.models import ContactInfo


def checkout(request):

    cartItem1 = CartItem()
    cartItem1.img = "chrome-book-11.jpg"
    cartItem1.imgAltText = "HP Chromebook 11"
    cartItem1.title = "HP Chromebook 11"
    cartItem1.label = "Laptops"
    cartItem1.price = 199.99
    cartItem1.quantity = 2

    cartItem2 = CartItem()
    cartItem2.img = "chrome-book-14.jpg"
    cartItem2.imgAltText = "HP Chromebook 14"
    cartItem2.title = "HP Chromebook 14"
    cartItem2.label = "Laptops"
    cartItem2.price = 209.99
    cartItem2.quantity = 1

    cartItem3 = CartItem()
    cartItem3.img = "ipad-air.jpg"
    cartItem3.imgAltText = "iPad Air"
    cartItem3.title = "iPad Air"
    cartItem3.label = "Tablets"
    cartItem3.price = 449.99
    cartItem3.quantity = 2

    cartItem4 = CartItem()
    cartItem4.img = "mi-pad-2.jpg"
    cartItem4.imgAltText = "Mi Pad 2"
    cartItem4.title = "Mi Pad 2"
    cartItem4.label = "Tablets"
    cartItem4.price = 199.99
    cartItem4.quantity = 3

    cartItems = [cartItem1, cartItem2, cartItem3, cartItem4]

    summary = Summary()
    summary.subTotal = 1499.00
    summary.discount = 0.00
    summary.delivery = 0.00
    summary.total = 1499.00

    dAddress1 = DeliveryAddress()
    dAddress1.isSelected = True
    dAddress1.name = "John Doe"
    dAddress1.country = "United States"
    dAddress1.city = "New York City"
    dAddress1.street = "45 Park Avenue"
    dAddress1.building = "Jericho"
    dAddress1.zipCode = "11378"

    dAddress2 = DeliveryAddress()
    dAddress2.name = "John Doe"
    dAddress2.country = "United States"
    dAddress2.city = "New York City"
    dAddress2.street = "45 Park Avenue"
    dAddress2.building = "Jericho"
    dAddress2.zipCode = "11378"

    dAddresses = [dAddress1, dAddress2]

    dOption1 = DeliveryOption()
    dOption1.isSelected = True
    dOption1.img = "fedex.jpg"
    dOption1.imgTitle = "FedEx"
    dOption1.imgAltText = "fedex"
    dOption1.desc = "2-3 working days"

    dOption2 = DeliveryOption()
    dOption2.img = "dhl.jpg"
    dOption2.imgTitle = "DHL"
    dOption2.imgAltText = "dhl"
    dOption2.desc = "5-10 working days"

    dOptions = [dOption1, dOption2]

    pMethod1 = PaymentMethod()
    pMethod1.isSelected = True
    pMethod1.img = "paypal.jpg"
    pMethod1.imgTitle = "PayPal"
    pMethod1.imgAltText = "paypal"
    pMethod1.desc = "0% Service fee"

    pMethods = [pMethod1]

    contactInfo = ContactInfo()
    contactInfo.companyName = "FlyBuy, Inc."
    contactInfo.addressText1 = "1305 Market Street, Suite 800"
    contactInfo.addressText2 = "San Francisco, CA 94102"
    contactInfo.phoneNo = " (123) 456-7890"
    contactInfo.supportMail = "sup@example.com"
    contactInfo.partnerMail = "col@example.com"

    return render(request, 'checkout/checkout.html', {'cartItems': cartItems, 'summary': summary, 'dAddresses': dAddresses, 'dOptions': dOptions, 'pMethods': pMethods, 'contactInfo': contactInfo})
