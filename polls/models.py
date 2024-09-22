from django.db import models


# Create your models here.
class book(models.Model):
    title = models.CharField(max_length=128)
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=100)
