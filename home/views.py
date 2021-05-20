from django.shortcuts import render
from home.models import NewArticle, NewProducts, Recommendation, SlideItem
from contacts.models import ContactInfo


def home(request):

    contactInfo = ContactInfo()
    contactInfo.companyName = "FlyBuy, Inc."
    contactInfo.addressText1 = "1305 Market Street, Suite 800"
    contactInfo.addressText2 = "San Francisco, CA 94102"
    contactInfo.phoneNo = " (123) 456-7890"
    contactInfo.supportMail = "sup@example.com"
    contactInfo.partnerMail = "col@example.com"

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

    product1 = NewProducts()
    product1.isFavorite = True
    product1.headline = "Surface Pro"
    product1.isOffer = True
    product1.sale = 199.99
    product1.priceThrough = 299.99
    product1.label = "Hybrid"
    product1.img = "surface-pro.jpg"
    product1.imgAltText = "Surface Pro"

    product2 = NewProducts()
    product2.isFavorite = False
    product2.headline = "Lenovo Yoga"
    product2.isOffer = True
    product2.sale = 299.99
    product2.priceThrough = 399.99
    product2.label = "Hybrid"
    product2.img = "lenovo-yoga.jpg"
    product2.imgAltText = "Lenovo Yoga"

    product3 = NewProducts()
    product3.isFavorite = True
    product3.headline = "ASUS Transformer"
    product3.isOffer = False
    product3.sale = 399.99
    product3.label = "Hybrid"
    product3.img = "asus-transformer.jpg"
    product3.imgAltText = "ASUS Transformer"

    products = [product1, product2, product3]

    recommend1 = Recommendation()
    recommend1.isFavorite = False
    recommend1.headline = "HP Chromebook 11"
    recommend1.isOffer = False
    recommend1.sale = 199.99
    recommend1.label = "Laptops"
    recommend1.img = "chrome-book-11.jpg"
    recommend1.imgAltText = "HP Chromebook 11"

    recommend2 = Recommendation()
    recommend2.isFavorite = False
    recommend2.headline = "HP Chromebook 14"
    recommend2.isOffer = True
    recommend2.sale = 209.99
    recommend2.priceThrough = 249.99
    recommend2.label = "Laptops"
    recommend2.img = "chrome-book-14.jpg"
    recommend2.imgAltText = "HP Chromebook 14"

    recommend3 = Recommendation()
    recommend3.isFavorite = True
    recommend3.headline = "Asus Chromebook"
    recommend3.isOffer = False
    recommend3.sale = 299.99
    recommend3.label = "Laptops"
    recommend3.img = "chrome-book-asus.jpg"
    recommend3.imgAltText = "ASUS Chromebook"

    recommend4 = Recommendation()
    recommend4.isFavorite = True
    recommend4.headline = "HP Chromebook 14"
    recommend4.isOffer = True
    recommend4.sale = 209.99
    recommend4.priceThrough = 249.99
    recommend4.label = "Laptops"
    recommend4.img = "chrome-book-14.jpg"
    recommend4.imgAltText = "HP Chromebook 14"

    recommends = [recommend1, recommend2, recommend3, recommend4]

    newArticle1 = NewArticle()
    newArticle1.isPhotoArticle = True
    newArticle1.img = "img1.jpg"
    newArticle1.imgTitle = "Apple Devices"
    newArticle1.imgAltText = "Apple Devices"
    newArticle1.headline = "The next generation of Multi-Touch"
    newArticle1.date = "07.01.2017"
    newArticle1.desc = "The original iPhone introduced the world to Multi-Touch, forever changing the way people experience technology. With 3D Touch, you can do things that were never possible before. It senses how deeply you press the display, letting you do all kinds of essential things more quickly and simply. And it gives you real-time feedback in the form of subtle taps from the all-new Taptic Engine."

    newArticle2 = NewArticle()
    newArticle2.isVideoArticle = True
    newArticle2.img = "img2.jpg"
    newArticle2.imgTitle = "Coffee"
    newArticle2.imgAltText = "Coffee"
    newArticle2.headline = "MacBook Pro - brand new day for business"
    newArticle2.date = "02.01.2017"
    newArticle2.desc = "Organizations everywhere are realizing the potential that Mac brings to their employees by giving them the freedom to use the tools they already know and love. Software and hardware made for each other. Because Apple designs both the software and hardware, every Mac delivers the best possible experience for employees."

    newArticles = [newArticle1, newArticle2]

    return render(request, 'home/home.html', {'items': items, 'products': products, 'recommends': recommends, 'newArticles': newArticles, 'contactInfo': contactInfo})
