from django.shortcuts import render
from gallery.models import GalleryItem


def gallery(request):

    item1 = GalleryItem()
    item1.isVideo = True
    item1.videoThumb = "video-apple.jpg"
    item1.videoId = "110691368"
    item1.videoTitle = "Apple iPad Air"
    item1.videoDesc = "So capable, you won’t want to put it down. So thin and light, you won’t have to."

    item2 = GalleryItem()
    item2.img = "img1.jpg"
    item2.imgTitle = "HP Chromebook 14"
    item2.imgDesc = "HP Chromebook 14 with all modern technologies to achive 'the most fast laptop on earth' title."

    items = [item1, item2]

    return render(request, 'gallery/gallery.html', {'items': items})
