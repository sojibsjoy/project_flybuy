from django.shortcuts import render
from catalog.models import CartItem


def cart(request):

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

    return render(request, 'cart/cart.html', {'cartItems': cartItems})
