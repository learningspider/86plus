from django.db import models

# Create your models here.
class memberCard(models.Model):
    openid = models.CharField(max_length=60)
    phonenumber = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    IDcard = models.CharField(max_length=18)
    
