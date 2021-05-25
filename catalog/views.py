from catalog.models import Comment, PreviewItem, ProductDetail, ProductItem
from cart.models import CartItem
from home.models import Recommendation
from contacts.models import ContactInfo
from django.shortcuts import render


def catalog(request):

    cartItems = CartItem.objects.all()

    productItems = ProductItem.objects.all()

    contactInfo = ContactInfo.objects.first()

    return render(request, 'catalog/catalog.html', {'cartItems': cartItems, 'productItems': productItems, 'contactInfo': contactInfo})


def product(request):

    productDetail = ProductDetail.objects.first()

    cartItems = CartItem.objects.all()

    previewItems = PreviewItem.objects.all()

    recommends = Recommendation.objects.all()

    comments = Comment.objects.all()

    contactInfo = ContactInfo.objects.first()

    return render(request, 'catalog/product.html', {'productDetail': productDetail, 'cartItems': cartItems, 'previewItems': previewItems, 'recommends': recommends, 'comments': comments, 'contactInfo': contactInfo})
