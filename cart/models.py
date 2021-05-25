from django.db import models


class CartItem(models.Model):
    img = models.ImageField(upload_to='productImgs')
    imgAltText = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    label = models.CharField(max_length=30)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)
