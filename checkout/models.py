from django.db import models


class Summary(models.Model):
    subTotal = models.FloatField(default=0.00)
    discount = models.FloatField(default=0.00)
    delivery = models.FloatField(default=0.00)
    total = models.FloatField(default=0.00)


class DeliveryAddress(models.Model):
    isSelected = models.BooleanField(default=False)
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    building = models.CharField(max_length=30)
    zipCode = models.IntegerField(default=0)


class DeliveryOption(models.Model):
    isSelected = models.BooleanField(default=False)
    img = models.ImageField(upload_to='deliveryCompanyLogos')
    imgTitle = models.CharField(max_length=30)
    imgAltText = models.CharField(max_length=30)
    desc = models.CharField(max_length=30)


class PaymentMethod(models.Model):
    isSelected = models.BooleanField(default=False)
    img = models.ImageField(upload_to='paymentCompanyLogos')
    imgTitle = models.CharField(max_length=30)
    imgAltText = models.CharField(max_length=30)
    desc = models.CharField(max_length=30)
