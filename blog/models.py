from django.db import models


class Article(models.Model):
    isPhotoArticle = models.BooleanField(default=False)
    isVideoArticle = models.BooleanField(default=False)
    isReviewArticle = models.BooleanField(default=False)
    img = models.ImageField(upload_to='blogItemPics')
    imgTitle = models.CharField(max_length=30)
    imgAltText = models.CharField(max_length=30)
    headline = models.CharField(max_length=75)
    date = models.CharField(max_length=30)
    desc = models.TextField()


class PhotoBlogItem(models.Model):
    img = models.ImageField(upload_to='blogItemPics')
    imgAltText = models.CharField(max_length=30)
    headline = models.CharField(max_length=75)
    bodyText = models.TextField()


class PhotoBlogComment(models.Model):
    authorName = models.CharField(max_length=30)
    date = models.CharField(max_length=20)
    comment = models.TextField()


class VideoBlogItem(models.Model):
    videoId = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    thumbImg = models.ImageField(upload_to='blogItemPics')
    thumbImgAltText = models.CharField(max_length=30)
    headline = models.TextField()
    bodyText = models.TextField()


class VideoBlogComment(models.Model):
    authorName = models.CharField(max_length=30)
    date = models.CharField(max_length=20)
    comment = models.TextField()


class ReviewBlogItem(models.Model):
    title = models.CharField(max_length=30)
    titleDesc = models.TextField()
    isVideoAvailable = models.BooleanField(default=False)
    videoId = models.CharField(max_length=30)
    thumbImg = models.ImageField(upload_to='blogItemPics')
    thumbImgAltText = models.CharField(max_length=30)
    videoTitle = models.CharField(max_length=100)
    videoDesc = models.TextField()
    startingPrice = models.FloatField(0.00)
    ffFlag = models.BooleanField(default=False)
    ffTitle1 = models.CharField(max_length=50)
    ffTitle2 = models.CharField(max_length=50)
    ffImg = models.ImageField(upload_to='blogItemPics')
    ffImgAltText = models.CharField(max_length=30)
    ffDesc = models.TextField()
    sfFlag = models.BooleanField(default=False)
    sfTitle1 = models.CharField(max_length=50)
    sfTitle2 = models.CharField(max_length=50)
    sfImg = models.ImageField(upload_to='blogItemPics')
    sfImgAltText = models.CharField(max_length=30)
    sfDesc = models.TextField()
    tfFlag = models.BooleanField(default=False)
    tfTitle1 = models.CharField(max_length=50)
    tfTitle2 = models.CharField(max_length=50)
    tfImg = models.ImageField(upload_to='blogItemPics')
    tfImgAltText = models.CharField(max_length=30)
    tfDesc = models.TextField()
    bottomHeadline = models.TextField()
    bottomText = models.TextField()


class ReviewProduct(models.Model):
    isFavorite = models.BooleanField(default=False)
    img = models.ImageField(upload_to='productImgs')
    imgAltText = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    sale = models.FloatField(default=0.00)
    isOffer = models.BooleanField(default=False)
    priceThrough = models.FloatField(default=0.00)
    label = models.CharField(max_length=30)
