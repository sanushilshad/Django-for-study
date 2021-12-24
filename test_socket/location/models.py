from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.binding.websockets import WebsocketBinding


# Create your models here.
class Location(models.Model):
    latitude = models.CharField(max_length=20,null=False,blank=False)
    longitude = models.CharField(max_length=20,null=False,blank=False)
    current_datetime = models.BigIntegerField(null=False)
    
    
class LocationBinding(WebsocketBinding):
    
    model = Location
    stream = "intval"
    fields = ["latitude", "longitude","current_datetime"]

    @classmethod
    def group_names(cls, instance):
        return ["intval-updates"]

    def has_permission(self, user, action, pk):
        return True
    