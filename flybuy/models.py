from django.db import models


class SlideItem(models.Model):
    centerPosition = models.BooleanField(default=False)
    leftPosition = models.BooleanField(default=False)
    rightPosition = models.BooleanField(default=False)
    dataMarker = models.IntegerField(default=1)
    title = models.CharField(max_length=40)
    subTitle = models.TextField()
    imgPrimary = models.ImageField(upload_to='slidePics')
    imgSecondary = models.ImageField(upload_to='slidePics')
    imgAltText = models.CharField(max_length=30)
