from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Company_register(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    cname = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    pnumber = models.CharField(max_length=11)
    processed = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    slot = models.IntegerField(default=0)
    declined = models.BooleanField(default=False)
    user=models.IntegerField(null=True)

class Slot(models.Model):
    book=models.BooleanField(default=False)