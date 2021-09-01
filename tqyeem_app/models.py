from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    address = models.CharField(max_length=42)


class ApprovedSeller(models.Model):
    productId = models.IntegerField()
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=200)


