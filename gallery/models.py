from django.db import models


class GalleryItem:
    img: str
    imgTitle: str
    imgDesc: str
    isVideo: bool
    videoThumb: str
    videoId: str
    videoTitle: str
    videoDesc: str
