from django.db import models


class ProductItem(models.Model):
    isFavorite = models.BooleanField(default=False)
    img = models.ImageField(upload_to='productImgs')
    imgAltText = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    sale = models.FloatField(default=0.00)
    isOffer = models.BooleanField(default=False)
    priceThrough = models.FloatField(default=0.00)
    label = models.CharField(max_length=30)


class ProductDetail(models.Model):
    title = models.CharField(max_length=30)
    brandLogo = models.ImageField(upload_to='brandLogos')
    brandLogoAltText = models.CharField(max_length=30)
    subTitle1 = models.CharField(max_length=40)
    subTitle2 = models.CharField(max_length=40)
    subTitle3 = models.CharField(max_length=40)
    sale = models.FloatField(default=0.0)
    isOffer = models.BooleanField(default=False)
    priceThrough = models.FloatField(default=0.0)
    desc = models.TextField()
    osDetail = models.CharField(max_length=200)
    processorDetial = models.CharField(max_length=200)
    processorTechDetial = models.CharField(max_length=200)
    graphicsDetail = models.CharField(max_length=200)
    memoryDetail = models.CharField(max_length=200)
    harddriveDetail = models.CharField(max_length=200)
    wirelessDetail = models.CharField(max_length=200)
    powerSupplyDetail = models.CharField(max_length=200)
    batteryDetail = models.CharField(max_length=200)


class PreviewItem(models.Model):
    dataMarker = models.IntegerField(default=1)
    isActive = models.BooleanField(default=False)
    isVideo = models.BooleanField(default=False)
    videoId = models.CharField(max_length=30)
    videoTitle = models.CharField(max_length=100)
    videoDesc = models.TextField()
    videoThumbImg = models.ImageField(upload_to='productImgs')
    videoThumbImgAltText = models.CharField(max_length=30)
    img = models.ImageField(upload_to='productImgs')
    imgAltText = models.CharField(max_length=30)


class Comment(models.Model):
    authorName = models.CharField(max_length=30)
    date = models.CharField(max_length=20)
    desc = models.TextField()
