from faq.models import LeftQuestion, RightQuestion
from contacts.models import ContactInfo
from django.shortcuts import render


def faq(request):

    leftQs = LeftQuestion.objects.all()

    rightQs = RightQuestion.objects.all()

    contactInfo = ContactInfo.objects.first()

    return render(request, 'faq/faq.html', {'leftQs': leftQs, 'rightQs': rightQs, 'contactInfo': contactInfo})
