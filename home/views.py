from django.shortcuts import redirect, render
from flybuy.models import SlideItem
from home.models import NewArticle, NewProducts, Recommendation
from contacts.models import ContactInfo
from django.contrib.auth.models import User, auth


def home(request):

    items = SlideItem.objects.all()

    products = NewProducts.objects.all()

    recommends = Recommendation.objects.all()

    newArticles = NewArticle.objects.all()

    contactInfo = ContactInfo.objects.first()

    return render(request, 'home/home.html', {'items': items, 'products': products, 'recommends': recommends, 'newArticles': newArticles, 'contactInfo': contactInfo})


def logout(request):
    auth.logout(request)
    return redirect('/')
