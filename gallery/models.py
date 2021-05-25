from django.db import models


class GalleryItem(models.Model):
    img = models.ImageField(upload_to='productImgs')
    imgTitle = models.CharField(max_length=30)
    imgDesc = models.TextField()
    isVideo = models.BooleanField(default=False)
    videoThumb = models.ImageField(upload_to='productImgs')
    videoId = models.CharField(max_length=30)
    videoTitle = models.CharField(max_length=30)
    videoDesc = models.TextField()
