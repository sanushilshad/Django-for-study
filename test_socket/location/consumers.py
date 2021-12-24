from django.http import HttpResponse
from channels.handler import AsgiHandler
import time
import json
import urlparse 
# In consumers.py
from channels import Group
from channels.generic.websockets import WebsocketConsumer
from channels.generic.websockets import WebsocketDemultiplexer
from .models import LocationBinding

class MyConsumer(WebsocketConsumer):
    
    http_user = True
    strict_ordering = False

    def connection_groups(self, **kwargs):
        return ["intval-updates"]

    def connect(self, message, **kwargs):
        self.message.reply_channel.send({"accept": True})

    def receive(self, text=None, bytes=None, **kwargs):
        self.send(text=text, bytes=bytes)

    def disconnect(self, message, **kwargs):
        pass
    
    
    


class Demultiplexer(WebsocketDemultiplexer):

    consumers = {
        "intval": LocationBinding.consumer,
    }

    def connection_groups(self):
        return ["intval-updates"]
