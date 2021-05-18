from django.shortcuts import render
from .models import Article


def blog(request):
    article1 = Article()
    article1.isPhotoArticle = True
    article1.img = "img1.jpg"
    article1.imgTitle = "Apple Devices"
    article1.imgAltText = "Apple Devices"
    article1.headline = "The next generation of Multi-Touch"
    article1.date = "07.01.2017"
    article1.desc = "The original iPhone introduced the world to Multi-Touch, forever changing the way people experience technology. With 3D Touch, you can do things that were never possible before. It senses how deeply you press the display, letting you do all kinds of essential things more quickly and simply. And it gives you real-time feedback in the form of subtle taps from the all-new Taptic Engine."

    article2 = Article()
    article2.isVideoArticle = True
    article2.img = "img2.jpg"
    article2.imgTitle = "Coffee"
    article2.imgAltText = "Coffee"
    article2.headline = "MacBook Pro - brand new day for business"
    article2.date = "02.01.2017"
    article2.desc = "Organizations everywhere are realizing the potential that Mac brings to their employees by giving them the freedom to use the tools they already know and love. Software and hardware made for each other. Because Apple designs both the software and hardware, every Mac delivers the best possible experience for employees."

    article3 = Article()
    article3.isReviewArticle = True
    article3.img = "img4.jpg"
    article3.imgTitle = "HP Chromebook"
    article3.imgAltText = "HP Chromebook"
    article3.headline = "HP Chromebook review."
    article3.date = "02.01.2017"
    article3.desc = "HP’s Chromebook 11 G4 ($199) has a dull-gray shell that screams, “bulk education purchase” more than “buy me.” Precisely because this school-oriented model can bang around in backpacks, however, it could teach its consumer Chromebook cousins a thing or two about build quality."

    articles = [article1, article2, article3]
    return render(request, 'blog/blog.html', {'articles': articles})


def item_photo(request):
    return render(request, 'blog/item-photo.html')


def item_video(request):
    return render(request, 'blog/item-video.html')


def item_review(request):
    return render(request, 'blog/item-review.html')
