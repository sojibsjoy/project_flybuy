from django.shortcuts import render
from flybuy.models import SlideItem
from contacts.models import ContactInfo


def index(request):

    items = SlideItem.objects.all()

    contactInfo = ContactInfo.objects.first()

    return render(request, 'index.html', {'items': items, 'contactInfo': contactInfo})
