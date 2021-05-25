from django.db import models


class ContactInfo(models.Model):
    companyName = models.CharField(max_length=30)
    addressText1 = models.CharField(max_length=50)
    addressText2 = models.CharField(max_length=50)
    phoneNo = models.CharField(max_length=30)
    supportMail = models.EmailField()
    partnerMail = models.EmailField()
