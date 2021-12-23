from django.http import HttpResponse
from channels.handler import AsgiHandler
import time

def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    message.reply_channel.send({
        "text": message.content['text'] + ' Kevin',
    })
        
