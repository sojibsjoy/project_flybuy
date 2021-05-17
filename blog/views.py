from django.shortcuts import render


def blog(request):
    return render(request, 'blog/blog.html')


def item_photo(request):
    return render(request, 'blog/item-photo.html')


def item_video(request):
    return render(request, 'blog/item-video.html')


def item_review(request):
    return render(request, 'blog/item-review.html')
