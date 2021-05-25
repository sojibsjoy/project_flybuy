from contacts.models import ContactInfo
from django.shortcuts import render


def contacts(request):

    contactInfo = ContactInfo.objects.first()

    return render(request, 'contacts/contacts.html', {'contactInfo': contactInfo})
