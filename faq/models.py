from django.db import models


class LeftQuestion(models.Model):
    qId = models.CharField(max_length=30)
    qText = models.CharField(max_length=50)
    qAnswer = models.TextField()


class RightQuestion(models.Model):
    qId = models.CharField(max_length=30)
    qText = models.CharField(max_length=50)
    qAnswer = models.TextField()
