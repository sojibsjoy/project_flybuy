from django.shortcuts import render
from gallery.models import GalleryItem
from contacts.models import ContactInfo


def gallery(request):

    items = GalleryItem.objects.all()

    contactInfo = ContactInfo.objects.first()

    return render(request, 'gallery/gallery.html', {'items': items, 'contactInfo': contactInfo})
