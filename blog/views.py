from django.shortcuts import render
from blog.models import Article, PhotoBlogComment, PhotoBlogItem, ReviewBlogItem, ReviewProduct, VideoBlogComment, VideoBlogItem
from contacts.models import ContactInfo


def blog(request):

    articles = Article.objects.all()

    contactInfo = ContactInfo.objects.first()

    return render(request, 'blog/blog.html', {'articles': articles, 'contactInfo': contactInfo})


def item_photo(request):

    photoBlogItem = PhotoBlogItem.objects.first()

    pbcs = PhotoBlogComment.objects.all()

    contactInfo = ContactInfo.objects.first()

    return render(request, 'blog/item-photo.html', {'photoBlogItem': photoBlogItem, 'pbcs': pbcs, 'contactInfo': contactInfo})


def item_video(request):

    videoBlogItem = VideoBlogItem.objects.first()

    vbcs = VideoBlogComment.objects.all()

    contactInfo = ContactInfo.objects.first()

    return render(request, 'blog/item-video.html', {'videoBlogItem': videoBlogItem,  'vbcs': vbcs, 'contactInfo': contactInfo})


def item_review(request):

    reviewBlogItem = ReviewBlogItem.objects.first()

    rProducts = ReviewProduct.objects.all()

    contactInfo = ContactInfo.objects.first()

    return render(request, 'blog/item-review.html', {'reviewBlogItem': reviewBlogItem, 'rProducts': rProducts, 'contactInfo': contactInfo})
