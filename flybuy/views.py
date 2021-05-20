from django.shortcuts import render
from home.models import SlideItem
from contacts.models import ContactInfo


def index(request):

    item1 = SlideItem()
    item1.dataMarker = 1
    item1.leftPosition = True
    item1.title = "New amazing laptops"
    item1.subTitle = "Provide lightweight and powerull"
    item1.imgPrimary = "newlaptops.jpg"
    item1.imgAltText = "Laptops"

    item2 = SlideItem()
    item2.dataMarker = 2
    item2.centerPosition = True
    item2.title = "8 Windows Hybrid Laptops"
    item2.subTitle = "The laptop comes with an Intel i5 chip and 8GB of RAM."
    item2.imgPrimary = "surfaces.jpg"
    item2.imgAltText = "Surface Pro"

    item3 = SlideItem()
    item3.dataMarker = 3
    item3.rightPosition = True
    item3.title = "Luxury devices"
    item3.subTitle = "Luxury watches, business tablets and 3D touch: How Apple plans to stay ahead in mobile.\nWhen it comes to the brand’s latest iPhones, the biggest excitement isn’t focused on the addition of a rose gold coloured device but the new 3D touch sensors."
    item3.imgPrimary = "ipadair2.jpg"
    item3.imgSecondary = "ipadair2m.jpg"
    item3.imgAltText = "iPad Air 2"

    items = [item1, item2, item3]

    contactInfo = ContactInfo()
    contactInfo.companyName = "FlyBuy, Inc."
    contactInfo.addressText1 = "1305 Market Street, Suite 800"
    contactInfo.addressText2 = "San Francisco, CA 94102"
    contactInfo.phoneNo = " (123) 456-7890"
    contactInfo.supportMail = "sup@example.com"
    contactInfo.partnerMail = "col@example.com"

    return render(request, 'index.html', {'items': items, 'contactInfo': contactInfo})
