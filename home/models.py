from django.db import models


class NewProducts(models.Model):
    isFavorite = models.BooleanField(default=False)
    headline = models.CharField(max_length=30)
    isOffer = models.BooleanField(default=False)
    sale = models.FloatField()
    priceThrough = models.FloatField()
    label = models.CharField(max_length=30)
    img = models.ImageField(upload_to='productImgs')
    imgAltText = models.CharField(max_length=30)


class Recommendation(models.Model):
    isFavorite = models.BooleanField(default=False)
    headline = models.CharField(max_length=30)
    isOffer = models.BooleanField(default=False)
    sale = models.FloatField()
    priceThrough = models.FloatField()
    label = models.CharField(max_length=30)
    img = models.ImageField(upload_to='productImgs')
    imgAltText = models.CharField(max_length=30)


class NewArticle(models.Model):
    isPhotoArticle = models.BooleanField(default=False)
    isVideoArticle = models.BooleanField(default=False)
    isReviewArticle = models.BooleanField(default=False)
    img = models.ImageField(upload_to='blogItemPics')
    imgTitle = models.CharField(max_length=30)
    imgAltText = models.CharField(max_length=30)
    headline = models.CharField(max_length=75)
    date = models.CharField(max_length=30)
    desc = models.TextField()
