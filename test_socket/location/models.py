from django.db import models

# Create your models here.
class Location(models.Model):
    latitude = models.CharField(max_length=20,null=False,blank=False)
    longitude = models.CharField(max_length=20,null=False,blank=False)
    current_datetime = models.BigIntegerField(null=False)
    